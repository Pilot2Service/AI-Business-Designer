#!/usr/bin/env python3
"""
market_sizing.py -- TAM / SAM / SOM calculator with a top-down vs.
bottom-up cross-check, per the market-sizing-tam-sam-som skill's Method.

No third-party dependencies (stdlib only): json, argparse, sys.

Usage:
  python3 market_sizing.py INPUT.json
  python3 market_sizing.py -            (read JSON from stdin)
  python3 market_sizing.py --example    (print a sample input and exit)

Input JSON shape:
{
  "top_down": {"market_figure": 5000000000, "source": "Industry report XYZ 2026"},
  "bottom_up": {"price_per_customer": 1200, "total_potential_customers": 3000000,
                "source": "Internal estimate"},
  "sam_filters": [
    {"name": "geography: EU only", "factor": 0.35},
    {"name": "segment: SMB only", "factor": 0.5}
  ],
  "som_constraints": [
    {"name": "sales capacity, year 1-3", "factor": 0.08}
  ],
  "som_time_horizon": "3 years",
  "divergence_warning_ratio": 3.0
}

- "top_down" and "bottom_up" are each optional, but at least one is
  required; supplying both lets the script cross-check them (Method step 1
  says running both is "the single most effective way to catch an inflated
  or nonsensical TAM").
- "sam_filters" / "som_constraints": each is a named, explicit narrowing
  factor (0 < factor <= 1) applied multiplicatively -- Method steps 2-3
  require every narrowing filter to be named, not folded into one opaque
  percentage.

Output: TAM (top-down, bottom-up, and their ratio with a divergence flag),
SAM and SOM computed from EACH available TAM basis (so you see a range,
not one arbitrarily chosen number), and the filter breakdown.

Exit codes: 0 = success, 1 = invalid input.
"""
import argparse
import json
import sys

EXAMPLE_INPUT = {
    "top_down": {"market_figure": 5000000000, "source": "Industry report XYZ 2026"},
    "bottom_up": {
        "price_per_customer": 1200,
        "total_potential_customers": 3000000,
        "source": "Internal estimate from customer interviews",
    },
    "sam_filters": [
        {"name": "geography: EU only", "factor": 0.35},
        {"name": "segment: SMB only", "factor": 0.5},
    ],
    "som_constraints": [
        {"name": "sales capacity, year 1-3", "factor": 0.08},
    ],
    "som_time_horizon": "3 years",
    "divergence_warning_ratio": 3.0,
}


def apply_filters(base, filters):
    value = base
    chain = []
    for f in filters:
        name = f.get("name", "unnamed filter")
        factor = f.get("factor")
        if factor is None or not (0 < factor <= 1):
            return None, chain, f"Filter '{name}' has an invalid factor (must be 0 < factor <= 1)."
        value *= factor
        chain.append({"name": name, "factor": factor, "value_after": round(value, 2)})
    return value, chain, None


def run(data):
    errors = []
    top_down = data.get("top_down")
    bottom_up = data.get("bottom_up")

    tam_topdown = None
    tam_bottomup = None

    if top_down:
        mf = top_down.get("market_figure")
        if not isinstance(mf, (int, float)) or mf <= 0:
            errors.append("top_down.market_figure must be a positive number.")
        else:
            tam_topdown = mf

    if bottom_up:
        price = bottom_up.get("price_per_customer")
        customers = bottom_up.get("total_potential_customers")
        if not isinstance(price, (int, float)) or price <= 0:
            errors.append("bottom_up.price_per_customer must be a positive number.")
        elif not isinstance(customers, (int, float)) or customers <= 0:
            errors.append("bottom_up.total_potential_customers must be a positive number.")
        else:
            tam_bottomup = price * customers

    if tam_topdown is None and tam_bottomup is None:
        errors.append("Provide at least one of top_down or bottom_up (both is strongly preferred).")

    if errors:
        return None, errors

    result = {"tam": {}, "sam": {}, "som": {}}

    result["tam"]["top_down"] = {
        "value": round(tam_topdown, 2) if tam_topdown is not None else None,
        "source": (top_down or {}).get("source"),
    }
    result["tam"]["bottom_up"] = {
        "value": round(tam_bottomup, 2) if tam_bottomup is not None else None,
        "source": (bottom_up or {}).get("source"),
        "formula": "price_per_customer * total_potential_customers" if tam_bottomup else None,
    }

    if tam_topdown is not None and tam_bottomup is not None:
        hi, lo = max(tam_topdown, tam_bottomup), min(tam_topdown, tam_bottomup)
        ratio = round(hi / lo, 2) if lo > 0 else None
        warn_ratio = data.get("divergence_warning_ratio", 3.0)
        result["tam"]["cross_check"] = {
            "ratio": ratio,
            "diverges_significantly": bool(ratio and ratio >= warn_ratio),
            "note": (
                f"Top-down and bottom-up TAM differ by {ratio}x. Method step 1 flags this as "
                "the primary signal of an inflated or nonsensical TAM -- reconcile the two "
                "estimates (check the bottom-up customer count and price, and the top-down "
                "market definition) before using either number in a business case."
                if ratio and ratio >= warn_ratio
                else f"Top-down and bottom-up TAM are within {ratio}x of each other -- a "
                     "reasonable cross-check pass."
            ),
        }

    sam_filters = data.get("sam_filters", [])
    som_constraints = data.get("som_constraints", [])

    for basis_name, tam_value in (("top_down", tam_topdown), ("bottom_up", tam_bottomup)):
        if tam_value is None:
            continue
        sam_value, sam_chain, err = apply_filters(tam_value, sam_filters)
        if err:
            errors.append(err)
            continue
        result["sam"][basis_name] = {
            "value": round(sam_value, 2),
            "filters_applied": sam_chain,
        }
        som_value, som_chain, err2 = apply_filters(sam_value, som_constraints)
        if err2:
            errors.append(err2)
            continue
        result["som"][basis_name] = {
            "value": round(som_value, 2),
            "constraints_applied": som_chain,
            "time_horizon": data.get("som_time_horizon", "not specified -- add one, per Method step 3"),
        }

    if errors:
        return result, errors

    return result, []


def main():
    parser = argparse.ArgumentParser(
        description="Calculate TAM/SAM/SOM with a top-down vs. bottom-up cross-check.",
        epilog="Examples:\n"
               "  python3 market_sizing.py input.json\n"
               "  echo '{...}' | python3 market_sizing.py -\n"
               "  python3 market_sizing.py --example",
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
    if errors and result is None:
        for e in errors:
            print(f"Error: {e}", file=sys.stderr)
        return 1

    if errors:
        for e in errors:
            print(f"Warning: {e}", file=sys.stderr)

    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
