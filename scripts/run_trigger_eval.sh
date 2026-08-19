#!/usr/bin/env bash
# run_trigger_eval.sh -- measure a skill's description trigger rate, per
# agentskills.io's "Optimizing skill descriptions" methodology
# (https://agentskills.io/skill-creation/optimizing-descriptions).
#
# For each query in evals/<skill-id>/eval_queries.json, runs Claude Code
# RUNS times with the plugin installed, checks whether the skill's SKILL.md
# was actually loaded (a Skill tool call naming this skill), and computes a
# trigger rate. A should-trigger query passes if its rate is >= THRESHOLD;
# a should-not-trigger query passes if its rate is < THRESHOLD.
#
# Requires: Claude Code CLI (`claude`) installed locally with this
# marketplace's plugin(s) already installed (see README.md > Install it),
# and `jq`. Not runnable inside a sandboxed session with no shell access to
# a real Claude Code install -- this is meant to be run by the repo owner
# on their own machine.
#
# Usage:
#   scripts/run_trigger_eval.sh <skill-id> [runs] [threshold]
#   scripts/run_trigger_eval.sh roi-npv-sensitivity-model 3 0.5
#
# Output: a JSON array on stdout, one object per query, with the measured
# trigger_rate and a pass/fail verdict. Also prints a pass/fail summary to
# stderr.

set -euo pipefail

SKILL_ID="${1:?Usage: $0 <skill-id> [runs] [threshold]}"
RUNS="${2:-3}"
THRESHOLD="${3:-0.5}"

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
QUERIES_FILE="$REPO_ROOT/evals/$SKILL_ID/eval_queries.json"

if [ ! -f "$QUERIES_FILE" ]; then
  echo "Error: no eval file at $QUERIES_FILE" >&2
  echo "(Query sets exist for the 24 skills marked 'validated' in skills_index.json as of 2026-08-19 -- add one for other skills following the same {\"query\":..., \"should_trigger\": true|false} x 12 shape.)" >&2
  exit 1
fi

if ! command -v claude >/dev/null 2>&1; then
  echo "Error: 'claude' (Claude Code CLI) not found on PATH. This script runs real queries against your local Claude Code install with this repo's plugins installed -- see README.md > Install it." >&2
  exit 1
fi

if ! command -v jq >/dev/null 2>&1; then
  echo "Error: 'jq' not found on PATH." >&2
  exit 1
fi

check_triggered() {
  local query="$1"
  claude -p "$query" --output-format json 2>/dev/null \
    | jq -e --arg skill "$SKILL_ID" \
      'any(.messages[].content[]?; .type == "tool_use" and .name == "Skill" and .input.skill == $skill)' \
      > /dev/null 2>&1
}

count=$(jq length "$QUERIES_FILE")
pass=0
fail=0
results="[]"

for i in $(seq 0 $((count - 1))); do
  query=$(jq -r ".[$i].query" "$QUERIES_FILE")
  should_trigger=$(jq -r ".[$i].should_trigger" "$QUERIES_FILE")
  triggers=0

  for _ in $(seq 1 "$RUNS"); do
    check_triggered "$query" && triggers=$((triggers + 1))
  done

  rate=$(awk "BEGIN { printf \"%.3f\", $triggers / $RUNS }")
  verdict="fail"
  if [ "$should_trigger" = "true" ]; then
    awk -v r="$rate" -v t="$THRESHOLD" 'BEGIN { exit !(r >= t) }' && verdict="pass"
  else
    awk -v r="$rate" -v t="$THRESHOLD" 'BEGIN { exit !(r < t) }' && verdict="pass"
  fi
  [ "$verdict" = "pass" ] && pass=$((pass + 1)) || fail=$((fail + 1))

  echo "[$SKILL_ID] ($((i+1))/$count) should_trigger=$should_trigger rate=$rate -> $verdict" >&2

  entry=$(jq -n \
    --arg query "$query" \
    --argjson should_trigger "$should_trigger" \
    --argjson triggers "$triggers" \
    --argjson runs "$RUNS" \
    --arg rate "$rate" \
    --arg verdict "$verdict" \
    '{query: $query, should_trigger: $should_trigger, triggers: $triggers, runs: $runs, trigger_rate: ($rate | tonumber), verdict: $verdict}')
  results=$(echo "$results" | jq --argjson e "$entry" '. + [$e]')
done

echo "=== $SKILL_ID: $pass/$count passed (threshold $THRESHOLD, $RUNS runs/query) ===" >&2
echo "$results"
