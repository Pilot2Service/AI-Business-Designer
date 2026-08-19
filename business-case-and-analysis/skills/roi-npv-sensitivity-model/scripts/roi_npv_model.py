#!/usr/bin/env python3
"""
roi_npv_model.py -- ROI / NPV / IRR / sensitivity calculator.

Computes NPV, IRR, payback period, and ROI from a series of incremental net
cash flows (already compared against a "do nothing" baseline, per the
roi-npv-sensitivity-model skill's Method step 1), then runs a one-at-a-time
sensitivity analysis on named variables and reports upside/downside
scenarios and the breakeven shift needed on the most sensitive variable.

No third-party dependencies (stdlib only): json, argparse, sys, math.

Usage:
  python3 roi_npv_model.py INPUT.json
  python3 roi_npv_model.py -            (read JSON from stdin)
  python3 roi_npv_model.py --example    (print a sample input and exit)

Input JSON shape:
{
  "discount_rate": 0.10,
  "net_cash_flows": [-100000, 20000, 45000, 45000, 45000],
  "sensitivity_variables": [
    {"name": "adoption_rate", "target": "benefits", "range_pct": 0.20},
    {"name": "unit_cost",     "target": "costs",    "range_pct": 0.20}
  ]
}

- "net_cash_flows": one entry per period (period 0, 1, 2, ...), already
  incremental vs. the do-nothing baseline. Negative = net cost that
  period, positive = net benefit.
- "sensitivity_variables": each varies ONE side of the cash flows
  (target "benefits" scales all positive entries, target "costs" scales
  the magnitude of all negative entries) by +/- range_pct, holding
  everything else constant, per the skill's Method step 4.

Output: a single JSON object on stdout with npv, irr, payback_period_years,
roi, sensitivity (tornado-ranked), scenarios (upside/downside), and
breakeven for the most sensitive variable.

Exit codes: 0 = success, 1 = invalid input, 2 = could not compute (e.g. IRR
has no sign change in the search range -- reported in the output with a
null value and a note, not a crash).
"""
import argparse
import json
import sys

EXAMPLE_INPUT = {
    "discount_rate": 0.10,
    "net_cash_flows": [-100000, 20000, 45000, 45000, 45000],
    "sensitivity_variables": [
        {"name": "adoption_rate", "target": "benefits", "range_pct": 0.20},
        {"name": "unit_cost", "target": "costs", "range_pct": 0.20},
        {"name": "benefit_timing_slip", "target": "benefits", "range_pct": 0.10},
    ],
}


def npv(rate, cash_flows):
    return sum(cf / ((1.0 + rate) ** t) for t, cf in enumerate(cash_flows))


def irr(cash_flows, lo=-0.99, hi=10.0, iterations=200, tol=1e-7):
    """Bisection search for the discount rate where NPV == 0.
    Returns None if NPV(lo) and NPV(hi) don't bracket a sign change."""
    f_lo = npv(lo, cash_flows)
    f_hi = npv(hi, cash_flows)
    if f_lo == 0:
        return lo
    if f_hi == 0:
        return hi
    if (f_lo > 0) == (f_hi > 0):
        return None
    for _ in range(iterations):
        mid = (lo + hi) / 2.0
        f_mid = npv(mid, cash_flows)
        if abs(f_mid) < tol:
            return mid
        if (f_mid > 0) == (f_lo > 0):
            lo, f_lo = mid, f_mid
        else:
            hi, f_hi = mid, f_mid
    return (lo + hi) / 2.0


def payback_period(cash_flows):
    """Simple (undiscounted) payback period in periods, fractional.
    Returns None if cumulative cash flow never turns non-negative."""
    cumulative = 0.0
    for t, cf in enumerate(cash_flows):
        prev_cumulative = cumulative
        cumulative += cf
        if cumulative >= 0 and t > 0 and prev_cumulative < 0:
            fraction = -prev_cumulative / cf if cf != 0 else 0.0
            return round((t - 1) + fraction, 3)
        if cumulative >= 0 and t == 0:
            return 0.0
    return None


def roi(cash_flows):
    total_cost = sum(-cf for cf in cash_flows if cf < 0)
    total_benefit = sum(cf for cf in cash_flows if cf > 0)
    if total_cost == 0:
        return None
    return round((total_benefit - total_cost) / total_cost, 4)


def scale_cash_flows(cash_flows, target, multiplier):
    """Scale the benefit (positive) or cost (negative) side of cash flows
    by `multiplier`, leaving the other side untouched."""
    out = []
    for cf in cash_flows:
        if target == "benefits" and cf > 0:
            out.append(cf * multiplier)
        elif target == "costs" and cf < 0:
            out.append(cf * multiplier)
        else:
            out.append(cf)
    return out


def run(data):
    errors = []
    discount_rate = data.get("discount_rate")
    cash_flows = data.get("net_cash_flows")
    if discount_rate is None or not isinstance(discount_rate, (int, float)):
        errors.append("discount_rate must be a number (e.g. 0.10 for 10%).")
    if not cash_flows or not isinstance(cash_flows, list) or len(cash_flows) < 2:
        errors.append(
            "net_cash_flows must be a list of at least 2 numbers "
            "(period 0 = initial investment, period 1+ = subsequent net flows)."
        )
    if errors:
        return None, errors

    base_npv = round(npv(discount_rate, cash_flows), 2)
    base_irr = irr(cash_flows)
    result = {
        "npv": base_npv,
        "irr": round(base_irr, 4) if base_irr is not None else None,
        "irr_note": None if base_irr is not None else (
            "No sign change found in the -99%..1000% search range -- "
            "this cash-flow series may never break even, or breaks even "
            "at an implausible rate. Check the inputs."
        ),
        "payback_period_periods": payback_period(cash_flows),
        "roi": roi(cash_flows),
        "sensitivity": [],
        "scenarios": {},
        "breakeven": None,
    }

    sens_vars = data.get("sensitivity_variables", [])
    tornado = []
    for var in sens_vars:
        name = var.get("name", "unnamed")
        target = var.get("target")
        range_pct = var.get("range_pct", 0.20)
        if target not in ("benefits", "costs"):
            result["sensitivity"].append(
                {"name": name, "error": "target must be 'benefits' or 'costs'"}
            )
            continue
        up_flows = scale_cash_flows(cash_flows, target, 1 + range_pct)
        down_flows = scale_cash_flows(cash_flows, target, 1 - range_pct)
        up_npv = round(npv(discount_rate, up_flows), 2)
        down_npv = round(npv(discount_rate, down_flows), 2)
        swing = abs(up_npv - down_npv)
        tornado.append({
            "name": name,
            "target": target,
            "range_pct": range_pct,
            "npv_at_plus_range": up_npv,
            "npv_at_minus_range": down_npv,
            "npv_swing": round(swing, 2),
        })

    tornado.sort(key=lambda x: x["npv_swing"], reverse=True)
    result["sensitivity"] = tornado

    # Upside / downside scenario: apply +range to benefits and -range to
    # costs simultaneously (upside), and the reverse (downside), using each
    # variable's own range_pct.
    upside_flows = list(cash_flows)
    downside_flows = list(cash_flows)
    for var in sens_vars:
        target = var.get("target")
        range_pct = var.get("range_pct", 0.20)
        if target == "benefits":
            upside_flows = scale_cash_flows(upside_flows, "benefits", 1 + range_pct)
            downside_flows = scale_cash_flows(downside_flows, "benefits", 1 - range_pct)
        elif target == "costs":
            upside_flows = scale_cash_flows(upside_flows, "costs", 1 - range_pct)
            downside_flows = scale_cash_flows(downside_flows, "costs", 1 + range_pct)
    result["scenarios"] = {
        "upside_npv": round(npv(discount_rate, upside_flows), 2),
        "downside_npv": round(npv(discount_rate, downside_flows), 2),
        "base_npv": base_npv,
    }

    # Breakeven: for the most sensitive variable, linearly interpolate the
    # % change from base needed to bring NPV to 0.
    if tornado:
        top = tornado[0]
        pts = [
            (-top["range_pct"], top["npv_at_minus_range"]),
            (0.0, base_npv),
            (top["range_pct"], top["npv_at_plus_range"]),
        ]
        pts.sort(key=lambda p: p[0])
        breakeven_pct = None
        for (x0, y0), (x1, y1) in zip(pts, pts[1:]):
            if (y0 <= 0 <= y1) or (y1 <= 0 <= y0):
                if y1 != y0:
                    breakeven_pct = x0 + (0 - y0) * (x1 - x0) / (y1 - y0)
                break
        result["breakeven"] = {
            "variable": top["name"],
            "target": top["target"],
            "pct_change_from_base_for_npv_zero": (
                round(breakeven_pct * 100, 2) if breakeven_pct is not None else None
            ),
            "note": (
                "Linear interpolation between the computed -range/base/+range "
                "points, not an exact re-solve -- treat as an estimate."
                if breakeven_pct is not None
                else "NPV does not cross zero within the tested +/-range for "
                     "this variable; widen range_pct to find the breakeven."
            ),
        }

    return result, []


def main():
    parser = argparse.ArgumentParser(
        description="Calculate ROI, NPV, IRR, payback, and sensitivity from net cash flows.",
        epilog="Examples:\n"
               "  python3 roi_npv_model.py input.json\n"
               "  echo '{...}' | python3 roi_npv_model.py -\n"
               "  python3 roi_npv_model.py --example",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("input", nargs="?", help="Path to input JSON file, or '-' for stdin.")
    parser.add_argument("--example", action="store_true", help="Print a sample input JSON and exit.")
    args = parser.parse_args()

    if args.example:
        print(json.dumps(EXAMPLE_INPUT, indent=2))
        return 0

    if not args.input:
        parser.print_usage(sys.stderr)
        print("Error: provide an input file path, '-' for stdin, or --example.", file=sys.stderr)
        return 1

    try:
        if args.input == "-":
            data = json.load(sys.stdin)
        else:
            with open(args.input, "r", encoding="utf-8") as f:
                data = json.load(f)
    except (json.JSONDecodeError, OSError) as e:
        print(f"Error: could not read/parse input: {e}", file=sys.stderr)
        return 1

    result, errors = run(data)
    if errors:
        for e in errors:
            print(f"Error: {e}", file=sys.stderr)
        return 1

    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
