---
layout: post
title: 围棋术语简介
categories: Go
update: 2017-05-09
tags: Go
---

本文对围棋术语进行介绍。

<!-- more -->

本文术语大部分翻译选自[此页面](http://senseis.xmp.net/?ChineseGoTerms)。本系列文章的 SGF 对局预览器来自使用 MIT 协议的[WGo.js](http://wgo.waltheri.net/player)，在此表示感谢。正文中的代码格式：

```html
<script type="text/javascript" src="go-support/wgo/wgo.min.js"></script>
<script type="text/javascript" src="go-support/wgo/wgo.player.min.js"></script>
<script type="text/javascript" src="go-support/wgo/i18n.zh.js"></script>
<link rel="stylesheet" type="text/css" href="go-support/wgo/wgo.player.css" />

<div data-wgo="go-support/sgf/Go-terms-intro.sgf" style="width: 700px"></div>
```

WGo.js 虽然界面美观，但是对变化图的支持却不佳。在有变化图的情况，使用 [eidogo](http://eidogo.com/source) 作为预览器。代码格式：

```html
<script type="text/javascript" src="go-support/player/js/all.compressed.js"></script>

<div class="eidogo-player-auto" sgf="go-support/sgf/Go-terms-intro.sgf" align="center"></div>
```

## 规则

- 猜先：guessing the stones
- 变化图：variation
- 参考图：reference
- 点目：counting
- 读秒：byo-yomi
- 超时胜、负：win on time, lose by time
- 和棋：draw
- 不入子、禁着点：suicide, illegal point
- 级、段：kyu, dan
- 复盘：game review
- 棋谱：game record
- 十番棋：ten-game match
- 劫、劫争：ko (fight)
    - 劫材：ko threat
    - 本身劫材：local ko threat（必须应的劫材，否则劫赢棋也死）


## 布局与官子

布局：opening
- 星、小目、三三：star point, 3-4 points (komoku), san-san
- 天元：tengen
- 角、边、中心：corner, side, center
- 地：territory
- 定式、场合定式：joseki, situational joseki
- 分先：even game （无贴目）
- 根据：base（例如拆二）
- 大场：big point
- 好点：good point
- 大局：whole board thinking
- 模样：territorial framework
- 大模样：large-scale framework
- 出头：getting ahead
- 挂角：corner approach
- 守角：corner enclosure
- 分投：splitting move

布局中常见的说法：
- 台象：Tower
- 雪崩形：avalanche
- 二连星：two stars in a row, nirensei
- 向小目：facing komoku
- 三连星：san ren sei
- 中国流：Chinese opening
- 小林流：Kobayashi opening
- 秀策流：Shusaku opening
- 宇宙流：cosmic style
- 双飞燕：4-4 point double low approach
- 妖刀：magic sword（对小目一间高挂进行二间高夹）
- 初棋无劫：There are no ko threat in the opening.

<div class="eidogo-player-auto" sgf="go-support/sgf/Go-terms-intro.sgf" align="center"></div>

中盘：
- 厚势：influence
- 腾挪：sabaki
- 打入：invasion
- 侵消：erasure
- 作战：combat
- 开花：ponnuki
- 试应手：probe
- 点角：corner invasion
- 大龙：dragon
- 决战：decisive battle
- 逆转：overturn
- 天王山：Tennozan（双方必争点）
- 铁柱：iron pillar（四线向三线立的阻止腾挪的手段）

官子：endgame
- 单官：neutral point
- 半目劫：half-point ko
- 先手/后手：initiative (sente), gote
    - 先手利：forcing move
    - 失先手：loss of initiative
- 逆官子：reverse endgame move
- 伸腿、大伸腿：(large) monkey jump

## 移动

单方的移动：
- 尖：diagonal
- 虎、虎口：tiger's mouth, hanging connection
    - 双虎：trumpet connection
- 长、并：stretch, horizontal stretch
- 爬：crawl
- 立：descent, stand
- 连、接、粘：connect
- 单关（一间跳）：one-point jump
- 双：bamboo joint
- 飞：knight's move
- 大飞、超大飞：(very) large knight's move
- 象飞：elephant's move
- 拆二、拆三：two/three-space extension
- 逼、拆逼：checking, checking extension
- 补强：reinforce
- 脱先：tenuki

双方之间：
- 冲：push through
- 退：pull back
- 断：cut
- 刺：peep
- 打吃、反打：atari, counter atari
- 双打：double atari
- 反提：recapture
- 打二还一：capture 2 recapture 1
- 扳、扳断：hane、hane through
    - 连扳：double hane
    - 反扳：counter hane
- 吃：capture
- 抱吃（门吃）：capturing by atari
- 枷：net
- 征子（扭羊头）、缓气征子：ladder, loose ladder
    - 引征：ladder breaker
- 扑：throw in
- 挖：wedge
- 跨：waist cut
- 挡：block
- 压：press, push
- 拐：bend, turn
- 挤：choke, atekomi
- 顶、尖顶：bump, diagonal attachment
- 镇：cap, capping play
- 肩冲：shoulder hit（亦作“尖冲”）
- 夹攻、反夹：pincer, counter pincer
    - 二间高夹：two-space high pincer
- 紧夹：clamp（官子手段或死活手筋）
- 封、封锁：seal in
- 搭：attach
- 托：underneath attachment
- 渡：bridge under
- 靠：attach
    - 碰：attach to the side
    - 靠长：attach-extend
    - 靠扳：attach-staircase
    - 扭断（扭十字）：attach-crosscut
- 透点：placement

## 死活 life and death

基本型：
- 直三：straight three
- 弯三：bent three
- 盘角曲四：bent four in the corner
- 方四：square four
- 丁四：T-four, pyramid four, farmer's hat
- 刀五：bulky five
- 花五：crossed five
- 花六：rabbity six, nutcracker
- 板六：rectangular six
- 小猪嘴：tripod group with extra leg
- 大猪嘴：J group
- 带钩：L group
- 斗方（金柜角）：carpenter's square

手筋及其他术语：
- 手筋：tesuji
- 棋筋：key stones
- 对杀：capturing race
- 气：liberty
    - 长气：increase liberties
    - 紧气：reduce liberties
    - 公气：shared liberties
    - 外气：outside liberties
    - 撞气：reduce self liberties
- 眼位：eye space
- 双活：seki
- 净活、净杀、净死：unconditional kill/life/death
- 劫活、劫杀：live/kill by ko
    - 抛劫：throw-in ko（以扑开劫）
    - 提劫：taking the ko
    - 套劫：two-stage ko
    - 紧气劫：direct ko
    - 缓气劫：approach ko
    - 生死劫（天下大劫）：all-dominating ko
    - 无忧劫：hanami ko, picnic ko
    - 连环劫：double ko
- 弃子：sacrifice
- 见合：miai
- 硬腿：first-line descent
- 卡眼：falsify eye
- 倒扑：snapback
- 倒脱靴（脱骨）：under the stones
- 胀牯牛：internal liberty shortage, oshi-tsubushi
- 点方：eye-stealing tesuji
    - 方形：mouth shape
- 愚形：dumpling shape
- 石塔（秤砣、大头鬼）：stone tower
- 滚打包收：squeeze
- 接不归：connect and die
- 有眼杀瞎：eye kills no eye
- 金鸡独立：double shortage of liberties
- 老鼠偷油：mouse stealing oil
- 黄莺扑蝶：the raccoon-dog drums his belly
- 乌龟不出头（鹤颈）：crane's nest

## 评价

- 安定、不安定：settled/unsettled
- 胜着、败着：winning/losing move
- 薄、厚：thin, thick
- 轻盈、笨重：light, heavy
- 本手：proper move
- 崩：collapse
- 变着：unusual play
- 步调：logical order of moves
- 有利、不利：(dis)advantageous
- 成功：success
- 成立：possible
- 重复、凝形：Overconcentrated shape（例如外势相距过近）
- 次序：sequence
- 错着：mistake
- 恶手：bad move
- 废着：useless move
- 浮棋、孤子：floating stones
- 鬼手：ghost move
- 后续手段：follow-up
- 缓手：slow
- 急所：urgent point
- 坚实：solid
- 冷静：calm
- 恋子：reluctance to sacrifice
- 两分：equal
- 优势、劣势：superior, inferior
- 裂形：split shape
- 满意：satisfied
- 妙手：excellent
- 骗着、欺着：tricky play, hamete
- 强硬：strong
- 权利：privilege
- 胜负手：all-or-nothing move
- 俗手：crude move
- 随手：hasty move
- 稳妥：stable
- 唯一手：only move
- 无理：overplay
- 有余味：aji
- 转换：exchange
