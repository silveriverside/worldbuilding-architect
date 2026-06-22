# Visual Style Bible — 锚地 Anchorage

> 视觉的"核心问题"：先定全局，再画局部。任何一张角色图、场景图、物件图、分镜，
> 都必须继承这里定义的风格锚、色板、形状语言与世界逻辑，否则风格会打架。
> 视觉一致性（visual consistency）= 跨图保持同一套画风/配色/材质/形状语义。
> 这是世界观"命名一致性"在视觉上的延伸——见 `08-naming-lexicon.md` 的同构思路。

## 1. Art style（风格锚 · 全局唯一）
- 媒介：写实厚涂概念设计（painterly concept art），偏电影分镜质感，非卡通、非赛璐璐。
- 基调：工业、潮湿、缓慢的不安；伟大工程脚下的市井政治；历史洪流里的小人物。
- 参考定位（学结构不抄设定）：攻壳机动队的湿润霓虹与义体冷感、Blade Runner 2049 的体量与雾、
  船坞/港口工业纪实摄影的真实磨损。
- **全局 style 后缀**（可直接粘进任意文生图工具）：
  `cinematic painterly concept art, industrial humid harbour, volumetric haze,
   muted teal-and-rust palette, weathered surfaces, overcast diffuse light,
   small humans dwarfed by megastructure, film still, high detail —no neon-clean, no cartoon`

## 2. Color palette（色板 · 主 70 / 辅 20 / 点缀 10）
- 主色（70%）：潮湿的青灰、缆绳钢灰、混凝土冷调（teal-grey / steel / wet concrete）。
- 辅色（20%）：锈红、油污褐——义体与机械的体温（rust / oil-brown）。
- 点缀（10%）：固件许可灯的冷蓝、港务封条的警示黄（license-blue / authority-yellow）。
- 情绪流程：越往城上越冷越蓝（缆与上传诊所），越往潮下越暖越脏（作坊与劳工区）。

## 3. Shape language（形状语言 · 跨实体共用）
- 垂直 vs 水平：缆与电梯是绝对垂直的"神性"线；市井是层叠的水平脏乱——二者对冲。
- 主导形：钢索的直线/张力，对比缆脚下有机生长的违章建筑曲线。
- 母题：缆/绳/锚/钩（系链时代的隐喻），潮位线（分层的社会边界）。

## 4. World logic（世界逻辑 · 视觉可信度根基）
- 气候决定外观：赤道潮滩 → 一切都在生锈、长盐、滴水；金属有盐蚀，布料发潮。
- 经济决定材质：穷人用补贴"丙系"义体（粗糙塑料+裸露固件），富人用"光环"（精密、哑光、贵金属）。
- 阶级决定光：上层是诊所的无影冷光，潮下是作坊的单灯暖光与阴影。

## 5. Reference 体系（分桶，每桶若干，仅作灵感/物件参照）
> 找冷门或专业物件时优先搜真实参考图：船坞结构、义肢机构、太空电梯工程图、港口起重机、
> 工业封条/标识、潮间带盐蚀质感。链接放各实体的 Visual 区块，不下载入库。
- shape 桶：太空电梯/系绳卫星工程图、港口龙门吊。
- material 桶：盐蚀钢、做旧塑料义体、油污工装。
- lighting 桶：阴天港口、单灯地下作坊、诊所冷光。
- story 桶：移民潮港口纪实、罢工现场、义体维修摊。

## 6. 生成锚点（reusable prompt anchor）
- 每个实体的 Visual 区块都以"全局 style 后缀（见 §1）+ 本实体固定特征"拼成完整 prompt。
- 若用模型生成：固定 seed 复现、备好负向词（见 §1 的 —no…）、首图作 reference 锚定后续。
- 若不用 AI 生成：本区块即一份给人类画师的 brief，同样成立。
