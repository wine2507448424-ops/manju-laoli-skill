# 总控路由补丁说明

本扩展安装在仓库根目录，与 `short-drama-director`、`sd-asset-engine` 等目录同级。

## 路由触发
现代都市/霸总/豪门/职场/商战/都市悬疑；现代办公室、豪宅、酒店、医院、餐厅等场景资产；俯视结构图、人物站位图、走位图、机位覆盖、真人/3D双模式与跨镜连续性。

## 子技能路由
| 请求 | 子技能 | 必读 |
|---|---|---|
| 现代场景资产、俯视结构图、站位/走位、机位覆盖 | `sd-modern-drama-engine` | `sd-modern-drama-engine/SKILL.md` 与对应 references |
| 场景坐标/导演调度 | 同上 + 原总控 | `short-drama-director/references/blocking-direction.md` |
| 故事板图与镜头面板 | 同上 + 原分镜引擎 | `sd-storyboard-engine/references/storyboard-sheet-template.md` |
| 连续性 | 同上 + 原质检引擎 | `sd-qc-engine` 对应连续性规则 |

## 原规则不变
五道前置锁、I画风锁、M0/M1/M2、Seedance 2.5/2.0语法分离、七段式投喂、原C系列机检和投喂层闸门均保持原样。

## 版本标识
个人扩展分支；不改写上游版本号，不宣称为原作者官方发行。
