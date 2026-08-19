#!/usr/bin/env python3
"""
validate.py — structural + frontmatter gate for the AI Business Designer skills repo.

Run before every commit (and wired into CI). Exit code 1 on any failure — this must
be green before push.

Also drift-checks README.md and docs/index.html against skills_index.json (see
check_docs_sync): if either doc's stated pack/skill/agent counts, or a pack's
stated skill count in its table row, stops matching the index, this fails
instead of silently going stale.

Usage:
    python3 scripts/validate.py
"""
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

NON_PACK_DIRS = {
    "meta", "templates", "playbooks", "scripts", "specialisation-packs",
    ".claude-plugin", ".git", ".github",
}

REQUIRED_PACK_FILES = ["README.md", "CLAUDE.md", os.path.join(".claude-plugin", "plugin.json")]

errors = []
warnings = []
agent_count = 0


def parse_frontmatter_keys(text, path):
    m = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
    if not m:
        errors.append(f"{path}: no YAML frontmatter block found")
        return {}
    keys = []
    for line in m.group(1).split("\n"):
        kv = re.match(r"^([A-Za-z_][A-Za-z0-9_]*):", line)
        if kv:
            keys.append(kv.group(1))
    return keys


# Regression guard: substrings that flag a low-effort, boilerplate description.
# Added 2026-08-19 after an agentskills.io audit found 24 skills using a generic
# "Use when you need <pack>-level support for a comparable task" tail that named
# the pack instead of the skill's actual method and trigger situation — the exact
# antipattern agentskills.io's own spec warns against ("Poor example: Helps with
# PDFs."). This list is deliberately narrow (known-bad phrases only) rather than a
# broad heuristic, to avoid false positives on legitimately concise descriptions.
BANNED_DESCRIPTION_PATTERNS = [
    "level support for a comparable task",
    "helps with",
]


def _extract_description(text):
    m = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
    if not m:
        return None
    dm = re.search(r'^description:\s*"?(.*?)"?\s*$', m.group(1), re.MULTILINE)
    return dm.group(1) if dm else None


def _check_skill_frontmatter(name, skill_id, skill_md):
    if not os.path.exists(skill_md):
        errors.append(f"pack '{name}': {skill_id}/ has no SKILL.md")
        return
    with open(skill_md, encoding="utf-8") as f:
        text = f.read()
    keys = parse_frontmatter_keys(text, skill_md)
    extra = [k for k in keys if k not in ("name", "description")]
    missing = [k for k in ("name", "description") if k not in keys]
    if extra:
        errors.append(f"{skill_md}: forbidden frontmatter keys {extra} (only name+description allowed)")
    if missing:
        errors.append(f"{skill_md}: missing required frontmatter keys {missing}")
        return
    description = _extract_description(text)
    if description:
        desc_lower = description.lower()
        for pattern in BANNED_DESCRIPTION_PATTERNS:
            if pattern in desc_lower:
                errors.append(
                    f"{skill_md}: description contains a generic/boilerplate phrase "
                    f"('{pattern}') — rewrite to describe what the skill does and the "
                    f"user's actual trigger situation (see agentskills.io's "
                    f"description-optimization guide), not a pack-name filler."
                )


AGENT_ALLOWED_KEYS = ("name", "description", "tools", "model")
AGENT_REQUIRED_KEYS = ("name", "description")


def _check_agent_frontmatter(pack_name, agent_file):
    """Agents (<pack>/agents/<agent-id>.md) are delegatable, read-only subagents —
    a different mechanism from skills, so a different (slightly wider) frontmatter
    contract applies: name + description required, tools/model optional, nothing
    else."""
    agent_id = os.path.splitext(os.path.basename(agent_file))[0]
    with open(agent_file, encoding="utf-8") as f:
        text = f.read()
    keys = parse_frontmatter_keys(text, agent_file)
    extra = [k for k in keys if k not in AGENT_ALLOWED_KEYS]
    missing = [k for k in AGENT_REQUIRED_KEYS if k not in keys]
    if extra:
        errors.append(f"{agent_file}: forbidden frontmatter keys {extra} (allowed: {list(AGENT_ALLOWED_KEYS)})")
    if missing:
        errors.append(f"{agent_file}: missing required frontmatter keys {missing}")
    m = re.search(r"^name:\s*(.+)$", text, re.MULTILINE)
    if m and m.group(1).strip() != agent_id:
        errors.append(f"{agent_file}: frontmatter name '{m.group(1).strip()}' != filename '{agent_id}'")
    if "tools" not in keys:
        warnings.append(f"{agent_file}: no 'tools' field — agent will inherit full tool access, prefer an explicit read-only list")


def check_agents_in(pack_id, pack_dir):
    agents_dir = os.path.join(pack_dir, "agents")
    if not os.path.isdir(agents_dir):
        return 0
    count = 0
    for fname in sorted(os.listdir(agents_dir)):
        if not fname.endswith(".md"):
            continue
        _check_agent_frontmatter(pack_id, os.path.join(agents_dir, fname))
        count += 1
    return count


def check_packs():
    global agent_count
    packs = []
    for name in sorted(os.listdir(ROOT)):
        full = os.path.join(ROOT, name)
        if not os.path.isdir(full) or name in NON_PACK_DIRS or name.startswith("."):
            continue
        if not os.path.exists(os.path.join(full, ".claude-plugin", "plugin.json")):
            continue
        packs.append(name)
        for req in REQUIRED_PACK_FILES:
            if not os.path.exists(os.path.join(full, req)):
                errors.append(f"pack '{name}': missing required file {req}")
        if re.match(r"^\d", name):
            errors.append(f"pack '{name}': numeric prefix not allowed (see CONTRIBUTING.md)")

        agent_count += check_agents_in(name, full)

        skills_dir = os.path.join(full, "skills")
        if not os.path.isdir(skills_dir):
            warnings.append(f"pack '{name}': no skills/ directory yet")
            continue
        for skill_id in sorted(os.listdir(skills_dir)):
            if not os.path.isdir(os.path.join(skills_dir, skill_id)):
                continue  # ignore stray files (e.g. macOS .DS_Store) that aren't skill folders
            _check_skill_frontmatter(name, skill_id, os.path.join(skills_dir, skill_id, "SKILL.md"))
    return packs


def check_specialisation_pack_skills():
    """Specialisation packs (specialisation-packs/*/) don't have plugin.json and
    aren't installable plugins in their own right, but once they have a non-empty
    skills/ directory, the same frontmatter contract applies, and README.md +
    CLAUDE.md become required (mirrors REQUIRED_PACK_FILES minus plugin.json)."""
    global agent_count
    base = os.path.join(ROOT, "specialisation-packs")
    if not os.path.isdir(base):
        return
    for name in sorted(os.listdir(base)):
        full = os.path.join(base, name)
        if not os.path.isdir(full) or name.startswith("."):
            continue
        skills_dir = os.path.join(full, "skills")
        has_skills = os.path.isdir(skills_dir) and any(
            os.path.exists(os.path.join(skills_dir, s, "SKILL.md")) for s in os.listdir(skills_dir)
        )
        if not has_skills:
            continue  # empty/placeholder specialisation pack — nothing to validate yet
        pack_id = f"specialisation-packs/{name}"
        if not os.path.exists(os.path.join(full, "README.md")):
            errors.append(f"pack '{pack_id}': missing required file README.md")
        if not os.path.exists(os.path.join(full, "CLAUDE.md")):
            errors.append(f"pack '{pack_id}': missing required file CLAUDE.md (required once skills/ is populated)")
        agent_count += check_agents_in(pack_id, full)
        for skill_id in sorted(os.listdir(skills_dir)):
            if not os.path.isdir(os.path.join(skills_dir, skill_id)):
                continue  # ignore stray files (e.g. macOS .DS_Store) that aren't skill folders
            _check_skill_frontmatter(pack_id, skill_id, os.path.join(skills_dir, skill_id, "SKILL.md"))


def check_marketplace(packs):
    mp_path = os.path.join(ROOT, ".claude-plugin", "marketplace.json")
    if not os.path.exists(mp_path):
        errors.append("missing .claude-plugin/marketplace.json")
        return
    with open(mp_path, encoding="utf-8") as f:
        try:
            mp = json.load(f)
        except json.JSONDecodeError as e:
            errors.append(f"marketplace.json: invalid JSON — {e}")
            return
    if "$schema" not in mp:
        warnings.append("marketplace.json: no $schema field")
    listed_sources = set()
    for p in mp.get("plugins", []):
        src = p.get("source", "").lstrip("./")
        listed_sources.add(src.split("/")[0])
        if "displayName" not in p:
            warnings.append(f"marketplace.json: plugin '{p.get('name')}' has no displayName")
    for pack in packs:
        if pack not in listed_sources:
            errors.append(f"pack '{pack}' exists on disk but is not listed in marketplace.json")


def check_skills_index():
    idx_path = os.path.join(ROOT, "skills_index.json")
    if not os.path.exists(idx_path):
        errors.append("missing skills_index.json")
        return
    with open(idx_path, encoding="utf-8") as f:
        try:
            idx = json.load(f)
        except json.JSONDecodeError as e:
            errors.append(f"skills_index.json: invalid JSON — {e}")
            return
    for s in idx.get("skills", []):
        p = os.path.join(ROOT, s["path"])
        if not os.path.exists(p):
            errors.append(f"skills_index.json: entry '{s['id']}' points to missing file {s['path']}")

    # orphan check: every SKILL.md on disk should be represented in the index
    indexed_ids = {s["id"] for s in idx.get("skills", [])}

    def check_orphans_in(skills_dir):
        if not os.path.isdir(skills_dir):
            return
        for skill_id in os.listdir(skills_dir):
            if os.path.exists(os.path.join(skills_dir, skill_id, "SKILL.md")) and skill_id not in indexed_ids:
                errors.append(f"skill '{skill_id}' on disk but missing from skills_index.json — run scripts/generate_index.py")

    for name in sorted(os.listdir(ROOT)):
        full = os.path.join(ROOT, name)
        if not os.path.isdir(full) or name in NON_PACK_DIRS or name.startswith("."):
            continue
        check_orphans_in(os.path.join(full, "skills"))

    spec_base = os.path.join(ROOT, "specialisation-packs")
    if os.path.isdir(spec_base):
        for name in sorted(os.listdir(spec_base)):
            check_orphans_in(os.path.join(spec_base, name, "skills"))

    # same orphan check for agents/*.md
    indexed_agent_ids = {a["id"] for a in idx.get("agents", [])}

    def check_agent_orphans_in(agents_dir):
        if not os.path.isdir(agents_dir):
            return
        for fname in os.listdir(agents_dir):
            if fname.endswith(".md") and fname[:-3] not in indexed_agent_ids:
                errors.append(f"agent '{fname[:-3]}' on disk but missing from skills_index.json — run scripts/generate_index.py")

    for name in sorted(os.listdir(ROOT)):
        full = os.path.join(ROOT, name)
        if not os.path.isdir(full) or name in NON_PACK_DIRS or name.startswith("."):
            continue
        check_agent_orphans_in(os.path.join(full, "agents"))

    if os.path.isdir(spec_base):
        for name in sorted(os.listdir(spec_base)):
            check_agent_orphans_in(os.path.join(spec_base, name, "agents"))


def _pack_skill_counts(idx):
    """Ground truth: how many skills each pack actually has, keyed by folder
    name (the same slug used in README.md's `dir/README.md` links and
    docs/index.html's `.../blob/main/dir/README.md` hrefs)."""
    skills = idx.get("skills", [])
    core = {}
    for p in idx.get("packs", []):
        core[p["dir"]] = sum(1 for s in skills if s.get("pack") == p["name"])
    spec = {}
    for sp in idx.get("specialisation_packs", []):
        pack_key = f"specialisation-packs/{sp['dir']}"
        spec[sp["dir"]] = sum(1 for s in skills if s.get("pack") == pack_key)
    return core, spec


def _index_truth(idx):
    core_counts, spec_counts = _pack_skill_counts(idx)
    populated_spec = {d for d, c in spec_counts.items() if c > 0}
    return {
        "core_packs": len(idx.get("packs", [])),
        "populated_spec_packs": len(populated_spec),
        "skills": len(idx.get("skills", [])),
        "agents": len(idx.get("agents", [])),
    }, core_counts, spec_counts, populated_spec


def _check_stat_numbers(source_label, text, pattern, truth):
    """Compares a (core packs, spec packs, skills, agents) 4-tuple stated in
    text against the true counts from skills_index.json."""
    m = re.search(pattern, text, re.DOTALL)
    if not m:
        warnings.append(f"{source_label}: could not locate the stats line to drift-check "
                         f"(wording may have changed — update the pattern in validate.py)")
        return
    stated_core, stated_spec, stated_skills, stated_agents = (int(g) for g in m.groups())
    if stated_core != truth["core_packs"]:
        errors.append(f"{source_label}: says {stated_core} core packs, "
                       f"skills_index.json has {truth['core_packs']}")
    if stated_spec != truth["populated_spec_packs"]:
        errors.append(f"{source_label}: says {stated_spec} specialisation packs, "
                       f"skills_index.json has {truth['populated_spec_packs']} populated")
    if stated_skills != truth["skills"]:
        errors.append(f"{source_label}: says {stated_skills} skills, "
                       f"skills_index.json has {truth['skills']}")
    if stated_agents != truth["agents"]:
        errors.append(f"{source_label}: says {stated_agents} audit agents, "
                       f"skills_index.json has {truth['agents']}")


def _rows_from_readme(text):
    """Each core/specialisation pack row in README.md's markdown tables:
    | [`dir`](maybe-specialisation-packs/dir/README.md) | description | N |
    The code-span dir and the path dir are always identical by convention,
    so only the code-span capture is used."""
    rows = []
    for pack_dir, prefix, count in re.findall(
        r"\|\s*\[`([a-z0-9-]+)`\]\((specialisation-packs/)?[a-z0-9-]+/README\.md\)[^|]*\|[^|]*\|\s*(\d+)\s*\|",
        text,
    ):
        rows.append((bool(prefix), pack_dir, count))
    return rows


def _rows_from_pages(text):
    """Each core/specialisation pack row in docs/index.html's compact tables:
    <td class="pack-name"><a href=".../blob/main/maybe-specialisation-packs/dir/README.md">...
      ...<span class="skill-count">N</span>"""
    rows = []
    for prefix, pack_dir, count in re.findall(
        r'<td class="pack-name"><a href="[^"]*/blob/main/(specialisation-packs/)?([a-z0-9-]+)/README\.md">'
        r'.*?<span class="skill-count">(\d+)</span>',
        text, re.DOTALL,
    ):
        rows.append((bool(prefix), pack_dir, count))
    return rows


def _check_pack_row_counts(source_label, rows, core_counts, spec_counts):
    """Compares each (is_spec, pack_dir, count) row against the true
    per-pack skill count from skills_index.json."""
    seen = set()
    for is_spec, pack_dir, count_str in rows:
        seen.add((is_spec, pack_dir))
        truth_map = spec_counts if is_spec else core_counts
        truth_count = truth_map.get(pack_dir)
        if truth_count is None:
            errors.append(f"{source_label}: lists pack '{pack_dir}' not found in skills_index.json")
            continue
        if int(count_str) != truth_count:
            errors.append(f"{source_label}: pack '{pack_dir}' shown with {count_str} skills, "
                           f"skills_index.json has {truth_count}")
    for pack_dir in core_counts:
        if (False, pack_dir) not in seen:
            warnings.append(f"{source_label}: core pack '{pack_dir}' not found in the pack table "
                             f"(drift-check skipped it)")
    for pack_dir, count in spec_counts.items():
        if count > 0 and (True, pack_dir) not in seen:
            warnings.append(f"{source_label}: populated specialisation pack '{pack_dir}' not found "
                             f"in the pack table (drift-check skipped it)")


def check_docs_sync():
    """Drift check: the skill/pack counts advertised in README.md and
    docs/index.html must match skills_index.json — the single source of
    truth generated by scripts/generate_index.py. Catches exactly the kind
    of staleness that otherwise only gets caught when a person happens to
    notice (see CHANGELOG 0.24.x)."""
    idx_path = os.path.join(ROOT, "skills_index.json")
    if not os.path.exists(idx_path):
        return  # already reported by check_skills_index()
    with open(idx_path, encoding="utf-8") as f:
        try:
            idx = json.load(f)
        except json.JSONDecodeError:
            return  # already reported by check_skills_index()

    truth, core_counts, spec_counts, _ = _index_truth(idx)

    readme_path = os.path.join(ROOT, "README.md")
    if os.path.exists(readme_path):
        with open(readme_path, encoding="utf-8") as f:
            readme = f.read()
        _check_stat_numbers(
            "README.md", readme,
            r"(\d+)\s+core packs\s*·\s*(\d+)\s+populated specialisation packs\s*·\s*(\d+)\s+skills\s*·\s*(\d+)\s+audit agents",
            truth,
        )
        _check_pack_row_counts("README.md", _rows_from_readme(readme), core_counts, spec_counts)

    pages_path = os.path.join(ROOT, "docs", "index.html")
    if os.path.exists(pages_path):
        with open(pages_path, encoding="utf-8") as f:
            pages = f.read()
        _check_stat_numbers(
            "docs/index.html", pages,
            r"<b>(\d+)</b>\s*core packs.*?<b>(\d+)</b>\s*specialisation packs.*?<b>(\d+)</b>\s*skills.*?<b>(\d+)</b>\s*audit agents",
            truth,
        )
        _check_pack_row_counts("docs/index.html", _rows_from_pages(pages), core_counts, spec_counts)


def main():
    packs = check_packs()
    check_specialisation_pack_skills()
    check_marketplace(packs)
    check_skills_index()
    check_docs_sync()

    if warnings:
        print(f"Warnings ({len(warnings)}):")
        for w in warnings:
            print("  -", w)
    if errors:
        print(f"\nERRORS ({len(errors)}) — validation FAILED:")
        for e in errors:
            print("  -", e)
        return 1
    print(f"OK — {len(packs)} packs and {agent_count} agents validated, no errors.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
