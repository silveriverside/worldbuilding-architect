"""Generate Mermaid diagrams (product A) embedded in a Markdown file.

Diagrams:
  - worldline tree   -> gitGraph (branch = divergence, merge = convergence)
  - era timeline     -> timeline
  - character network-> graph with edge labels
  - faction map      -> graph (rivals / sponsor)

Mermaid renders natively in Obsidian (full type support). Output is a
single Markdown file under _views/.
"""


def _esc(s):
    return str(s).replace('"', "'") if s is not None else ""


def worldline_gitgraph(worldlines):
    trunk = next((w for w in worldlines if w.get("status") == "trunk"), None)
    branches = [w for w in worldlines if w.get("status") != "trunk"]
    out = ["```mermaid", "gitGraph"]
    out.append('   commit id: "trunk: %s"' % _esc(trunk["name"] if trunk else "α"))
    for w in branches:
        bid = _esc(w.get("id"))
        out.append("   branch %s" % bid)
        out.append("   checkout %s" % bid)
        out.append('   commit id: "%s @%s"' % (_esc(w.get("name")), _esc(w.get("diverge_at"))))
        conv = w.get("converges")
        if conv:
            out.append('   commit id: "converge: %s"' % _esc(conv))
        out.append("   checkout main")
    out.append("```")
    return "\n".join(out)


def era_timeline(eras):
    eras = sorted(eras, key=lambda e: e.get("order") or 0)
    out = ["```mermaid", "timeline", "   title 时代主轴 / Eras"]
    for e in eras:
        span = "%s–%s" % (e.get("span_start", "?"), e.get("span_end", "?"))
        tips = e.get("tipping_points") or []
        label = "%s (%s)" % (_esc(e.get("name")), span)
        if tips:
            events = " : ".join(_esc(t) for t in tips)
            out.append("   %s : %s" % (label, events))
        else:
            out.append("   %s" % label)
    out.append("```")
    return "\n".join(out)


def character_graph(characters):
    out = ["```mermaid", "graph LR"]
    seen = set()
    drawn_pairs = set()
    for c in characters:
        cid = _esc(c.get("id"))
        out.append('   %s["%s"]' % (cid, _esc(c.get("name"))))
        seen.add(c.get("id"))
    for c in characters:
        cid = _esc(c.get("id"))
        for rel in c.get("relations") or []:
            to = rel.get("to")
            label = _esc(rel.get("type"))
            if to in seen:
                key = tuple(sorted([c.get("id"), to]))
                if key in drawn_pairs:
                    continue
                drawn_pairs.add(key)
                out.append('   %s -- "%s" --- %s' % (cid, label, _esc(to)))
            else:
                node = "ext_" + _esc(to)
                out.append('   %s(["%s"])' % (node, _esc(to)))
                out.append('   %s -. "%s" .-> %s' % (cid, label, node))
    out.append("```")
    return "\n".join(out)


def faction_graph(factions):
    out = ["```mermaid", "graph TD"]
    ids = {f.get("id") for f in factions}
    drawn = set()
    for f in factions:
        fid = _esc(f.get("id"))
        out.append('   %s["%s"]' % (fid, _esc(f.get("name"))))
    for f in factions:
        fid = _esc(f.get("id"))
        for r in f.get("rivals") or []:
            key = tuple(sorted([f.get("id"), r]))
            if r in ids and key not in drawn:
                out.append('   %s <-- "宿敌" --> %s' % (fid, _esc(r)))
                drawn.add(key)
        sponsor = f.get("sponsor")
        if sponsor:
            snode = "spon_" + _esc(sponsor)
            out.append('   %s{{"%s"}}' % (snode, _esc(sponsor)))
            out.append('   %s -. "赞助/绑定" .-> %s' % (snode, fid))
    out.append("```")
    return "\n".join(out)


def build_markdown(model):
    parts = ["# Views — 自动生成，请勿手改",
             "",
             "> 本文件由 `scripts/build_views.py` 从 codex 的 front-matter 自动生成。",
             "> 唯一真相源是各 .md 正文；改世界观后重跑脚本即可同步。",
             ""]
    if model["worldline"]:
        parts += ["## 世界线树 / Worldline tree", "", worldline_gitgraph(model["worldline"]), ""]
    if model["era"]:
        parts += ["## 时代主轴 / Timeline", "", era_timeline(model["era"]), ""]
    if model["faction"]:
        parts += ["## 派系关系 / Factions", "", faction_graph(model["faction"]), ""]
    if model["character"]:
        parts += ["## 人物关系 / Characters", "", character_graph(model["character"]), ""]
    return "\n".join(parts)
