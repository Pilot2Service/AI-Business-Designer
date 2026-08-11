#!/usr/bin/env python3
"""
generate_index.py — rebuilds skills_index.json from disk + SKILL.md frontmatter.

Never hand-edit skills_index.json. Run this after adding, moving, or renaming a skill.
Preserves maturity / source_layer / grounded_in / owner_input_needed for skills that
already exist in the index (so re-running this does not silently reset progress you've
made filling in [OWNER INPUT] sections and bumping maturity).

Usage:
    python3 scripts/generate_index.py
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


def parse_frontmatter(text):
    """Minimal YAML frontmatter parser for the restricted name/description schema."""
    m = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
    if not m:
        return None, []
    block = m.group(1)
    data = {}
    extra_keys = []
    current_key = None
    for line in block.split("\n"):
        if not line.strip():
            continue
        kv = re.match(r"^([A-Za-z_][A-Za-z0-9_]*):\s*(.*)$", line)
        if kv:
            key, val = kv.group(1), kv.group(2).strip()
            current_key = key
            if key not in ("name", "description"):
                extra_keys.append(key)
            val = val.strip()
            if val.startswith('"') and val.endswith('"') and len(val) >= 2:
                val = val[1:-1]
            elif val.startswith(">") or val == "":
                val = ""  # multi-line block scalar — not expected in this schema
            data[key] = val
        elif current_key and line.startswith("  "):
            data[current_key] = (data.get(current_key, "") + " " + line.strip()).strip()
    return data, extra_keys


def find_agents(pack_dir_full, pack_name):
    """Agents (<pack>/agents/<agent-id>.md) are delegatable, read-only subagents —
    indexed separately from skills since they use a wider frontmatter (tools/model
    allowed in addition to name+description, ks. scripts/validate.py)."""
    agents_dir = os.path.join(pack_dir_full, "agents")
    out = []
    if not os.path.isdir(agents_dir):
        return out
    for fname in sorted(os.listdir(agents_dir)):
        if not fname.endswith(".md"):
            continue
        agent_id = fname[:-3]
        with open(os.path.join(agents_dir, fname), encoding="utf-8") as f:
            text = f.read()
        fm, _ = parse_frontmatter(text)
        fm = fm or {}
        out.append({
            "id": agent_id,
            "pack": pack_name,
            "description": fm.get("description", ""),
            "path": os.path.relpath(os.path.join(agents_dir, fname), ROOT),
        })
    return out


def load_existing_index():
    path = os.path.join(ROOT, "skills_index.json")
    if not os.path.exists(path):
        return {}
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    return {s["id"]: s for s in data.get("skills", [])}


def find_pack_dirs():
    packs = []
    for name in sorted(os.listdir(ROOT)):
        full = os.path.join(ROOT, name)
        if not os.path.isdir(full) or name in NON_PACK_DIRS or name.startswith("."):
            continue
        plugin_json = os.path.join(full, ".claude-plugin", "plugin.json")
        if os.path.exists(plugin_json):
            with open(plugin_json, encoding="utf-8") as f:
                meta = json.load(f)
            packs.append({"dir": name, "name": meta.get("name", name), "title": meta.get("displayName", name)})
    return packs


def find_specialisation_packs():
    base = os.path.join(ROOT, "specialisation-packs")
    out = []
    if not os.path.isdir(base):
        return out
    for name in sorted(os.listdir(base)):
        readme = os.path.join(base, name, "README.md")
        if os.path.exists(readme):
            with open(readme, encoding="utf-8") as f:
                text = f.read()
            fm, _ = parse_frontmatter(text)
            # title: prefer "# Title" without a trailing "[SCAFFOLD ...]" marker; fall
            # back to a plain "# Title" heading (populated packs have no marker).
            title_match = re.search(r"^#\s+(.+?)\s*\[", text, re.MULTILINE)
            if not title_match:
                title_match = re.search(r"^#\s+(.+?)\s*$", text, re.MULTILINE)
            title = title_match.group(1) if title_match else name
            fm = fm or {}
            status = fm.get("status", "placeholder")
            out.append({
                "dir": name, "title": title,
                "status": status,
                "owner_input_needed": fm.get("owner_input_needed", "true") != "false",
            })
    return out


def find_specialisation_pack_skill_source(pack_dir):
    """A specialisation pack has no plugin.json, so it needs a synthetic pack
    record for indexing purposes. Pack 'name' for these skills is the folder
    name, prefixed so it's visually distinguishable from core-pack names in
    skills_index.json."""
    return {"dir": pack_dir, "name": f"specialisation-packs/{pack_dir}"}


def main():
    existing = load_existing_index()
    packs = find_pack_dirs()
    skills = []
    agents = []
    errors = []

    def index_skills_dir(skills_dir, pack_name):
        if not os.path.isdir(skills_dir):
            return
        for skill_id in sorted(os.listdir(skills_dir)):
            skill_md = os.path.join(skills_dir, skill_id, "SKILL.md")
            if not os.path.exists(skill_md):
                continue
            with open(skill_md, encoding="utf-8") as f:
                text = f.read()
            fm, extra_keys = parse_frontmatter(text)
            if fm is None:
                errors.append(f"{skill_md}: no frontmatter found")
                continue
            if extra_keys:
                errors.append(f"{skill_md}: extra frontmatter keys not allowed: {extra_keys}")
            if fm.get("name") != skill_id:
                errors.append(f"{skill_md}: name '{fm.get('name')}' != folder '{skill_id}'")

            prev = existing.get(skill_id, {})
            skills.append({
                "id": skill_id,
                "pack": pack_name,
                "title": prev.get("title", skill_id.replace("-", " ").title()),
                "description": fm.get("description", ""),
                "maturity": prev.get("maturity", "scaffold"),
                "source_layer": prev.get("source_layer", "research"),
                "grounded_in": prev.get("grounded_in", []),
                "owner_input_needed": prev.get("owner_input_needed", True),
                "path": os.path.relpath(skill_md, ROOT),
            })

    for pack in packs:
        index_skills_dir(os.path.join(ROOT, pack["dir"], "skills"), pack["name"])
        agents.extend(find_agents(os.path.join(ROOT, pack["dir"]), pack["name"]))

    specialisation_packs = find_specialisation_packs()
    for sp in specialisation_packs:
        src = find_specialisation_pack_skill_source(sp["dir"])
        index_skills_dir(os.path.join(ROOT, "specialisation-packs", sp["dir"], "skills"), src["name"])
        agents.extend(find_agents(os.path.join(ROOT, "specialisation-packs", sp["dir"]), src["name"]))

    index = {
        "repo": "ai-business-designer-skills",
        "version": "0.22.0",
        "generated": "auto",
        "generated_by": "scripts/generate_index.py — do not hand-edit",
        "packs": [{"dir": p["dir"], "name": p["name"], "title": p["title"]} for p in packs],
        "specialisation_packs": specialisation_packs,
        "skills": skills,
        "agents": agents,
    }

    if errors:
        print("Frontmatter errors (index was still written, fix these):")
        for e in errors:
            print("  -", e)

    out_path = os.path.join(ROOT, "skills_index.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(index, f, ensure_ascii=False, indent=2)
        f.write("\n")
    print(f"Wrote {out_path} — {len(skills)} skills, {len(packs)} packs, {len(agents)} agents.")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
