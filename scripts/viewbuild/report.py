"""Build report: what was rendered + which files lack the skeleton.

Degraded entries are surfaced as a fixable to-do list, per project rule
that fallbacks must be logged as bugs to fix, not normal operation.
"""


def build_report(model, degraded):
    lines = ["# Build report — view generation", ""]
    lines.append("## Rendered")
    lines.append("")
    lines.append("| type | count |")
    lines.append("|---|---|")
    for t in ("worldline", "era", "faction", "character"):
        lines.append("| %s | %d |" % (t, len(model.get(t, []))))
    lines.append("")
    if degraded:
        lines.append("## ⚠ Degraded — fixable gaps (NOT normal; add skeleton)")
        lines.append("")
        lines.append("| file | reason |")
        lines.append("|---|---|")
        for d in degraded:
            lines.append("| %s | %s |" % (d["file"], d["reason"]))
        lines.append("")
        lines.append("> 这些文件未进入图谱。补齐 front-matter 后重跑即可纳入。")
    else:
        lines.append("## ✓ No degraded files — every expected entity had its skeleton.")
    lines.append("")
    return "\n".join(lines), len(degraded)
