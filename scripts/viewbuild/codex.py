"""Scan a worldbuilding codex into a structured model.

Reads every .md file, extracts front-matter via the local parser, and
groups entities by `type`. Files lacking the relational skeleton are
recorded as `degraded` so the build report can flag them as fixable
gaps (never silently ignored).
"""
import os

from .frontmatter import parse_frontmatter

# directory -> entity type expected to live there (for degraded-detection)
EXPECTED = {
    "01-timeline": "era",
    "02-factions": "faction",
    "06-characters": "character",
    "11-worldlines": "worldline",
}

# files that are indexes / scaffolding, not entities — skip degraded-warning
SKIP_NAMES = {"_index.md", "README.md", "CHANGELOG.md"}


def _slug(path):
    return os.path.splitext(os.path.basename(path))[0]


def scan_codex(root):
    """Return (model: dict[type->list], degraded: list[dict])."""
    model = {"era": [], "faction": [], "character": [], "worldline": []}
    degraded = []
    for dirpath, _dirs, files in os.walk(root):
        # don't descend into generated views
        if os.path.basename(dirpath) == "_views":
            continue
        for fn in sorted(files):
            if not fn.endswith(".md"):
                continue
            full = os.path.join(dirpath, fn)
            rel = os.path.relpath(full, root)
            try:
                with open(full, encoding="utf-8") as f:
                    text = f.read()
            except OSError as e:
                degraded.append({"file": rel, "reason": f"read error: {e}"})
                continue
            meta, _body, had = parse_frontmatter(text)
            etype = meta.get("type")
            if etype in model:
                meta.setdefault("id", _slug(full))
                meta["_file"] = rel
                model[etype].append(meta)
                continue
            # no usable type — is this a slot we expected to be structured?
            top = rel.split(os.sep)[0]
            if fn in SKIP_NAMES or fn.startswith("_"):
                continue
            if top in EXPECTED:
                degraded.append({
                    "file": rel,
                    "reason": (
                        f"no front-matter type; expected '{EXPECTED[top]}'. "
                        "Diagram cannot include this entity until skeleton added."
                    ) if not had else
                    f"front-matter present but missing 'type: {EXPECTED[top]}'.",
                })
    return model, degraded
