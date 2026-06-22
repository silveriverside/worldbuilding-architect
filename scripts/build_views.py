#!/usr/bin/env python3
"""build_views.py — generate visual views from a worldbuilding codex.

From the codex front-matter (the relational skeleton) this produces, under
<codex>/_views/:
  - views.md        Mermaid diagrams (product A) — renders in Obsidian/readers
  - index.html      single self-contained interactive page (product B) — open
                    by double-click, pan/zoom/click, zero dependencies
  - _build_report.md  what was rendered + fixable gaps (degraded files)

The codex .md bodies remain the single source of truth; views are derived.
Re-run after editing the world to keep everything in sync.

Usage:
    python build_views.py <codex-dir> [--title "World Name"]
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from viewbuild.codex import scan_codex
from viewbuild.mermaid import build_markdown
from viewbuild.html import build_html
from viewbuild.report import build_report


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if not args:
        print(__doc__)
        sys.exit(1)
    codex = os.path.abspath(args[0])
    if not os.path.isdir(codex):
        print("error: not a directory: %s" % codex)
        sys.exit(1)

    title = os.path.basename(codex.rstrip("/"))
    if "--title" in sys.argv:
        i = sys.argv.index("--title")
        if i + 1 < len(sys.argv):
            title = sys.argv[i + 1]

    model, degraded = scan_codex(codex)
    total = sum(len(v) for v in model.values())
    if total == 0:
        print("error: no entities with front-matter found under %s" % codex)
        print("       add 'type:' skeletons (see assets/templates/) and retry.")
        sys.exit(2)

    out_dir = os.path.join(codex, "_views")
    os.makedirs(out_dir, exist_ok=True)

    with open(os.path.join(out_dir, "views.md"), "w", encoding="utf-8") as f:
        f.write(build_markdown(model))
    with open(os.path.join(out_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(build_html(model, title))
    report, n_degraded = build_report(model, degraded)
    with open(os.path.join(out_dir, "_build_report.md"), "w", encoding="utf-8") as f:
        f.write(report)

    print("Views written to %s" % out_dir)
    for t in ("worldline", "era", "faction", "character"):
        print("  %-10s %d" % (t, len(model[t])))
    if n_degraded:
        print("WARNING: %d file(s) lack the skeleton — see _build_report.md "
              "(fixable, not normal)." % n_degraded)
    else:
        print("All expected entities had their skeleton.")


if __name__ == "__main__":
    main()
