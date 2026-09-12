# Moondrop Mountain — REGRESSION / KEEP-FIXED

## BUILD 20260905jc (Local 9/12) — Bird ride to High Peak bear
After `peakRocksCleared`, bird menu adds BEAR (PEAK balcony kept); lands highPeak near bear; Jobs ASK THE BIRD TO THE BEAR once; dialogue 7-choice layout; highPeak cache null-guard. Atlas 1477. Frozen DAY_MS/walk/Orion/grass/evening. Never START OVER.

## BUILD 20260905jb (Local 9/12) — Cabin exit + lean interior
Cabin doormat/inndoor → goExitCabin (not farm house); walk-onto cabinOut auto-exits; lean props bed/stove/craft/chest + door only; sceneCache artRev 05jb. Atlas 1477. Frozen DAY_MS/walk/Orion/grass/evening. Never START OVER.

## BUILD 20260905iz (Local 9/11) — Abandoned Cabin + dark forest north bank
HIGH_PEAK 64×68 (~4×N / ~2×E/W north bank); cabin center (bed/stove/chest/craft); wizard west; east chop trees; dark forest north needs lit torch; blue mush plant grows by day; cabin bed = save once reachable (farm bed stops). Bridge/bear/river south frozen. Atlas 1477. Never START OVER.

## BUILD 20260905iy (Local 9/11) — High Peak river + fell-tree log bridge
HIGH_PEAK 64×68; bear ty 48; E–W river blocks (`TOO WET`) until `bridgePine` chop → fall anim → `logBridge` + `found.logBridge` forever; tall grove scenery; wizard north bank after bear clear + bridge. Bear grilled-swordfish feed unchanged. Pink gate PASS; atlas 1477. Never START OVER.

## BUILD 20260905ix (Local 9/11) — grilled golden swordfish distinct + bear-only
Dense sword+sparkle tray icon (not cookedFish lookalike); animated twinkle overlay; cannot eat grilled golden swordfish (bear feed only); bag tip FEEDS THE SLEEPY BEAR. Frozen DAY_MS/walk/Orion/grass/evening.

## BUILD 20260905iw (Local 9/11) — ocean golden swordfish fairer
Ocean golden roll 1/50→1/20; soft pity `found.oceanCatchesNoGolden` forces golden after 25 ocean catches without one; farm ponds stay oceanOnly-blocked. Save-safe. Story fish for sleepy bear. Frozen DAY_MS/walk/Orion/grass/evening.


## BUILD 20260905iv (Local 9/11) — multi-tab day-clock save harden
Multi-tab localStorage race: `savedAt` + adopt-ahead on persist; `storage` syncs clock fields; updateClock only when visible + hasFocus. DAY_MS frozen. Autotest stubs. Needs live verify. Never START OVER.


## BUILD 20260905iu (Local 9/11) — wizard Imagine regen
Graphics audit: replace 05it code-BOX wizardHouse/wizardNpc/wand/wizardRobes with Imagine + BOX/AREA dense 2×. Pink gate PASS. No atlas repack. Frozen assets untouched.


**Rule:** Skim this before every ship. Never revert these without Darren saying so.
These are **HITL bugs Darren manually hit or called out** — not every backlog ship note.
Source: live reports + Local ship notes that closed those reports. Full history stays in `BACKLOG.md`.

Status column: **KEEP** = still required in new builds.

---

## BUILD 20260905it (Local 9/10) — wizard house / wand / robes

- High Peak past bear: wizard house enter/exit, wizard talk → wand in weapon dock, robes overlay while wand held.
- Save-safe: `found.wizardMet` / `found.wand` / `wandOwned` (never START OVER).
- Frozen untouched: DAY_MS, walk energy, Orion base art, grass0–3, evening.
- Kickables 2×: already Done 05iq; pink gate recheck PASS (playBall + kickCart).
- Art: standalone dense 2× PNGs (no atlas height change / no 1× repack). Pink-chroma gate PASS.
- Autotest: wizard house prop + stoop + grant wand + select + exit peak.

## Frozen forever (do not touch)

| Invariant | BUILD | Status |
| --- | --- | --- |
| Never press / never wipe household save with **START OVER** unless Darren means it | household rule | KEEP |
| **DAY_MS = 480000** (~8 real min/day); PHASE_MS = DAY_MS/4 — do not “fix clock” by changing DAY_MS | 20260830k + 20260905bq | KEEP |
| **Walk energy** drain / restore rates frozen | frozen | KEEP |
| **Orion art** sprites frozen | frozen | KEEP |
| **Farm grass0–3** tiles frozen | frozen | KEEP |
| **Evening color / outdoor grade values** frozen (wash math may change; the look must not soften) | frozen + 05hg | KEEP |

---

## Boat / Ocean

| Invariant | BUILD | Status |
| --- | --- | --- |
| Rideable pier boat: GET IN → row water → **GET OUT** only on sand/pier (TOO DEEP on open water); leave-ocean blocked while aboard | 20260905a | KEEP |
| Aboard: water taps **row** (not “need a fishing pole”); pole-steal toast must not block rowing | 20260905h | KEEP |
| **Fish from the boat** when pole is selected (Space/tap water casts ocean fish + rare golden swordfish); without pole, water still rows | 20260905hj | KEEP |
| Ocean **golden swordfish** roll **1/20** + soft pity after **25** ocean catches without one (`found.oceanCatchesNoGolden`); farm ponds never get it (`oceanOnly`) | 20260905iw | KEEP |
| Grilled **golden swordfish** tray icon distinct (long sword bill + sparkles; not cookedFish lookalike); animated twinkle in `paintFishIcon` | 20260905ix | KEEP |
| Cannot **eat** grilled golden swordfish (tray-tap / `eatCookedFish`); bear-feed spend still works; bag tip FEEDS THE SLEEPY BEAR (no EAT/YUM) | 20260905ix | KEEP |
| **Island boat GET OUT** works on island beach sand/pier (all `f` rowable while aboard); boat docks / stays where you leave it (`boatDock`, `BOAT STAYS HERE.`) | 20260905ad + 20260905bo | KEEP |
| Hard-refresh mid-row keeps you **aboard** (onBoat persist); island cave refresh does not dump you on the farm | 20260905ef + 20260905eh | KEEP |

---

## Peak / Mine

| Invariant | BUILD | Status |
| --- | --- | --- |
| Island cave **Diamond Pickaxe** is real inventory / usable pick (farm+mine rocks chip faster; not bare-hand) | 20260905af + 20260905fa | KEEP |
| Peak summit rocks **really clear**: painted pile scrubbed; smashable prop only; 10 diamond-pick hits remove prop, open walk cols 18–20 rows 2–5, persist `peakRocksCleared`, bust peak cache | 20260905bt | KEEP |
| Peak rock hits show **progressive crack stages** (5 stages / 10 hits — not darken-only) | 20260905bu | KEEP |
| After rocks clear: **secret mountain mine** mouth on cleared path; walk/tap/Space enter; OUT back to peak; save-safe loot flags | 20260905hl | KEEP |
| Summit mountain mine polish: denser crystals (glow+sparkle+toast), kickable carts (CART/CLANK), 3 chests with gems/ore/gold/bars; OUT still labeled; enter/OUT peak keep | 20260905hu | KEEP |
| Mountain-mine north exit → **HIGH PEAK**; sleepy bear blocks path; only grilled golden swordfish feeds / clears path; bearFed+pathClear save; Jobs tips A BIGGER PEAK OPENS / THE BEAR IS SLEEPY / GRILL A GOLDEN SWORDFISH; OUT still returns to old peak | 20260905hw | KEEP |
| High Peak **river** E–W hard-blocks until riverside `bridgePine` axe-chop → fall anim → walkable `logBridge`; `found.logBridge` persists forever (never START OVER); scenery `peakGiant` not choppable | 20260905iy | KEEP |
| Wizard house on **north bank** past bridge; only after bearFed/pathClear + bridge crossable; Jobs CHOP THE TALL TREE BY THE RIVER / VISIT THE WIZARD HOUSE; bear grilled-swordfish feed unchanged | 20260905iy | KEEP |
| Cabin bed sleeps+saves once bridge+bear; farm house bed no longer save point when cabin reachable; bridge/bear/wand west unchanged | 20260905iz | KEEP |
| Dark forest north of cabin needs lit torch; blue glow mushroom pick → plant on cabin garden grows by day | 20260905iz | KEEP |
| Torch craft branch+moss; light on stove; east choppable trees; wizard west of cabin | 20260905iz | KEEP |
| Cabin doormat/inndoor tap → goExitCabin (not goExitHouse); walk-onto cabinOut auto-exits to highPeak cabinLand walkable | 20260905jb | KEEP |
| Cabin interior lean: bed + stove + workbench + houseChest + doormat/inndoor only (no fireplace/windows/table/lantern/rug/crate/plant) | 20260905jb | KEEP |
| HIGH PEAK ground + bear are **Imagine stamps** (flat 16px rock/dirt path tiles — not postage-stamp peakMap crops; dense 2× true sleeping-pose sleepingBear; Imagine pines — no code checker / oval / triangle paint) | 20260905hz + 20260905hy | KEEP |
| PEAK ground is **tiles-only** (warm brown dirt path on walk mask + calm pale snow-rock off-path) + smashable rock **props** never painted-in; clearing leaves clean path (no scrub scar / busy stripe checker); `peakRocksCleared` household save kept | 20260905ib | KEEP |
| Mine OUT/UP findable (bobbing gold labels + Jobs tip); pad must not cover OUT | 20260905bx + 31t | KEEP |
| Door / ladder / cave landings leave a **2-tile gap** so one step cannot auto-reenter or auto-exit | 20260905er–05ew | KEEP |

---

## Inventory / HUD

| Invariant | BUILD | Status |
| --- | --- | --- |
| **Bag ↔ tray drag swap** is atomic: neither stack vanishes; no shared-cell alias minting twins | 20260905x + 20260905be (+ 05ce mirror) | KEEP |
| Mid-drag **bagHeld** never vanishes on save/tab-hide; counts/spend/select see the ghost; no duplicate tool grant | 20260905ee + 05ej–05eq | KEEP |
| **Only one fishing pole** forever (dedupe tray/bag/chest/held; Pip BUY shows OWNED; never stack>1) | 20260904g + 20260905bg | KEEP |
| **Only one weapon** in the 10-tray at a time (sword/bow); second parks in bag; tools (axe/pick/shovel/pole/diamondPick) stay | 20260905ay | KEEP |
| Cave sword pins tray slot 0 (evicts bow); tray sword stays findable | 04c / 05ay | KEEP |
| Buys / crafts / chest TAKE / cook / smelt that kids need next **pin + select** into tray (not bag-only dead ends). Placeable pick pins too; keepHeld when tool held — see next row | 05fe–05gt wave (keep behavior) | KEEP |
| **Selected tool stays selected** across dig/chop/mine loot walk-ons + fish catch + collectible pick + **placeable pick** (fence/kit/path/player flower) — still **pin** into tray; do not steal shovel/axe/pick/pole/seeds/weapon; empty hand still auto-selects. Shop/craft/chest TAKE/cook/smelt still pin+select | 20260905hp + 20260905hq | KEEP |
| Dedicated **weapon dock** (sword/bow only); tray is tools/seeds/food; second weapon swaps into dock and old goes to bag; BAG open shows big dock + **WEAPON** ghost when empty | 20260905hm | KEEP |
| **Bow selectable from weapon dock** — soft sword-ensure must not kick a parked bow; bag→dock swap / dock tap arms bow; hard pin only on cave claim / iron craft / giveTool sword; sword pad select still works | 20260905ho | KEEP |
| **BAG select tip** — with bag open, tapping a cell shows NAME + 1 kid-plain blurb strip; updates on select/held; clears on close/empty; drag swap + X close still work | 20260905ic | KEEP |
| **Press Start 2P locked fonts** — tray/bag counts **bake 24 / show 6** (exact 4:1 NN) cream `#FFF8E8` + thin dark cardinal outline, **tight digit tracking** / no shadow (`drawSlotCount` / `PIXEL_COUNT_BAKE` / `PIXEL_COUNT_SIZE` / `TEXT_COUNT_SCALE`; not soft 6px fillText; no 05hx 0.85); world labels 8px white + thin cardinal outline (OUT no gold); HUD DAY/clock/BAG/place 8px white+outline, money gold, no energy "E"; `clockHudLine` `SPR · AM|PM|EVE|NIGHT`; FontFace load gated with boot; **dialogue/talk boxes** also Press Start 8px via `drawPixelText` (not legacy FONT) | 20260905is | KEEP |

---


---

## Doors / entrance labels

| Invariant | BUILD | Status |
| --- | --- | --- |
| **Walk-through entrance labels** — MINE/DOWN/OUT/UP/PEAK/WOODS/OCEAN/SHOP words do not solid-block; kids walk the door tile under the float | 20260905id | KEEP |
| Labels **centered above the entrance** (ladder/cave/door top-middle), not parked beside so kids path around; pinned (no bob/camera drift) | 20260905id | KEEP |

## Graphics / density

| Invariant | BUILD | Status |
| --- | --- | --- |
| **Chicken body opaque** — white feathers solid (no checkerboard / grass bleed-through); atlas stamp must keep height ≥1200 + rock0.w ≥32 (no full 1× repack) | 20260905ht | KEEP |
| Imagine art **pink-chroma gate**: no magenta plates; world props 2× of logical draw; tiles stay 16px grid; BOX/AREA downsample (no NN-upscale fake density) | 20260905hx + 20260905hz | KEEP |
| World evening/morning **BUFFER× grade scratch** so outdoor props stay as crisp as tray (no soft half-res upscale) | 20260905hg | KEEP |
| Internal **BUFFER=2** canvas (640×384) for dense tray/world blit | 20260905g | KEEP |
| Props keep denser Imagine frames (2× / 3× src) — car uses dense frames but **draws vehicle-sized** (~0.75 of 3× ≈ a bit taller than Orion), not house-tall | 20260905hi (was 05hh/05cc) | KEEP |
| South camera keeps Orion **above the hotbar** (CAM_PAD_BOTTOM) on overworld too | 20260905c + 05cg | KEEP |
| Orion visible on northernmost walk tiles (foot boost; no global +64 canopy hack) | 20260905ba + 05bw + 05hv | KEEP |

---

## Farm / Town

| Invariant | BUILD | Status |
| --- | --- | --- |
| **Shovel tills farm grass** into plantable dirt again; mounds still loot; far plain-grass taps WALK (no whole-farm dig-steal); `farmHole` persists as dirt (05hr autotest clears swing so KEEP stays green) | 20260905hi + 20260905hr | KEEP |
| **Chicken scoot** on walk/tap/Space (penned hens hop ≤2) | 20260904g + 20260905bu + 05gw | KEEP |
| **Palm axe-chop** finishes to stump + wood (and coconut eat path) | 20260905bu + 05gz | KEEP |
| Reed car beep / kick-cart / Jobs kept at the smaller draw size | 20260905hi | KEEP |

---

## Combat

| Invariant | BUILD | Status |
| --- | --- | --- |
| Bow selected → strike pad + Space/tap actually **shootArrow** | 20260905ez | KEEP |
| Fat-finger sword pad hits all 8 neighbors; pad remash; pad-over-OUT kept clear | 20260905bz (+05hv dock facing-away autotest) | KEEP |
| Every foe kill drops loot (no empty POOF); hit/kill juice readable | 20260905ci–05cj | KEEP |

---

## Boot / Loading

| Invariant | BUILD | Status |
| --- | --- | --- |
| Boot **must leave LOADING FARM** — `artDensityOk` miss may soft-reload atlas once; after that **fail soft** and still `scheduleLoop` (never eternal green LOADING). Dense atlas height ≥1200 + rock0.w ≥32; weapon-dock chrome append must not shrink/repack to 1×. Soft-reload only when sessionStorage one-shot sticks — blocked storage must fail soft (no reload loop / no skip `scheduleLoop`) | 20260905hn + 20260905hs | KEEP |

---

## Clock / Perf / Story

| Invariant | BUILD | Status |
| --- | --- | --- |
| Day-clock **race harden** without changing DAY_MS: dedicated clockMark, 50ms step cap, ≤1 day rollover/tick, reset on pause/visibility/pageshow, single-flight rAF; **+ multi-tab** savedAt / adopt-ahead persist / storage clock sync / hasFocus gate (05iv). Expected rate ~2 real min/phase (~8 min/day) — a day flip in a ~15 min pass is normal, not a race | 20260905bq + 20260905ir + 20260905iv | KEEP |
| Snappier Chromebook/iPad draw: reuse graded scratch bitmaps; multiply+mask night wash (no per-frame getImageData); off-camera cull — **without** softening 05hg density or evening colors | 20260905hk | KEEP |
| Three-lights story spine → Moondrop Night (Home / Town / Peak lamps) | 20260905cb | KEEP |

---

## Appendix — Space / tap parity (optional skim)

Darren’s long Space-adjacent wave (05fl–05gy, doors, dig, fish, craft, etc.) is one durable rule:

> **Space / J / E should do the same kid action tap already does** (facing **or** adjacent), for doors, tools, talk, scoot, fish, place, harvest.

Do not re-open that wave item-by-item unless a specific interaction goes silent again. Details live in `BACKLOG.md` Local 9/6 notes.

---

*Last sweep: 2026-09-07 — 05io tray/bag counts 6px Press Start cream (was 05in 8px); HUD/labels/clock stay 8px; 05id walk-through entrance labels kept; prior 05a–05ic keep-list still applies.*
