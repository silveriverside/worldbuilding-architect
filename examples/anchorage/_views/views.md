# Views — 自动生成，请勿手改

> 本文件由 `scripts/build_views.py` 从 codex 的 front-matter 自动生成。
> 唯一真相源是各 .md 正文；改世界观后重跑脚本即可同步。

## 世界线树 / Worldline tree

```mermaid
gitGraph
   commit id: "trunk: 本线 The Standing Line"
   branch wl-b1
   checkout wl-b1
   commit id: "干线 The Dry Line @+80"
   commit id: "converge: 第一次回声"
   checkout main
   branch wl-b2
   checkout wl-b2
   commit id: "静线 The Long Quiet @+110"
   commit id: "converge: 第一次回声"
   checkout main
```

## 时代主轴 / Timeline

```mermaid
timeline
   title 时代主轴 / Eras
   系链时代 The Tether Years (+0–+40) : 丙七召回
   退线纪 The Slack (+40–+95) : 韦氏裁决 : 走样的发现
```

## 派系关系 / Factions

```mermaid
graph TD
   the-grounders["落地党 The Grounders"]
   the-shelved["搁架众 The Shelved"]
   the-grounders <-- "宿敌" --> the-shelved
   spon_义体行会{{"义体行会"}}
   spon_义体行会 -. "赞助/绑定" .-> the-grounders
   spon_港务{{"港务"}}
   spon_港务 -. "赞助/绑定" .-> the-shelved
```

## 人物关系 / Characters

```mermaid
graph LR
   mira-okonkwo["Mira Okonkwo"]
   silas-quist["Silas Quist"]
   mira-okonkwo -- "对手" --- silas-quist
   ext_港务(["港务"])
   mira-okonkwo -. "任职" .-> ext_港务
   ext_潮下作坊(["潮下作坊"])
   silas-quist -. "出身" .-> ext_潮下作坊
```
