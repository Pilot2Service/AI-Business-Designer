#!/usr/bin/env python3
"""
value_curve.py -- Strategy Canvas / Value Curve chart generator, per the
strategy-canvas-and-value-curve skill's Method (Kim & Mauborgne's Blue
Ocean Strategy Value Curve, and the owner's 360 Comparison Factors tool).

No third-party dependencies (stdlib only): json, argparse, sys. Draws an
SVG line chart by hand (no plotting library needed) and prints a JSON
analysis to stdout that flags the "as-is curve" (factors where players
cluster tightly -- Method step 5) vs. factors with real spread (existing
differentiation).

Usage:
  python3 value_curve.py INPUT.json --output curve.svg
  python3 value_curve.py -  --output curve.svg      (read JSON from stdin)
  python3 value_curve.py --example                  (print a sample input and exit)

Input JSON shape:
{
  "factors": ["Price", "Service speed", "Customization", "Brand", "Range"],
  "scale_max": 2,
  "players": [
    {"name": "Us", "scores": {"Price": 1, "Service speed": 2, "Customization": 2, "Brand": 0, "Range": 1}},
    {"name": "Competitor A", "scores": {"Price": 2, "Service speed": 1, "Customization": 0, "Brand": 1, "Range": 1}}
  ]
}

- "scale_max" defaults to 2 (the 360 model's 0-2 scale: 0 = weak/not
  offered, 1 = industry mid-level, 2 = strong/distinctive) but can be
  overridden if a different scale is used.
- Every factor listed must have a score for every player; missing scores
  are reported as an error rather than silently defaulted, per the skill's
  "don't invent competitor data" rule -- if a score is genuinely unknown,
  mark it in the input as null and it will be flagged, not guessed.

Output: an SVG file written to --output (default value_curve.svg in the
current directory) plus a JSON analysis on stdout: per-factor min/max/
spread across players, factors flagged as "as-is curve" candidates (low
spread = everyone competes the same way) vs. "differentiation exists"
(high spread), sorted by spread ascending so the as-is candidates surface
first (these are Method step 6's Eliminate/Reduce/Raise candidates).

Exit codes: 0 = success, 1 = invalid input.
"""
import argparse
import json
import sys

EXAMPLE_INPUT = {
    "factors": ["Price", "Service speed", "Customization", "Brand", "Range"],
    "scale_max": 2,
    "players": [
        {"name": "Us", "scores": {"Price": 1, "Service speed": 2, "Customization": 2, "Brand": 0, "Range": 1}},
        {"name": "Competitor A", "scores": {"Price": 2, "Service speed": 1, "Customization": 0, "Brand": 1, "Range": 1}},
        {"name": "Competitor B", "scores": {"Price": 1, "Service speed": 1, "Customization": 0, "Brand": 1, "Range": 1}},
        {"name": "Do nothing", "scores": {"Price": 2, "Service speed": 0, "Customization": 0, "Brand": 0, "Range": 0}},
    ],
}

PALETTE = [
    "#2563eb", "#dc2626", "#059669", "#d97706", "#7c3aed",
    "#0891b2", "#be185d", "#4d7c0f", "#b45309", "#4338ca",
]


def validate(data):
    errors = []
    factors = data.get("factors")
    players = data.get("players")
    if not factors or not isinstance(factors, list):
        errors.append("factors must be a non-empty list of factor names.")
    if not players or not isinstance(players, list) or len(players) < 1:
        errors.append("players must be a non-empty list of {name, scores} objects.")
    if errors:
        return errors
    for p in players:
        name = p.get("name", "<unnamed player>")
        scores = p.get("scores", {})
        for f in factors:
            if f not in scores or scores[f] is None:
                errors.append(f"Player '{name}' is missing a score for factor '{f}'. "
                               f"Use a real score or mark it explicitly as unknown -- "
                               f"don't leave it out silently.")
    return errors


def analyze(data):
    factors = data["factors"]
    players = data["players"]
    analysis = []
    for f in factors:
        scores = [p["scores"][f] for p in players]
        lo, hi = min(scores), max(scores)
        spread = hi - lo
        analysis.append({
            "factor": f,
            "min": lo,
            "max": hi,
            "spread": spread,
            "avg": round(sum(scores) / len(scores), 2),
            "as_is_curve_candidate": spread <= 1,
        })
    analysis.sort(key=lambda x: x["spread"])
    return analysis


def render_svg(data, path):
    factors = data["factors"]
    players = data["players"]
    scale_max = data.get("scale_max", 2)

    width, height = 900, 480
    margin_left, margin_right = 140, 40
    margin_top, margin_bottom = 40, 100
    plot_w = width - margin_left - margin_right
    plot_h = height - margin_top - margin_bottom

    n = len(factors)
    x_step = plot_w / (n - 1) if n > 1 else 0

    def x_for(i):
        return margin_left + i * x_step

    def y_for(score):
        frac = score / scale_max if scale_max else 0
        return margin_top + plot_h - frac * plot_h

    svg = []
    svg.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
               f'viewBox="0 0 {width} {height}" font-family="Helvetica,Arial,sans-serif">')
    svg.append(f'<rect x="0" y="0" width="{width}" height="{height}" fill="#ffffff"/>')

    # Y gridlines + labels (0..scale_max)
    steps = scale_max if scale_max <= 6 else 6
    for i in range(int(steps) + 1):
        val = scale_max * i / steps
        y = y_for(val)
        svg.append(f'<line x1="{margin_left}" y1="{y:.1f}" x2="{width - margin_right}" y2="{y:.1f}" '
                   f'stroke="#e5e7eb" stroke-width="1"/>')
        svg.append(f'<text x="{margin_left - 10}" y="{y+4:.1f}" text-anchor="end" '
                   f'font-size="11" fill="#6b7280">{val:g}</text>')

    # X axis labels (rotated factor names)
    for i, f in enumerate(factors):
        x = x_for(i)
        svg.append(f'<line x1="{x:.1f}" y1="{margin_top}" x2="{x:.1f}" y2="{margin_top + plot_h}" '
                   f'stroke="#f3f4f6" stroke-width="1"/>')
        svg.append(f'<text x="{x:.1f}" y="{margin_top + plot_h + 20}" text-anchor="end" '
                   f'font-size="12" fill="#111827" transform="rotate(-30 {x:.1f} {margin_top + plot_h + 20})">'
                   f'{f}</text>')

    # Player curves
    legend_y = height - 45
    legend_x = margin_left
    for pi, p in enumerate(players):
        color = PALETTE[pi % len(PALETTE)]
        pts = " ".join(f"{x_for(i):.1f},{y_for(p['scores'][f]):.1f}" for i, f in enumerate(factors))
        svg.append(f'<polyline points="{pts}" fill="none" stroke="{color}" stroke-width="2.5"/>')
        for i, f in enumerate(factors):
            svg.append(f'<circle cx="{x_for(i):.1f}" cy="{y_for(p["scores"][f]):.1f}" r="4" fill="{color}"/>')
        # legend entry
        lx = legend_x + (pi % 3) * 260
        ly = legend_y + (pi // 3) * 20
        svg.append(f'<line x1="{lx}" y1="{ly}" x2="{lx+20}" y2="{ly}" stroke="{color}" stroke-width="3"/>')
        svg.append(f'<text x="{lx+26}" y="{ly+4}" font-size="12" fill="#111827">{p["name"]}</text>')

    svg.append(f'<line x1="{margin_left}" y1="{margin_top + plot_h}" x2="{width - margin_right}" '
               f'y2="{margin_top + plot_h}" stroke="#111827" stroke-width="1.5"/>')
    svg.append(f'<line x1="{margin_left}" y1="{margin_top}" x2="{margin_left}" '
               f'y2="{margin_top + plot_h}" stroke="#111827" stroke-width="1.5"/>')
    svg.append('</svg>')

    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(svg))


def main():
    parser = argparse.ArgumentParser(
        description="Generate a Strategy Canvas / Value Curve SVG chart plus an as-is-curve analysis.",
        epilog="Examples:\n"
               "  python3 value_curve.py input.json --output curve.svg\n"
               "  echo '{...}' | python3 value_curve.py - --output curve.svg\n"
               "  python3 value_curve.py --example",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("input", nargs="?", help="Path to input JSON file, or '-' for stdin.")
    parser.add_argument("--output", default="value_curve.svg", help="SVG output path (default: value_curve.svg).")
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

    errors = validate(data)
    if errors:
        for e in errors:
            print(f"Error: {e}", file=sys.stderr)
        return 1

    render_svg(data, args.output)
    analysis = analyze(data)
    print(json.dumps({
        "svg_written_to": args.output,
        "factor_analysis": analysis,
        "as_is_curve_candidates": [a["factor"] for a in analysis if a["as_is_curve_candidate"]],
        "note": "as_is_curve_candidates are low-spread factors (Method step 5) -- run the ERRC "
                "grid (step 6) on these first: they're where the industry silently agrees, and "
                "usually the highest-leverage place to Eliminate or Reduce.",
    }, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
