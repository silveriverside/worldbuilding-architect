#!/usr/bin/env python3
"""
init_codex.py — scaffold a worldbuilding codex folder from the bundled templates.

Usage:
    python init_codex.py "<world-name>" [target_dir] [--multiline]

Creates  <target_dir>/worldbuilding/<world-slug>/  with the standard structure and seeds
index/registry files from assets/templates/. Existing files are never overwritten.
Pass --multiline to also scaffold the optional multi-worldline machinery
(10-timeline-mechanics.md + 11-worldlines/) for time-travel / branching / loop worlds.
"""
import os
import re
import sys
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
TPL = os.path.join(HERE, "..", "assets", "templates")

SUBDIRS = [
    "01-timeline",
    "02-factions",
    "03-tech-and-phenomena",
    "04-geography",
    "05-peoples-and-species",
    "06-characters",
    "07-storylines",
]

# template file -> destination relative path
SEED = {
    "00-overview.md": "00-overview.md",
    "01-timeline-index.md": "01-timeline/_index.md",
    "07-storylines-index.md": "07-storylines/_index.md",
    "08-naming-lexicon.md": "08-naming-lexicon.md",
    "09-undercurrents.md": "09-undercurrents.md",
}

INDEX_STUBS = {
    "02-factions/_index.md": "# Factions — Index\n\n| Faction | One-line | World if they win | File |\n|---|---|---|---|\n",
    "03-tech-and-phenomena/_index.md": "# Tech & Phenomena — Index\n\n| Name | What it breaks | File |\n|---|---|---|\n",
    "04-geography/_index.md": "# Geography — Index\n\n| Place | Ascendant name | Centered on | File |\n|---|---|---|---|\n",
    "05-peoples-and-species/_index.md": "# Peoples & Species — Index\n\n| Name | Naming convention | File |\n|---|---|---|\n",
    "06-characters/_index.md": "# Characters — Index\n\n| Name | Affiliation | Lines carried | File |\n|---|---|---|---|\n",
}

# optional multi-worldline machinery (only with --multiline)
MULTILINE_SEED = {
    "10-timeline-mechanics.md": "10-timeline-mechanics.md",
    "11-worldlines-tree.md": "11-worldlines/_tree.md",
}


def slugify(name: str) -> str:
    s = name.strip().lower()
    s = re.sub(r"[^\w一-鿿-]+", "-", s)
    return re.sub(r"-+", "-", s).strip("-") or "world"


def write_if_absent(path: str, content: str):
    if os.path.exists(path):
        print(f"  skip (exists): {os.path.relpath(path, ROOT)}")
        return
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  create: {os.path.relpath(path, ROOT)}")


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    flags = {a for a in sys.argv[1:] if a.startswith("--")}
    if not args:
        print(__doc__)
        sys.exit(1)
    world = args[0]
    target = args[1] if len(args) > 1 else os.getcwd()
    multiline = "--multiline" in flags
    global ROOT
    ROOT = os.path.join(target, "worldbuilding", slugify(world))
    os.makedirs(ROOT, exist_ok=True)
    for d in SUBDIRS:
        os.makedirs(os.path.join(ROOT, d), exist_ok=True)

    # seed from templates (with world-name substitution)
    for tpl_name, dest in SEED.items():
        src = os.path.join(TPL, tpl_name)
        try:
            with open(src, encoding="utf-8") as f:
                content = f.read().replace("{{WORLD_NAME}}", world)
        except FileNotFoundError:
            content = f"# {dest}\n"
        write_if_absent(os.path.join(ROOT, dest), content)

    for dest, content in INDEX_STUBS.items():
        write_if_absent(os.path.join(ROOT, dest), content)

    if multiline:
        os.makedirs(os.path.join(ROOT, "11-worldlines"), exist_ok=True)
        for tpl_name, dest in MULTILINE_SEED.items():
            src = os.path.join(TPL, tpl_name)
            try:
                with open(src, encoding="utf-8") as f:
                    content = f.read().replace("{{WORLD_NAME}}", world)
            except FileNotFoundError:
                content = f"# {dest}\n"
            write_if_absent(os.path.join(ROOT, dest), content)

    write_if_absent(
        os.path.join(ROOT, "CHANGELOG.md"),
        f"# Changelog — {world}\n\n> Append a line each session: what changed, so the history-of-the-history is traceable.\n\n",
    )

    print(f"\nCodex ready: {ROOT}")
    print("Next: fill 00-overview.md, sketch eras in 01-timeline/_index.md, seed 2-3 factions.")
    if multiline:
        print("Multi-worldline: fix causality rules in 10-timeline-mechanics.md BEFORE writing any time travel.")


if __name__ == "__main__":
    main()
