<div align="center">

# Kling 4 Use Cases

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](LICENSE)
[![EvoLink](https://img.shields.io/badge/Explore_video_models-EvoLink-black)](https://evolink.ai/models?utm_source=github&utm_medium=badge&utm_campaign=awesome-kling-4-usecases&utm_content=ja_badge)

[![English](https://img.shields.io/badge/English-111111)](README.md) [![Español](https://img.shields.io/badge/Espa%C3%B1ol-ffb703)](README_es.md) [![Português](https://img.shields.io/badge/Portugu%C3%AAs-2a9d8f)](README_pt.md) [![日本語](https://img.shields.io/badge/%E6%97%A5%E6%9C%AC%E8%AA%9E-52b788)](README_ja.md) [![한국어](https://img.shields.io/badge/%ED%95%9C%EA%B5%AD%EC%96%B4-4ea8de)](README_ko.md) [![Deutsch](https://img.shields.io/badge/Deutsch-f4a261)](README_de.md) [![Français](https://img.shields.io/badge/Fran%C3%A7ais-e76f51)](README_fr.md) [![Türkçe](https://img.shields.io/badge/T%C3%BCrk%C3%A7e-d62828)](README_tr.md) [![繁體中文](https://img.shields.io/badge/%E7%B9%81%E9%AB%94%E4%B8%AD%E6%96%87-8338ec)](README_zh-TW.md) [![简体中文](https://img.shields.io/badge/%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87-ef476f)](README_zh-CN.md) [![Русский](https://img.shields.io/badge/%D0%A0%D1%83%D1%81%D1%81%D0%BA%D0%B8%D0%B9-577590)](README_ru.md)

</div>

## 🍌 はじめに

**公開動画、作者の制作手順、公開された Prompt を通じて Kling 4 / 4.0 を調べる資料集です。** 映像制作者、クリエイティブ開発者、モデル評価者が具体的な観察・試験対象を選べるようにまとめています。各ケースは元投稿と投稿アカウントにリンクします。

表紙画像をクリックして動画を見て、根拠の説明を読んでください。作者が実際に公開した場合だけ Prompt をコピーできます。投稿者は配信者の場合もあり、ここでの署名は原作者の確認を意味しません。

[EvoLink の動画モデルを見る](https://evolink.ai/models?utm_source=github&utm_medium=introduction&utm_campaign=awesome-kling-4-usecases&utm_content=ja_introduction)

## 📊 概要

**83ケース・10ケースに11組の公開 Prompt・8分類。** 制作手順、広告、物語、動作、ゲーム風コンセプト、アニメ、世界、比較を扱います。各ケースには出典、アカウント、活用の着眼点、媒体、種類、UTC の出典日付があります。

> [!NOTE]
> 出典に基づく例であり、独立検証した Kling API 呼び出しや統制された評価ではありません。同じ作品の別の抜粋も含みます。ゲーム風動画は遊べるゲームではなく、編集映画の長さはネイティブ生成時間ではありません。価格とポイントは作者の説明として扱います。

[ケースデータ](data/use-cases.json)または[並べ替え可能な CSV](data/use-cases.csv)には収集時の反応数、Prompt の有無、出典関係が含まれます。[収集範囲](docs/collection-scope.md)で二つの検索期間と間の空白を確認できます。固定日時の資料集であり、網羅的なリアルタイム索引ではありません。

<a id="quick-start"></a>
## ⚡ はじめ方

1. [EvoLink の動画モデルを見る](https://evolink.ai/models?utm_source=github&utm_medium=quick_start&utm_campaign=awesome-kling-4-usecases&utm_content=ja_quick_start)でアカウント作成またはログイン
2. 対応モデルを使う際は[API キーを作成・取得](https://evolink.ai/dashboard/keys?utm_source=github&utm_medium=api_key&utm_campaign=awesome-kling-4-usecases&utm_content=ja_api_key)
3. タスク送信前にモデルの可用性を確認する **2026-10-17 時点で、本資料集は Kling 4 の API 経路と専用のインストール可能な Skill を検証していない** [Codex CLI 設定ガイドを読む](https://evolink.ai/docs/en/cli/codex?utm_source=github&utm_medium=setup_docs&utm_campaign=awesome-kling-4-usecases&utm_content=ja_setup_docs)で一般的な設定を確認できますが、Kling 4 の検証済み初回呼び出し例ではありません

このリポジトリは調査と創作の参考資料です。実行可能な API 例やモデルインストーラーは含みません。ケースを再現する際、別の Kling バリアントで置き換えないでください。

## 📑 目次

| ケース | 分類 | 観察の着眼点 | 種類 |
|---|---|---|---|
| [SF映像の人物と環境の参照シート](#case-1) | 制作手順と参照資料 | 人物表と環境表が長い映像指示とどう併記されるか確認する | Demo |
| [エージェントの絵コンテからアニメ映像へ](#case-2) | 制作手順と参照資料 | 脚本、絵コンテ、Prompt をつなぐ作者の手順を短編アニメの計画に生かす | Tutorial |
| [壮大な幻想場面と参照シート](#case-3) | 制作手順と参照資料 | 人物表、環境表、長い場面指示の対応を確認する | Demo |
| [動画タスクを追うスマートフォンのチャット](#case-4) | 制作手順と参照資料 | 作者が提案する Codex から MCP への接続を確認し、検証済みの自分のツールで再現する | Tutorial |
| [森林道路を走る起亜SUVの広告](#case-5) | 広告と商品物語 | 公開された15カットの指示で30秒広告の車両連続性を計画する | Demo |
| [複数人物によるスキンケアUGC広告](#case-6) | 広告と商品物語 | 見える広告形式を参考に、制作記録を残す UGC 実験を計画する | Demo |
| [小さなドラゴンがデザートをキャラメリゼ](#case-7) | 広告と商品物語 | 一つの具体的な調理動作を通じて、人物主導の商品物語を調べる | Demo |
| [オレンジジュースの紙パックの広告映像](#case-8) | 広告と商品物語 | 単一商品を中心に包装の見え方、果物のモチーフ、場面転換を確認する | Demo |
| [淡い緑の部屋にいるヘッドホン姿の少女](#case-9) | 人物と物語 | 接写、全身の動き、同じ背景の間で人物の外観を確認する | Demo |
| [古典的な列柱廊へ近づく男性](#case-10) | 人物と物語 | 見える範囲で控えめな動きと建築背景の連続性を確認する | Demo |
| [濡れた髪の女性を捉える感情的な接写](#case-11) | 人物と物語 | 会話中心の演技で微細な表情変化と画面構成を調べる | Demo |
| [映画館で時間を共有する母と子](#case-12) | 人物と物語 | 短い感情表現を具体的な個人の物語に結びつける方法を調べる | Demo |
| [二人の司会者による日本語ニュース](#case-13) | 人物と物語 | 会話、二人の配置、画面内の文字図形に絞った評価を設計する | Demo |
| [オフィスのロビーを走る小さなカート](#case-14) | 人物と物語 | 日常建築に意外な乗り物を置き、喜劇的な大きさの対比を調べる | Demo |
| [恋人の視点で見る夏の散歩](#case-15) | 人物と物語 | 詳しい公開指示をコピーし、日常のしぐさで30秒の流れを計画する | Demo |
| [車両や兵士と人物接写の映像集](#case-16) | 人物と物語 | モンタージュから具体的な課題を選び、個別の条件付き試験につなげる | Demo |
| [King Cardsの魔術と都市飛行](#case-17) | 人物と物語 | 長めの作品が舞台魔術、紙の乗り物、繰り返し登場する赤い鳥をどうつなぐか調べる | Demo |
| [トラクターとともに嵐に向き合う農村の女性](#case-18) | 人物と物語 | 人物、機械、天候が短い物語の前提を伝える方法を確認する | Demo |
| [恐竜冒険映画と再利用できるショット指示](#case-19) | 人物と物語 | 完成作品と、作者が公開した7秒のアクションおよび8秒の運転指示を見比べる | Demo |
| [異世界につながるエレベーターを開く配達員](#case-20) | 人物と物語 | 同じ主人公が、見慣れた扉の先で変わる環境にどう反応するか確認する | Demo |
| [地下の亀の配管工を描くコメディ](#case-21) | 人物と物語 | 作者の制作説明から概念、人物設計、脚本、会話、音声の判断を分けて理解する | Demo |
| [車の意外な展開で終わる街頭の追跡](#case-22) | 人物と物語 | 人物の動き、構図、街路状況の変化で喜劇の間を調べる | Demo |
| [青いドラゴンを見つける若いヒロイン](#case-23) | 人物と物語 | 個人的な幻想物語が同じ登場人物を含む編集映像になる過程を調べる | Demo |
| [紙の乗り物で花の街へ向かう旅](#case-24) | 人物と物語 | King Cards の短い抜粋で人物、乗り物、背景の変化を調べる | Demo |
| [紙の馬車で石の乗客が人間に変わる](#case-25) | 人物と物語 | 動く乗り物の中で位置を追いながら短い変身を確認する | Demo |
| [円形劇場をカードで満たす魔術師](#case-26) | 人物と物語 | 中心の演技、動く小道具、周囲の観客を同じ場面として確認する | Demo |
| [中庭で足湯を楽しむ女性](#case-27) | 人物と物語 | 複雑なアクションではなく日常のしぐさ、衣服、静かな背景を調べる | Demo |
| [鷹を軸にした通報テーマの短編](#case-28) | 人物と物語 | キャラクターのモチーフがスマートフォン画面を主題に結びつける方法を調べる | Demo |
| [台所を忍び歩く茶トラ猫](#case-29) | 人物と物語 | 身近な室内で小さな動作とカメラ距離の変化を調べる | Demo |
| [街で出会い抱き合う二人の男性](#case-30) | 人物と物語 | 短い交流の中で接近、身体接触、人物位置を確認する | Demo |
| [月夜の雲上で繰り広げる剣の決闘](#case-31) | 動作と身体接触 | 複数人物の動き、空中での配置、衣装の輪郭の連続性を確認する | Demo |
| [道場でのテコンドーの組手](#case-32) | 動作と身体接触 | 身体接触、間合いの変化、カメラ位置を比較する | Demo |
| [市街地を追走する二台のスポーツカー](#case-33) | 動作と身体接触 | 素早いカメラ切り替えの中で車両の同一性と進行方向を確認する | Demo |
| [動くカメラで捉えるボクシング](#case-34) | 動作と身体接触 | 一枚の見栄えだけでなく、パンチ、防御の移動、接近時の接触を調べる | Demo |
| [爆発する街路を進む女性戦士](#case-35) | 動作と身体接触 | 同じ人物と車両、煙、大規模な背景効果の関係を確認する | Demo |
| [都市の怪物と対峙する少女](#case-36) | 動作と身体接触 | 市街地での対決を追いながら人物と怪物の大きさを比べる | Demo |
| [異星の密林を突進する機械の捕食者](#case-37) | 動作と身体接触 | 公開 Prompt で加速、環境の反応、後退する手持ち視点を調べる | Demo |
| [槍を交える騎馬の戦士](#case-38) | 動作と身体接触 | 開けた戦場で騎手の相互作用、馬の動き、武器接触を確認する | Demo |
| [床のマットと接触する空手の組手](#case-39) | 動作と身体接触 | 孤立したポーズではなく演者と周囲の接触を調べる | Demo |
| [コンビニ店員と格闘者の対決](#case-40) | 動作と身体接触 | 日本語会話のあるアクションで近接接触と場面の連続性を調べる | Demo |
| [石の台上で戦う鎧の幻想戦士](#case-41) | 動作と身体接触 | キーフレームに基づくポーズを使った戦闘の配置を調べる | Demo |
| [夜の町を駆け抜ける猫](#case-42) | 動作と身体接触 | 一続きのショットを求める Prompt で、つながった屋内外の高速移動を試す | Demo |
| [雨の森で戦う侍](#case-43) | 動作と身体接触 | 雨の激しい戦闘で衣装の安定性と武器の接触を調べる | Demo |
| [森で戦う黒い服の女性](#case-44) | 動作と身体接触 | 同じ森林アクションの再エンコード版を比べ、姿勢とカメラ移動を確認する | Demo |
| [紫のタコと対峙する赤い紙の鳥](#case-45) | 動作と身体接触 | 小さな飛行主体と大きな組み立て生物の相互作用を調べる | Demo |
| [空中でダンクするバスケットボール選手](#case-46) | 動作と身体接触 | 身体の軌道、ボール位置、リングとの接触を調べる | Demo |
| [賞金稼ぎを描くゲーム風コンセプト](#case-47) | ゲームと乗り物のコンセプト | 人物の動作と会話を組み合わせたゲーム予告の参考として使う | Demo |
| [夜の巨大な斜面を登る空飛ぶ車](#case-48) | ゲームと乗り物のコンセプト | 動くゲームの証拠ではなく、映画的な乗り物コンセプトの参考にする | Demo |
| [夕暮れの海岸道路を走るスポーツカー](#case-49) | ゲームと乗り物のコンセプト | 追走カメラ、照明、計器風の表示をレース映像の参考として調べる | Demo |
| [島の景観を飛ぶ戦闘機](#case-50) | ゲームと乗り物のコンセプト | 飛行カメラの動きとゲーム風インターフェースの構成を調べる | Demo |
| [浮遊島の間を滑空する人物](#case-51) | ゲームと乗り物のコンセプト | 三人称視点の映像で狭い場所から広い空景へ移る方法を調べる | Demo |
| [ライダーを追うバイクレースのコンセプト](#case-52) | ゲームと乗り物のコンセプト | バイクの動き、追走距離、コースの照明を調べる | Demo |
| [港湾を舞台にした一人称射撃映像](#case-53) | ゲームと乗り物のコンセプト | 作者の時間指定付き戦術射撃指示をコピーし、15秒の映像目標を定める | Demo |
| [未来都市を飛ぶ自動車](#case-54) | ゲームと乗り物のコンセプト | 路上走行、飛行、都市の目印の間の移行を確認する | Demo |
| [都市の空飛ぶ車を追う警察](#case-55) | ゲームと乗り物のコンセプト | 追走カメラが地上交通と飛行のような動きをどう結ぶか調べる | Demo |
| [海岸のドライブからヘリコプター飛行へ](#case-56) | ゲームと乗り物のコンセプト | 車両、歩く人物、空中映像の間の切り替えを調べる | Demo |
| [イラストと実写風映像を組み合わせた音楽動画](#case-57) | アニメと様式化した人物 | 完成した MV が異なる画風と繰り返す感情的モチーフをどう結ぶか調べる | Demo |
| [台所で出会うおばあさんと小さな粘土ドラゴン](#case-58) | アニメと様式化した人物 | 短い台所アニメの人物間交流と素材表現を確認する | Demo |
| [夜市で料理するアニメのシェフ](#case-59) | アニメと様式化した人物 | 短い料理アニメで手の動き、道具、照明を確認する | Demo |
| [ミニチュア戦士のストップモーション戦闘](#case-60) | アニメと様式化した人物 | 小さなスケールとコマ撮り風表現が短いアクションに与える効果を調べる | Demo |
| [光る三日月の上で眠る少女](#case-61) | アニメと様式化した人物 | 装飾的な光のモチーフと穏やかな人物の動きを確認する | Demo |
| [交差点のフラッシュモブに加わる歩行者](#case-62) | アニメと様式化した人物 | 街頭ダンスの集団動作、空間配置、視点変化を確認する | Demo |
| [雷雲の下で戦うアニメの剣士](#case-63) | アニメと様式化した人物 | 明瞭な人物の輪郭と刃の相互作用を調べる | Demo |
| [白黒の舞台で踊る集団](#case-64) | アニメと様式化した人物 | 色を除いた条件で振り付けと照明を調べる | Demo |
| [森の雪で遊ぶリス](#case-65) | アニメと様式化した人物 | 表情豊かな動物の動きと柔らかいアニメ様式の一貫性を調べる | Demo |
| [お菓子の世界を歩く赤い衣の人物](#case-66) | アニメと様式化した人物 | 菓子の形で構成された環境と様式化した人物の動きを調べる | Demo |
| [王冠を着けた白猫がカレーを食べる](#case-67) | アニメと様式化した人物 | 衣装、食べ物、表情が動物キャラクターの短い物語をどう支えるか調べる | Demo |
| [森林の旅からドラゴンの飛行へ](#case-68) | 世界と生物 | 閉じた森林から広い空中景観へ続く映像の展開を確認する | Demo |
| [顔のない人影を描くホラーモンタージュ](#case-69) | 世界と生物 | 怪物の一貫性と不気味なモチーフ間の切り替えを確認する | Demo |
| [動き出す球形の異星人集落](#case-70) | 世界と生物 | 作者の公開 Prompt をコピーし、架空の町で連動する環境の動きを試す | Demo |
| [浅い湖を渡る巨大な異星生物](#case-71) | 世界と生物 | 作者の Prompt を使って重さ、水の押し出し、緩やかなクレーン移動を試す | Demo |
| [甲板から飛び立つ大型メカ](#case-72) | 世界と生物 | 機械の関節、スケール、立位から飛行への変化を調べる | Demo |
| [混雑した吊り橋へ近づく巨大生物](#case-73) | 世界と生物 | 豪雨の中で巨大生物、車、人々の大きさの関係を確認する | Demo |
| [紙の街を進む新聞紙の乗り物](#case-74) | 世界と生物 | 折り紙風の都市で素材の統一性と追従カメラを確認する | Demo |
| [丘で歩行し砲撃する重装メカ](#case-75) | 世界と生物 | 機械の動き、地面との接触、大型武器との関係を確認する | Demo |
| [雨夜を進むゴシックな人影](#case-76) | 世界と生物 | 雰囲気、輪郭、反復する視覚的モチーフを確認する | Demo |
| [光るキノコのトンネルに入る紙の馬車](#case-77) | 世界と生物 | 限られた車内視点から明るい環境へ移る過程を確認する | Demo |
| [森林格闘の同じPromptをKlingとSeedanceで比較](#case-78) | 比較と評価 | 表示された二つの結果を、作者の設定と評価範囲を保って比較する | Evaluation |
| [固定カメラのカフェで会話する二人の女性](#case-79) | 比較と評価 | 公開された正確な会話 Prompt で発話交替と横顔の口の同期を試す | Evaluation |
| [StandardとFlashによる五人の会話](#case-80) | 比較と評価 | 作者が示す二つの出力で人物配置と場面構成を比較する | Evaluation |
| [虎の頭を持つ戦士による近接動作テスト](#case-81) | 比較と評価 | 作者の格闘映像から接触の多い動きと人物参照の使い方を確認する | Evaluation |
| [音声ずれテスト中に変化する司会者](#case-82) | 比較と評価 | 自分で同期精度を測定するための出発点として使う | Evaluation |
| [同じ飛行車コンセプトをKlingとSeedanceで比較](#case-83) | 比較と評価 | プラットフォームの比較条件を保ち、ラベル付きの二映像を見比べる | Evaluation |

<a id="category-workflow"></a>
## 🛠️ 制作手順と参照資料

<a id="case-1"></a>
### ケース 1: [SF映像の人物と環境の参照シート](https://x.com/_lexers/status/2111014728160235719) (投稿者 [@_lexers](https://x.com/_lexers))

**人物表と環境表が長い映像指示とどう併記されるか確認する**

砂漠世界、参照画像、スクロールする Prompt が見えるが、全文は書き起こしていない

[![SF映像の人物と環境の参照シート](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D11/poster-c7f71e602146.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D11/video-c7f71e602146.mp4)

Type: Demo | Date: 2026-10-16

---

<a id="case-2"></a>
### ケース 2: [エージェントの絵コンテからアニメ映像へ](https://x.com/z933TfmXkaISSVc/status/2111002792102158714) (投稿者 [@z933TfmXkaISSVc](https://x.com/z933TfmXkaISSVc))

**脚本、絵コンテ、Prompt をつなぐ作者の手順を短編アニメの計画に生かす**

作者は執筆に Opus 5.5、生成に Claude と MCP を使ったと述べるが、動画から実行ログは確認できない

[![エージェントの絵コンテからアニメ映像へ](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D15/poster-a0d7f303f6cf.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D15/video-a0d7f303f6cf.mp4)

Type: Tutorial | Date: 2026-10-16

---

<a id="case-3"></a>
### ケース 3: [壮大な幻想場面と参照シート](https://x.com/dylannknox/status/2110984061569421429) (投稿者 [@dylannknox](https://x.com/dylannknox))

**人物表、環境表、長い場面指示の対応を確認する**

アーチ天井の空間とスクロールする Prompt を組み合わせた表示で、全文は未転記

[![壮大な幻想場面と参照シート](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D19/poster-225fcfcd6ec2.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D19/video-225fcfcd6ec2.mp4)

Type: Demo | Date: 2026-10-16

---

<a id="case-4"></a>
### ケース 4: [動画タスクを追うスマートフォンのチャット](https://x.com/agi_aibusi/status/2110941943006118201) (投稿者 [@agi_aibusi](https://x.com/agi_aibusi))

**作者が提案する Codex から MCP への接続を確認し、検証済みの自分のツールで再現する**

録画は会話とタスク状態を示すが、サブスクリプションのポイント説明は一般的な API 課金規則を証明しない

[![動画タスクを追うスマートフォンのチャット](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D28/poster-fbf3abad9feb.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D28/video-fbf3abad9feb.mp4)

Type: Tutorial | Date: 2026-10-16

---


<a id="category-ads"></a>
## 📦 広告と商品物語

<a id="case-5"></a>
### ケース 5: [森林道路を走る起亜SUVの広告](https://x.com/Diplomeme/status/2110947179057811727) (投稿者 [@Diplomeme](https://x.com/Diplomeme))

**公開された15カットの指示で30秒広告の車両連続性を計画する**

Prompt は未提供の車両参照画像を必要とし、4K の記載は指示であって出力解像度の確認結果ではない

[![森林道路を走る起亜SUVの広告](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D26/poster-cf1e54b34518.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D26/video-cf1e54b34518.mp4)

**プロンプト** · [公開 Prompt の出典](https://x.com/Diplomeme/status/2110947179057811727)

```
High-octane, hyper-realistic automotive commercial for the Kia Seltos, shot with the visual intensity of a Christopher Nolan-style cinematic production using actual 70mm IMAX cameras. Fast-paced multi-shot editing with quick, cinematic cuts timed at exactly one shot every 2 seconds across a complete 30-second timeline. The champagne-gold Kia Seltos, matching the exact vehicle design in the provided reference images, charges through a dense forest road surrounded by towering trees and dappled sunlight. High-contrast Nolan-esque color grading with deep shadows, cold teals, warm champagne-gold reflections, and bright highlights. Sunlight pierces through the forest canopy, reflecting across the sculpted bodywork, signature vertical LED daytime running lights, black front grille, muscular wheel arches, and distinctive rear light bar. Rapid sequence of intense cuts:•Shot 1 (0-2s): Ground-level cinematic establishing shot of an empty winding forest road, towering trees casting deep shadows as sunlight breaks through the canopy. The distant engine note of the approaching Kia Seltos builds tension.•Shot 2 (2-4s): Low eye-level tracking shot of the champagne-gold Kia Seltos emerging between the trees, accelerating along the forest road and revealing its bold front grille, distinctive vertical LED lighting signature, and commanding SUV stance.•Shot 3 (4-6s): Tight, detailed close-up of the front fascia, Kia emblem, illuminated LED daytime running lights, glossy black grille elements, and champagne-gold paint reflecting the passing forest.•Shot 4 (6-8s): Dramatic low-angle tracking shot moving alongside the front wheel as the alloy spokes spin rapidly, tires maintain realistic contact with the asphalt, and the SUV’s sculpted bodywork catches streaks of sunlight.•Shot 5 (8-10s): Fast lateral tracking shot revealing the complete side profile, muscular wheel arches, black lower-body cladding, door contours, windows, roofline, and metallic champagne-gold finish as the Kia Seltos sweeps through the forest.•Shot 6 (10-12s): Low-angle handheld-style camera whip-pan from the road surface to the SUV’s front three-quarter profile as it exits a sweeping bend, with realistic suspension movement, controlled body roll, and natural background motion blur.•Shot 7 (12-14s): Extreme close-up of sunlight traveling across the sculpted hood, Kia emblem, sharp body creases, and vertical LED lights, emphasizing precise automotive design and premium paint reflections.•Shot 8 (14-16s): Rear three-quarter tracking shot following the Kia Seltos through the forest, showcasing the distinctive rear light bar, angular vertical taillights, rear spoiler, sculpted tailgate, and authentic model badging.•Shot 9 (16-18s): Dynamic wheel-height tracking shot as the SUV drives across alternating patches of sunlight and shadow, capturing realistic tire rotation, subtle road texture, reflections along the lower doors, and the movement of the suspension over natural road undulations.•Shot 10 (18-20s): High-angle wide shot of the Kia Seltos commanding a sweeping forest road, surrounded by towering trees and atmospheric shafts of sunlight, with the winding asphalt leading the eye toward the moving SUV.•Shot 11 (20-22s): Fast front-facing tracking shot of the Kia Seltos approaching the camera along a straight section of forest road, its LED lights illuminated and grille dominating the frame as the camera smoothly retreats ahead of the vehicle.•Shot 12 (22-24s): Rapid cinematic transition into a close rear tracking angle as the SUV accelerates away through the trees, the rear lighting signature glowing against the darker forest and the road markings sweeping beneath the frame.•Shot 13 (24-26s): Dramatic low-angle front three-quarter hero shot as the Kia Seltos exits the forest bend and enters a naturally illuminated clearing, revealing its full stance, champagne-gold bodywork, alloy wheels, and signature front lighting.•Shot 14 (26-28s): Controlled cinematic orbit around the stationary Kia Seltos at a scenic forest-road pull-off, transitioning from the front three-quarter view toward the side and rear profile while the surrounding trees and golden sunlight create a premium automotive campaign atmosphere.•Shot 15 (28-30s): Hard cut to black with a final sweep of light revealing the KIA emblem followed by the SELTOS model name and the campaign tagline: “OWN EVERY TURN.” End with a powerful, clean, premium automotive advertising finish.Raw automotive documentary-style camera textures, organic lens flares, lifelike vehicle physics, authentic wheel rotation and tire contact, realistic suspension movement, natural road reflections, physically accurate metallic paint reflections, cinematic motion blur, subtle engine vibration, and an immersive forest-road atmosphere. Preserve the exact Kia Seltos identity, champagne-gold exterior color, front grille design, LED lighting signatures, alloy wheels, body proportions, side profile, and rear design from the provided reference images throughout every shot. Maintain consistent vehicle geometry, wheel design, lighting signatures, paint color, and branding across all 15 shots. No vehicle redesign, no morphing, no inconsistent body panels, no incorrect logos, no artificial CGI appearance, no impossible driving maneuvers, no exaggerated visual effects, and no abrupt changes in road geography. Ultra-detailed, 4K resolution, premium global automotive advertising quality.
```

Type: Demo | Date: 2026-10-16

---

<a id="case-6"></a>
### ケース 6: [複数人物によるスキンケアUGC広告](https://x.com/ErnestoSOFTWARE/status/2110917624167108665) (投稿者 [@ErnestoSOFTWARE](https://x.com/ErnestoSOFTWARE))

**見える広告形式を参考に、制作記録を残す UGC 実験を計画する**

作者は Higgsfield MCP を宣伝し低コストを述べるが、広告成果や請求の証拠はない

[![複数人物によるスキンケアUGC広告](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D37/poster-4ca47c0af310.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D37/video-4ca47c0af310.mp4)

Type: Demo | Date: 2026-10-16

---

<a id="case-7"></a>
### ケース 7: [小さなドラゴンがデザートをキャラメリゼ](https://x.com/magnific/status/2111200639707668507) (投稿者 [@magnific](https://x.com/magnific))

**一つの具体的な調理動作を通じて、人物主導の商品物語を調べる**

プラットフォームの作例は小型ドラゴンとクレームブリュレを並べるが、売上効果は示さない

[![小さなドラゴンがデザートをキャラメリゼ](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D76/poster-6f401168b0fb.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D76/video-6f401168b0fb.mp4)

Type: Demo | Date: 2026-10-16

---

<a id="case-8"></a>
### ケース 8: [オレンジジュースの紙パックの広告映像](https://x.com/leilamakes/status/2111108005567582329) (投稿者 [@leilamakes](https://x.com/leilamakes))

**単一商品を中心に包装の見え方、果物のモチーフ、場面転換を確認する**

紙パック、果物、小売店風の映像を組み合わせるが、Prompt は公開していない

[![オレンジジュースの紙パックの広告映像](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D85/poster-af7aa6745461.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D85/video-af7aa6745461.mp4)

Type: Demo | Date: 2026-10-16

---


<a id="category-story"></a>
## 🎬 人物と物語

<a id="case-9"></a>
### ケース 9: [淡い緑の部屋にいるヘッドホン姿の少女](https://x.com/iam_mian7/status/2110826299417854081) (投稿者 [@iam_mian7](https://x.com/iam_mian7))

**接写、全身の動き、同じ背景の間で人物の外観を確認する**

緑髪でヘッドホンを着けた人物が淡い緑の室内で姿勢を変え、画角も変化する

[![淡い緑の部屋にいるヘッドホン姿の少女](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D03/poster-3305b566e9a1.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D03/video-3305b566e9a1.mp4)

Type: Demo | Date: 2026-10-15

---

<a id="case-10"></a>
### ケース 10: [古典的な列柱廊へ近づく男性](https://x.com/lexx_aura/status/2111017349755043959) (投稿者 [@lexx_aura](https://x.com/lexx_aura))

**見える範囲で控えめな動きと建築背景の連続性を確認する**

確認画像は男性と列柱廊を示すもので、投稿の包括的な CGI 賛辞から複雑な動作能力は証明できない

[![古典的な列柱廊へ近づく男性](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D09/poster-e4099969039c.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D09/video-e4099969039c.mp4)

Type: Demo | Date: 2026-10-16

---

<a id="case-11"></a>
### ケース 11: [濡れた髪の女性を捉える感情的な接写](https://x.com/sophiaparkerr_/status/2110777323423400161) (投稿者 [@sophiaparkerr_](https://x.com/sophiaparkerr_))

**会話中心の演技で微細な表情変化と画面構成を調べる**

暗い緑の照明下で女性の顔を中心に映し、音声品質は独立採点していない

[![濡れた髪の女性を捉える感情的な接写](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D14/poster-bd91c5962388.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D14/video-bd91c5962388.mp4)

Type: Demo | Date: 2026-10-15

---

<a id="case-12"></a>
### ケース 12: [映画館で時間を共有する母と子](https://x.com/liluocheng13/status/2110981671243874346) (投稿者 [@liluocheng13](https://x.com/liluocheng13))

**短い感情表現を具体的な個人の物語に結びつける方法を調べる**

作者は16秒の映像を過去の関係の記憶と結び、画像は Gemini、動画は Kling 4.0 と記している

[![映画館で時間を共有する母と子](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D21/poster-59193966fd28.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D21/video-59193966fd28.mp4)

Type: Demo | Date: 2026-10-16

---

<a id="case-13"></a>
### ケース 13: [二人の司会者による日本語ニュース](https://x.com/seisei_ai_1st/status/2110975778183942532) (投稿者 [@seisei_ai_1st](https://x.com/seisei_ai_1st))

**会話、二人の配置、画面内の文字図形に絞った評価を設計する**

作者は日本語音声に言及するが、映像確認はニュース形式までで発音は独立検証していない

[![二人の司会者による日本語ニュース](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D23/poster-6d7a8b12e568.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D23/video-6d7a8b12e568.mp4)

Type: Demo | Date: 2026-10-16

---

<a id="case-14"></a>
### ケース 14: [オフィスのロビーを走る小さなカート](https://x.com/PromptSin/status/2110943847706775742) (投稿者 [@PromptSin](https://x.com/PromptSin))

**日常建築に意外な乗り物を置き、喜劇的な大きさの対比を調べる**

作者は Kling 4 Flash と記載し、座った運転者がオフィス風ロビーを走る

[![オフィスのロビーを走る小さなカート](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D27/poster-df7aadba33d7.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D27/video-df7aadba33d7.mp4)

Type: Demo | Date: 2026-10-16

---

<a id="case-15"></a>
### ケース 15: [恋人の視点で見る夏の散歩](https://x.com/agi_aibusi/status/2110924173619138656) (投稿者 [@agi_aibusi](https://x.com/agi_aibusi))

**詳しい公開指示をコピーし、日常のしぐさで30秒の流れを計画する**

Prompt は女性の外観、六つの時間指定場面、一般向けカメラの挙動、環境音を定義する

[![恋人の視点で見る夏の散歩](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D34/poster-8bef5187ff5c.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D34/video-8bef5187ff5c.mp4)

**プロンプト** · [公開 Prompt の出典](https://x.com/agi_aibusi/status/2110924176890757483)

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
### ケース 16: [車両や兵士と人物接写の映像集](https://x.com/jerrod_lew/status/2110911158156931427) (投稿者 [@jerrod_lew](https://x.com/jerrod_lew))

**モンタージュから具体的な課題を選び、個別の条件付き試験につなげる**

約63秒の添付は映像集であり、一回のネイティブ生成の長さを示さない

[![車両や兵士と人物接写の映像集](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D39/poster-7d5e3845dc71.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D39/video-7d5e3845dc71.mp4)

Type: Demo | Date: 2026-10-16

---

<a id="case-17"></a>
### ケース 17: [King Cardsの魔術と都市飛行](https://x.com/tphuang/status/2110902762619933119) (投稿者 [@tphuang](https://x.com/tphuang))

**長めの作品が舞台魔術、紙の乗り物、繰り返し登場する赤い鳥をどうつなぐか調べる**

全編モンタージュは後続投稿でも使われ、各抜粋は別映画ではなく関連素材として扱う

[![King Cardsの魔術と都市飛行](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D42/poster-cd1175d34d80.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D42/video-cd1175d34d80.mp4)

Type: Demo | Date: 2026-10-16

---

<a id="case-18"></a>
### ケース 18: [トラクターとともに嵐に向き合う農村の女性](https://x.com/Bic_Revelation/status/2110847934346489947) (投稿者 [@Bic_Revelation](https://x.com/Bic_Revelation))

**人物、機械、天候が短い物語の前提を伝える方法を確認する**

出典は国際農山漁村女性デーと関連づけるが、生成手順は公開していない

[![トラクターとともに嵐に向き合う農村の女性](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D47/poster-6a9f1d8d21de.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D47/video-6a9f1d8d21de.mp4)

Type: Demo | Date: 2026-10-15

---

<a id="case-19"></a>
### ケース 19: [恐竜冒険映画と再利用できるショット指示](https://x.com/techhalla/status/2110806819937378773) (投稿者 [@techhalla](https://x.com/techhalla))

**完成作品と、作者が公開した7秒のアクションおよび8秒の運転指示を見比べる**

二枚の Prompt カードを画像から転記し、埋め込み参照サムネイルは独立した原画像とは区別する

[![恐竜冒険映画と再利用できるショット指示](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D50/poster-9890fdc58895.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D50/video-9890fdc58895.mp4)

作者返信の絵コンテ・参照画像・Prompt カードです。埋め込みサムネイルは元の参照ファイルではありません。

![作者返信の絵コンテ・参照画像・Prompt カードです。埋め込みサムネイルは元の参照ファイルではありません。 1](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/source-prompts/2110806822957273273-0.jpg)

![作者返信の絵コンテ・参照画像・Prompt カードです。埋め込みサムネイルは元の参照ファイルではありません。 2](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/source-prompts/2110806822957273273-1.jpg)

![作者返信の絵コンテ・参照画像・Prompt カードです。埋め込みサムネイルは元の参照ファイルではありません。 3](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/source-prompts/2110806826350412052-0.jpg)

![作者返信の絵コンテ・参照画像・Prompt カードです。埋め込みサムネイルは元の参照ファイルではありません。 4](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/source-prompts/2110806826350412052-1.jpg)

**プロンプト 1** · [公開 Prompt の出典](https://x.com/techhalla/status/2110806822957273273)

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

**プロンプト 2** · [公開 Prompt の出典](https://x.com/techhalla/status/2110806826350412052)

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
### ケース 20: [異世界につながるエレベーターを開く配達員](https://x.com/PromptSin/status/2110790343298023798) (投稿者 [@PromptSin](https://x.com/PromptSin))

**同じ主人公が、見慣れた扉の先で変わる環境にどう反応するか確認する**

黄色い制服の配達員が氷、水、炎のような対照的な場面に遭遇する

[![異世界につながるエレベーターを開く配達員](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D53/poster-c385592b815a.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D53/video-c385592b815a.mp4)

Type: Demo | Date: 2026-10-15

---

<a id="case-21"></a>
### ケース 21: [地下の亀の配管工を描くコメディ](https://x.com/Starjupi/status/2110781205415104571) (投稿者 [@Starjupi](https://x.com/Starjupi))

**作者の制作説明から概念、人物設計、脚本、会話、音声の判断を分けて理解する**

スレッドは手順とモデル機能を説明するが、実際の生成 Prompt は公開していない

[![地下の亀の配管工を描くコメディ](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D58/poster-80ebae3e19ee.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D58/video-80ebae3e19ee.mp4)

Type: Demo | Date: 2026-10-15

---

<a id="case-22"></a>
### ケース 22: [車の意外な展開で終わる街頭の追跡](https://x.com/_3912657840/status/2110778910019559744) (投稿者 [@_3912657840](https://x.com/_3912657840))

**人物の動き、構図、街路状況の変化で喜劇の間を調べる**

作者はテキストから動画への実験と記すが、実際の Prompt は非公開

[![車の意外な展開で終わる街頭の追跡](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D59/poster-32460fac82cb.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D59/video-32460fac82cb.mp4)

Type: Demo | Date: 2026-10-15

---

<a id="case-23"></a>
### ケース 23: [青いドラゴンを見つける若いヒロイン](https://x.com/nrqa__/status/2110764587113222208) (投稿者 [@nrqa__](https://x.com/nrqa__))

**個人的な幻想物語が同じ登場人物を含む編集映像になる過程を調べる**

約95秒の短編映画であり、一度の生成の長さを意味しない

[![青いドラゴンを見つける若いヒロイン](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D63/poster-e7d8328e9da0.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D63/video-e7d8328e9da0.mp4)

Type: Demo | Date: 2026-10-15

---

<a id="case-24"></a>
### ケース 24: [紙の乗り物で花の街へ向かう旅](https://x.com/Aiwithkami/status/2111121831528980566) (投稿者 [@Aiwithkami](https://x.com/Aiwithkami))

**King Cards の短い抜粋で人物、乗り物、背景の変化を調べる**

同じ長編作品から共有された場面であり、別の独立制作映画ではない

[![紙の乗り物で花の街へ向かう旅](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D66/poster-e0abfdd43b76.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D66/video-e0abfdd43b76.mp4)

Type: Demo | Date: 2026-10-16

---

<a id="case-25"></a>
### ケース 25: [紙の馬車で石の乗客が人間に変わる](https://x.com/AlexM12jx/status/2111165921364504890) (投稿者 [@AlexM12jx](https://x.com/AlexM12jx))

**動く乗り物の中で位置を追いながら短い変身を確認する**

King Cards に帰属する抜粋として扱い、出典の帰属と原作者の確認を分ける

[![紙の馬車で石の乗客が人間に変わる](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D69/poster-00ccb9224112.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D69/video-00ccb9224112.mp4)

Type: Demo | Date: 2026-10-16

---

<a id="case-26"></a>
### ケース 26: [円形劇場をカードで満たす魔術師](https://x.com/MelinaVale14/status/2111125493957505478) (投稿者 [@MelinaVale14](https://x.com/MelinaVale14))

**中心の演技、動く小道具、周囲の観客を同じ場面として確認する**

King Cards のこの部分にある異なるエンコードと短縮版を統合している

[![円形劇場をカードで満たす魔術師](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D70/poster-b5d7e24dfed1.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D70/video-b5d7e24dfed1.mp4)

Type: Demo | Date: 2026-10-16

---

<a id="case-27"></a>
### ケース 27: [中庭で足湯を楽しむ女性](https://x.com/Naonekozamurai/status/2111231708108575006) (投稿者 [@Naonekozamurai](https://x.com/Naonekozamurai))

**複雑なアクションではなく日常のしぐさ、衣服、静かな背景を調べる**

作者は10秒1080pとポイント量を述べるが、キャンペーン価格かは不確かとしている

[![中庭で足湯を楽しむ女性](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D74/poster-c60960ec9979.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D74/video-c60960ec9979.mp4)

Type: Demo | Date: 2026-10-16

---

<a id="case-28"></a>
### ケース 28: [鷹を軸にした通報テーマの短編](https://x.com/fatoomdes/status/2111180507254042955) (投稿者 [@fatoomdes](https://x.com/fatoomdes))

**キャラクターのモチーフがスマートフォン画面を主題に結びつける方法を調べる**

作者は完成作品を Kling 4.0 によるものとするが、映像内の告発内容を本資料は独立評価しない

[![鷹を軸にした通報テーマの短編](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D79/poster-c65afae88005.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D79/video-c65afae88005.mp4)

Type: Demo | Date: 2026-10-16

---

<a id="case-29"></a>
### ケース 29: [台所を忍び歩く茶トラ猫](https://x.com/magnific/status/2111139954440949990) (投稿者 [@magnific](https://x.com/magnific))

**身近な室内で小さな動作とカメラ距離の変化を調べる**

Magnific の作例が猫の調理台移動を追い、最後は接写になる

[![台所を忍び歩く茶トラ猫](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D82/poster-ff6f8d465033.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D82/video-ff6f8d465033.mp4)

Type: Demo | Date: 2026-10-16

---

<a id="case-30"></a>
### ケース 30: [街で出会い抱き合う二人の男性](https://x.com/leilamakes/status/2111108104452706636) (投稿者 [@leilamakes](https://x.com/leilamakes))

**短い交流の中で接近、身体接触、人物位置を確認する**

大きなスレッド内の作者返信に付いた映像で、その会話関係を保持している

[![街で出会い抱き合う二人の男性](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D83/poster-57f8a9708fd1.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D83/video-57f8a9708fd1.mp4)

Type: Demo | Date: 2026-10-16

---


<a id="category-action"></a>
## ⚔️ 動作と身体接触

<a id="case-31"></a>
### ケース 31: [月夜の雲上で繰り広げる剣の決闘](https://x.com/AiwithAmeliaa/status/2110782285691965754) (投稿者 [@AiwithAmeliaa](https://x.com/AiwithAmeliaa))

**複数人物の動き、空中での配置、衣装の輪郭の連続性を確認する**

二人の剣士が月明かりの雲上で戦う映像で、投稿アカウントは広告であると明示している

[![月夜の雲上で繰り広げる剣の決闘](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D01/poster-c67c148695e9.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D01/video-c67c148695e9.mp4)

Type: Demo | Date: 2026-10-15

---

<a id="case-32"></a>
### ケース 32: [道場でのテコンドーの組手](https://x.com/Stevemnx3/status/2111039167090016566) (投稿者 [@Stevemnx3](https://x.com/Stevemnx3))

**身体接触、間合いの変化、カメラ位置を比較する**

道場の広い画面と、道着姿の二人が接近する画面が切り替わる

[![道場でのテコンドーの組手](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D02/poster-1ef935905f1c.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D02/video-1ef935905f1c.mp4)

Type: Demo | Date: 2026-10-16

---

<a id="case-33"></a>
### ケース 33: [市街地を追走する二台のスポーツカー](https://x.com/PromptSin/status/2111042013210825211) (投稿者 [@PromptSin](https://x.com/PromptSin))

**素早いカメラ切り替えの中で車両の同一性と進行方向を確認する**

赤と黒のスポーツカーが市街地と橋を走り抜ける

[![市街地を追走する二台のスポーツカー](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D04/poster-61e7dd165825.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D04/video-61e7dd165825.mp4)

Type: Demo | Date: 2026-10-16

---

<a id="case-34"></a>
### ケース 34: [動くカメラで捉えるボクシング](https://x.com/SirGlavan_/status/2110785627251704302) (投稿者 [@SirGlavan_](https://x.com/SirGlavan_))

**一枚の見栄えだけでなく、パンチ、防御の移動、接近時の接触を調べる**

グローブを着けた二人がリングで打ち合い、カメラの距離と角度が変化する

[![動くカメラで捉えるボクシング](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D06/poster-0a6d9253b137.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D06/video-0a6d9253b137.mp4)

Type: Demo | Date: 2026-10-15

---

<a id="case-35"></a>
### ケース 35: [爆発する街路を進む女性戦士](https://x.com/Lisa__Rodin/status/2110771984024129887) (投稿者 [@Lisa__Rodin](https://x.com/Lisa__Rodin))

**同じ人物と車両、煙、大規模な背景効果の関係を確認する**

黒い服の女性が壊れた街を進む場面で、複数アカウントが異なる版を共有している

[![爆発する街路を進む女性戦士](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D07/poster-e910366e89fb.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D07/video-e910366e89fb.mp4)

Type: Demo | Date: 2026-10-15

---

<a id="case-36"></a>
### ケース 36: [都市の怪物と対峙する少女](https://x.com/torotoromoney/status/2111026942489329670) (投稿者 [@torotoromoney](https://x.com/torotoromoney))

**市街地での対決を追いながら人物と怪物の大きさを比べる**

明るい髪の主人公が損壊した建物の間で巨大な触手生物と向き合う

[![都市の怪物と対峙する少女](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D08/poster-699eced69da0.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D08/video-699eced69da0.mp4)

Type: Demo | Date: 2026-10-16

---

<a id="case-37"></a>
### ケース 37: [異星の密林を突進する機械の捕食者](https://x.com/Alin_Reaper05/status/2110996672343917052) (投稿者 [@Alin_Reaper05](https://x.com/Alin_Reaper05))

**公開 Prompt で加速、環境の反応、後退する手持ち視点を調べる**

金属の手足と有機組織を組み合わせた生物で、作者が直接の返信に生成指示を公開している

[![異星の密林を突進する機械の捕食者](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D18/poster-e28f30cd8013.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D18/video-e28f30cd8013.mp4)

**プロンプト** · [公開 Prompt の出典](https://x.com/Alin_Reaper05/status/2110996674558530007)

```
A living mechanical predator with a glowing orange central eye moves through dense alien jungle vegetation, using long metallic limbs wrapped in pulsing flesh to pull itself between trees, organic tendrils grabbing branches while hydraulic joints extend and retract, the creature suddenly notices the camera and rapidly charges forward, handheld tracking camera retreats through foliage, branches break naturally, mud splashes, vines react realistically, intense acceleration, realistic weight and momentum, dark cinematic lighting, high-end creature VFX.
```

Type: Demo | Date: 2026-10-16

---

<a id="case-38"></a>
### ケース 38: [槍を交える騎馬の戦士](https://x.com/alifcoder/status/2110980799264903190) (投稿者 [@alifcoder](https://x.com/alifcoder))

**開けた戦場で騎手の相互作用、馬の動き、武器接触を確認する**

添付映像は騎馬戦であり、投稿のパンチに関する説明をそのまま画面の事実にはしない

[![槍を交える騎馬の戦士](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D22/poster-98d16e333c2b.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D22/video-98d16e333c2b.mp4)

Type: Demo | Date: 2026-10-16

---

<a id="case-39"></a>
### ケース 39: [床のマットと接触する空手の組手](https://x.com/WuxiaRocks/status/2110962012100653419) (投稿者 [@WuxiaRocks](https://x.com/WuxiaRocks))

**孤立したポーズではなく演者と周囲の接触を調べる**

作者が足によるマットの沈みを指摘しているが、これは出典の観察であり定量的な物理評価ではない

[![床のマットと接触する空手の組手](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D24/poster-0a576d72f135.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D24/video-0a576d72f135.mp4)

Type: Demo | Date: 2026-10-16

---

<a id="case-40"></a>
### ケース 40: [コンビニ店員と格闘者の対決](https://x.com/seisei_ai_1st/status/2110853231316496547) (投稿者 [@seisei_ai_1st](https://x.com/seisei_ai_1st))

**日本語会話のあるアクションで近接接触と場面の連続性を調べる**

作者は比較に同じ Prompt を使ったとするが、参照された指示は今回の収集範囲外

[![コンビニ店員と格闘者の対決](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D46/poster-1b049353be78.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D46/video-1b049353be78.mp4)

Type: Demo | Date: 2026-10-15

---

<a id="case-41"></a>
### ケース 41: [石の台上で戦う鎧の幻想戦士](https://x.com/AIWarper/status/2110833050955526292) (投稿者 [@AIWarper](https://x.com/AIWarper))

**キーフレームに基づくポーズを使った戦闘の配置を調べる**

作者は10枚のキーフレームを使ったとし、開けた台上で異なる鎧の人物が戦う

[![石の台上で戦う鎧の幻想戦士](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D48/poster-b680150c5bc2.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D48/video-b680150c5bc2.mp4)

Type: Demo | Date: 2026-10-15

---

<a id="case-42"></a>
### ケース 42: [夜の町を駆け抜ける猫](https://x.com/umesh_ai/status/2110797373584887907) (投稿者 [@umesh_ai](https://x.com/umesh_ai))

**一続きのショットを求める Prompt で、つながった屋内外の高速移動を試す**

作者は後に Flash との比較で20秒を選んだと述べるが、その条件は元の Prompt に追加していない

[![夜の町を駆け抜ける猫](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D51/poster-074081e6557c.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D51/video-074081e6557c.mp4)

**プロンプト** · [公開 Prompt の出典](https://x.com/umesh_ai/status/2110797376827035806)

```
An amateur handheld recording in third-person perspective rapidly follows a cat through its nighttime adventures in one continuous shot, with no cuts, no stopping, and no pause. The sequence feels like fast-forward, showing all the curious, mischievous, funny, and chaotic things a cat might do while the town, house, garden, and everything around it are half-asleep.The cat races through about ten places a cat would naturally explore at night, each one flowing into the next in a single continuous chase: a quiet bedroom, a dim hallway, a kitchen, a living room, a backyard garden, a fence line, a garage, a rooftop, a tree, and a sleepy street or alley. The camera is shaky and imperfect, always struggling to keep up as it follows close behind. In every location, the cat causes some kind of chaos. In the bedroom it jumps onto furniture and disturbs sleeping people. In the hallway it sends small objects tumbling. In the kitchen it knocks items off the counter. In the living room it darts across shelves and tips things over. In the garden it rustles plants, digs, or startles birds. On the fence it rattles loose objects. In the garage it weaves through clutter and causes things to wobble or fall. On the rooftop it skids across surfaces and startles other animals. In the tree it shakes branches and scatters leaves. In the street or alley it darts through trash, shadows, and unexpected little messes, always leaving brief chaos behind before sprinting onward.The cat behaves like a restless, curious nighttime troublemaker: climbing, leaping, squeezing through gaps, chasing tiny movements, staring at strange things, swatting objects, knocking things over, and vanishing into corners before bursting back out again. Every scene should contain a clear action, reaction, or small disaster caused by the cat.Everything around it feels sleepy and still, with dark houses, quiet gardens, dim windows, silent rooftops, and empty streets. The contrast is that the cat is pure energy, moving so quickly that the world smears into motion blur and fragmented glimpses of chaos. The overall feeling is funny, lively, mischievous, and cinematic, like a whole secret night of cat behavior compressed into one rapid continuous chase.
```

Type: Demo | Date: 2026-10-15

---

<a id="case-43"></a>
### ケース 43: [雨の森で戦う侍](https://x.com/AI__TSUBAKI/status/2110796958935978171) (投稿者 [@AI__TSUBAKI](https://x.com/AI__TSUBAKI))

**雨の激しい戦闘で衣装の安定性と武器の接触を調べる**

作者の15秒、1080p、202ポイントという設定は出典の説明であり、現在の API 価格ではない

[![雨の森で戦う侍](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D52/poster-428a2ca3573f.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D52/video-428a2ca3573f.mp4)

Type: Demo | Date: 2026-10-15

---

<a id="case-44"></a>
### ケース 44: [森で戦う黒い服の女性](https://x.com/OxBairan/status/2110785228155560230) (投稿者 [@OxBairan](https://x.com/OxBairan))

**同じ森林アクションの再エンコード版を比べ、姿勢とカメラ移動を確認する**

複数アカウントが短い抜粋を再利用しており、一つの素材グループに統合している

[![森で戦う黒い服の女性](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D56/poster-e86261e950fa.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D56/video-e86261e950fa.mp4)

Type: Demo | Date: 2026-10-15

---

<a id="case-45"></a>
### ケース 45: [紫のタコと対峙する赤い紙の鳥](https://x.com/AIwithkhan/status/2111128321262276695) (投稿者 [@AIwithkhan](https://x.com/AIwithkhan))

**小さな飛行主体と大きな組み立て生物の相互作用を調べる**

King Cards の別の抜粋であり、似たモデル公開告知とともに繰り返し共有されている

[![紫のタコと対峙する赤い紙の鳥](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D67/poster-d6f35850335e.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D67/video-d6f35850335e.mp4)

Type: Demo | Date: 2026-10-16

---

<a id="case-46"></a>
### ケース 46: [空中でダンクするバスケットボール選手](https://x.com/leilamakes/status/2111108072236060864) (投稿者 [@leilamakes](https://x.com/leilamakes))

**身体の軌道、ボール位置、リングとの接触を調べる**

作者返信に付いた生成スポーツ動画であり、独立検証された実際の身体能力の証拠ではない

[![空中でダンクするバスケットボール選手](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D84/poster-d1fcc959cdd5.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D84/video-d1fcc959cdd5.mp4)

Type: Demo | Date: 2026-10-16

---


<a id="category-game"></a>
## 🎮 ゲームと乗り物のコンセプト

<a id="case-47"></a>
### ケース 47: [賞金稼ぎを描くゲーム風コンセプト](https://x.com/NyaiiBubu/status/2111040233387200905) (投稿者 [@NyaiiBubu](https://x.com/NyaiiBubu))

**人物の動作と会話を組み合わせたゲーム予告の参考として使う**

投稿は AAA 風と説明するが、確認できる成果物は生成動画であり、遊べるゲームではない

[![賞金稼ぎを描くゲーム風コンセプト](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D05/poster-96e6493c7d87.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D05/video-96e6493c7d87.mp4)

Type: Demo | Date: 2026-10-16

---

<a id="case-48"></a>
### ケース 48: [夜の巨大な斜面を登る空飛ぶ車](https://x.com/higgsfield_ai/status/2110937478492479783) (投稿者 [@higgsfield_ai](https://x.com/higgsfield_ai))

**動くゲームの証拠ではなく、映画的な乗り物コンセプトの参考にする**

プラットフォームのブランド付き映像が、急斜面を登って飛び出す車を追う

[![夜の巨大な斜面を登る空飛ぶ車](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D29/poster-9f0ea0939850.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D29/video-9f0ea0939850.mp4)

Type: Demo | Date: 2026-10-16

---

<a id="case-49"></a>
### ケース 49: [夕暮れの海岸道路を走るスポーツカー](https://x.com/higgsfield_ai/status/2110928479734964409) (投稿者 [@higgsfield_ai](https://x.com/higgsfield_ai))

**追走カメラ、照明、計器風の表示をレース映像の参考として調べる**

プラットフォームの見本は夕暮れの海岸レースで、実行可能なゲームは提供されていない

[![夕暮れの海岸道路を走るスポーツカー](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D31/poster-94729ec66a60.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D31/video-94729ec66a60.mp4)

Type: Demo | Date: 2026-10-16

---

<a id="case-50"></a>
### ケース 50: [島の景観を飛ぶ戦闘機](https://x.com/higgsfield_ai/status/2110925937634410612) (投稿者 [@higgsfield_ai](https://x.com/higgsfield_ai))

**飛行カメラの動きとゲーム風インターフェースの構成を調べる**

明るい海岸を飛ぶジェット機に、ゲーム風の画角と表示が付いている

[![島の景観を飛ぶ戦闘機](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D33/poster-06b6b22e3e0e.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D33/video-06b6b22e3e0e.mp4)

Type: Demo | Date: 2026-10-16

---

<a id="case-51"></a>
### ケース 51: [浮遊島の間を滑空する人物](https://x.com/higgsfield_ai/status/2110922885141606859) (投稿者 [@higgsfield_ai](https://x.com/higgsfield_ai))

**三人称視点の映像で狭い場所から広い空景へ移る方法を調べる**

プラットフォームは様式化した浮遊島を移動する人物の追従映像を示す

[![浮遊島の間を滑空する人物](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D35/poster-41fca9f81d16.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D35/video-41fca9f81d16.mp4)

Type: Demo | Date: 2026-10-16

---

<a id="case-52"></a>
### ケース 52: [ライダーを追うバイクレースのコンセプト](https://x.com/higgsfield_ai/status/2110915957833248859) (投稿者 [@higgsfield_ai](https://x.com/higgsfield_ai))

**バイクの動き、追走距離、コースの照明を調べる**

プラットフォーム映像はレースゲーム風の提示であり、対話型アプリではない

[![ライダーを追うバイクレースのコンセプト](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D38/poster-6fbf86005055.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D38/video-6fbf86005055.mp4)

Type: Demo | Date: 2026-10-16

---

<a id="case-53"></a>
### ケース 53: [港湾を舞台にした一人称射撃映像](https://x.com/higgsfield_ai/status/2110905436371370009) (投稿者 [@higgsfield_ai](https://x.com/higgsfield_ai))

**作者の時間指定付き戦術射撃指示をコピーし、15秒の映像目標を定める**

返信は15秒、根の投稿は30秒、添付は約14.3秒であり、それぞれ別の情報として保持する

[![港湾を舞台にした一人称射撃映像](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D41/poster-d66668c4a4fe.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D41/video-d66668c4a4fe.mp4)

**プロンプト** · [公開 Prompt の出典](https://x.com/higgsfield_ai/status/2110906696851955916)

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
### ケース 54: [未来都市を飛ぶ自動車](https://x.com/YapayZekaSerisi/status/2111104253817155607) (投稿者 [@YapayZekaSerisi](https://x.com/YapayZekaSerisi))

**路上走行、飛行、都市の目印の間の移行を確認する**

見える成果物は未来交通の動画であり、遊べるゲームは提供されていない

[![未来都市を飛ぶ自動車](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D72/poster-78d337068f01.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D72/video-78d337068f01.mp4)

Type: Demo | Date: 2026-10-16

---

<a id="case-55"></a>
### ケース 55: [都市の空飛ぶ車を追う警察](https://x.com/higgsfield_ai/status/2111235977406763103) (投稿者 [@higgsfield_ai](https://x.com/higgsfield_ai))

**追走カメラが地上交通と飛行のような動きをどう結ぶか調べる**

Higgsfield が同社プラットフォームの別の Kling 4.0 ゲームコンセプトとして示す

[![都市の空飛ぶ車を追う警察](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D73/poster-d291f74977e7.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D73/video-d291f74977e7.mp4)

Type: Demo | Date: 2026-10-16

---

<a id="case-56"></a>
### ケース 56: [海岸のドライブからヘリコプター飛行へ](https://x.com/frameo_ai/status/2111097408633639000) (投稿者 [@frameo_ai](https://x.com/frameo_ai))

**車両、歩く人物、空中映像の間の切り替えを調べる**

Frameo のゲーム風動画コンセプトと連携予告であり、実行可能なゲームではない

[![海岸のドライブからヘリコプター飛行へ](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D87/poster-31d433ad4429.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D87/video-31d433ad4429.mp4)

Type: Demo | Date: 2026-10-16

---


<a id="category-animation"></a>
## 🎨 アニメと様式化した人物

<a id="case-57"></a>
### ケース 57: [イラストと実写風映像を組み合わせた音楽動画](https://x.com/IntLab0000/status/2111016713869463957) (投稿者 [@IntLab0000](https://x.com/IntLab0000))

**完成した MV が異なる画風と繰り返す感情的モチーフをどう結ぶか調べる**

作者は MCP 支援で制作したと述べるが、約136秒の添付は編集作品であり、単一生成の長さを示さない

[![イラストと実写風映像を組み合わせた音楽動画](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D10/poster-32d9ded7f2d0.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D10/video-32d9ded7f2d0.mp4)

Type: Demo | Date: 2026-10-16

---

<a id="case-58"></a>
### ケース 58: [台所で出会うおばあさんと小さな粘土ドラゴン](https://x.com/higgsfield_ai/status/2110927330390790226) (投稿者 [@higgsfield_ai](https://x.com/higgsfield_ai))

**短い台所アニメの人物間交流と素材表現を確認する**

小さなドラゴン、調理道具、粘土風の描画を組み合わせた場面

[![台所で出会うおばあさんと小さな粘土ドラゴン](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D32/poster-1098bee49c56.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D32/video-1098bee49c56.mp4)

Type: Demo | Date: 2026-10-16

---

<a id="case-59"></a>
### ケース 59: [夜市で料理するアニメのシェフ](https://x.com/higgsfield_ai/status/2110922265340891255) (投稿者 [@higgsfield_ai](https://x.com/higgsfield_ai))

**短い料理アニメで手の動き、道具、照明を確認する**

プラットフォーム自身の見本で、描画風の料理人が賑やかな屋台で働く

[![夜市で料理するアニメのシェフ](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D36/poster-a89dc333a50c.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D36/video-a89dc333a50c.mp4)

Type: Demo | Date: 2026-10-16

---

<a id="case-60"></a>
### ケース 60: [ミニチュア戦士のストップモーション戦闘](https://x.com/higgsfield_ai/status/2110910617574121905) (投稿者 [@higgsfield_ai](https://x.com/higgsfield_ai))

**小さなスケールとコマ撮り風表現が短いアクションに与える効果を調べる**

小さな戦士が赤い生物と戦い、生成時間の主張はプラットフォーム側の説明にとどまる

[![ミニチュア戦士のストップモーション戦闘](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D40/poster-0096a333b2d9.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D40/video-0096a333b2d9.mp4)

Type: Demo | Date: 2026-10-16

---

<a id="case-61"></a>
### ケース 61: [光る三日月の上で眠る少女](https://x.com/minuitIA/status/2110823653336027226) (投稿者 [@minuitIA](https://x.com/minuitIA))

**装飾的な光のモチーフと穏やかな人物の動きを確認する**

作者が投稿した就寝イメージを、月を題材にした短い映像へ展開している

[![光る三日月の上で眠る少女](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D49/poster-cadca8a36e4a.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D49/video-cadca8a36e4a.mp4)

Type: Demo | Date: 2026-10-15

---

<a id="case-62"></a>
### ケース 62: [交差点のフラッシュモブに加わる歩行者](https://x.com/seisei_ai_1st/status/2110790316584562789) (投稿者 [@seisei_ai_1st](https://x.com/seisei_ai_1st))

**街頭ダンスの集団動作、空間配置、視点変化を確認する**

作者は繰り返し使うフラッシュモブ設定で新モデルを試している

[![交差点のフラッシュモブに加わる歩行者](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D54/poster-0f0e0bc769b1.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D54/video-0f0e0bc769b1.mp4)

Type: Demo | Date: 2026-10-15

---

<a id="case-63"></a>
### ケース 63: [雷雲の下で戦うアニメの剣士](https://x.com/Dani__oros/status/2110790297458544971) (投稿者 [@Dani__oros](https://x.com/Dani__oros))

**明瞭な人物の輪郭と刃の相互作用を調べる**

作者は大まかな Prompt による初期試験と説明するが、根の投稿に指示本文はない

[![雷雲の下で戦うアニメの剣士](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D55/poster-28acdf9e07a3.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D55/video-28acdf9e07a3.mp4)

Type: Demo | Date: 2026-10-15

---

<a id="case-64"></a>
### ケース 64: [白黒の舞台で踊る集団](https://x.com/MO_IAI/status/2110784427408105640) (投稿者 [@MO_IAI](https://x.com/MO_IAI))

**色を除いた条件で振り付けと照明を調べる**

複数のダンサーと変化する隊形を白黒で映す演目

[![白黒の舞台で踊る集団](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D57/poster-0bf2843739e2.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D57/video-0bf2843739e2.mp4)

Type: Demo | Date: 2026-10-15

---

<a id="case-65"></a>
### ケース 65: [森の雪で遊ぶリス](https://x.com/fAIkout/status/2110768302851342454) (投稿者 [@fAIkout](https://x.com/fAIkout))

**表情豊かな動物の動きと柔らかいアニメ様式の一貫性を調べる**

小さなリスが雪や森の物と触れ合う作者の作例

[![森の雪で遊ぶリス](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D62/poster-c2c730ddad9a.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D62/video-c2c730ddad9a.mp4)

Type: Demo | Date: 2026-10-15

---

<a id="case-66"></a>
### ケース 66: [お菓子の世界を歩く赤い衣の人物](https://x.com/jji1jj/status/2111165487648301173) (投稿者 [@jji1jj](https://x.com/jji1jj))

**菓子の形で構成された環境と様式化した人物の動きを調べる**

見た目の異なる King Cards の場面研究であり、別の独立映画ではない

[![お菓子の世界を歩く赤い衣の人物](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D71/poster-f533cc90221d.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D71/video-f533cc90221d.mp4)

Type: Demo | Date: 2026-10-16

---

<a id="case-67"></a>
### ケース 67: [王冠を着けた白猫がカレーを食べる](https://x.com/craftcapitallab/status/2111200513924731150) (投稿者 [@craftcapitallab](https://x.com/craftcapitallab))

**衣装、食べ物、表情が動物キャラクターの短い物語をどう支えるか調べる**

王冠の猫とカレーを組み合わせ、装飾的なタイトルで終わる作例

[![王冠を着けた白猫がカレーを食べる](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D77/poster-0c65da3cad85.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D77/video-0c65da3cad85.mp4)

Type: Demo | Date: 2026-10-16

---


<a id="category-world"></a>
## 🌍 世界と生物

<a id="case-68"></a>
### ケース 68: [森林の旅からドラゴンの飛行へ](https://x.com/Lianaalane/status/2110953699250151850) (投稿者 [@Lianaalane](https://x.com/Lianaalane))

**閉じた森林から広い空中景観へ続く映像の展開を確認する**

乗り手とドラゴンが森林から山間の谷へ移動し、重複する再エンコード版は統合済み

[![森林の旅からドラゴンの飛行へ](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D13/poster-ea2c6c571381.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D13/video-ea2c6c571381.mp4)

Type: Demo | Date: 2026-10-16

---

<a id="case-69"></a>
### ケース 69: [顔のない人影を描くホラーモンタージュ](https://x.com/h_ashizawaJP/status/2110999675709034742) (投稿者 [@h_ashizawaJP](https://x.com/h_ashizawaJP))

**怪物の一貫性と不気味なモチーフ間の切り替えを確認する**

白い人影、歪んだ顔、暗い森林とともに、生成音と別工程の音声ミックスが説明される

[![顔のない人影を描くホラーモンタージュ](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D16/poster-f97b54673926.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D16/video-f97b54673926.mp4)

Type: Demo | Date: 2026-10-16

---

<a id="case-70"></a>
### ケース 70: [動き出す球形の異星人集落](https://x.com/Alin_Reaper05/status/2110997688682770563) (投稿者 [@Alin_Reaper05](https://x.com/Alin_Reaper05))

**作者の公開 Prompt をコピーし、架空の町で連動する環境の動きを試す**

返信は回転する機械住宅、有機的な配管、小型ロボット、浅い水、上昇するカメラを指定する

[![動き出す球形の異星人集落](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D17/poster-0727879b80e3.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D17/video-0727879b80e3.mp4)

**プロンプト** · [公開 Prompt の出典](https://x.com/Alin_Reaper05/status/2110997691274580344)

```
A colorful alien settlement filled with enormous spherical buildings and bizarre organic machines comes alive at sunrise, round red mechanical houses rotate their giant lens-like windows, pipes expand and contract like breathing organs, small robotic creatures run through shallow water, flying vehicles weave between towers, camera glides smoothly through the town at ground level before rising above the rooftops, puddles reflecting neon lights and clouds, natural vegetation moving in the wind, playful but believable extraterrestrial world, cinematic photorealism.
```

Type: Demo | Date: 2026-10-16

---

<a id="case-71"></a>
### ケース 71: [浅い湖を渡る巨大な異星生物](https://x.com/Alin_Reaper05/status/2110982741491904596) (投稿者 [@Alin_Reaper05](https://x.com/Alin_Reaper05))

**作者の Prompt を使って重さ、水の押し出し、緩やかなクレーン移動を試す**

二頭の長い首の動物が、赤い植生と黄緑の空に囲まれた青緑の水を渡る

[![浅い湖を渡る巨大な異星生物](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D20/poster-51289a03af36.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D20/video-51289a03af36.mp4)

**プロンプト** · [公開 Prompt の出典](https://x.com/Alin_Reaper05/status/2110982744247353611)

```
Two enormous long-necked alien animals slowly walk through a shallow turquoise lagoon surrounded by bright red grass and exotic palm forests. Their massive bodies create realistic waves and splashes with every step while smaller creatures flee along the shoreline. The camera begins low near the water and smoothly cranes upward, revealing the gigantic animals against a glowing yellow-green sky and distant mountains. Realistic weight and inertia, detailed skin movement, volumetric mist, natural vegetation motion, cinematic alien wildlife documentary, smooth continuous camera movement, highly coherent anatomy.
```

Type: Demo | Date: 2026-10-16

---

<a id="case-72"></a>
### ケース 72: [甲板から飛び立つ大型メカ](https://x.com/PDyv9gdatT4132/status/2110948121295696380) (投稿者 [@PDyv9gdatT4132](https://x.com/PDyv9gdatT4132))

**機械の関節、スケール、立位から飛行への変化を調べる**

大型ロボットが作動し、船のような甲板から浮き上がる映像

[![甲板から飛び立つ大型メカ](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D25/poster-621b9b81c745.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D25/video-621b9b81c745.mp4)

Type: Demo | Date: 2026-10-16

---

<a id="case-73"></a>
### ケース 73: [混雑した吊り橋へ近づく巨大生物](https://x.com/jji1jj/status/2110775129043320994) (投稿者 [@jji1jj](https://x.com/jji1jj))

**豪雨の中で巨大生物、車、人々の大きさの関係を確認する**

後続投稿は同じ映像を再利用しており、追加出典として保持し、新規ケースにはしない

[![混雑した吊り橋へ近づく巨大生物](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D60/poster-cdf43480c9f5.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D60/video-cdf43480c9f5.mp4)

Type: Demo | Date: 2026-10-15

---

<a id="case-74"></a>
### ケース 74: [紙の街を進む新聞紙の乗り物](https://x.com/Gemalpha_88/status/2111113629919854891) (投稿者 [@Gemalpha_88](https://x.com/Gemalpha_88))

**折り紙風の都市で素材の統一性と追従カメラを確認する**

共有された King Cards の映像であり、独立検証された別作品ではない

[![紙の街を進む新聞紙の乗り物](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D68/poster-692aeb10394f.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D68/video-692aeb10394f.mp4)

Type: Demo | Date: 2026-10-16

---

<a id="case-75"></a>
### ケース 75: [丘で歩行し砲撃する重装メカ](https://x.com/ojiji2025/status/2111218605069365688) (投稿者 [@ojiji2025](https://x.com/ojiji2025))

**機械の動き、地面との接触、大型武器との関係を確認する**

作者の初めてのメカ作例であり、工学文書に基づくシミュレーションではない

[![丘で歩行し砲撃する重装メカ](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D75/poster-dd1ae88aa463.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D75/video-dd1ae88aa463.mp4)

Type: Demo | Date: 2026-10-16

---

<a id="case-76"></a>
### ケース 76: [雨夜を進むゴシックな人影](https://x.com/fabulatenebris/status/2111183079955951804) (投稿者 [@fabulatenebris](https://x.com/fabulatenebris))

**雰囲気、輪郭、反復する視覚的モチーフを確認する**

暗い人物と城のような背景を使った、様式化した雨夜の作品

[![雨夜を進むゴシックな人影](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D78/poster-6a014db111fa.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D78/video-6a014db111fa.mp4)

Type: Demo | Date: 2026-10-16

---

<a id="case-77"></a>
### ケース 77: [光るキノコのトンネルに入る紙の馬車](https://x.com/Hope_Ai01/status/2111146114972058097) (投稿者 [@Hope_Ai01](https://x.com/Hope_Ai01))

**限られた車内視点から明るい環境へ移る過程を確認する**

King Cards のさらに別の抜粋で、関連する出典の文脈を保持している

[![光るキノコのトンネルに入る紙の馬車](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D81/poster-9d22c4d4055d.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D81/video-9d22c4d4055d.mp4)

Type: Demo | Date: 2026-10-16

---


<a id="category-evaluation"></a>
## 🔬 比較と評価

<a id="case-78"></a>
### ケース 78: [森林格闘の同じPromptをKlingとSeedanceで比較](https://x.com/AibeginnerR8/status/2110935157503041672) (投稿者 [@AibeginnerR8](https://x.com/AibeginnerR8))

**表示された二つの結果を、作者の設定と評価範囲を保って比較する**

両方720pと表示され、音声は Kling を使用する。作者は、この試行ではカット、タイミング、動作追従で Seedance を好む

[![森林格闘の同じPromptをKlingとSeedanceで比較](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D30/poster-a0590043e48c.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D30/video-a0590043e48c.mp4)

**プロンプト** · [公開 Prompt の出典](https://x.com/AibeginnerR8/status/2110935160434610592)

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
### ケース 79: [固定カメラのカフェで会話する二人の女性](https://x.com/tanabe_fragm/status/2110887676832543125) (投稿者 [@tanabe_fragm](https://x.com/tanabe_fragm))

**公開された正確な会話 Prompt で発話交替と横顔の口の同期を試す**

作者の価格は10秒に対するものだが添付は約15秒で、音声と課金の独立検証はない

[![固定カメラのカフェで会話する二人の女性](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D44/poster-293ead53e5df.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D44/video-293ead53e5df.mp4)

**プロンプト** · [公開 Prompt の出典](https://x.com/tanabe_fragm/status/2110887676832543125)

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
### ケース 80: [StandardとFlashによる五人の会話](https://x.com/onofumi_AI/status/2110866433198702728) (投稿者 [@onofumi_AI](https://x.com/onofumi_AI))

**作者が示す二つの出力で人物配置と場面構成を比較する**

出典は20秒、180対120ポイントと述べるが、作者およびアカウント固有の数値である

[![StandardとFlashによる五人の会話](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D45/poster-1007d8f82463.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D45/video-1007d8f82463.mp4)

Type: Evaluation | Date: 2026-10-15

---

<a id="case-81"></a>
### ケース 81: [虎の頭を持つ戦士による近接動作テスト](https://x.com/ozansihay/status/2110763522099474800) (投稿者 [@ozansihay](https://x.com/ozansihay))

**作者の格闘映像から接触の多い動きと人物参照の使い方を確認する**

作者は接触で Seedance を好み、30秒1080pで405ポイントと述べ、宣伝も明示している

[![虎の頭を持つ戦士による近接動作テスト](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D64/poster-e99a824137b0.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D64/video-e99a824137b0.mp4)

Type: Evaluation | Date: 2026-10-15

---

<a id="case-82"></a>
### ケース 82: [音声ずれテスト中に変化する司会者](https://x.com/plasm0/status/2110763509307064539) (投稿者 [@plasm0](https://x.com/plasm0))

**自分で同期精度を測定するための出発点として使う**

作者は合格と述べるが、確認画像が示すのは司会者の変化であり、発話同期の正確さではない

[![音声ずれテスト中に変化する司会者](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D65/poster-285b037dd41e.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D65/video-285b037dd41e.mp4)

Type: Evaluation | Date: 2026-10-15

---

<a id="case-83"></a>
### ケース 83: [同じ飛行車コンセプトをKlingとSeedanceで比較](https://x.com/itsPolloAI/status/2111097887656726915) (投稿者 [@itsPolloAI](https://x.com/itsPolloAI))

**プラットフォームの比較条件を保ち、ラベル付きの二映像を見比べる**

Pollo AI は同じ Prompt と述べるが、本文や反復した統制試験は提供しない

[![同じ飛行車コンセプトをKlingとSeedanceで比較](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D86/poster-f8698ad3f5cb.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-kling-4-usecases/assets/cases/D86/video-f8698ad3f5cb.mp4)

Type: Evaluation | Date: 2026-10-16

---

## 関連リポジトリ

現行モデルの経路が未検証のため、Kling 4 専用 API や Skill のリポジトリはリンクしていません。近隣モデルの資料は [Seedance 2.5 ガイド](https://github.com/EvoLinkAI/awesome-seedance-2.5-guide)を参照できますが、別モデルの説明であり、本資料の Kling ケースを検証するものではありません。

<a id="acknowledge"></a>
## 🙏 謝辞

本資料集に含まれる内容を公開したアカウントに感謝する：

[@_3912657840](https://x.com/_3912657840), [@_lexers](https://x.com/_lexers), [@agi_aibusi](https://x.com/agi_aibusi), [@AI__TSUBAKI](https://x.com/AI__TSUBAKI), [@AibeginnerR8](https://x.com/AibeginnerR8), [@AIWarper](https://x.com/AIWarper), [@AiwithAmeliaa](https://x.com/AiwithAmeliaa), [@Aiwithkami](https://x.com/Aiwithkami), [@AIwithkhan](https://x.com/AIwithkhan), [@AlexM12jx](https://x.com/AlexM12jx), [@alifcoder](https://x.com/alifcoder), [@Alin_Reaper05](https://x.com/Alin_Reaper05), [@Bic_Revelation](https://x.com/Bic_Revelation), [@craftcapitallab](https://x.com/craftcapitallab), [@Dani__oros](https://x.com/Dani__oros), [@Diplomeme](https://x.com/Diplomeme), [@dylannknox](https://x.com/dylannknox), [@ErnestoSOFTWARE](https://x.com/ErnestoSOFTWARE), [@fabulatenebris](https://x.com/fabulatenebris), [@fAIkout](https://x.com/fAIkout), [@fatoomdes](https://x.com/fatoomdes), [@frameo_ai](https://x.com/frameo_ai), [@Gemalpha_88](https://x.com/Gemalpha_88), [@h_ashizawaJP](https://x.com/h_ashizawaJP), [@higgsfield_ai](https://x.com/higgsfield_ai), [@Hope_Ai01](https://x.com/Hope_Ai01), [@iam_mian7](https://x.com/iam_mian7), [@IntLab0000](https://x.com/IntLab0000), [@itsPolloAI](https://x.com/itsPolloAI), [@jerrod_lew](https://x.com/jerrod_lew), [@jji1jj](https://x.com/jji1jj), [@leilamakes](https://x.com/leilamakes), [@lexx_aura](https://x.com/lexx_aura), [@Lianaalane](https://x.com/Lianaalane), [@liluocheng13](https://x.com/liluocheng13), [@Lisa__Rodin](https://x.com/Lisa__Rodin), [@magnific](https://x.com/magnific), [@MelinaVale14](https://x.com/MelinaVale14), [@minuitIA](https://x.com/minuitIA), [@MO_IAI](https://x.com/MO_IAI), [@Naonekozamurai](https://x.com/Naonekozamurai), [@nrqa__](https://x.com/nrqa__), [@NyaiiBubu](https://x.com/NyaiiBubu), [@ojiji2025](https://x.com/ojiji2025), [@onofumi_AI](https://x.com/onofumi_AI), [@OxBairan](https://x.com/OxBairan), [@ozansihay](https://x.com/ozansihay), [@PDyv9gdatT4132](https://x.com/PDyv9gdatT4132), [@plasm0](https://x.com/plasm0), [@PromptSin](https://x.com/PromptSin), [@seisei_ai_1st](https://x.com/seisei_ai_1st), [@SirGlavan_](https://x.com/SirGlavan_), [@sophiaparkerr_](https://x.com/sophiaparkerr_), [@Starjupi](https://x.com/Starjupi), [@Stevemnx3](https://x.com/Stevemnx3), [@tanabe_fragm](https://x.com/tanabe_fragm), [@techhalla](https://x.com/techhalla), [@torotoromoney](https://x.com/torotoromoney), [@tphuang](https://x.com/tphuang), [@umesh_ai](https://x.com/umesh_ai), [@WuxiaRocks](https://x.com/WuxiaRocks), [@YapayZekaSerisi](https://x.com/YapayZekaSerisi), [@z933TfmXkaISSVc](https://x.com/z933TfmXkaISSVc)

第三者の動画、画像、Prompt は各権利者の権利に従います。編集文章と構造は [CC BY 4.0](LICENSE) で提供しますが、第三者素材を再許諾するものではありません。署名、権利、転載の訂正は [Issue](https://github.com/cheercheung/awesome-kling-4-usecases/issues) で連絡できます。[媒体方針](docs/media-policy.md)と[貢献案内](CONTRIBUTING.md)も参照してください。

[EvoLink の動画モデルを見る](https://evolink.ai/models?utm_source=github&utm_medium=footer&utm_campaign=awesome-kling-4-usecases&utm_content=ja_footer)
