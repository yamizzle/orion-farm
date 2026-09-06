# Moondrop Mountain — REGRESSION / KEEP-FIXED

**Rule:** Skim this before every ship. Never revert these without Darren saying so.
These are **HITL bugs Darren manually hit or called out** — not every backlog ship note.
Source: live reports + Local ship notes that closed those reports. Full history stays in `BACKLOG.md`.

Status column: **KEEP** = still required in new builds.

---

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
| Buys / crafts / catches / chest TAKE that kids need next **pin + select** into tray (not bag-only dead ends) | 05fe–05gt wave (keep behavior) | KEEP |

---

## Graphics / density

| Invariant | BUILD | Status |
| --- | --- | --- |
| World evening/morning **BUFFER× grade scratch** so outdoor props stay as crisp as tray (no soft half-res upscale) | 20260905hg | KEEP |
| Internal **BUFFER=2** canvas (640×384) for dense tray/world blit | 20260905g | KEEP |
| Props keep denser Imagine frames (2× / 3× src) — car uses dense frames but **draws vehicle-sized** (~0.75 of 3× ≈ a bit taller than Orion), not house-tall | 20260905hi (was 05hh/05cc) | KEEP |
| South camera keeps Orion **above the hotbar** (CAM_PAD_BOTTOM) on overworld too | 20260905c + 05cg | KEEP |
| Orion visible on northernmost walk tiles (foot boost; no global +64 canopy hack) | 20260905ba + 05bw | KEEP |

---

## Farm / Town

| Invariant | BUILD | Status |
| --- | --- | --- |
| **Shovel tills farm grass** into plantable dirt again; mounds still loot; far plain-grass taps WALK (no whole-farm dig-steal); `farmHole` persists as dirt | 20260905hi | KEEP |
| **Chicken scoot** on walk/tap/Space (penned hens hop ≤2) | 20260904g + 20260905bu + 05gw | KEEP |
| **Palm axe-chop** finishes to stump + wood (and coconut eat path) | 20260905bu + 05gz | KEEP |
| Reed car beep / kick-cart / Jobs kept at the smaller draw size | 20260905hi | KEEP |

---

## Combat

| Invariant | BUILD | Status |
| --- | --- | --- |
| Bow selected → strike pad + Space/tap actually **shootArrow** | 20260905ez | KEEP |
| Fat-finger sword pad hits all 8 neighbors; pad remash; pad-over-OUT kept clear | 20260905bz | KEEP |
| Every foe kill drops loot (no empty POOF); hit/kill juice readable | 20260905ci–05cj | KEEP |

---

## Clock / Perf / Story

| Invariant | BUILD | Status |
| --- | --- | --- |
| Day-clock **race harden** without changing DAY_MS: dedicated clockMark, 50ms step cap, ≤1 day rollover/tick, reset on pause/visibility/pageshow, single-flight rAF | 20260905bq | KEEP |
| Snappier Chromebook/iPad draw: reuse graded scratch bitmaps; multiply+mask night wash (no per-frame getImageData); off-camera cull — **without** softening 05hg density or evening colors | 20260905hk | KEEP |
| Three-lights story spine → Moondrop Night (Home / Town / Peak lamps) | 20260905cb | KEEP |

---

## Appendix — Space / tap parity (optional skim)

Darren’s long Space-adjacent wave (05fl–05gy, doors, dig, fish, craft, etc.) is one durable rule:

> **Space / J / E should do the same kid action tap already does** (facing **or** adjacent), for doors, tools, talk, scoot, fish, place, harvest.

Do not re-open that wave item-by-item unless a specific interaction goes silent again. Details live in `BACKLOG.md` Local 9/6 notes.

---

*Last sweep: 2026-09-06 from BACKLOG Local ship notes (05a–05hl) + Darren HITL keep-list. Prefer this file over re-reading every ship note before a build.*
