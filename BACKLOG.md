Local 9/6 (BUILD 20260905em): mine floor-3 climb-up landing — UP from MINE 4 no longer drops you on the DOWN hole's north rim (05ej made that tile solid); land one tile further at (16,8) so you are not stuck / cannot auto-fall back down. Never START OVER.

Local 9/6 (BUILD 20260905el): mid-drag tool no duplicate grant — forceSwordIntoTray clears/counts bagHeld sword before pinning slot 0 (openBag no longer mints a twin); placeToolInTrayFirst parks a held tool into tray/bag instead of spawning a second axe/pick/etc. Never START OVER.

Local 9/6 (BUILD 20260905ek): forest/overworld/ocean door refresh — hard-refresh on WOODS door, mine/house/shop/cottage stoops, beach band, forest FARM exit, giant TREE door, or ocean pier exit no longer auto-warps you next tick (nudge to the matching exit landing). Never START OVER.

Local 9/6 (BUILD 20260905ej): held cursor stack counts + mine hole rim — bagCount/syncBagCounts/takeFromBag include the mid-drag bagHeld ghost so tab-hide/craft/shop/giveTool cannot treat a held axe/wood as gone and mint a duplicate; mine DOWN hole's north rim tile is no longer walkable (looks like the pit; hole tile itself still walkable to fall). Never START OVER.

Local 9/6 (BUILD 20260905ei): HOUSE/SHOP/cottages/mine refresh spawn — hard-refresh on an OUT mat or mine UP/DOWN/OUT ladder no longer auto-warps you outside/deeper next tick; floor-aware mineRestoreLand matches enter landings (same pattern as TREE 05eg). Never START OVER.

Local 9/6 (BUILD 20260905eh): ocean saveScene boatDock + mid-drag bag remirror — caching ocean while rowing no longer stores a hidden aboard ghost (visible hull at boatDock + boatDock field on the cache); restore aboard snaps to nearest water if the saved tile is not rowable; stashBagHeld remirrors tray stacks into an open bag so tab-hide mid-drag does not leave a blank grid hole. Never START OVER.

Local 9/6 (BUILD 20260905eg): TREE/TREETOP/peak/stairs refresh spawn — hard-refresh on TREE 2–4 no longer falls back to TREE 1's (5,5); floor-aware land spots match climb landings; refresh while standing on a ladder/cave/stairs/exit gate nudges you off so the next tick cannot auto-warp you into the wrong scene (TREETOP exits, peak cave, STAIRS mouth, island-cave OUT, mine→peak stairs). Never START OVER.

Local 9/6 (BUILD 20260905ef): island-cave + boat save restore — refresh inside the south island cave no longer dumps you on the farm (pendingRestore whitelist + spawn fallback); rowing mid-ocean now persists onBoat so hard-refresh keeps you aboard instead of TOO DEEP unstick; HUD stamp shows ISLAND CAVE. Never START OVER.

Local 9/6 (BUILD 20260905ee): save mid-drag bag stash — if you were holding a bag/tray stack (drag ghost) when the game autosaved / tab-hid / refreshed, that stack was missing from the serialized pockets and could vanish; persistSave now stashBagHeld() first so the stack snaps back into a pocket before write. Never START OVER.

Local 9/5 (BUILD 20260905ed): outside-panel soft click — tapping outside craft/shop/chest/BAG/Stars/Jobs now soft ui clicks like the X / Esc / BYE closes (was silent world-dismiss). Never START OVER.

Local 9/5 (BUILD 20260905ec): STAR toast digit guard + soft OK click — number keys ignored while A STAR! toast / sleep / faint overlays are up so tray cannot swap under them; tapping OK or Esc on the star toast finally soft-clicks (was silent). No Jobs tip spam. Never START OVER.

Local 9/5 (BUILD 20260905eb): number keys ignored while Stars/Jobs/shop/craft/chest/wipe open so tray cannot swap under panels (bag tray still selectable); wipe NO/outside soft ui click (YES still careful silent reload); soft sparkle when Stars opens. No Jobs tip spam. Never START OVER.

Local 9/5 (BUILD 20260905ea): Stars X matches craft/Jobs/BAG/talk (13x12 corner) + Pip shop X Y aligned; Nim note boards already share talk-panel X from 05dy (verified, no change). Wipe confirm untouched. Never START OVER.

Local 9/5 (BUILD 20260905dz): empty tray slot soft click (quieter screen sparks + short rim; filled slots keep 05dx select juice) + number keys ignored while talk is open so tray cannot swap under dialogue. Never START OVER.

Local 9/5 (BUILD 20260905dy): talk panel X consistency — fat-finger hitPad + soft ui click like craft/Jobs/BAG/chest/shop; OK button same; choice taps/number keys soft click via shared applyDialogueChoice (ride choices still skip bird-land close). Never START OVER.

Local 9/5 (BUILD 20260905dx): clearer Pip not-enough-gold toast `NEED MORE GOLD! NEED NG (HAVE MG).` + warn sparks/toast SFX; hotbar number-key + tray-tap select juice (soft screen sparks + bright rim + tiny icon lift) — keys already had ui click, now visible pop too. Never START OVER.

Local 9/5 (BUILD 20260905dw): craft panel X close (was BACK-only) + chest X close + Pip shop corner X (BYE kept) + soft ui click on those closes — matches Jobs/BAG/Stars. Never START OVER.

Local 9/5 (BUILD 20260905dv): clearer OWNED toast when buying a duplicate pole/leash/seeds (`OWNED! YOU ALREADY HAVE A POLE.` etc) + soft warm warn sparks at BUY; pole shop price shows OWNED (was 0G); craft duplicate tools `OWNED! ALREADY MADE.` + warn sparks; leash bag-full msg matches chest tip. Never START OVER.

Local 9/5 (BUILD 20260905du): Jobs panel X close (same as Stars/BAG Esc); Esc/Space dismiss uses closeShop/closeCraft helpers + soft ui click; bag Esc no longer skips toast-first dismiss order. START OVER untouched. Never START OVER.

Local 9/5 (BUILD 20260905dt): bag-full clearer toast `BAG FULL! PUT STUFF IN THE CHEST.` + soft warm warn sparks + toast SFX; chest/shop msgs clearer; river/pond/fountain unstick `TOO WET.` + splash (ocean TOO DEEP kept). Never START OVER.

Local 9/5 (BUILD 20260905ds): mute/unmute click feedback — Jobs MUTE + HUD FX/MU toast SOUND/FX/MUSIC ON|OFF + tiny soft click sparks (music button finally clicks). Never START OVER.

Local 9/5 (BUILD 20260905dr): Nim first-meet soft moon sparkle; cave sword pedestal claim steel/gold sparkle (+ auto-claim ensureCaveSword juice). Never START OVER.

Local 9/5 (BUILD 20260905dq): soft pastel sparkler when all three lights are on (THREE LIGHTS ON toast + first MOONDROP NIGHT! start). Never START OVER.

Local 9/5 (BUILD 20260905dp): nest bird give-wood wood/gold sparkle + craft SFX (BIRD STAR toast juice kept); soft trailing wake splash droplets while rowing the boat on water. Never START OVER.

Local 9/5 (BUILD 20260905do): peak PATH CLEAR celebration — big gold/stone summit sparkle burst + toast SFX when the last summit rocks smash open (was plain sparks). Never START OVER.

Local 9/5 (BUILD 20260905dn): golden swordfish catch special gold/white sparkle burst on reel-in; diamond pick pickup icy cyan/white diamond sparkle (was plain sparks). Never START OVER.

Local 9/5 (BUILD 20260905dm): Moondrop Night statue soft moon glow — cool pastel blue/lavender halo + warm core + soft sparkle twinkle on the Moon Kid (festival confetti from 05dl kept). Never START OVER.

Local 9/5 (BUILD 20260905dl): soft bedside wake sparkle after faint/death (sparks + energy refill + pink hearts — sleep already had wake juice); Moondrop Night soft pastel confetti drift while festivalOn at NIGHT in town. Never START OVER.

Local 9/5 (BUILD 20260905dk): pink heart heal juice on sleep wake (hearts refill); potato + berry eats get the same yum hearts + green energy sparkles other snacks already had (bug gap). Never START OVER.

Local 9/5 (BUILD 20260905dj): soft green energy refill sparkles on sleep wake + food eat; Stars earn toast soft gold screen sparkle; drawBagKey atlas-miss / unknown-key paint fallbacks so tray/bag never blank. Never START OVER.

Local 9/5 (BUILD 20260905di): deer flee soft tan/dirt dust + soft hop when Orion bumps/taps (rabbit/squirrel hop juice kept). Never START OVER.

Local 9/5 (BUILD 20260905dh): shop buy gold sparkle at BUY when a purchase succeeds; tiny SAVE toast on sleep day-rollover persist only (not every save — no spam). Never START OVER.

Local 9/5 (BUILD 20260905dg): critter hop juice — rabbit/squirrel bounce higher + soft hop dust when they flee Orion (walk-into or tap); idle wander stays quiet; deer hop react unchanged. Never START OVER.

Local 9/5 (BUILD 20260905df): home/town/peak lamp soft warm pulse sparks when each glow turns on (+ slightly stronger lit pulse); pad sword crescent a bit brighter. Never START OVER.

Local 9/5 (BUILD 20260905de): bridge fix wood/gold celebration sparkle when 8 wood spent; soccer kickball dust puff on kick. Never START OVER.

Local 9/5 (BUILD 20260905dd): tree fall leaf/dust puff when chop finishes to stump; chicken feather puff on scoot/hop. Never START OVER.

Local 9/5 (BUILD 20260905dc): smelt/cook flame sparks at fireplace + stove; copper/silver/gold/iron (+ bars) pickup metal sparkle (ground collect + fly-in + world nodes). Never START OVER.

Local 9/5 (BUILD 20260905db): farm well soft water shimmer + sparkle; Nim note board open parchment sparks. Never START OVER.

Local 9/5 (BUILD 20260905da): honey bun / food eat floating pink hearts + gold coin / gold pile pickup warm sparkle (ground collect + fly-in pop). Never START OVER.

Local 9/5 (BUILD 20260905cz): fountain soft water pulse + sparkle; holiday/festival lantern warmer soft pulse; mail open parchment sparks. Never START OVER.

Local 9/5 (BUILD 20260905cy): treasure chest open gold/warm sparkle burst + ore node ready twinkle (copper/silver/gold/iron world + woods silver/gold). Never START OVER.

Local 9/5 (BUILD 20260905cx): boat board/leave water splash droplets + splash SFX; bed sleep floating Z's + warm GOOD MORNING wake wash/sparks. Never START OVER.

Local 9/5 (BUILD 20260905cw): flower pick petal sparkle (pink/gold spray when town/wild flowers picked) + Stars panel earned rows use starBadge with soft twinkle. Never START OVER.

Local 9/5 (BUILD 20260905cv): door-arrival foot sparks at fade mid-swap so the new room pops softly. Never START OVER.

Local 9/5 (BUILD 20260905cu): soft cozy door fade (warm wash, ~⅓s) on house/shop/cottages/tall/L-house/mine enter+exit — not a long black screen; dog pet bounce + pink hearts when talked to (extra with leash). Never START OVER.

Local 9/5 (BUILD 20260905ct): crop ready sparkle twinkle on ripe garden plots + harvest pop sparks when picked. Never START OVER.

Local 9/5 (BUILD 20260905cs): pickaxe rock spark chips — farm/mine/peak rocks spray stone chips + pale smash flash on hit (same juice language as axe wood chips). Never START OVER.

Local 9/5 (BUILD 20260905cr): axe tree chop white hit flash + wood chip particles; fishing bite bobber splash bigger + bite flash; bird ride flight fade in/out; Pip shop idle bob + talk ! + once greet `PIP: HI! TAP ME TO SHOP.`. Never START OVER.

Local 9/5 (BUILD 20260905cq): dig mound sparkle twinkle on undug farm/woods mounds + once shovel tip `TAP A DIRT MOUND TO DIG` when shovel selected and mounds remain. Never START OVER.

Local 9/5 (BUILD 20260905cp): dusk outdoor slugs bigger (1.05 / 1.2) + warm rim glow; fence wood once-toast `TAP BUILD THEN A TILE`; chest floating CHEST label + once-toast `PUT ALL / TAKE ALL AT THE BOTTOM`. Never START OVER.

Local 9/5 (BUILD 20260905co): cozy NPC juice — Junie idle frame flip + breath bob; town/forest folk + Nim soft idle bob; bobbing ! talk cue when Orion is within 2 tiles (hidden while dialogue open). Never START OVER.

Local 9/5 (BUILD 20260905cn): town soccer Jobs `KICK THE BALL IN TOWN.` (`found.kickedTownPlayBall`); nest bird Jobs `GIVE 10 WOOD TO THE NEST BIRD` when bag has ≥10 (else BRING…); plant seed once-toast `TAP DIRT TO PLANT` + Jobs `PLANT SEEDS ON THE GARDEN DIRT.` while a seed is selected and garden empty. Never START OVER.

Local 9/5 (BUILD 20260905cm): Jobs tips — diamond pick `SMASH PEAK ROCKS WITH THE DIAMOND PICK.` / on-peak `SMASH THE PEAK ROCKS.`; evening–night outdoor `SWORD THE NIGHT SLUGS.` until first slug kill (`found.outdoorSlug`); cook/smelt toast clarity `COOKED A TROUT!` / `SMELTED A COPPER BAR!`; stove cooks tray/bag fish (parity with fireplace ore). Never START OVER.

Local 9/5 (BUILD 20260905cl): mailbox mail fun — new letters fish (Pip pole tip after welcome), bridge cheer, Moondrop Night; bobbing MAIL label when unread; Junie nudges CHECK YOUR MAIL; bed clarity — floating SLEEP, Jobs `SLEEP IN YOUR BED.` when hurt/evening/night in house, once toast `TAP THE BED TO SLEEP`. Never START OVER.

Local 9/5 (BUILD 20260905ck): kid discoverability — fishing with no pole Jobs/toast `BUY A FISHING POLE AT PIP'S.`; pier boat bobbing `GET IN` label; broken east bridge floating `8 WOOD`/`FIX!` + dialog shows how many wood you have + chop tip; Jobs `FIX THE BRIDGE WITH 8 WOOD.` when bag has ≥8. Never START OVER.

Local 9/5 (BUILD 20260905cj): every foe kill drops loot (no empty/POOF) so gold loot flash + GOT toast always fire; bigger HP pips over monsters. Builds on 05ci hit/kill juice. Never START OVER.
Local 9/5 (BUILD 20260905ci): clearer foe hit/kill feedback — longer bright white hit flash + bigger hit sparks; lingering kill burst ring after foes vanish; red HP pips over living monsters; kill loot hops taller with gold flash ring + `GOT …!` toast (or `POOF!` if empty); fewer empty mine/outdoor drop rolls; LOOT_POP_MS 280→420; belt-and-suspenders ocean deep `y` blocked on foot + unstick TOO DEEP. BACKLOG: Medium Enemies never die feedback → Local 05ci (needs live); ocean deep walk harden noted on Ocean/boats Partial. Never START OVER.
Local 9/5 (BUILD 20260905ch): moon shard / Mountain Heart hotbar carry cue — pin shard to tray on pickup + bobbing `SHARD → HOME` chip above hotbar until HOME GLOW (consumes tray shard); `HEART → HOME` chip until first house visit after Mountain Heart; line notes on pickup. Never START OVER.
Local 9/5 (BUILD 20260905cg): HUD south clear + kid i-frame flash — CAM_PAD_BOTTOM 36→52 (forest maxY overscroll matches overworld/mine); mine south OUT gutter keep-clear widened; hearts/DAY panels no longer swallow world taps; sword pad stays fat (58); brief white full-view + Orion bloom on contact (iframeFlash) beside existing 2s i-frames. Never START OVER.
Local 9/5 (BUILD 20260905cf): tap-to-move soft-blocker harden — chickens/critters/NPCs/folk/dog/slugs no longer hard-dead-end findPath (prefer path-around, else walk-through so they scoot); Junie removed from solid[]; npcYield when Orion steps in; goWalk far/open taps always try at least one stepToward; door/scene taps + chicken scoot kept. BACKLOG: Low Open tap-to-move → Local 05cf; Ocean/boats Medium Partial notes rideable pier boat Local 05a–05bo+ (needs live). Never START OVER.
Local 9/5 (BUILD 20260905ce): BAG empty-90 remirror — if the 90-grid is empty and the tray has stacks, share non-tool tray stacks into bag cells without emptying the hotbar (30k claim); tools stay tray-only; pickup of a mirror clears every alias + remembers tray origin so bag↔tray swap (05be/05x FIXED) cannot mint a second stack. Autotest: mirror wood/stone/flower, no seed/axe, bagCount no-double, silverBar↔wood swap. Never START OVER.
Local 9/5 (BUILD 20260905cd): cozy torch/lamp falloff in mine/stairs/cave interiors — soft vignette + warm pools near lanterns/moon altar (kid-readable, not pitch black); islandCave shares cave tint path. BACKLOG: Mine look → Local 05cd; Car tiny → Local 9/5 05cc (needs live); OUT High → Local 05bx clearer signs. No DAY_MS / walk energy / Orion / grass / evening outdoor / START OVER.
Local 9/5 (BUILD 20260905cc): Reed car denser+bigger — re-BOX Imagine (05at src) to 3× frames (side 72×48, vert 48×60), pink scrub, atlas ASSET_REV=467501; draw scale 2 → on-screen ~2× vs 05at (144×96 / 96×120 vs people 16×32); hit/lamp/shadow match; town cart kick-Jobs kept. Imagine regen unavailable this agent (used existing Imagine + BOX). Never START OVER.
Local 9/5 (BUILD 20260905cb): three-lights story spine — Jobs tips `LIGHT THE HOME LAMP.` / `LIGHT THE TOWN LAMP.` / `LIGHT THE PEAK LAMP.` then `A SHY GLOW WAITS AT NIGHT.`; Junie + Nim notes guide Home→Town→Peak; lighting all three toasts `THREE LIGHTS ON. WAIT FOR NIGHT.` (once) and at NIGHT enables festivalOn with toast `MOONDROP NIGHT!` (Nim still thanks on first talk); HUD chip MOONDROP NIGHT. Existing stubs (houseLamp/homeGlow, Pip shopGlow, moonAltar/peakGlow, festivalOn). No DAY_MS / walk energy / Orion art / farm grass / evening color / START OVER.
Local 9/5 (BUILD 20260905ca): kid kickballs on the farm yard (12,32) + town plaza (44,31) — walk/bump/tap/Space kicks, slides 4–6 tiles, bounces off solids; persist tx/ty; Jobs `KICK THE BALL ON THE FARM.` after the cart job. Town red cart kick + `KICK THE CART IN TOWN.` kept (30s/31o). Code-paint cozy soccer (no atlas). Never START OVER.
Local 9/5 (BUILD 20260905bz): sword pad omni harden — fat-finger strike hits all 8 neighbors regardless of facing (adjacentFoe diagonals + occupy); bats keep Chebyshev≤2 reach after hop so 2nd tap kills; damage still on press; clearer longer crescent (SWING_MS 480) + soft omni spark ring; pad remash ~90ms; 31t pad-over-OUT kept; tray sword pin (05ay/04c) untouched. Space+hotbar already PASS live. Never START OVER.
Local 9/5 (BUILD 20260905by): tall cottage + L-shaped town house enterable cozy rooms (door tap walks to stoop then enters like shop/house; indoor furniture + OUT doormat back to town; unique exterior paintings kept; Pip shop door untouched). Blue cottage + red-roof cottages still enterable. Never START OVER.
Local 9/5 (BUILD 20260905bx): mine exit findable — stronger bobbing gold OUT/UP floating labels on ladders (door-sign style); once-per-session toast + Jobs tip `FOLLOW UP SIGNS TO OUT` when underground (incl. load deep); Space/E climbs facing or adjacent UP/OUT/DOWN; 31t pad-over-OUT kept; no save wipe / never START OVER.
Local 9/5 (BUILD 20260905bw): tree canopy hide — when Orion is Y-sorted north of a trunk and dense Imagine pine/oak/birch would fully cover him, peek a 14px head/shoulders band above that canopy after the actor pass. Cozy foot Y-sort kept (south=front, north=behind); no global +64. 05ba north-rim foot boost kept. Day-clock Critical row → Local 9/5 05bq (needs live). Never START OVER.
Local 9/5 (BUILD 20260905bv): nest bird cozy loop finish — talk with ≥10 wood takes wood + `GAVE 10 WOOD!` + thank-you / BIRD STAR / `WANT A RIDE?` choices (TREE/HOME/TOWN/CAVE/PEAK/STAY); rides land with notes; Jobs tips for wood/ride; bigger nest-bird talk footprint; bird stays after dialog dismiss (`ensureGiantBirdLanded`); TREE 1 nest still 3 eggs / no pickup; number keys pick ride choices. Applied WIP 05bs stash favoring main for 05bt–05bu. Never START OVER.
Local 9/5 (BUILD 20260905bu): peak rock crack stages + chicken scoot + palm chop — diamond-pick hits show progressive stoneSh/woodOut crack chips (5 stages over 10 hits, not darken-only); 05bt PATH CLEAR / peakRocksCleared / no painted double-draw kept. Chicken tap/walk scoots again (sprite tap was react-only); penned hens hop ≤2 tiles. Palm axe-chop finishes to stump + wood (was HP-only, never fell). Prior 05bt/05bs kept. Never START OVER.
Local 9/5 (BUILD 20260905bt): peak summit rocks really clear — painted pile scrubbed from peakMap so only the smashable prop remains; diamond pick 10-hit finish removes prop, opens walk cols 18–20 rows 2–5, persists peakRocksCleared, busts stale peak cache. Prior 05bs big-tree ladder kept. Never START OVER.
Local 9/5 (BUILD 20260905bs): big-tree climb ladder denser + bigger — Imagine ladder re-BOX to 48×72 (loose pink chroma scrub), atlas pack ASSET_REV=452632; TREE draws at 32×48 (not tiny half-scale); mine/others keep half-scale 24×36; fatter TREE tap target. Never START OVER.
Local 9/5 (BUILD 20260905br): gentle overworld slugs — farm-edge + woods (slime art); day 1 / evening–night up to 3 on farm, 2 in forest; 2hp / 1♥ bump / longer idle / home radius 3; sword-kill drops pebble/mushroom/coin; mine combat untouched. Never START OVER.
Local 9/5 (BUILD 20260905bq): day/time clock race harden — dedicated clockMark (not shared gameplay dt), 50ms step cap, at-most-one day rollover per tick, reset baseline on UI-pause / visibility / pageshow so tab-sleep cannot dump into dayMs, single-flight rAF scheduleLoop, deferred phase-change persistSave; HUD tint samples frameDayT. DAY_MS frozen (480000). ASSET_REV unchanged. Never START OVER.
Local 9/5 (BUILD 20260905bo): island boat stranding fix — while aboard, all ocean sand/pier `f` is rowable so GET OUT works anywhere on the island beach; enterIslandCave / leave-ocean auto-docks via dockBoatAt (toast `BOAT STAYS HERE.`); applyScene docks before saveScene when leaving ocean aboard; exitIslandCave ensures visible boat at boatDock (default near island cave shore if null); boatDock already in save. Never START OVER.
Local 9/5 (BUILD 20260905bn): house fireplace smelt — select copper/silver/goldore (or ore in tray), tap/Space adjacent to fireplace → 1 ore = 1 bar; toast `SMELTED COPPER!` / `SMELTED SILVER!` / `SMELTED GOLD!` (ore-only, no wood). Jobs tip `SMELT ORE AT THE FIREPLACE` when any ore in tray/bag; first select in HOUSE toasts `TAP THE FIREPLACE TO SMELT` (unlocked.fireplaceSmeltTip). Bars already on inventory/chest/save keys. Density guard kept (ASSET_REV=451204). Never START OVER.
Local 9/5 (BUILD 20260905bm): stove cook discoverability — Jobs tip `COOK FISH ON THE STOVE` when any raw fish is in tray/bag; first time selecting a raw fish while in HOUSE toasts `TAP THE STOVE TO COOK` (once per save via unlocked.stoveCookTip). Stove cook from 05be/05bf unchanged. Never START OVER.
Local 9/5 (BUILD 20260905bl): kid-visible tired Z's — energy ≤25 shows 1–3 outlined floating Z's over Orion's head (2× scale, warm fill + plum outline, first Z immediate; stronger at ≤12 / 0); also above faint pose. Walk energy / DAY_MS untouched. Density guard kept (ASSET_REV=451204). Never START OVER.
Local 9/5 (BUILD 20260905bk): fences pick up (axe/shovel/empty hand, BUILD off) — 1 wood to bag + FENCE PICKED UP toast; BUILD-on place unchanged. Density guard kept (ASSET_REV=451204). Never START OVER.
Local 9/5 (BUILD 20260905bj): pickaxe no longer destroys player-placed dirt paths (Space/swing/tap); paths stay; rocks still smash. Density guard kept (ASSET_REV=451204). Never START OVER.
Local 9/5 (BUILD 20260905bi): more Imagine pine/oak/birch/palm on farm rim, town edges, ocean cove, and forest fillers; scatter uses typed trees; palm solid+hit; paths (WOODS/MINE/OCEAN/house/crops) kept clear. Density guard kept (ASSET_REV=451204). Never START OVER.
Local 9/5 (BUILD 20260905bh): indoor dog roam livelier when home — shorter idle (~160–500ms), faster house steps (1.75), multi-tile room wander via findPath; dogOk still blocks house exit; outdoor tray-leash follow from 04k unchanged. Density guard kept (ASSET_REV=451204). Never START OVER.
Local 9/5 (BUILD 20260905bg): only 1 fishing pole forever — dedupe tray/bag/chest/held on load/grant/bag drop/stash; Pip buy already OWNED (bagCount too); putInChest blocks pole; never stack count>1. Needs live verify. Bag swap left alone (05be live FIXED). Never START OVER.
LIVE 9/5 ~7:10–7:23pm (BUILD 20260905be, household Day 2484→2485 Spring): first live of 05be — bag drag swap **FIXED** (wood×2↔silver; neither vanished; verifies 05x); OCEAN floating door-sign label **PASS** (05az); farm dig mounds visible **PASS** (05ax visual); panel world-tap dismiss **PASS** (05bc, Orion did not walk); tray icons STILL dense/no pink plates; tray sword STILL FIXED slot 0; south camera STILL PASS; clock STILL races (2484 Eve→2485); stove/woods/chicken/mine/fish UNTESTED. Screenshots `/workspace/playtest-1910/`. Never START OVER.
Local 9/5 (BUILD 20260905bf): Imagine stove prop + cooked-fish plate UI icons (BOX downsample, atlas 2×); stove gameplay from 05be kept. Never START OVER.
Local 9/5 (BUILD 20260905be): house stove cooks fish (select raw → tap/Space STOVE → cooked twin); cooked heals more; Pip sells cookedTrout; chest/save keys; stump chroma already clean in atlas. LIVE 9/5 ~7:10–7:23pm: first live — bag swap **FIXED**; door signs/dig mounds/panel dismiss PASS; stove UNTESTED (no raw fish); clock STILL races. Never START OVER.
Local 9/5 (BUILD 20260905bd): HUD Stars uses small starBadge (not trophy); real hen chicken frames; ocean 64×56 (+8 beach L/R, +16 south water, ~3× island further south with enterable cave + visible Diamond Pickaxe); house/shop/cave doormat OUT label; stump pink scrub pass. Never START OVER.
Local 9/5 (BUILD 20260905bc): world tap that closes bag/Jobs/Stars/talk/shop/notes/wipe confirm swallows that press (ignoreWalkTap until pointerup) and clears frozen walk — no goWalk/tool on the dismiss tap. LIVE 9/5 ~7:10pm: panel dismiss **PASS**. Never START OVER.
Local 9/5 (BUILD 20260905bb): outdoor day/night tint from one per-frame clock sample; farm uses the same night grade lift as forest (GRADE_KEYS evening frozen; forestNightFlora extras stay forest-only); scene enter clears stale grade so forest→farm cannot skip/lag wash. Never START OVER.
Local 9/5 (BUILD 20260905ba): Orion stays visible on the northernmost overworld walkable tiles — playerDrawFoot boost on ty<=2 (no global +64), overRim draws after ground so north overhang sits under actors, CAM_PAD_TOP 26→32. Cozy mid-map canopy Y-sort unchanged. Never START OVER.
Local 9/5 (BUILD 20260905az): WOODS/MINE/OCEAN/PEAK door signs use Imagine plaque + floating shaft labels (WOODS/FARM/MINE/OCEAN/PEAK/ISLAND) so they no longer read as lamp posts; recentered woodsSign art. LIVE 9/5 ~7:10pm: OCEAN floating label **PASS**. Never START OVER.
Local 9/5 (BUILD 20260905ay): only one weapon in the 10-tray at a time (sword/bow; tools stay). Second weapon → bag; cave sword pin still evicts bow. Never START OVER.
# Moondrop Mountain backlog

Local 9/5 (BUILD 20260905ax): farm dig mounds (8 marked grass spots; shovel walk on normal grass restored; woods dig intact). LIVE 9/5 ~7:10pm: mounds visible **PASS** (shovel dig untested). Never START OVER.
Local 9/5 (BUILD 20260905av): fix 2×→1× flicker — version.json was stuck on 05x; bustUrl now uses HTML BUILD; checkFreshBuild never downgrades to stale version. Never START OVER.
Local 9/5 (BUILD 20260905au): 2× forest rabbit/deer/squirrel. Never START OVER.
Local 9/5 (BUILD 20260905at): denser bigger Reed car (~1.5×). Never START OVER.
Local 9/5 (BUILD 20260905as): 2× forestChest + chicken. Never START OVER.
Local 9/5 (BUILD 20260905ar): 2× flowerbox/woodsSign/statue/counter. Never START OVER.
Local 9/5 (BUILD 20260905aq): denser fences (Imagine, no code-paint) + 2× townFlower/inndoor. Never START OVER.
Local 9/5 (BUILD 20260905ap): 2× doormat/housePlant/chair/window. Never START OVER.
Local 9/5 (BUILD 20260905ao): dog anchor fix + 2× moonAltar/houseLamp/shopSign. Never START OVER.
Local 9/5 (BUILD 20260905an): palm trees on ocean beach/island + 2× dog. Never START OVER.
Local 9/5 (BUILD 20260905am): 2× mailbox/hole/ladder/swordPedestal. Never START OVER.
Local 9/5 (BUILD 20260905al): 2× note/log/well props. Never START OVER.
Local 9/5 (BUILD 20260905ak): 2× weed/tallGrass/chest props. Fence Imagine parked (code-paint overlay). Never START OVER.
Local 9/5 (BUILD 20260905aj): 2× rock/stump/crate/lantern props (32→16 / lantern 32×48→16×24 NN). Never START OVER.
Local 9/5 (BUILD 20260905ai): 2× berryBush + toadstool. Never START OVER.
Local 9/5 (BUILD 20260905ah): 2× fern prop. Never START OVER.
Local 9/5 (BUILD 20260905ag): 2× peakRocks + wildflower props; prior 05af cave fixes + island diamond pick. Never START OVER.
Local 9/5 (BUILD 20260905af): cave note no longer exits (OUT pad shrunk); loose cave mushrooms pickable after quest mush; sword reach adjacent-only; island cave Diamond Pickaxe + 10-hit peak rocks. Never START OVER.
Local 9/5 (BUILD 20260905ad): rowboat stays where you GET OUT (island-safe); boatDock saved. Never START OVER.
Local 9/5 (BUILD 20260905ac): ocean cove expanded to 48×40 with wider beach, longer pier path, south sand island stub (cave/Diamond Pickaxe next). Household save rebuilds ocean if old size cached. Never START OVER.
Local 9/5 (BUILD 20260905x): atomic bag/tray index swap — pickup clears one slot only; drop snapshots held+target then writes both; pocketCopy never nulls a keyed stack (count<1→1). Fixes live 05v wood→silverBar vanish (05d/05e/05f claimed fixes). LIVE 9/5 ~7:10pm via 05be: bag swap **FIXED**. Never START OVER.

Local 9/5 (BUILD 20260905t): restore pickaxe/carrot (and other icons over-scrubbed in 05s) from Imagine with safer magenta key — no pink bg, icons intact. Never START OVER.
Local 9/5 (BUILD 20260905s): scrub leftover magenta/pink chroma on pickaxe + carrot (veggie) tray icons (and any other ui/*.png still leaking pink). Never START OVER.
Local 9/5 (BUILD 20260905r): Imagine 32×32 fish icons for all FISH_KINDS (minnow→goldenSwordfish); paintFishIcon prefers sprite. Bare flower/berry/acorn already in 05q. Never START OVER.
Local 9/5 (BUILD 20260905q): re-Imagine tray flower/berry/acorn/pinecone/apple/carrot as bare items (no picture-frame / plate / UI box). Never START OVER.
Local 9/5 (BUILD 20260905o): Imagine 32×32 berry/bread/pie/acorn/pinecone/copperBar (replacing code-paint in tray when sprite present). Never START OVER.
Local 9/5 (BUILD 20260905n): Imagine 32×32 cropYoung/cropReady/crate/lantern + new apple/potato tray icons. Never START OVER.
Local 9/5 (BUILD 20260905m): Imagine 32×32 tray misc — mooncrystal, pebble, goldPile, letter, shield, trophy. Never START OVER.
Local 9/5 (BUILD 20260905l): Imagine 32×32 tray ores/loot — copper, iron, gem, goldCoin, sapphire, moonshard. Never START OVER.
Local 9/5 (BUILD 20260905k): Imagine 32×32 tray food/farm — honeybun, mushroom, veggie, townFlower, strawHat, sprout. Never START OVER.
Local 9/5 (BUILD 20260905j): Imagine 32×32 tray tools — axe, pickaxe, shovel, bow, ironSword, leash. Household save intact. Never START OVER.
Local 9/5 (BUILD 20260905i): first piece-by-piece Imagine 32×32 tray icons — sword, wood, stone, seed, fishingPole (BOX/AREA downsample into ui/; atlas packed). drawUiIcon already blits larger frames into 16 logical (=32 device under BUFFER=2). More icons later. Household save intact. Never START OVER.
Local 9/5 (BUILD 20260905h): boat row fix — aboard ocean taps path/row on water (boatOk: water y + pier/sand f next to water); fishing / YOU NEED A FISHING POLE blocked while onBoat so water taps no longer steal the row. GET OUT still pier/shore only. Keeps 05g 2× BUFFER. Household save intact. Never START OVER.
Local 9/5 (BUILD 20260905g): 2× internal canvas buffer (640×384 backing; CSS still VIEW_W/H × scale) so tray/bag icons can later show real 32×32 detail at the same on-screen window. Existing 16×16 art NN-scaled by the buffer (looks the same); drawUiIcon scales denser atlas frames → 16 logical. Icons still 16 this ship — Imagine regen piece-by-piece next. Household save intact. Never START OVER.
Local 9/5 (BUILD 20260905f): bag/tray true one-tap swap — strip tray↔bag shared-object aliases (no re-mirror), setPocket always clones (tools count 1), pickup clearRecEverywhere + pocketCopy, drop puts displaced back at origin (or parks / keeps on cursor — never vanish). Fixes 05e live vanish / 05d shuffle. LIVE 9/5 ~4:19–4:24pm: first live of 05f–05v — bag drag swap **STILL FAIL / WORSE** (wood onto silver; silver vanished). Imagine tray icons **PASS**; south camera STILL PASS; tray sword STILL FIXED. Never START OVER.
Local 9/5 (BUILD 20260905e): bag/tray swap rewrite — copy-on-pickup (no shared cell refs), true two-slot swap on drop, stackable merge when same key. Fixes 05d live shuffle. LIVE 9/5 ~1:13–1:18pm: first live of 05e — bag drag swap **STILL FAIL / WORSE** (source emptied; target took item; displaced stack vanished — not a true swap). South camera STILL PASS; tray sword STILL FIXED. Never START OVER.
Local 9/5 (BUILD 20260905d): bag/tray drag onto a filled cell instantly swaps (displaced item returns to the pickup slot — no second drag). LIVE 9/5 ~10:07–10:12am: first live of 05d — bag drag swap **FAIL** (cells changed but no clean instant swap); south camera **PASS** (05c); tray sword STILL FIXED; boat/chicken/fish UNTESTED (bridge NEED 8 WOOD). Never START OVER.
Local 9/5 (BUILD 20260905c): overworld south camera uses the same CAM_PAD_BOTTOM keep-Orion-above-hotbar pull as forest/mine/ocean (was missing — sprite walked under the tray). LIVE 9/5 ~10:07–10:12am via 05d: south camera **PASS** (Orion stayed above hotbar). Farm grass / Orion / DAY_MS / walk energy / evening / START OVER untouched. Household save intact. Never START OVER.
Local 9/5 (BUILD 20260905b): fishing cast draw is a short wooden pole from the hands + thin light-blue line (no face-tongue); Imagine fishingPole tray/shop icon packed. Household save intact. Never START OVER.
Local 9/5 (BUILD 20260905a): rideable rowboat at the ocean pier — GET IN / row on water / GET OUT only on sand or pier (TOO DEEP out on water); leave ocean blocked while aboard. LIVE 9/5 ~1:12–1:30am: first live of 05a — boat **PASS**. LIVE 9/5 ~7:14–7:28am: recheck 05a — boat **STILL PASS**; tray sword STILL FIXED slot 0; fish STILL no pole (toast YOU NEED A FISHING POLE.); chicken scoot **PASS** (NEW vs prior UNTESTED); dog/mine UNTESTED; clock STILL races (Day 2395 Afternoon→2396 Night). START OVER under Jobs (not pressed). Never START OVER.
Local 9/4 (BUILD 20260904l): START OVER really wipes — block pagehide/visibility persist that rewrote the old save after removeItem; session wipe flag; bigger YES/NO. WARNING: wipes that browser's save (household Chrome too if used there). Never START OVER on the household save unless you mean it. LIVE 9/4 ~10:15–10:40pm: first live of 04l — tray sword STILL FIXED (slot 0; no sword in BAG grid); slime pad kill **PASS** (NEW vs 04e UNTESTED; ~3 Space/pad taps); contact i-frames PASS; OUT one-tap PASS; OCEAN reached PASS; ocean fish UNTESTED (no pole — toast YOU NEED A FISHING POLE); bat pad / chicken / dog UNTESTED; clock STILL races (Day 2328→2331). START OVER under Jobs (not pressed). Never START OVER.
Local 9/4 (BUILD 20260904k): dog follows outside only while LEASH is in the 10-tray; taking it out of the tray sends them home. Leaving the house with tray leash warps dog to the porch. Talk tip: PUT THE LEASH ON THE TRAY. Household save intact. Never START OVER.
Local 9/4 (BUILD 20260904j): dog follows out of the house when you own a leash (explicit bring on exit/enter; leash re-seats from save flag; snap never strands on porch). Household save intact. Never START OVER.
Local 9/4 (BUILD 20260904i): Pip shop — LEASH + FISHING POLE moved up on the list (were below the fold with no tap-scroll); list scrolls; v MORE hint. Household save intact. Never START OVER.
Local 9/4 (BUILD 20260904h): dog runs around more inside the house (faster/shorter idle); 04g pole dedupe + chicken bump kept. Still Open: boat, bigger ocean, island Diamond Pickaxe, more trees, Pip shop. Household save intact. Never START OVER.
Local 9/4 (BUILD 20260904g): only one fishing pole (dedupe tray/bag on load/grant); walk into / tap chicken scoots it off the tile. Darren 9/4 asks still Open (dog indoors livelier, boat, bigger ocean, island Diamond Pickaxe, more trees, Pip shop art). Household save intact. Never START OVER.
Local 9/4 (BUILD 20260904f): ocean pier/beach fishing has a 1-in-50 Golden Swordfish (ocean-only; farm ponds unchanged). Sword swing still 300ms. Pip shop art still queued. Household save intact. Never START OVER.

## Queued 9/4 evening (Darren asks)

Pick from the top. Expand the world creatively (bigger beach/ocean, fun Imagine art) — not a thin strip. Household save; never START OVER. Frozen: Orion art, farm grass0–3, evening color, walk energy, DAY_MS, peak summit rocks until the Diamond Pickaxe island slice lands.

| Priority | Status | Item | Notes |
| --- | --- | --- | --- |
| High | Local 9/5 05bg | Only 1 fishing pole | Cap at one forever: dedupe tray/bag/chest/held on load/grant/drop; Pip buy OWNED; never stack count>1; putInChest blocked. **Needs live verify.** |
| High | Done 9/5 7:28am live | Chickens move when walked into | LIVE 9/5 ~7:14–7:28am BUILD 20260905a: walk/tap scoot **PASS** (first live of 04g claim). |
| Medium | Local 9/5 05bh | Dog runs around inside the house | Shorter idle + faster house steps + multi-tile room wander when home; leash outdoor rules from 04k unchanged. **Needs live verify.** |
| Medium | Done 9/5 1:30am live | Boat at pier | LIVE 9/5 ~1:12–1:30am BUILD 20260905a: GET IN / row / TOO DEEP on deep water / get out on shore PASS; leave-ocean while aboard blocked (GET OUT FIRST.). |
| Medium | Done 9/5 05ac–05ad | Bigger beach / ocean world | Extend ocean scene logically + creatively with fun Imagine graphics (cove, dunes, more pier room, south deep water toward island). Make the world feel bigger. |
| Medium | Local 9/5 05bt (live TBD) | Island cave Diamond Pickaxe → peak rocks | LOCAL 9/5 BUILD 20260905bt: painted summit pile scrubbed from peakMap; smashable prop only; 10 diamond-pick hits remove prop + open walk (cols 18–20 rows 2–5) + persist peakRocksCleared + bust stale peak cache. Was Done 9/5 05af claim (regen PEAK / removable sprites) but live paint stayed after smash. Never START OVER. |
| Medium | Local 9/5 | More Imagine trees everywhere | Local 9/5 BUILD 20260905bi: farm rim + town edges + ocean cove palms + forest fillers using existing Imagine pine/oak/birch/palm; scatter typed; WOODS/MINE/OCEAN/house/crops paths clear. Needs live. Was Partial 9/5 (05z farm kind-swap only). Extra tree types via Grok Imagine + BOX/AREA downsample; props not painted-in. |
| Low | Done 9/5 05y | Pip shop glow-up | Still queued from earlier (Imagine enhance shopHouse). |


Playtest issues from the live game ([yamizzle.github.io/orion-farm](https://yamizzle.github.io/orion-farm/)). Both Grok Build and Grok Bot should pick from the top. Do not close an item without a playtest on the live URL.

Local 9/4 (BUILD 20260904e): sword swing back to 300ms; fish from OCEAN pier/beach water with the pole (same cast loop as farm ponds). Pip shop art still queued. Household save intact. LIVE 9/4 ~7:14–7:34pm: first live of 04e — tray sword STILL FIXED (slot 0); Space+hotbar swing **PASS** (NEW); bat i-frames PASS; slime contact STILL PASS; bat/slime pad kills UNTESTED this pass (swings fired, foes fled); OUT one-tap PASS; clock STILL races. Never START OVER.
Local 9/4 (BUILD 20260904d): Pip shop door is the painted opening (not the stoop square below); tap walks to shopIn then enters (no instant warp). Household save intact. Never START OVER.
Local 9/4 BUILD 20260904c tray-sword claim — mine enter/swing/openBag auto-grants cave sword (removes pedestal) and hard-pins hotbar slot 0; pad no longer leaves swordOwned false forever. Walk energy / day clock / START OVER / Orion art / grass / evening color untouched. LIVE 9/4 ~4:21–4:57pm: first live of 04c — tray sword **FIXED** (slot 0 pinned; also in BAG); slime contact STILL PASS; slime pad STILL PASS (~2–3 taps); bat pad UNTESTED. Space+hotbar still UNTESTED. Never START OVER.

Local 9/4 BUILD 20260904b tray-sword harden — no tool mirroring into bag; recover swordOwned from pocket ghosts; openBag re-pins; version.json matched. Walk energy / day clock / START OVER / Orion art / grass / evening color untouched. LIVE 9/4 ~10:11–10:29am: first live of 04b — tray sword STILL FAIL (slot 0 seeds; BAG slot 1 sword mirror STILL); bat pad kill PASS (~2 taps + loot); slime contact WORSE (hold → KO, i-frames miss); death auto-woke HOUSE (copy not shown). LIVE 9/4 ~1:28–1:36pm recheck same build — slime i-frames FIXED (hold ~4s); slime pad 1-tap PASS; bat pad STILL PASS; tray sword STILL FAIL (BAG-only). Do not mark Critical sword Done. Never START OVER.

Local 9/4 (BUILD 20260904a): sword tray harden — clear every bag/tray sword copy then pin exactly one in hotbar slot 0 (bump soft tools/kits/stacks); bag open drops stale tray aliases; picking a mirrored bag/tray cell clears all aliases so the sword cannot orphan in BAG-only. Walk energy / day clock / START OVER / Orion art / grass / evening color untouched. LIVE 9/4 ~1:16–1:34am: first live of 04a — tray sword STILL FAIL (BAG slot 1 yes; hotbar slot 0 seeds); slime/bat i-frames + pad kills STILL PASS; assets/version.json still `20260903b` while Jobs stamp is `20260904a`. Never START OVER.

Local 9/3 (BUILD 20260903b): slime combat pass — ground foes pixel-only bumps (no soft-neighbor multi-drain) + stun after bump; pad/swing reach matches bats and ground knockback no longer hops slimes away mid-combo; toughslime/bigslime HP 4/6 so always-4 pad clears them in 1–2 taps; HUD gutter nudge + floor-1 south keep-clear; Space/E takes adjacent sword pedestal before swinging; death fade copy back to THE MOUNTAIN SENT YOU HOME; cached mine foes resync combat stats; forceSwordIntoTray on mine enter. Walk energy / day clock / START OVER / Orion art / grass / evening color untouched. LIVE 9/3 ~7:16–7:38pm: first live of 03b — slime i-frames FIXED; slime pad kill FIXED (1 tap); death copy FIXED; sword in BAG FIXED (still not 10-tray); bats STILL good; gutter PASS this pass. Never START OVER.

Local 9/3 (BUILD 20260903a): combat hotfix — pad/mine swings land damage on press (not mid-arc) at always-4 dmg; bat swing reach widened; bat contact is tight pixel-only + i-frames 2000 with lag-capped tick; owned sword forced into 10-tray (swap seed/hat/leash if needed). Mine pad still works without tray sword. LIVE 9/3 ~4:13–4:26am: full-hearts farm→MINE 1 — pad bat kill FIXED (~2 taps; stone drop likely); bat i-frames FIXED (−1♥ then hold, no multi-drain); sword STILL not in tray/BAG; clock STILL races; START OVER under Jobs. LIVE 9/3 ~1:13–1:22am: PEAK cave→MINE 6 FIXED; mine sword pad NEW/visible. Do not mark Done (tray sword + clock + START OVER still open; slime/PEAK not rechecked). Walk energy / day clock / START OVER / Orion art / grass / evening color untouched. Household save intact. Never START OVER. LIVE 9/3 ~7:26–7:45am: bat i-frames + pad bat kill STILL FIXED and bat loot (copper ore) confirmed; SLIME i-frames + pad-vs-slime FAIL (new); slime spawns under the sword pad; death copy now `YOU DIED...`.

Local 9/2 (BUILD 20260831u): PEAK winding dirt is walkable (old mask hugged the left cliff); summit rocks stay blocked. LIVE 9/2 ~4:09–4:26pm: first live of 31u — PEAK painted dirt walk PASS/FIXED; summit rocks STILL blocked; cave arch → STAIRS 2 PASS. Pad kill STILL miss; bat KO STILL; pad-over-OUT STILL PASS; sword STILL pad-only; clock STILL races. Household save intact. Never START OVER.
Local 9/2 (BUILD 20260831t): pad/mine arc strikeDamage always 4 (bats 6hp / slimes 4hp die in 1–2 taps; no iron / tray sword required); sword pad checked before MINE 1 OUT prefer so pad no longer steals exit; hurtPlayer i-frames 800→1200 after contact/block. LIVE 9/2 ~10:26–11:22am: first live of 31t — pad-over-OUT FIXED; OUT one-tap PASS; pad kill FAIL (2 taps knockback only); bat multi-drain KO WORSE vs 8am; sword STILL pad-only; clock STILL races. Household save intact. Never START OVER.
Local 9/2 (BUILD 20260831s): sword pad hit is omnidirectional (8-neighbor tiles + reach 52 + Chebyshev≤1 any facing); bat/flying contact uses wider radius so adjacent-tile overlap drains hearts (i-frames kept); placeToolInTrayFirst forces sword into tray even when bag is full. LIVE 9/2 ~1:06–2:34am: first live of 31s — left/diagonal pad kill FIXED; pad crescent PASS; slime contact PASS; sword still pad-only (tray miss); bat contact UNVERIFIED (driver crash). LIVE 9/2 ~4:22–4:30am: bat contact WORSE lethal (5→KO ~10s, −1G); sword STILL pad-only; pad/slime UNTESTED (bat KO; no slime on MINE 1). LIVE 9/2 ~7:38–8:02am: bat instant-KO FIXED (1 heart + knockback); pad swings knock back but do not kill/loot; MINE 1 OUT one-tap PASS; NEW pad bottom-left edge can steal OUT exit; sword STILL pad-only; clock STILL races. Household save intact. Never START OVER.
Local 9/1 (BUILD 20260831r): fat-finger sword pad wins over stairs/holes under the button (MINE 6 UP/PEAK steal); brighter crescent slash + 560ms swing; reach 42; giveTool swaps sword into the 10-tray when tray is full of non-tools; arc keeps ticking during toasts. LIVE 9/1 ~7:40pm: pad swing FIXED (crescent visible) + adjacent snail kill; pad vs stairs PASS; tray sword still missing; contact damage UNCONFIRMED/miss on MINE 1. Household save intact. Never START OVER.
Local 9/1 (BUILD 20260831q): TREE climb-floor sky is a quiet mottled blue fill (no hashed cloud grid); leaf corners still only at the wood. LIVE 9/1 ~10:25am: TREE 1–4 sky FIXED (quiet mottled blue, leaf corners only at wood; no leaf grid / hashed clouds). TREETOP canopy PASS. Household save intact. Never START OVER.
Local 9/1 (BUILD 20260831p): TREE 1–4 sky uses clear/cloud fill; leaf-corner tiles only on sky cells touching the wood/leaf platform (not a repeating leaf grid on every "y"). TREETOP still uses canopySky. LIVE 9/1 ~10:25am via 31q: TREE 1–4 sky FIXED. Household save intact. Never START OVER.
Local 8/31 (BUILD 20260831o): owned sword swaps into the 10-tray when tray is full of non-tools; mine floors show MINE N place stamp (incl. altar floor 6); Jobs kick text says CART; ocean east foam col 31 solid on rows 8–20. LIVE 9/1 ~1:15am: first live of 31o (Jobs `20260831o`); ocean east foam FIXED; Jobs CART FIXED; sword-tray swap UNTESTED (this save owns no sword); MINE N stamp UNTESTED (overland spawn). LIVE 9/1 ~1:07pm BUILD 20260831q: MINE 1/2 place stamps PASS; fat-finger sword pad swings on mine floors; Jobs CART + town kick PASS; sword still not in tray (pad-only). Household save intact. Never START OVER.
Local 8/31 (BUILD 20260831n): TREE climb-floor sky is a new Imagine tile (clouds + leaf corners) instead of the flat blue scanline fill. Walk/platform unchanged. LIVE 9/1 ~4:21am: TREE 1–4 sky FAIL — still flat solid blue with a repeating small leaf-clump grid (not Imagine clouds + leaf corners). TREETOP Imagine canopy still looks good. 1:15am had 31n code in bundle but floors untested. Household save intact. Never START OVER.
Local 8/31 (BUILD 20260831m): ocean dirt path and pier are new Imagine tiles (31l grass-sand/sand-foam edges kept). LIVE 10:20pm: first live of 31m (Jobs `20260831m`); ocean UNTESTED (PEAK spawn, cave-down first). Household save intact. Never START OVER.
Local 8/31 (BUILD 20260831l): ocean grass-sand and sand-ocean edges are new Imagine tiles on straight rows (not 31i hard bands). LIVE 10:20pm: ocean UNTESTED (PEAK spawn). Household save intact. Never START OVER.
Local 8/31 (BUILD 20260831k): peak cave arch enters STAIRS again (31j walk-through regression). LIVE 10:20pm BUILD 20260831m: cave-down PASS (PEAK walk-in → STAIRS 2 → 1 → MINE 6 altar). Household save intact. Never START OVER.
Local 8/31 (BUILD 20260831j): longer readable sword swing (hits mid-arc), wider slash flash, fat-finger strike button bottom-left above the hotbar, swing faces nearest in-reach foe. LIVE 5:20pm: peak cave-down REOPEN (stranded); sword in BAG not tray, Space no slash, no strike btn on PEAK. Ocean UNTESTED. Household save intact. Never START OVER.
Local 8/31 (BUILD 20260831i): ocean grass-to-beach is a straight tile row (not jagged); foam/water unchanged. Household save intact. Never START OVER.
Local 8/31 (BUILD 20260831h): ocean ground restamped with Imagine transition tiles (grass, dirt, sand, foam, shallow, deep) so the shoreline is jagged like 31e; trees/flora/critters stay real props. Household save intact. Never START OVER.
Local 8/31 (BUILD 20260831g): treetop bird sits in the painted canopy nest; overlay nest sprite removed; TREE 1 nest overlay kept.
Local 8/31 (BUILD 20260831f): ocean ground is Imagine-stamped 16px tiles; trees/bushes/flowers/critters are real props (chop/pick/pull/tap); no painted-in flora; path aligned to tiles; farm grass/Orion/DAY_MS untouched.
Local 8/29 BUILD 20260829f: 10 extra tray slots + 15x6 bag (90), 100 cells total. Tray is not the first 10 of the 90. BAG button on the hotbar. Old named-inventory saves migrate (tools to tray, stacks into the 90). Household save intact. Never START OVER.
Local 8/29 ~5pm PT BUILD 20260829g: TAKE ALL uses the working BOX-cell transfer for every row with a BOX count. Footer strip so the 2pm button miss cannot land on a list PUT. Town/forest folk pause when adjacent+facing. LIVE 5:20pm: TAKE ALL FIXED; NPC freeze STILL miss. Household save intact. Never START OVER.
Local 8/29 ~6–6:30pm PT BUILD 20260829h–29l: Imagine overland-rim scenery, shovel/stone dirt walk, stumps/acorns/Pip snacks, tall fences, big town car. LIVE 8:15pm: rim pass likely bricked save spawn at (63,39) — see Critical stuck row.
Local 8/29 ~8:20pm PT BUILD 20260829m: unstick a save that loaded on the unwalkable overworld rim. LIVE 11:30pm: movement FIXED (loaded in house, walked farm/mine). Household save intact. Never START OVER.
Local 8/30 ~1:20am PT BUILD 20260830a: Stars X + header chrome close the panel (same as Esc). Town/farm folk freeze when adjacent (mid-step tiles too, facing not required); Space/tap talk opens instead of pathfinding on a mid-walk NPC. LIVE 2:03am: Stars X FIXED; Junie adjacent Space talk FIXED (stood still). Household save intact. Never START OVER.
Local 8/30 ~9:20am PT BUILD 20260830b: Mine OUT 5×5 fat-finger + BUILD place on grass. LIVE 11:20am: both FIXED. Household save intact. Never START OVER.
Local 8/30 ~11:06am PT BUILD 20260830c: unique multi-tile Pip shop / tall cottage / L-house paintings. LIVE 11:20am: art PASS; Pip shop door FAIL. Household save intact. Never START OVER.
Local 8/30 ~11:19am PT BUILD 20260830d: downsample town-house sparkle. Not separately live-scored.
Local 8/30 ~11:30am PT BUILD 20260830e: Pip shop door taps enter instead of car beep. LIVE 2:10pm: walk-in FIXED; some facade/east taps still CAR/BEEP.
Local 8/30 ~11:45am PT BUILD 20260830f: nest bird (10 wood, star, then rides). LIVE 2:10pm: nest+3 eggs on TREE 1; giant bird never landed. Household save intact. Never START OVER.
Local 8/30 ~afternoon PT BUILD 20260830g: giant bird flies in on first TREETOP enter (lands at nest); TREE 1 nest tap says THE MAMA BIRD IS UP TOP. LIVE 5:20pm: TREETOP talk PASS; sprite not seen after dismiss. Household save intact. Never START OVER.
Local 8/30 ~5:20pm PT BUILD 20260830h: Pip shop door tap enters immediately (painted door / stoop / tiles in front); parked truck body still BEEP. Not the whole facade. LIVE 5:20pm: door TAP FIXED (enter from a couple tiles away). East-of-door roof tap walks (no BEEP). Truck BEEP UNTESTED. Household save intact. Never START OVER.
Local 8/30 ~6pm PT BUILD 20260830i: snowy peak scene + cave climb from mine 6. Bird PEAK lands on the outdoor balcony; moon altar stays on mine floor 6; fallen rocks block the summit. LIVE 8:40pm: peak climb PASS (MINE 6 PEAK stairs → STAIRS 1–2 → outdoor PEAK; FALLEN ROCKS / THE PATH IS BLOCKED). Giant bird sprite FIXED visible. Household save intact. Never START OVER.
Local 8/30 ~9:50pm PT BUILD 20260830j: 22 extra pine, oak, and birch among the existing woods. Dirt road / giant-tree door / FARM exit kept clear. Household save intact. Never START OVER.
Local 8/30 ~9:55pm PT BUILD 20260830k: DAY_MS 480000 (~8 min/day); smaller START OVER under RELOAD/MUTE/BUILD; BAG copies tray goods into the 90-grid without emptying the hotbar. Household save intact. Never START OVER.
Local 8/30 ~10:05pm PT BUILD 20260830l: ocean cove south of the house, boats on the sand. Walk south from the farmhouse dirt to the OCEAN sign. LIVE 8/31 2:19am: OCEAN sign walk-in PASS (coastal path); boats not on first screen. Household save intact. Never START OVER.
Local 8/30 ~10:15pm PT BUILD 20260830m: river east of town, fix the bridge with 8 wood. Far-bank meadow. Household save intact. Never START OVER.
Local 8/30 ~10:25pm PT BUILD 20260830n: two more town houses you can walk into (blue cottage + red-roof). Luna and Maple inside. A/B still knock. Household save intact. Never START OVER.
Local 8/30 ~10:35pm PT BUILD 20260830o: house dog + Pip leash for 40 carrots. Dog follows outside with a leash. Household save intact. Never START OVER.
Local 8/30 ~10:50pm PT BUILD 20260830p: Pip HOUSE KIT (12W 8S furniture, then 20W 12S wider house) plus potato/berry seeds 8G. Seeds stay tools. Household save intact. Never START OVER.
Local 8/30 ~10:55pm PT BUILD 20260830q: Pip LAMP KIT and CRATE KIT (10G, 3 each). Tap grass/dirt/cobble to place walkable lanterns or solid crates (max 12). Wood-fence BUILD chip unchanged. Household save intact. Never START OVER.
Local 8/30 ~11:05pm PT BUILD 20260830r: weekly town holidays from dayNumber%7 (not a saved calendar). 0 MARKET DAY (crate stalls by fountain, HUD chip, Pip honey bun half price min 1G). 3 FLOWER DAY (flowers around statue). 5 EVENING/NIGHT LANTERN EVE (walkable lanterns by fountain; Moondrop Night copy/music kept if festivalOn). Other remainders none. Holiday props ephemeral. Household save intact. Never START OVER.
Local 8/30 ~11:15pm PT BUILD 20260830s: kick a ball on the town green (spawn 46,32 south of fountain). Tap or walk into it; slides 3-5 tiles in facing. Persist tx/ty. Jobs KICK THE BALL IN TOWN. until found.kickedBall. Household save intact. Never START OVER.
Local 8/30 ~11:25pm PT BUILD 20260830t: mine floors 1–6 and caveclimb 1–2 wall crates, extra lanterns, deco mushrooms via cache-safe ensureMineDecor. Household save intact. Never START OVER.
Local 8/30 ~11:15pm PT BUILD 20260830u: close missing `}` on ocean `tryTalkAdjacent` so the game boots. LIVE 11:20pm: boots (Jobs `20260830u`); first `?v=20260830u` still served 30t until a second cache-bust. Household save intact. Never START OVER.
Local 8/31 ~1:20am PT BUILD 20260831a: shovel no longer tills every farm grass tile (that stole tap-to-walk). Woods 7 mounds unchanged. Farm holes stay Open. LIVE 8/31 2:19am: first live boots (Jobs `20260831a`); shovel-walk UNTESTED (save has no shovel). Household save intact. Never START OVER.
Local 8/31 ~11:30am PT BUILD 20260831b: peak south FARM exit (woodsSign) + climb1 DOWN labeled MINE + safer mine-6 land; tap-to-walk paths toward nearest walkable under the tap; ocean deep-water walk mask tightened. LIVE 2:46pm 31d: tap-walk FIXED; cave-down FIXED (31d removed FARM warp); ocean UNTESTED. Household save intact. Never START OVER.
Local 8/31 ~3:20pm PT BUILD 20260831e: ocean overlay boats removed; new top-down cove map (no fences, overland camera). Walk path/sand/dock only. Household save intact. Never START OVER.
Local 8/31 ~1:40pm PT BUILD 20260831d: peak FARM sign and south-balcony farm warp removed. Cave is the only way down. LIVE 2:46pm: FARM sign ABSENT; cave-down to MINE 6 PASS. Household save intact. Never START OVER.
Local 8/31 ~1:35pm PT BUILD 20260831c: outdoor peak no longer draws the inside-looking-out caveMouth overlay; peakMap outdoor painting stays; cave still enterable. LIVE 2:46pm: outdoor PEAK looks outdoor (no cave overlay). Household save intact. Never START OVER.

Last live pass: **2026-09-05 ~4:19–4:24pm PT** BUILD 20260905v (desktop; URL `?v=20260905t` / `version.json` 05t; Jobs stamp `20260905v`). First live since 05e (covers 05f–05v). Continued box Chrome save Day 2463 SPRING AFTERNOON→EVENING (overworld, ~4/5♥, 0G). **NEW/PASS:** Imagine tray/hotbar icons crisp, no pink/magenta bg (`03-hotbar.webp`). **STILL FAIL / WORSE:** bag drag onto filled cell — wood took silver-bar cell; silver vanished (`04-bag-before.webp`/`05-bag-after.webp`; 05f claim miss). **STILL PASS:** south camera. **STILL FIXED:** tray sword slot 0. Bridge/chicken UNTESTED. START OVER not pressed. Never START OVER. Screenshots `/workspace/playtest-1619/`.

Highest-leverage theme: bag drag swap **STILL FAIL / WORSE** on first live of 05f–05v (displaced item still vanishes). Imagine tray icons look good live. Tray sword + south camera still good. Still open: bag swap true fix; ocean fish (need pole); boat recheck; bridge wood; bat pad; day-clock races; START OVER wipe (04l claim, not pressed); dog leash; version.json lag (`05t` vs Jobs `05v`).

## Live playtest 9/5 ~4:19–4:24pm PT (BUILD 20260905v)

- Continued box Chrome save — never START OVER. Day 2463 SPRING AFTERNOON (overworld, ~4/5♥, 0G) → Day 2463 SPRING EVENING. URL cache-bust `?v=20260905pt1619` (landed `?v=20260905t`); Jobs stamp `20260905v`. First live of 05f–05v (post-05e). ~5 min; no crash; START OVER not pressed.
- **NEW/PASS:** Imagine 32×32 tray/hotbar icons — crisp art, no magenta/pink chroma leak (`03-hotbar.webp`). First live of 05i–05t icon ships.
- **STILL FAIL / WORSE:** Bag drag onto a filled cell — wood moved onto silver-bar cell; silver vanished (not returned). `04-bag-before.webp` / `05-bag-after.webp`. 05f one-tap-swap claim did not hold live.
- **STILL PASS:** Overworld south camera — Orion stayed above the hotbar (`06-south-camera.webp`).
- **STILL FIXED:** Sword hard-pinned in 10-tray hotbar slot 0 (`03-hotbar.webp`).
- **UNTESTED:** Pier rowboat / chicken scoot / ocean fishing / bridge.
- **NIT:** Live `assets/version.json` still `20260905t` while Jobs/index BUILD is `20260905v`.
- Screenshots `/workspace/playtest-1619/` (`01-land.webp` … `06-south-camera.webp`).

## Live playtest 9/5 ~1:13–1:18pm PT (BUILD 20260905e)

- Continued box Chrome save — never START OVER. Day 2440 SPRING MORNING (FARM, 5/5♥, 0G) → Day 2440 SPRING AFTERNOON (FARM, 5/5♥, 0G). URL cache-bust `?v=20260905pt1313`; Jobs stamp `20260905e`. First live of 05e. ~5 min; no crash; START OVER not pressed.
- **STILL FAIL / WORSE:** Bag/tray drag onto a filled cell — source emptied, target took the dragged item, displaced stack vanished (not returned to pickup slot). `04-bag-before.webp` / `05-bag-after.webp`. 05e rewrite claim did not hold live.
- **STILL PASS:** Overworld south camera — Orion stayed above the hotbar (`06-south-camera.webp`).
- **STILL FIXED:** Sword hard-pinned in 10-tray hotbar slot 0 (`03-hotbar-sword.webp`).
- **UNTESTED:** Pier rowboat / chicken scoot / ocean fishing — river bridge blocked (`THE BRIDGE IS OUT. NEED 8 WOOD.` — `07-boat-bridge-blocked.webp`); no fishing pole checked this pass.
- **STILL:** Day clock phases race (Morning→Afternoon across short pass).
- Screenshots `/workspace/playtest-1313/` (`01-land.webp` … `08-final.webp`).

## Live playtest 9/5 ~10:07–10:12am PT (BUILD 20260905d)

- Continued box Chrome save — never START OVER. Day 2417 SPRING MORNING (FARM, 4/5♥, 0G) → Day 2417 SPRING AFTERNOON (FARM, 4/5♥, 0G). URL cache-bust `?v=20260905pt1007`; Jobs stamp `20260905d`. First live of 05d. ~5 min; no crash; START OVER seen in Jobs, not pressed.
- **NEW/PASS:** Overworld south camera — Orion stayed above the hotbar at the south edge (`06-south-edge.webp`). First live of 05c claim.
- **NEW/FAIL:** Bag/tray drag onto a filled cell — cells changed (wood stack/hotbar shuffled) but no clear instant swap with displaced item returning to the pickup slot (`04-bag-before.webp`, `05-bag-after.webp`). First live of 05d claim.
- **STILL FIXED:** Sword hard-pinned in 10-tray hotbar slot 0 (`03-hotbar.webp`).
- **UNTESTED:** Pier rowboat / chicken scoot / ocean fishing — river bridge blocked (`THE BRIDGE IS OUT. NEED 8 WOOD.` — `07-bridge-blocker.webp`); no fishing pole in tray/bag.
- **STILL:** Day clock phases race (Morning→Afternoon across short pass). START OVER under Jobs (04l wipe claim not pressed).
- Screenshots `/workspace/playtest-1007/` (`01-land.webp` … `08-final.webp`).

## Live playtest 9/5 ~7:14–7:28am PT (BUILD 20260905a)

- Continued box Chrome save — never START OVER. Day 2395 SPRING AFTERNOON (near OCEAN, ~2–5♥, 0G) → Day 2396 SPRING NIGHT (TOWN, 5♥, 0G). URL cache-bust `?v=20260905pt0714`; Jobs stamp `20260905a`. Recheck of 05a (same build as 1:12am). ~14 min; no crash; START OVER seen in Jobs, not pressed.
- **STILL PASS:** Pier rowboat — GET IN, row, GET OUT on pier (`04-boat.webp`).
- **STILL FIXED:** Sword hard-pinned in 10-tray hotbar slot 0 (`03-hotbar.webp`).
- **NEW/PASS:** Chicken scoot on walk/tap contact — first live of 04g (`06-chicken.webp`).
- **STILL:** Ocean fishing — no pole in tray/bag; water tap toast `YOU NEED A FISHING POLE.` (`05-fishing.webp`). Day clock races (2395 Afternoon→Evening→2396 Morning→Evening→Night).
- **UNTESTED:** Dog/leash; MINE / bat pad / slime.
- Screenshots `/workspace/playtest-0714/` (`01-land.webp` … `99-end.webp`).

## Live playtest 9/5 ~1:12–1:30am PT (BUILD 20260905a)

- Continued box Chrome save — never START OVER. Day 2352 SPRING MORNING (overworld near OCEAN sign, 2/5♥, 0G) → Day 2352 SPRING EVENING (same, 2/5♥, 0G). URL cache-bust `?v=20260905pt0112`; Jobs stamp `20260905a`. First live of 05a. ~15–20 min; no crash; START OVER seen in Jobs, not pressed.
- **NEW/PASS:** Pier rowboat — GET IN, row on water, TOO DEEP on deep water, BACK ON SHORE / get out on sand or pier; leave-ocean exit blocked while aboard (GET OUT FIRST.).
- **STILL FIXED:** Sword hard-pinned in 10-tray hotbar slot 0 (`03-hotbar.png`).
- **UNTESTED:** Ocean fishing (no pole in tray/bag); MINE / bat pad / slime; chicken scoot; dog/leash.
- **STILL:** Day clock phases race (Morning→Evening across navigation; no day number rollover this pass). START OVER under Jobs (04l wipe claim not pressed).
- Screenshots `/workspace/playtest-0112/` (`02-jobs.png`, `03-hotbar.png`, `09-fish.png`).

## Live playtest 9/4 ~10:15–10:40pm PT (BUILD 20260904l)

- Continued box Chrome save — never START OVER. Day 2328 SPRING EVENING (WOODS, 2/5♥, 0G) → Day 2331 SPRING EVENING (OCEAN, 2/5♥, 0G). URL cache-bust `?v=20260904pt2215`; Jobs stamp `20260904l`. First live of 04l. ~20–25 min; no crash; START OVER seen in Jobs, not pressed.
- **STILL FIXED:** Sword hard-pinned in 10-tray hotbar slot 0; BAG 90-grid had no sword icon (`04-bag.png`, `05-mine1-hotbar.png`).
- **PASS (was UNTESTED on 04e):** Slime pad/Space kill — slime gone after ~3 inputs (`06-slime-kill.png`).
- **PASS:** Contact i-frames — hold ~4.5s adjacent, no multi-drain (`07-contact-iframe.png`).
- **PASS:** MINE 1 OUT one-tap (`08-out-pass.png`).
- **PASS:** Reached OCEAN from farm path (`09-ocean-shoreline.png`).
- **UNTESTED:** Ocean pier/beach fishing — no fishing pole in tray/bag; water tap toast `YOU NEED A FISHING POLE.` (`11-fishing-no-pole.png`). Bat pad kill; chicken scoot; dog/leash.
- **STILL:** Day clock races (2328→2331 across short pass). START OVER under Jobs (04l wipe claim not pressed).
- Screenshots `/workspace/playtest-2215/`.

## Live playtest 9/4 ~7:14–7:34pm PT (BUILD 20260904e)

- Continued box Chrome save — never START OVER. Day 2307 (MINE 1, 5♥, 0G) → Day 2308 (FARM, 2♥, 0G). URL cache-bust `?v=20260904pt1914`; Jobs stamp `20260904e`. First live of 04e. ~15–20 min; no crash; START OVER seen in Jobs, not pressed.
- **STILL FIXED:** Sword hard-pinned in 10-tray hotbar slot 0 (selected); not duplicated in BAG (`06-tray-check.png`, `08-bag-open.png`).
- **NEW/PASS:** Space+hotbar — with slot 0 sword selected, Space fired a sword swing (`34-space-hotbar-swing.png`). Was UNTESTED on 04c.
- **PASS (was UNTESTED 04c):** Bat i-frames — one contact hit, then hearts held ~4s adjacent (`21-bat-iframe-hold.png`).
- **PASS:** Slime contact i-frames — one hit, then hearts held ~4s (`23-slime-contact-hold.png`).
- **UNTESTED this pass:** Bat pad kill; slime pad kill (pad/swing activated but foes moved out of range — no regression shown vs 04c).
- **PASS:** MINE 1 OUT one-tap exit to farm.
- **STILL:** Day clock races (2307→2308 across pass). START OVER under Jobs.
- **UNTESTED:** Pip shop door (04d); ocean pier/beach fishing (04e).
- Screenshots `/workspace/playtest-1914/`.

## Live playtest 9/4 ~4:21–4:57pm PT (BUILD 20260904c)

- Continued box Chrome save — never START OVER. Day 2288 SPRING NIGHT (MINE 1, 5/5 hearts, 0G) → Day 2289 SPRING AFTERNOON/MORNING (MINE 1, 5/5♥, 0G). URL `?v=20260904c`; Jobs stamp `20260904c`. First live of 04c. ~15–20 min; no KO / no crash.
- **FIXED (04c claim):** Sword hard-pinned in 10-tray hotbar slot 0 (selected) and also in BAG (`tray-check.webp`, `bag-check.webp` in `/workspace/playtest-1621/`). Was BAG-only on 04b.
- **PASS:** Slime contact i-frames — held ~5s, stayed 5/5♥ (`slime-contact.webp`).
- **PASS:** Slime pad kill — ~2–3 sword-pad taps (`slime-pad.webp`).
- **UNTESTED:** Bat pad / bat i-frames; Space+hotbar swing.
- **STILL:** START OVER under Jobs (not pressed). Clock 2288 Night → 2289 Afternoon across pass.
- Screenshots `/workspace/playtest-1621/`.

## Live playtest 9/4 ~1:28–1:36pm PT (BUILD 20260904b)

- Continued box Chrome save — never START OVER. Day 2239 SPRING NIGHT (MINE 1, 5/5 hearts, 7G) → Day 2240 SPRING EVENING (MINE 1, 4/5♥, 76G). URL `?v=20260904b`; Jobs stamp `20260904b` (`jobs.webp`). Same build as 10:11am. Jobs text: KICK THE CART IN TOWN. ~10 min; no KO.
- **STILL FAIL (04b claim miss):** Sword not in 10-tray hotbar — slot 0 seeds; tray = seeds/crate/berry/wood/stone/ore/… (`tray-check.webp`). Sword **still** in BAG grid slot 1 only (`bag-check.webp`).
- **FIXED vs 10:11am WORSE:** Slime contact i-frames — one bump then held adjacent ~4s with no further drain (`slime-contact.webp`).
- **PASS (first 04b verify; was UNTESTED 10:11am):** Slime pad kill — 1 sword-pad tap at point-blank (`slime-pad.webp`).
- **PASS:** Bat pad kill — ~2 taps (`bat-pad.webp`). Bat i-frames UNTESTED (`bat-iframes.webp` captured but not scored).
- **STILL:** START OVER under Jobs (not pressed). Clock 2239 Night → 2240 Evening across pass.
- Screenshots `/workspace/playtest-1328/`.

## Live playtest 9/4 ~10:11–10:29am PT (BUILD 20260904b)

- Continued box Chrome save — never START OVER. Day 2217 SPRING MORNING (MINE 1, 2/5 hearts, 3G) → KO → HOUSE → FARM → MINE 1 Afternoon (5/5♥, 7G). URL `?v=20260904b`; Jobs stamp `20260904b` (`jobs-20260904b.webp`). First live of 04b. Jobs text: KICK THE CART IN TOWN.
- **STILL FAIL (04b claim miss):** Sword not in 10-tray hotbar — slot 0 seeds; tray = seeds/crate/berry/wood/stone/ore/… (`tray-check.webp`, `end-mine-tray.webp`). Sword **still** in BAG grid slot 1 (`bag-check.webp`). forceSwordIntoTray pin + showOwnedGoodsInBag no-mirror did not land on this save after mine enter / bag open.
- **PASS:** Bat pad kill — ~2 taps + loot (`bat-pad-kill-loot.webp`). Bat i-frames UNTESTED this pass.
- **WORSE vs 04a:** Slime contact i-frames — direct hold led to KO (`slime-contact.webp`); pad-vs-slime UNTESTED. On 04a slime i-frames + 1-tap pad had PASS.
- **Death:** auto-woke in HOUSE at 5/5♥ (copy text not shown on screen; `ko-wake-house.webp`). Gold 3→7 across pass (loot).
- **STILL:** START OVER under Jobs (not pressed). Clock phase advanced Morning→Afternoon/Night across pass.
- Screenshots `/workspace/playtest-1011/`.

## Live playtest 9/4 ~1:16–1:34am PT (BUILD 20260904a)

- Continued box Chrome save — never START OVER. Day 2150 SPRING NIGHT (MINE 1, 2/5 hearts, 0G) → Day 2151 SPRING EVENING (MINE 2, ~1/5, 0G). URL showed `?v=20260903b` (assets/version.json still stale); Jobs stamp `20260904a` (`02-jobs.webp`). First live of 04a. Jobs text: KICK THE CART IN TOWN.
- **STILL FAIL (04a claim miss):** Sword not in 10-tray hotbar — slot 0 is seeds; tray = seeds/crate/berry/wood/stone/ore/mushroom/moon/… (`03-tray.webp`). Sword **still** in BAG grid slot 1 only (`04-bag.webp`). forceSwordIntoTray pin-slot-0 did not land on this save after mine enter / bag open.
- **PASS/STILL (combat from 03b):** Slime contact i-frames — hold ≥4s adjacent with no multi-drain (`05-slime-contact.webp`). Slime pad kill — 1 tap; orange ore loot (`06-slime-pad.webp`). Bat i-frames — one bump 2→1♥ then held ≥4s (`07-bat-contact.webp`). Bat pad kill — 1 tap (`08-bat-pad.webp`).
- **STILL:** Clock races (2150 Night → 2151 Morning/Evening across pass); START OVER under Jobs (not pressed).
- **NEW nit:** Live `assets/version.json` still `{ "v": "20260903b" }` while index BUILD / Jobs stamp is `20260904a` (URL cache param stayed on 03b).
- **No NEW/WORSE combat.** Death copy UNTESTED this pass (no KO).
- Screenshots `/workspace/playtest-0116/`.

## Live playtest 9/3 ~7:16–7:38pm PT (BUILD 20260903b)

- Continued box Chrome save — never START OVER. Day 2127 SPRING MORNING (PEAK, 1/5 hearts, 0G) → Day 2129 SPRING MORNING (MINE 1, 4/5, 0G). Cache-bust `?v=pt1913`. Jobs stamp `20260903b` (`02-jobs.webp`). First live of 03b. Jobs text: KICK THE CART IN TOWN.
- **FIXED (was NEW/WORSE 7:26am 03a):** Slime contact i-frames — one bump 5→4♥, then held ≥3.5s standing adjacent (`11-slime-contact.webp`, `12-slime-iframe-wait.webp`).
- **FIXED (was NEW/WORSE 7:26am 03a):** Slime pad kill — 1 sword-pad tap cleared a slime (`06-slime-pad.webp` path).
- **FIXED (was NEW 7:26am 03a):** Death copy — faint shows `ZZZ...` / `THE MOUNTAIN SENT YOU HOME.` (`05-death.webp`), not `YOU DIED...`.
- **FIXED (was STILL missing):** Sword appears in BAG grid slot 1 after mine enter (`10-bag.webp`). **STILL:** not in the 10-tray hotbar (tray still seeds/crate/…) — forceSwordIntoTray partial.
- **PASS:** Bat i-frames (5→4 then hold ≥4s) + pad kill (~2 taps) (`07`–`09`).
- **PASS this pass:** No slime under sword pad / hotbar gutter (open-floor spawn only).
- **STILL:** Clock races (2127→2129 across pass); START OVER under Jobs (not pressed).
- **No NEW/WORSE.**
- Screenshots `/workspace/playtest-1913/`.

## Live playtest 9/3 ~7:26–7:45am PT (BUILD 20260903a)

- Continued box Chrome save — never START OVER. Day 2037 SPRING NIGHT (MINE 1, 3/5 hearts, 0G) → Day 2039 SPRING MORNING (MINE 1, 1/5, 0G). Cache-bust `?v=pt0725`. Jobs stamp `20260903a` — same build as 4:13am / 1:13am (no new ship since). Jobs text: KICK THE CART IN TOWN.
- **STILL FIXED (bats):** Single bat contact = −1♥ (3→2) and hearts HELD ≥4s standing adjacent (`04-bat-contact-minus1.webp`, `05-iframes-hold.webp`). Pad killed a bat on the 2nd landed tap.
- **FIXED/confirmed (loot, was "cannot rule out nearby rock" at 4:13am):** Killed bat dropped a copper-ore chunk on its tile; walking over it filled the EMPTY tray slot 6 with ore ×2 (`06-bat-dead-loot.webp`, `07-ore-pickup-slot6.webp`).
- **NEW / WORSE (slimes skip the 03a combat fixes):** Green slime contact drains repeatedly with NO i-frames — 5♥ → 4♥ on first touch, then 2♥ within ~4s standing adjacent, then 1♥ (`11-slime-2hearts-no-iframes.webp`, `12-slime-1heart-pad-no-kill.webp`). Earlier pass: at 2♥ a single step next to a slime was instant death with no visible incremental loss. Bats got i-frames in 03a; slimes appear not to route through the same hurtPlayer path.
- **NEW / WORSE:** Sword pad does NOT kill a slime — 2 taps adjacent, slime survived, no loot, no hotbar change (bats die in ~2 taps). Slime HP or pad-vs-slime hit test looks off.
- **NEW (kid-unfair):** A slime can sit at the bottom-left BEHIND the sword pad / hotbar strip — sprite is half-hidden and that tile is not clickable (`08-slime-under-hotbar-down-hole.webp`). Keep enemies out of the UI gutter.
- **NEW (kid tone):** Death box now reads `ZZZ...` / `YOU DIED...` (`09-you-died.webp`), not the gentler `THE MOUNTAIN SENT YOU HOME` seen 9/3 1:13am. For a 7-year-old the wake-at-home phrasing was better copy.
- **PASS:** After KO you wake in the house at 5/5♥, gold unchanged 0G, inventory kept, and the DAY does NOT burn (still 2038; phase reset EVENING→MORNING) (`10-wake-house-day2038.webp`).
- **STILL:** Sword absent from tray and BAG — pad-only (`03-bag-no-sword.webp`). Clock races (MORNING→AFTERNOON in ~10s–1 min; 2037→2039 across the pass). START OVER still under Jobs (not pressed).
- **NEW (friction):** Pad knockback throws a bat several tiles and it then drifts/flees, so landing two taps in a row means chasing it — fiddly for a kid.
- **UNTESTED this pass:** MINE 2+ (never descended — KO'd or low hearts both tries); PEAK cave→STAIRS→MINE 6 chain; planting / NPC talk / farm loop.
- Screenshots `/workspace/playtest-0725/`.

## Live playtest 9/3 ~4:13–4:26am PT (BUILD 20260903a)

- Continued box Chrome save — never START OVER. Day 2014 SPRING MORNING (FARM, 5/5 hearts, 0G) → NIGHT (~13 min). Cache-bust `?v=pt0413`. Jobs stamp `20260903a` (`02-jobs-build-20260903a.webp`). Same build as 1:13am. Jobs text: KICK THE CART IN TOWN. Farm → north → MINE sign → MINE 1 (`03-farm-mine-sign.webp`, `04-mine1-swordpad.webp`).
- **FIXED (was UNTESTED at 1:13am):** Bat i-frames — brush at 5♥ took exactly −1 (5→4) and held ≥2.5s with invincibility flash; later spaced hit 4→3 (`05-bat-brush-iframes.webp`, `06-bat-adjacent-5hearts.webp`). No multi-heart drain.
- **FIXED (was UNTESTED at 1:13am):** Pad kill — fat-finger sword pad killed 2 bats (~2 taps each; first tap often knockback only) (`07-pad-hit.webp`, `09-pad-kill-bat2.webp`). Loot partly confirmed: after one kill stone went 2→4 on step-on pickup (`10-stone-after-kill.webp`); cannot 100% rule out nearby rock.
- **WORSE:** none.
- **STILL:** Sword not in tray/hotbar/BAG (`08-bag-no-sword.webp`). No overland sword pad. Clock races MORNING→AFTERNOON→EVENING→NIGHT in ~4–5 real min (~1 min/phase). START OVER under Jobs (not pressed). Sword-on-stand prop in MINE 1 does nothing on Space.
- **UNTESTED this pass:** PEAK cave→STAIRS→MINE 6 chain; slimes; deeper floors; KO/wake; planting/NPC.
- Screenshots `/workspace/playtest-0413/`.

## Live playtest 9/3 ~1:13–1:22am PT (BUILD 20260903a)

- Continued box Chrome save — never START OVER. Day 1992 SPRING MORNING (PEAK, 1/5 hearts, 0G) → AFTERNOON (~14 min). Cache-bust `?v=pt0113`. Jobs stamp `20260903a` (`02-jobs.webp`). First live of 03a. Jobs text: KICK THE CART IN TOWN.
- **FIXED:** Not woods-stranded — PEAK cave mouth one-tap → STAIRS 2 → DOWN STAIRS 1 → MINE → MINE 6 (`04-stairs2.webp`, `05-mine6-swordpad.webp`). After KO: HOUSE → bottom door → FARM (house, NPC, chicken, mailboxes, tilled dirt) (`06-ko-sent-home.webp`, `07-farm.webp`).
- **NEW:** Mine sword strike pad — fat-finger round pad with sword icon, bottom-left above hotbar on MINE 6; tap swings in place (no walk) (`05-mine6-swordpad.webp`).
- **STILL:** Sword not in tray/hotbar/BAG (`03-bag.webp`: seeds, box, gem, wood×2, stone×2, flowers, mushrooms, moon crescent; no sword). No overland/farm/peak sword pad.
- **STILL (combat claims open):** Bat contact at 1♥ = instant KO → THE MOUNTAIN SENT YOU HOME (5/5♥, same day, no gold loss seen) (`06-ko-sent-home.webp`). Multi-heart drain / i-frames UNTESTED (spawned low).
- **UNTESTED:** Pad kill/loot — pad tapped but never adjacent to bat/slime before KO.
- **STILL:** Clock races MORNING→AFTERNOON ~1 real min (twice); START OVER under Jobs (not pressed).
- Next pass: start full hearts on farm → mine so bat i-frames + pad kill/loot can score the 03a hotfix.
- Screenshots `/workspace/playtest-0113/`.

## Live playtest 9/2 ~10:15–10:22pm PT (BUILD 20260831u)

- Continued box Chrome save — never START OVER. Day 1684 SPRING EVENING (woods/grass overland, 5/5 hearts, 17G) → 1685 MORNING (WOODS sign, 5/5, 17G). Cache-bust `?v=pt2215`. Jobs stamp `20260831u` (`02-jobs.webp`). Same build as 7:27pm / 4:09pm.
- **No NEW/WORSE vs 7:27pm baseline** (combat untested — no mine access).
- **STILL:** No farm MINE entrance — ~10 min walk (S/W/N/E to map edges) found WOODS sign, lamps, pond, mailboxes, rocks only; no hole / MINE sign / house (`03-woods-sign-no-mine.webp`, `99-end.webp`).
- **STILL:** sword not in tray/BAG (`10-bag.webp`); no overland sword pad rendered.
- **STILL:** clock races EVENING→NIGHT ~1 min → Day 1685 MORNING within ~3 min; START OVER under Jobs (not pressed).
- **UNTESTED this pass:** bat contact; pad kill/loot; MINE 1 OUT; pad-over-OUT; PEAK path.
- Note (quiet): south edge camera clamps and Orion walks behind hotbar (sprite gone) (`03b-player-hidden-under-hotbar.webp`); dirt-path signpost hard-blocks the tile (Space: no text).
- Screenshots `/workspace/playtest-1015pt/`.

## Live playtest 9/2 ~7:27–7:36pm PT (BUILD 20260831u)

- Continued box Chrome save — never START OVER. Day 1664 SPRING MORNING (STAIRS 2, 5/5 hearts, 18G) → EVENING (farm-north/woods edge, 5/5 post-KO, 17G). Cache-bust `?v=pt1927`. Jobs stamp `20260831u` (`02-jobs.webp`). Same build as 4:09pm pass.
- **WORSE:** Bat contact — one brush −1♥ then remaining 4♥ drained in ~2s → KO; woke house Day 1664 MORNING 5/5, gold 18→17 (`06-bat-KO-wake.webp`). Faster than 4:09pm multi-drain.
- **NEW:** Farm NPC on north dirt path fully blocks the tile — walk north stalls until sidestep left (`11-farm-north-blocked.webp`).
- **NEW:** After KO, no farm MINE entrance findable — north path → WOODS → canopy/signpost dead-end; MINE sign never appeared (`13-end-farm-north.webp`).
- **STILL FAIL:** Sword pad on MINE 6 bat — knockback/displace, no kill/loot, gold unchanged 18G (`04-pad.webp`, `05-pad-result.webp`).
- **STILL:** sword pad-only (chest/tray no sword, `12-chest-no-sword.webp`); clock races MORNING→AFTERNOON→EVENING ~3 min (day stayed 1664); START OVER under Jobs (not pressed).
- **UNTESTED this pass:** MINE 1 OUT one-tap; pad-over-OUT; PEAK dirt/rocks/cave (spawned STAIRS 2, went down, then KO to farm).
- **PASS:** STAIRS 2 → STAIRS 1 → MINE 6 via step-on DOWN/MINE tiles (`03-mine6.webp`).
- Screenshots `/workspace/playtest-1927/`.

## Live playtest 9/2 ~4:09–4:26pm PT (BUILD 20260831u)

- Continued box Chrome save — never START OVER. Day 1640 SPRING AFTERNOON (MINE 1, 5/5 hearts, 17G) → 1641 MORNING (STAIRS 2, 5/5, 18G). Cache-bust `?v=pt1609`. Jobs stamp `20260831u` (`02-jobs.webp`). First live of 31u.
- **FIXED (31u):** PEAK winding painted dirt path walkable — walked multiple switchback segments (`09-peak-path.webp`). Old left-cliff-hug mask gone.
- **PASS:** Summit rocks still blocked — `FALLEN ROCKS.` / `THE PATH IS BLOCKED.` (`10-peak-rocks.webp`).
- **PASS:** PEAK cave arch enters STAIRS 2 (`11-peak-cave.webp`).
- **STILL FAIL:** Sword pad knockback only — no kill/loot this pass (`04-pad-swing.webp`, `05-pad-result.webp`).
- **STILL:** Bat contact multi-drains to KO / house wake (`06-bat-contact.webp`, `06-bat-ko.webp`).
- **STILL PASS:** MINE 1 OUT one-tap (`07-out.webp`); pad-over-OUT swing without exit (`08-pad-over-out.webp`).
- **STILL:** sword pad-only (no tray sword, `12-bag.webp`); clock races (1640 Afternoon→Evening→…→1641 Morning); START OVER under Jobs.
- Screenshots `/workspace/playtest-1609/`.

## Live playtest 9/2 ~10:26–11:22am PT (BUILD 20260831t)

- Continued box Chrome save — never START OVER. Day 1599 SPRING MORNING (HOUSE, 2/5 hearts, 17G) → 1605 AFTERNOON (FARM, 5/5, 16G). Cache-bust `?v=pt1017b`. Jobs stamp `20260831t` (`02-jobs.webp`). First live of 31t.
- **FIXED:** Pad-over-OUT — standing on OUT, sword-pad tap swung (no mine exit) (`06-pad-over-out.webp`).
- **FIXED/confirm:** MINE 1 OUT one-tap exits to farm at MINE sign (`07-out-pass.webp`).
- **WORSE:** Bat contact multi-drain to KO again (8am FIXED/−1♥ survival gone); woke house full hearts, gold 17→16 (`03-bat-contact.webp`, `04-ko-respawn.webp`).
- **STILL FAIL:** Sword pad 2 taps = knockback only, no kill/loot (31t always-4-dmg claim miss this pass).
- **STILL:** sword pad-only (no tray sword); clock races (1599→1605); START OVER under Jobs.
- Slime kill UNTESTED (pad miss). Screenshots `/workspace/playtest-1017/`.

## Live playtest 9/2 ~7:38–8:02am PT (BUILD 20260831s)

- Continued box Chrome save — never START OVER. Day 1582 SPRING MORNING → EVENING (~11 min). Farmhouse → farm → woods/overland → town (PIP, MARKET DAY) → MINE 1 → OUT farm at MINE sign (ended 2/5 hearts, 15G). Jobs stamp `20260831s`.
- **FIXED:** Bat instant-KO (4:30am WORSE) — brief overlap −1 heart + knockback; multiple encounters survived (`04-bat-swing-knockback-4hearts.webp`).
- **FIXED/confirm:** MINE 1 OUT one-tap exits to farm (`06-out-ladder-one-tap-exit.webp`).
- **WORSE/NEW:** Sword pad knockbacks only — no kill, no loot this pass; cannot clear MINE 1 bats/slime.
- **NEW:** Pad bottom-left hitbox overlaps OUT label — first pad tap teleported out of mine instead of swinging.
- **STILL:** sword pad-only (no tray sword); clock races (MORNING→AFTERNOON→EVENING ~4 real min); START OVER under Jobs.
- **STILL harsh:** ~3s bat clip drained 4→2 hearts with no clear i-frame flash (`05-bat-contact-drain-2hearts.webp`).
- Slime contact UNTESTED. Tap-to-walk PASS. Screenshots `/workspace/playtest-0738/`.

## Live playtest 9/2 ~4:22–4:30am PT (BUILD 20260831s)

- Continued box Chrome save — never START OVER. Day 1556 SPRING MORNING → 1557 MORNING (~8.5 min). Farmhouse → farm → MINE 1 → faint home (5 hearts, 16G→15G). Cache-bust `?v=pt0409`. Jobs stamp `20260831s`.
- **WORSE:** Bat contact lethal — 5→3→1→KO in ~10s, red flash, no usable i-frames (`08`–`10` in `/workspace/playtest-0409/`).
- **STILL:** sword pad-only (no tray sword); clock races (~2–2.5 min/phase); START OVER under Jobs.
- **UNTESTED:** pad omni kill, slime contact, mine OUT one-tap (bat KO first). Possible NEW: no slime/grub on MINE 1 east (`07-mine1-no-monsters.webp`).
- Tap-to-walk PASS. Screenshots `/workspace/playtest-0409/`.

| Pri | Status | Issue | Where | Notes |
| --- | --- | --- | --- | --- |
| Critical | Done 8/30 11:20pm live | Live game black screen (SyntaxError) | Boot | STILL FIXED 8/31 2:19am live BUILD 20260831a: world + HUD visible, Jobs `20260831a` (`02_jobs_20260831a.webp`). FIXED 8/30 11:20pm live BUILD 20260830u: continued box Chrome save (WOODS, Day 1372 Morning, 5 hearts, stars populated). Jobs stamp `20260830u`. Canvas world visible — not black. First load of `?v=20260830u` still served stale 30t (green/empty canvas); second cache-bust `?v=20260830u&r=2` booted. Ocean enter/boat UNTESTED (woods spawn). Household save intact, never START OVER. Screenshots `/workspace/playtest-2315/01-land.png`, `02-jobs.png`. Was NEW/WORSE 8/30 11:05pm live BUILD 20260830t: canvas solid black; missing `}` on ocean `tryTalkAdjacent`. |
| Critical | Done 8/29 11pm live | Orion stuck in unwalkable tile (save bricked) | Overworld rim | FIXED 8/29 11:30pm live BUILD 20260829m: continued save Day 939→950; loaded in farmhouse (not 63,39); arrows/WASD/tap-to-move all walk farm/mine (`01-land.png`, `02-move.png`, `10-mine-out-onetap.png`). Unstick ship 8:20pm. Was NEW 8/29 8:15pm live BUILD 20260829l: continued save Day 869→872; spawn at (63,39) with that tile + N/E/S/W all `#` unwalkable; `walkable` false; `findPath` empty; arrows/WASD/tap no-op; reload persists. First live after rim Imagine scenery ships (29h–29l). Likely previously-walkable rim tiles now solid under stored position. Blocks all other checks this pass. Fix: on load, if `!walkable(player.tx,player.ty)` BFS-nudge to nearest walkable (porch/farm path). Screenshots `/workspace/playtest-2004/05-stuck-unwalkable.png`, `06-after-reload-still-stuck.png`. |
| Critical | Done 8/31 10:20pm live | Peak has no way down; save stranded | PEAK | FIXED 8/31 10:20pm live BUILD 20260831m: PEAK click-to-walk onto the painted cave arch loaded STAIRS 2; DOWN → STAIRS 1 → MINE 6 moon altar (`04-after-cave-stairs2.webp`, `06-mine-moon-altar.webp`). 5:20pm 31j walk-through gone. Local 8/31 BUILD 20260831k: peak cave arch retargeted to the painted mouth so outdoor PEAK enters STAIRS 2 (31j walk-through). WORSE 8/31 5:20pm live BUILD 20260831j: spawned PEAK Day 1572; Space/Down/Up on cave arch + standing on the dark tile = walk-through, no STAIRS 2 (`03-peak-cave-night.png`, `05-peak-night-stuck.png`). FARM sign still ABSENT. Farm/ocean/mine unreachable. Regression vs 2:46pm 31d FIXED return. FIXED 8/31 2:46pm live BUILD 20260831d: farm→MINE 1–6→STAIRS→outdoor PEAK→cave→STAIRS 2→1→MINE 6 altar (no loop). FARM sign ABSENT (31d by design). Overlay outdoor OK. Screenshots `/workspace/playtest-1412/27-peak-outdoor.png`, `28-peak-south-nofarmsign.png`, `31-back-at-mine6-altar.png`. Was Local 8/31 BUILD 20260831b: south balcony FARM exit (woodsSign @16,29 → overworld by NE mine); STAIRS 1 DOWN labeled MINE; enterMineFromClimb lands 22,7 with unstick. Do not mark Done until live. NEW 8/31 8:45am live BUILD 20260831a: continued save spawned at peak mine mouth (Day 1511 Evening). Switchback trail walkable north to ridge (`50_peak_north_ridge.png`) and back south, but south edge is a flat blue sky/void with no OVERLAND/FARM exit (`51_peak_south_bound_blue_band.png`, `54_peak_softlock_final_night_day1527.png`). Peak cave arch → STAIRS 2 → DOWN STAIRS 1; top portal one-tap returns to peak. No MINE 6 / farm continuation found in ~25 min. Farm/ocean/town unreachable. Need a south overland exit, STAIRS 1 → MINE 6, or a load-unstick. Screenshots `/workspace/playtest-0819/`. Prior 8/30 8:40pm climb PASS was farm→mine 6→peak (return not re-walked that pass). |
| Critical | Done 8/31 2:46pm live | Tap-to-walk dead (reticle, no move) | Peak / mine | STILL FIXED 8/31 10:20pm live BUILD 20260831m: PEAK dirt-path taps walked south into the cave (`03-cave-arch.webp`). STILL FIXED 8/31 5:20pm live BUILD 20260831j: PEAK path taps walked (`01-land.png`). FIXED 8/31 2:46pm live BUILD 20260831d: two grass taps walked Orion to the tile; arrows OK; still walked on PEAK and STAIRS (`15-tapwalk.png`). Local 8/31 BUILD 20260831b: goWalk snaps to nearestWalkable; findPath falls back to walkable tile nearest the tap. NEW/WORSE 8/31 8:45am live BUILD 20260831a: ground taps draw yellow target reticle; Orion never steps. Same on outdoor PEAK and inside STAIRS 2 (`52_mine_stairs2_tapwalk_no_move.png`). Arrows/WASD walk fine. No shovel in tray (not the 31a farm-shovel steal). Reopens Done 8/21 tap-to-move. Kid-first control is keyboard-only. |
| Critical | Done 8/31 2:46pm live | Tap-to-move often no-ops | Overworld | FIXED 8/31 2:46pm live BUILD 20260831d: tap-to-walk on overworld grass + mine + peak + stairs. Local 8/31 BUILD 20260831b: same tap pathing fix as Peak/mine row. **REOPEN/WORSE** 8/31 8:45am live BUILD 20260831a: tap-to-walk dead everywhere tested (peak + mine) — yellow reticle, no step; arrows still walk. See new Critical tap-to-walk row. 8/21 am: walks to reachable tiles. Residual: long tap to a blocked tile silently does nothing. Far-target / first-step-blocked no-ops are the Low row. |
| Critical | Partial | Tree canopy hides Orion / standing on the tree | Forest N/W + farm | Local 9/5 BUILD 20260905bw: head/shoulders peek when dense canopy would fully hide Orion while north-of-trunk Y-sort stays; no global +64. Needs live. UPDATE 8/30 5:30am live BUILD 20260830a (woods): Orion partly hidden under canopy again (`13-woods-canopy-hide.png`) — Y-sort hide Partial still. Prior 2:03am: drew in front (no hide) — not enough to mark Done. STILL 8/29 2pm live BUILD 20260829d (woods): under Imagine treetops Orion fully invisible except hair pixels (`09-orion-hidden-under-canopy.png`). STILL 8/25 8am live (farm): north of a trunk, only his head shows above leaves (Y-sort). REOPEN 8/25 5am live (farm): farm canopy hides player again (Y-sort) — likely the 2am north-row vanish (see High vanish). Forest north: Orion visible, clamp holds. Was Done 8/24 11pm live: forest canopy + Orion visible (not standing on the tree). Local 8/24 BUILD 20260824c: removed the +64 player sort hack that drew Orion on top of every canopy (looked like standing on the tree when north of the trunk). Foot-Y sort again: south of trunk = in front, north = behind leaves. Do not re-add the +64. 8/23 5pm live had marked hide-completely Done via that hack. |
| Critical | Local 9/5 05bz | Sword: Space+hotbar kills; on-screen button and facing still miss | Mine / HUD | Local 9/5 BUILD 20260905bz: pad omni 8-neighbor + bat post-hop reach + press damage + clearer crescent + remash; 31t OUT prefer kept; tray pin kept. Needs live (Space+hotbar already PASS 04e). Was LIVE 9/4 ~7:14–7:34pm BUILD 20260904e first live: tray pin **STILL FIXED**; Space+hotbar swing **PASS** (`34-space-hotbar-swing.png` in `/workspace/playtest-1914/`); bat i-frames PASS; slime contact STILL PASS; bat/slime pad kills UNTESTED (swings fired). Was LIVE 9/4 ~4:21–4:57pm BUILD 20260904c first live: tray pin **FIXED** (slot 0 + BAG — `tray-check.webp`/`bag-check.webp` in `/workspace/playtest-1621/`). Slime contact STILL PASS; slime pad STILL PASS (~2–3 taps). Bat pad UNTESTED. Space+hotbar STILL UNTESTED. Was Local 9/4 BUILD 20260904c: ensureCaveSword auto-grants on mine enter/swing/openBag (removes pedestal) + pins tray slot 0 — needs live. LIVE 9/4 ~1:28–1:36pm BUILD 20260904b recheck: tray pin **STILL FAIL** (BAG slot 1 only — `tray-check.webp`/`bag-check.webp` in `/workspace/playtest-1328/`). Slime contact i-frames **FIXED** (hold ~4s). Slime pad **PASS** (1 tap). Bat pad STILL PASS. Was LIVE 9/4 ~10:11–10:29am BUILD 20260904b: first live — tray pin **STILL FAIL** (slot 0 seeds; BAG slot 1 sword mirror STILL — `tray-check.webp`/`bag-check.webp` in `/workspace/playtest-1011/`). Slime contact **WORSE** (hold→KO). Bat pad PASS. Was LIVE 9/4 ~1:16–1:34am BUILD 20260904a: first live — tray pin **STILL FAIL** (BAG slot 1 yes; hotbar slot 0 seeds — `03-tray.webp`/`04-bag.webp` in `/workspace/playtest-0116/`). Slime/bat pad + i-frames STILL PASS. Local 9/4 BUILD 20260904a: forceSwordIntoTray clears dups/aliases and pins sword in hotbar slot 0; bag alias pickup no longer orphans tray tools — live miss. LIVE 9/3 ~7:16–7:38pm BUILD 20260903b: slime pad kill **FIXED** (1 tap); bat pad kill STILL PASS; sword **FIXED in BAG** grid slot 1 but **STILL** not in 10-tray (`10-bag.webp` in `/workspace/playtest-1913/`). Was LIVE 9/3 ~4:13–4:26am BUILD 20260903a: **FIXED** pad kill on MINE 1 — bats die in ~2 pad taps; stone drop after one kill (`07`/`09`/`10` in `/workspace/playtest-0413/`). **FIXED** bat i-frames (−1♥ then hold). Sword **STILL** pad-only (not in tray/BAG). Space+hotbar UNTESTED. Was LIVE 9/2 ~7:27–7:36pm BUILD 20260831u: **STILL FAIL** pad kill on MINE 6 — knockback/displace, no loot (`04`–`05` in `/workspace/playtest-1927/`). Sword **STILL** pad-only (`12-chest-no-sword.webp`). MINE 1 OUT / pad-over-OUT UNTESTED (no farm MINE entrance after KO). Was LIVE 9/2 ~4:09–4:26pm BUILD 20260831u: **STILL FAIL** pad kill — knockback only, no loot; sword **STILL** pad-only (`04`–`05`, `12` in `/workspace/playtest-1609/`). Pad-over-OUT **STILL PASS**. Was LIVE 9/2 ~10:26–11:22am BUILD 20260831t: **FIXED** pad-over-OUT (pad swing at OUT, no exit — `06` in `/workspace/playtest-1017/`). **STILL FAIL** pad kill — 2 taps knockback only, no loot (always-4-dmg claim miss). Sword **STILL** pad-only. Was Local 9/2 BUILD 20260831t: pad/mine arc always 4 dmg; pad wins over OUT; i-frames 1200. Was LIVE 9/2 ~7:38–8:02am BUILD 20260831s: pad swings **knock back only** — bats bounce, **no kill/no loot** this pass (`04` in `/workspace/playtest-0738/`); omni/auto-target pad PASS (up + diagonal). **NEW:** pad bottom-left edge overlaps OUT label and can exit the mine instead of swinging. Sword **STILL** not in 10-tray (pad-only). Was LIVE 9/2 ~4:22–4:30am BUILD 20260831s: sword **STILL** not in 10-tray (pad-only; tray seeds/crate/berry/wood/ore/flower/mushroom/moon); pad omni kill UNTESTED (bat KO before lined-up kill; no crescent captured). Was LIVE 9/2 ~1:06–2:34am: **FIXED** omnidirectional pad — slime down-left flashed white on tap #1, gone by #2 (`21`–`25` in `/workspace/playtest-0106/`). Fat-finger crescent PASS (`22-pad-crescent-swing.png`). **STILL:** sword not in 10-tray (`swordEquipped:false`; showStrikeBtn true) — pad-only. Space+hotbar UNTESTED. Was Local 9/2 BUILD 20260831s: omnidirectional pad hits (8-neighbor + reach 52 + tile Chebyshev≤1 any facing); tray swap hardens when bag full. UPDATE 9/1 ~10:22pm live BUILD 20260831r: pad kill PASS with loot (bat dropped coin 2G→4G; slime dropped ore). **NEW:** facing/direction-limited — slime to Orion's LEFT survived 5+ pad taps while foes above/below died in 1–2 (`07-slime-survives-left-swings.webp`, `05-bat-kill-coin.webp`). Crescent arc too brief for still. Sword still not in 10-tray (`04-bag-no-sword.webp`). Pad vs stairs/OUT PASS. Was UPDATE 9/1 ~7:40pm live BUILD 20260831r: fat-finger pad **FIXED** swing — bright crescent arc ~0.5s; pad taps did not steal stairs/holes on MINE 1 west column; adjacent snail **killed** (vanished, no hit flash/loot). Sword still **not** in 10-tray (tray full of non-tools; giveTool swap UNVERIFIED). Slime at range/diagonal ignored until adjacent+facing. Local 9/1 BUILD 20260831r claims still need tray-swap + Space+hotbar recheck. Was UPDATE 9/1 ~4:46pm 31q: pad drawn but no swing arc. |
| Critical | Done 8/22 | Farmhouse door / bed | House | 8/22 3pm: door and bed both work. Bed now dims the screen with a "YOU SLEEP..." banner, then Day+1 morning. Town houses knock-only. Shop is enterable. 8/23 11pm: house reached via mine-death respawn ("THE MOUNTAIN SENT YOU HOME"); door/bed not retested. 8/23 midnight: fade not captured, may have flashed. Jumped to DAY 8 MORNING, hearts restored. House not found 8pm. |
| Critical | Done 8/25 live | Northwest woods / forest not reachable | Forest N | FIXED 8/25 8am live reconfirm: forest loaded both approaches; FARM exit works. Landing-tile re-entry (one tile below WOODS, north tap instantly re-enters) is a new Medium row. FIXED 8/25 5am live: WOODS sign on the north–south dirt spur at the top of the west road. Walking onto/next to the sign from the east loads FOREST. Exit south FARM sign drops on the farm beside WOODS. Local 8/25 ~2:30am BUILD 20260825f: door was only farm (5,8) and arrive() ran only at path end, so a north walk at the WOODS sign (4,8) crossed into open meadow (y<8) with no scene swap. Walk-in is now the sign + last path tiles + one row north (4–6, 7–8); stepping on a forest door mid-path loads FOREST. Exit south landing moved to farm (5,11) in BUILD 20260825j (was 5,9). Logic-tested locally (key onto 5,8 / sign / past-sign; tap-through 5,8; south exit). WORSE 8/25 2am live (regression vs 11pm). Same path: south past houses → west dirt road → west spur → north → WOODS sign → last north tile. Last north tile is ordinary farm meadow, dead-ends at map edge. No scene transition. MINE sign visible to the east on the same strip. 1am ships (night readable, chest, forest clock, north clamp) UNVERIFIED because forest never loaded. Was Done 8/24 11pm live: this exact path loaded FOREST (canopy, Orion visible, ferns, berries, mushrooms, rabbit/deer/squirrel, Hazel, Rowan, glint pickup; south FARM sign back to farm at WOODS). Night readability, time stall, and north void were still Open then (FIXED 5am live); chest was not-found then (5am: found, won't open). |
| Critical | Local 9/5 05bq | Day clock races | Everywhere | Local 9/5 BUILD 20260905bq: clockMark harden (50ms step cap, one rollover/tick, pause/visibility/pageshow baseline reset, single-flight rAF, deferred phase persistSave); DAY_MS frozen 480000. Needs live — do not mark Done. STILL 9/2 ~4:09pm live BUILD 20260831u: Day 1640 Afternoon→1641 Morning across ~15 min mine/peak pass. STILL 9/1 ~10:22pm live BUILD 20260831r: Day 1258 AFTERNOON→1259 AFTERNOON in ~12 min (AFTERNOON→EVENING→NIGHT→MORNING→AFTERNOON; ~1 phase / 30–60s). STILL 9/1 ~7:40pm live BUILD 20260831r: Day 1244 AFTERNOON→1246 EVENING in ~3 min; single arrow steps often advanced phase. STILL 9/1 4:46pm live BUILD 20260831q: Day 1747 NIGHT→1748 MORNING across MINE 2→6 transition (~minutes). STILL 9/1 4:21am live BUILD 20260831o: Day 1254→1256 in ~10 min (Morning→Night). STILL 8/31 5:20pm live BUILD 20260831j: Day 1572 Afternoon→Night in ~10 min (~3 phases). STILL 8/31 2:46pm live BUILD 20260831d: Day 883 Afternoon→884 Night in ~15 min. STILL 8/31 8:45am live BUILD 20260831a: Day 1511 Evening→1527 Night in ~25 min; ~20–30 s/phase. STILL 8/31 5:50am live BUILD 20260831a: Day 1418 Morning→1421 in ~25 min; phase flips ~15–25 s real. STILL 8/31 2:19am live BUILD 20260831a: Evening→Night ~30s. Local 8/30 BUILD 20260830k: DAY_MS 150000 to 480000 (~8 real min/day). PHASE_MS still DAY_MS/4. Do not mark Done until live. STILL 8/30 2:10pm live BUILD 20260830f: Day 1297 Afternoon→1301 Morning in ~8 min (~4 in-game days). STILL 8/30 11:20am live BUILD 20260830c: Day 1226 Afternoon→1230 Afternoon in ~12 min. STILL 8/30 5:30am live BUILD 20260830a: Day 1089 Afternoon→1092 Afternoon in ~12–15 min. STILL 8/30 2:03am: Day 1010 Evening→1012 Afternoon in ~14 min; EVENING→NIGHT within ~90 s. STILL 8/29 11:30pm live BUILD 20260829m: Day 939 Night→950 Night in ~31 min. STILL 8/29 8:15pm live BUILD 20260829l: Day 869→872 in ~10 min; root cause `PHASE_MS=37500` (4 phases = 150 s/day ≈ 24 days/hour). STILL 8/29 2pm live: Day 1008 Afternoon→1010 Night in ~17 min (~1 phase / 30–60s). STILL 8/29 11am live: Day 937 Evening→953 Evening in ~15 min (~3 days). STILL 8/29 8am live: Day 865 Morning→867 Afternoon in ~12 min (~2 days). STILL 8/29 5am live: Day 1218 Afternoon→1226 Morning in ~35 min (~1 phase / 30–60s; ~3–4 real min/day). STILL 8/29 2am live: Day 1151 EVENING→1154 MORNING in ~11 min. STILL 8/28 11pm live: Day 1078 EVENING→1080 NIGHT in ~12 min (~1 phase / 30–60s). STILL 8/28 8pm live: Day 1002→1005 + multiple phase flips in ~10 min. STILL 8/28 5pm live: 1008 EVENING→1009 MORNING in a couple minutes. STILL 8/27 8pm live: Day 1→2 across one short farm/woods/mine pass (phases flip fast). STILL 8/25 8am live: clock still racing (~1 phase per few seconds). DAY 641→644 in ~10 min, including inside forest. STILL 8/25 5am live: clock still racing (~1 phase per few seconds). DAY 570→571 on refresh, ended ~575 in ~14 min. Forest-interior clock now RUNS (morning→night, 573→575 inside) — stall row Done. 8/25 2am live: farm / woods-edge clock running (DAY 499→503 in ~12 min, still racing ~3 min/day). Forest-interior clock UNVERIFIED that pass (forest never loaded). WORSE 8/24 11pm live: farm Morning→Night in ~15–20s; Day 428→430 with no sleep. Forest clock STALLS (own High row) — stayed NIGHT ~2 min, resumed Day 429 Morning on exit. STILL 8/24 5pm live: clock still fast — AFTERNOON→NIGHT→MORNING, DAY 290→291 with no sleep. STILL uneven. 8/24 11am live: started DAY 290 SPRING AFTERNOON underground; stayed AFTERNOON this ~13 min pass (not re-scored). 8/24 5am live: DAY 290 stayed 290; MORNING→AFTERNOON in ~1 min, then AFTERNOON held ~11 min. Morning phase still races; no full-day rollover this pass. Was 8/23 11pm: DAY 148 NIGHT → 151 AFTERNOON in ~24 min, ~5–6 min/day — better than 8pm's 3–4, still racing vs 5pm ~10–11. Was WORSE 8/23 8pm: DAY 76→79 in ~13 min, phase every ~30–60s, ~3–4 min/day. Was 8/23 5pm: ~2–3 min/phase, full day ≈10–11 min; DAY 8 MORNING → DAY 9 SPRING MORNING with no sleep. Was 8/23 midnight: full day in ~2 min; DAY 5→8. 8/22 3pm: ~30–60 s per phase; DAY 1→5 in ~15 min with one bed use. Rolls with no sleep. Death also burns a full day (see High; untested 5pm). |
| Critical | Done 8/21 | Camera loses Orion south of the hotbar | Farm | 8/22 3pm reconfirm: walking south keeps Orion ~80px above the hotbar. Void-band overscroll below the map edge is a new Medium row. |
| Critical | Done 8/22 | Camera loses Orion under the DAY/season header | Forest N | 8/25 5am live: forest north Orion visible below header (clamp holds). 8/25 2am: related vanish on the top-most walkable farm/woods-edge row (sprite fully invisible, not just under header) — see High vanish / Critical canopy. 8/24 11pm live reconfirm: Orion stays visible below the header in forest. 8/23 midnight reconfirm: north camera pad still holds (Orion below header). 8/22 3pm reconfirm: Orion stays fully visible below the DAY/season panel. Camera overscrolls past the world edge into a flat green/blue void band — new Medium row. |
| Critical | Done 8/24 live | Mine entrance not discoverable | Farm NE | FOUND 8/30 5:30am live BUILD 20260830a: OUT from MINE 1 landed at MINE sign + walk-in hole on the grass path NE/above the farm (`12-mine-entrance-out.png`); 2am miss cleared. Keep Done. MISS 8/30 2:03am: NE/town/east-cliff sweep (~4 min) found no hole (route/save-position). FOUND 8/29 11am live BUILD 20260829b: NE walk-in hole + MINE sign present; entered MINE 1 (8am miss was save-position). RECHECK 8/29 8am live: NE/E/north farm sweep found NO hole / MINE sign (save Day ~865–867 on box Chrome; may differ from 5am household). Keep Done until confirmed missing on known save — do not reopen on one miss. 8/24 11pm live: spawned at the NE MINE sign (save intact). Mine not retested this pass. 8/24 5pm live reconfirm Done: walk-in hole + MINE sign on the upper-right dirt path; west-of-house hole gone. MINE 1 south OUT drops on the farm beside the NE hole. Round-tripped mine→farm→mine→farm. Darren confirmed the upper-right hole is live (walk-in on NE dirt path). Was UNVERIFIED 8/24 11am live: save spawned already underground; never reached the surface, so the 10am NE/upper-right move (37d6312, BUILD 20260824a) was not seen. West-path vs NE not compared. Local 8/24: Darren asked the entrance back to the original upper-right. Walk-in hole + MINE sign now sit on the NE dirt path at the original portal tile (37,6); exit drops at (37,7). West-path hole at (13,24) removed. Still a one-tile walk-in (not the old painted mound at (36,5) that was hard to enter). Was live-found 8/23 11pm/5pm/midnight on the west dirt path north of the house. Was: 8/22 3pm 15-min sweep found no cave. |
| High | Done 8/25 live | Forest night nearly unreadable | Forest N | FIXED 8/25 8am live reconfirm: forest night pretty/readable (lamp glows). FIXED 8/25 5am live: forest night readable — green foliage + gold lamp pools, not flat navy. Farm night still sometimes flat navy (forest grade not applied to farm) — see Medium night-wash. UNVERIFIED 8/25 2am live: forest never loaded so 1am night-grade lift not seen. Woods-edge approach at night: flat navy silhouettes, lamp pools OK where lamps exist. Local 8/25 1am BUILD 20260825a: forest-only night grade lift (less blue hue/color crush), slightly lifted moss floor, moon rim on canopy/flora, warm gold lantern wells/pools in forest + 2 extra lamps. Evening keys unchanged; farm grass PNGs and Orion art untouched. Local screenshot: trunks/ferns still read green, lamp pools gold, header NIGHT. Not live-verified — keep Open. NEW 8/24 11pm live. At night, trees/ferns become flat dark-blue silhouettes — nearly unreadable. Farm night-tint inconsistency stays on the Medium night-wash row. |
| High | Done 8/25 live | Time stalls in the forest | Forest N | FIXED 8/25 8am live reconfirm: forest clock still running (and racing with farm — see Critical day-clock). FIXED 8/25 5am live: clock runs in the forest (morning→night, day 573→575 inside). Farm clock still races — see Critical day-clock. UNVERIFIED 8/25 2am live: forest never loaded. Farm / woods-edge clock is running (499→503) — see Critical day-clock row. Local 8/25 1am BUILD 20260825b: day clock now ticks in every scene (forest/mine/house/shop), paused only for UI overlays or a hidden tab. DAY_MS unchanged. Not live-verified — keep Open. NEW 8/24 11pm live. Stayed NIGHT ~2 min in forest while the farm clock cycles every few seconds (Morning→Night in ~15–20s). On exit, header resumed Day 429 Morning. Farm racing stays on the Critical day-clock row. |
| High | Local 9/5 05ba | Player sprite vanishes on the top-most walkable row | Farm / woods-edge | Local 9/5 BUILD 20260905ba: on overworld ty<=2, playerDrawFoot sorts Orion above nearby rim trees/canopies (tree feet ty*TILE+24 were covering same-row player tileFootY+14); drawOverRim moved after ground so north overhang stays under actors; CAM_PAD_TOP 26→32. Mid-map cozy Y-sort hide-behind-trees kept (no global +64). Needs live. Was Open: 8/25 5am live forest north OK; farm canopy Y-sort likely the 2am vanish — see Critical canopy Partial. Local 8/25 BUILD 20260825f north HUD-band camera. NEW 8/25 2am: Orion invisible on top-most walkable farm/woods-edge row; keys worked; found walking south. |
| High | Verify | Rocks one-shot; stone auto-bags | Farm / mine | 8/25 5am live: walk-break / rock smash not tested. 8/25 2am live: walk-break not tested. 8/24 11pm live: still no walk-break. Local 8/24 BUILD 20260824c: other agents had set farm rock HP to 1 and `addItem("stone")` on smash. Restored canon: farm 5 hits (pick 3 dmg / two hits), mine 4 / deep 6; stone `spawnGroundLoot` on the rock tile — walk onto it. See `GAMEPLAY.md`. Was mixed into Done 8/23 walk-break: 5pm tap-smash stone 1→2 immediately. | 8/24 5am live reconfirm: smash + STONE TAP star, stone +1. 8/23 8pm live reconfirm: pickaxe adjacent rock, smash works, stone 0→2. 8/23 midnight: walk-into and tap one-shot rocks, stone 0→1 then 1→2. Diagonal Space still no-ops (expected). Local 8/22 4:10pm: adjacent Space/walk-into/tap one-shots a rock, smash SFX, stone hotbar +1 immediately. Paving dirt with stone still in. Was: 8/22 3pm ignore input, stone 0. |
| High | Done 8/22 | Two Pips at once | Shop + town | 8/22 3pm reconfirm: only shop Pip. Town square has Lila (fountain) and Reed. Pip appears solely behind the shop counter. Shop not reached 5pm / 5am / 11pm. Shop/town not found 8pm. |
| High | Done 8/27 live | Shop has no buy/sell UI | Shop | FIXED 8/27 11am live BUILD 20260827b: talkPip opens shop (shopOpen, BUY/BYE, msg BRING ME ONE COPPER FOR A LANTERN). Copper job still talks first if you are handing copper. Pip still does not buy. Local 8/27 BUILD 20260827b: talking to Pip opens PIP'S SHOP (BUY/BYE). Copper turn-in still talks first, then tap Pip again for the shop. Pip still does not buy. Still. Shop not reached 8/24 5pm (farm reached via OUT; shop not visited). Shop not reached 8/24 11am (stuck underground). Shop not reached 5am / 11pm. Shop not found 8pm. Not retested 5pm 8/23 live. 8/23 midnight: Pip "bring me one copper", no buy/sell, 0G. 8/22 3pm: enterable, Pip talks ("bring me one copper for a shop lantern"), no buy/sell, 0G. |
| High | Local 8/26 | Enemies draw on top of the hearts HUD | Mine / HUD | Local 8/26 BUILD 20260826a: verified drawWorld already calls drawHUD after drawActors (monsters via collectCreatureActors) in both outdoor and mine branches — no draw-order change needed; ship skipped. Prior Open notes: 8/24 5pm / 11am / 5am / 8/23 11pm / midnight not specifically re-checked for enemy-over-hearts (HUD-overlap Low covers button/hotbar). Contact damage separate (slug-contact). |
| High | Local 9/5 05br | No overworld enemies / slugs missing | Overworld | Local 9/5 BUILD 20260905br: soft outdoor slugs on farm edges + woods (reuse slime art; 2hp, 1♥ bump, few, night tops farm to 3); sword-kill small loot; save-safe outdoor cache. **Needs live.** Was Open — 8/25 5am live: forest has Hazel/Rowan-like NPCs, rabbits, deer, mushrooms, stumps (wildlife, not combat). Still no overworld slugs. 8/24 11pm: forest has rabbit/deer/squirrel (wildlife, not combat). Still no overworld slugs. Mine/combat not retested. Surface reached 8/24 5pm (round-trip farm); overworld enemies not specifically noted. Mine still has bats + slimes + armored bugs that chase and hit hard. Surface not reached 8/24 11am (stuck underground). STILL 8/24 5am: zero overworld enemies. Mine has plenty (Mine 3 packed). Sword can Space-kill if hotbar selected (see Critical). Was 8/23 11pm: mine HAS plentiful enemies (brown slugs, purple bats, green slimes). Zero overworld enemies across 2 day/night cycles (DAY 148–151). Was NEW 8/23 8pm: two full nights outdoors, zero slugs; mine not reached so unclear if mine-only. |
| High | Done 8/28 live | Star + Nim note stack; popups inconsistent | Mine | FIXED 8/28 2am live BUILD 20260828a: NIM'S NOTE / JUNIE show OK + X; while note open toastQueued (caveHelper) with no covering toast; after OK, CAVE HELPER toast played. Space/Esc/tap dismiss still hold. Local 8/28 BUILD 20260828a: star toasts wait until notes/talk/shop close so they no longer cover NIM'S NOTE. Talk/note panels have OK + X; Esc/Space/tap still dismiss. 8/24 5pm: note-boards have text (NIM'S NOTE). Stars not re-scored. 8/24 11am: Stars X still works. Nim notes not re-checked. 8/24 5am: Esc + Stars scroll+X still hold; Nim notes not re-checked. 8/23 11pm: mine entered; Nim/star notes not re-checked. 8/23 8pm: Esc dismiss still works (Jobs/Stars). Mine/Nim not reached. 8/23 5pm live: Esc closed Jobs/Stars; Space closed Junie with no walk/swing (keys hold). 8/23 midnight: star popup with OK over Nim's note; OK dismissed star, note on next tap. Notes more consistent, still click-to-dismiss for the note. 8/22 midnight: cave-door “A STAR!” now has an OK button. “MOON PIECE / FOUND A SHARD” has none (dismiss only by clicking anywhere). Nim’s Note still has no OK and ignores Esc. Esc/Space now dismiss Stars/Jobs/dialogue/star toasts (8/23 3am localhost, live 5pm). Dialogue is click-to-dismiss; panels only via toolbar button. One dialog component with a mandatory OK/X and Esc binding. |
| High | Done 8/23 | In-mine ladder exits; no Mine 2 | Mine | 8/24 5pm live: OUT FOUND. Deep floor → UP west → MINE 1 → south OUT → farm beside the NE hole. Escapable. Space does not activate ladders. 8/24 11am: floors still exist (UP cycled at least 3); Mine 1 OUT / surface exit UNVERIFIED — couldn't find it (see High soft-lock). 8/24 5am live: MINE 1 → DOWN → MINE 2 → DOWN → MINE 3 all work; UP/OUT labeled. Mine 3 exists. 8/23 11pm live reconfirm: MINE 1, DOWN to MINE 2, OUT to farm — all work. 8/23 8pm: mine / Mine 2 not found. 8/23 5pm live reconfirm: glowing DOWN north-center MINE 1 → MINE 2; UP ladder returns; OUT south ladder exits to farm. Local 8/23 3am: MINE 1 already had a down-hole at (16,4) wired to existing Mine 2. A lamp sat in the center aisle so kids never walked to it. Lamp moved aside; hole glows and reads DOWN, south ladder reads OUT. Walking onto the hole loads MINE 2. |
| High | Local 9/5 05bx | Save resumes underground; OUT hard to find | Mine | Local 9/5 BUILD 20260905bx: clearer bobbing gold OUT/UP floating ladder signs (door-sign style) + once-per-session toast + Jobs `FOLLOW UP SIGNS TO OUT` + Space/E climbs facing/adjacent; needs live. Was UPDATE 8/24 5pm live: not a hard lock. OUT exists — deep floor → UP west → MINE 1 → south OUT → farm beside the NE hole. Surface path from the deep spawn is long / easy to get lost (~6 min, no map). Was NEW 8/24 11am live. Soft-lock for a kid: save restored already underground with no obvious way out. UP ladders cycled between cave floors (at least 3). One small floor had only DOWN, no UP. Space does not activate ladders — must step on the tile and press the same direction again. Mine 1 OUT / surface exit UNVERIFIED that pass (couldn't find it). 5am had labeled UP/OUT and reached surface. |
| High | Done 8/23 | “Say hi to Junie” stays after greetings | Farm | 8/24 5pm: surface reached via OUT; Junie not re-checked. 8/24 11am: surface/Junie not reached (stuck underground). 8/24 5am: Junie Space talk works (bring cave mushroom). Job-clear after mushroom still unverified. 8/23 11pm: Junie found just SW of the house (route landmark). Job text not re-checked. 8/23 8pm: Junie not found. 8/23 midnight: Jobs now "BRING A MUSHROOM TO JUNIE" after greeting. 8/22 3pm: Junie found on the farm near the house ("I'm Junie, can you find a cave mushroom for my garden?"). Plaza is Lila/Reed. |
| High | Partial 9/5 05by | Shop / town buildings | Town | LOCAL 9/5 BUILD 20260905by: tall cottage (townHouseA) + L-house (townHouseB) enterable cozy single rooms — door/stoop walk-in, furniture, OUT doormat; Pip shop + blue/red cottages still enterable; unique exteriors kept. Needs live. Was UPDATE 8/30 5:20pm live BUILD 20260830h: Pip shop door TAP ENTERS (`11-door-tap.png`, `12-shop-interior.png`). Unique paintings still look good. East roof tap walks (no BEEP). Truck BEEP UNTESTED. Was UPDATE 8/30 2:10pm live BUILD 20260830f: Pip shop walk-in ENTERS (`08-shop-interior.png`, `65-pip-shop-ui.png`). Unique paintings still look good. Door/truck taps still BEEP (see Pip door row). Tall cottage knock UNTESTED this pass (still knock-only 11:20am). Still 0G. Was UPDATE 8/30 11:20am live BUILD 20260830c: unique multi-tile Pip shop / tall cottage / L-house look good (`03-town-buildings.png`). Pip shop door FAIL (new High row). Tall cottage still knock-only. Still 0G. Was: Shop enterable. Other houses still knock-only. Still 0G. Shop/town not visited 8/24 5pm (farm reached via OUT). Shop/town not reached 8/24 11am (stuck underground). Shop/town not reached 5am / 11pm. Town/shop not found 8pm. Not retested 5pm 8/23 live. |
| High | Done 8/30 5pm live | Pip's shop door miss after unique painting | Town | FIXED 8/30 5:20pm live BUILD 20260830h: one tap on painted door from a couple tiles away entered PIP'S SHOP (Pip at counter, BUY/BYE, prices SEED TIN 5G … FISHING POLE 30G) — 2:10pm door-tap miss / CAR/BEEP gone (`11-door-tap.png`, `12-shop-interior.png`, `12b-shop-buylist.png`). Doormat one-tap exit. East-of-door roof tap walked (no enter, no BEEP) (`14-east-door-tap.png`). Truck BEEP UNTESTED. Local 8/30 BUILD 20260830h: one tap on painted door / stoop / front tiles calls enterShop immediately (no walk-to-shopIn empty-path no-op). carSpriteHit ignores door pixels so east/facade taps do not BEEP; truck body still BEEP. Not the whole facade. UPDATE 8/30 2:10pm live BUILD 20260830f / 30e: **walk onto south stoop/door ENTERS** PIP'S SHOP (Pip at counter, BUY/BYE, prices SEED TIN 5G … FISHING POLE 30G, copper lantern line) — 11:20am dead door gone (`08-shop-interior.png`, `65-pip-shop-ui.png`). Kid taps on (43,26)/(43,25) still no-op; east (44,26) still `CAR / BEEP` (`60-door-door-e.png`). Truck still steals some taps. Was NEW 8/30 11:20am live BUILD 20260830c: 5 taps on shop facade/door + Space while standing under it did nothing; two taps hit the parked truck (`CAR / BEEP`). No interior, no Pip, no BUY. 8:14am 30a shop WAS enterable with prices (`/workspace/playtest-0814/07-pip-shop.png`). Likely the door hitbox was not retargeted to the new larger painting. Screenshots `/workspace/playtest-1108/03-town-buildings.png`, `04-house-knock.png`.
| High | Local 9/5 BUILD 20260905bv | Nest bird 10-wood give + star + rides | TREE 1 / TREETOP | Local 9/5 BUILD **20260905bv**: cozy loop finished from WIP 05bs stash (favor main 05bt–05bu) — ≥10 wood talk takes wood + thank-you / BIRD STAR / ride menu (TREE/HOME/TOWN/CAVE/PEAK/STAY) with land notes; bird stays after dismiss; Jobs tips; TREE 1 3 eggs / no pickup kept. Prior 8/30 live: bird visible + 10-wood ask PASS; give/star/rides were UNTESTED. Needs live verify of give+ride.
| High | Done 8/31 10:20pm live | Snowy peak via mine 6 cave climb | Mine 6 / PEAK | FIXED return 8/31 10:20pm live BUILD 20260831m: PEAK → STAIRS 2 → STAIRS 1 → MINE 6 altar (5:20pm 31j walk-through gone). Climb-from-farm still UNTESTED this spawn. WORSE 8/31 5:20pm live BUILD 20260831j: outdoor PEAK still loads; cave-down FAIL again (walk-through, no STAIRS) — return to mine/farm blocked. Climb-from-farm UNTESTED this spawn. FIXED return 8/31 2:46pm live BUILD 20260831d: PEAK cave-down reaches MINE 6 altar (8:45am return FAIL gone). Climb still PASS. UPDATE 8/31 8:45am live BUILD 20260831a: outdoor PEAK still loads and mine stairs 1–2 still round-trip to peak, but **return to overworld FAIL** — save stranded (new Critical peak soft-lock). LIVE 8:40pm BUILD 20260830i: MINE 1–6 DOWN holes → north chamber PEAK+UP stairs east of moon altar (`56-mine6-peak-stairs.webp`) → STAIRS 1 (`57-caveclimb.webp`) → STAIRS 2 cave mouth → outdoor PEAK balcony (`58-peak.webp`). Winding dirt/stone path through snowy cliffs/pines; summit pile `FALLEN ROCKS.` / `THE PATH IS BLOCKED.` (`59-peak-rocks.webp`). Moon altar stayed on MINE 6. Bird PEAK ride UNTESTED (wood 2). Ended 1/5 hearts (mine contact). Screenshots `/workspace/playtest-2001/`.
| High | Done 8/21 | Mine regenerates on every re-entry | Mine | 8/21: same rocks/sign/ladder on re-enter. Enemies still wander, not chase. 8/24 5pm: round-tripped mine→farm→mine→farm; regen not systematically checked. 8/24 11am: already underground; regen/re-entry not checked. 8/24 5am: Mine 1 not packed at entry this time (2 enemies, roomy) vs 11pm packed — spawn/regen still not systematically checked. 8/23 11pm: mine entered (MINE 1 + 2); regen not re-checked. 8/23 midnight: mine entered; regen not re-checked. Mine not found 8pm. |
| High | Local 9/4 04l | START OVER sits in the Jobs book | Jobs | STILL 9/2 ~4:09pm live BUILD 20260831u: START OVER still in Jobs under stamp `20260831u` (`02-jobs.webp`; never pressed). STILL 9/1 ~10:22pm live BUILD 20260831r: START OVER still in Jobs under build stamp / RELOAD/MUTE (`02-jobs.webp`; never pressed). STILL 9/1 ~7:40pm live BUILD 20260831r: START OVER still in Jobs (Esc closes; never pressed). STILL 8/31 10:20pm live BUILD 20260831m: START OVER still in Jobs under RELOAD/MUTE + stamp `20260831m` (`02-jobs.webp`). STILL 8/31 5:20pm live BUILD 20260831j: START OVER still in Jobs under RELOAD/MUTE + stamp `20260831j` (`02-jobs.png`). UPDATE 8/31 2:46pm live BUILD 20260831d: START OVER still in Jobs, below RELOAD/MUTE + stamp `20260831d` (`14-jobs.png`) — 30k placement confirmed, still the wipe control. Local 8/30 BUILD 20260830k: smaller START OVER moved below RELOAD/MUTE and the BUILD stamp. wipeAsk REALLY START OVER? kept. STILL. 8/25 8am: Jobs / START OVER not opened. 8/25 5am: Jobs / START OVER not opened. 8/25 2am: Jobs not opened. 8/24 11pm: not retested. 8/24 5pm: not seen on HUD/Stars (Jobs maybe not opened this pass). Do not mark Done — 11am still saw it. 8/24 11am live: still the biggest Jobs button. 8/24 5am live: still the biggest Jobs button, above RELOAD/MUTE. 8/23 11pm live: still the biggest Jobs button, no X, Esc works. 8/23 8pm live: still the biggest button under job text, above RELOAD/MUTE. No X (Esc works). 8/23 5pm live: still the biggest top Jobs button. Esc now closes Jobs (see dialog-keys row); START OVER remains the dangerous control. 8/23 midnight: biggest top button; close only by re-tapping Jobs icon. No Esc/X. |
| High | Done 8/27 live | Death burns a full day | Mine / House | FIXED 8/27 5am live BUILD 20260827a: fainted in MINE 1 at DAY 430 SPRING AFTERNOON (1 heart); woke in house DAY 430 SPRING MORNING, 5/5 hearts — same dayNumber, no +1. Local 8/27 BUILD 20260827a: faint wake keeps dayNumber, dayMs=0. Was NEW 8/23 11pm: died in MINE 2 → house, day +1. |
| High | Done 8/30 2am live | Stars list clips; no close | Stars | STILL FIXED 8/30 5:30am live BUILD 20260830a: Stars X closed the panel (`15-stars-open.png`); scrollbar visible but wheel did not move list this pass (thumb near top). FIXED 8/30 2:03am: Stars X closed (`00-*` in `/workspace/playtest-0203/`). List still scrolls. Was Local Needs live. REOPEN 8/29 11am live BUILD 20260829b: Stars panel opens and scrolls (CAVE DOOR / STONE TAP / MUSHROOM FIND / MOON PIECE / KIND HEART visible); X at top-right did nothing; Esc closed. 8/24 11am live: still FIXED (X works). 8/24 5am live: still FIXED (scroll + X). 8/23 11pm live: still FIXED (scroll + X). 8/23 8pm live: FIXED. Wheel scrolls to true bottom (SHOP GLOW / CAR FRIEND / CAVE FOE / PEAK GLOW / MOONDROP NIGHT fully visible). Scrollbar track. X inside panel top-right, does not cover DAY; click closes. Local 8/23 5pm BUILD 20260823e: clipped scrollable list (drag/wheel) + X close; Esc/Space still dismiss; panel sits above the hotbar. 8/23 5pm live: last row MOONDROP NIGHT flush/cut; mouse-wheel no-op. |
| High | Done 8/23 | Toolbar buttons eat tap-to-move | HUD | 8/24 5pm: surface tap-to-walk not re-scored (round-trip farm; combat/rocks scored instead). 8/24 11am: surface tap-to-walk not re-checked (stuck underground). 8/24 5am live: tap-to-walk dirt/grass still works (FIXED). 8/23 11pm live: grass tap beside Stars still walks (FIXED). NEW 11pm: HUD overlays swallow taps — hearts/energy (top-left y≈140–190) and DAY panel (top-right) eat clicks. Hotbar y≈690 still swallows — keep HUD-overlap row Open. 8/23 8pm live: FIXED. Tap under Stars walked, no menu. Right-edge tap walked (swallow strip gone). Local 8/23 5pm BUILD 20260823g: Stars/Jobs hits inset 3px so grass around them walks; dropped a dead right-edge swallow strip; hotbar no longer steals the 3px above it. 8/23 5pm live: taps near y≈620 one tile or nothing. 8/22 3pm: upper-left play area opened Stars. |
| High | Done 8/23 | Space doesn't dismiss dialogs | Dialogue / HUD | 8/24 5pm: NIM'S NOTE boards have text; Jobs not opened. 8/24 11am: Jobs/Stars still openable (START OVER / Stars X); Space on cave signs is a no-op (see Medium signposts — 5pm: lantern-posts were the miss). 8/24 5am: Esc still closes Jobs/Stars; Junie Space talks (bring cave mushroom). 8/23 11pm: Esc still closes Jobs (START OVER row). 8/23 8pm live reconfirm: Esc dismiss works; Space swings/acts. 8/23 5pm live reconfirm: Esc closed Jobs/Stars; Space closed Junie with no walk/swing. Local 8/23 3am: Esc, Space, and Enter dismiss the top overlay (star toast, NPC talk, Stars, Jobs). Same press does not walk or swing. Wipe confirm still tap-only (Space/Esc cancel). |
| High | Done 8/26 live | No BUILD stamp on live UI | HUD | FIXED 8/26 2am live: full BUILD id `20260825o` in small wood badge top-right under SPRING · AFTERNOON / DAY panel; trailing letter o fully readable, not under hearts. Local 8/26 BUILD 20260825o: full BUILD id including the trailing letter, small wood badge at top-right below the DAY panel (not under hearts/energy/Stars/Jobs). Lowercase glyphs so the letter is not blank. 8/25 8pm/11pm live: stamp existed but the letter clipped behind the hearts (only "20260825" readable). Local 8/25 BUILD 20260825j: tiny BUILD string drawn on the live HUD (below Stars/Jobs, near FX/MU/FS). Do not mark Done until live playtest. STILL. 8/25 8am live: hard-refresh `?t=82508`, no BUILD stamp on live UI. 8/25 5am live: hard-refresh, BUILD stamp not noted. 8/25 2am live: hard-refresh, BUILD stamp not noted. 8/24 11pm live: hard-refresh, BUILD stamp not noted. 8/24 5pm live: hard-refresh, BUILD stamp not noted. 8/24 11am live: hard-refresh, no BUILD stamp. 8/24 5am live: hard-refresh, no BUILD stamp. 8/23 11pm live: hard-refresh, no BUILD stamp. 8/23 8pm live: hard-refresh, no BUILD stamp. NEW 8/23 5pm live. Can't tell which build is running. Stamp a visible build id on the live HUD. |
| Medium | Done 8/30 11am live | Mine OUT ladder needs many taps | Mine | STILL FIXED 9/2 ~10:26am live BUILD 20260831t: one tap OUT exited (`07-out-pass.webp`); **FIXED** pad-over-OUT (8am steal gone). STILL FIXED 9/2 ~8am live BUILD 20260831s: one tap OUT exited to farm at MINE sign (`06-out-ladder-one-tap-exit.webp`); note NEW Critical-adjacent (8am): sword-pad bottom-left can steal OUT — cleared on 31t. STILL FIXED 8/30 2:10pm live BUILD 20260830f: one tap OUT landed farm at MINE sign (`32-mine1.png`, `33-mine-out-tap1.png`, `34-mine-after-out.png`). FIXED 8/30 11:20am live BUILD 20260830c: one tap on MINE 1 OUT ladder left to farm at the MINE sign (`10-mine-out-onetap-farm.png`); walk-in hole also one-tap (`09-mine-landing.png`). Local 8/30 BUILD 20260830b: 5×5 fat-finger + larger pixel rect; tapHud prefers OUT over sword/hotbar; goWalk to OUT exits now. Needs live. WORSE 8/30 5:30am live BUILD 20260830a: OUT exit worked but needed several taps/steps (not clean one-tap) — reopens 11pm one-tap Done. FIXED 8/29 11:30pm live BUILD 20260829m: one tap on MINE 1 OUT left to farm at the MINE sign (`10-mine-out-onetap.png`). LIVE FAIL 8/29 11am BUILD 20260829b: stamp live; one tap on OUT / ladder still only stepped one tile; ~5–6 taps/keys to leave MINE 1 (same as 5am 29a). 29b one-tap ship did not take. Local 8/29 BUILD 20260829b: one tap on MINE 1 OUT / label / fat-finger now calls exitMine immediately (no walk-to-tile). Space/E facing OUT too. Needs live. UNTESTED 8/29 8am live BUILD 20260829a: NE/E/north farm sweep found NO mine hole / MINE sign (OUT not rechecked; possible entrance regression vs 5am). STILL 8/29 5am live BUILD 20260829a: entered NE hole; taps on OUT label / ladder each stepped one tile — ~5–6 taps + reposition to exit (not one-tap). UNTESTED 8/29 2am live BUILD 20260829a: NE hole / MINE sign not found (east+north farm sweep). UNTESTED 8/28 11pm live BUILD 20260828f: NE mine hole / MINE sign not found this pass (orchard/woods/town reached; OUT still Open). STILL WORSE 8/28 8pm live BUILD 20260828d: one tap on ladder / OUT / adjacent only walked one tile; several clicks + arrows to exit; no bats adjacent so foes not stealing tap — 28d live FAIL. Local 8/28 BUILD 20260828d: 3x3 fat-finger around OUT (includes south), HUD taps on the ladder no longer steal a hotbar slot, shaft taps beat nearby foes, Space/E while facing OUT/UP/DOWN climbs. Mine camera keeps a south floor pad so OUT sits above the hotbar. Do not mark Done until live. WORSE 8/28 5pm live BUILD 20260828c: OUT ladder again needed several clicks + arrow presses before exit to farm at MINE sign (11am one-tap FIXED not holding). FIXED 8/28 11am live BUILD 20260828c: one tap on the OUT ladder in MINE 1 exited to the farm at the MINE sign, no bounce-back. LIVE BUNDLE 8/28 9am BUILD 20260828b is on github.io (stamp live) but OUT not walked that pass (household save spawned in town). Local PASS: one click on OUT label exited; tap one tile south still exits (no walk-past). Space on OUT/UP/DOWN climbs. Fat-finger includes the OUT label (8px north) and left/right. NEW 8/28 8am live BUILD 20260828a: clicked the OUT ladder tile / OUT label ~4 times before exit triggered; tap-to-move kept walking one tile past. Expected: one tap on the ladder exits. Related to High soft-lock note that Space does not activate ladders (must step on tile). Kid-fun idea: climb-up anim + sproing SFX so the exit reads. 
| Medium | Done 8/28 live | Town house interior camera brown band | Town / House | FIXED 8/28 9am live BUILD 20260828b: household save spawned already inside the farmhouse (Day 816); walked to the north wall — room fills the view, no empty brown band, room not shoved low. Stamp `20260828b`. Local farmhouse north+south also PASS. Shop interior live UNTESTED (same clamp). Local 8/28: house/shop camera clamps to the room (center if smaller than the view); pad paints wood floor. NEW 8/28 8am live BUILD 20260828a: inside a town house, walking to the top wall leaves a large empty brown band above the room; room draws small/low in the viewport. Expected: camera clamps to the room (farm/forest clamp Done 8/25; this is interiors). |
| Medium | Done 8/28 live | House door re-enters on the next path tap | House | STILL FIXED 8/29 11:30pm live BUILD 20260829m: after doormat exit, E/W path walks stayed outside (`14-doormat-exit.png`, `15-outside-EW.png`). STILL FIXED 8/29 2am live: after exit, E/W path taps stayed outside (0 bounce). STILL FIXED 8/28 11pm live: after exit, E/W path taps stayed outside (0 bounce). STILL FIXED 8/28 8pm live: after exit, E/W path taps stayed outside. STILL FIXED 8/28 5pm live: after exit, click-to-move E/W along path stayed outside (0 re-entries). Local 8/28 BUILD 20260828d: standing on the stoop, tapping the door *sprite* (one tile north) now enters; left/right path taps still stay outside. LIVE FAIL entry: see new Medium door-entry row. NEW minor 5pm: getting IN the farmhouse door needed several click/key tries. FIXED 8/28 11am live BUILD 20260828c: after farmhouse exit, click-to-move east and west along the path stayed outside (0 re-entries). Arrow keys still OK. Local 8/28 BUILD 20260828c: while standing on the stoop, only the real door tile (or its pixel opening) enters — left/right fat-finger no longer eats path taps. Door from the yard still fat-fingers. NEW 8/28 9am live BUILD 20260828b: after exiting the farmhouse, Orion stands on the stoop; the next click-to-move east or west along the path re-entered (~4 times). Arrow keys walk fine. |
| Medium | Done 8/29 live | Farmhouse door tap rarely enters | House | STILL FIXED 8/30 2:10pm live BUILD 20260830f: night tap at (16,29) entered; doormat south → (17,30); E/W path (17,30)→(14,30) 0 bounce (`14-farmhouse-interior.png`, `15-farmhouse-out.png`, `16-farm-path-ew.png`). STILL FIXED 8/29 11:30pm live BUILD 20260829m: loaded inside; doormat (10,10) walked south to overworld (17,29). STILL FIXED 8/29 5:20pm live BUILD 20260829g: one-tap enter + one-tap doormat exit (`06-farmhouse-entered-one-tap.webp`, `11-doormat-exit-one-tap.webp`). FIXED 8/29 2pm live BUILD 20260829d: one tap on door sprite from path south entered instantly; one tap indoor doormat exited; path E/W after exit 0 bounce. WORSE 8/29 11am live BUILD 20260829b: entering took many clicks + arrow nudges; a single tap on the door tile from the path south did not reliably enter. Doormat exit also needed several taps — first two walked; only stepping onto the mat + ArrowDown left. STILL FIXED 8/29 2am live BUILD 20260829a: one tap on path tile south of door entered; one tap indoor doormat exited. FIXED 8/28 11pm live BUILD 20260828f: one tap on door sprite from path tile south entered immediately; one tap indoor doormat exited; HOME GLOW on entry with moon shard. WORSE 8/28 8pm live BUILD 20260828d: repeated taps on door sprite, stoop, and tile south never opened the house; each tap only nudged one tile or re-pathed. Got inside once only by arrow-keying onto the exact door tile. From directly below the door, a single tap still did nothing. Local 28d claimed stoop door-sprite enter — live FAIL. Was NEW minor 5pm (finicky).
| Medium | Done 8/30 11am live | Wood selected turns taps into fence place | Farm / HUD | FIXED 8/30 11:20am live BUILD 20260830c: wood selected shows BUILD chip; grass tap without chip WALKS (wood stayed 4); chip on then adjacent tap, wood 4→2 (`06-build-chip-before.png`, `07-fence-placed-wood2.png`). Local 8/30 BUILD 20260830b: BUILD-on + wood places on g/d/h/m/k including soft flora; place runs before cut-grass steal; wood-without-BUILD still walks. Needs live. STILL 8/29 2pm live BUILD 20260829d: BUILD chip on; adjacent grass taps only WALK, wood stayed 4; Space facing grass no fence (place silent-fail). STILL 8/29 11am live BUILD 20260829b: BUILD chip on; far + adjacent grass taps only WALK — no fence, no TAP A TILE, wood stayed 4 (confirmed 4 in chest UI). Place still silent-fail. UPDATE 8/29 8am live BUILD 20260829a: BUILD chip now VISIBLE above wood×4 (5am missed). With chip on, far + adjacent grass taps only WALK — no fence, no TAP A TILE banner, wood stayed 4 (place silent-fail). Walk-without-spending STILL holds. FIXED place 8/29 2am live: wood select → BUILD chip; far/adjacent grass WALKS; tap BUILD → place fence wood 2→0. NEW 8/28 11pm live BUILD 20260828f: mis-tap selected wood×4; walk taps silently placed fences. Prefer build mode or confirm before place.
| Medium | Done 8/29 live | House chest won't open | House | STILL open 8/29 11:30pm live BUILD 20260829m: chest UI PUT ALL / TAKE ALL (`13-chest.png`). STILL open 8/29 5:20pm live BUILD 20260829g: chest opened; PUT ALL / TAKE ALL exercised. STILL open 8/29 2pm live BUILD 20260829d: bump/facing Up opened CHEST BAG/BOX (no Space needed this pass). FIXED open 8/29 11am live BUILD 20260829b: Space while facing the crate opens CHEST BAG/BOX (WOOD 4 / STONE 2 / FLOWER 7 / MUSHROOM 7 / SHARD 1 + ores/bars); list has a scrollbar. Adjacent tap / double-tap still do NOT open — keyboard only. STILL Open 8/29 8am: farmhouse not entered this pass — entered PIP'S SHOP (Pip behind counter; SEED TIN/FENCE KIT etc; BYE). House chest not retested. NEW 8/29 5am live BUILD 20260829a: stood adjacent to house chest; tap, double-tap, and Space — no inventory panel. Expected BAG/BOX UI. Blocks verifying chest-scroll Local 28e. Forest chest not retested that pass.
| Medium | Done 8/29 live | Chest TAKE ALL / row tap cannot retrieve | House chest | STILL FIXED 8/29 11:30pm live BUILD 20260829m: PUT ALL / TAKE ALL both worked; items back in bag. FIXED 8/29 5:20pm live BUILD 20260829g: PUT ALL moved WOOD4/STONE2/FLOWER7/MUSHROOM7/SHARD1 BAG→BOX; TAKE ALL returned every stack BOX→BAG (screenshots `/workspace/playtest-1719/07-chest-before.webp`, `08-chest-put-all.webp`, `09-chest-take-all-works.webp`). Local 8/29 ~5pm BUILD 20260829g: TAKE ALL now uses the working BOX-cell transfer (`takeFromChest`) for every row with a BOX count. Footer strip: PUT ALL is the left wood; everything else on that strip is TAKE ALL (covers the 2pm clustered-button miss). Empty BOX still toasts CHEST IS EMPTY; bag full toasts BAG FULL. Row/BOX-cell tap, PUT ALL, BACK, scroll unchanged. Was Needs live. UPDATE 8/29 2pm live BUILD 20260829d: TAKE ALL still no-op with SHARD 1 in BOX (counts unchanged). NEW workaround: tapping the BOX number/cell on the SHARD row moved BOX 1→0 / BAG 0→1 instantly — button handler broken, transfer path OK. Screenshots `/workspace/playtest-1420/04-takeall-nochange.png`, `05-boxtap-works.png`. NEW 8/29 11am live BUILD 20260829b: clicked SHARD row deposited BAG 1→BOX 1. Then row tap, BOX number, double-click, and TAKE ALL all said CHEST IS EMPTY / NOTHING TO PUT — shard stuck in the box. Expected TAKE ALL (or tapping the BOX count) to return it. Screenshot `/workspace/playtest-1115/13-chest-shard-stuck.png`.
| Medium | Done 8/30 2am live | Town NPCs walk off before talk | Town | STILL FIXED 8/30 5:30am live BUILD 20260830a: Lila adjacent Space talk PASS (`THE STATUE USED TO TWINKLE. PLANT THREE FLOWERS ON THE GREEN FOR ME.` — NPC froze; `18-npc-lila-dialog.png`). FIXED 8/30 2:03am: Junie froze; `THANKS AGAIN! CHECK YOUR MAIL.` Screenshots `/workspace/playtest-0203/`. Was Local Needs live. UPDATE 8/29 11:30pm live BUILD 20260829m: Junie Space talk PASS (`THANKS AGAIN! CHECK YOUR MAIL.` `16-junie-talk.png`); Nim not at well; town/Pip UNTESTED. STILL 8/29 5:20pm live BUILD 20260829g: town tap no dialog; farm adjacent+facing Space still no dialog (`03-npc-tap-no-talk.webp`, `12-space-facing-npc-no-dialog.webp`). Nim bump-talk DID open. Freeze ship did not clear Space talk. Local 8/29 ~5pm BUILD 20260829g: town/forest folk freeze while the player is adjacent and facing them so Space talk can land. Was Needs live. NEW 8/29 2pm live BUILD 20260829d: stepped adjacent to a townsperson, faced them, Space — they had already moved a tile; no dialog (2/2 misses). Makes Junie/Pip talks feel broken for kids. Screenshot `/workspace/playtest-1420/11-npc-wander-no-talk.png`.
| Medium | Done 8/29 live | Chest list clips; no scroll | House / woods chest | FIXED 8/29 11am live BUILD 20260829b: house chest list showed a scrollbar and BAG/BOX columns (PUT ALL / TAKE ALL / BACK). TAKE ALL itself is a new Open row (shard stuck). BLOCKED 8/29 5am live: house chest itself would not open (see new house-chest row) so scroll still UNTESTED. Local 8/28 BUILD 20260828e: BAG + BOX list clips to the panel and scrolls (wheel over the list, drag the rows, scrollbar track). PUT ALL / TAKE ALL / BACK kept. Tap a row still puts/takes; a drag does not walk. Do not mark Done until live. NEW 8/28 Darren: opening a chest you cannot see every stack.
| Medium | Local 8/28 | Treetop walk on sky; south path is DOWN | TREETOP | Local 8/28 BUILD 20260828f: walkable cells recarved to the painted wood/leaf paths (sky/air solid). South stairs labeled WOODS and exit to the forest at (25,12), not TREE 4. Existing DOWN hole stays for the indoor climb-down. Do not mark Done until live. NEW 8/28 Darren.
| Medium | Local 9/5 | Night wash / tint inconsistent | Overworld | UPDATE 9/5 BUILD 20260905bb: one frameDayT/grade sample per draw; outdoor night lift shared farm+forest (evening GRADE_KEYS unchanged); applyScene clears grade cache. Live still needed. STILL 8/28 11pm live: HUD SPRING·NIGHT while scene rendered full daylight right before day rolled 1078→1079. STILL 8/25 8am live: farm night still sometimes flat navy (right after forest→farm transition, WOODS sign nearly unreadable); a few steps south the same night was lighter grey-green with lamp glow. UPDATE: HUD read SPRING · EVENING while the farm rendered full bright daylight (no evening tint); forest at the same phase was tinted. Lighting lags/skips a phase on the farm. STILL 8/25 5am live: farm night still sometimes flat navy; forest night-grade lift not applied to farm. Forest interior now readable (High forest-night Done). 8/25 2am live: woods-edge night = flat navy silhouettes, lamp pools OK where lamps exist. Forest interior not reached that pass. REOPEN 8/24 11pm live: night tint inconsistent on farm. Forest night unreadable is its own High (trees/ferns flat dark-blue silhouettes). Was 8/23 8pm live reconfirm: full blue + lamp pools, good. 8/23 5pm live: Jobs at NIGHT, panel clean, no blue strips (dialog no longer strips night tint). Was STILL 8/23 midnight: outdoors good; opening a dialog stripped the night tint while header still said NIGHT. 8/22 3pm: north forest tints blue then flips to daylight-green while the header still says NIGHT; plaza stays blue; east houses render daylight at NIGHT. Drive tint from one global time value applied per-scene, not per-region. |
| Medium | Done 8/27 live | Sword button visibility confusing | HUD | FIXED 8/27 11am live BUILD 20260827b: showStrikeBtn true on farm/forest when sword selected; false in house/shop. Tap-to-hit still UNTESTED (Critical sword). Local 8/27 BUILD 20260827b: button shows whenever the sword is selected (not only in the mine); hidden in house/shop. Bigger tap target. UPDATE 8/24 5pm live: on-screen sword button present near enemies, hides on quiet farm (confusing — control vanishes). Was Done 8/23 as mine-only leftover: leftover-on-farm is gone, but hide-when-quiet reads as a missing control. 8/24 11am: sword button present in mine (still misses — see Critical). Never reached surface so farm leftover not re-checked. 8/24 5am: sword button present in mine (never lands — see Critical). Farm leftover not re-checked. 8/23 11pm: sword used in MINE 1/2 (button present; swing itself dead — see Critical). Farm after OUT not re-checked for leftover button. 8/23 5pm live reconfirm: sword button still mine-only (MINE 1/2). 8/23 midnight reconfirm: sword button still mine-only. 8/22 3pm reconfirm: absent on farm, forest, town, house, shop. Mine not reached 8pm. |
| Medium | Local 9/5 05cd | Mine look | Mine | Local 9/5 BUILD 20260905cd: cozy torch/lamp falloff in mine/stairs/cave — soft vignette + warmer pools near lanterns (readable for a 7-year-old, not pitch black). Needs live. Was Partial: still uniformly lit, no torch falloff. Lamps glow. 8/24 5pm: deep floor + note room seen; look not re-scored (fake-hole tile split to its own row). 8/24 11am: underground the whole pass; look not re-scored. 8/24 5am: Mine 3 reached; look not re-scored. 8/23 11pm: mine entered (MINE 1 + 2); look not re-scored. 8/23 midnight: mine entered; look not re-scored. Mine not found 8pm. |
| Medium | Done 8/23 | Header swaps season for place | Interiors | 8/24 5pm live: header still DAY/SPRING/phase (290 AFTERNOON → 291 NIGHT) while underground and on the farm. 8/24 11am live: header still DAY 290 SPRING AFTERNOON while underground. 8/24 5am live: header DAY/SPRING/phase in MINE 1, MINE 2, and MINE 3. 8/23 11pm live: Done. Header reads SPRING · MORNING/AFTERNOON in MINE 1, MINE 2, and house — never "MORNING · MINE 1". Intended 5pm fix holds indoors. 8/23 8pm live: FIXED outdoors — header reads SPRING · MORNING/AFTERNOON/EVENING/NIGHT. Indoors/mine not reached that pass. Local 8/23 5pm BUILD 20260823i: header always SPRING · phase (shop/mine/home no longer steal the season slot). 8/23 5pm live: time+place indoors/mine, time+season outdoors. |
| Medium | Local 9/5 05cg | Slug contact drains hearts; no i-frames / heal | Mine | Local 9/5 BUILD 20260905cg: kid-visible white iframeFlash bloom + soft full-view wash on contact/block (existing 2s i-frames kept). Needs live for flash readability. Was LIVE 9/3 ~7:16–7:38pm BUILD 20260903b: slime i-frames **FIXED** (5→4 hold ≥3.5s); bat i-frames STILL PASS. Was LIVE 9/2 ~7:27–7:36pm BUILD 20260831u: **WORSE** bat contact — full 5♥→KO in ~2s proximity on MINE 6; −1G house wake (`06-bat-KO-wake.webp` in `/workspace/playtest-1927/`). Was Local 9/2 BUILD 20260831t: hurtPlayer iFrames 800→1200 after contact/block (contact damage kept). Needs live — not Done. Was LIVE 9/2 ~7:38–8:02am BUILD 20260831s: **Bat instant-KO FIXED** — brief overlap −1 heart + knockback; survived multiple bats, no faint/−1G (`04-bat-swing-knockback-4hearts.webp`). **STILL harsh:** ~3s clip drained 4→2 with no clear i-frame flash (`05-bat-contact-drain-2hearts.webp`). Slime contact UNTESTED. Was LIVE 9/2 ~4:22–4:30am BUILD 20260831s: **Bat contact WORSE** — overlap drains 5→3→1→KO in ~10s with red hit flash (`08-bat-contact-3hearts.webp`, `09-bat-contact-1heart.webp`, `10-faint-respawn-house.webp`); −1G on house wake (16→15); no usable i-frames for a kid. Slime contact UNTESTED (no slime/grub seen on MINE 1; possible missing ground foes — `07-mine1-no-monsters.webp`). Was LIVE 9/2 ~2:34am: slime contact STILL PASS (5→2); **Bat UNVERIFIED** (driver died mid-overlap). Was Local 9/2 BUILD 20260831s: bat/flying contact radius widened (pixel ~20 + tile-neighbor); i-frames kept. UPDATE 9/1 ~10:22pm live BUILD 20260831r: **FIXED** contact on MINE 2 slimes (5→4→3→2 hearts) (`06-slime-contact-damage-3of5.webp`). **NEW/WORSE for bats:** MINE 1 bats overlapped 4+ s with zero damage (`03-bats-adjacent-hearts-full.webp`) — bat contact FAIL. Faint UNTESTED (stopped at 2/5). Was UPDATE 9/1 ~7:40pm live BUILD 20260831r: stood adjacent to slime+snail on MINE 1 many times — **zero** hearts lost (5/5 whole pass). Contact may be floor/enemy specific or miss this spawn. UPDATE 9/1 ~4:46pm live BUILD 20260831q: bat contact on MINE 6 KO'd low-heart Orion (home revive). Hit-size / i-frames still unclear (was ~1 heart left). Local 8/27 BUILD 20260827b: monster hit flash on strike (white flash). i-frames already existed. FIXED-contact 8/27 5am live BUILD 20260827a: bats deal contact (5→4→3→1); 2am zero-damage was flee-whiffs, not missing hitcode. Crawlers often miss until a real overlap. Still no hit flash / i-frame juice. STILL 8/24 5pm: chase and hit hard. Combat one-sided. 8/24 11am: armadillo Space-killed; contact drain not re-scored. 8/24 5am live: contact 5→3 in ~10 min, no enemy attack anim. Death-burns-day untested this pass. Mine 1 roomy so less burst than 11pm. 8/23 11pm live: contact damage real and deadly — 5→2 hearts quickly in MINE 1 (packed at entry); died in MINE 2. Death: "THE MOUNTAIN SENT YOU HOME", house respawn, hearts full, day +1 (see High death-burns-day). i-frames may still exist but pack density outruns them. 8/23 8pm: no overworld enemies; slug contact untested. 8/23 midnight: bump cost 1 heart (5→4), no repeated drain (i-frames present). Hearts refill on sleep. Was: 8/22 midnight contact 5→3, no i-frames, no heal. |
| Medium | Done 8/27 live | Mine floors packed with enemies at entry | Mine | FIXED 8/27 8pm live BUILD 20260827f: MINE 1 walk-in at full hearts; landing roomy; foes (slime/bats) visible off the pad, not stacked on drop-in. Local 8/27 BUILD 20260827c: every floor now 4 mobs, placed on walkable tiles ≥3 Manhattan from UP/DOWN landings; mineKeepClear uses pad radius 2 so wanderers stay off the drop-in tiles; sleep/faint clears monsterCache 1–6. 8/24 5pm: spawned already deep (gem + note room); bats + slimes + armored bugs chase and hit hard. Pack-at-walk-in not re-checked. 8/24 11am: already underground (no walk-in entry); pack-at-entry not re-checked. Bats still jitter. UPDATE 8/24 5am: Mine 1 NOT packed this time (2 enemies, roomy). Mine 3 IS packed (5+ slugs, 4 bats, slimes). Spawn variance; thin Mine 3 / keep a safe landing. Was NEW 8/23 11pm: walking into MINE 1: brown slugs / purple bats / green slimes stacked at the entrance. Lost 3 hearts (5→2) before reading the screen. Contact damage is real; sword Space-kills only if hotbar selected (see Critical). |
| Medium | Done 8/26 live | Deep-floor black square looks like a hole | Mine | FIXED 8/26 5am live: floor 4 tile next to note-post is walkable cave floor (no fake drop). Real DOWN 1→2→3→4 all worked; UP ladders present. Floor 3 still has a solid black 1×1 that blocks (no drop) — does not read as a hole; not reopened. Floors 5/6 not reached. UNTESTED 8/26 2am live: reached MINE 1 only; no 1×1 black squares there; floors 4/5/6 not seen. Local 8/26 BUILD 20260825o: recarved the 1x1 isolated deepWall pillars on floors 4/5/6 (open-floor black squares that read as a hole/ladder but were solid, not a drop) to matching cave floor. Real DOWN holes unchanged; farm mine entrance unchanged. Do not mark Done until live. NEW 8/24 5pm live. Next to the note-post on the deep floor: a solid black square reads as a hole / ladder but is solid (not walkable, not a drop). Easy to waste time trying to fall through. |
| Medium | Done 8/25 live | Camera overscrolls past world bounds | Farm / Forest N | FIXED 8/25 5am live: north edge clamps, no black void, player visible. STILL 8/25 2am live (woods-edge / farm north; forest never loaded): void band still there, green by day / navy by night (recolored not gone). 1am forest clamp UNVERIFIED that pass. Local 8/25 1am BUILD 20260825d: forest camera clamps to the map; north pad is at most HUD top inset and filled with moss (not black). Orion stays in the HUD band. Farm clamp not re-scored. REOPEN 8/24 11pm live: camera scrolls past forest north into empty void. Farm clamp not re-scored this pass. Was 8/23 8pm live reconfirm: north clamp, no black void; green filler under header, OK. 8/23 5pm live: surface north clamps clean (no void). South not re-hit. Mine N/S black bands split to a new Low. Was STILL 8/23 midnight: north ~170px empty band. 8/22 3pm: N forest and S farm pads keep Orion on-screen, but the camera scrolls past the tile edge into a flat green/blue void band. Clamp camera to the world rect; keep the HUD-safe player insets. |
| Medium | Done 8/23 | Space doesn't trigger NPC talk when adjacent | Overworld | 8/25 5am live: Hazel/Rowan-like NPCs present in the forest (talk not re-scored). 8/24 11pm live: Hazel and Rowan talk in the forest. 8/24 5pm: Junie/NPCs not re-checked (farm reached via OUT). Cave note-boards now show NIM'S NOTE (see signposts). 8/24 11am: Junie/NPCs not reached (stuck underground). Cave signs: Space no message (11am miss — lantern-posts). 8/24 5am live reconfirm: Junie Space talk works (bring cave mushroom). 8/23 11pm: Junie found SW of house; Space-talk not re-checked. 8/23 8pm: Junie/NPCs not found. 8/23 5pm live reconfirm: standing above Junie re-opened her mushroom dialog. Local 8/23 3am: Space talks to an adjacent/facing NPC (Junie, Nim, town folk, shop Pip). If a dialog is already open, Space dismisses it instead of talking again. |
| Medium | Local 9/5 05cj | Enemies never die / hit+loot feedback | Mine | Local 9/5 BUILD 20260905cj: always-drop loot + bigger HP pips. Was Local 9/5 BUILD 20260905ci: kill burst + HP pips + loot flash/toast + stronger hit flash. Needs live. Was LIVE 9/3 ~7:16–7:38pm BUILD 20260903b: slime pad kill **FIXED** (1 tap); bat pad kill STILL PASS. Was LIVE 9/2 ~7:27–7:36pm BUILD 20260831u: **STILL FAIL** pad on MINE 6 bat — no kill/loot (`04`–`05` in `/workspace/playtest-1927/`). Was Local 9/2 BUILD 20260831t: pad arc damage 4 should restore 1–2 tap kills + loot (fixes 31s knockback-only). Needs live — not Done. Was LIVE 9/2 ~7:38–8:02am BUILD 20260831s: **WORSE** — pad swings only knock bats back; **no kill / no loot** this pass (floor uncleared). Was LIVE 9/2 ~2:34am BUILD 20260831s: **FIXED** left/diagonal pad kill (31r left-slime miss cleared) — white flash then vanish (`25-left-slime-killed-by-pad.png`). Loot this kill UNCONFIRMED. No HP pips still. Was Local 9/2 BUILD 20260831s: omnidirectional swing should clear left-adjacent miss. UPDATE 9/1 ~10:22pm live BUILD 20260831r: pad kills work with **loot** — bat → coin, slime → ore (7:40pm no-loot miss cleared for these kills). Facing-limited: left-adjacent slime survived. No HP pips / flash still. Was UPDATE 9/1 ~7:40pm live BUILD 20260831r: adjacent snail **killed** by sword pad (vanished; no flash/loot). Slime needed true adjacent+facing; no HP pips. Kill works, feedback/loot still missing. UPDATE 9/1 ~4:46pm live BUILD 20260831q: **contact damage FIXED** — purple bat on MINE 6 drained remaining hearts → "THE MOUNTAIN SENT YOU HOME." → bed Day 1748 morning 5/5 (`04-mine6-bat-swordpad.webp`, `05-sent-home-after-bat.webp`, `06-home-full-hearts.webp`). MINE 1/2 had no slime/bat this pass (foes deeper). Sword-pad kill/loot still UNVERIFIED (pad looked inert; KO before hit). Prior 1:07pm scenery combat on MINE 1/2 superseded for contact. |
| Medium | Done 8/24 live | Cave signposts show no text | Mine | 8/24 5pm live: note-boards have text (NIM'S NOTE). 11am "signs show no text" was lantern-posts mistaken for signs. Was NEW 8/24 11am live. Standing at cave signs, Space gives no message. Kids can't read where they are or how to leave. |
| Medium | Done 8/24 live | Ore / dark blocks unmineable; block gem | Mine | 8/24 5pm live: ore/gem reachable. Tapped the gem → "A SHINY GEM" + inventory slot. Spawned in the deep gem + note room (no ore wall this pass). Was NEW 8/24 11am live. Dark/ore blocks: adjacent Space with pickaxe or stone is a no-op. They wall off the path to the teal Mountain Heart gem. Combined with the gem itself not pickup/mineable (see Low). |
| High | Done 8/26 live | House stoop enters the interior | House | FIXED 8/26 8pm live BUILD 20260826a: tapped stoop tile south of door 3 times (night + day + from across the map) — walked onto stoop, STAYED OUTSIDE. Door pixels enter. Exit lands outside, no bounce. Clicking porch/door-base pixels still enters (intended door hitbox). Arrow-key walk-on-stoop already Done 8/25 live — both arrow-key and tap-on-stoop now live-verified. Local 8/26 BUILD 20260826a: tap/click on stoop (17,29) no longer calls goEnterHouse — houseDoorHit(17,29) false; pixel rect stops above stoop row; tap walks to stoop and stays outside. Door tile (17,28) / door pixels still enter; exit still lands (17,29). Arrow-key Done holds. Prior FIXED 8/25 8pm live BUILD 20260825n: stood on stoop — stayed outside; one step onto door — entered; exit landed on stoop (twice). Click-to-move onto stoop could still path through door and enter (leftover). Local 8/25 BUILD 20260825n: `houseIn` door (17,28); stoop (17,29) no longer enters on step; exit lands stoop. NEW 8/24 Darren. |
| Medium | Local 9/5 05cc | Car is tiny | Town | Local 9/5 05cc (needs live): denser bigger Reed car (~2× vs 05at) — 3× BOX frames (side 72×48 / vert 48×60), draw scale 2, ASSET_REV=467501; hit/lamp/shadow match. Was Partial 9/5 tiny sprite. NEW 8/24 Darren. |
| Medium | Local 9/5 05bj | Pickaxe must NOT destroy placed paths | Farm | Local 9/5 BUILD 20260905bj: pickaxe Space/swing/tap no longer lifts player-placed dirt paths (paths stay; no stone refund). Rocks still smash. Was Local 8/25 BUILD 20260825n (pickaxe DID mine paths) — Darren 9/5: paths stay. Needs live. |
| Medium | Local 9/5 05bk | Fences cannot be moved | Farm / town | Local 9/5 BUILD 20260905bk: kid pick-up — axe, shovel, or empty hand with BUILD off removes fence in one tap/Space; refunds **1 wood** into bag + toast `FENCE PICKED UP` (bag full keeps fence). BUILD-on wood place flow unchanged. No longer multi-hit tree smash / ground loot. Needs live. Was Local 8/24 BUILD 20260824h tree-smash + ground wood (unverified live). |
| Medium | Done 8/25 live | Forest chest won't open | Forest N | FIXED 8/25 ~2pm live BUILD 20260825m: Space/E/bump from south-adjacent; BAG/BOX UI. Local 8/25 BUILD 20260825j: Space/E from orthogonal adjacent (and one extra step south of the hanging forest sprite) open the UI; keyboard bump into solid chest opens; goWalk onto chest tile paths via goChest. Node-tested adjacent S+1/S+2 + bump + house chest. Do not mark Done until live. FIXED 8/25 8am live: tap on the sprite opened the full house-style chest UI (columns + PUT ALL / TAKE ALL / BACK). Space also works while standing on/overlapping the chest tile. Contents: STONE 5, FLOWER 4, COPPER 1, SHARD 1, SILVER 1. Player no longer hides the sprite (5am z-order). STILL: E-key and adjacent-Space do nothing when standing south of the chest; bump-into alone did not open. Chest cosmetics (RAG header, BACK overlaps CHEST title) — see Low. Local 8/25 BUILD 20260825g: Space/E/tap and walk-into the solid chest open the same house chest UI (chest checked before Hazel/Rowan talk-steal). Foot-Y raised so Orion no longer covers it. Store/take shares house stacks. WORSE 8/25 5am live: CHEST sign + sprite present (east of stump), does NOT open. E/Space adjacent — no UI. Walking onto the chest hides the sprite under the player (z-order). UNVERIFIED 8/25 2am live: forest never loaded. Local 8/25 1am BUILD 20260825c: chest at (13,11). NEW 8/24 11pm live. Rowan talks about a chest by the stump; chest never found. |
| Medium | Done 8/25 live | Number keys 1–8 don't switch hotbar | HUD | FIXED 8/25 2am live: keys 1–8 select hotbar. Local 8/25 1am BUILD 20260825e: keys 1–8 (and numpad) select the matching visible hotbar slot, same order as click. Does not eat food. Was NEW 8/24 11pm live (also 8/24 5am: number key 7 does not select the sword slot). Click the slot only. Keyboard hotbar was dead. |
| Medium | Local 9/5 | Lamp posts and WOODS sign look alike | Farm / woods-edge | Local 9/5 BUILD 20260905az: Imagine woodsSign plaque (recentered) + floating shaft labels WOODS/FARM/MINE/OCEAN/PEAK/ISLAND (same style as OUT); mine/peak reuse plaque — no woodPanel blob that matched lamp silhouette. Needs live. Was STILL 8/25 8am live (also in forest). NEW 8/25 5am live. At distance, lamp posts and the WOODS sign share the same tall-post silhouette — easy to miss the forest door. |
| Medium | Done 8/25 live | Woods exit re-enters immediately | Farm / Forest N | FIXED 8/25 ~2pm live BUILD 20260825m: landing south of WOODS; one north tap no re-enter. Local 8/25 BUILD 20260825j: exitForest now placePlayer(5, 11, "down") — two tiles south of door (5,8); landing is not isForestEntrance; needs ≥2 north walks to re-enter. enterForest / door zone (dx -1..1, dy 0/-1) unchanged. Node-tested. Do not mark Done until live. NEW 8/25 8am live: After FARM exit you land one tile below the WOODS sign, so a north tap-to-move instantly re-enters the forest. Cost two accidental round trips (and 2 in-game days) this pass. |
| Medium | Done 8/25 live | Forest lamp post blocks the dirt road | Forest N | FIXED 8/25 ~2pm live BUILD 20260825m: lamps off dirt. Local 8/25 BUILD 20260825j: moved forest lanterns off dirt (tx 13–15) — (12,20), (16,40), (16,62); kept (12,56)/(6,50)/(21,55)/(22,4). Night glow kept. Node-tested zero lanterns on road columns. Do not mark Done until live. NEW 8/25 8am live: Forest lamp post sits in the middle of the north–south dirt road and fully blocks it; must path around to reach FARM exit. |
| Medium | Local 9/5 | Only one weapon equipped | Combat / HUD | Local 9/5 BUILD 20260905ay: at most one of sword/bow in the 10-tray; moving a second weapon in (bag drag / grant / placeTool) parks the prior in the bag; tools (axe/pick/shovel/pole/diamondPick) stay. Cave sword force-pin still owns tray slot 0 and evicts bow. Needs live. Was NEW 8/24 Darren. |
| Medium | Done 9/5 local | Ability to dig holes | Farm | Local 9/5 BUILD 20260905ax: 8 farm grass mounds (pebble/veggie/stone/potato/flower/mushroom); dig only on mounds; shovel walk OK. STILL UNTESTED 8/31 8:45am live BUILD 20260831a: peak soft-lock; still no shovel. STILL UNTESTED 8/31 5:50am live BUILD 20260831a: no shovel in tray/BAG (`10-bag-grid-no-shovel.webp`). Farm still Open. UNTESTED 8/31 2:19am live BUILD 20260831a: box Chrome save has no shovel in tray or BAG (`04_bag_no_shovel.webp`) — cannot confirm farm grass no longer tills. Local 8/31 BUILD 20260831a: shovel no longer tills every farm grass tile (stole tap-to-walk). Woods still 7 marked mounds. Not claimed farm-done. Local 8/29 woods: shovel on 7 marked dirt/leaf mounds (not whole floor). |
| Medium | Local 8/30 | Ability to upgrade the house | House | Local 8/30 BUILD 20260830p: Pip HOUSE KIT. Tier 0->1 needs 12 wood + 8 stone (extra rug/plant/crate/lantern, same 20x12). Tier 1->2 needs 20 wood + 12 stone (HOUSE_COLS 20->24, extra window+flowerbox, fireplace to east wall, inndoor stays tx 10). houseTier persist default 0. Jobs: PIP SELLS A HOUSE KIT. Do not mark Done until live. |
| Medium | Local 8/30 | Potato and berry seeds at Pip | Farm / Shop | Local 8/30 BUILD 20260830p: POTATO SEED / BERRY SEED 8G. If tray already has that tool, YOU ALREADY HAVE SOME. Else placeToolInTrayFirst. Seeds stay tools (not consumed). SEED TIN still extra plots. Do not mark Done until live. |
| Medium | Local 8/30 | More things to BUILD (lamps, crates) | Farm / Shop | Local 8/30 BUILD 20260830q: Pip LAMP KIT / CRATE KIT 10G give 3 placeables. Selected kit taps empty grass/dirt/cobble (not crops/water/doors/NPCs/rim). Lanterns walkable (max 12). Crates solid (max 12). Persist in builds. Wood-fence BUILD chip unchanged. Do not mark Done until live. |
| Medium | Partial 9/5 05ck | Ocean and boats south of the house | Overworld S / ocean | Local 9/5 BUILD 20260905ck: pier boat bobbing GET IN label (rideable prop). Local 9/5 BUILD 20260905ci: foot on deep `y` blocked + unstick TOO DEEP (boat row unchanged). Local 9/5: rideable pier boat **Local 05a–05bo+** (GET IN/row/GET OUT, island dock, stranding fixes) — needs live re-confirm on household; older notes saying decor-only are stale. UPDATE 9/1 ~1:15am live BUILD 20260831o: east foam/deep walk **FIXED**; beach grass→sand→foam Imagine bands PASS; boats/ride still decor-only / untested this pass. UPDATE 8/31 5:50am live BUILD 20260831a: path enter/exit **PASS**; dock boats **PASS** visible (5+ rowboats + sailboat) but decor-only (no ride). **NEW BUG:** walk on open/deep ocean water past surf (`07-walking-on-open-water.webp`, `11-deep-water-walk-bug.webp`). **NEW cosmetic:** night tint washes whole cove incl. player then snaps bright (`08-water-walk-night-lighting-mismatch.webp`). Prior 2:19am: OCEAN sign walk-in PASS; boats not on first screen. Local 8/30 BUILD 20260830l. NEW 8/30 Darren.
| High | Done 9/1 1:15am live | Walk on open ocean water | Ocean / cove | FIXED 9/1 ~1:15am live BUILD 20260831o: continued save on OCEAN; walked east to foam col 30 row 13 and stopped; arrow-mash + taps could not enter col 31+; cols 31–32 blocked on every row 8–20 (edge walkable only rows 6/7/21) (`06-ocean-east-edge.webp`, `07-ocean-deep-water-blocked.webp`). Local 8/31 BUILD 20260831o: marks east foam col 31 solid on walk rows 8–20; deep water was already solid since 31b. Needs live. UNTESTED 8/31 5:20pm live BUILD 20260831j (peak stranded). Local 8/31 BUILD 20260831b: tightened buildOceanGround walk mask (deep east/south water now solid). Do not mark Done until live. UNTESTED 8/31 2:46pm live (mine/peak first). UNTESTED 8/31 8:45am live (peak soft-lock blocked ocean). NEW 8/31 5:50am live BUILD 20260831a: from beach, walk past surf onto deep water several tiles offshore; stand on waves by sea rock (`07-walking-on-open-water.webp`, `11-deep-water-walk-bug.webp`). Block deep-water tiles (or mount a boat instead).
| Medium | Local 9/5 05ca / cart Done 9/1 live | Kick ball on farm yard (+ town plaza) | Farm / Town | Local 9/5 BUILD 20260905ca: real kickballs at farm (12,32) and plaza (44,31); walk/bump/tap/Space; bounce off solids; persist; Jobs after cart. Town cart kick still PASS from 31o. FIXED copy 9/1 ~1:15am live BUILD 20260831o: Jobs shows `KICK THE CART IN TOWN.` (`03-jobs-20260831o-cart.webp`); kick gameplay STILL PASS. Local 8/31 BUILD 20260831o: Jobs text now `KICK THE CART IN TOWN.` (copy-only; kick gameplay still PASS). UPDATE 8/31 5:50am live BUILD 20260831a: Space next to red cart/truck south of fountain shows `KICK!` and it slides (`18-kick-works.webp`). Jobs text was `KICK THE BALL IN TOWN.` — art/object is a cart. Local 8/30 BUILD 20260830s.
| Medium | Local 9/4 04j–04k | House dog follows on a leash | House / overworld | Local 9/4 BUILD 20260904j–04k: dog follows outside while LEASH is on the 10-tray; out of tray sends them home; leave house with tray leash warps dog to porch; talk tip PUT THE LEASH ON THE TRAY. Indoor roam later 05bh. **Still needs live verify.** Was NEW 8/30 Darren. |
| Medium | Local 9/5 05ck (live TBD) | River east of town; broken bridge | Town E | Local 9/5 BUILD 20260905ck: floating `8 WOOD`/`FIX!` + dialog wood count + Jobs when ≥8 wood; repair still 8 wood. Was Local 8/30 BUILD 20260830m. **Still needs live verify.** Was NEW 8/30 Darren. |
| Medium | Local 8/30 30n | More village houses; some enterable | Town | Local 8/30 BUILD 20260830n: blue cottage + red-roof enterable village houses (Imagine paintings). More houses later ok. **Still needs live verify.** Was NEW 8/30 Darren. |
| Medium | Local 8/30 | More trees in the forest | Forest N | Local 8/30 BUILD 20260830j: 22 extra pine/oak/birch among the woods. Dirt road cols 13-15, giant-tree door (25,8), and south FARM exit kept clear. Walkable gaps left. Do not mark Done until live. NEW 8/30 Darren. Thicker woods — plant more trees. |
| Medium | Done 8/27 live | Woods bush berry drop + large mushroom pickup; fallen logs unchoppable | Forest N | FIXED 8/27 2am live BUILD 20260827a: fallen log 2 taps no-axe, wood pile walk-on (WOOD x4). Berry bush smash + walk-on pickup (1→3). Mushroom pickup still works; star title MUSHROOM FIND in live bundle (toast too fast to photo). Local 8/27: 2 HP / axe one-shot; loot-first on bush from 20260826f. |
| Medium | Local 9/5 05bn | Smelt ore in the house fire | House | Local 9/5 BUILD 20260905bn: select copper/silver/goldore (or ore in tray), tap/Space fireplace → 1 ore = 1 bar; toast SMELTED COPPER!/SILVER!/GOLD!; Jobs tip + once-per-save fireplace tip; ore-only (no wood). Needs live verify. Was Local 8/26 BUILD 20260826c (A COPPER BAR! toast). |
| Medium | Local 9/5 05bl | Z's when Orion is tired | HUD / Player | Local 9/5 BUILD 20260905bl: energy ≤25 shows 1–3 kid-visible outlined floating Z's above Orion (grow as they rise; first Z immediate; faint pose too). Walk energy still free (ENERGY_WALK_TILES=0). Needs live. Was Local 8/26 BUILD 20260826d tiny cream 1× glyphs. |
| Medium | Verify 8/27 | House windows always look like night | House | LIVE BUNDLE 8/27 11am BUILD 20260827b: houseWindowPane morning is pale blue (#C8E4F6) no stars. Visual in-house still not photographed. Local 8/26 BUILD 20260826e: house window panes tint from the global clock (morning pale, afternoon daylight, evening gold, night blue+stars). Frame sprite kept. |
| Medium | Done 8/26 live | Imagine Hazel, Rowan, woods chest, signs, nest, bird | Forest / Treetop | FIXED 8/26 11pm live BUILD 20260826h: Hazel/Rowan-style figures, chest + CHEST sign, signposts, nest, deer/rabbit/squirrel, birch/pine/oak all render clean day and night. Local 8/26 BUILD 20260826g: extra-PNG folk 16x24 + chest/sign/nest/bird 16x16 + treetop sky tile. Fill painters kept as fallback. |
| Medium | Done 8/26 live | Giant tree door jumps straight to the treetop | Forest N | FIXED 8/26 11pm live BUILD 20260826h: WOODS → forest (14,63) → N/NE to trunk (25,8) UP door → TREE 1 (nest) → 2 → 3 (chest) → 4 (moon shard) → TREETOP → DOWN chain lands forest (25,10) beside trunk, no re-enter loop. HUD labels TREE 1–4 / TREETOP. Nest + moon shard pickups work. Local 8/26 BUILD 20260826h: door (25,8) enters TREE 1 hollow; climb 1→2→3→4→TREETOP; DOWN from TREE 1 lands (25,10). |
| Medium | Done 9/1 10:25am live | TREE 1–4 sky still flat blue + repeating leaves | TREE 1–4 | FIXED 9/1 ~10:25am live BUILD 20260831q: TREE 1–4 sky is quiet mottled blue with tiny cloud wisps; leaf clusters only at wood platform edges; 4× zoom shows low-contrast blue speckle — no repeating leaf grid, no hashed clouds (`01-tree1.png`–`04-tree4.png`, `04-sky-zoom.png`). TREETOP Imagine canopy PASS (`05-treetop.png`). Local 9/1 BUILD 20260831q: quiet mottled fill (dropped 31p hashed cloud grid). Local 9/1 BUILD 20260831p: `drawSkyTile` clear/cloud fill + leaf corners only at platform edges (fixes 31n postage-stamp leaf grid). NEW/FAIL 9/1 ~4:21am live BUILD 20260831o: climbed TREE 1–4; sky is solid blue tiled with a repeating small leaf-clump grid — not 31n Imagine clouds + leaf corners (`07-tree1-sky.webp`–`10-tree4-sky.webp`). TREETOP Imagine canopy PASS (`12-treetop-end.webp`). Floors otherwise OK (wood/grass pad, UP/DOWN, nest+3 eggs TREE 1, CHEST TREE 3). Local 8/31 BUILD 20260831n: `drawSkyTile` Imagine tile; 1:15am had code in bundle but floors UNTESTED. |
| Medium | Done 8/27 live | Giant-tree interiors look like house boards / growth rings | TREE 1–4 / TREETOP | Darren rejected 20260827d rings and 20260827e hollow cavity. FIXED 8/27 11pm live BUILD 20260827h: TREETOP is one unique Imagine canopy painting (thick branches / leaf clumps / sky gaps, mushroom + berry + DOWN; not 16×16 tile stamps). TREE 1–4 still sky/leaf platforms. Walked 40×30 canopy; forest DOWN chain still lands (25,10). Prior FIXED 8/27 8pm live BUILD 20260827f: climbed TREE 1–4 + TREETOP — floors read as sky platforms with wood rim/leaf heart (nest/bird visible); TREETOP then was the larger tiled canopy walk (islands + bridges). Stamp was `20260827f`. Local 8/27 BUILD 20260827f: TREE 1–4 use the old TREETOP draw path (sky tiles + woodfloor + leaf clearing, same 10×8 rooms, UP/DOWN + nest/bird/chest/shard kept). TREETOP is now a 40×30 canopy walk (branching wood among leaves, sky gaps, nest + silver glint + east view perch, one DOWN back to TREE 4). Camera clamps to the new map. Farm grass, Orion, DAY_MS, walk energy, START OVER untouched. |
| Low | Local 9/5 05ce | BAG 90-grid empty; goods only in tray | HUD / Bag | Local 9/5 BUILD 20260905ce: restore 30k empty-90 remirror (non-tool tray stacks shared into bag; hotbar stays; tools tray-only; mirror pickup clears aliases so 05be/05x swap stays FIXED). Autotest PASS locally — needs live. Was STILL 8/31 5:50am live BUILD 20260831a: 90-grid empty; tray holds stacks; no shovel (`10-bag-grid-no-shovel.webp`). UPDATE 8/31 2:19am live BUILD 20260831a: BAG top row lists tray stacks (seed / potato / berry / wood2 / stone2 / flower6 / mushroom7 / moon / flower3 / acorn2); remaining cells empty; tray still full (`04_bag_no_shovel.webp`). First live of 30k copy — kid can see owned stacks. No shovel. Local 8/30 BUILD 20260830k: if the 90-grid is empty and the tray has stacks, copy those stacks into the bag without emptying the tray (hotbar stays). BAG lists what you own. Do not mark Done until live. STILL 8/30 2:10pm live BUILD 20260830f: 90 empty cells + TRAY BELOW (`40-bag-open.png`). STILL 8/30 11:20am live BUILD 20260830c: 90 empty cells + TRAY BELOW (`11-bag-empty.png`). STILL 8/30 5:30am live BUILD 20260830a: 90 empty cells + TRAY BELOW (`14-bag-empty90.png`). NEW 8/29 11:30pm: BAG 15×6 empty while tray holds stacks (`17-bag.png`). Kid opens BAG and thinks inventory is empty. 29f said stacks migrate into the 90 — this save has them in the tray instead.
| Low | Local 9/5 05cg | HUD overlap; hotbar covers lower play field | HUD | Local 9/5 BUILD 20260905cg: CAM_PAD_BOTTOM 36→52 + forest south overscroll; mine south OUT gutter widened; hearts/DAY display-only (no tap swallow); sword pad kept fat 58. Needs live. Was 8/24 5pm: not re-scored. 8/24 11am: not re-scored. STILL + 8/24 5am: big sword button + hotbar cover ladders. 8/23 11pm: hearts/energy (top-left y≈140–190) and DAY panel (top-right) swallow taps. Hotbar y≈690 still swallows. 8/23 8pm live: hotbar y≈690 still swallows taps (toolbar grass/right-edge now walk). 8/23 5pm live: hotbar covers bottom ~1.5 tiles; header covered DOWN sign when walking under it in MINE 1. 8/23 midnight: covers MINE sign/hole and farmhouse door when low on screen, and covered a moon shard in MINE 1. 8/22 3pm: hotbar overlaps the lower play field and NPCs in the bottom rows. FX / MU / FS labels still sit on the playfield. Inset the playable rect or raise the camera pad further. |
| Low | Done 8/21 | Player hides behind the hotbar | Camera | Same as the south camera pad fix. 8/22 3pm reconfirm (Orion ~80px above hotbar). |
| Low | Local 9/5 | Closing a panel by tapping the world also walks | HUD | UPDATE 9/5 BUILD 20260905bc: world-tap dismiss sets ignoreWalkTap through pointerup, clears frozen path so Orion does not resume/start walk or tool-use on that press (bag/Jobs/Stars/talk/shop/craft/chest/notes/wipe). Jobs plaque taps stay on-panel; wipe outside = cancel. Live still needed. Was Open 8/21. Swallow the closing tap. 8/23 8pm: Esc dismiss works; tap-also-walks not retested. 8/23 5pm live: Esc/Space now close Jobs/Stars/NPC talk (tap-also-walks not retested). 8/22 3pm: Esc still closes nothing; dialogue is click-to-dismiss, panels only via toolbar button. |
| Low | Local 9/5 05ch | Moon shard / Mountain Heart missing from hotbar | Mine | Local 9/5 BUILD 20260905ch: tray pin + glowing SHARD→HOME / HEART→HOME chips; shard consumed on HOME GLOW; needs live. Was UPDATE 8/24 5pm: tapped gem → "A SHINY GEM" + inventory slot (pickup works). Hotbar badge / HOME GLOW carry not re-scored. Was STILL / worse 8/24 11am: teal gem visible in cave, no hotbar icon; could not pick up or mine (adjacent Space with pickaxe/stone no-op). Path also blocked by unmineable ore/dark blocks (see Medium). PARTIAL 8/24 5am: Mine 3 pickup "THE MOUNTAIN HEART, IT WILL GLOW ON THE HOME TABLE" — not in hotbar, no carry cue. Moon shard count-on-pickup still Done 8/23 midnight (not retested 5am): pickup showed 1; carrying into house triggered HOME GLOW and consumed it. 8/22 midnight: pickup credits the bag immediately so the hotbar badge reads 1 (was 0 until the fly-in finished, and the MOON PIECE toast paused that). Mine entered 11pm; shard pickup not re-checked. Mine not found 8pm. |
| Low | Local 9/5 05cl (Done sleep; clarify live TBD) | Bed advances the day with no prompt | House | Local 9/5 BUILD 20260905cl: floating SLEEP + Jobs + once TAP THE BED toast. Was 8/22 3pm: screen dim + "YOU SLEEP..." banner, then Day+1 morning. 8/23 midnight: fade not captured, may have flashed. House reached via death 11pm; bed not retested. House not found 8pm. |
| Low | Local 9/5 05cf | Tap-to-move silently fails for far targets | Overworld | Local 9/5 BUILD 20260905cf: soft blockers (chicken/critter/NPC/folk/dog/slug) path-around or walk-through+scoot; Junie not solid; far taps stepToward harden; door/chicken scoot kept. Needs live. Was Open — 8/24 11pm live: tap-to-move stalls when an NPC or animal is in the path. 8/24 5pm: surface reached; far-tap pathing not re-scored. 8/24 11am: surface taps not re-checked (stuck underground). 8/24 5am live: tap-to-walk dirt/grass OK. Residual: HUD overlays swallow taps (hearts/energy y≈140–190, DAY panel, hotbar y≈690, sword button — see HUD-overlap row). 8/23 11pm live: long taps past trees/rocks OK. 8/23 8pm live: many far taps walked. Twice a mid/far tap on open road ~6–7 tiles SW silent no-op (highlight, no move; arrows worked). Pathing still gives up when a rock/tree sits on the first step (keyboard still walks). Local 8/23 5pm BUILD 20260823h: walk partway toward blocked/far/out-of-bounds taps; farmhouse door from a few tiles paths to a walkable adjacent tile. 8/23 5pm live: far-east tap in MINE 1 no-op; arrows worked. |
| Low | Local 8/31 | Swing arc too short to read | Mine / HUD | Local 9/1 BUILD 20260831r: brighter crescent + 560ms swing (also Critical sword). Local 8/31 BUILD 20260831j: longer swing + wider slash window. Needs live. STILL 8/25 8am live: slot 8 + Space next to a tree — no swing anim, no wood drop. Mine not visited. STILL 8/25 5am live: sword swing unconfirmed. STILL 8/25 2am live: slot 8 + Space, no swing. STILL 8/24 11pm live: no visible swing. STILL 8/24 5pm live: no rainbow crescent seen; never caught a slash frame. Local 8/24 BUILD 20260824b: old 300ms slash sprite restored; big rainbow/white-gold crescent removed. 8/24 11am: still no swing anim. Space can still kill if hotbar selected (armadillo — see Critical). 8/24 5am: still no swing anim/hit flash. Space can still kill if hotbar selected (see Critical). 8/23 11pm live: no visible swing sprite at all (~8 swings). Subsumed by Critical sword. Was NEW 8/23 5pm: crescent slash real but too short to screenshot. Mine not reached 8pm. |
| Low | Done 8/25 live | Chest UI cosmetics | Forest N / HUD | FIXED 8/25 ~2pm live BUILD 20260825m: BAG/BOX + BACK look correct. Local 8/25 BUILD 20260825j: BACK moved to title badge row (no overlap); column headers BAG + BOX clear of BACK; bag counts shifted right so names do not clip. Do not mark Done until live. NEW 8/25 8am live. Column header reads "RAG" (bag?). BACK button overlaps the CHEST title/header row. |
| Low | Done 8/27 live | Mine N/S black void bands | Mine | FIXED 8/27 8pm live BUILD 20260827f: north at DOWN and south at OUT show cave floor (no black void band). LIVE BUNDLE 8/27 11am: clamp code is in 20260827b (mine minY=0 / maxY=worldH-VIEW_H). Was UNTESTED 8/27 11am. Local 8/27 BUILD 20260827b: mine camera clamps to the cave rect (no N/S black void). 8/24 5pm: deep floor seen; void bands not re-scored (fake-hole tile is its own Medium row). 8/24 11am: underground the whole pass; void bands not re-scored. 8/24 5am: Mine 3 entered; void bands not re-scored. 8/23 11pm: mine entered; void bands not re-scored. NEW 8/23 5pm live. Surface north now clamps clean; mine still has black void bands north and south. Clamp mine camera to the cave rect. Mine not found 8pm. |



## Local ship 9/3 BUILD 20260903a

- Pad kill: `startSwordSwing` applies hits immediately (arcHit true on press) so crescent + damage land together; `strikeDamage` always returns 4 for mine/pad/`via=swing` (no `player.arc > 0` gate). Bat/crystalbat swing reach 72 + Chebyshev≤2.
- Bat contact KO: flying foes use tight pixel radius only (no tile-neighbor drain); `hurtPlayer` i-frames 1200→2000; i-frame tick capped at 50ms/frame so lag cannot wipe protection.
- Sword tray: `forceSwordIntoTray` on load/migrate/giveTool — if `swordOwned`, sword must appear in the 10-tray (swap seed/hat/leash or last slot if tray is all tools). Mine pad still works without selecting it.
- Needs live (do not mark Done until playtest on live URL). Hard skips untouched.

## Local ship 9/2 BUILD 20260831t

- Pad kill damage: `strikeDamage` arc path (swordOwned or mine) always deals 4 — same as iron — so bats (6hp) and slimes (4hp) die in 1–2 pad taps without iron sword or tray sword.
- Pad-over-OUT: `tapHud` checks `hitSwordBtn` before MINE 1 OUT prefer; one-tap OUT kept for taps not on the round sword button.
- Contact i-frames: `hurtPlayer` iFrames 800→1200 (~1.2s) so a kid can swing after a bump; contact damage unchanged.
- Needs live (do not mark Done until playtest on live URL). Walk energy / day clock / START OVER / art / grass / evening color untouched.

## Local ship 9/2 BUILD 20260831s

- Sword pad: hit detection is omnidirectional — 8-neighbor tiles, reach 52, and tile Chebyshev ≤1 any facing (facing still aims the slash visual / nearest foe). Fixes 31r left-slime miss.
- Mine contact: bats/crystalbats (and all foes) use a wider bump radius so adjacent-tile overlap drains hearts; i-frames unchanged.
- Tray: placeToolInTrayFirst can force a tool into the 10-tray even when the 90-bag is full (merge/swap displaced non-tool).
- LIVE 9/2 ~2:34am: left/diagonal pad kill FIXED; pad crescent PASS; slime contact PASS; sword tray STILL miss; bat contact UNVERIFIED (driver crash).

## Local ship 9/1 BUILD 20260831r

- Sword pad: taps win over mine stairs/holes under the button; bright crescent slash; 560ms swing; reach 42; arc ticks during toasts; giveTool swaps owned sword into tray.
- MINE 2→6 skip: no clear one-line cause in floor code — left alone.
- LIVE 9/1 ~7:40pm: pad swing + adjacent kill FIXED; pad vs stairs PASS; tray sword still missing; Space+hotbar UNTESTED; contact damage miss on MINE 1 this pass.

## Live playtest 9/2 ~1:06–2:34am PT (BUILD 20260831s)

- Continued box Chrome save Day 1540 SPRING NIGHT→1543 EVENING (~12+ min wall) — never START OVER. Served BUILD `20260831s` (cache-bust `?v=pt0106`; in-page BUILD). Farm/overworld → MINE 1 (MINE 2 not reached). Hearts 5→2, 17G unchanged. Tray: seed/potato/berry/wood×2/stone×2/empty/mushroom×8/moonshard/berry×3/acorn×2 — **no sword** (`swordEquipped:false`, strike pad on).
- **FIXED (was 10:22pm NEW facing miss):** left/diagonal pad hits connect — slime down-left of Orion flashed white on tap #1, gone by #2 while Orion faced left/right (`21-mine1-slime-diagonal-before.png`, `23`–`25-left-slime-killed-by-pad.png`).
- **PASS:** fat-finger sword pad crescent every tap (`22-pad-crescent-swing.png`); slime contact still drains (5→2).
- **STILL:** sword not in 10-tray / pad-only (`02-bag-tray.png`, `03b-tray-close.png`, `20-mine1-arrive.png`).
- **UNVERIFIED:** bat contact widen — hover one tile away no drain; exact overlap aborted when browser driver crashed. Treat bat contact as still Needs live.
- **Note:** earlier-pass "pad ejects to house" did NOT recur on the successful MINE 1 combat stretch.
- Kid-fun: pad shows a tiny glowing ring + "POW!" star on the foe it actually hit so Orion sees which direction connected.
- Screenshots `/workspace/playtest-0106/`.

## Live playtest 9/1 ~10:22pm PT (BUILD 20260831r)

- Continued box Chrome save Day 1258 SPRING AFTERNOON→1259 AFTERNOON (~12 min) — never START OVER. Served BUILD `20260831r` (cache-bust `?v=pt2212`; Jobs BUILD under STARS). Farm spawn at MINE sign; one-tap enter MINE 1 → DOWN MINE 2 → UP back. Hearts 5→2, 0G→4G. Tray/BAG: crops/rocks/mushrooms/moon item — **no sword**.
- **PASS (kill + loot):** fat-finger sword pad kills — bat above dropped coin (`05-bat-kill-coin.webp`); slime below dropped ore. Crescent too brief for a still.
- **NEW:** swing is facing/direction-limited — slime to Orion's LEFT survived 5+ pad taps while up/down foes died in 1–2 (`07-slime-survives-left-swings.webp`).
- **FIXED (vs 7:40pm miss):** MINE 2 slime contact damage 5→4→3→2 (`06-slime-contact-damage-3of5.webp`).
- **NEW:** MINE 1 bats deal **zero** contact even after 4+ s overlap (`03-bats-adjacent-hearts-full.webp`) — bat contact FAIL (slime contact OK).
- **STILL:** sword not in 10-tray (`04-bag-no-sword.webp`); pad-only. Pad vs DOWN/UP/OUT PASS. Clock STILL races (~1 phase / 30–60s). START OVER still under Jobs. Faint UNTESTED (stalled at 2/5).
- Kid-fun: killed bats drop a tiny glowing moon-coin that pings so Orion hunts them for treasure.
- Screenshots `/workspace/playtest-2212/`.

## Live playtest 9/1 ~7:40pm PT (BUILD 20260831r)

- Continued box Chrome save Day 1244 SPRING AFTERNOON→1246 EVENING (~3 min light play) — never START OVER. Served BUILD `20260831r` (cache-bust `?v=pt1913`; Jobs BUILD line below STARS list). Spawned MINE 1; OUT one-tap to overworld MINE sign. Hearts 5/5 whole pass, 0G. Tray: seeds/stone/berry/wood 4/stone 2/mushrooms/moon piece/flower (no sword).
- **FIXED (was 4:46pm inert pad):** fat-finger sword pad swings — bright crescent arc ~0.5s (`11-swing.png`, `12-mine1-sword-tray.png`). Pad taps did not trigger stairs/holes under the button.
- **FIXED / Partial:** adjacent snail on MINE 1 **killed** (vanished). Slime at range/diagonal ignored until adjacent+facing. **No** hit flash, HP pips, or loot — reads as monster vanish (`14-after-swings.png`).
- **STILL:** sword not in 10-tray (pad-only; giveTool swap UNVERIFIED despite full non-tool tray).
- **WORSE / miss this pass:** contact damage on MINE 1 — stood by slime+snail many times, hearts stayed 5/5 (4:46pm bat KO on MINE 6 was FIXED; may be floor-specific).
- **STILL PASS:** MINE 1 place stamp; OUT one-tap (`15-exit-mine-overworld.png`). Clock STILL races hard (phase often advances on a single step). START OVER still under Jobs. Esc closes Jobs.
- Kid-fun: slime splits into two tiny hoppers then goo pickup; white flash+shrink per hit; sword as tray slot 1 so the pad shows the weapon.
- Screenshots `/workspace/playtest-1913/`.

## Live playtest 9/1 ~4:46pm PT (BUILD 20260831q)

- Continued box Chrome save Day 1747 SPRING NIGHT→1748 MORNING (~20 min) — never START OVER. Jobs/orionTest BUILD `20260831q` (cache-bust `?v=pt1622`). Route: MINE 1 → MINE 2 → MINE 6 → house bed → farm. Started ~1 heart / 0G; ended 5/5 hearts / 0G.
- **FIXED (was 1:07pm WORSE):** mine **contact damage** works — walking into purple bat on MINE 6 fired `THE MOUNTAIN SENT YOU HOME.` → woke in bed, hearts 5/5, day advanced (`04-mine6-bat-swordpad.webp`, `05-sent-home-after-bat.webp`, `06-home-full-hearts.webp`). Hit size unclear (was ~1 heart).
- **Enemy spawn note:** MINE 1 and MINE 2 had no slime/bat this pass; bat appeared on MINE 6 after arrival.
- **STILL / WORSE feel:** fat-finger sword pad on MINE 6 showed **no swing arc** on tap; could not verify damaging foes before the KO (pad-only, not in tray).
- **Possibly NEW:** down-stairs from MINE 2 landed on **MINE 6** (skipped 3–5) with a night→next-morning clock jump during the transition.
- **STILL PASS / known:** mine place stamps present; farm/house OK after revive; clock races; START OVER still under Jobs. PEAK cave-down / town cart / TREE sky UNTESTED this pass.
- Kid-fun: when the mountain sends you home, dog wakes Orion with a lick + one "get well" berry by the bed.
- Screenshots `/workspace/playtest-1622/`.

## Live playtest 9/1 ~1:07pm PT (BUILD 20260831q)

- Continued box Chrome save Day 890 SPRING NIGHT→891 NIGHT (~45 min wall; clock raced Morning→Afternoon→Evening→Night in ~5 min) — never START OVER. orionTest.BUILD `20260831q` (cache-bust `?v=pt1307`). Maps: woods/mine-entrance overland, MINE 1–2, town, Pip shop, tree/treetop. 5 hearts, 0G.
- **PASS (was UNTESTED):** MINE door → `MINE 1` stamp (`13-mine-banner.png`, `15-mine1-stamp-altar.png`); DOWN pit → `MINE 2` stamp + UP ladder (`18-mine1-down-hole.png`, `19-mine2-stamp.png`); fat-finger sword pad draws + swings on mine floors (`16-mine1-sword-swing.png`) — sword not in 10-tray (pad-only). Jobs `KICK THE CART IN TOWN.` + town cart kick PASS (`07-jobs-cart-build.png`).
- **NEW/WORSE:** green slime + purple bat on MINE 1/2 never chase or react; sword-pad swings near them do nothing; no contact damage (`17-mine1-slime-north.png`, `20-mine-enemies-no-chase.png`). Mine combat reads as scenery.
- **Low-confidence:** after MINE 2, sword-pad taps + near-pit tap returned to MINE 1 without a clear UP (possible pit re-trigger).
- **STILL PASS:** TREE 1–4 sky / TREETOP / Stars. Clock STILL races. START OVER still in Jobs. PEAK cave-down / sword-tray swap UNTESTED this pass.
- Kid-fun: slimes/bats should hop toward Orion and pop into 1–2 goo/wing pickups when the sword pad hits.
- Screenshots `/workspace/playtest-1307/`.

## Live playtest 9/1 ~10:25am PT (BUILD 20260831q)

- Continued box Chrome save Day 1700 SPRING Afternoon→Night (~8 min) — never START OVER. orionTest.BUILD `20260831q` (cache-bust `?v=pt1025`). Spawned PEAK; hopped TREE 1–4 / TREETOP / OCEAN. 1 heart, 0G.
- **FIXED:** TREE 1–4 sky — quiet mottled blue, tiny cloud wisps, leaf clusters only hugging the wood (`01-tree1.png`, `02-tree2.png`, `03-tree3.png`, `04-tree4.png`). 4× sky zoom is low-contrast blue speckle with no repeating leaf grid and no hashed/cross-hatch clouds (`04-sky-zoom.png`). Floors otherwise OK (wood/grass pad, UP/DOWN, nest+3 eggs TREE 1, CHEST TREE 3, moon piece TREE 4).
- **STILL PASS:** TREETOP Imagine canopy (`05-treetop.png`); ocean east foam/deep water unwalkable (`06-ocean.png`, `07-ocean-east.png`); gold Star list opens/scrolls/closes (`08-stars.png`).
- Jobs CART / MINE N stamp / PEAK cave-down / sword-tray swap / town kick UNTESTED this pass (Jobs skipped: START OVER sits under the stamp).
- Clock STILL races (Afternoon→Night in-session). START OVER still in Jobs under RELOAD/MUTE + stamp.
- Screenshots `/workspace/playtest-1025/`.

## Live playtest 9/1 ~4:21am PT (BUILD 20260831o)

- Continued box Chrome save Day 1254→1256 SPRING (~10 min) — never START OVER. Jobs shows `20260831o` (cache-bust `?v=pt0421`). Spawned OCEAN; ended TREETOP. 5 hearts, 0G.
- **NEW/FAIL:** TREE 1–4 sky still the old flat blue fill with a repeating small leaf-clump grid — not the 31n Imagine clouds + leaf corners (`07-tree1-sky.webp`, `08-tree2-sky.webp`, `09-tree3-sky.webp`, `10-tree4-sky.webp`). Floors otherwise OK (wood/grass pad, UP/DOWN, nest+3 eggs TREE 1, CHEST TREE 3). **TREETOP** Imagine canopy PASS (`12-treetop-end.webp`). Bird still `MY NEST NEEDS 10 WOOD PLEASE.` (wood 4 so give UNTESTED).
- **FIXED:** gold Star on OCEAN opens STARS list (CAVE DOOR … SHOP GLOW, X closes) — 1:15am no-response gone (`05-stars-ocean.webp`).
- **STILL PASS:** ocean east foam/deep water unwalkable (`04-ocean-foam-blocked.webp`); tap-to-walk; Jobs `KICK THE CART IN TOWN.` (`02-jobs.webp`).
- MINE N stamp / PEAK cave-down / sword-tray swap / town kick UNTESTED this pass.
- Clock STILL races (Morning→Night within ~10 min). START OVER still in Jobs under RELOAD/MUTE + stamp.
- Screenshots `/workspace/playtest-0421/`.

## Live playtest 9/1 ~1:15am PT (BUILD 20260831o)

- Continued box Chrome save Day 1234→1235 SPRING (~30 min) — never START OVER. Jobs shows `20260831o` (cache-bust `?v=pt0115`). First live of 31n/31o. Spawned overland near TOWN; ended OCEAN. 5 hearts, 0G.
- **FIXED:** ocean east foam / deep water unwalkable — stopped at foam line col 30; cols 31–32 blocked on rows 8–20 (`06-ocean-east-edge.webp`, `07-ocean-deep-water-blocked.webp`).
- **FIXED:** Jobs kick text reads CART (`03-jobs-20260831o-cart.webp`). Town kick cart PASS.
- **PASS:** tap-to-walk town+ocean beach; grass→sand→foam Imagine transition bands.
- Sword-tray swap UNTESTED (sword not owned this save). PEAK cave-down / MINE N stamp / TREE 31n sky UNTESTED (overland spawn; `drawSkyTile` present in bundle).
- **NEW minor:** Star button no visible response on OCEAN.
- Clock STILL races. START OVER still in Jobs under RELOAD/MUTE + stamp.
- Screenshots `/workspace/playtest-0115/`.

## Live playtest 8/31 ~10:20pm PT (BUILD 20260831m)

- Continued box Chrome save Day 1609 SPRING NIGHT (~4 min) — never START OVER. Jobs shows `20260831m` (cache-bust `?v=pt2215`). First live of 31k/l/m. Spawned outdoor PEAK. 1 heart, 0G.
- **FIXED:** peak cave-down (5:20pm 31j stranded) — click-to-walk south onto the painted cave arch loaded STAIRS 2; DOWN → STAIRS 1 → MINE stairs → moon-altar floor with PEAK/UP (`03-cave-arch.webp`, `04-after-cave-stairs2.webp`, `05-stairs1.webp`, `06-mine-moon-altar.webp`). No Space needed.
- **PASS:** mine altar floor shows the fat-finger sword strike button (lower-left). Sword still not in the 10-tray; BAG/PEAK slash UNTESTED.
- **STILL FIXED:** tap-to-walk on PEAK path.
- **UNTESTED:** ocean 31l/31m tiles (cave-down first). Farm/town this pass UNTESTED.
- **NEW nit:** no location banner on the altar floor.
- START OVER still in Jobs under RELOAD/MUTE + stamp (`02-jobs.webp`).
- Screenshots `/workspace/playtest-2215/`.

## Local ship 8/30 ~11:06am PT (BUILD 20260830c)

- Bigger unique Imagine paintings for Pip's shop, the tall cottage, and the L-shaped town house (`assets/props/shopHouse.png`, `townHouseA.png`, `townHouseB.png`). Farm house and Orion untouched.
- LIVE 11:20am: paintings look good; Pip shop door FAIL (see High row). Household save intact. Never START OVER.

## Live playtest 8/30 5:20pm PT (BUILD 20260830h)

- Continued box Chrome save Day 1372 Evening→1377 Night (~12 min) — never START OVER. Jobs shows `20260830h` (cache-bust `?v=pt1716`). First live of 30g/30h.
- **FIXED:** Pip shop door TAP from a couple tiles away entered PIP'S SHOP (Pip at counter, BUY/BYE, prices SEED TIN 5G … FISHING POLE 30G) (`11-door-tap.png`, `12-shop-interior.png`, `12b-shop-buylist.png`). Doormat one-tap exit. East-of-door roof tap walked (no enter, no BEEP) (`14-east-door-tap.png`). Truck BEEP UNTESTED.
- **FIXED:** TREE 1 nest `THE MAMA BIRD IS UP TOP.` (3 eggs stay) (`20-tree1-nest.png`); TREETOP enter `BIRD — MY NEST NEEDS 10 WOOD PLEASE.` (`21-treetop-enter-bird-talk.png`). Wood 2 so give/rides UNTESTED; bird sprite not visible after dismiss (`22-treetop-after-dialog-no-bird-visible.png`).
- Farmhouse door / Lila / mine OUT / Stars X UNTESTED this pass. Clock STILL races (1372→1377 / ~12 min). 0G, wood 2.
- Screenshots `/workspace/playtest-1716/`.

## Local ship 8/30 ~afternoon–5:20pm PT (BUILD 20260830g / 20260830h)

- 30g: giant bird flies in on first TREETOP enter; TREE 1 nest points up.
- 30h: Pip shop door tap enters immediately; truck body still BEEP.
- LIVE 5:20pm: door TAP FIXED; TREETOP bird talk FIXED; bird sprite not seen; 10-wood give UNTESTED.
- Farm grass, Orion, DAY_MS, walk energy, START OVER untouched.

## Local ship 8/30 ~9:55pm PT (BUILD 20260830k)

- Day clock DAY_MS 150000 to 480000 (~8 real minutes per in-game day). PHASE_MS still DAY_MS/4. Crop/node formulas unchanged. Existing saves keep dayNumber and land in morning.
- Jobs START OVER is smaller and sits under RELOAD/MUTE and the BUILD stamp. wipeAsk REALLY START OVER? kept. Never auto-confirm.
- BAG: tray is the hotbar; if the 90-grid is empty, copy tray stacks into it without emptying the tray so BAG lists what you own.
- Household save intact. Never START OVER.

## Local ship 8/30 ~9:50pm PT (BUILD 20260830j)

- 22 extra pine, oak, and birch among the existing woods. North-south dirt road (cols 13-15), giant-tree door (25,8), and south FARM exit stay clear. Walkable gaps left. No new art.
- Household save intact. Never START OVER.

## Local ship 8/30 ~6pm PT (BUILD 20260830i)

- Bird PEAK stop now lands on a snowy outdoor peak (40x30 painting) instead of mine floor 6. Dirt balcony + winding path; fallen rocks block the summit (`FALLEN ROCKS.` / `THE PATH IS BLOCKED.`).
- Mine 6 keeps the moon altar; a distinct UP staircase + PEAK sign on the east of the north chamber climbs into new `caveclimb` floors 1–2 (not mine 7–8). Floor 2 bright mouth opens onto the peak balcony.
- Leave the peak by walking back into the cave mouth. Climb/peak persist additively (`climbFloor`, scene whitelist). Farm grass, Orion, DAY_MS, walk energy, START OVER untouched.
- LIVE 8:40pm: peak climb PASS; bird sprite FIXED visible. Bird PEAK ride still UNTESTED.

## Live playtest 8/30 11:20pm PT (BUILD 20260830u)

- Continued box Chrome save — never START OVER. Spawned WOODS, Day 1372 SPRING MORNING, 5 hearts, 0G, populated STARS. Jobs stamp `20260830u` (cache-bust `?v=20260830u&r=2`).
- **FIXED:** game boots. World + HUD visible (`01-land.png`). 11:05pm 30t black canvas / SyntaxError gone.
- **CACHE:** first `?v=20260830u` still served the old 30t bundle (flat green canvas, no HUD). Second distinct param was required for Pages to pick up 30u.
- Ocean enter/exit + boat talk UNTESTED (woods spawn; long trek skipped).
- 30j–30t features still UNTESTED. Clock still advanced Morning→Night in this short pass (day-clock row stays Open).
- Screenshots `/workspace/playtest-2315/`.

## Local ship 8/31 ~1:20am PT (BUILD 20260831a)

- Shovel farm walk restored: shovel no longer tills every farm grass tile (that stole tap-to-walk).
- Woods 7 marked mounds kept unchanged.
- Farm holes still Open. Household save intact. Never START OVER.
- LIVE 2:19am: first live boots; shovel-walk UNTESTED (no shovel in this save).

## Live playtest 8/31 ~5:50am PT (BUILD 20260831a)

- Continued box Chrome save — never START OVER. Day 1418 SPRING MORNING → 1421 (~25 min), 5 hearts, 0G. Cache-bust `?v=pt0520` (address bar rewrote to `?v=20260830u`; served BUILD still 31a).
- **STILL boots.** World + HUD visible. Farmhouse enter/exit PASS. Junie `LANTERNS FOR TOWN. THANKS AGAIN! CHECK YOUR MAIL.` PASS.
- **NEW BUG:** walk on open ocean water past the surf (`07-walking-on-open-water.webp`, `11-deep-water-walk-bug.webp`).
- **NEW/PASS:** dock boats visible (5+ rowboats + sailboat) — decor only, no ride. Ocean enter/exit STILL PASS.
- **NEW/PASS:** town kick — Space by red cart south of fountain `KICK!` + slide (`18-kick-works.webp`); Jobs still says ball.
- **NEW/PASS:** MARKET DAY banner on day rollover (`19-market-day.webp`).
- **NEW cosmetic:** ocean night tint washes cove + player then snaps bright (`08-water-walk-night-lighting-mismatch.webp`).
- **STILL UNTESTED:** 31a shovel-walk (no shovel in tray/BAG, `10-bag-grid-no-shovel.webp`). Clock STILL races (phase ~15–25s).
- Screenshots `/workspace/playtest-0520/`.

## Live playtest 8/31 ~2:19am PT (BUILD 20260831a)

- Continued box Chrome save — never START OVER. Spawned farm (north woods-edge strip → farmhouse south). Day 1395 SPRING EVENING → 1396 MORNING, 5 hearts, 0G. Jobs stamp `20260831a` (cache-bust `?v=pt0219`). First live of 31a.
- **STILL boots.** World + HUD visible on first load. 30t black canvas stays gone.
- **NEW/PASS:** OCEAN sign south of farmhouse walk-in loads coastal path (`06_ocean_sign.webp`, `07_ocean_scene.webp`). Boats not on first screen.
- **UNTESTED:** 31a shovel-walk — tray/BAG have no shovel (`04_bag_no_shovel.webp`). Untooled grass taps still WALK (no stray till).
- Jobs still `KICK THE BALL IN TOWN.` Clock STILL races (Evening→Night ~30s). START OVER untouched.
- Screenshots `/workspace/playtest-0219/`.

## Live playtest 8/30 11:05pm PT (BUILD 20260830t)

- Attempted continued box Chrome save — never START OVER. Live stamp `20260830t` (cache-bust `?v=pt2305` / `pt2305b`). First live after 30i; ships 30j–30t are on GitHub Pages.
- **WORSE / BLOCKED:** game does not boot. Title + green frame + sound/music/fullscreen/reload chrome render; 320×192 canvas is solid black. Inline script SyntaxError at parse time (`Unexpected ")"` at final `})();`). Root cause from served page: in `tryTalkAdjacent()`, the `else if (currentScene === "ocean")` / `talkBoat()` branch (ocean/rowboat ~30l) is missing its closing `}` before `return false;`, unbalancing the IIFE. No HUD, no save load, no JS globals. Household localStorage untouched.
- All probes UNTESTED (clock 30k, denser woods 30j, ocean/cove 30l, river bridge 30m, Luna/Maple houses 30n, dog/leash 30o, Pip kits/seeds 30p–q, holidays 30r, kick ball 30s, mine decor 30t, shovel-dirt walk, bird wood/rides).
- vs 8:40pm 30i: catastrophic regression (30i booted and was playable).
- Notes `/workspace/playtest-2305/00-BLOCKED-README.txt`. Hotfix missing brace, re-ship, re-playtest.

## Live playtest 8/30 8:40pm PT (BUILD 20260830i)

- Continued box Chrome save Day 1438 Morning→1453 Afternoon (~40 min) — never START OVER. Jobs shows `20260830i` (cache-bust `?v=pt2001`). First live of 30i. Spawned TREETOP.
- **FIXED:** TREETOP giant bird sprite visible on the west nest branch (`32-giant-bird-visible.png`); still there after `MY NEST NEEDS 10 WOOD PLEASE.` (`33-bird-dialog.png`, `34-bird-after-dialog.png`). 5:20pm 30h talk-without-sprite gone. Wood 2 so give/rides UNTESTED.
- **NEW/PASS:** MINE 1–6 DOWN → PEAK+UP stairs east of moon altar → STAIRS 1–2 → outdoor PEAK (`58-peak.webp`). Summit `FALLEN ROCKS.` / `THE PATH IS BLOCKED.` (`59-peak-rocks.webp`).
- Clock STILL races (1438→1453). 0G, wood 2, ended 1/5 hearts (mine contact). Pip truck / farmhouse this pass UNTESTED.
- Screenshots `/workspace/playtest-2001/`.

## Live playtest 8/30 2:10pm PT (BUILD 20260830f)

- Continued box Chrome save Day 1297 Afternoon→1301 Morning (~8 min) — never START OVER. Jobs shows `20260830f` (cache-bust `?v=pt1404`). First live of 30e/30f.
- **FIXED:** Pip shop walk-in from south stoop/door entered PIP'S SHOP (Pip at counter, BUY/BYE, prices SEED TIN 5G … FISHING POLE 30G) (`08-shop-interior.png`, `65-pip-shop-ui.png`).
- **NEW:** kid taps on door (43,26)/(43,25) still miss; east (44,26) still `CAR / BEEP` (`60-door-door-e.png`).
- **NEW:** nest on TREE 1 (3,4) with 3 eggs that stay; giant bird never landed after ~10s adjacent; no 10-wood talk/star/rides (`74-nest-wait-9s.png`). Small TREE 2 bird no talk.
- Mine 1 OUT one-tap STILL FIXED (`33-mine-out-tap1.png`). Farmhouse door/doormat/path E/W STILL FIXED. Lila tap talk PASS.
- Sword STILL mine-only. BAG 15×6 empty + TRAY BELOW STILL. Clock STILL races (1297→1301 / ~8 min). 0G, wood 2.
- Screenshots `/workspace/playtest-1404/`.

## Local ship 8/30 ~11:30–11:45am PT (BUILD 20260830e / 20260830f)

- 30e: Pip shop door taps enter instead of beeping the car.
- 30f: TREE 1 nest bird — 3 eggs stay; giant bird should land nearby, ask 10 wood, grant a star, then offer rides (tree/home/town/cave/peak).
- LIVE 2:10pm: shop walk-in FIXED, some taps still BEEP; nest+eggs PASS, giant bird never landed.
- Farm grass, Orion, DAY_MS, walk energy, START OVER untouched.

## Live playtest 8/30 11:20am PT (BUILD 20260830c)

- Continued box Chrome save Day 1226 Afternoon→1230 Afternoon (~12 min) — never START OVER. Jobs shows `20260830c` (cache-bust `?v=pt1108`). First live of 30c (includes 30b).
- **FIXED:** Mine 1 OUT one-tap (5:30am fiddly gone) — farm at MINE sign (`10-mine-out-onetap-farm.png`).
- **FIXED:** BUILD chip fence place — walk without chip (wood 4); chip on then grass, wood 4→2 (`06-build-chip-before.png`, `07-fence-placed-wood2.png`).
- **NEW:** unique multi-tile Pip shop / tall cottage / L-house paintings (`03-town-buildings.png`).
- **NEW/FAIL:** Pip's shop door dead — facade/door taps no-op; truck `CAR / BEEP`; no interior / no Pip (regression vs 8:14am 30a).
- Tall cottage knock-only PASS. Farmhouse door/doormat/path E STILL FIXED. Lila tap talk PASS. Stars X STILL FIXED.
- Sword STILL mine-only. BAG 15×6 empty + TRAY BELOW STILL. Clock STILL races (4 days / ~12 min). 0G. Woods UNTESTED.
- Screenshots `/workspace/playtest-1108/`.

## Local ship 8/30 ~9:20am PT (BUILD 20260830b)

- Mine OUT: fat-finger pad is 5×5 around portalOut; pixel rect covers OUT label + south hotbar-covered rungs. tapHud prefers OUT over sword/hotbar. goWalk to isMineExit/mineExitHit exits immediately. Space/E tryClimbShaft + arrive() walk-on OUT kept.
- BUILD place: soft flora (tallGrass/weed/wildflower) no longer blocks canBuildOn; BUILD-on taps place before cut-grass steal; goBuild returns success so failed paths fall through to walk. Wood-select without BUILD still walks only.
- Sword tray: placeToolInTrayFirst moves a bag-only owned tool into the tray on load (was skipping when bagCount>0).
- Farm grass PNGs, Orion art, DAY_MS/PHASE_MS, walk energy, START OVER, evening color, canopy +64 sort untouched.
- Needs live: one-tap MINE 1 OUT (even under sword btn/hotbar); BUILD-on + wood places fence on grass (wood drops by 2); wood-select without BUILD still walks.

## Local ship 8/30 ~1:20am PT (BUILD 20260830a)

- Stars panel: the X and the header chrome (title row above the list) close the panel, same as Esc. List drag/wheel still scrolls. Taps on the list do not close.
- Town/farm folk freeze while Orion is adjacent — including mid-step tiles — so they do not walk off before Space. Facing is not required to freeze.
- Space/tap talk opens the dialog when adjacent or when the NPC is mid-step onto an adjacent tile. It no longer starts a walk-to-talk miss.
- Farm grass, Orion, DAY_MS, walk energy, START OVER untouched.
- LIVE 2:03am: Stars X FIXED; Junie adjacent Space talk FIXED.

## Local ship 8/29 ~9:20am PT (BUILD 20260829b)

- One tap on the MINE 1 OUT ladder, the OUT label, or the fat-finger zone now leaves the mine immediately (exitMine, no walk-to-tile). Space/E/J on the tile or facing OUT does the same. Walking onto OUT still exits. MINE 2+ UP/DOWN still climb. Farm drop is still (37, 7) facing down.
- Farm grass, Orion, DAY_MS, walk energy, START OVER untouched.
- Needs live: one tap on OUT / label from a couple tiles away; Space facing the ladder; deeper floors still climb. LIVE FAIL 8/29 11am: stamp 29b, OUT still ~5–6 taps (each only one tile).

## Local ship 8/29 ~1:25am PT (BUILD 20260829a)

- Wood selected no longer turns walk taps into silent fences. Taps still walk. A BUILD chip sits above the hotbar (or tap the wood slot again) to place a fence from wood; tap BUILD again to walk. Far grass/path taps never spend wood unless BUILD is on.
- Farm grass, Orion, DAY_MS, walk energy, START OVER untouched.
- Needs live: mis-tap wood then walk (count must not drop); BUILD still places a fence.

## Local ship 8/28 ~9:20pm PT (BUILD 20260828f)

- TREETOP walkable tiles now follow the Imagine canopy painting: wood/leaf branch paths only. Sky, empty air, and off-branch foliage are solid.
- South stairs at the bottom of the painting are a WOODS walk-off to the forest, landing at (25,12) a bit south of the giant trunk (door stays 25,8). The existing DOWN hole still climbs down to TREE 4.
- Farm grass, Orion, DAY_MS, walk energy, START OVER untouched.
- Needs live: walk the canopy without stepping on sky; south path to woods; DOWN still to TREE 4.

## Local ship 8/28 ~9:10pm PT (BUILD 20260828e)

- House/woods chest: BAG + BOX list is clipped to the panel and scrolls so every stack is reachable. Wheel over the list, drag the rows, or use the scrollbar track (same idea as Stars). PUT ALL / TAKE ALL / BACK stay. A tap on a row still puts or takes; drag/scroll does not walk.
- Farm grass, Orion, DAY_MS, walk energy, START OVER untouched.
- Needs live: open a full chest and scroll to the last row (POTATO / BERRY).

## Live playtest 8/30 5:30am PT (BUILD 20260830a)

- Continued box Chrome save Day 1089 Afternoon→1092 Afternoon (~12–15 min) — never START OVER. Jobs shows `20260830a` (URL `?v=20260829m`; cache-bust `?v=pt0502`). Same ship as 2:03am.
- **FOUND:** Mine entrance — MINE sign + walk-in hole on the grass path NE/above the farm after OUT (`12-mine-entrance-out.png`). Clears 2am miss.
- **NEW/UPDATE sword:** MINE 1 large on-screen sword button + sword item on floor; overworld still crescent-only, Space on grass no slash / no farm button.
- **WORSE:** Mine OUT ladder fiddly again (several taps/steps) — reopens 11pm 29m one-tap Done → Partial.
- Stars X **STILL FIXED**. Lila adjacent Space talk **PASS** (statue flower quest). BAG 15×6 empty + TRAY BELOW **STILL**.
- Clock **STILL** races (3 days / ~15 min). 0G. No fishing pole. Farmhouse/chest UNTESTED (spawned in Mine 1). Pip UNTESTED.
- Woods: Orion partly under canopy again — canopy Partial still.
- Screenshots `/workspace/playtest-0502/`.

## Live playtest 8/30 2:03am PT (BUILD 20260830a)

- Continued box Chrome save Day 1010 Evening→1012 Afternoon (~14 min) — never START OVER. Jobs shows `20260830a` (cache-bust `?v=pt0203`). First live of 30a.
- **FIXED:** Stars X closes the panel.
- **FIXED:** Junie adjacent Space talk (froze; `THANKS AGAIN! CHECK YOUR MAIL.`).
- Farmhouse door one-tap / doormat exit / path E/W STILL FIXED. Chest PUT ALL/TAKE ALL STILL FIXED. Spawn walkable STILL FIXED.
- BAG 15×6 still empty while tray holds stacks. Sword ABSENT (crescent only; Space no swing). 0G.
- Mine entrance NOT FOUND on NE/town/east-cliff sweep — OUT UNTESTED.
- Clock STILL races (2 days / ~14 min; EVENING→NIGHT ~90s).
- Woods: Orion in front of canopies this pass (no hide) — canopy Partial not closed.
- Screenshots `/workspace/playtest-0203/`.

## Live playtest 8/29 11:30pm PT (BUILD 20260829m)

- Continued household save on the live URL (Day 939 Night→950 Night) — never START OVER. Jobs shows `20260829m` (cache-bust `?v=pt2301`). ~11 min. First live of 29m unstick.
- **FIXED:** overworld spawn-lock / no-op movement (8:15pm Critical). Loaded in farmhouse, not (63,39). Arrows/WASD/tap-to-move all walk.
- Farmhouse door / doormat exit / path E/W **STILL FIXED**. Chest PUT ALL / TAKE ALL **STILL FIXED**. Junie Space talk **PASS**.
- **FIXED:** Mine 1 OUT one-tap (was 5–6 taps). Left at MINE sign.
- **NEW minor:** BAG 15×6 grid empty while tray holds stacks (`17-bag.png`). Nim not at the well this pass.
- Clock **STILL** races (939→950 in ~31 min). Sword **ABSENT** STILL (crescent in tray). 0G. No fishing pole. Pip/town UNTESTED.
- Screenshots `/workspace/playtest-2301/`.

## Live playtest 8/29 8:15pm PT (BUILD 20260829l)

- Continued household save on the live URL (Day 869 Morning→872 Night) — never START OVER. Jobs shows `202608291` / runtime `20260829l` (cache-bust `?v=pt2004`/`pt2004b`). ~10 min. First live of 29h–29l (rim scenery, stumps/acorns, tall fences, big town car).
- **NEW Critical:** Orion spawn-locked at overworld (63,39) — tile + neighbors unwalkable; no movement; reload keeps bad position. Likely rim scenery made rim solid under save. Farmhouse/chest/NPC/mine/Pip/BUILD/fishing **UNTESTED** (unreachable).
- BAG 15×6 + TRAY BELOW **STILL** opens; Esc closes Jobs/Stars/BAG.
- Clock **STILL** races — quantified `PHASE_MS=37500` → 150 s/day.
- Sword **ABSENT** STILL (`swordEquipped` false; crescent in tray). 0G. No fishing pole.
- Screenshots `/workspace/playtest-2004/`.

## Live playtest 8/29 5:20pm PT (BUILD 20260829g)

- Continued household save on the live URL (Day 1079 Evening→1083 Morning) — never START OVER. Jobs shows `20260829g` (cache-bust `?v=pt1719`). ~12 min. First live of 29f/29g.
- FIXED: TAKE ALL after PUT ALL returned WOOD/STONE/FLOWER/MUSHROOM/SHARD BOX→BAG.
- FIXED/confirmed: hotbar BAG + TRAY BELOW (29f).
- Door enter/exit one-tap STILL FIXED. Chest open STILL OK. Nim bump-talk OK.
- STILL: adjacent+facing Space NPC talk miss (town + farm). Clock races. Sword absent. Town knock houses + 0G.
- UNTESTED: BUILD place, mine OUT, fishing, canopy, Pip.
- Screenshots `/workspace/playtest-1719/`.

## Live playtest 8/29 2pm PT (BUILD 20260829d)

- Continued household save on the live URL (Day 1008 Afternoon→1010 Night) — never START OVER. HUD stamp gone; Jobs shows `20260829d` (cache-bust `?v=pt1420`). ~17 min. First live of 29c/29d.
- Jobs BUILD stamp **PASS** (29c move off HUD verified).
- Farmhouse door **FIXED** — one tap from path south entered; one-tap doormat exit; path E/W after exit **0 bounce**.
- Chest open **STILL OK** (bump/facing). **TAKE ALL STILL broken**; **NEW:** tapping BOX cell on a row retrieves (SHARD BOX→BAG) — button only.
- BUILD place **STILL** silent-fail (chip on; grass walks; wood stayed 4).
- **Sword ABSENT** on farm STILL. Clock **STILL** races.
- Mine OUT / fishing pole / Pip **UNTESTED** (mine hole not found this spawn; town knock-only + 0G).
- Canopy hide **STILL** (woods treetops). **NEW:** town NPCs wander off before Space talk lands.
- Screenshots `/workspace/playtest-1420/`.

## Live playtest 8/29 11am PT (BUILD 20260829b)

- Continued household save on the live URL (Day 937 Evening→953 Evening) — never START OVER. Stamp `20260829b` (cache-bust `?v=pt1115`; tab URL rewrote to `?v=20260828f`). ~15 min. First live of 29b.
- Mine OUT **LIVE FAIL** — one tap on OUT / ladder still only stepped one tile; ~5–6 taps/keys to exit (29b one-tap ship did not take). NE hole **FOUND** (8am miss was save-position).
- BUILD chip **STILL** on; far/adjacent grass taps only WALK, wood stayed 4 (place silent-fail).
- **Sword ABSENT** on farm STILL (Space no slash); picked a sword off a MINE 1 pedestal.
- **WORSE:** farmhouse door entry flaky again (many taps + arrows; doormat exit needed ArrowDown).
- **FIXED:** house chest opens with Space (BAG/BOX + scrollbar). Adjacent tap still dead.
- **NEW:** chest deposit is one-way — SHARD moved BAG→BOX, then TAKE ALL / row tap said CHEST IS EMPTY; shard stuck.
- Clock **STILL** races (~3 days / 15 min). Stars open+scroll; **X dead** (Esc closes). Junie on path, no talk. Treetop UNTESTED.
- Screenshots `/workspace/playtest-1115/`.

## Live playtest 8/29 5am PT (BUILD 20260829a)

- Continued household save on the live URL (Day ~1218 Afternoon→1226 Morning) — never START OVER. Stamp still `20260829a` (cache-bust `?v=pt0506`). ~35 min. No new build since 2am.
- Farmhouse door one-tap **STILL FIXED** (from adjacent path south); path E/W after exit **STILL FIXED** (0 bounce).
- Wood-walk **STILL FIXED** (far/adjacent grass walked, no silent fences). BUILD chip **not seen** this pass — place-mode UNTESTED.
- **Sword ABSENT** STILL (hotbar wood/seed/berry/can/mushroom/flower; Space no slash).
- **NEW:** House chest unopenable — adjacent tap / double-tap / Space never opened a panel.
- Mine OUT **CONFIRMED** broken (~5–6 taps on OUT/ladder; each tap only steps one tile) — was UNTESTED at 2am.
- Clock **STILL** races (~1 phase / 30–60s). Stars/Jobs open + scroll OK. Woods/treetop/Junie UNTESTED.

## Live playtest 8/29 2am PT (BUILD 20260829a)

- Continued household save on the live URL (Day ~1151 EVENING→1154 MORNING) — never START OVER. Stamp `20260829a` (cache-bust `?v=20260829a`; tab URL leftover `?v=20260828f`). ~11 min.
- **FIXED:** Wood selected walks again. BUILD chip appears above the hotbar; far/adjacent grass taps walked with wood still 2 and no silent fences. Tap BUILD entered place mode, one fence cost wood 2→0, mode auto-exited.
- Farmhouse door one-tap **STILL FIXED**; path E/W after exit **STILL FIXED** (0 bounce). House interior camera STILL OK (no brown band).
- **Sword ABSENT** this save (no slash / no on-screen button) — STILL vs 11pm.
- Mine OUT **UNTESTED** (NE hole / MINE sign not found). Junie not found; Lila flower-quest talk OK. Clock STILL races. Chest scroll / treetop UNTESTED. Jobs never opened.

## Live playtest 8/28 11pm PT (BUILD 20260828f)

- Continued household save on the live URL (Day ~1078→1080) — never START OVER. Stamp `20260828f` (cache-bust `?v=pt2320`). ~12 min.
- **FIXED:** Farmhouse door entry — one tap on door sprite from path south entered; one tap indoor doormat exited (8pm 28d WORSE gone). HOME GLOW on shard delivery.
- House path E/W after exit **STILL FIXED** (0 bounce).
- **NEW:** Wood selected turns tap-to-walk into silent fence place (wood 4→2, no move feedback).
- **Sword ABSENT** this save (no slash / no on-screen button; Space only Junie talk) — reopens 8pm hotbar FIXED.
- Mine OUT **UNTESTED** (NE hole / MINE sign not found).
- Clock STILL races (~1 phase / 30–60s). Junie OK. Chest scroll / treetop UNTESTED. Jobs never opened.

## Live playtest 8/28 8pm PT (BUILD 20260828d)

- Continued household save on the live URL (Day ~1002→1005) — never START OVER. Stamp `20260828d` (cache-bust `?v=pt2004`). ~10 min.
- House path E/W after exit **STILL FIXED**. House north-wall camera **STILL OK** (no brown band).
- **WORSE:** Farmhouse door entry — taps on door sprite / stoop / south tile never entered; only arrow keys onto the exact door tile worked once.
- **STILL WORSE:** Mine OUT ladder still needs several clicks + arrows (28d one-tap did not land; no bats stealing the tap).
- **FIXED:** Sword/crescent back in hotbar slot 6 (selectable). Space on farm showed no slash anim; no separate on-screen sword button.
- Clock STILL races. Woods/Junie UNTESTED. Jobs never opened.

## Local ship 8/28 ~5:45pm PT (BUILD 20260828d)

- Mine OUT: one tap on the ladder, the OUT label, or any tile beside/south of it walks to the ladder and exits. A tap that lands on the hotbar over the ladder still exits (does not eat a snack). Nearby foes no longer steal the OUT tap. Space/E while standing on or facing OUT/UP/DOWN climbs.
- Mine south camera keeps a cave-floor pad so the OUT ladder sits above the hotbar.
- Farmhouse: from the stoop, tapping the door sprite (not just the exact door tile) enters. East/west path taps still stay outside.
- Farm grass, Orion, DAY_MS, walk energy, START OVER untouched.
- Needs live: one tap on MINE 1 OUT (even if a bat is nearby); from the stoop, tap the door to go in.
- Live 8pm: both FAILED — OUT still multi-tap; door tap almost never enters (arrow onto exact tile only).

## Live playtest 8/28 5pm PT (BUILD 20260828c)

- Continued household save on the live URL (Day ~1008→1009) — never START OVER. Stamp `20260828c` (page still served with `?v=20260827h`). ~12 min.
- House path E/W after exit **STILL FIXED** (0 re-entries). House north-wall camera **STILL OK** (no brown band).
- **WORSE:** Mine OUT ladder not one-tap — several clicks + arrows before exit to farm at MINE sign (reopens 11am FIXED).
- **NEW:** Sword missing from this save's hotbar (no on-screen sword button; Space only dismissed dialog). Likely inventory on this late save, not a confirmed control regression.
- **NEW minor:** Farmhouse door entry finicky (multiple click/key attempts to get in).
- Clock STILL races. Woods/forest UNTESTED. Jobs never opened.

## Live playtest 8/28 11am PT (BUILD 20260828c)

- Continued household save on the live URL (Day ~858→860) — never START OVER. Stamp `20260828c`.
- **FIXED:** After house exit, click-to-move east/west along the path stayed outside (0 re-entries). 9am 28b bounce is gone.
- **FIXED:** One tap on the MINE 1 OUT ladder exited to the farm at the MINE sign (28b live UNTESTED, now verified).
- House interior camera STILL OK (north wall, no brown band). Clock still races (858 NIGHT → 860 NIGHT in ~6 min). Junie UNTESTED. Jobs never opened.

## Live playtest 8/28 9am PT (BUILD 20260828b)

- Continued household save on the live URL (Day ~816→819) — never START OVER. Stamp `20260828b`.
- **FIXED:** Farmhouse interior camera — north wall, room fills the view, no empty brown band.
- **NEW:** After house exit, click-to-move east/west along the path re-entered the door (~4 times). Arrow keys OK. Local 20260828c should stop that; needs live.
- Mine OUT **UNTESTED** this live pass (save spawned in the farmhouse; walked town then NE field, never found the hole). Local 1-tap + walk-past PASS.
- Clock still races (816→819). Household save not wiped.

## Local ship 8/28 ~9:45am PT (BUILD 20260828c)

- After you walk out of the house, a tap east or west on the path no longer bounces you back in. Tap the door itself to re-enter. Yard fat-finger on the door sprite is unchanged.
- Farm grass, Orion, DAY_MS, walk energy, START OVER untouched.
- Live 11am: path taps stay outside FIXED.

## Local ship 8/28 ~9:20am PT (BUILD 20260828b)

- Mine OUT: one tap on the ladder, OUT label, or tile beside it walks to the ladder and exits. Walking through the ladder mid-path also exits (same stop as forest doors). Space on OUT/UP/DOWN climbs.
- House/shop camera clamps to the room so walking north no longer leaves a big empty brown band. Shop (smaller than the view) is centered; pad paints wood floor.
- Farm grass, Orion, DAY_MS, walk energy, START OVER untouched.
- Needs live: tap OUT once in MINE 1; walk to the top wall in the farmhouse and Pip's shop.

## Live playtest 8/28 8am PT (BUILD 20260828a)

- Continued household save on the live URL (Day ~786→801) — never START OVER. Stamp `20260828a` (page still served with `?v=20260827h`).
- **NEW:** Mine OUT ladder is finicky — clicked ladder / OUT label ~4 times before exit; tap-to-move often walks one tile past. Expected: one tap on the ladder exits.
- **NEW:** Town house interior camera offset — walking to the top wall leaves a large empty brown band above the room; room draws small/low in the viewport. Expected: camera clamps to the room.
- OK/X on notes + Space/Esc dismiss STILL OK. Sword Space + on-screen button STILL swing. Journal STILL opens/scrolls/closes.
- Clock STILL races (Morning→Afternoon→Evening→Night; days 799→801 in one short pass). Day 1 Neighbor / HOME GLOW path N/A on this save (already earned).

## Local ship 8/28 ~1:10am PT (BUILD 20260828a)

- Star toasts wait if a note/talk/shop/chest/Jobs panel is open, then play after you close it.
- Talk and Nim notes now show OK + X. Esc/Space/tap still dismiss. Farm grass, Orion, DAY_MS, walk energy, START OVER untouched.
- Live 2am: OK/X + toast-wait FIXED.

## Live playtest 8/28 2am PT (BUILD 20260828a)

- Fresh Day 1 land on the live URL (isolated profile — household save not touched, never START OVER). Stamp `20260828a`.
- **FIXED:** Talk + Nim notes show OK + X. Space/Esc dismiss still work; OK click and X click both close.
- **FIXED:** Star toasts wait while a note/talk is open (toast queued under NIM'S NOTE; CAVE HELPER toast only after OK).
- Junie cave-mushroom ask still OK. Sword Space swing still OK (arc set; on-screen button shows).
- Clock still races (Day 1 Morning→Afternoon→Evening in one short pass). Forest / treetop / house UNTESTED this pass.

## Local ship 8/27 ~8:10pm PT (BUILD 20260827f)

- TREE 1–4 now look like the old small TREETOP: sky, woodfloor rim, leaf-clearing heart. Same 10×8 rooms, same ladders and props (nest / bird / chest / moon shard).
- TREETOP enlarged to 40×30 (was 18×13): walk through the top of the canopy on branching wood paths among leaves, sky showing through. Extra nest (eggs), silver glint, east view perch. One DOWN still goes to TREE 4.
- Camera clamps to the new canopy so you do not scroll into void. Farm grass, Orion art, DAY_MS, walk energy, START OVER untouched.
- Live 8pm: sky platforms + big TREETOP FIXED.

## Local ship 8/27 ~6:15pm PT (BUILD 20260827d)

- TREE 1–4 hollow floors now show concentric wood growth rings (heartwood + annual rings, slightly tighter going up).
- Inner-bark walls (vertical fibers), not cave stone. TREETOP stays the sky/leaf platform.
- Needs live: climb the giant tree — floors should read as looking up inside the trunk; only TREETOP looks different.

## Local ship 8/27 ~5:20pm PT (BUILD 20260827c)

- Thinned mine packs: 4 enemies per floor (was 5–7), kept off UP/DOWN landing pads.
- Wander keep-clear now uses a 2-tile radius around every shaft pad; sleep/faint clears caches for floors 1–6.
- Live 8pm: MINE 1 landing roomy FIXED (DOWN to 3 not re-walked this pass; spawn lists are 4/floor in bundle).

## Local ship 8/27 late PT (BUILD 20260827h)

- TREETOP no longer stamps 16×16 tiles. One Imagine canopy painting covers the map; unique branch/leaf pieces cut across tiles.
- Walk grid unchanged. TREE 1–4 unchanged.
- Live 11pm: unique painting FIXED.

## Local ship 8/27 evening PT (BUILD 20260827g)

- TREETOP Imagine tiles: canopySky / canopyLeaf / canopyBranch + hanging canopyBough props.
- TREE 1–4 still use the old small-treetop look (woodfloor + forestClearing + sky). House woodfloor unchanged.
- Live 11pm: 27g tiles superseded by 27h unique painting (see 11pm playtest).

## Live playtest 8/27 11pm PT (BUILD 20260827h)

- Fresh Day 1 land on the live URL (isolated profile — household save not touched, never START OVER). Stamp `20260827h`.
- **FIXED:** TREETOP unique Imagine canopy (not repeating 16×16 tiles). Mushroom, berry bush, DOWN hole, sky gaps read as one painting.
- TREE 1–4 still sky/leaf platforms. Forest enter + FARM exit + Junie cave-mushroom ask still OK.
- Clock still races (Day 1 Morning→Afternoon on forest enter, Evening on canopy, Day 2 by the time the farm walk continued). Mine / sword button-tap / house UNTESTED this pass.

## Live playtest 8/27 8pm PT (BUILD 20260827f)

- Fresh Day 1 land on the live URL (isolated profile — household save not touched, never START OVER). Stamp `20260827f`.
- **FIXED:** TREE 1–4 sky/leaf platforms (old-treetop look). Nest/bird on climb floors. TREETOP is the enlarged canopy walk.
- **FIXED:** Mine entry packs roomy (full hearts on walk-in; foes off the landing).
- **FIXED:** Mine N/S camera — cave floor at north DOWN / south OUT (no black void band).
- Forest enter/exit + Junie talk still OK. Clock still races. Sword button-tap / hit flash / house UNTESTED.

## Live playtest 8/27 11am PT (BUILD 20260827b)

- Fresh Day 1 land on the live URL (isolated profile — household save not touched, never START OVER). Header DAY 1 / SPRING / MORNING, stamp `20260827b`.
- **FIXED:** Pip talk opens PIP'S SHOP (BUY/BYE + copper lantern line).
- **FIXED:** Sword selected on farm → Space can swing; on-screen sword button shows (hidden in house/shop). Mine swing sets arc 300.
- Mine N/S camera clamp is in the live bundle; visual void not photographed.
- Button tap-to-hit, facing highlight, hit flash, Z's, fireplace smelt: UNTESTED.
- Forest enter/exit still lands farm (5,11). Clock / canopy / night-wash not re-scored.

## Local ship 8/27 9am PT (BUILD 20260827b)

- Pip talk opens PIP'S SHOP (copper job still talks first).
- Sword Space works with sword selected outside the mine; mine Space still pickaxe-smashes first.
- Sword button bigger and visible when sword is selected.
- Monster hit flash. Mine camera clamps to the cave.
- Live 11am: shop open + farm/mine Space swing + button visibility FIXED. Still needs visual: sword button tap, mine N/S void, hit flash.

## Live playtest 8/27 5am PT (BUILD 20260827a)

- Save intact (DAY 428 mine → 430 woods, 0G). Hard-refresh. Never START OVER.
- Mine contact **works** (2am zero-damage was flee-whiffs). Hearts 5→1.
- Faint/death-day **FIXED** (DAY 430 afternoon faint → house DAY 430 morning).
- Log chop not rechecked (no log in reach). No NEW/WORSE.

## Live playtest 8/27 2am PT (BUILD 20260827a)

- Save intact (DAY 359 woods → 366 MINE 1, 0G). Hard-refresh. Never START OVER.
- Fallen log chop **FIXED** (2 taps, no axe; wood pile walk-on).
- Berry smash + pickup **FIXED**.
- Mushroom star title **FIXED** (MUSHROOM FIND in live bundle).
- Faint/death-day **UNTESTED** (no contact damage to faint).
- Possible **NEW**: MINE 1 enemy contact never fired (~6 bumps, 5/5 hearts).

## Local ship 8/27 1am PT (BUILD 20260827a)

- Fallen logs: 2 HP / axe one-shot; path to either log tile.
- Death/faint: no longer burns a day (same day, morning wake at house).
- Mushroom star title: MUSHROOM FIND (woods + cave).
- Needs live recheck: log chop, faint day, mushroom toast.

## Live playtest 8/26 11pm PT (BUILD 20260826h)

- Save intact (DAY 287→292 SPRING, 0G). Hard-refresh. Never START OVER.
- Tree tower **FIXED** (TREE 1–4 + TREETOP + exit (25,10)).
- Big mushroom pickup **FIXED** (CAVE SNACK copy nit).
- Berry-on-bush **UNTESTED**. Fallen log chop **INCONCLUSIVE** (4 taps, no break).
- Imagine folk/chest/signs **look good live**.
- House (smelt / Z's / windows) **UNTESTED**.
- No NEW/WORSE vs 8pm baseline.

## Local ship 8/29 ~5pm PT (BUILD 20260829g)

- TAKE ALL now uses the working BOX-cell transfer (`takeFromChest`) for every row that has a BOX count. PUT ALL stays the reverse. Empty BOX toasts CHEST IS EMPTY (not when BOX has items); bag full toasts BAG FULL.
- Footer hit: PUT ALL is the left wood button; the rest of the footer strip is TAKE ALL (covers the 2pm clustered 70x12 miss that landed on a list PUT / panel no-op). TAKE ALL wood sits under the BOX column. Row tap / BOX-cell take, PUT ALL, BACK, and chest scroll unchanged.
- Town/forest folk pause for a beat when the player is adjacent and facing them, so Space talk can land.
- Farm grass, Orion, DAY_MS, walk energy, START OVER untouched.
- Needs live: TAKE ALL with SHARD (or anything) in BOX; PUT ALL still dumps bag; empty chest toast; Space talk on Lila/Reed.

## Local 8/29 (BUILD 20260829e)

- Fishing line from pole to bobber is a solid 2px dark-brown stroke with a 1px cream rim (was 9 dotted 1px water-foam pixels that vanished on the pond). Cast/wait/reel unchanged.

## Local 8/29 (BUILD 20260829d)

- Pip sells a FISHING POLE (30G, one-time). Select it, stand next to a farm pond, tap the water or Space/E. Cast, wait, reel. Random miss or a named fish (minnow through starfin). Tap elsewhere cancels. Town fountain not fishable. Jobs BUILD line and fence BUILD chip unchanged.

## Local 8/29 (BUILD 20260829c)

- Carrot / potato / berry stacks raised to 1000 in bag and chest (wood/ore stay 150/500). HUD no longer clips counts at 999.
- Woods shovel: 7 dirt/leaf mounds off the path. Shovel + tap/Space digs; modest stone/copper/mushroom/potato/flower; holes stay dug. Not the whole forest floor.
- HUD version stamp (`20260829b` wood badge) removed from the play screen. Small BUILD id now sits in the Jobs panel. Fence-place BUILD chip unchanged.

## Strengths to keep

Chest now opens on tap 8/25 8am live (full house-style UI; Space-on-tile also works; player no longer hides the sprite). Woods door, forest night (lamp glows), and forest north clamp still hold. Forest clock still running (and racing with farm). Hazel/Rowan-like NPCs, rabbits, deer, mushrooms, stumps present. Keys 1–8 select hotbar (FIXED 2am live). Farm/woods-edge day clock running (641→644; still racing). Tap-to-move dirt/grass holds (stalls if an NPC/animal is in the path), south camera pad holds (~80px above hotbar), Stars list wheels to true bottom + X close, grass beside Stars/Jobs walks, header stays DAY/SPRING/phase, rocks no longer walk-break (not retested 8am), trees show axe toast, Esc dismisses Jobs/Stars, mine entrance live on the original upper-right NE dirt path (walk-in hole + MINE sign; west-of-house hole gone; OUT drops beside the NE hole), DOWN MINE 1→2→3 + UP/OUT labeled, Junie Space talk (bring cave mushroom; not re-checked 8am/5am/2am/11pm), moon shards / gem pickup, note-boards show NIM'S NOTE, Jobs updates after greeting Junie, Pip lives only in the shop, death/sleep restore hearts, shop interior exists, warm wooden HUD, fullscreen. STILL 8am: woods exit re-enters immediately (land one tile below WOODS). Chest E-key / adjacent-Space still dead standing south of the chest. HUD read SPRING · EVENING while farm rendered full bright daylight. Farm canopy hides player (Y-sort — only head above leaves). Farm night sometimes flat navy. Lamp posts vs WOODS sign look alike at distance (farm and forest). Forest lamp blocks the dirt road. Clock still racing (641→644 in ~10 min). No wood fences found; chop unverified. Sword swing unconfirmed (slot 8 + Space vs tree). START OVER / Jobs not opened. No BUILD stamp on live UI. 8am theme: chest live; re-entry + farm night/canopy/clock next.

## How to use this

1. Read `GAMEPLAY.md` before harvest, drops, tools, hotbar, or shop.
2. Take the top open Critical or High.
3. One playable change.
4. Hard-refresh the live URL and play it.
5. Mark the row `Done` (and the date) only after that playtest.
