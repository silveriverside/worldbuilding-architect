<!-- VIEW SKELETON (optional): declare the TRUNK worldline here so build_views.py
     can root the tree. Each branch lives in its own wl-<id>-<slug>.md with its
     own skeleton (template at the bottom of this file).
---
id: wl-alpha
type: worldline
name: "{{home line name}}"
parent: null
status: trunk
fixed_points: ["{{events recurring across lines}}"]
---
-->

# Worldlines — Tree

> The shape of the multiverse at a glance. See `references/multi-worldline.md`.
> Author worldlines as DIFFS against the trunk codex, not full rewrites.

## Branch tree
```
WL-α (home line) ──┬── WL-β1  (<divergence>) ──── ...
                   └── WL-β2  (<divergence>) ──── ...
```

## Worldline registry
| ID | In-world name (with provenance) | Parent | Divergence point | Convergence status | File |
|----|----------------------------------|--------|------------------|--------------------|------|
| WL-α | *(the "home"/base line)* | — | — | trunk | base codex |
| WL-β1 | | WL-α | | live / merging / pruned | `wl-b1-<slug>.md` |

> Fixed points (events recurring across most lines) are logged in `10-timeline-mechanics.md`.

---

## Worldline file template (copy into `wl-<id>-<slug>.md`)

```
---
id: wl-<id>
type: worldline
name: "{{NAME}}"
parent: {{parent-id, or null for the trunk}}
diverge_at: "{{event/date}}"
diverge_trigger: "{{the choice that split it}}"
converges: "{{fixed point it is pulled toward, optional}}"
status: live   # live / merging / pruned ; use `trunk` for the home line
---
# Worldline WL-<id> — {{NAME}}

> A DIFF against {{PARENT}}. Read the trunk + this patch to know what's true here.

## Divergence
- Splits from: {{PARENT}} at {{event/date}}
- The cause/choice that split it: {{ }}

## Delta from parent (only what's different)
- Who lives / dies differently: {{ }}
- What tech / institution exists or doesn't: {{ }}
- Who holds power differently: {{ }}
- Renamed places / new vocabulary: {{ }}  (→ lexicon)

## Convergence
- Being pulled back toward an attractor? Toward which fixed point? {{ }}
- Merged into / pruned by: {{ }}

## Storylines running here
- {{ → 07-storylines/ }}
```
