<div align="center">

# Kling 4 Use Cases

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](LICENSE)
[![EvoLink](https://img.shields.io/badge/Explore_video_models-EvoLink-black)](https://evolink.ai/models?utm_source=github&utm_medium=badge&utm_campaign=awesome-kling-4-usecases&utm_content=zh-CN_badge)

[![English](https://img.shields.io/badge/English-111111)](README.md) [![Español](https://img.shields.io/badge/Espa%C3%B1ol-ffb703)](README_es.md) [![Português](https://img.shields.io/badge/Portugu%C3%AAs-2a9d8f)](README_pt.md) [![日本語](https://img.shields.io/badge/%E6%97%A5%E6%9C%AC%E8%AA%9E-52b788)](README_ja.md) [![한국어](https://img.shields.io/badge/%ED%95%9C%EA%B5%AD%EC%96%B4-4ea8de)](README_ko.md) [![Deutsch](https://img.shields.io/badge/Deutsch-f4a261)](README_de.md) [![Français](https://img.shields.io/badge/Fran%C3%A7ais-e76f51)](README_fr.md) [![Türkçe](https://img.shields.io/badge/T%C3%BCrk%C3%A7e-d62828)](README_tr.md) [![繁體中文](https://img.shields.io/badge/%E7%B9%81%E9%AB%94%E4%B8%AD%E6%96%87-8338ec)](README_zh-TW.md) [![简体中文](https://img.shields.io/badge/%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87-ef476f)](README_zh-CN.md) [![Русский](https://img.shields.io/badge/%D0%A0%D1%83%D1%81%D1%81%D0%BA%D0%B8%D0%B9-577590)](README_ru.md)

</div>

## 🍌 简介

**通过公开视频、创作者工作流和已公开提示词，了解 Kling 4 / 4.0 的具体用法** 本仓库帮助视频创作者、开发者和模型评测者挑选值得观察或测试的场景，每个案例都链接原帖与发帖账号

点击视频封面观看，结合证据说明阅读；只有作者实际公开了 Prompt 才提供原文供复制，发帖账号可能是分发方，署名本身不代表原创身份已经确认

[查看 EvoLink 视频模型](https://evolink.ai/models?utm_source=github&utm_medium=introduction&utm_campaign=awesome-kling-4-usecases&utm_content=zh-CN_introduction)

## 📊 概览

**83 个精选案例 · 10 个案例包含 11 组公开 Prompt · 8 个分类** 内容覆盖工作流、广告、叙事、动作、游戏概念、动画、世界场景与对比，每个案例都有来源、账号链接、使用要点、媒体、类型及 UTC 来源日期

> [!NOTE]
> 这些案例有公开来源支持，但并非独立验证的 Kling API 调用或受控基准测试，部分条目是同一部成片的不同剪段；游戏式视频不代表可玩的游戏，剪辑成片时长也不代表原生生成时长，价格与积分仍按作者自述标注

下载[案例数据](data/use-cases.json)或[可排序 CSV](data/use-cases.csv)，其中保留采集时的互动指标、Prompt 状态与来源关系；[采集范围](docs/collection-scope.md)说明了两次检索的时间窗口及其间隔，本仓库是固定日期的资料集，并非实时全量索引

<a id="quick-start"></a>
## ⚡ 快速开始

1. [查看 EvoLink 视频模型](https://evolink.ai/models?utm_source=github&utm_medium=quick_start&utm_campaign=awesome-kling-4-usecases&utm_content=zh-CN_quick_start)，注册或登录账号
2. 使用已支持模型时，[创建或获取 API Key](https://evolink.ai/dashboard/keys?utm_source=github&utm_medium=api_key&utm_campaign=awesome-kling-4-usecases&utm_content=zh-CN_api_key)
3. 提交任务前先确认具体模型可用性，**截至 2026-10-17，本资料集尚未验证 Kling 4 的 API 路由与专用可安装 Skill**；可通过[阅读 Codex CLI 设置文档](https://evolink.ai/docs/en/cli/codex?utm_source=github&utm_medium=setup_docs&utm_campaign=awesome-kling-4-usecases&utm_content=zh-CN_setup_docs)了解通用配置，该文档不是经验证的 Kling 4 首次调用示例

本仓库用于研究与创作参考，不提供可运行 API 示例或模型安装器；复现案例时，不要把其他 Kling 版本直接当成同一模型

## 📑 目录

| 案例 | 分类 | 观察要点 | 类型 |
|---|---|---|---|
| [科幻场景中的角色与环境参考](#case-1) | 工作流与参考资料 | 观察独立角色表和环境表如何与长篇视频创作要求并列呈现 | Demo |
| [从 Agent 分镜到动画片段](#case-2) | 工作流与参考资料 | 将作者的剧本、分镜、Prompt 串联方式用于短动画的前期规划 | Tutorial |
| [宏大奇幻场景的参考图表](#case-3) | 工作流与参考资料 | 观察角色表、环境表与长篇场景要求之间的对应关系 | Demo |
| [手机聊天界面中的视频任务](#case-4) | 工作流与参考资料 | 先观察作者提出的 Codex 到 MCP 衔接方式，再用自己的已验证工具复现 | Tutorial |
| [起亚 SUV 的森林公路广告](#case-5) | 广告与产品故事 | 用公开的十五镜分镜，规划三十秒广告中的车辆连续性 | Demo |
| [多人物护肤品 UGC 广告拼贴](#case-6) | 广告与产品故事 | 参考可见广告形式，规划保留完整制作记录的 UGC 对照实验 | Demo |
| [迷你龙给甜点焦糖化](#case-7) | 广告与产品故事 | 以一个明确的食物动作，观察角色驱动的产品故事 | Demo |
| [橙汁纸盒的广告场景](#case-8) | 广告与产品故事 | 围绕单一产品观察包装可见度、水果意象与转场 | Demo |
| [浅绿房间里的耳机女孩](#case-9) | 角色与叙事 | 观察近景、全身动作与同一浅色场景中的角色外观 | Demo |
| [走近古典柱廊的男子](#case-10) | 角色与叙事 | 通过可见片段观察克制的动作和建筑环境连续性 | Demo |
| [湿发女性的情绪近景](#case-11) | 角色与叙事 | 观察以对白表演为主的样片中细微的面部变化和构图 | Demo |
| [电影院里的母女情绪瞬间](#case-12) | 角色与叙事 | 观察短情绪场景如何依托一个具体的个人故事 | Demo |
| [两位主播播报日语新闻](#case-13) | 角色与叙事 | 据此设计针对对白、双人调度和屏幕图文的专项测试 | Demo |
| [办公大厅里的迷你卡丁车](#case-14) | 角色与叙事 | 通过把意外的交通工具放进日常建筑场景，观察喜剧性的比例反差 | Demo |
| [男友视角下的夏日散步](#case-15) | 角色与叙事 | 复制详细公开要求，以日常互动规划三十秒连续叙事 | Demo |
| [车辆、士兵与人物近景合集](#case-16) | 角色与叙事 | 用蒙太奇挑出具体任务，再分别进行受控测试 | Demo |
| [King Cards 的魔术与城市飞行](#case-17) | 角色与叙事 | 观察较长短片如何连接舞台魔术、纸质载具和反复出现的红鸟 | Demo |
| [乡村女性与暴雨前的拖拉机](#case-18) | 角色与叙事 | 观察角色、机器和天气如何传达简短的叙事前提 | Demo |
| [恐龙冒险短片与可复用镜头要求](#case-19) | 角色与叙事 | 对照成片与作者公开的七秒动作、八秒驾车要求进行学习 | Demo |
| [快递员打开通向异世界的电梯](#case-20) | 角色与叙事 | 观察固定主角如何对同一扇门外不断变化的环境作出反应 | Demo |
| [地下乌龟水管工的喜剧场景](#case-21) | 角色与叙事 | 用作者的流程说明区分概念、角色设计、脚本、对白与声音决策 | Demo |
| [以车辆意外收尾的街头追逐](#case-22) | 角色与叙事 | 通过人物动作、构图和街头状况变化观察喜剧节奏 | Demo |
| [少女发现蓝龙的奇幻短片](#case-23) | 角色与叙事 | 观察个人奇幻故事如何形成包含固定角色的组合片段 | Demo |
| [纸质载具驶入花城](#case-24) | 角色与叙事 | 观察 King Cards 短剪段中的人物、载具与环境变化 | Demo |
| [纸质车厢里的石像变成人](#case-25) | 角色与叙事 | 观察移动载具内的角色位置与短暂形态变化 | Demo |
| [魔术师与纸牌环绕的剧场](#case-26) | 角色与叙事 | 把中心人物表演、移动道具和周围观众作为同一场景观察 | Demo |
| [庭院足浴中的女性日常](#case-27) | 角色与叙事 | 观察普通手势、服装和安静环境，而非复杂动作 | Demo |
| [以猎鹰串联举报主题短片](#case-28) | 角色与叙事 | 观察角色意象如何把手机界面镜头连接成一个主题表达 | Demo |
| [厨房里蹑行的橘猫](#case-29) | 角色与叙事 | 观察日常室内环境中的小动作与镜头距离变化 | Demo |
| [两名男子在街角相见拥抱](#case-30) | 角色与叙事 | 观察简短社交互动中的接近、身体接触与角色位置 | Demo |
| [月下云端双人剑斗](#case-31) | 动作与身体互动 | 用这段画面观察多人动作、空中调度与服装轮廓的连续性 | Demo |
| [跆拳道馆内的双人格斗](#case-32) | 动作与身体互动 | 对照格斗过程中的身体接触、双方距离与镜头位置 | Demo |
| [两辆跑车穿越城市追逐](#case-33) | 动作与身体互动 | 观察快速切换镜位时车辆身份和运动方向的延续 | Demo |
| [移动镜头下的拳击交锋](#case-34) | 动作与身体互动 | 观察出拳、防守位移与近身接触，不只看单张好看的画面 | Demo |
| [穿越爆炸街道的女战士](#case-35) | 动作与身体互动 | 观察固定角色与行驶车辆、烟雾及大规模背景特效的关系 | Demo |
| [少女与城市巨兽对峙](#case-36) | 动作与身体互动 | 跟随城市中的冲突场景，比较人物和巨兽的体量关系 | Demo |
| [穿过外星丛林的机械捕食者](#case-37) | 动作与身体互动 | 用公开 Prompt 观察加速、环境反应和后退的手持视角 | Demo |
| [骑手在战场上持长枪交锋](#case-38) | 动作与身体互动 | 观察开阔战场中的骑手互动、马匹运动与武器接触 | Demo |
| [空手道交手与地垫接触](#case-39) | 动作与身体互动 | 观察表演者与周围环境的接触，不把动作仅看作孤立姿势 | Demo |
| [便利店员工与格斗者交手](#case-40) | 动作与身体互动 | 观察带日语对白的动作样例中的近身接触与场景连续性 | Demo |
| [石台上的铠甲奇幻格斗](#case-41) | 动作与身体互动 | 观察关键帧驱动的风格化战斗中的动作调度 | Demo |
| [猫咪穿越夜间城镇](#case-42) | 动作与身体互动 | 复制作者的一镜到底 Prompt，探索相连室内外空间中的快速运动 | Demo |
| [雨中森林里的武士对决](#case-43) | 动作与身体互动 | 观察雨景格斗中的服装稳定性与武器接触 | Demo |
| [树林中黑衣女性的动作片段](#case-44) | 动作与身体互动 | 对照同一林间动作场景的不同编码版本，观察姿势与镜头运动 | Demo |
| [红纸鸟对抗紫色章鱼](#case-45) | 动作与身体互动 | 观察小型飞行主体与大型拼装生物之间的互动 | Demo |
| [篮球运动员飞身扣篮](#case-46) | 动作与身体互动 | 观察身体轨迹、篮球位置与篮筐接触 | Demo |
| [赏金猎人风格的游戏概念](#case-47) | 游戏与载具概念 | 将片段作为结合人物动作和对白的游戏预告场景参考 | Demo |
| [飞车冲上夜间巨型坡道](#case-48) | 游戏与载具概念 | 将片段用作电影化车辆概念参考，不当作游戏已经可运行的证据 | Demo |
| [日落海岸公路上的跑车竞速](#case-49) | 游戏与载具概念 | 观察竞速视频概念中的追逐镜头、光线和仪表式叠层 | Demo |
| [战斗机飞越海岛环境](#case-50) | 游戏与载具概念 | 用样片观察飞行镜头的运动和游戏界面构图 | Demo |
| [角色在浮空岛之间滑翔](#case-51) | 游戏与载具概念 | 观察第三人称视频概念从狭窄空间转入宽阔空景的方式 | Demo |
| [跟随骑手的摩托竞速概念](#case-52) | 游戏与载具概念 | 观察游戏式视频中的摩托动作、追逐镜头距离与赛道照明 | Demo |
| [第一人称港口射击场景](#case-53) | 游戏与载具概念 | 复制作者按时间分段的战术射击要求，定义十五秒视觉目标 | Demo |
| [未来城市中的飞行汽车](#case-54) | 游戏与载具概念 | 通过概念画面观察街面驾驶、飞行和城市地标之间的转换 | Demo |
| [警车追逐穿城飞车](#case-55) | 游戏与载具概念 | 观察追逐镜头概念如何结合地面车流与腾空动作 | Demo |
| [海滨驾驶转入直升机飞行](#case-56) | 游戏与载具概念 | 观察跑车、步行人物和空中镜头之间的转换 | Demo |
| [插画与实拍风格交织的音乐视频](#case-57) | 动画与风格化角色 | 观察完整 MV 如何结合不同风格和反复出现的情绪意象 | Demo |
| [厨房里的奶奶与迷你黏土龙](#case-58) | 动画与风格化角色 | 观察紧凑厨房动画中的角色互动与材质风格 | Demo |
| [夜市摊位上的动漫厨师](#case-59) | 动画与风格化角色 | 观察短篇烹饪动画中的手部动作、道具与照明 | Demo |
| [微缩人物的定格风格战斗](#case-60) | 动画与风格化角色 | 观察微缩比例和定格风格如何塑造短动作片段 | Demo |
| [发光月牙座椅上的睡眠场景](#case-61) | 动画与风格化角色 | 用场景观察装饰性光线主题与轻微人物动作 | Demo |
| [城市路口的快闪群舞](#case-62) | 动画与风格化角色 | 观察街舞片段中的群体动作、空间排列与视角变化 | Demo |
| [暴风云下的动漫剑客对决](#case-63) | 动画与风格化角色 | 观察风格化格斗中清晰的人物轮廓与兵刃互动 | Demo |
| [黑白舞台上的多人舞蹈](#case-64) | 动画与风格化角色 | 在去除色彩的条件下观察编舞与灯光 | Demo |
| [森林里玩雪的松鼠](#case-65) | 动画与风格化角色 | 观察富于表情的动物动作与统一的柔和动画风格 | Demo |
| [红衣人物穿过糖果世界](#case-66) | 动画与风格化角色 | 观察风格化人物动作与由甜点构成的环境 | Demo |
| [戴王冠的白猫吃咖喱](#case-67) | 动画与风格化角色 | 观察服装、食物道具与表情如何支撑动物角色短故事 | Demo |
| [从森林旅程转入骑龙飞行](#case-68) | 世界场景与生物 | 观察画面如何从封闭树林逐步展开为空中远景 | Demo |
| [恐怖蒙太奇中的无面人形](#case-69) | 世界场景与生物 | 观察怪物形象的连续性及不同诡异意象之间的转场 | Demo |
| [苏醒的球形外星聚落](#case-70) | 世界场景与生物 | 复制作者公开的 Prompt，探索虚构小镇中多种环境运动的配合 | Demo |
| [外星巨兽涉过浅水湖](#case-71) | 世界场景与生物 | 复制作者的 Prompt，探索体重、水面反应和缓慢升镜 | Demo |
| [巨型机甲从甲板起飞](#case-72) | 世界场景与生物 | 观察机械关节、体量与从站立转入飞行的过程 | Demo |
| [巨兽逼近拥堵的悬索桥](#case-73) | 世界场景与生物 | 观察暴雨环境中巨兽、车辆和人群之间的比例关系 | Demo |
| [报纸载具穿越纸质城市](#case-74) | 世界场景与生物 | 观察折纸风城市中的环境材质一致性与跟随镜头 | Demo |
| [山坡上的重型步行机甲](#case-75) | 世界场景与生物 | 观察机械运动、地面接触与超大武器之间的关系 | Demo |
| [哥特人物穿行雨夜](#case-76) | 世界场景与生物 | 观察氛围、轮廓和反复出现的视觉主题 | Demo |
| [纸质车厢进入发光菌菇隧道](#case-77) | 世界场景与生物 | 观察画面如何从受限的车厢视角转入明亮环境 | Demo |
| [同一森林格斗 Prompt 的双模型对比](#case-78) | 对比与评测 | 比较两路显示结果，同时保留作者声明的设置和评价边界 | Evaluation |
| [咖啡馆里的固定双人对白](#case-79) | 对比与评测 | 用公开对白 Prompt 测试轮流说话与侧脸口型同步 | Evaluation |
| [标准版与 Flash 的五人对白](#case-80) | 对比与评测 | 比较作者展示的两路结果中的角色位置与场景构图 | Evaluation |
| [虎头人物测试近身动作](#case-81) | 对比与评测 | 用创作者的格斗片段观察高接触动作与角色参考图的作用 | Evaluation |
| [音画漂移测试中的变化主持人](#case-82) | 对比与评测 | 把样片作为独立测量同步效果的起点 | Evaluation |
| [同一飞车概念的双模型对比](#case-83) | 对比与评测 | 比较两条带标签的视频轨道，同时保留平台的对比口径 | Evaluation |

<a id="category-workflow"></a>
## 🛠️ 工作流与参考资料

<a id="case-1"></a>
### 案例 1: [科幻场景中的角色与环境参考](https://x.com/_lexers/status/2111014728160235719) (作者 [@_lexers](https://x.com/_lexers))

**观察独立角色表和环境表如何与长篇视频创作要求并列呈现**

视频展示沙漠世界、参考图与滚动 Prompt，全文尚未转录

[![科幻场景中的角色与环境参考](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D11/poster-c7f71e602146.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D11/video-c7f71e602146.mp4)

Type: Demo | Date: 2026-10-16

---

<a id="case-2"></a>
### 案例 2: [从 Agent 分镜到动画片段](https://x.com/z933TfmXkaISSVc/status/2111002792102158714) (作者 [@z933TfmXkaISSVc](https://x.com/z933TfmXkaISSVc))

**将作者的剧本、分镜、Prompt 串联方式用于短动画的前期规划**

作者自述用 Opus 5.5 写作，再以 Claude 和 MCP 生成，动画附件无法验证工具执行日志

[![从 Agent 分镜到动画片段](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D15/poster-a0d7f303f6cf.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D15/video-a0d7f303f6cf.mp4)

Type: Tutorial | Date: 2026-10-16

---

<a id="case-3"></a>
### 案例 3: [宏大奇幻场景的参考图表](https://x.com/dylannknox/status/2110984061569421429) (作者 [@dylannknox](https://x.com/dylannknox))

**观察角色表、环境表与长篇场景要求之间的对应关系**

组合展示中可见拱顶环境和滚动 Prompt，但完整文字尚未转录

[![宏大奇幻场景的参考图表](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D19/poster-225fcfcd6ec2.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D19/video-225fcfcd6ec2.mp4)

Type: Demo | Date: 2026-10-16

---

<a id="case-4"></a>
### 案例 4: [手机聊天界面中的视频任务](https://x.com/agi_aibusi/status/2110941943006118201) (作者 [@agi_aibusi](https://x.com/agi_aibusi))

**先观察作者提出的 Codex 到 MCP 衔接方式，再用自己的已验证工具复现**

录屏显示聊天和任务状态，作者讨论的订阅积分规则不代表通用 API 计费规则

[![手机聊天界面中的视频任务](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D28/poster-fbf3abad9feb.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D28/video-fbf3abad9feb.mp4)

Type: Tutorial | Date: 2026-10-16

---


<a id="category-ads"></a>
## 📦 广告与产品故事

<a id="case-5"></a>
### 案例 5: [起亚 SUV 的森林公路广告](https://x.com/Diplomeme/status/2110947179057811727) (作者 [@Diplomeme](https://x.com/Diplomeme))

**用公开的十五镜分镜，规划三十秒广告中的车辆连续性**

Prompt 依赖此处未提供的车辆参考图，其中的 4K 是指令要求，不是经核验的输出分辨率

[![起亚 SUV 的森林公路广告](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D26/poster-cf1e54b34518.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D26/video-cf1e54b34518.mp4)

**提示词** · [公开提示词来源](https://x.com/Diplomeme/status/2110947179057811727)

```
High-octane, hyper-realistic automotive commercial for the Kia Seltos, shot with the visual intensity of a Christopher Nolan-style cinematic production using actual 70mm IMAX cameras. Fast-paced multi-shot editing with quick, cinematic cuts timed at exactly one shot every 2 seconds across a complete 30-second timeline. The champagne-gold Kia Seltos, matching the exact vehicle design in the provided reference images, charges through a dense forest road surrounded by towering trees and dappled sunlight. High-contrast Nolan-esque color grading with deep shadows, cold teals, warm champagne-gold reflections, and bright highlights. Sunlight pierces through the forest canopy, reflecting across the sculpted bodywork, signature vertical LED daytime running lights, black front grille, muscular wheel arches, and distinctive rear light bar. Rapid sequence of intense cuts:•Shot 1 (0-2s): Ground-level cinematic establishing shot of an empty winding forest road, towering trees casting deep shadows as sunlight breaks through the canopy. The distant engine note of the approaching Kia Seltos builds tension.•Shot 2 (2-4s): Low eye-level tracking shot of the champagne-gold Kia Seltos emerging between the trees, accelerating along the forest road and revealing its bold front grille, distinctive vertical LED lighting signature, and commanding SUV stance.•Shot 3 (4-6s): Tight, detailed close-up of the front fascia, Kia emblem, illuminated LED daytime running lights, glossy black grille elements, and champagne-gold paint reflecting the passing forest.•Shot 4 (6-8s): Dramatic low-angle tracking shot moving alongside the front wheel as the alloy spokes spin rapidly, tires maintain realistic contact with the asphalt, and the SUV’s sculpted bodywork catches streaks of sunlight.•Shot 5 (8-10s): Fast lateral tracking shot revealing the complete side profile, muscular wheel arches, black lower-body cladding, door contours, windows, roofline, and metallic champagne-gold finish as the Kia Seltos sweeps through the forest.•Shot 6 (10-12s): Low-angle handheld-style camera whip-pan from the road surface to the SUV’s front three-quarter profile as it exits a sweeping bend, with realistic suspension movement, controlled body roll, and natural background motion blur.•Shot 7 (12-14s): Extreme close-up of sunlight traveling across the sculpted hood, Kia emblem, sharp body creases, and vertical LED lights, emphasizing precise automotive design and premium paint reflections.•Shot 8 (14-16s): Rear three-quarter tracking shot following the Kia Seltos through the forest, showcasing the distinctive rear light bar, angular vertical taillights, rear spoiler, sculpted tailgate, and authentic model badging.•Shot 9 (16-18s): Dynamic wheel-height tracking shot as the SUV drives across alternating patches of sunlight and shadow, capturing realistic tire rotation, subtle road texture, reflections along the lower doors, and the movement of the suspension over natural road undulations.•Shot 10 (18-20s): High-angle wide shot of the Kia Seltos commanding a sweeping forest road, surrounded by towering trees and atmospheric shafts of sunlight, with the winding asphalt leading the eye toward the moving SUV.•Shot 11 (20-22s): Fast front-facing tracking shot of the Kia Seltos approaching the camera along a straight section of forest road, its LED lights illuminated and grille dominating the frame as the camera smoothly retreats ahead of the vehicle.•Shot 12 (22-24s): Rapid cinematic transition into a close rear tracking angle as the SUV accelerates away through the trees, the rear lighting signature glowing against the darker forest and the road markings sweeping beneath the frame.•Shot 13 (24-26s): Dramatic low-angle front three-quarter hero shot as the Kia Seltos exits the forest bend and enters a naturally illuminated clearing, revealing its full stance, champagne-gold bodywork, alloy wheels, and signature front lighting.•Shot 14 (26-28s): Controlled cinematic orbit around the stationary Kia Seltos at a scenic forest-road pull-off, transitioning from the front three-quarter view toward the side and rear profile while the surrounding trees and golden sunlight create a premium automotive campaign atmosphere.•Shot 15 (28-30s): Hard cut to black with a final sweep of light revealing the KIA emblem followed by the SELTOS model name and the campaign tagline: “OWN EVERY TURN.” End with a powerful, clean, premium automotive advertising finish.Raw automotive documentary-style camera textures, organic lens flares, lifelike vehicle physics, authentic wheel rotation and tire contact, realistic suspension movement, natural road reflections, physically accurate metallic paint reflections, cinematic motion blur, subtle engine vibration, and an immersive forest-road atmosphere. Preserve the exact Kia Seltos identity, champagne-gold exterior color, front grille design, LED lighting signatures, alloy wheels, body proportions, side profile, and rear design from the provided reference images throughout every shot. Maintain consistent vehicle geometry, wheel design, lighting signatures, paint color, and branding across all 15 shots. No vehicle redesign, no morphing, no inconsistent body panels, no incorrect logos, no artificial CGI appearance, no impossible driving maneuvers, no exaggerated visual effects, and no abrupt changes in road geography. Ultra-detailed, 4K resolution, premium global automotive advertising quality.
```

Type: Demo | Date: 2026-10-16

---

<a id="case-6"></a>
### 案例 6: [多人物护肤品 UGC 广告拼贴](https://x.com/ErnestoSOFTWARE/status/2110917624167108665) (作者 [@ErnestoSOFTWARE](https://x.com/ErnestoSOFTWARE))

**参考可见广告形式，规划保留完整制作记录的 UGC 对照实验**

作者推介 Higgsfield MCP 并自述低成本，但未提供投放表现或账单证据

[![多人物护肤品 UGC 广告拼贴](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D37/poster-4ca47c0af310.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D37/video-4ca47c0af310.mp4)

Type: Demo | Date: 2026-10-16

---

<a id="case-7"></a>
### 案例 7: [迷你龙给甜点焦糖化](https://x.com/magnific/status/2111200639707668507) (作者 [@magnific](https://x.com/magnific))

**以一个明确的食物动作，观察角色驱动的产品故事**

平台自有样片把微型龙放在焦糖布蕾旁，不能证明销售表现

[![迷你龙给甜点焦糖化](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D76/poster-6f401168b0fb.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D76/video-6f401168b0fb.mp4)

Type: Demo | Date: 2026-10-16

---

<a id="case-8"></a>
### 案例 8: [橙汁纸盒的广告场景](https://x.com/leilamakes/status/2111108005567582329) (作者 [@leilamakes](https://x.com/leilamakes))

**围绕单一产品观察包装可见度、水果意象与转场**

来源把橙汁纸盒、水果和零售场景结合起来，没有公开 Prompt

[![橙汁纸盒的广告场景](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D85/poster-af7aa6745461.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D85/video-af7aa6745461.mp4)

Type: Demo | Date: 2026-10-16

---


<a id="category-story"></a>
## 🎬 角色与叙事

<a id="case-9"></a>
### 案例 9: [浅绿房间里的耳机女孩](https://x.com/iam_mian7/status/2110826299417854081) (作者 [@iam_mian7](https://x.com/iam_mian7))

**观察近景、全身动作与同一浅色场景中的角色外观**

绿发耳机女孩在浅绿室内改变姿态，镜头景别也随之变化

[![浅绿房间里的耳机女孩](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D03/poster-3305b566e9a1.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D03/video-3305b566e9a1.mp4)

Type: Demo | Date: 2026-10-15

---

<a id="case-10"></a>
### 案例 10: [走近古典柱廊的男子](https://x.com/lexx_aura/status/2111017349755043959) (作者 [@lexx_aura](https://x.com/lexx_aura))

**通过可见片段观察克制的动作和建筑环境连续性**

抽样画面显示男子与古典柱廊，不能用原帖宽泛的 CGI 赞美证明复杂动作能力

[![走近古典柱廊的男子](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D09/poster-e4099969039c.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D09/video-e4099969039c.mp4)

Type: Demo | Date: 2026-10-16

---

<a id="case-11"></a>
### 案例 11: [湿发女性的情绪近景](https://x.com/sophiaparkerr_/status/2110777323423400161) (作者 [@sophiaparkerr_](https://x.com/sophiaparkerr_))

**观察以对白表演为主的样片中细微的面部变化和构图**

画面集中于绿色暗光中的女性面部，未独立评分音频质量

[![湿发女性的情绪近景](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D14/poster-bd91c5962388.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D14/video-bd91c5962388.mp4)

Type: Demo | Date: 2026-10-15

---

<a id="case-12"></a>
### 案例 12: [电影院里的母女情绪瞬间](https://x.com/liluocheng13/status/2110981671243874346) (作者 [@liluocheng13](https://x.com/liluocheng13))

**观察短情绪场景如何依托一个具体的个人故事**

作者将 16 秒短片与旧日关系的回忆相连，并注明图像用 Gemini、视频用 Kling 4.0

[![电影院里的母女情绪瞬间](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D21/poster-59193966fd28.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D21/video-59193966fd28.mp4)

Type: Demo | Date: 2026-10-16

---

<a id="case-13"></a>
### 案例 13: [两位主播播报日语新闻](https://x.com/seisei_ai_1st/status/2110975778183942532) (作者 [@seisei_ai_1st](https://x.com/seisei_ai_1st))

**据此设计针对对白、双人调度和屏幕图文的专项测试**

作者讨论日语语音，画面核验只确认新闻演播室形式，未独立验证发音

[![两位主播播报日语新闻](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D23/poster-6d7a8b12e568.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D23/video-6d7a8b12e568.mp4)

Type: Demo | Date: 2026-10-16

---

<a id="case-14"></a>
### 案例 14: [办公大厅里的迷你卡丁车](https://x.com/PromptSin/status/2110943847706775742) (作者 [@PromptSin](https://x.com/PromptSin))

**通过把意外的交通工具放进日常建筑场景，观察喜剧性的比例反差**

作者标注使用 Kling 4 Flash，片段显示坐着的角色驾车穿过办公大厅

[![办公大厅里的迷你卡丁车](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D27/poster-df7aadba33d7.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D27/video-df7aadba33d7.mp4)

Type: Demo | Date: 2026-10-16

---

<a id="case-15"></a>
### 案例 15: [男友视角下的夏日散步](https://x.com/agi_aibusi/status/2110924173619138656) (作者 [@agi_aibusi](https://x.com/agi_aibusi))

**复制详细公开要求，以日常互动规划三十秒连续叙事**

Prompt 指定了一位女性的外观、六个定时片段、家用相机行为与环境声音

[![男友视角下的夏日散步](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D34/poster-8bef5187ff5c.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D34/video-8bef5187ff5c.mp4)

**提示词** · [公开提示词来源](https://x.com/agi_aibusi/status/2110924176890757483)

```
Create a 30-second video in 1920×1080, with the realism of an ordinary recording a boyfriend made of his girlfriend during a summer walk in Japan.

The small story:
They have no particular destination. She has just opened a can of fruit juice, and he starts recording without announcing it. Over the next half-minute, she gradually notices the camera, gets a little embarrassed, and begins including him in the moment. Their familiarity should come through in how she waits for him, looks at him, and closes the distance between them.

The woman:
A beautiful Japanese woman around 24 years old, with an approachable, individual face rather than a polished model appearance. Dark brown eyes, natural skin texture, light everyday makeup, and straight black hair loosely gathered in a low ponytail. A few short strands around her temples have escaped in the summer humidity.

She wears a faded navy cotton T-shirt, loose ivory trousers, comfortable gray sneakers, and a small rust-colored crossbody bag. A plain elastic hair tie is around one wrist. Keep her facial features, hair, outfit, bag, and proportions consistent in every shot.

Her expressions are understated and responsive. Sometimes she looks distracted or squints in the light. Her smile develops because of something between them, rather than appearing on cue.

The place:
A residential neighborhood in a regional Japanese city, near a narrow canal. Late afternoon in midsummer, with warm sunlight still reaching the upper parts of the houses.

Use ordinary local details: patched asphalt, short concrete bridges over the canal, metal railings warm from the sun, compact houses with tiled roofs, frosted entrance windows, outdoor air-conditioning units, bicycles tucked beside gates, and plants growing in mismatched pots. Utility wires cross the sky. A striped fabric awning hangs outside a closed shop farther down the street.

Avoid famous landmarks and postcard compositions. The location should feel like somewhere the couple already knows.

How the camera behaves:
The boyfriend holds a small consumer camera at his own eye or chest level. Most of the time he is beside her or only a step behind. The viewpoint should feel like her companion's attention, with no third-person shots of the couple.

Let framing respond to their interaction. When she suddenly looks at him, he may take a fraction of a second to correct the composition. When he laughs, the camera moves slightly. When they walk, his footsteps create a gentle, uneven rhythm.

Use ordinary consumer-camera rendering: restrained detail, modest dynamic range, occasional clipped highlights, a little shadow noise, and slight focus hesitation when she moves closer. Preserve natural skin color.

Keep the camera's attention on her face, gestures, and shared surroundings. Avoid fashion poses, body-scanning shots, elaborate camera moves, slow motion, or a glossy advertising finish.

Suggested edit — six short memories from the same walk:

0:00–0:05
She stands beside a low canal railing with a small, unbranded can of mandarin orange juice. The recording begins just as she finishes lifting the pull tab. She takes a sip, lowers the can, and notices that he is filming.

She looks directly at him with a briefly puzzled expression, then gives a small, amused smile, as though silently asking, “Really, you're filming this?”

Begin with a slightly loose frame that includes her hands and the canal, then let the boyfriend adjust it toward her face.

0:05–0:10
A cut to the two of them walking side by side along the narrow lane. She carries the can naturally in one hand.

She gets half a step ahead, realizes he has slowed down while filming, and turns back. Instead of posing, she waits with a mildly impatient but affectionate look. Once he catches up, she resumes walking beside him.

Her gaze should meet the person holding the camera, not an imaginary audience.

0:10–0:15
They pause near a house entrance where a small glass wind chime hangs beneath the eaves.

A breeze makes it ring. She glances upward and listens for a moment. Loose strands of hair move against her cheek; she brushes them aside with her free hand.

She notices him still watching her through the camera and suppresses a smile before looking back toward the wind chime.

Keep this moment quiet and unhurried.

0:15–0:20
On a short concrete bridge, she stops to look down at the canal. The camera first catches the rippling water, then tilts back toward her after she has already turned around.

She leans slightly toward him to see what he is recording. Her face briefly comes too close for the camera's focus, making her laugh softly and step back.

The laugh should feel like a shared interruption, with a small answering movement from the camera.

0:20–0:25
They rest beside the bridge in the shade. She is closer to the camera now, relaxed enough to stop paying attention to being filmed.

She takes another small sip of juice, then holds the can toward him as an offer. Leave the can clearly visible in the foreground, separate from her face.

He does not take it during the shot. She gives a tiny questioning lift of her eyebrows, then draws it back with an affectionate smile.

0:25–0:30
She steps toward him and gently touches his free forearm, inviting him to keep walking. Only a small, natural part of his arm may enter the lower edge of the frame.

As they start moving together, he lowers the camera. The view drifts from her smiling face to her bag, their moving shadows, and the sunlit pavement.

Let the last second settle on the overlapping shadows of two people walking close together. End with an ordinary recording stop, without a dramatic transition or title.

Sound:
Use the sound that would actually reach the camera microphone: cicadas, the juice can opening, a few footsteps, a wind chime, faint canal water, distant tires on the road, and their quiet laughter.

A single softly spoken Japanese remark such as “撮ってたの？” may occur when she first notices the camera, but speech is optional. Do not add explanatory dialogue.

No music, voiceover, or added dramatic sound effects.

Continuity and physical detail:
There is one juice can, carried by her throughout the sequence. Its color, size, opening, and remaining shape stay consistent. The crossbody strap stays on the same shoulder. Her ponytail remains tied.

Hands should hold objects with believable contact and weight. Walking speed, foot placement, shadows, and reflections must agree with the surroundings. Keep the canal, bridge, houses, sunlight direction, and summer weather coherent between cuts.

Emotional direction:
The viewer should feel that she knows and trusts the person behind the camera. Build that feeling through small changes in distance and attention: noticing him, waiting for him, leaning in, offering a drink, and asking him to walk beside her.

Let ordinary pauses remain. Her beauty is something her boyfriend happens to notice during their time together.

The finished video should feel like a personal memory he would keep because of the way she looked at him that afternoon.
```

Type: Demo | Date: 2026-10-16

---

<a id="case-16"></a>
### 案例 16: [车辆、士兵与人物近景合集](https://x.com/jerrod_lew/status/2110911158156931427) (作者 [@jerrod_lew](https://x.com/jerrod_lew))

**用蒙太奇挑出具体任务，再分别进行受控测试**

约 63 秒附件属于样片合集，不能据此认定单次原生生成时长

[![车辆、士兵与人物近景合集](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D39/poster-7d5e3845dc71.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D39/video-7d5e3845dc71.mp4)

Type: Demo | Date: 2026-10-16

---

<a id="case-17"></a>
### 案例 17: [King Cards 的魔术与城市飞行](https://x.com/tphuang/status/2110902762619933119) (作者 [@tphuang](https://x.com/tphuang))

**观察较长短片如何连接舞台魔术、纸质载具和反复出现的红鸟**

这段整片混剪也出现在后续账号的帖子中，相关剪段不当作独立电影计数

[![King Cards 的魔术与城市飞行](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D42/poster-cd1175d34d80.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D42/video-cd1175d34d80.mp4)

Type: Demo | Date: 2026-10-16

---

<a id="case-18"></a>
### 案例 18: [乡村女性与暴雨前的拖拉机](https://x.com/Bic_Revelation/status/2110847934346489947) (作者 [@Bic_Revelation](https://x.com/Bic_Revelation))

**观察角色、机器和天气如何传达简短的叙事前提**

来源将场景联系到国际农村妇女日，没有公开生成配方

[![乡村女性与暴雨前的拖拉机](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D47/poster-6a9f1d8d21de.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D47/video-6a9f1d8d21de.mp4)

Type: Demo | Date: 2026-10-15

---

<a id="case-19"></a>
### 案例 19: [恐龙冒险短片与可复用镜头要求](https://x.com/techhalla/status/2110806819937378773) (作者 [@techhalla](https://x.com/techhalla))

**对照成片与作者公开的七秒动作、八秒驾车要求进行学习**

两份 Prompt 卡片都保留为图片转录，内嵌参考缩略图不是独立输入原图

[![恐龙冒险短片与可复用镜头要求](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D50/poster-9890fdc58895.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D50/video-9890fdc58895.mp4)

作者回复图片：分镜、参考图与提示词卡片，内嵌缩略图不是原始参考文件

![作者回复图片：分镜、参考图与提示词卡片，内嵌缩略图不是原始参考文件 1](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/source-prompts/2110806822957273273-0.jpg)

![作者回复图片：分镜、参考图与提示词卡片，内嵌缩略图不是原始参考文件 2](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/source-prompts/2110806822957273273-1.jpg)

![作者回复图片：分镜、参考图与提示词卡片，内嵌缩略图不是原始参考文件 3](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/source-prompts/2110806826350412052-0.jpg)

![作者回复图片：分镜、参考图与提示词卡片，内嵌缩略图不是原始参考文件 4](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/source-prompts/2110806826350412052-1.jpg)

**提示词 1** · [公开提示词来源](https://x.com/techhalla/status/2110806822957273273)

```
OMNI REFERENCE · 16:9 · 7 s · 1080p · NATIVE AUDIO

A 7-second live-action action sequence with several fast hard cuts, real time speed, no slow
motion, energetic handheld camera. Location: the secret laboratory from Image1 with aquariums and
1980s computers, red alarm lights flashing, then a steel side door and the dark jungle outside at
night. Hannah is the woman in Image2, exactly as on her wardrobe sheet; use that image only for
her face, hair and costume. The attackers are punk thugs like the man in Image3: mohawks, purple
leather, studded wristbands. There is only ONE Hannah, never duplicated. 0-2s: tight close-up of
Hannah's face in the red flashing light as two punks grab her arms from both sides; she grits her
teeth. 2-3.5s: hard cut, medium shot: she stamps on one punk's foot, elbows the other in the face
and twists free, both stagger back into a rack of glass jars. 3.5-5s: hard cut: she sprints down
the lab between the aquariums, punks chasing behind her with flashlights. 5-6s: hard cut: she
slams through a steel side door marked only by a red bulb, out into the night. 6-7s: hard cut,
from the jungle looking back: she runs straight toward camera into the dark ferns and trees, the
lit doorway behind her, flashlight beams sweeping after her. Audio: alarm wailing, grunts, glass
smashing, footsteps, the door banging, jungle insects.

+ look: 1987 B-movie film stock, practical effects, film grain. No music, only SFX.
```

**提示词 2** · [公开提示词来源](https://x.com/techhalla/status/2110806826350412052)

```
OMNI REFERENCE · 16:9 · 8 s · 1080p · NATIVE AUDIO

An 8-second live-action sequence with a few hard cuts, real time speed, no slow motion, handheld
camera. The whole scene is at dawn: low orange sun, pale pink-grey sky, never a blue daytime sky.
Location: the smoking ruins of the laboratory compound from Image1, small fires still burning, a
dirt track leading out through a broken gate. The car is the battered black 1953 Cadillac
convertible from Image2, top down, parked in the smoke. Hannah is the woman in Image3, exactly as
on her wardrobe sheet. Use the reference images only for her face, costume and the car, never for
backgrounds. Hannah is completely alone: no other people, no animals, no dinosaurs anywhere in the
scene. 0-2s: Hannah walks through the smoke to the Cadillac and vaults over the closed driver's
door into the seat, the door stays shut. 2-4s: hard cut, close on Hannah: she turns the key, the
engine coughs and roars, she puts on a pair of sunglasses without a word. 4-6s: hard cut, low
angle by the rear wheel: the tire spins and kicks up dirt and gravel as the car lurches forward.
6-8s: hard cut, wide from the broken gate: the Cadillac drives away down the dirt track out of the
ruined compound into the dawn, dust and smoke trailing behind it. Audio: crackling fire, the
engine starting and revving, tires on gravel.

+ look: 1987 B-movie film stock, practical effects, film grain. No music, only SFX.
```

Type: Demo | Date: 2026-10-15

---

<a id="case-20"></a>
### 案例 20: [快递员打开通向异世界的电梯](https://x.com/PromptSin/status/2110790343298023798) (作者 [@PromptSin](https://x.com/PromptSin))

**观察固定主角如何对同一扇门外不断变化的环境作出反应**

黄制服快递员面对冰、水与火焰等反差场景

[![快递员打开通向异世界的电梯](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D53/poster-c385592b815a.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D53/video-c385592b815a.mp4)

Type: Demo | Date: 2026-10-15

---

<a id="case-21"></a>
### 案例 21: [地下乌龟水管工的喜剧场景](https://x.com/Starjupi/status/2110781205415104571) (作者 [@Starjupi](https://x.com/Starjupi))

**用作者的流程说明区分概念、角色设计、脚本、对白与声音决策**

评论链解释了流程和模型功能，但没有公开实际生成 Prompt

[![地下乌龟水管工的喜剧场景](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D58/poster-80ebae3e19ee.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D58/video-80ebae3e19ee.mp4)

Type: Demo | Date: 2026-10-15

---

<a id="case-22"></a>
### 案例 22: [以车辆意外收尾的街头追逐](https://x.com/_3912657840/status/2110778910019559744) (作者 [@_3912657840](https://x.com/_3912657840))

**通过人物动作、构图和街头状况变化观察喜剧节奏**

作者标注这是文生视频实验，但没有公开实际 Prompt

[![以车辆意外收尾的街头追逐](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D59/poster-32460fac82cb.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D59/video-32460fac82cb.mp4)

Type: Demo | Date: 2026-10-15

---

<a id="case-23"></a>
### 案例 23: [少女发现蓝龙的奇幻短片](https://x.com/nrqa__/status/2110764587113222208) (作者 [@nrqa__](https://x.com/nrqa__))

**观察个人奇幻故事如何形成包含固定角色的组合片段**

来源展示约 95 秒短片，不代表一次生成的时长

[![少女发现蓝龙的奇幻短片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D63/poster-e7d8328e9da0.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D63/video-e7d8328e9da0.mp4)

Type: Demo | Date: 2026-10-15

---

<a id="case-24"></a>
### 案例 24: [纸质载具驶入花城](https://x.com/Aiwithkami/status/2111121831528980566) (作者 [@Aiwithkami](https://x.com/Aiwithkami))

**观察 King Cards 短剪段中的人物、载具与环境变化**

这是同一长片中被重复分享的场景，不能算成另一部独立制作的电影

[![纸质载具驶入花城](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D66/poster-e0abfdd43b76.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D66/video-e0abfdd43b76.mp4)

Type: Demo | Date: 2026-10-16

---

<a id="case-25"></a>
### 案例 25: [纸质车厢里的石像变成人](https://x.com/AlexM12jx/status/2111165921364504890) (作者 [@AlexM12jx](https://x.com/AlexM12jx))

**观察移动载具内的角色位置与短暂形态变化**

片段同样被归于 King Cards，来源归属与原创作者身份的判断分别保留

[![纸质车厢里的石像变成人](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D69/poster-00ccb9224112.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D69/video-00ccb9224112.mp4)

Type: Demo | Date: 2026-10-16

---

<a id="case-26"></a>
### 案例 26: [魔术师与纸牌环绕的剧场](https://x.com/MelinaVale14/status/2111125493957505478) (作者 [@MelinaVale14](https://x.com/MelinaVale14))

**把中心人物表演、移动道具和周围观众作为同一场景观察**

King Cards 此段的不同编码与短版已合并

[![魔术师与纸牌环绕的剧场](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D70/poster-b5d7e24dfed1.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D70/video-b5d7e24dfed1.mp4)

Type: Demo | Date: 2026-10-16

---

<a id="case-27"></a>
### 案例 27: [庭院足浴中的女性日常](https://x.com/Naonekozamurai/status/2111231708108575006) (作者 [@Naonekozamurai](https://x.com/Naonekozamurai))

**观察普通手势、服装和安静环境，而非复杂动作**

作者自述十秒 1080p 的生成及积分数，并对是否为活动价表示不确定

[![庭院足浴中的女性日常](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D74/poster-c60960ec9979.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D74/video-c60960ec9979.mp4)

Type: Demo | Date: 2026-10-16

---

<a id="case-28"></a>
### 案例 28: [以猎鹰串联举报主题短片](https://x.com/fatoomdes/status/2111180507254042955) (作者 [@fatoomdes](https://x.com/fatoomdes))

**观察角色意象如何把手机界面镜头连接成一个主题表达**

作者将成片归于 Kling 4.0，本仓库不独立评判片中涉及的指控

[![以猎鹰串联举报主题短片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D79/poster-c65afae88005.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D79/video-c65afae88005.mp4)

Type: Demo | Date: 2026-10-16

---

<a id="case-29"></a>
### 案例 29: [厨房里蹑行的橘猫](https://x.com/magnific/status/2111139954440949990) (作者 [@magnific](https://x.com/magnific))

**观察日常室内环境中的小动作与镜头距离变化**

Magnific 样片跟随猫穿过台面，最后落到近景

[![厨房里蹑行的橘猫](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D82/poster-ff6f8d465033.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D82/video-ff6f8d465033.mp4)

Type: Demo | Date: 2026-10-16

---

<a id="case-30"></a>
### 案例 30: [两名男子在街角相见拥抱](https://x.com/leilamakes/status/2111108104452706636) (作者 [@leilamakes](https://x.com/leilamakes))

**观察简短社交互动中的接近、身体接触与角色位置**

该媒体来自较长会话中的作者回复，所属会话关系已经保留

[![两名男子在街角相见拥抱](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D83/poster-57f8a9708fd1.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D83/video-57f8a9708fd1.mp4)

Type: Demo | Date: 2026-10-16

---


<a id="category-action"></a>
## ⚔️ 动作与身体互动

<a id="case-31"></a>
### 案例 31: [月下云端双人剑斗](https://x.com/AiwithAmeliaa/status/2110782285691965754) (作者 [@AiwithAmeliaa](https://x.com/AiwithAmeliaa))

**用这段画面观察多人动作、空中调度与服装轮廓的连续性**

两名剑客在月下云层交锋，发帖账号明确披露了广告

[![月下云端双人剑斗](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D01/poster-c67c148695e9.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D01/video-c67c148695e9.mp4)

Type: Demo | Date: 2026-10-15

---

<a id="case-32"></a>
### 案例 32: [跆拳道馆内的双人格斗](https://x.com/Stevemnx3/status/2111039167090016566) (作者 [@Stevemnx3](https://x.com/Stevemnx3))

**对照格斗过程中的身体接触、双方距离与镜头位置**

画面在训练馆全景与两名着道服人物的近身动作间切换

[![跆拳道馆内的双人格斗](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D02/poster-1ef935905f1c.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D02/video-1ef935905f1c.mp4)

Type: Demo | Date: 2026-10-16

---

<a id="case-33"></a>
### 案例 33: [两辆跑车穿越城市追逐](https://x.com/PromptSin/status/2111042013210825211) (作者 [@PromptSin](https://x.com/PromptSin))

**观察快速切换镜位时车辆身份和运动方向的延续**

红黑两辆跑车在城市街道与桥面上竞逐

[![两辆跑车穿越城市追逐](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D04/poster-61e7dd165825.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D04/video-61e7dd165825.mp4)

Type: Demo | Date: 2026-10-16

---

<a id="case-34"></a>
### 案例 34: [移动镜头下的拳击交锋](https://x.com/SirGlavan_/status/2110785627251704302) (作者 [@SirGlavan_](https://x.com/SirGlavan_))

**观察出拳、防守位移与近身接触，不只看单张好看的画面**

两名戴拳套的拳手在擂台对打，镜头距离和角度不断变化

[![移动镜头下的拳击交锋](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D06/poster-0a6d9253b137.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D06/video-0a6d9253b137.mp4)

Type: Demo | Date: 2026-10-15

---

<a id="case-35"></a>
### 案例 35: [穿越爆炸街道的女战士](https://x.com/Lisa__Rodin/status/2110771984024129887) (作者 [@Lisa__Rodin](https://x.com/Lisa__Rodin))

**观察固定角色与行驶车辆、烟雾及大规模背景特效的关系**

黑衣女性穿过受损街道，这个场景的多个版本由不同账号重复分享

[![穿越爆炸街道的女战士](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D07/poster-e910366e89fb.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D07/video-e910366e89fb.mp4)

Type: Demo | Date: 2026-10-15

---

<a id="case-36"></a>
### 案例 36: [少女与城市巨兽对峙](https://x.com/torotoromoney/status/2111026942489329670) (作者 [@torotoromoney](https://x.com/torotoromoney))

**跟随城市中的冲突场景，比较人物和巨兽的体量关系**

浅发主角在损坏的建筑之间面对一只巨大触手生物

[![少女与城市巨兽对峙](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D08/poster-699eced69da0.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D08/video-699eced69da0.mp4)

Type: Demo | Date: 2026-10-16

---

<a id="case-37"></a>
### 案例 37: [穿过外星丛林的机械捕食者](https://x.com/Alin_Reaper05/status/2110996672343917052) (作者 [@Alin_Reaper05](https://x.com/Alin_Reaper05))

**用公开 Prompt 观察加速、环境反应和后退的手持视角**

生物结合金属肢体与有机组织，作者在直接回复中公开了生成指令

[![穿过外星丛林的机械捕食者](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D18/poster-e28f30cd8013.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D18/video-e28f30cd8013.mp4)

**提示词** · [公开提示词来源](https://x.com/Alin_Reaper05/status/2110996674558530007)

```
A living mechanical predator with a glowing orange central eye moves through dense alien jungle vegetation, using long metallic limbs wrapped in pulsing flesh to pull itself between trees, organic tendrils grabbing branches while hydraulic joints extend and retract, the creature suddenly notices the camera and rapidly charges forward, handheld tracking camera retreats through foliage, branches break naturally, mud splashes, vines react realistically, intense acceleration, realistic weight and momentum, dark cinematic lighting, high-end creature VFX.
```

Type: Demo | Date: 2026-10-16

---

<a id="case-38"></a>
### 案例 38: [骑手在战场上持长枪交锋](https://x.com/alifcoder/status/2110980799264903190) (作者 [@alifcoder](https://x.com/alifcoder))

**观察开阔战场中的骑手互动、马匹运动与武器接触**

附件展示的是骑马战斗，不把原帖关于拳击的描述直接当成这些画面的事实

[![骑手在战场上持长枪交锋](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D22/poster-98d16e333c2b.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D22/video-98d16e333c2b.mp4)

Type: Demo | Date: 2026-10-16

---

<a id="case-39"></a>
### 案例 39: [空手道交手与地垫接触](https://x.com/WuxiaRocks/status/2110962012100653419) (作者 [@WuxiaRocks](https://x.com/WuxiaRocks))

**观察表演者与周围环境的接触，不把动作仅看作孤立姿势**

作者特别指出脚压地垫的细节，这是来源观察，不是量化物理测试

[![空手道交手与地垫接触](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D24/poster-0a576d72f135.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D24/video-0a576d72f135.mp4)

Type: Demo | Date: 2026-10-16

---

<a id="case-40"></a>
### 案例 40: [便利店员工与格斗者交手](https://x.com/seisei_ai_1st/status/2110853231316496547) (作者 [@seisei_ai_1st](https://x.com/seisei_ai_1st))

**观察带日语对白的动作样例中的近身接触与场景连续性**

作者称对比时使用相同 Prompt，但该引用 Prompt 不在本次取得的来源集合中

[![便利店员工与格斗者交手](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D46/poster-1b049353be78.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D46/video-1b049353be78.mp4)

Type: Demo | Date: 2026-10-15

---

<a id="case-41"></a>
### 案例 41: [石台上的铠甲奇幻格斗](https://x.com/AIWarper/status/2110833050955526292) (作者 [@AIWarper](https://x.com/AIWarper))

**观察关键帧驱动的风格化战斗中的动作调度**

作者自述使用十个关键帧，可见片段为开阔平台上两名不同装甲人物的交手

[![石台上的铠甲奇幻格斗](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D48/poster-b680150c5bc2.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D48/video-b680150c5bc2.mp4)

Type: Demo | Date: 2026-10-15

---

<a id="case-42"></a>
### 案例 42: [猫咪穿越夜间城镇](https://x.com/umesh_ai/status/2110797373584887907) (作者 [@umesh_ai](https://x.com/umesh_ai))

**复制作者的一镜到底 Prompt，探索相连室内外空间中的快速运动**

作者后续解释为与 Flash 比较而选择二十秒，此参数没有补进原始 Prompt

[![猫咪穿越夜间城镇](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D51/poster-074081e6557c.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D51/video-074081e6557c.mp4)

**提示词** · [公开提示词来源](https://x.com/umesh_ai/status/2110797376827035806)

```
An amateur handheld recording in third-person perspective rapidly follows a cat through its nighttime adventures in one continuous shot, with no cuts, no stopping, and no pause. The sequence feels like fast-forward, showing all the curious, mischievous, funny, and chaotic things a cat might do while the town, house, garden, and everything around it are half-asleep.The cat races through about ten places a cat would naturally explore at night, each one flowing into the next in a single continuous chase: a quiet bedroom, a dim hallway, a kitchen, a living room, a backyard garden, a fence line, a garage, a rooftop, a tree, and a sleepy street or alley. The camera is shaky and imperfect, always struggling to keep up as it follows close behind. In every location, the cat causes some kind of chaos. In the bedroom it jumps onto furniture and disturbs sleeping people. In the hallway it sends small objects tumbling. In the kitchen it knocks items off the counter. In the living room it darts across shelves and tips things over. In the garden it rustles plants, digs, or startles birds. On the fence it rattles loose objects. In the garage it weaves through clutter and causes things to wobble or fall. On the rooftop it skids across surfaces and startles other animals. In the tree it shakes branches and scatters leaves. In the street or alley it darts through trash, shadows, and unexpected little messes, always leaving brief chaos behind before sprinting onward.The cat behaves like a restless, curious nighttime troublemaker: climbing, leaping, squeezing through gaps, chasing tiny movements, staring at strange things, swatting objects, knocking things over, and vanishing into corners before bursting back out again. Every scene should contain a clear action, reaction, or small disaster caused by the cat.Everything around it feels sleepy and still, with dark houses, quiet gardens, dim windows, silent rooftops, and empty streets. The contrast is that the cat is pure energy, moving so quickly that the world smears into motion blur and fragmented glimpses of chaos. The overall feeling is funny, lively, mischievous, and cinematic, like a whole secret night of cat behavior compressed into one rapid continuous chase.
```

Type: Demo | Date: 2026-10-15

---

<a id="case-43"></a>
### 案例 43: [雨中森林里的武士对决](https://x.com/AI__TSUBAKI/status/2110796958935978171) (作者 [@AI__TSUBAKI](https://x.com/AI__TSUBAKI))

**观察雨景格斗中的服装稳定性与武器接触**

作者自述十五秒、1080p、202 积分，这些是来源设置，不是当前 API 报价

[![雨中森林里的武士对决](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D52/poster-428a2ca3573f.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D52/video-428a2ca3573f.mp4)

Type: Demo | Date: 2026-10-15

---

<a id="case-44"></a>
### 案例 44: [树林中黑衣女性的动作片段](https://x.com/OxBairan/status/2110785228155560230) (作者 [@OxBairan](https://x.com/OxBairan))

**对照同一林间动作场景的不同编码版本，观察姿势与镜头运动**

多个账号重复使用这段场景的短剪辑，现已合并为一组素材

[![树林中黑衣女性的动作片段](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D56/poster-e86261e950fa.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D56/video-e86261e950fa.mp4)

Type: Demo | Date: 2026-10-15

---

<a id="case-45"></a>
### 案例 45: [红纸鸟对抗紫色章鱼](https://x.com/AIwithkhan/status/2111128321262276695) (作者 [@AIwithkhan](https://x.com/AIwithkhan))

**观察小型飞行主体与大型拼装生物之间的互动**

该场景也是 King Cards 剪段，多个账号配合近似模型发布话术分享

[![红纸鸟对抗紫色章鱼](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D67/poster-d6f35850335e.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D67/video-d6f35850335e.mp4)

Type: Demo | Date: 2026-10-16

---

<a id="case-46"></a>
### 案例 46: [篮球运动员飞身扣篮](https://x.com/leilamakes/status/2111108072236060864) (作者 [@leilamakes](https://x.com/leilamakes))

**观察身体轨迹、篮球位置与篮筐接触**

这段生成体育视频来自作者回复，不被当作独立验证的真实身体表现

[![篮球运动员飞身扣篮](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D84/poster-d1fcc959cdd5.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D84/video-d1fcc959cdd5.mp4)

Type: Demo | Date: 2026-10-16

---


<a id="category-game"></a>
## 🎮 游戏与载具概念

<a id="case-47"></a>
### 案例 47: [赏金猎人风格的游戏概念](https://x.com/NyaiiBubu/status/2111040233387200905) (作者 [@NyaiiBubu](https://x.com/NyaiiBubu))

**将片段作为结合人物动作和对白的游戏预告场景参考**

作者称其为 AAA 风格概念，实际可见产物是生成视频，并非可玩的游戏

[![赏金猎人风格的游戏概念](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D05/poster-96e6493c7d87.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D05/video-96e6493c7d87.mp4)

Type: Demo | Date: 2026-10-16

---

<a id="case-48"></a>
### 案例 48: [飞车冲上夜间巨型坡道](https://x.com/higgsfield_ai/status/2110937478492479783) (作者 [@higgsfield_ai](https://x.com/higgsfield_ai))

**将片段用作电影化车辆概念参考，不当作游戏已经可运行的证据**

带平台品牌的样片跟随汽车爬上陡坡，随后呈现腾空效果

[![飞车冲上夜间巨型坡道](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D29/poster-9f0ea0939850.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D29/video-9f0ea0939850.mp4)

Type: Demo | Date: 2026-10-16

---

<a id="case-49"></a>
### 案例 49: [日落海岸公路上的跑车竞速](https://x.com/higgsfield_ai/status/2110928479734964409) (作者 [@higgsfield_ai](https://x.com/higgsfield_ai))

**观察竞速视频概念中的追逐镜头、光线和仪表式叠层**

平台样片呈现日落海岸赛车场景，没有提供可执行游戏

[![日落海岸公路上的跑车竞速](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D31/poster-94729ec66a60.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D31/video-94729ec66a60.mp4)

Type: Demo | Date: 2026-10-16

---

<a id="case-50"></a>
### 案例 50: [战斗机飞越海岛环境](https://x.com/higgsfield_ai/status/2110925937634410612) (作者 [@higgsfield_ai](https://x.com/higgsfield_ai))

**用样片观察飞行镜头的运动和游戏界面构图**

喷气战机掠过明亮海岸，画面采用游戏式镜位与叠层

[![战斗机飞越海岛环境](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D33/poster-06b6b22e3e0e.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D33/video-06b6b22e3e0e.mp4)

Type: Demo | Date: 2026-10-16

---

<a id="case-51"></a>
### 案例 51: [角色在浮空岛之间滑翔](https://x.com/higgsfield_ai/status/2110922885141606859) (作者 [@higgsfield_ai](https://x.com/higgsfield_ai))

**观察第三人称视频概念从狭窄空间转入宽阔空景的方式**

平台展示角色穿越风格化浮空岛环境的跟随镜头

[![角色在浮空岛之间滑翔](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D35/poster-41fca9f81d16.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D35/video-41fca9f81d16.mp4)

Type: Demo | Date: 2026-10-16

---

<a id="case-52"></a>
### 案例 52: [跟随骑手的摩托竞速概念](https://x.com/higgsfield_ai/status/2110915957833248859) (作者 [@higgsfield_ai](https://x.com/higgsfield_ai))

**观察游戏式视频中的摩托动作、追逐镜头距离与赛道照明**

平台样片采用竞速游戏的展示形式，并非交互式应用

[![跟随骑手的摩托竞速概念](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D38/poster-6fbf86005055.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D38/video-6fbf86005055.mp4)

Type: Demo | Date: 2026-10-16

---

<a id="case-53"></a>
### 案例 53: [第一人称港口射击场景](https://x.com/higgsfield_ai/status/2110905436371370009) (作者 [@higgsfield_ai](https://x.com/higgsfield_ai))

**复制作者按时间分段的战术射击要求，定义十五秒视觉目标**

回复写 15 秒，根帖写 30 秒，附件约 14.3 秒，这三种来源口径分别保留

[![第一人称港口射击场景](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D41/poster-d66668c4a4fe.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D41/video-d66668c4a4fe.mp4)

**提示词** · [公开提示词来源](https://x.com/higgsfield_ai/status/2110906696851955916)

```
15-second horizontal 16:9 1080p first-person gameplay recording of a competitive 5v5 tactical shooter in team elimination mode, captured straight from a PC screen. Modern next-gen competitive shooter graphics: bright, clean, readable daylight, crisp PBR materials, high frame rate, sharp image. Pure first-person view: the player's hands in purple tactical gloves hold an original assault rifle with a flashy custom skin of hot-pink and teal graffiti patterns, positioned in the lower right of the frame. Clean screen with the HUD turned off: the only on-screen element is a small green crosshair in the center. There is no minimap, no kill feed, no health, ammo or money counters, no timer and no banners. Snappy competitive movement with quick peeks, crouching, strafing and precise flicks. The whole video is one continuous round with no cinematic cuts.

Setting: a sunny Asian harbor market district at midday, an original competitive map. There are narrow alleys between stacked, faded red, blue and yellow shipping containers, sun-bleached concrete, stalls with colorful canvas tarps and hanging paper lanterns, food carts, wooden crates and fish barrels, metal stairs and catwalks, corrugated metal walls, an open harbor basin of deep blue-green water with moored wooden fishing boats and floating pontoons, cranes on the docks in the background, and colorful painted shop signs made of abstract shapes, not letters. Bright high sun, clear blue sky with a few clouds, hard crisp shadows, seagulls in the distance and sunlight glittering on the water.

[00:00–00:02] The player strafes out from behind a shipping container, flicks onto an enemy soldier at the alley entrance and drops him with a short burst. The enemy ragdolls onto the concrete.
[00:02–00:04] He sprints along the containers, wide-swings around a stack of crates and drops an enemy hiding behind them with a quick two-shot tap.
[00:04–00:06] He jiggle-peeks the corner of a market stall and lands a clean headshot on an enemy on the catwalk.
[00:06–00:08] He hops down from the pier onto a floating wooden pontoon at the edge of the harbor basin and casually reloads with a fast magazine swap while moving along the planks.
[00:08–00:10] He advances along the pontoons between moored wooden fishing boats and taps an enemy standing on a boat deck. The body ragdolls off the deck and drops into the water with a splash.
[00:10–00:11] He throws a smoke grenade ahead onto the dock. It bounces across the wooden planks, then pops, and thick grey smoke spreads over the pier in the sunlight.
[00:11–00:13] Two enemies push out of the smoke along the dock. He sprays and taps them down; bullet impacts kick up wood splinters from the planks and small splashes in the water. Both enemies ragdoll onto the dock.
[00:13–00:15] The round is won. Standing alone on the pontoon in the middle of the harbor, he glances down at the sunlit water lapping against the boards, then looks back up and inspects his rifle with a stylish flip animation.

Style: authentic competitive esports gameplay footage that looks like a real ranked match caught on stream, with confident, clean play. Readable action, stable first-person camera with natural view bob and recoil, sharp, high detail, bright saturated daylight colors. No real-world text, no words, no brand logos, no watermark, no IP characters or maps.

Audio: competitive shooter sound design, with punchy rifle bursts with echo off the containers, shell casings clinking on concrete and wood, footsteps on concrete and hollow wooden planks, bullet impacts on wood and metal with small water splashes, a smoke grenade hiss, a crisp magazine reload, seagulls, lapping water against the boats, distant harbor horns and a short round-win sting at the end. No dialogue.
```

Type: Demo | Date: 2026-10-16

---

<a id="case-54"></a>
### 案例 54: [未来城市中的飞行汽车](https://x.com/YapayZekaSerisi/status/2111104253817155607) (作者 [@YapayZekaSerisi](https://x.com/YapayZekaSerisi))

**通过概念画面观察街面驾驶、飞行和城市地标之间的转换**

可见产物为未来交通视频，来源未提供可玩的游戏

[![未来城市中的飞行汽车](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D72/poster-78d337068f01.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D72/video-78d337068f01.mp4)

Type: Demo | Date: 2026-10-16

---

<a id="case-55"></a>
### 案例 55: [警车追逐穿城飞车](https://x.com/higgsfield_ai/status/2111235977406763103) (作者 [@higgsfield_ai](https://x.com/higgsfield_ai))

**观察追逐镜头概念如何结合地面车流与腾空动作**

Higgsfield 将其展示为平台上的另一个 Kling 4.0 游戏概念例子

[![警车追逐穿城飞车](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D73/poster-d291f74977e7.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D73/video-d291f74977e7.mp4)

Type: Demo | Date: 2026-10-16

---

<a id="case-56"></a>
### 案例 56: [海滨驾驶转入直升机飞行](https://x.com/frameo_ai/status/2111097408633639000) (作者 [@frameo_ai](https://x.com/frameo_ai))

**观察跑车、步行人物和空中镜头之间的转换**

Frameo 展示的是游戏式视频概念和接入预告，并非可执行游戏

[![海滨驾驶转入直升机飞行](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D87/poster-31d433ad4429.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D87/video-31d433ad4429.mp4)

Type: Demo | Date: 2026-10-16

---


<a id="category-animation"></a>
## 🎨 动画与风格化角色

<a id="case-57"></a>
### 案例 57: [插画与实拍风格交织的音乐视频](https://x.com/IntLab0000/status/2111016713869463957) (作者 [@IntLab0000](https://x.com/IntLab0000))

**观察完整 MV 如何结合不同风格和反复出现的情绪意象**

作者自述使用 MCP 辅助制作，约 136 秒的附件是组合成片，不是单次生成时长的证明

[![插画与实拍风格交织的音乐视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D10/poster-32d9ded7f2d0.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D10/video-32d9ded7f2d0.mp4)

Type: Demo | Date: 2026-10-16

---

<a id="case-58"></a>
### 案例 58: [厨房里的奶奶与迷你黏土龙](https://x.com/higgsfield_ai/status/2110927330390790226) (作者 [@higgsfield_ai](https://x.com/higgsfield_ai))

**观察紧凑厨房动画中的角色互动与材质风格**

画面结合微型龙、烹饪物件和黏土质感的视觉处理

[![厨房里的奶奶与迷你黏土龙](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D32/poster-1098bee49c56.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D32/video-1098bee49c56.mp4)

Type: Demo | Date: 2026-10-16

---

<a id="case-59"></a>
### 案例 59: [夜市摊位上的动漫厨师](https://x.com/higgsfield_ai/status/2110922265340891255) (作者 [@higgsfield_ai](https://x.com/higgsfield_ai))

**观察短篇烹饪动画中的手部动作、道具与照明**

平台自有样片展示一位插画风格厨师在热闹摊位前工作

[![夜市摊位上的动漫厨师](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D36/poster-a89dc333a50c.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D36/video-a89dc333a50c.mp4)

Type: Demo | Date: 2026-10-16

---

<a id="case-60"></a>
### 案例 60: [微缩人物的定格风格战斗](https://x.com/higgsfield_ai/status/2110910617574121905) (作者 [@higgsfield_ai](https://x.com/higgsfield_ai))

**观察微缩比例和定格风格如何塑造短动作片段**

小武士对抗红色生物，生成耗时说法仍属于平台自述

[![微缩人物的定格风格战斗](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D40/poster-0096a333b2d9.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D40/video-0096a333b2d9.mp4)

Type: Demo | Date: 2026-10-16

---

<a id="case-61"></a>
### 案例 61: [发光月牙座椅上的睡眠场景](https://x.com/minuitIA/status/2110823653336027226) (作者 [@minuitIA](https://x.com/minuitIA))

**用场景观察装饰性光线主题与轻微人物动作**

创作者把睡前人物意象延展为一段月亮主题的短视觉片段

[![发光月牙座椅上的睡眠场景](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D49/poster-cadca8a36e4a.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D49/video-cadca8a36e4a.mp4)

Type: Demo | Date: 2026-10-15

---

<a id="case-62"></a>
### 案例 62: [城市路口的快闪群舞](https://x.com/seisei_ai_1st/status/2110790316584562789) (作者 [@seisei_ai_1st](https://x.com/seisei_ai_1st))

**观察街舞片段中的群体动作、空间排列与视角变化**

作者用经常测试的快闪题材展示新模型效果

[![城市路口的快闪群舞](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D54/poster-0f0e0bc769b1.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D54/video-0f0e0bc769b1.mp4)

Type: Demo | Date: 2026-10-15

---

<a id="case-63"></a>
### 案例 63: [暴风云下的动漫剑客对决](https://x.com/Dani__oros/status/2110790297458544971) (作者 [@Dani__oros](https://x.com/Dani__oros))

**观察风格化格斗中清晰的人物轮廓与兵刃互动**

作者称这是用较模糊 Prompt 完成的初次测试，但未在根帖公开该 Prompt

[![暴风云下的动漫剑客对决](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D55/poster-28acdf9e07a3.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D55/video-28acdf9e07a3.mp4)

Type: Demo | Date: 2026-10-15

---

<a id="case-64"></a>
### 案例 64: [黑白舞台上的多人舞蹈](https://x.com/MO_IAI/status/2110784427408105640) (作者 [@MO_IAI](https://x.com/MO_IAI))

**在去除色彩的条件下观察编舞与灯光**

来源展示多位舞者与不断变化的队形组合

[![黑白舞台上的多人舞蹈](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D57/poster-0bf2843739e2.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D57/video-0bf2843739e2.mp4)

Type: Demo | Date: 2026-10-15

---

<a id="case-65"></a>
### 案例 65: [森林里玩雪的松鼠](https://x.com/fAIkout/status/2110768302851342454) (作者 [@fAIkout](https://x.com/fAIkout))

**观察富于表情的动物动作与统一的柔和动画风格**

创作者样片跟随小松鼠和积雪、林间物件互动

[![森林里玩雪的松鼠](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D62/poster-c2c730ddad9a.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D62/video-c2c730ddad9a.mp4)

Type: Demo | Date: 2026-10-15

---

<a id="case-66"></a>
### 案例 66: [红衣人物穿过糖果世界](https://x.com/jji1jj/status/2111165487648301173) (作者 [@jji1jj](https://x.com/jji1jj))

**观察风格化人物动作与由甜点构成的环境**

这是 King Cards 中视觉不同的场景研究，不是另一部独立制作的电影

[![红衣人物穿过糖果世界](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D71/poster-f533cc90221d.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D71/video-f533cc90221d.mp4)

Type: Demo | Date: 2026-10-16

---

<a id="case-67"></a>
### 案例 67: [戴王冠的白猫吃咖喱](https://x.com/craftcapitallab/status/2111200513924731150) (作者 [@craftcapitallab](https://x.com/craftcapitallab))

**观察服装、食物道具与表情如何支撑动物角色短故事**

作者把王冠白猫与咖喱结合，片尾使用装饰性标题

[![戴王冠的白猫吃咖喱](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D77/poster-0c65da3cad85.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D77/video-0c65da3cad85.mp4)

Type: Demo | Date: 2026-10-16

---


<a id="category-world"></a>
## 🌍 世界场景与生物

<a id="case-68"></a>
### 案例 68: [从森林旅程转入骑龙飞行](https://x.com/Lianaalane/status/2110953699250151850) (作者 [@Lianaalane](https://x.com/Lianaalane))

**观察画面如何从封闭树林逐步展开为空中远景**

人物骑龙从森林飞向山谷，同一片段的重复编码版本已合并

[![从森林旅程转入骑龙飞行](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D13/poster-ea2c6c571381.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D13/video-ea2c6c571381.mp4)

Type: Demo | Date: 2026-10-16

---

<a id="case-69"></a>
### 案例 69: [恐怖蒙太奇中的无面人形](https://x.com/h_ashizawaJP/status/2110999675709034742) (作者 [@h_ashizawaJP](https://x.com/h_ashizawaJP))

**观察怪物形象的连续性及不同诡异意象之间的转场**

苍白人形、扭曲面孔和昏暗树林对应作者关于生成音效与后期混音的讨论

[![恐怖蒙太奇中的无面人形](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D16/poster-f97b54673926.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D16/video-f97b54673926.mp4)

Type: Demo | Date: 2026-10-16

---

<a id="case-70"></a>
### 案例 70: [苏醒的球形外星聚落](https://x.com/Alin_Reaper05/status/2110997688682770563) (作者 [@Alin_Reaper05](https://x.com/Alin_Reaper05))

**复制作者公开的 Prompt，探索虚构小镇中多种环境运动的配合**

回复指定了旋转机械房屋、有机管道、小机器人、浅水及上升镜头

[![苏醒的球形外星聚落](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D17/poster-0727879b80e3.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D17/video-0727879b80e3.mp4)

**提示词** · [公开提示词来源](https://x.com/Alin_Reaper05/status/2110997691274580344)

```
A colorful alien settlement filled with enormous spherical buildings and bizarre organic machines comes alive at sunrise, round red mechanical houses rotate their giant lens-like windows, pipes expand and contract like breathing organs, small robotic creatures run through shallow water, flying vehicles weave between towers, camera glides smoothly through the town at ground level before rising above the rooftops, puddles reflecting neon lights and clouds, natural vegetation moving in the wind, playful but believable extraterrestrial world, cinematic photorealism.
```

Type: Demo | Date: 2026-10-16

---

<a id="case-71"></a>
### 案例 71: [外星巨兽涉过浅水湖](https://x.com/Alin_Reaper05/status/2110982741491904596) (作者 [@Alin_Reaper05](https://x.com/Alin_Reaper05))

**复制作者的 Prompt，探索体重、水面反应和缓慢升镜**

两只长颈巨兽穿过青绿色水面，周围是红色植被与黄绿色天空

[![外星巨兽涉过浅水湖](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D20/poster-51289a03af36.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D20/video-51289a03af36.mp4)

**提示词** · [公开提示词来源](https://x.com/Alin_Reaper05/status/2110982744247353611)

```
Two enormous long-necked alien animals slowly walk through a shallow turquoise lagoon surrounded by bright red grass and exotic palm forests. Their massive bodies create realistic waves and splashes with every step while smaller creatures flee along the shoreline. The camera begins low near the water and smoothly cranes upward, revealing the gigantic animals against a glowing yellow-green sky and distant mountains. Realistic weight and inertia, detailed skin movement, volumetric mist, natural vegetation motion, cinematic alien wildlife documentary, smooth continuous camera movement, highly coherent anatomy.
```

Type: Demo | Date: 2026-10-16

---

<a id="case-72"></a>
### 案例 72: [巨型机甲从甲板起飞](https://x.com/PDyv9gdatT4132/status/2110948121295696380) (作者 [@PDyv9gdatT4132](https://x.com/PDyv9gdatT4132))

**观察机械关节、体量与从站立转入飞行的过程**

作者发布的样片展示大型机器人启动并从舰船式甲板升起

[![巨型机甲从甲板起飞](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D25/poster-621b9b81c745.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D25/video-621b9b81c745.mp4)

Type: Demo | Date: 2026-10-16

---

<a id="case-73"></a>
### 案例 73: [巨兽逼近拥堵的悬索桥](https://x.com/jji1jj/status/2110775129043320994) (作者 [@jji1jj](https://x.com/jji1jj))

**观察暴雨环境中巨兽、车辆和人群之间的比例关系**

后续帖子复用了同一画面，保留为补充来源而不是新案例

[![巨兽逼近拥堵的悬索桥](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D60/poster-cdf43480c9f5.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D60/video-cdf43480c9f5.mp4)

Type: Demo | Date: 2026-10-15

---

<a id="case-74"></a>
### 案例 74: [报纸载具穿越纸质城市](https://x.com/Gemalpha_88/status/2111113629919854891) (作者 [@Gemalpha_88](https://x.com/Gemalpha_88))

**观察折纸风城市中的环境材质一致性与跟随镜头**

画面来自被重复分享的 King Cards，并非另一项独立验证的制作项目

[![报纸载具穿越纸质城市](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D68/poster-692aeb10394f.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D68/video-692aeb10394f.mp4)

Type: Demo | Date: 2026-10-16

---

<a id="case-75"></a>
### 案例 75: [山坡上的重型步行机甲](https://x.com/ojiji2025/status/2111218605069365688) (作者 [@ojiji2025](https://x.com/ojiji2025))

**观察机械运动、地面接触与超大武器之间的关系**

创作者分享首次机甲尝试，并非有工程文档支持的模拟

[![山坡上的重型步行机甲](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D75/poster-dd1ae88aa463.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D75/video-dd1ae88aa463.mp4)

Type: Demo | Date: 2026-10-16

---

<a id="case-76"></a>
### 案例 76: [哥特人物穿行雨夜](https://x.com/fabulatenebris/status/2111183079955951804) (作者 [@fabulatenebris](https://x.com/fabulatenebris))

**观察氛围、轮廓和反复出现的视觉主题**

来源呈现带昏暗人物与城堡式环境的风格化雨夜作品

[![哥特人物穿行雨夜](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D78/poster-6a014db111fa.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D78/video-6a014db111fa.mp4)

Type: Demo | Date: 2026-10-16

---

<a id="case-77"></a>
### 案例 77: [纸质车厢进入发光菌菇隧道](https://x.com/Hope_Ai01/status/2111146114972058097) (作者 [@Hope_Ai01](https://x.com/Hope_Ai01))

**观察画面如何从受限的车厢视角转入明亮环境**

这是另一个 King Cards 剪段，相关来源关系已经保留

[![纸质车厢进入发光菌菇隧道](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D81/poster-9d22c4d4055d.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D81/video-9d22c4d4055d.mp4)

Type: Demo | Date: 2026-10-16

---


<a id="category-evaluation"></a>
## 🔬 对比与评测

<a id="case-78"></a>
### 案例 78: [同一森林格斗 Prompt 的双模型对比](https://x.com/AibeginnerR8/status/2110935157503041672) (作者 [@AibeginnerR8](https://x.com/AibeginnerR8))

**比较两路显示结果，同时保留作者声明的设置和评价边界**

两路都标注 720p，并使用 Kling 音频；作者在本例中认为 Seedance 更遵循分镜、时长与动作要求

[![同一森林格斗 Prompt 的双模型对比](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D30/poster-a0590043e48c.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D30/video-a0590043e48c.mp4)

**提示词** · [公开提示词来源](https://x.com/AibeginnerR8/status/2110935160434610592)

```
参照素材
参照画像1 ：兜なしのドワーフA。顔、体格、髭、髪、衣服の基準。
参照画像2 ：角兜のドワーフB。顔、体格、髭、髪、衣服、兜の基準。
参照画像3 ：森の景観、植生、色、光、雰囲気の基準。
人物写真は同一性と衣装に使う。最初から森にいるAのアップで始め、写真の白背景や直立ポーズは引き継がない。

実写映画調、30秒、全8ショット。2人の重く頑丈なドワーフが、速い拳と脚の攻防を連続させる。4秒以降は、攻撃を受け流す動きが反撃になり、蹴りを外す踏み替えが次の接近になる。打った側もかわした側も足を動かし続け、相手の反応を次の攻撃へつなぐ。顔だけの反応カットや、腕を触れ合わせて待つ時間を挟まず、手足と相手の応答が読める距離から撮る。短い踏ん張りの間にも、拳、肩、足運びのいずれかが次の攻防へ動き続ける。通常速度。

薄暗い針葉樹の森。高い幹、深緑のシダ、苔むした根、落ち葉の地面。戦う通路の脇に太い幹と露出した根がある。前半と後半で同じ根を使う。自然な皮膚、革と布、重い髭の揺れ、柔らかな森の光。
開始時はAが画面左、Bが画面右で向かい合い、それぞれ相手を見る。カメラは2人を結ぶ軸の同じ側を保つ。以後の手足の左右は、その人物自身の身体を基準にする。

SHOT 1｜0〜2秒：Aの挑発
顔と右手が入る胸上のアップ。AはBを見て、掌を上に向け、指を小さく2回曲げて招く。口元に薄い笑み。手招きしながら、かすれた軽い声で「グラ・ドゥン！」と短く言う。発声は約0.6〜1.4秒。2秒でBのアップへ切り替える。

SHOT 2｜2〜4秒：Bの返答と加速
角兜と顔が入るBの胸上のアップ。Aを見て、口の片側を上げてにやりと笑う。低く太い声で「バル・ガッ！」。発声は約2.5〜3.3秒。語尾に肩を前へ倒して地面を蹴り、Aへ踏み出す。その加速の途中で4秒の全身アクションへ切る。

SHOT 3｜4〜8秒：拳のラリーから低い蹴り
Aの肩越しに、Bが同じ突進の続きで奥から急接近。カメラが両者の足まで入る画へ広がる。
Bの左の短い拳をAが右手で外へ払い、続くBの右ストレートをAが左前腕で逸らす。Aは空いた右拳をBの胴へ返し、Bが左肘を締めて受ける。Bの右フックをAが低くくぐり、抜ける勢いでAが右の低い蹴りを出す。Bは狙われた前足を引いて外し、蹴りの通過とともに踏み直して再接近。拳、低い回避、蹴り、踏み直しを一続きに見せる。

SHOT 4｜8〜12秒：押されながらも打ち返す
斜め横からの全身追従。8〜10秒、Bが左の拳から右の胴打ちへつなぎ、Aが左右の前腕で処理しながら下がる。Aは受けた直後に左拳をBの脇腹へ返し、Bが肘を下げて遮る。
10〜12秒、Bが低い蹴りを出す。Aは狙われた足を引いて外すが、Bは蹴った足の着地から肩を押し込む。Aは一歩滑り、後ろ足の踵を露出した根に当てて支える。足が止まる短い瞬間にも、AはBの押す腕を外へずらし、反撃を始める。Aの眉と口元が力み、Bは息を吐いて圧力をかける。接触点、双方の足、根を同じ画面に入れる。

SHOT 5｜12〜17秒：攻防しながら幹の脇へ移動
斜め前から下がりながら捉える。Aは根を蹴り、左前腕でBの右腕を外へ押し、右拳で胴へ反撃。Bは左腕で受け、右肘を返す。Aは左前腕で遮りながら頭を攻撃線の外へ移す。Aが続けて左の前蹴りを出すと、Bは胴を引いて半歩下がる。Aが蹴り脚を下ろすのに合わせ、Bが右拳で追い、Aはその外を抜けて幹の脇へ進む。Bも追い、左手をAの右前腕へ伸ばす。
カメラはこの移動中に緩やかに腰の高さへ下がり、2人の全身を保つ。
17秒前後、既にある手前の太い幹のすぐ脇をカメラが滑らかに通過する。樹皮が画面左から右へ素早く流れ、画面全体を約0.1秒だけ覆う。全体の通過は約0.3秒。全面が樹皮に覆われた中で、1回だけマスクカットする。遮蔽前後でカメラの高さ、人物の大きさ、幹の流れる方向と速度をそろえる。2人は移動を続け、Bの手はまだAをつかまない。

SHOT 6｜17〜22秒：つかみをほどき、立ったまま反撃
同じ方向へ流れる幹の縁が抜け、同じ軸側、同じ高さの低い斜め前の全身画へつながる。Aが先、Bが追う位置、身体の向き、歩幅、勢いを継続。画面が開くと同時に攻防が続き、見せ直しの静止を挟まない。
17〜19秒、Bの左手がAの右前腕をつかむ。Aは踏み込みながら右肘を返してつかみを外し、空いている左拳をBの胴へ返す。Bが右前腕で遮り、すぐ右の短いアッパーを返す。Aは後ろ足で支えて上体を外し、その戻る勢いで左膝をBの腹へ突き上げる。Bは腰を引いて外す。
19〜22秒、Aが左脚を下ろした瞬間、Bがその前足へ低い足払い。Aは前足を引いて空振りさせ、反対の足で身体を支える。引いた足を斜め前へ踏み直し、Aが右拳を返す。Bは左前腕で受け、さらに踏み込む。Aは立ったまま相手を見て後退し、同じ根の位置へ誘う。両者の手は相手への打撃、防御、短いつかみに使う。この区間は脚を引く回避と踏み替えでつなぎ、地面を叩く動作を入れない。

SHOT 7｜22〜27秒：連打の圧力を投げへ変える
斜め横の全身ショット。Bが左右の短い拳で押し込み、Aは受け流しながら一歩ずつ根へ下がる。Aが身体を少し開くと、Bが肩から再突進。
Aは後ろ足で根を押し、左手でBの右前腕を取り、右腕でBの上体を制御する。根に当てた踵から支持を移し、Bの進路へ腰を入れて回る。Bの前進が横方向の投げへ変わり、落ち葉の上へ落下する。Aは着地に合わせて腕を解放し、そのまま足を運んで追う。踏ん張り、支持の移動、腰の回転、Bの落下と着地を同じショットで見せ切る。

SHOT 8｜27〜30秒：倒れたBから即座に反撃
Bの低い後方斜めからAを見る。Bは着地の勢いで転がり、片手と片膝で身体を起こしながら、詰めてきたAへ低い足払いを返す。Aは小さく跳び越え、脚の軌道の外へ着地。着地からAが右拳を出し、Bが立ち上がりながら左前腕で受ける。Bの目に警戒と闘志。カメラはBとともに上がり、互いが次の一歩を踏み込むところで終了。

音声・BGM
セリフは意味を定めない短いドワーフ語風の創作音。AとBの声を区別し、発声する本人の口と合わせる。セリフは冒頭の各ひと言だけ。
約144 BPMの荒々しいファンタジー戦闘のインストゥルメンタル。低いフレームドラム、乾いた木製打楽器、短く刻む低弦。0〜4秒は薄く敷いて声を前に出し、4秒の突進から速い刻みを立ち上げる。12〜22秒は低弦の反復を重ね、マスクカットでも拍を途切れさせない。投げで打楽器を厚くし、Bの着地に低いアクセント。最後まで進行中のリズムを保って30秒で切る。歌声なし。
重い足音、衣服と革の軋み、息、前腕で受ける音、打撃、シダと落ち葉、投げの着地音。SHOT 2→3と幹の遮蔽前後で足音と呼吸を連続させる。BGMは声と動作音より下。

連続性
2人の顔、体格、髭、衣服、Bの角兜を維持。髭と衣服は加速に遅れて揺れる。攻撃線から外れた回避、接触による反動、足の支持と蹴りの回収を見せる。マスクカットはSHOT 5→6の1回、それ以外は通常のカット。字幕や画面内文字なし。
```

Type: Evaluation | Date: 2026-10-16

---

<a id="case-79"></a>
### 案例 79: [咖啡馆里的固定双人对白](https://x.com/tanabe_fragm/status/2110887676832543125) (作者 [@tanabe_fragm](https://x.com/tanabe_fragm))

**用公开对白 Prompt 测试轮流说话与侧脸口型同步**

作者报价按十秒计算，附件约十五秒，未独立验证音频或计费

[![咖啡馆里的固定双人对白](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D44/poster-293ead53e5df.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D44/video-293ead53e5df.mp4)

**提示词** · [公开提示词来源](https://x.com/tanabe_fragm/status/2110887676832543125)

```
A fixed, locked-off medium two-shot in a bright café at midday, horizontal 16:9 cinematic framing. Two young Japanese women in their early twenties sit facing each other across a small wooden table. The camera is at table height beside the table, so both women are seen in three-quarter view from the waist up — Misaki on the left of frame, Yui on the right — with their faces large and clearly lit. A large window runs along the background; soft natural daylight falls on their faces from the side, not from behind. Two iced lattes sit on the table between them. Photorealistic, natural skin texture, gentle background blur.

Misaki (left): 22, cheerful and talkative, black chin-length bob, white knit sweater, expressive hand gestures.
Yui (right): 23, gentle and easygoing, long brown hair, beige cardigan, laughs easily.

The camera does not move or cut. Exactly four lines of dialogue, in natural Tokyo-standard Japanese, in this order. While one speaks, the other listens with her mouth closed, reacting only with nods and smiles.

0–4s: Misaki leans forward toward Yui, eyes bright, excited:「ねえ聞いて！ 昨日ね、駅前のパン屋さん、やっと行けたの」
4–7s: Yui's eyes widen, surprised, quick:「え、まって、あの毎朝並んでるとこ？」
7–11s: Misaki nods hard, hands miming something crispy, delighted:「そうそう！ メロンパン、ぱりっぱりで…もう最高だった」
11–15s: Yui bursts out laughing and speaks through the laugh, playfully envious:「ずるい！ 今度ぜったい一緒に行こうね」

Precise lip sync: lips fully close on ま, ぱ, め, ば sounds; mouth shapes follow each vowel. No extra lines, no ad-libs, no narration. Audio is only the two voices and soft café ambience — no background music. No subtitles, no on-screen text. Single continuous horizontal shot, same framing from start to end.
```

Type: Evaluation | Date: 2026-10-16

---

<a id="case-80"></a>
### 案例 80: [标准版与 Flash 的五人对白](https://x.com/onofumi_AI/status/2110866433198702728) (作者 [@onofumi_AI](https://x.com/onofumi_AI))

**比较作者展示的两路结果中的角色位置与场景构图**

来源自述场景长二十秒，分别消耗 180 与 120 积分，这些数值仅代表该作者账号口径

[![标准版与 Flash 的五人对白](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D45/poster-1007d8f82463.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D45/video-1007d8f82463.mp4)

Type: Evaluation | Date: 2026-10-15

---

<a id="case-81"></a>
### 案例 81: [虎头人物测试近身动作](https://x.com/ozansihay/status/2110763522099474800) (作者 [@ozansihay](https://x.com/ozansihay))

**用创作者的格斗片段观察高接触动作与角色参考图的作用**

作者仍偏好 Seedance 的身体接触表现，自述三十秒 1080p 花费 405 积分，并披露推广

[![虎头人物测试近身动作](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D64/poster-e99a824137b0.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D64/video-e99a824137b0.mp4)

Type: Evaluation | Date: 2026-10-15

---

<a id="case-82"></a>
### 案例 82: [音画漂移测试中的变化主持人](https://x.com/plasm0/status/2110763509307064539) (作者 [@plasm0](https://x.com/plasm0))

**把样片作为独立测量同步效果的起点**

作者声称测试通过，抽样画面只确认主持人发生变化，并未验证语音同步准确性

[![音画漂移测试中的变化主持人](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D65/poster-285b037dd41e.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D65/video-285b037dd41e.mp4)

Type: Evaluation | Date: 2026-10-15

---

<a id="case-83"></a>
### 案例 83: [同一飞车概念的双模型对比](https://x.com/itsPolloAI/status/2111097887656726915) (作者 [@itsPolloAI](https://x.com/itsPolloAI))

**比较两条带标签的视频轨道，同时保留平台的对比口径**

Pollo AI 称使用了相同 Prompt，但没有给出实际 Prompt 或多次受控测试

[![同一飞车概念的双模型对比](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D86/poster-f8698ad3f5cb.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D86/video-f8698ad3f5cb.mp4)

Type: Evaluation | Date: 2026-10-16

---

## 相关仓库

尚未验证当前模型的可用路由，因此暂不链接专用 Kling 4 API 或 Skill 仓库；相邻模型的资料可参考 [Seedance 2.5 指南](https://github.com/EvoLinkAI/awesome-seedance-2.5-guide)，该指南讨论不同模型，不能据此验证本仓库的 Kling 案例

<a id="acknowledge"></a>
## 🙏 致谢

感谢本资料集中公开分享内容的账号：

[@_3912657840](https://x.com/_3912657840), [@_lexers](https://x.com/_lexers), [@agi_aibusi](https://x.com/agi_aibusi), [@AI__TSUBAKI](https://x.com/AI__TSUBAKI), [@AibeginnerR8](https://x.com/AibeginnerR8), [@AIWarper](https://x.com/AIWarper), [@AiwithAmeliaa](https://x.com/AiwithAmeliaa), [@Aiwithkami](https://x.com/Aiwithkami), [@AIwithkhan](https://x.com/AIwithkhan), [@AlexM12jx](https://x.com/AlexM12jx), [@alifcoder](https://x.com/alifcoder), [@Alin_Reaper05](https://x.com/Alin_Reaper05), [@Bic_Revelation](https://x.com/Bic_Revelation), [@craftcapitallab](https://x.com/craftcapitallab), [@Dani__oros](https://x.com/Dani__oros), [@Diplomeme](https://x.com/Diplomeme), [@dylannknox](https://x.com/dylannknox), [@ErnestoSOFTWARE](https://x.com/ErnestoSOFTWARE), [@fabulatenebris](https://x.com/fabulatenebris), [@fAIkout](https://x.com/fAIkout), [@fatoomdes](https://x.com/fatoomdes), [@frameo_ai](https://x.com/frameo_ai), [@Gemalpha_88](https://x.com/Gemalpha_88), [@h_ashizawaJP](https://x.com/h_ashizawaJP), [@higgsfield_ai](https://x.com/higgsfield_ai), [@Hope_Ai01](https://x.com/Hope_Ai01), [@iam_mian7](https://x.com/iam_mian7), [@IntLab0000](https://x.com/IntLab0000), [@itsPolloAI](https://x.com/itsPolloAI), [@jerrod_lew](https://x.com/jerrod_lew), [@jji1jj](https://x.com/jji1jj), [@leilamakes](https://x.com/leilamakes), [@lexx_aura](https://x.com/lexx_aura), [@Lianaalane](https://x.com/Lianaalane), [@liluocheng13](https://x.com/liluocheng13), [@Lisa__Rodin](https://x.com/Lisa__Rodin), [@magnific](https://x.com/magnific), [@MelinaVale14](https://x.com/MelinaVale14), [@minuitIA](https://x.com/minuitIA), [@MO_IAI](https://x.com/MO_IAI), [@Naonekozamurai](https://x.com/Naonekozamurai), [@nrqa__](https://x.com/nrqa__), [@NyaiiBubu](https://x.com/NyaiiBubu), [@ojiji2025](https://x.com/ojiji2025), [@onofumi_AI](https://x.com/onofumi_AI), [@OxBairan](https://x.com/OxBairan), [@ozansihay](https://x.com/ozansihay), [@PDyv9gdatT4132](https://x.com/PDyv9gdatT4132), [@plasm0](https://x.com/plasm0), [@PromptSin](https://x.com/PromptSin), [@seisei_ai_1st](https://x.com/seisei_ai_1st), [@SirGlavan_](https://x.com/SirGlavan_), [@sophiaparkerr_](https://x.com/sophiaparkerr_), [@Starjupi](https://x.com/Starjupi), [@Stevemnx3](https://x.com/Stevemnx3), [@tanabe_fragm](https://x.com/tanabe_fragm), [@techhalla](https://x.com/techhalla), [@torotoromoney](https://x.com/torotoromoney), [@tphuang](https://x.com/tphuang), [@umesh_ai](https://x.com/umesh_ai), [@WuxiaRocks](https://x.com/WuxiaRocks), [@YapayZekaSerisi](https://x.com/YapayZekaSerisi), [@z933TfmXkaISSVc](https://x.com/z933TfmXkaISSVc)

第三方视频、图片和提示词仍受各自权利约束，仓库编辑文字与结构采用 [CC BY 4.0](LICENSE)，这不代表重新授权第三方素材；如需更正署名、权属或转载，请[提交 Issue](https://github.com/cheercheung/awesome-kling-4-usecases/issues)，并参阅[媒体政策](docs/media-policy.md)与[贡献说明](CONTRIBUTING.md)

[查看 EvoLink 视频模型](https://evolink.ai/models?utm_source=github&utm_medium=footer&utm_campaign=awesome-kling-4-usecases&utm_content=zh-CN_footer)
