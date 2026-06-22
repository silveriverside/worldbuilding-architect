---
id: wl-alpha
type: worldline
name: "本线 The Standing Line"
parent: null
status: trunk
fixed_points: ["丙七召回", "韦氏裁决", "第一次回声"]
---

# Worldlines — Tree

> 多元宇宙的形状。见 `references/multi-worldline.md`。
> 世界线一律以"对主干的 diff"撰写，不重写整个设定。

## Branch tree
```
WL-α (主线/home) ──┬── WL-β1  (韦氏裁决判"副本非人") ──── 上传被禁、港务靠义体修复夺权
                   └── WL-β2  (港务把回声证据多压了 22 年) ──┐
                                                          └── 在「第一次回声」处向 α 收束
```
> 三条线最终都撞上同一个不动点——**第一次回声**（漂民始终在那片"海"里，暗流④是吸引子）。
> 变的只是抵达它的路径、日期与代价；这正是世界线收束的意义。

## Worldline registry
| ID | In-world name (with provenance) | Parent | Divergence point | Convergence status | File |
|----|----------------------------------|--------|------------------|--------------------|------|
| WL-α | **本线 the Standing Line**（港务术语，"锚还立着的那条"）| — | — | trunk（主干设定）| 基础 codex |
| WL-β1 | **干线 the Dry Line**（因上传被禁、人人"落地"，戏称"干的"——没有上传的"湿"档案）| WL-α | +80 韦氏裁决判**副本非人** | live；仍朝第一次回声收束 | `wl-b1-the-dry-line.md` |
| WL-β2 | **静线 the Long Quiet**（回声被多压了二十二年，海面"久静"）| WL-α | +110 港务压下首份回声证据 | live；在第一次回声处与 α 收束 | `wl-b2-the-long-quiet.md` |

> 不动点（各线复现的事件）登记于 `10-timeline-mechanics.md`：丙七召回、韦氏裁决、第一次回声。
