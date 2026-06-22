<!-- VIEW SKELETON (optional): minimal fields for scripts/build_views.py to draw
     the character network. Use other characters' ids in `to:` for internal edges;
     any other name renders as an external node. Delete this block to opt out.
---
id: {{slug}}
type: character
name: "{{NAME}}"
affiliation: ["{{faction-id or group}}"]
relations:
  - to: {{other-character-id-or-name}}
    type: {{对手/血缘/任职/盟友…}}
lines: ["{{storyline}}"]
---
-->

# Character — {{NAME}}

> Actors who carry the storylines. Tie them to factions, events, and lines they cross.

## Name & provenance
*(Named per their culture's convention — see their `05-peoples-and-species/` file.)*

## Who they are
*(Role, era(s) active, affiliation — link to `02-factions/`.)*

## What they want vs. what they fear
*( )*

## Their place in the web
- Mainline(s) they carry: *(→ `07-storylines/`)*
- Hidden-line involvement: *(do they unknowingly serve the hidden mainline?)*
- Side-arcs: *( )*

## The small decisions that matter
*(Local choices they make that feed undercurrents / become later triggers — the "you were there"
mechanic. See `references/emergent-history.md`.)*

## Arc / trajectory
*( )*

## Visual (OPTIONAL — only if illustrating; inherits `12-visual-style.md`)
- **固定特征 (identity anchors)**: *(跨图不可变的辨识特征：脸/发/肤/标记/义体等)*
- **比例 / 体型**: *(头身比、身量、体态)*
- **Signature outfit**: *(标志性服装，逐件颜色款式)*
- **表情谱**: *(默认 + 2-3 个关键情绪)*
- **剪影**: *(远处即可辨识的轮廓要素)*
- **配色**: *(本角色主色，须落在圣经色板内)*
- **参考 (reference)**: *(网络参考图 URL，仅灵感/物件参照，不下载)*
- **生成 prompt**: `<圣经 §1 全局 style 后缀> + <本角色固定特征英文串>`
- **产出图**: *(assets/visuals/<slug>/ 的相对链接；无则留空)*
