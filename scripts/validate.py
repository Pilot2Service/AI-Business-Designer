#!/usr/bin/env python3
"""
validate.py — structural + frontmatter gate for the AI Business Designer skills repo.

Run before every commit (and wire into CI once this repo has one). Exit code 1 on any
failure, matching the [redacted]/claude-for-legal-finland convention of a validator
that must be green before push.

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


def check_packs():
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

        skills_dir = os.path.join(full, "skills")
        if not os.path.isdir(skills_dir):
            warnings.append(f"pack '{name}': no skills/ directory yet")
            continue
        for skill_id in sorted(os.listdir(skills_dir)):
            _check_skill_frontmatter(name, skill_id, os.path.join(skills_dir, skill_id, "SKILL.md"))
    return packs


def check_specialisation_pack_skills():
    """Specialisation packs (specialisation-packs/*/) don't have plugin.json and
    aren't installable plugins in their own right, but once they have a non-empty
    skills/ directory, the same frontmatter contract applies, and README.md +
    CLAUDE.md become required (mirrors REQUIRED_PACK_FILES minus plugin.json)."""
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
        for skill_id in sorted(os.listdir(skills_dir)):
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


def main():
    packs = check_packs()
    check_specialisation_pack_skills()
    check_marketplace(packs)
    check_skills_index()

    if warnings:
        print(f"Varoituksia ({len(warnings)}):")
        for w in warnings:
            print("  -", w)
    if errors:
        print(f"\nVIRHEITÄ ({len(errors)}) — validointi EPÄONNISTUI:")
        for e in errors:
            print("  -", e)
        return 1
    print(f"OK — {len(packs)} pakkia validoitu, ei virheitä.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
