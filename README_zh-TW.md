<div align="center">

# Kling 4 Use Cases

<a href="https://evolink.ai/models?utm_source=github&utm_medium=banner&utm_campaign=awesome-kling-4-usecases&utm_content=zh-TW_banner"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/images/en.png" alt="Kling 4 使用案例" width="760"></a>

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](LICENSE)
[![EvoLink](https://img.shields.io/badge/Explore_video_models-EvoLink-black)](https://evolink.ai/models?utm_source=github&utm_medium=badge&utm_campaign=awesome-kling-4-usecases&utm_content=zh-TW_badge)

[![English](https://img.shields.io/badge/English-111111)](README.md) [![Español](https://img.shields.io/badge/Espa%C3%B1ol-ffb703)](README_es.md) [![Português](https://img.shields.io/badge/Portugu%C3%AAs-2a9d8f)](README_pt.md) [![日本語](https://img.shields.io/badge/%E6%97%A5%E6%9C%AC%E8%AA%9E-52b788)](README_ja.md) [![한국어](https://img.shields.io/badge/%ED%95%9C%EA%B5%AD%EC%96%B4-4ea8de)](README_ko.md) [![Deutsch](https://img.shields.io/badge/Deutsch-f4a261)](README_de.md) [![Français](https://img.shields.io/badge/Fran%C3%A7ais-e76f51)](README_fr.md) [![Türkçe](https://img.shields.io/badge/T%C3%BCrk%C3%A7e-d62828)](README_tr.md) [![繁體中文](https://img.shields.io/badge/%E7%B9%81%E9%AB%94%E4%B8%AD%E6%96%87-8338ec)](README_zh-TW.md) [![简体中文](https://img.shields.io/badge/%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87-ef476f)](README_zh-CN.md) [![Русский](https://img.shields.io/badge/%D0%A0%D1%83%D1%81%D1%81%D0%BA%D0%B8%D0%B9-577590)](README_ru.md)

</div>

## 🍌 簡介

**透過公開影片、創作者工作流和已公開提示詞，瞭解 Kling 4 / 4.0 的具體用法** 本倉庫幫助影片創作者、開發者和模型評測者挑選值得觀察或測試的場景，每個案例都連結原帖與發帖賬號

點選影片封面觀看，結合證據說明閱讀；只有作者實際公開了 Prompt 才提供原文供複製，發帖賬號可能是分發方，署名本身不代表原創身份已經確認

[檢視 EvoLink 影片模型](https://evolink.ai/models?utm_source=github&utm_medium=introduction&utm_campaign=awesome-kling-4-usecases&utm_content=zh-TW_introduction)

## 📊 概覽

**83 個精選案例 · 10 個案例包含 11 組公開 Prompt · 8 個分類** 內容覆蓋工作流、廣告、敘事、動作、遊戲概念、動畫、世界場景與對比，每個案例都有來源、賬號連結、使用要點、媒體、型別及 UTC 來源日期

> [!NOTE]
> 這些案例有公開來源支援，但並非獨立驗證的 Kling API 呼叫或受控基準測試，部分條目是同一部成片的不同剪段；遊戲式影片不代表可玩的遊戲，剪輯成片時長也不代表原生生成時長，價格與積分仍按作者自述標註

下載[案例資料](data/use-cases.json)或[可排序 CSV](data/use-cases.csv)，其中保留採集時的互動指標、Prompt 狀態與來源關係；[採集範圍](docs/collection-scope.md)說明了兩次檢索的時間視窗及其間隔，本倉庫是固定日期的資料集，並非實時全量索引

<a id="quick-start"></a>
## ⚡ 快速開始

1. [檢視 EvoLink 影片模型](https://evolink.ai/models?utm_source=github&utm_medium=quick_start&utm_campaign=awesome-kling-4-usecases&utm_content=zh-TW_quick_start)，註冊或登入賬號
2. 使用已支援模型時，[建立或獲取 API Key](https://evolink.ai/dashboard/keys?utm_source=github&utm_medium=api_key&utm_campaign=awesome-kling-4-usecases&utm_content=zh-TW_api_key)
3. 提交任務前先確認具體模型可用性，**截至 2026-10-17，本資料集尚未驗證 Kling 4 的 API 路由與專用可安裝 Skill**；可透過[閱讀 Codex CLI 設定文件](https://evolink.ai/docs/en/cli/codex?utm_source=github&utm_medium=setup_docs&utm_campaign=awesome-kling-4-usecases&utm_content=zh-TW_setup_docs)瞭解通用設定，該文件不是經驗證的 Kling 4 首次呼叫範例

本倉庫用於研究與創作參考，不提供可執行 API 示例或模型安裝器；復現案例時，不要把其他 Kling 版本直接當成同一模型

## 📑 目錄

| 案例 | 分類 | 觀察要點 | 型別 |
|---|---|---|---|
| [科幻場景中的角色與環境參考](#case-1) | 工作流與參考資料 | 觀察獨立角色表和環境表如何與長篇影片創作要求並列呈現 | Demo |
| [從 Agent 分鏡到動畫片段](#case-2) | 工作流與參考資料 | 將作者的劇本、分鏡、Prompt 串聯方式用於短動畫的前期規劃 | Tutorial |
| [宏大奇幻場景的參考圖表](#case-3) | 工作流與參考資料 | 觀察角色表、環境表與長篇場景要求之間的對應關係 | Demo |
| [手機聊天介面中的影片任務](#case-4) | 工作流與參考資料 | 先觀察作者提出的 Codex 到 MCP 銜接方式，再用自己的已驗證工具復現 | Tutorial |
| [起亞 SUV 的森林公路廣告](#case-5) | 廣告與產品故事 | 用公開的十五鏡分鏡，規劃三十秒廣告中的車輛連續性 | Demo |
| [多人物護膚品 UGC 廣告拼貼](#case-6) | 廣告與產品故事 | 參考可見廣告形式，規劃保留完整製作記錄的 UGC 對照實驗 | Demo |
| [迷你龍給甜點焦糖化](#case-7) | 廣告與產品故事 | 以一個明確的食物動作，觀察角色驅動的產品故事 | Demo |
| [橙汁紙盒的廣告場景](#case-8) | 廣告與產品故事 | 圍繞單一產品觀察包裝可見度、水果意象與轉場 | Demo |
| [淺綠房間裡的耳機女孩](#case-9) | 角色與敘事 | 觀察近景、全身動作與同一淺色場景中的角色外觀 | Demo |
| [走近古典柱廊的男子](#case-10) | 角色與敘事 | 透過可見片段觀察剋制的動作和建築環境連續性 | Demo |
| [溼發女性的情緒近景](#case-11) | 角色與敘事 | 觀察以對白表演為主的樣片中細微的面部變化和構圖 | Demo |
| [電影院裡的母女情緒瞬間](#case-12) | 角色與敘事 | 觀察短情緒場景如何依託一個具體的個人故事 | Demo |
| [兩位主播播報日語新聞](#case-13) | 角色與敘事 | 據此設計針對對白、雙人排程和螢幕圖文的專項測試 | Demo |
| [辦公大廳裡的迷你卡丁車](#case-14) | 角色與敘事 | 透過把意外的交通工具放進日常建築場景，觀察喜劇性的比例反差 | Demo |
| [男友視角下的夏日散步](#case-15) | 角色與敘事 | 複製詳細公開要求，以日常互動規劃三十秒連續敘事 | Demo |
| [車輛、士兵與人物近景合集](#case-16) | 角色與敘事 | 用蒙太奇挑出具體任務，再分別進行受控測試 | Demo |
| [King Cards 的魔術與城市飛行](#case-17) | 角色與敘事 | 觀察較長短片如何連線舞臺魔術、紙質載具和反覆出現的紅鳥 | Demo |
| [鄉村女性與暴雨前的拖拉機](#case-18) | 角色與敘事 | 觀察角色、機器和天氣如何傳達簡短的敘事前提 | Demo |
| [恐龍冒險短片與可複用鏡頭要求](#case-19) | 角色與敘事 | 對照成片與作者公開的七秒動作、八秒駕車要求進行學習 | Demo |
| [快遞員開啟通向異世界的電梯](#case-20) | 角色與敘事 | 觀察固定主角如何對同一扇門外不斷變化的環境作出反應 | Demo |
| [地下烏龜水管工的喜劇場景](#case-21) | 角色與敘事 | 用作者的流程說明區分概念、角色設計、指令碼、對白與聲音決策 | Demo |
| [以車輛意外收尾的街頭追逐](#case-22) | 角色與敘事 | 透過人物動作、構圖和街頭狀況變化觀察喜劇節奏 | Demo |
| [少女發現藍龍的奇幻短片](#case-23) | 角色與敘事 | 觀察個人奇幻故事如何形成包含固定角色的組合片段 | Demo |
| [紙質載具駛入花城](#case-24) | 角色與敘事 | 觀察 King Cards 短剪段中的人物、載具與環境變化 | Demo |
| [紙質車廂裡的石像變成人](#case-25) | 角色與敘事 | 觀察移動載具內的角色位置與短暫形態變化 | Demo |
| [魔術師與紙牌環繞的劇場](#case-26) | 角色與敘事 | 把中心人物表演、移動道具和周圍觀眾作為同一場景觀察 | Demo |
| [庭院足浴中的女性日常](#case-27) | 角色與敘事 | 觀察普通手勢、服裝和安靜環境，而非複雜動作 | Demo |
| [以獵鷹串聯舉報主題短片](#case-28) | 角色與敘事 | 觀察角色意象如何把手機介面鏡頭連線成一個主題表達 | Demo |
| [廚房裡躡行的橘貓](#case-29) | 角色與敘事 | 觀察日常室內環境中的小動作與鏡頭距離變化 | Demo |
| [兩名男子在街角相見擁抱](#case-30) | 角色與敘事 | 觀察簡短社互動動中的接近、身體接觸與角色位置 | Demo |
| [月下雲端雙人劍鬥](#case-31) | 動作與身體互動 | 用這段畫面觀察多人動作、空中排程與服裝輪廓的連續性 | Demo |
| [跆拳道館內的雙人格鬥](#case-32) | 動作與身體互動 | 對照格鬥過程中的身體接觸、雙方距離與鏡頭位置 | Demo |
| [兩輛跑車穿越城市追逐](#case-33) | 動作與身體互動 | 觀察快速切換鏡位時車輛身份和運動方向的延續 | Demo |
| [移動鏡頭下的拳擊交鋒](#case-34) | 動作與身體互動 | 觀察出拳、防守位移與近身接觸，不只看單張好看的畫面 | Demo |
| [穿越爆炸街道的女戰士](#case-35) | 動作與身體互動 | 觀察固定角色與行駛車輛、煙霧及大規模背景特效的關係 | Demo |
| [少女與城市巨獸對峙](#case-36) | 動作與身體互動 | 跟隨城市中的衝突場景，比較人物和巨獸的體量關係 | Demo |
| [穿過外星叢林的機械捕食者](#case-37) | 動作與身體互動 | 用公開 Prompt 觀察加速、環境反應和後退的手持視角 | Demo |
| [騎手在戰場上持長槍交鋒](#case-38) | 動作與身體互動 | 觀察開闊戰場中的騎手互動、馬匹運動與武器接觸 | Demo |
| [空手道交手與地墊接觸](#case-39) | 動作與身體互動 | 觀察表演者與周圍環境的接觸，不把動作僅看作孤立姿勢 | Demo |
| [便利店員工與格鬥者交手](#case-40) | 動作與身體互動 | 觀察帶日語對白的動作樣例中的近身接觸與場景連續性 | Demo |
| [石臺上的鎧甲奇幻格鬥](#case-41) | 動作與身體互動 | 觀察關鍵幀驅動的風格化戰鬥中的動作排程 | Demo |
| [貓咪穿越夜間城鎮](#case-42) | 動作與身體互動 | 復製作者的一鏡到底 Prompt，探索相連室內外空間中的快速運動 | Demo |
| [雨中森林裡的武士對決](#case-43) | 動作與身體互動 | 觀察雨景格鬥中的服裝穩定性與武器接觸 | Demo |
| [樹林中黑衣女性的動作片段](#case-44) | 動作與身體互動 | 對照同一林間動作場景的不同編碼版本，觀察姿勢與鏡頭運動 | Demo |
| [紅紙鳥對抗紫色章魚](#case-45) | 動作與身體互動 | 觀察小型飛行主體與大型拼裝生物之間的互動 | Demo |
| [籃球運動員飛身扣籃](#case-46) | 動作與身體互動 | 觀察身體軌跡、籃球位置與籃筐接觸 | Demo |
| [賞金獵人風格的遊戲概念](#case-47) | 遊戲與載具概念 | 將片段作為結合人物動作和對白的遊戲預告場景參考 | Demo |
| [飛車衝上夜間巨型坡道](#case-48) | 遊戲與載具概念 | 將片段用作電影化車輛概念參考，不當作遊戲已經可執行的證據 | Demo |
| [日落海岸公路上的跑車競速](#case-49) | 遊戲與載具概念 | 觀察競速影片概念中的追逐鏡頭、光線和儀表式疊層 | Demo |
| [戰鬥機飛越海島環境](#case-50) | 遊戲與載具概念 | 用樣片觀察飛行鏡頭的運動和遊戲介面構圖 | Demo |
| [角色在浮空島之間滑翔](#case-51) | 遊戲與載具概念 | 觀察第三人稱影片概念從狹窄空間轉入寬闊空景的方式 | Demo |
| [跟隨騎手的摩托競速概念](#case-52) | 遊戲與載具概念 | 觀察遊戲式影片中的摩托動作、追逐鏡頭距離與賽道照明 | Demo |
| [第一人稱港口射擊場景](#case-53) | 遊戲與載具概念 | 復製作者按時間分段的戰術射擊要求，定義十五秒視覺目標 | Demo |
| [未來城市中的飛行汽車](#case-54) | 遊戲與載具概念 | 透過概念畫面觀察街面駕駛、飛行和城市地標之間的轉換 | Demo |
| [警車追逐穿城飛車](#case-55) | 遊戲與載具概念 | 觀察追逐鏡頭概念如何結合地面車流與騰空動作 | Demo |
| [海濱駕駛轉入直升機飛行](#case-56) | 遊戲與載具概念 | 觀察跑車、步行人物和空中鏡頭之間的轉換 | Demo |
| [插畫與實拍風格交織的音樂影片](#case-57) | 動畫與風格化角色 | 觀察完整 MV 如何結合不同風格和反覆出現的情緒意象 | Demo |
| [廚房裡的奶奶與迷你黏土龍](#case-58) | 動畫與風格化角色 | 觀察緊湊廚房動畫中的角色互動與材質風格 | Demo |
| [夜市攤位上的動漫廚師](#case-59) | 動畫與風格化角色 | 觀察短篇烹飪動畫中的手部動作、道具與照明 | Demo |
| [微縮人物的定格風格戰鬥](#case-60) | 動畫與風格化角色 | 觀察微縮比例和定格風格如何塑造短動作片段 | Demo |
| [發光月牙座椅上的睡眠場景](#case-61) | 動畫與風格化角色 | 用場景觀察裝飾性光線主題與輕微人物動作 | Demo |
| [城市路口的快閃群舞](#case-62) | 動畫與風格化角色 | 觀察街舞片段中的群體動作、空間排列與視角變化 | Demo |
| [暴風雲下的動漫劍客對決](#case-63) | 動畫與風格化角色 | 觀察風格化格鬥中清晰的人物輪廓與兵刃互動 | Demo |
| [黑白舞臺上的多人舞蹈](#case-64) | 動畫與風格化角色 | 在去除色彩的條件下觀察編舞與燈光 | Demo |
| [森林裡玩雪的松鼠](#case-65) | 動畫與風格化角色 | 觀察富於表情的動物動作與統一的柔和動畫風格 | Demo |
| [紅衣人物穿過糖果世界](#case-66) | 動畫與風格化角色 | 觀察風格化人物動作與由甜點構成的環境 | Demo |
| [戴王冠的白貓吃咖哩](#case-67) | 動畫與風格化角色 | 觀察服裝、食物道具與表情如何支撐動物角色短故事 | Demo |
| [從森林旅程轉入騎龍飛行](#case-68) | 世界場景與生物 | 觀察畫面如何從封閉樹林逐步展開為空中遠景 | Demo |
| [恐怖蒙太奇中的無麵人形](#case-69) | 世界場景與生物 | 觀察怪物形象的連續性及不同詭異意象之間的轉場 | Demo |
| [甦醒的球形外星聚落](#case-70) | 世界場景與生物 | 復製作者公開的 Prompt，探索虛構小鎮中多種環境運動的配合 | Demo |
| [外星巨獸涉過淺水湖](#case-71) | 世界場景與生物 | 復製作者的 Prompt，探索體重、水面反應和緩慢升鏡 | Demo |
| [巨型機甲從甲板起飛](#case-72) | 世界場景與生物 | 觀察機械關節、體量與從站立轉入飛行的過程 | Demo |
| [巨獸逼近擁堵的懸索橋](#case-73) | 世界場景與生物 | 觀察暴雨環境中巨獸、車輛和人群之間的比例關係 | Demo |
| [報紙載具穿越紙質城市](#case-74) | 世界場景與生物 | 觀察摺紙風城市中的環境材質一致性與跟隨鏡頭 | Demo |
| [山坡上的重型步行機甲](#case-75) | 世界場景與生物 | 觀察機械運動、地面接觸與超大武器之間的關係 | Demo |
| [哥特人物穿行雨夜](#case-76) | 世界場景與生物 | 觀察氛圍、輪廓和反覆出現的視覺主題 | Demo |
| [紙質車廂進入發光菌菇隧道](#case-77) | 世界場景與生物 | 觀察畫面如何從受限的車廂視角轉入明亮環境 | Demo |
| [同一森林格鬥 Prompt 的雙模型對比](#case-78) | 對比與評測 | 比較兩路顯示結果，同時保留作者宣告的設定和評價邊界 | Evaluation |
| [咖啡館裡的固定雙人對白](#case-79) | 對比與評測 | 用公開對白 Prompt 測試輪流說話與側臉口型同步 | Evaluation |
| [標準版與 Flash 的五人對白](#case-80) | 對比與評測 | 比較作者展示的兩路結果中的角色位置與場景構圖 | Evaluation |
| [虎頭人物測試近身動作](#case-81) | 對比與評測 | 用創作者的格鬥片段觀察高接觸動作與角色參考圖的作用 | Evaluation |
| [音畫漂移測試中的變化主持人](#case-82) | 對比與評測 | 把樣片作為獨立測量同步效果的起點 | Evaluation |
| [同一飛車概念的雙模型對比](#case-83) | 對比與評測 | 比較兩條帶標籤的影片軌道，同時保留平臺的對比口徑 | Evaluation |

<a id="category-workflow"></a>
## 🛠️ 工作流與參考資料

<a id="case-1"></a>
### 案例 1: [科幻場景中的角色與環境參考](https://x.com/_lexers/status/2111014728160235719) (作者 [@_lexers](https://x.com/_lexers))

**觀察獨立角色表和環境表如何與長篇影片創作要求並列呈現**

影片展示沙漠世界、參考圖與滾動 Prompt，全文尚未轉錄

[![科幻場景中的角色與環境參考](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D11/poster-c7f71e602146.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D11/video-c7f71e602146.mp4)

Type: Demo | Date: 2026-10-16

---

<a id="case-2"></a>
### 案例 2: [從 Agent 分鏡到動畫片段](https://x.com/z933TfmXkaISSVc/status/2111002792102158714) (作者 [@z933TfmXkaISSVc](https://x.com/z933TfmXkaISSVc))

**將作者的劇本、分鏡、Prompt 串聯方式用於短動畫的前期規劃**

作者自述用 Opus 5.5 寫作，再以 Claude 和 MCP 生成，動畫附件無法驗證工具執行日誌

[![從 Agent 分鏡到動畫片段](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D15/poster-a0d7f303f6cf.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D15/video-a0d7f303f6cf.mp4)

Type: Tutorial | Date: 2026-10-16

---

<a id="case-3"></a>
### 案例 3: [宏大奇幻場景的參考圖表](https://x.com/dylannknox/status/2110984061569421429) (作者 [@dylannknox](https://x.com/dylannknox))

**觀察角色表、環境表與長篇場景要求之間的對應關係**

組合展示中可見拱頂環境和滾動 Prompt，但完整文字尚未轉錄

[![宏大奇幻場景的參考圖表](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D19/poster-225fcfcd6ec2.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D19/video-225fcfcd6ec2.mp4)

Type: Demo | Date: 2026-10-16

---

<a id="case-4"></a>
### 案例 4: [手機聊天介面中的影片任務](https://x.com/agi_aibusi/status/2110941943006118201) (作者 [@agi_aibusi](https://x.com/agi_aibusi))

**先觀察作者提出的 Codex 到 MCP 銜接方式，再用自己的已驗證工具復現**

錄屏顯示聊天和任務狀態，作者討論的訂閱積分規則不代表通用 API 計費規則

[![手機聊天介面中的影片任務](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D28/poster-fbf3abad9feb.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D28/video-fbf3abad9feb.mp4)

Type: Tutorial | Date: 2026-10-16

---


<a id="category-ads"></a>
## 📦 廣告與產品故事

<a id="case-5"></a>
### 案例 5: [起亞 SUV 的森林公路廣告](https://x.com/Diplomeme/status/2110947179057811727) (作者 [@Diplomeme](https://x.com/Diplomeme))

**用公開的十五鏡分鏡，規劃三十秒廣告中的車輛連續性**

Prompt 依賴此處未提供的車輛參考圖，其中的 4K 是指令要求，不是經核驗的輸出解析度

[![起亞 SUV 的森林公路廣告](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D26/poster-cf1e54b34518.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D26/video-cf1e54b34518.mp4)

**提示詞** · [公開提示詞來源](https://x.com/Diplomeme/status/2110947179057811727)

```
High-octane, hyper-realistic automotive commercial for the Kia Seltos, shot with the visual intensity of a Christopher Nolan-style cinematic production using actual 70mm IMAX cameras. Fast-paced multi-shot editing with quick, cinematic cuts timed at exactly one shot every 2 seconds across a complete 30-second timeline. The champagne-gold Kia Seltos, matching the exact vehicle design in the provided reference images, charges through a dense forest road surrounded by towering trees and dappled sunlight. High-contrast Nolan-esque color grading with deep shadows, cold teals, warm champagne-gold reflections, and bright highlights. Sunlight pierces through the forest canopy, reflecting across the sculpted bodywork, signature vertical LED daytime running lights, black front grille, muscular wheel arches, and distinctive rear light bar. Rapid sequence of intense cuts:•Shot 1 (0-2s): Ground-level cinematic establishing shot of an empty winding forest road, towering trees casting deep shadows as sunlight breaks through the canopy. The distant engine note of the approaching Kia Seltos builds tension.•Shot 2 (2-4s): Low eye-level tracking shot of the champagne-gold Kia Seltos emerging between the trees, accelerating along the forest road and revealing its bold front grille, distinctive vertical LED lighting signature, and commanding SUV stance.•Shot 3 (4-6s): Tight, detailed close-up of the front fascia, Kia emblem, illuminated LED daytime running lights, glossy black grille elements, and champagne-gold paint reflecting the passing forest.•Shot 4 (6-8s): Dramatic low-angle tracking shot moving alongside the front wheel as the alloy spokes spin rapidly, tires maintain realistic contact with the asphalt, and the SUV’s sculpted bodywork catches streaks of sunlight.•Shot 5 (8-10s): Fast lateral tracking shot revealing the complete side profile, muscular wheel arches, black lower-body cladding, door contours, windows, roofline, and metallic champagne-gold finish as the Kia Seltos sweeps through the forest.•Shot 6 (10-12s): Low-angle handheld-style camera whip-pan from the road surface to the SUV’s front three-quarter profile as it exits a sweeping bend, with realistic suspension movement, controlled body roll, and natural background motion blur.•Shot 7 (12-14s): Extreme close-up of sunlight traveling across the sculpted hood, Kia emblem, sharp body creases, and vertical LED lights, emphasizing precise automotive design and premium paint reflections.•Shot 8 (14-16s): Rear three-quarter tracking shot following the Kia Seltos through the forest, showcasing the distinctive rear light bar, angular vertical taillights, rear spoiler, sculpted tailgate, and authentic model badging.•Shot 9 (16-18s): Dynamic wheel-height tracking shot as the SUV drives across alternating patches of sunlight and shadow, capturing realistic tire rotation, subtle road texture, reflections along the lower doors, and the movement of the suspension over natural road undulations.•Shot 10 (18-20s): High-angle wide shot of the Kia Seltos commanding a sweeping forest road, surrounded by towering trees and atmospheric shafts of sunlight, with the winding asphalt leading the eye toward the moving SUV.•Shot 11 (20-22s): Fast front-facing tracking shot of the Kia Seltos approaching the camera along a straight section of forest road, its LED lights illuminated and grille dominating the frame as the camera smoothly retreats ahead of the vehicle.•Shot 12 (22-24s): Rapid cinematic transition into a close rear tracking angle as the SUV accelerates away through the trees, the rear lighting signature glowing against the darker forest and the road markings sweeping beneath the frame.•Shot 13 (24-26s): Dramatic low-angle front three-quarter hero shot as the Kia Seltos exits the forest bend and enters a naturally illuminated clearing, revealing its full stance, champagne-gold bodywork, alloy wheels, and signature front lighting.•Shot 14 (26-28s): Controlled cinematic orbit around the stationary Kia Seltos at a scenic forest-road pull-off, transitioning from the front three-quarter view toward the side and rear profile while the surrounding trees and golden sunlight create a premium automotive campaign atmosphere.•Shot 15 (28-30s): Hard cut to black with a final sweep of light revealing the KIA emblem followed by the SELTOS model name and the campaign tagline: “OWN EVERY TURN.” End with a powerful, clean, premium automotive advertising finish.Raw automotive documentary-style camera textures, organic lens flares, lifelike vehicle physics, authentic wheel rotation and tire contact, realistic suspension movement, natural road reflections, physically accurate metallic paint reflections, cinematic motion blur, subtle engine vibration, and an immersive forest-road atmosphere. Preserve the exact Kia Seltos identity, champagne-gold exterior color, front grille design, LED lighting signatures, alloy wheels, body proportions, side profile, and rear design from the provided reference images throughout every shot. Maintain consistent vehicle geometry, wheel design, lighting signatures, paint color, and branding across all 15 shots. No vehicle redesign, no morphing, no inconsistent body panels, no incorrect logos, no artificial CGI appearance, no impossible driving maneuvers, no exaggerated visual effects, and no abrupt changes in road geography. Ultra-detailed, 4K resolution, premium global automotive advertising quality.
```

Type: Demo | Date: 2026-10-16

---

<a id="case-6"></a>
### 案例 6: [多人物護膚品 UGC 廣告拼貼](https://x.com/ErnestoSOFTWARE/status/2110917624167108665) (作者 [@ErnestoSOFTWARE](https://x.com/ErnestoSOFTWARE))

**參考可見廣告形式，規劃保留完整製作記錄的 UGC 對照實驗**

作者推介 Higgsfield MCP 並自述低成本，但未提供投放表現或賬單證據

[![多人物護膚品 UGC 廣告拼貼](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D37/poster-4ca47c0af310.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D37/video-4ca47c0af310.mp4)

Type: Demo | Date: 2026-10-16

---

<a id="case-7"></a>
### 案例 7: [迷你龍給甜點焦糖化](https://x.com/magnific/status/2111200639707668507) (作者 [@magnific](https://x.com/magnific))

**以一個明確的食物動作，觀察角色驅動的產品故事**

平臺自有樣片把微型龍放在焦糖布蕾旁，不能證明銷售表現

[![迷你龍給甜點焦糖化](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D76/poster-6f401168b0fb.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D76/video-6f401168b0fb.mp4)

Type: Demo | Date: 2026-10-16

---

<a id="case-8"></a>
### 案例 8: [橙汁紙盒的廣告場景](https://x.com/leilamakes/status/2111108005567582329) (作者 [@leilamakes](https://x.com/leilamakes))

**圍繞單一產品觀察包裝可見度、水果意象與轉場**

來源把橙汁紙盒、水果和零售場景結合起來，沒有公開 Prompt

[![橙汁紙盒的廣告場景](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D85/poster-af7aa6745461.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D85/video-af7aa6745461.mp4)

Type: Demo | Date: 2026-10-16

---


<a id="category-story"></a>
## 🎬 角色與敘事

<a id="case-9"></a>
### 案例 9: [淺綠房間裡的耳機女孩](https://x.com/iam_mian7/status/2110826299417854081) (作者 [@iam_mian7](https://x.com/iam_mian7))

**觀察近景、全身動作與同一淺色場景中的角色外觀**

綠髮耳機女孩在淺綠室內改變姿態，鏡頭景別也隨之變化

[![淺綠房間裡的耳機女孩](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D03/poster-3305b566e9a1.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D03/video-3305b566e9a1.mp4)

Type: Demo | Date: 2026-10-15

---

<a id="case-10"></a>
### 案例 10: [走近古典柱廊的男子](https://x.com/lexx_aura/status/2111017349755043959) (作者 [@lexx_aura](https://x.com/lexx_aura))

**透過可見片段觀察剋制的動作和建築環境連續性**

抽樣畫面顯示男子與古典柱廊，不能用原帖寬泛的 CGI 讚美證明覆雜動作能力

[![走近古典柱廊的男子](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D09/poster-e4099969039c.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D09/video-e4099969039c.mp4)

Type: Demo | Date: 2026-10-16

---

<a id="case-11"></a>
### 案例 11: [溼發女性的情緒近景](https://x.com/sophiaparkerr_/status/2110777323423400161) (作者 [@sophiaparkerr_](https://x.com/sophiaparkerr_))

**觀察以對白表演為主的樣片中細微的面部變化和構圖**

畫面集中於綠色暗光中的女性面部，未獨立評分音訊質量

[![溼發女性的情緒近景](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D14/poster-bd91c5962388.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D14/video-bd91c5962388.mp4)

Type: Demo | Date: 2026-10-15

---

<a id="case-12"></a>
### 案例 12: [電影院裡的母女情緒瞬間](https://x.com/liluocheng13/status/2110981671243874346) (作者 [@liluocheng13](https://x.com/liluocheng13))

**觀察短情緒場景如何依託一個具體的個人故事**

作者將 16 秒短片與舊日關係的回憶相連，並註明影象用 Gemini、影片用 Kling 4.0

[![電影院裡的母女情緒瞬間](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D21/poster-59193966fd28.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D21/video-59193966fd28.mp4)

Type: Demo | Date: 2026-10-16

---

<a id="case-13"></a>
### 案例 13: [兩位主播播報日語新聞](https://x.com/seisei_ai_1st/status/2110975778183942532) (作者 [@seisei_ai_1st](https://x.com/seisei_ai_1st))

**據此設計針對對白、雙人排程和螢幕圖文的專項測試**

作者討論日語語音，畫面核驗只確認新聞演播室形式，未獨立驗證發音

[![兩位主播播報日語新聞](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D23/poster-6d7a8b12e568.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D23/video-6d7a8b12e568.mp4)

Type: Demo | Date: 2026-10-16

---

<a id="case-14"></a>
### 案例 14: [辦公大廳裡的迷你卡丁車](https://x.com/PromptSin/status/2110943847706775742) (作者 [@PromptSin](https://x.com/PromptSin))

**透過把意外的交通工具放進日常建築場景，觀察喜劇性的比例反差**

作者標註使用 Kling 4 Flash，片段顯示坐著的角色駕車穿過辦公大廳

[![辦公大廳裡的迷你卡丁車](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D27/poster-df7aadba33d7.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D27/video-df7aadba33d7.mp4)

Type: Demo | Date: 2026-10-16

---

<a id="case-15"></a>
### 案例 15: [男友視角下的夏日散步](https://x.com/agi_aibusi/status/2110924173619138656) (作者 [@agi_aibusi](https://x.com/agi_aibusi))

**複製詳細公開要求，以日常互動規劃三十秒連續敘事**

Prompt 指定了一位女性的外觀、六個定時片段、家用相機行為與環境聲音

[![男友視角下的夏日散步](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D34/poster-8bef5187ff5c.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D34/video-8bef5187ff5c.mp4)

**提示詞** · [公開提示詞來源](https://x.com/agi_aibusi/status/2110924176890757483)

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
### 案例 16: [車輛、士兵與人物近景合集](https://x.com/jerrod_lew/status/2110911158156931427) (作者 [@jerrod_lew](https://x.com/jerrod_lew))

**用蒙太奇挑出具體任務，再分別進行受控測試**

約 63 秒附件屬於樣片合集，不能據此認定單次原生生成時長

[![車輛、士兵與人物近景合集](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D39/poster-7d5e3845dc71.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D39/video-7d5e3845dc71.mp4)

Type: Demo | Date: 2026-10-16

---

<a id="case-17"></a>
### 案例 17: [King Cards 的魔術與城市飛行](https://x.com/tphuang/status/2110902762619933119) (作者 [@tphuang](https://x.com/tphuang))

**觀察較長短片如何連線舞臺魔術、紙質載具和反覆出現的紅鳥**

這段整片混剪也出現在後續賬號的帖子中，相關剪段不當作獨立電影計數

[![King Cards 的魔術與城市飛行](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D42/poster-cd1175d34d80.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D42/video-cd1175d34d80.mp4)

Type: Demo | Date: 2026-10-16

---

<a id="case-18"></a>
### 案例 18: [鄉村女性與暴雨前的拖拉機](https://x.com/Bic_Revelation/status/2110847934346489947) (作者 [@Bic_Revelation](https://x.com/Bic_Revelation))

**觀察角色、機器和天氣如何傳達簡短的敘事前提**

來源將場景聯絡到國際農村婦女日，沒有公開生成配方

[![鄉村女性與暴雨前的拖拉機](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D47/poster-6a9f1d8d21de.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D47/video-6a9f1d8d21de.mp4)

Type: Demo | Date: 2026-10-15

---

<a id="case-19"></a>
### 案例 19: [恐龍冒險短片與可複用鏡頭要求](https://x.com/techhalla/status/2110806819937378773) (作者 [@techhalla](https://x.com/techhalla))

**對照成片與作者公開的七秒動作、八秒駕車要求進行學習**

兩份 Prompt 卡片都保留為圖片轉錄，內嵌參考縮圖不是獨立輸入原圖

[![恐龍冒險短片與可複用鏡頭要求](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D50/poster-9890fdc58895.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D50/video-9890fdc58895.mp4)

作者回復圖片：分鏡、參考圖與提示詞卡片，內嵌縮圖不是原始參考檔案

![作者回復圖片：分鏡、參考圖與提示詞卡片，內嵌縮圖不是原始參考檔案 1](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/source-prompts/2110806822957273273-0.jpg)

![作者回復圖片：分鏡、參考圖與提示詞卡片，內嵌縮圖不是原始參考檔案 2](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/source-prompts/2110806822957273273-1.jpg)

![作者回復圖片：分鏡、參考圖與提示詞卡片，內嵌縮圖不是原始參考檔案 3](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/source-prompts/2110806826350412052-0.jpg)

![作者回復圖片：分鏡、參考圖與提示詞卡片，內嵌縮圖不是原始參考檔案 4](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/source-prompts/2110806826350412052-1.jpg)

**提示詞 1** · [公開提示詞來源](https://x.com/techhalla/status/2110806822957273273)

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

**提示詞 2** · [公開提示詞來源](https://x.com/techhalla/status/2110806826350412052)

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
### 案例 20: [快遞員開啟通向異世界的電梯](https://x.com/PromptSin/status/2110790343298023798) (作者 [@PromptSin](https://x.com/PromptSin))

**觀察固定主角如何對同一扇門外不斷變化的環境作出反應**

黃制服快遞員面對冰、水與火焰等反差場景

[![快遞員開啟通向異世界的電梯](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D53/poster-c385592b815a.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D53/video-c385592b815a.mp4)

Type: Demo | Date: 2026-10-15

---

<a id="case-21"></a>
### 案例 21: [地下烏龜水管工的喜劇場景](https://x.com/Starjupi/status/2110781205415104571) (作者 [@Starjupi](https://x.com/Starjupi))

**用作者的流程說明區分概念、角色設計、指令碼、對白與聲音決策**

評論鏈解釋了流程和模型功能，但沒有公開實際生成 Prompt

[![地下烏龜水管工的喜劇場景](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D58/poster-80ebae3e19ee.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D58/video-80ebae3e19ee.mp4)

Type: Demo | Date: 2026-10-15

---

<a id="case-22"></a>
### 案例 22: [以車輛意外收尾的街頭追逐](https://x.com/_3912657840/status/2110778910019559744) (作者 [@_3912657840](https://x.com/_3912657840))

**透過人物動作、構圖和街頭狀況變化觀察喜劇節奏**

作者標註這是文生影片實驗，但沒有公開實際 Prompt

[![以車輛意外收尾的街頭追逐](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D59/poster-32460fac82cb.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D59/video-32460fac82cb.mp4)

Type: Demo | Date: 2026-10-15

---

<a id="case-23"></a>
### 案例 23: [少女發現藍龍的奇幻短片](https://x.com/nrqa__/status/2110764587113222208) (作者 [@nrqa__](https://x.com/nrqa__))

**觀察個人奇幻故事如何形成包含固定角色的組合片段**

來源展示約 95 秒短片，不代表一次生成的時長

[![少女發現藍龍的奇幻短片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D63/poster-e7d8328e9da0.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D63/video-e7d8328e9da0.mp4)

Type: Demo | Date: 2026-10-15

---

<a id="case-24"></a>
### 案例 24: [紙質載具駛入花城](https://x.com/Aiwithkami/status/2111121831528980566) (作者 [@Aiwithkami](https://x.com/Aiwithkami))

**觀察 King Cards 短剪段中的人物、載具與環境變化**

這是同一長片中被重複分享的場景，不能算成另一部獨立製作的電影

[![紙質載具駛入花城](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D66/poster-e0abfdd43b76.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D66/video-e0abfdd43b76.mp4)

Type: Demo | Date: 2026-10-16

---

<a id="case-25"></a>
### 案例 25: [紙質車廂裡的石像變成人](https://x.com/AlexM12jx/status/2111165921364504890) (作者 [@AlexM12jx](https://x.com/AlexM12jx))

**觀察移動載具內的角色位置與短暫形態變化**

片段同樣被歸於 King Cards，來源歸屬與原創作者身份的判斷分別保留

[![紙質車廂裡的石像變成人](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D69/poster-00ccb9224112.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D69/video-00ccb9224112.mp4)

Type: Demo | Date: 2026-10-16

---

<a id="case-26"></a>
### 案例 26: [魔術師與紙牌環繞的劇場](https://x.com/MelinaVale14/status/2111125493957505478) (作者 [@MelinaVale14](https://x.com/MelinaVale14))

**把中心人物表演、移動道具和周圍觀眾作為同一場景觀察**

King Cards 此段的不同編碼與短版已合併

[![魔術師與紙牌環繞的劇場](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D70/poster-b5d7e24dfed1.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D70/video-b5d7e24dfed1.mp4)

Type: Demo | Date: 2026-10-16

---

<a id="case-27"></a>
### 案例 27: [庭院足浴中的女性日常](https://x.com/Naonekozamurai/status/2111231708108575006) (作者 [@Naonekozamurai](https://x.com/Naonekozamurai))

**觀察普通手勢、服裝和安靜環境，而非複雜動作**

作者自述十秒 1080p 的生成及積分數，並對是否為活動價表示不確定

[![庭院足浴中的女性日常](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D74/poster-c60960ec9979.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D74/video-c60960ec9979.mp4)

Type: Demo | Date: 2026-10-16

---

<a id="case-28"></a>
### 案例 28: [以獵鷹串聯舉報主題短片](https://x.com/fatoomdes/status/2111180507254042955) (作者 [@fatoomdes](https://x.com/fatoomdes))

**觀察角色意象如何把手機介面鏡頭連線成一個主題表達**

作者將成片歸於 Kling 4.0，本倉庫不獨立評判片中涉及的指控

[![以獵鷹串聯舉報主題短片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D79/poster-c65afae88005.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D79/video-c65afae88005.mp4)

Type: Demo | Date: 2026-10-16

---

<a id="case-29"></a>
### 案例 29: [廚房裡躡行的橘貓](https://x.com/magnific/status/2111139954440949990) (作者 [@magnific](https://x.com/magnific))

**觀察日常室內環境中的小動作與鏡頭距離變化**

Magnific 樣片跟隨貓穿過檯面，最後落到近景

[![廚房裡躡行的橘貓](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D82/poster-ff6f8d465033.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D82/video-ff6f8d465033.mp4)

Type: Demo | Date: 2026-10-16

---

<a id="case-30"></a>
### 案例 30: [兩名男子在街角相見擁抱](https://x.com/leilamakes/status/2111108104452706636) (作者 [@leilamakes](https://x.com/leilamakes))

**觀察簡短社互動動中的接近、身體接觸與角色位置**

該媒體來自較長會話中的作者回復，所屬會話關係已經保留

[![兩名男子在街角相見擁抱](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D83/poster-57f8a9708fd1.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D83/video-57f8a9708fd1.mp4)

Type: Demo | Date: 2026-10-16

---


<a id="category-action"></a>
## ⚔️ 動作與身體互動

<a id="case-31"></a>
### 案例 31: [月下雲端雙人劍鬥](https://x.com/AiwithAmeliaa/status/2110782285691965754) (作者 [@AiwithAmeliaa](https://x.com/AiwithAmeliaa))

**用這段畫面觀察多人動作、空中排程與服裝輪廓的連續性**

兩名劍客在月下雲層交鋒，發帖賬號明確披露了廣告

[![月下雲端雙人劍鬥](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D01/poster-c67c148695e9.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D01/video-c67c148695e9.mp4)

Type: Demo | Date: 2026-10-15

---

<a id="case-32"></a>
### 案例 32: [跆拳道館內的雙人格鬥](https://x.com/Stevemnx3/status/2111039167090016566) (作者 [@Stevemnx3](https://x.com/Stevemnx3))

**對照格鬥過程中的身體接觸、雙方距離與鏡頭位置**

畫面在訓練館全景與兩名著道服人物的近身動作間切換

[![跆拳道館內的雙人格鬥](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D02/poster-1ef935905f1c.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D02/video-1ef935905f1c.mp4)

Type: Demo | Date: 2026-10-16

---

<a id="case-33"></a>
### 案例 33: [兩輛跑車穿越城市追逐](https://x.com/PromptSin/status/2111042013210825211) (作者 [@PromptSin](https://x.com/PromptSin))

**觀察快速切換鏡位時車輛身份和運動方向的延續**

紅黑兩輛跑車在城市街道與橋面上競逐

[![兩輛跑車穿越城市追逐](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D04/poster-61e7dd165825.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D04/video-61e7dd165825.mp4)

Type: Demo | Date: 2026-10-16

---

<a id="case-34"></a>
### 案例 34: [移動鏡頭下的拳擊交鋒](https://x.com/SirGlavan_/status/2110785627251704302) (作者 [@SirGlavan_](https://x.com/SirGlavan_))

**觀察出拳、防守位移與近身接觸，不只看單張好看的畫面**

兩名戴拳套的拳手在擂臺對打，鏡頭距離和角度不斷變化

[![移動鏡頭下的拳擊交鋒](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D06/poster-0a6d9253b137.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D06/video-0a6d9253b137.mp4)

Type: Demo | Date: 2026-10-15

---

<a id="case-35"></a>
### 案例 35: [穿越爆炸街道的女戰士](https://x.com/Lisa__Rodin/status/2110771984024129887) (作者 [@Lisa__Rodin](https://x.com/Lisa__Rodin))

**觀察固定角色與行駛車輛、煙霧及大規模背景特效的關係**

黑衣女性穿過受損街道，這個場景的多個版本由不同賬號重複分享

[![穿越爆炸街道的女戰士](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D07/poster-e910366e89fb.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D07/video-e910366e89fb.mp4)

Type: Demo | Date: 2026-10-15

---

<a id="case-36"></a>
### 案例 36: [少女與城市巨獸對峙](https://x.com/torotoromoney/status/2111026942489329670) (作者 [@torotoromoney](https://x.com/torotoromoney))

**跟隨城市中的衝突場景，比較人物和巨獸的體量關係**

淺發主角在損壞的建築之間面對一隻巨大觸手生物

[![少女與城市巨獸對峙](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D08/poster-699eced69da0.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D08/video-699eced69da0.mp4)

Type: Demo | Date: 2026-10-16

---

<a id="case-37"></a>
### 案例 37: [穿過外星叢林的機械捕食者](https://x.com/Alin_Reaper05/status/2110996672343917052) (作者 [@Alin_Reaper05](https://x.com/Alin_Reaper05))

**用公開 Prompt 觀察加速、環境反應和後退的手持視角**

生物結合金屬肢體與有機組織，作者在直接回復中公開了生成指令

[![穿過外星叢林的機械捕食者](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D18/poster-e28f30cd8013.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D18/video-e28f30cd8013.mp4)

**提示詞** · [公開提示詞來源](https://x.com/Alin_Reaper05/status/2110996674558530007)

```
A living mechanical predator with a glowing orange central eye moves through dense alien jungle vegetation, using long metallic limbs wrapped in pulsing flesh to pull itself between trees, organic tendrils grabbing branches while hydraulic joints extend and retract, the creature suddenly notices the camera and rapidly charges forward, handheld tracking camera retreats through foliage, branches break naturally, mud splashes, vines react realistically, intense acceleration, realistic weight and momentum, dark cinematic lighting, high-end creature VFX.
```

Type: Demo | Date: 2026-10-16

---

<a id="case-38"></a>
### 案例 38: [騎手在戰場上持長槍交鋒](https://x.com/alifcoder/status/2110980799264903190) (作者 [@alifcoder](https://x.com/alifcoder))

**觀察開闊戰場中的騎手互動、馬匹運動與武器接觸**

附件展示的是騎馬戰鬥，不把原帖關於拳擊的描述直接當成這些畫面的事實

[![騎手在戰場上持長槍交鋒](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D22/poster-98d16e333c2b.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D22/video-98d16e333c2b.mp4)

Type: Demo | Date: 2026-10-16

---

<a id="case-39"></a>
### 案例 39: [空手道交手與地墊接觸](https://x.com/WuxiaRocks/status/2110962012100653419) (作者 [@WuxiaRocks](https://x.com/WuxiaRocks))

**觀察表演者與周圍環境的接觸，不把動作僅看作孤立姿勢**

作者特別指出腳壓地墊的細節，這是來源觀察，不是量化物理測試

[![空手道交手與地墊接觸](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D24/poster-0a576d72f135.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D24/video-0a576d72f135.mp4)

Type: Demo | Date: 2026-10-16

---

<a id="case-40"></a>
### 案例 40: [便利店員工與格鬥者交手](https://x.com/seisei_ai_1st/status/2110853231316496547) (作者 [@seisei_ai_1st](https://x.com/seisei_ai_1st))

**觀察帶日語對白的動作樣例中的近身接觸與場景連續性**

作者稱對比時使用相同 Prompt，但該引用 Prompt 不在本次取得的來源集合中

[![便利店員工與格鬥者交手](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D46/poster-1b049353be78.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D46/video-1b049353be78.mp4)

Type: Demo | Date: 2026-10-15

---

<a id="case-41"></a>
### 案例 41: [石臺上的鎧甲奇幻格鬥](https://x.com/AIWarper/status/2110833050955526292) (作者 [@AIWarper](https://x.com/AIWarper))

**觀察關鍵幀驅動的風格化戰鬥中的動作排程**

作者自述使用十個關鍵幀，可見片段為開闊平臺上兩名不同裝甲人物的交手

[![石臺上的鎧甲奇幻格鬥](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D48/poster-b680150c5bc2.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D48/video-b680150c5bc2.mp4)

Type: Demo | Date: 2026-10-15

---

<a id="case-42"></a>
### 案例 42: [貓咪穿越夜間城鎮](https://x.com/umesh_ai/status/2110797373584887907) (作者 [@umesh_ai](https://x.com/umesh_ai))

**復製作者的一鏡到底 Prompt，探索相連室內外空間中的快速運動**

作者後續解釋為與 Flash 比較而選擇二十秒，此引數沒有補進原始 Prompt

[![貓咪穿越夜間城鎮](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D51/poster-074081e6557c.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D51/video-074081e6557c.mp4)

**提示詞** · [公開提示詞來源](https://x.com/umesh_ai/status/2110797376827035806)

```
An amateur handheld recording in third-person perspective rapidly follows a cat through its nighttime adventures in one continuous shot, with no cuts, no stopping, and no pause. The sequence feels like fast-forward, showing all the curious, mischievous, funny, and chaotic things a cat might do while the town, house, garden, and everything around it are half-asleep.The cat races through about ten places a cat would naturally explore at night, each one flowing into the next in a single continuous chase: a quiet bedroom, a dim hallway, a kitchen, a living room, a backyard garden, a fence line, a garage, a rooftop, a tree, and a sleepy street or alley. The camera is shaky and imperfect, always struggling to keep up as it follows close behind. In every location, the cat causes some kind of chaos. In the bedroom it jumps onto furniture and disturbs sleeping people. In the hallway it sends small objects tumbling. In the kitchen it knocks items off the counter. In the living room it darts across shelves and tips things over. In the garden it rustles plants, digs, or startles birds. On the fence it rattles loose objects. In the garage it weaves through clutter and causes things to wobble or fall. On the rooftop it skids across surfaces and startles other animals. In the tree it shakes branches and scatters leaves. In the street or alley it darts through trash, shadows, and unexpected little messes, always leaving brief chaos behind before sprinting onward.The cat behaves like a restless, curious nighttime troublemaker: climbing, leaping, squeezing through gaps, chasing tiny movements, staring at strange things, swatting objects, knocking things over, and vanishing into corners before bursting back out again. Every scene should contain a clear action, reaction, or small disaster caused by the cat.Everything around it feels sleepy and still, with dark houses, quiet gardens, dim windows, silent rooftops, and empty streets. The contrast is that the cat is pure energy, moving so quickly that the world smears into motion blur and fragmented glimpses of chaos. The overall feeling is funny, lively, mischievous, and cinematic, like a whole secret night of cat behavior compressed into one rapid continuous chase.
```

Type: Demo | Date: 2026-10-15

---

<a id="case-43"></a>
### 案例 43: [雨中森林裡的武士對決](https://x.com/AI__TSUBAKI/status/2110796958935978171) (作者 [@AI__TSUBAKI](https://x.com/AI__TSUBAKI))

**觀察雨景格鬥中的服裝穩定性與武器接觸**

作者自述十五秒、1080p、202 積分，這些是來源設定，不是當前 API 報價

[![雨中森林裡的武士對決](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D52/poster-428a2ca3573f.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D52/video-428a2ca3573f.mp4)

Type: Demo | Date: 2026-10-15

---

<a id="case-44"></a>
### 案例 44: [樹林中黑衣女性的動作片段](https://x.com/OxBairan/status/2110785228155560230) (作者 [@OxBairan](https://x.com/OxBairan))

**對照同一林間動作場景的不同編碼版本，觀察姿勢與鏡頭運動**

多個賬號重複使用這段場景的短剪輯，現已合併為一組素材

[![樹林中黑衣女性的動作片段](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D56/poster-e86261e950fa.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D56/video-e86261e950fa.mp4)

Type: Demo | Date: 2026-10-15

---

<a id="case-45"></a>
### 案例 45: [紅紙鳥對抗紫色章魚](https://x.com/AIwithkhan/status/2111128321262276695) (作者 [@AIwithkhan](https://x.com/AIwithkhan))

**觀察小型飛行主體與大型拼裝生物之間的互動**

該場景也是 King Cards 剪段，多個賬號配合近似模型釋出話術分享

[![紅紙鳥對抗紫色章魚](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D67/poster-d6f35850335e.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D67/video-d6f35850335e.mp4)

Type: Demo | Date: 2026-10-16

---

<a id="case-46"></a>
### 案例 46: [籃球運動員飛身扣籃](https://x.com/leilamakes/status/2111108072236060864) (作者 [@leilamakes](https://x.com/leilamakes))

**觀察身體軌跡、籃球位置與籃筐接觸**

這段生成體育影片來自作者回復，不被當作獨立驗證的真實身體表現

[![籃球運動員飛身扣籃](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D84/poster-d1fcc959cdd5.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D84/video-d1fcc959cdd5.mp4)

Type: Demo | Date: 2026-10-16

---


<a id="category-game"></a>
## 🎮 遊戲與載具概念

<a id="case-47"></a>
### 案例 47: [賞金獵人風格的遊戲概念](https://x.com/NyaiiBubu/status/2111040233387200905) (作者 [@NyaiiBubu](https://x.com/NyaiiBubu))

**將片段作為結合人物動作和對白的遊戲預告場景參考**

作者稱其為 AAA 風格概念，實際可見產物是生成影片，並非可玩的遊戲

[![賞金獵人風格的遊戲概念](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D05/poster-96e6493c7d87.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D05/video-96e6493c7d87.mp4)

Type: Demo | Date: 2026-10-16

---

<a id="case-48"></a>
### 案例 48: [飛車衝上夜間巨型坡道](https://x.com/higgsfield_ai/status/2110937478492479783) (作者 [@higgsfield_ai](https://x.com/higgsfield_ai))

**將片段用作電影化車輛概念參考，不當作遊戲已經可執行的證據**

帶平臺品牌的樣片跟隨汽車爬上陡坡，隨後呈現騰空效果

[![飛車衝上夜間巨型坡道](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D29/poster-9f0ea0939850.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D29/video-9f0ea0939850.mp4)

Type: Demo | Date: 2026-10-16

---

<a id="case-49"></a>
### 案例 49: [日落海岸公路上的跑車競速](https://x.com/higgsfield_ai/status/2110928479734964409) (作者 [@higgsfield_ai](https://x.com/higgsfield_ai))

**觀察競速影片概念中的追逐鏡頭、光線和儀表式疊層**

平臺樣片呈現日落海岸賽車場景，沒有提供可執行遊戲

[![日落海岸公路上的跑車競速](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D31/poster-94729ec66a60.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D31/video-94729ec66a60.mp4)

Type: Demo | Date: 2026-10-16

---

<a id="case-50"></a>
### 案例 50: [戰鬥機飛越海島環境](https://x.com/higgsfield_ai/status/2110925937634410612) (作者 [@higgsfield_ai](https://x.com/higgsfield_ai))

**用樣片觀察飛行鏡頭的運動和遊戲介面構圖**

噴氣戰機掠過明亮海岸，畫面採用遊戲式鏡位與疊層

[![戰鬥機飛越海島環境](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D33/poster-06b6b22e3e0e.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D33/video-06b6b22e3e0e.mp4)

Type: Demo | Date: 2026-10-16

---

<a id="case-51"></a>
### 案例 51: [角色在浮空島之間滑翔](https://x.com/higgsfield_ai/status/2110922885141606859) (作者 [@higgsfield_ai](https://x.com/higgsfield_ai))

**觀察第三人稱影片概念從狹窄空間轉入寬闊空景的方式**

平臺展示角色穿越風格化浮空島環境的跟隨鏡頭

[![角色在浮空島之間滑翔](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D35/poster-41fca9f81d16.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D35/video-41fca9f81d16.mp4)

Type: Demo | Date: 2026-10-16

---

<a id="case-52"></a>
### 案例 52: [跟隨騎手的摩托競速概念](https://x.com/higgsfield_ai/status/2110915957833248859) (作者 [@higgsfield_ai](https://x.com/higgsfield_ai))

**觀察遊戲式影片中的摩托動作、追逐鏡頭距離與賽道照明**

平臺樣片採用競速遊戲的展示形式，並非互動式應用

[![跟隨騎手的摩托競速概念](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D38/poster-6fbf86005055.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D38/video-6fbf86005055.mp4)

Type: Demo | Date: 2026-10-16

---

<a id="case-53"></a>
### 案例 53: [第一人稱港口射擊場景](https://x.com/higgsfield_ai/status/2110905436371370009) (作者 [@higgsfield_ai](https://x.com/higgsfield_ai))

**復製作者按時間分段的戰術射擊要求，定義十五秒視覺目標**

回覆寫 15 秒，根帖寫 30 秒，附件約 14.3 秒，這三種來源口徑分別保留

[![第一人稱港口射擊場景](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D41/poster-d66668c4a4fe.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D41/video-d66668c4a4fe.mp4)

**提示詞** · [公開提示詞來源](https://x.com/higgsfield_ai/status/2110906696851955916)

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
### 案例 54: [未來城市中的飛行汽車](https://x.com/YapayZekaSerisi/status/2111104253817155607) (作者 [@YapayZekaSerisi](https://x.com/YapayZekaSerisi))

**透過概念畫面觀察街面駕駛、飛行和城市地標之間的轉換**

可見產物為未來交通影片，來源未提供可玩的遊戲

[![未來城市中的飛行汽車](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D72/poster-78d337068f01.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D72/video-78d337068f01.mp4)

Type: Demo | Date: 2026-10-16

---

<a id="case-55"></a>
### 案例 55: [警車追逐穿城飛車](https://x.com/higgsfield_ai/status/2111235977406763103) (作者 [@higgsfield_ai](https://x.com/higgsfield_ai))

**觀察追逐鏡頭概念如何結合地面車流與騰空動作**

Higgsfield 將其展示為平臺上的另一個 Kling 4.0 遊戲概念例子

[![警車追逐穿城飛車](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D73/poster-d291f74977e7.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D73/video-d291f74977e7.mp4)

Type: Demo | Date: 2026-10-16

---

<a id="case-56"></a>
### 案例 56: [海濱駕駛轉入直升機飛行](https://x.com/frameo_ai/status/2111097408633639000) (作者 [@frameo_ai](https://x.com/frameo_ai))

**觀察跑車、步行人物和空中鏡頭之間的轉換**

Frameo 展示的是遊戲式影片概念和接入預告，並非可執行遊戲

[![海濱駕駛轉入直升機飛行](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D87/poster-31d433ad4429.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D87/video-31d433ad4429.mp4)

Type: Demo | Date: 2026-10-16

---


<a id="category-animation"></a>
## 🎨 動畫與風格化角色

<a id="case-57"></a>
### 案例 57: [插畫與實拍風格交織的音樂影片](https://x.com/IntLab0000/status/2111016713869463957) (作者 [@IntLab0000](https://x.com/IntLab0000))

**觀察完整 MV 如何結合不同風格和反覆出現的情緒意象**

作者自述使用 MCP 輔助製作，約 136 秒的附件是組合成片，不是單次生成時長的證明

[![插畫與實拍風格交織的音樂影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D10/poster-32d9ded7f2d0.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D10/video-32d9ded7f2d0.mp4)

Type: Demo | Date: 2026-10-16

---

<a id="case-58"></a>
### 案例 58: [廚房裡的奶奶與迷你黏土龍](https://x.com/higgsfield_ai/status/2110927330390790226) (作者 [@higgsfield_ai](https://x.com/higgsfield_ai))

**觀察緊湊廚房動畫中的角色互動與材質風格**

畫面結合微型龍、烹飪物件和黏土質感的視覺處理

[![廚房裡的奶奶與迷你黏土龍](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D32/poster-1098bee49c56.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D32/video-1098bee49c56.mp4)

Type: Demo | Date: 2026-10-16

---

<a id="case-59"></a>
### 案例 59: [夜市攤位上的動漫廚師](https://x.com/higgsfield_ai/status/2110922265340891255) (作者 [@higgsfield_ai](https://x.com/higgsfield_ai))

**觀察短篇烹飪動畫中的手部動作、道具與照明**

平臺自有樣片展示一位插畫風格廚師在熱鬧攤位前工作

[![夜市攤位上的動漫廚師](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D36/poster-a89dc333a50c.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D36/video-a89dc333a50c.mp4)

Type: Demo | Date: 2026-10-16

---

<a id="case-60"></a>
### 案例 60: [微縮人物的定格風格戰鬥](https://x.com/higgsfield_ai/status/2110910617574121905) (作者 [@higgsfield_ai](https://x.com/higgsfield_ai))

**觀察微縮比例和定格風格如何塑造短動作片段**

小武士對抗紅色生物，生成耗時說法仍屬於平臺自述

[![微縮人物的定格風格戰鬥](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D40/poster-0096a333b2d9.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D40/video-0096a333b2d9.mp4)

Type: Demo | Date: 2026-10-16

---

<a id="case-61"></a>
### 案例 61: [發光月牙座椅上的睡眠場景](https://x.com/minuitIA/status/2110823653336027226) (作者 [@minuitIA](https://x.com/minuitIA))

**用場景觀察裝飾性光線主題與輕微人物動作**

創作者把睡前人物意象延展為一段月亮主題的短視覺片段

[![發光月牙座椅上的睡眠場景](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D49/poster-cadca8a36e4a.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D49/video-cadca8a36e4a.mp4)

Type: Demo | Date: 2026-10-15

---

<a id="case-62"></a>
### 案例 62: [城市路口的快閃群舞](https://x.com/seisei_ai_1st/status/2110790316584562789) (作者 [@seisei_ai_1st](https://x.com/seisei_ai_1st))

**觀察街舞片段中的群體動作、空間排列與視角變化**

作者用經常測試的快閃題材展示新模型效果

[![城市路口的快閃群舞](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D54/poster-0f0e0bc769b1.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D54/video-0f0e0bc769b1.mp4)

Type: Demo | Date: 2026-10-15

---

<a id="case-63"></a>
### 案例 63: [暴風雲下的動漫劍客對決](https://x.com/Dani__oros/status/2110790297458544971) (作者 [@Dani__oros](https://x.com/Dani__oros))

**觀察風格化格鬥中清晰的人物輪廓與兵刃互動**

作者稱這是用較模糊 Prompt 完成的初次測試，但未在根帖公開該 Prompt

[![暴風雲下的動漫劍客對決](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D55/poster-28acdf9e07a3.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D55/video-28acdf9e07a3.mp4)

Type: Demo | Date: 2026-10-15

---

<a id="case-64"></a>
### 案例 64: [黑白舞臺上的多人舞蹈](https://x.com/MO_IAI/status/2110784427408105640) (作者 [@MO_IAI](https://x.com/MO_IAI))

**在去除色彩的條件下觀察編舞與燈光**

來源展示多位舞者與不斷變化的隊形組合

[![黑白舞臺上的多人舞蹈](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D57/poster-0bf2843739e2.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D57/video-0bf2843739e2.mp4)

Type: Demo | Date: 2026-10-15

---

<a id="case-65"></a>
### 案例 65: [森林裡玩雪的松鼠](https://x.com/fAIkout/status/2110768302851342454) (作者 [@fAIkout](https://x.com/fAIkout))

**觀察富於表情的動物動作與統一的柔和動畫風格**

創作者樣片跟隨小松鼠和積雪、林間物件互動

[![森林裡玩雪的松鼠](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D62/poster-c2c730ddad9a.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D62/video-c2c730ddad9a.mp4)

Type: Demo | Date: 2026-10-15

---

<a id="case-66"></a>
### 案例 66: [紅衣人物穿過糖果世界](https://x.com/jji1jj/status/2111165487648301173) (作者 [@jji1jj](https://x.com/jji1jj))

**觀察風格化人物動作與由甜點構成的環境**

這是 King Cards 中視覺不同的場景研究，不是另一部獨立製作的電影

[![紅衣人物穿過糖果世界](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D71/poster-f533cc90221d.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D71/video-f533cc90221d.mp4)

Type: Demo | Date: 2026-10-16

---

<a id="case-67"></a>
### 案例 67: [戴王冠的白貓吃咖哩](https://x.com/craftcapitallab/status/2111200513924731150) (作者 [@craftcapitallab](https://x.com/craftcapitallab))

**觀察服裝、食物道具與表情如何支撐動物角色短故事**

作者把王冠白貓與咖哩結合，片尾使用裝飾性標題

[![戴王冠的白貓吃咖哩](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D77/poster-0c65da3cad85.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D77/video-0c65da3cad85.mp4)

Type: Demo | Date: 2026-10-16

---


<a id="category-world"></a>
## 🌍 世界場景與生物

<a id="case-68"></a>
### 案例 68: [從森林旅程轉入騎龍飛行](https://x.com/Lianaalane/status/2110953699250151850) (作者 [@Lianaalane](https://x.com/Lianaalane))

**觀察畫面如何從封閉樹林逐步展開為空中遠景**

人物騎龍從森林飛向山谷，同一片段的重複編碼版本已合併

[![從森林旅程轉入騎龍飛行](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D13/poster-ea2c6c571381.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D13/video-ea2c6c571381.mp4)

Type: Demo | Date: 2026-10-16

---

<a id="case-69"></a>
### 案例 69: [恐怖蒙太奇中的無麵人形](https://x.com/h_ashizawaJP/status/2110999675709034742) (作者 [@h_ashizawaJP](https://x.com/h_ashizawaJP))

**觀察怪物形象的連續性及不同詭異意象之間的轉場**

蒼白人形、扭曲面孔和昏暗樹林對應作者關於生成音效與後期混音的討論

[![恐怖蒙太奇中的無麵人形](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D16/poster-f97b54673926.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D16/video-f97b54673926.mp4)

Type: Demo | Date: 2026-10-16

---

<a id="case-70"></a>
### 案例 70: [甦醒的球形外星聚落](https://x.com/Alin_Reaper05/status/2110997688682770563) (作者 [@Alin_Reaper05](https://x.com/Alin_Reaper05))

**復製作者公開的 Prompt，探索虛構小鎮中多種環境運動的配合**

回覆指定了旋轉機械房屋、有機管道、小機器人、淺水及上升鏡頭

[![甦醒的球形外星聚落](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D17/poster-0727879b80e3.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D17/video-0727879b80e3.mp4)

**提示詞** · [公開提示詞來源](https://x.com/Alin_Reaper05/status/2110997691274580344)

```
A colorful alien settlement filled with enormous spherical buildings and bizarre organic machines comes alive at sunrise, round red mechanical houses rotate their giant lens-like windows, pipes expand and contract like breathing organs, small robotic creatures run through shallow water, flying vehicles weave between towers, camera glides smoothly through the town at ground level before rising above the rooftops, puddles reflecting neon lights and clouds, natural vegetation moving in the wind, playful but believable extraterrestrial world, cinematic photorealism.
```

Type: Demo | Date: 2026-10-16

---

<a id="case-71"></a>
### 案例 71: [外星巨獸涉過淺水湖](https://x.com/Alin_Reaper05/status/2110982741491904596) (作者 [@Alin_Reaper05](https://x.com/Alin_Reaper05))

**復製作者的 Prompt，探索體重、水面反應和緩慢升鏡**

兩隻長頸巨獸穿過青綠色水面，周圍是紅色植被與黃綠色天空

[![外星巨獸涉過淺水湖](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D20/poster-51289a03af36.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D20/video-51289a03af36.mp4)

**提示詞** · [公開提示詞來源](https://x.com/Alin_Reaper05/status/2110982744247353611)

```
Two enormous long-necked alien animals slowly walk through a shallow turquoise lagoon surrounded by bright red grass and exotic palm forests. Their massive bodies create realistic waves and splashes with every step while smaller creatures flee along the shoreline. The camera begins low near the water and smoothly cranes upward, revealing the gigantic animals against a glowing yellow-green sky and distant mountains. Realistic weight and inertia, detailed skin movement, volumetric mist, natural vegetation motion, cinematic alien wildlife documentary, smooth continuous camera movement, highly coherent anatomy.
```

Type: Demo | Date: 2026-10-16

---

<a id="case-72"></a>
### 案例 72: [巨型機甲從甲板起飛](https://x.com/PDyv9gdatT4132/status/2110948121295696380) (作者 [@PDyv9gdatT4132](https://x.com/PDyv9gdatT4132))

**觀察機械關節、體量與從站立轉入飛行的過程**

作者釋出的樣片展示大型機器人啟動並從艦船式甲板升起

[![巨型機甲從甲板起飛](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D25/poster-621b9b81c745.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D25/video-621b9b81c745.mp4)

Type: Demo | Date: 2026-10-16

---

<a id="case-73"></a>
### 案例 73: [巨獸逼近擁堵的懸索橋](https://x.com/jji1jj/status/2110775129043320994) (作者 [@jji1jj](https://x.com/jji1jj))

**觀察暴雨環境中巨獸、車輛和人群之間的比例關係**

後續帖子複用了同一畫面，保留為補充來源而不是新案例

[![巨獸逼近擁堵的懸索橋](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D60/poster-cdf43480c9f5.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D60/video-cdf43480c9f5.mp4)

Type: Demo | Date: 2026-10-15

---

<a id="case-74"></a>
### 案例 74: [報紙載具穿越紙質城市](https://x.com/Gemalpha_88/status/2111113629919854891) (作者 [@Gemalpha_88](https://x.com/Gemalpha_88))

**觀察摺紙風城市中的環境材質一致性與跟隨鏡頭**

畫面來自被重複分享的 King Cards，並非另一項獨立驗證的製作專案

[![報紙載具穿越紙質城市](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D68/poster-692aeb10394f.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D68/video-692aeb10394f.mp4)

Type: Demo | Date: 2026-10-16

---

<a id="case-75"></a>
### 案例 75: [山坡上的重型步行機甲](https://x.com/ojiji2025/status/2111218605069365688) (作者 [@ojiji2025](https://x.com/ojiji2025))

**觀察機械運動、地面接觸與超大武器之間的關係**

創作者分享首次機甲嘗試，並非有工程文件支援的模擬

[![山坡上的重型步行機甲](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D75/poster-dd1ae88aa463.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D75/video-dd1ae88aa463.mp4)

Type: Demo | Date: 2026-10-16

---

<a id="case-76"></a>
### 案例 76: [哥特人物穿行雨夜](https://x.com/fabulatenebris/status/2111183079955951804) (作者 [@fabulatenebris](https://x.com/fabulatenebris))

**觀察氛圍、輪廓和反覆出現的視覺主題**

來源呈現帶昏暗人物與城堡式環境的風格化雨夜作品

[![哥特人物穿行雨夜](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D78/poster-6a014db111fa.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D78/video-6a014db111fa.mp4)

Type: Demo | Date: 2026-10-16

---

<a id="case-77"></a>
### 案例 77: [紙質車廂進入發光菌菇隧道](https://x.com/Hope_Ai01/status/2111146114972058097) (作者 [@Hope_Ai01](https://x.com/Hope_Ai01))

**觀察畫面如何從受限的車廂視角轉入明亮環境**

這是另一個 King Cards 剪段，相關來源關係已經保留

[![紙質車廂進入發光菌菇隧道](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D81/poster-9d22c4d4055d.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D81/video-9d22c4d4055d.mp4)

Type: Demo | Date: 2026-10-16

---


<a id="category-evaluation"></a>
## 🔬 對比與評測

<a id="case-78"></a>
### 案例 78: [同一森林格鬥 Prompt 的雙模型對比](https://x.com/AibeginnerR8/status/2110935157503041672) (作者 [@AibeginnerR8](https://x.com/AibeginnerR8))

**比較兩路顯示結果，同時保留作者宣告的設定和評價邊界**

兩路都標註 720p，並使用 Kling 音訊；作者在本例中認為 Seedance 更遵循分鏡、時長與動作要求

[![同一森林格鬥 Prompt 的雙模型對比](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D30/poster-a0590043e48c.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D30/video-a0590043e48c.mp4)

**提示詞** · [公開提示詞來源](https://x.com/AibeginnerR8/status/2110935160434610592)

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
### 案例 79: [咖啡館裡的固定雙人對白](https://x.com/tanabe_fragm/status/2110887676832543125) (作者 [@tanabe_fragm](https://x.com/tanabe_fragm))

**用公開對白 Prompt 測試輪流說話與側臉口型同步**

作者報價按十秒計算，附件約十五秒，未獨立驗證音訊或計費

[![咖啡館裡的固定雙人對白](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D44/poster-293ead53e5df.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D44/video-293ead53e5df.mp4)

**提示詞** · [公開提示詞來源](https://x.com/tanabe_fragm/status/2110887676832543125)

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
### 案例 80: [標準版與 Flash 的五人對白](https://x.com/onofumi_AI/status/2110866433198702728) (作者 [@onofumi_AI](https://x.com/onofumi_AI))

**比較作者展示的兩路結果中的角色位置與場景構圖**

來源自述場景長二十秒，分別消耗 180 與 120 積分，這些數值僅代表該作者賬號口徑

[![標準版與 Flash 的五人對白](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D45/poster-1007d8f82463.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D45/video-1007d8f82463.mp4)

Type: Evaluation | Date: 2026-10-15

---

<a id="case-81"></a>
### 案例 81: [虎頭人物測試近身動作](https://x.com/ozansihay/status/2110763522099474800) (作者 [@ozansihay](https://x.com/ozansihay))

**用創作者的格鬥片段觀察高接觸動作與角色參考圖的作用**

作者仍偏好 Seedance 的身體接觸表現，自述三十秒 1080p 花費 405 積分，並披露推廣

[![虎頭人物測試近身動作](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D64/poster-e99a824137b0.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D64/video-e99a824137b0.mp4)

Type: Evaluation | Date: 2026-10-15

---

<a id="case-82"></a>
### 案例 82: [音畫漂移測試中的變化主持人](https://x.com/plasm0/status/2110763509307064539) (作者 [@plasm0](https://x.com/plasm0))

**把樣片作為獨立測量同步效果的起點**

作者聲稱測試透過，抽樣畫面只確認主持人發生變化，並未驗證語音同步準確性

[![音畫漂移測試中的變化主持人](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D65/poster-285b037dd41e.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D65/video-285b037dd41e.mp4)

Type: Evaluation | Date: 2026-10-15

---

<a id="case-83"></a>
### 案例 83: [同一飛車概念的雙模型對比](https://x.com/itsPolloAI/status/2111097887656726915) (作者 [@itsPolloAI](https://x.com/itsPolloAI))

**比較兩條帶標籤的影片軌道，同時保留平臺的對比口徑**

Pollo AI 稱使用了相同 Prompt，但沒有給出實際 Prompt 或多次受控測試

[![同一飛車概念的雙模型對比](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D86/poster-f8698ad3f5cb.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D86/video-f8698ad3f5cb.mp4)

Type: Evaluation | Date: 2026-10-16

---

## 相關倉庫

尚未驗證當前模型的可用路由，因此暫不連結專用 Kling 4 API 或 Skill 倉庫；相鄰模型的資料可參考 [Seedance 2.5 指南](https://github.com/EvoLinkAI/awesome-seedance-2.5-guide)，該指南討論不同模型，不能據此驗證本倉庫的 Kling 案例

<a id="acknowledge"></a>
## 🙏 致謝

感謝本資料集中公開分享內容的賬號：

[@_3912657840](https://x.com/_3912657840), [@_lexers](https://x.com/_lexers), [@agi_aibusi](https://x.com/agi_aibusi), [@AI__TSUBAKI](https://x.com/AI__TSUBAKI), [@AibeginnerR8](https://x.com/AibeginnerR8), [@AIWarper](https://x.com/AIWarper), [@AiwithAmeliaa](https://x.com/AiwithAmeliaa), [@Aiwithkami](https://x.com/Aiwithkami), [@AIwithkhan](https://x.com/AIwithkhan), [@AlexM12jx](https://x.com/AlexM12jx), [@alifcoder](https://x.com/alifcoder), [@Alin_Reaper05](https://x.com/Alin_Reaper05), [@Bic_Revelation](https://x.com/Bic_Revelation), [@craftcapitallab](https://x.com/craftcapitallab), [@Dani__oros](https://x.com/Dani__oros), [@Diplomeme](https://x.com/Diplomeme), [@dylannknox](https://x.com/dylannknox), [@ErnestoSOFTWARE](https://x.com/ErnestoSOFTWARE), [@fabulatenebris](https://x.com/fabulatenebris), [@fAIkout](https://x.com/fAIkout), [@fatoomdes](https://x.com/fatoomdes), [@frameo_ai](https://x.com/frameo_ai), [@Gemalpha_88](https://x.com/Gemalpha_88), [@h_ashizawaJP](https://x.com/h_ashizawaJP), [@higgsfield_ai](https://x.com/higgsfield_ai), [@Hope_Ai01](https://x.com/Hope_Ai01), [@iam_mian7](https://x.com/iam_mian7), [@IntLab0000](https://x.com/IntLab0000), [@itsPolloAI](https://x.com/itsPolloAI), [@jerrod_lew](https://x.com/jerrod_lew), [@jji1jj](https://x.com/jji1jj), [@leilamakes](https://x.com/leilamakes), [@lexx_aura](https://x.com/lexx_aura), [@Lianaalane](https://x.com/Lianaalane), [@liluocheng13](https://x.com/liluocheng13), [@Lisa__Rodin](https://x.com/Lisa__Rodin), [@magnific](https://x.com/magnific), [@MelinaVale14](https://x.com/MelinaVale14), [@minuitIA](https://x.com/minuitIA), [@MO_IAI](https://x.com/MO_IAI), [@Naonekozamurai](https://x.com/Naonekozamurai), [@nrqa__](https://x.com/nrqa__), [@NyaiiBubu](https://x.com/NyaiiBubu), [@ojiji2025](https://x.com/ojiji2025), [@onofumi_AI](https://x.com/onofumi_AI), [@OxBairan](https://x.com/OxBairan), [@ozansihay](https://x.com/ozansihay), [@PDyv9gdatT4132](https://x.com/PDyv9gdatT4132), [@plasm0](https://x.com/plasm0), [@PromptSin](https://x.com/PromptSin), [@seisei_ai_1st](https://x.com/seisei_ai_1st), [@SirGlavan_](https://x.com/SirGlavan_), [@sophiaparkerr_](https://x.com/sophiaparkerr_), [@Starjupi](https://x.com/Starjupi), [@Stevemnx3](https://x.com/Stevemnx3), [@tanabe_fragm](https://x.com/tanabe_fragm), [@techhalla](https://x.com/techhalla), [@torotoromoney](https://x.com/torotoromoney), [@tphuang](https://x.com/tphuang), [@umesh_ai](https://x.com/umesh_ai), [@WuxiaRocks](https://x.com/WuxiaRocks), [@YapayZekaSerisi](https://x.com/YapayZekaSerisi), [@z933TfmXkaISSVc](https://x.com/z933TfmXkaISSVc)

第三方影片、圖片和提示詞仍受各自權利約束，倉庫編輯文字與結構採用 [CC BY 4.0](LICENSE)，這不代表重新授權第三方素材；如需更正署名、權屬或轉載，請[提交 Issue](https://github.com/cheercheung/awesome-kling-4-usecases/issues)，並參閱[媒體政策](docs/media-policy.md)與[貢獻說明](CONTRIBUTING.md)

[檢視 EvoLink 影片模型](https://evolink.ai/models?utm_source=github&utm_medium=footer&utm_campaign=awesome-kling-4-usecases&utm_content=zh-TW_footer)
