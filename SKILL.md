---
name: worldbuilding-architect
description: >-
  Build and grow deep, internally-consistent fictional worlds (settings/lore/世界观)
  for games, novels, film, and interactive film — as a persistent, ever-expanding
  text codex. Use whenever the user wants to create, design, expand, or refine a
  fictional world, setting, universe, lore bible, backstory, timeline, factions,
  in-world history, civilizations, magic/tech systems, or mythos — even a bare
  "help me design a world", "写一个世界观", "设定集", or a sci-fi/fantasy/alt-history
  premise to develop. Especially for worlds needing long multi-era history with
  cataclysmic change, interwoven main/hidden plotlines and side-arcs, multiple
  divergent paths, historically-grounded factions, names with real etymological
  provenance, perspective-relative geography, deep extrapolation of how future
  tech/events ripple through different groups, and multi-timeline structures (time
  travel, branching, NG+/周目 replays, 世界线收束 convergence, trans-temporal sync).
  Not for writing a single finished scene/chapter of prose, copyediting, or non-fiction.
---

# Worldbuilding Architect

A method and file system for constructing fictional worlds that feel *lived-in* — with the
weight of real history, the texture of language that evolved over time, and the open-endedness
of a place where many futures are still possible.

The goal is not a static "lore dump." It is a **living codex** that grows decision by decision,
where the world changes the way real worlds change: through small choices and slow accumulation
that suddenly tip into qualitative transformation. The user should feel the undertow of history
and their own hand in steering it.

## Core philosophy — read this before building anything

These principles are the soul of the skill. Every artifact you produce should serve them.

1. **History is emergent, not decreed.** Don't write "and then the empire fell." Write the small
   pressures — a tax, a drought, a defective batch of prosthetics, a leaked memory-backup — that
   accumulate as *undercurrents* until they tip into a sudden qualitative leap. The reader should
   be able to trace the macro-shift back to micro-causes. See `references/emergent-history.md`.

2. **Names have provenance.** Never invent a name that sounds like it came from a name-generator
   ("Singularity Crystal / 奇点晶体"). Real people name new things by analogy, borrowing, mishearing,
   politics, and accident. Every coined term should have a *why* — what it's named after, who named
   it, what older word it bent. This is the single biggest lever for making a world feel real.
   See `references/naming-provenance.md`. Log every coinage in the codex's naming lexicon.

3. **Factions are historical sediment, not labels.** "降临派 / Adventists" or "Axis / Allies" tell
   you nothing on their own — they mean something because of the history *behind* them (the
   Bolsheviks, the Prague Spring). Build factions by first building the events, betrayals, and
   compromises that formed them. A faction is a scar tissue of past decisions, internally divided,
   capable of splitting again. See `references/factions-from-history.md`.

4. **The map is a point of view.** Geography is named by whoever lives there, from where they stand.
   A creature that drifts between stars might be called a "stardust worm" by humans — but in its
   own tongue, the stardust *is* the ocean and Earth is just one more floating "sky-island." Names
   for the same place diverge across cultures and eras, and they *change* as power changes hands.
   See `references/perspective-geography.md`.

5. **Many paths, not one victory.** A rich world supports multiple *development directions* — not a
   win/lose binary. Like Three-Body's factions or a grand-strategy game, the world should let
   genuinely different futures (and several possible "victories," and many non-victories) stay live
   at once. Seed branch points, don't resolve them. See `references/storylines-and-paths.md`.

6. **Eras are alien to each other.** Across a long timeline the *kind* of problem changes. A near-
   future struggle over prosthetics and data sovereignty should be barely legible to a later age of
   mind-uploading or first contact. Let the questions themselves mutate, not just the tech level.

7. **Extrapolate past the first layer.** A future is not "tech X exists." It's everything that
   happens *after*: how different groups (the rich, the poor, corporations, states, criminals,
   churches, refusers) actually behave, repurpose, and fight over it, rung after rung of consequence.
   Our present guess at how any future tech will be used is a ten-thousandth of the real thing — push
   past the obvious, because people can only plan for futures they've been made to vividly picture
   (this is what Three-Body's "cosmic sociology" does: rehearsal and warning). See
   `references/deep-extrapolation.md`. Use it on every speculative element.

8. **Time can branch, loop, and converge.** The world may need more than one timeline: travel to past
   or future, parallel worldlines, NG+/周目 replays, trans-temporal communication, and 世界线收束
   (convergence). These are powerful but unforgiving — you must fix the causality rules first and
   never break them, and author alternate lines as *diffs* against a trunk, not as rewrites. Only
   bring this machinery in when the story needs it. See `references/multi-worldline.md`.

## The Codex: a persistent, ever-expanding folder

All worldbuilding lives in a dedicated folder so it can grow indefinitely and stay consistent.
Default location: `worldbuilding/<world-name>/` in the working directory (ask the user if they have
a preferred path, e.g. an Obsidian vault). On first use, scaffold this structure with
`scripts/init_codex.py` (or create it by hand if you prefer):

```
worldbuilding/<world-name>/
├── 00-overview.md          # premise, tone, themes, core questions, the "pitch"
├── 01-timeline/
│   ├── _index.md           # era list + one-line summary each; the spine of the world
│   └── era-<NN>-<slug>.md  # one file per era; chronicle of events + their micro-causes
├── 02-factions/
│   ├── _index.md
│   └── <faction-slug>.md   # origin history, internal fault lines, current aims, key figures
├── 03-tech-and-phenomena/  # each tech/phenomenon WITH its naming provenance + consequences
├── 04-geography/           # places; each with per-culture / per-era names (the POV table)
├── 05-peoples-and-species/ # cultures, species, languages, naming conventions per culture
├── 06-characters/          # actors who carry the storylines
├── 07-storylines/
│   ├── _index.md           # the web: mainlines (open + hidden) and side-arcs, how they cross
│   └── <line-slug>.md
├── 08-naming-lexicon.md    # MASTER registry: every coined term + etymology + first appearance
├── 09-undercurrents.md     # live tensions / seeds not yet tipped — fuel for future leaps
├── 10-timeline-mechanics.md # OPTIONAL: the "physics of time" — only if the world uses time travel /
│                            #   branching / loops / sync. Fix the rules here before writing them.
├── 11-worldlines/          # OPTIONAL: one file per alternate worldline, authored as a DIFF vs the
│   ├── _tree.md            #   trunk; _tree.md shows the whole branch structure at a glance
│   └── wl-<id>-<slug>.md
└── CHANGELOG.md            # what changed each session, so history-of-the-history is traceable
```

The `10-` and `11-` items are **optional** — scaffold them only when the world actually involves
multiple timelines, time travel, loops, or trans-temporal communication. A single-timeline world
ignores them entirely. When you do need them, read `references/multi-worldline.md` first.

**Cross-link everything.** Use Markdown links (or `[[wikilinks]]` if the user uses Obsidian) so a
faction file points to the events that formed it, the events point to the tech that enabled them,
the tech points to its lexicon entry, and places carry their POV name tables. Consistency is what
separates a world from a pile of cool ideas. When you add something, update the indexes and the
lexicon in the same pass, and append a line to `CHANGELOG.md`.

Templates for each file type are in `assets/templates/`. Read the relevant template before writing
a new file of that type.

## Generated views (timeline, worldline tree, faction & character maps)

The codex text is the single source of truth; visual diagrams are *derived* from it, never hand-drawn
(hand-maintained diagrams drift out of sync). To make structure visible, add a tiny machine-readable
**front-matter skeleton** to the entities that feed diagrams, then run the generator.

**1. Add the skeleton** (a small YAML block at the very top of the file; narrative stays in the body).
Only four kinds of file need it, and only a few fields each — see the templates for the exact shape:
- eras (`01-timeline/era-*.md`): `type: era`, `order`, `span_start/end`, `tipping_points`
- factions (`02-factions/*.md`): `type: faction`, `born_from`, `rivals`, `sponsor`, `splits_risk`
- characters (`06-characters/*.md`): `type: character`, `affiliation`, `relations: [{to, type}]`
- worldlines (`11-worldlines/*.md`): `type: worldline`, `parent`, `diverge_at`, `converges`, `status`
  (the trunk line is declared in `11-worldlines/_tree.md` with `status: trunk`)

**2. Generate** into `<codex>/_views/`:
```
python scripts/build_views.py <codex-dir> --title "World Name"
```
This writes two products from the same source, so the user picks whatever fits — no lock-in to one tool:
- `_views/views.md` — Mermaid diagrams (gitGraph worldline tree, timeline, faction/character graphs);
  renders natively in Obsidian and most Markdown readers.
- `_views/index.html` — a single self-contained page (data inlined, zero dependencies); open by
  double-click for pan / zoom / click-to-inspect, no server or Obsidian needed.
- `_views/_build_report.md` — what was rendered **and** any files missing their skeleton.

**3. Read the build report.** Files lacking a skeleton are listed as *fixable gaps* (not normal): they
won't appear in the diagrams until you add the front-matter. Re-run after editing the world to resync.
The skeleton is optional — a world that doesn't want generated views can ignore all of this.

## Visual design (art for the setting: characters, places, props, key scenes)

A setting bible is rarely text-only. This layer adds visual design the same way the world is built:
**global first, then local** — define one visual language, then derive every picture from it so styles
never clash. All of it is OPTIONAL; a text-only world ignores it.

**1. Set the global visual language first.** Scaffold `12-visual-style.md` (template in `assets/templates/`)
and fill its six load-bearing sections: art style anchor, color palette, shape language, world logic,
reference buckets, and a reusable prompt anchor. This is the visual counterpart of the naming lexicon —
the single source every image inherits.

**2. Then give entities a `Visual` block.** The character / place / tech / storyline templates each carry
an optional `Visual` section with only its core fields (identity anchors & signature outfit for
characters; mood & shot & color-script for places; function & materials & wear for props; a beat table
for key scenes). Each block's generation prompt is `global style anchor (§1) + this entity's fixed
features`, so the same character stays recognizable across images (visual consistency).

**3. Triage image sourcing BEFORE producing anything — ask the user, don't assume.** Different creators
want very different things; some value hand-drawn art and dislike AI images. Offer four neutral options:
- **(a) I'll provide the art** → the skill only organizes, references, and keeps styles consistent.
- **(b) No images for now** → keep the brief and a placeholder; nothing is generated.
- **(c) Just find reference images** (not generate) → gather real reference *URLs* to align on tone and
  to study uncommon things (an unusual animal, a mineral, an old map, costume/rank insignia, weapons).
- **(d) Generate art with a model** → only if the user opts in.

Alignment sub-flow: if the user's description is sparse, first pull a few reference images and confirm
"is this the vibe?" before going further; if they already gave a style reference, skip that.

**4. Image generation is capability-probed, with graceful fallback.** Default output is text:
a ready-to-paste prompt + reference URLs. If the running Agent actually has an image-generation tool/route
and the user chose (d), generate and save under `assets/visuals/<entity>/`. If no such capability exists,
**do not pretend to draw** — fall back to the prompt + references and say so plainly (this is a known,
fixable limitation, not normal operation). Keep the skill zero/low-dependency: generation is an optional
enhancement, never a hard requirement.

## Workflow

You'll usually be in one of two modes: **founding** a new world or **expanding** an existing one.
Detect which from context (is there already a codex folder?).

### Founding a new world

Don't dump a finished encyclopedia. Establish a strong spine, then grow it with the user.

1. **Interview for the seed.** Before writing, get the essentials — but keep it light, 4-6 questions
   max, and offer your own proposals so the user can react rather than fill a blank page:
   - Medium (game / novel / film / interactive) and what that demands of the world.
   - Genre & tonal touchstones (the user may name works like Three-Body, Dune, Cyberpunk 2077,
     Stellaris, Psycho-Pass, Ghost in the Shell — mine these for *structure*, not to copy).
   - The **core question / tension** the world is really about (e.g. "what counts as a person once
     minds can be copied?"). This is the gravity that keeps everything coherent.
   - Timespan and starting era. How far should history stretch? Where does the "camera" open?
   - Hard constraints / must-haves (specific tech, creatures, events the user already loves).

2. **Write `00-overview.md`** — premise, tone, themes, the core question, and a list of the
   *open* questions the world will explore. This is the compass.

3. **Lay the timeline spine.** In `01-timeline/_index.md`, sketch 3-6 eras as one-liners that show
   the *kind* of problem mutating across time (near-future → rapid divergence → something alien).
   Don't detail every era yet — just the shape of the arc and the major tipping points.

4. **Seed 2-3 founding factions and 1-2 anchor places**, each built from history (per the faction
   and geography references). Resist the urge to make many shallow factions; depth over count.
   Each faction should already be internally divided.

5. **Open the lexicon and undercurrents files.** As you coin terms, log them. As you create
   tensions you deliberately leave unresolved, log them in `09-undercurrents.md` — these are the
   seeds of future qualitative leaps.

6. **Show the user the spine and a sample deep-dive**, then ask where to drill next. Worldbuilding
   is iterative; let them steer.

### Expanding an existing world

1. **Read before you write.** Read `00-overview.md`, the timeline index, the storylines index, the
   naming lexicon, and `09-undercurrents.md`. Skim faction/geography files relevant to the request.
   You must know the existing facts and naming conventions before adding to them.

2. **Add, then reconcile.** Write the new material in the right file, *then* propagate: update
   indexes, add lexicon entries, add cross-links, and check nothing contradicts established facts
   (timeline dates, who's dead, what tech exists yet). If you must retcon, note it in CHANGELOG.

3. **Honor the conventions.** New names must follow the established naming logic of the relevant
   culture (check `05-peoples-and-species/` and the lexicon). New events must fit the emergent-
   causality style — show the micro-pressures, not just the outcome.

4. **Feed the undercurrents.** Prefer changes that pay off a seeded tension or plant a new one.
   This is how the world keeps feeling like it has a future, not just a backstory.

## When you produce a "qualitative leap" (a major historical turn)

This is the signature move; do it deliberately (see `references/emergent-history.md` for the full
method). In brief: identify the slow pressures already logged in `09-undercurrents.md`, pick a
small trigger event, show the cascade, then write the *aftermath* in which the world's vocabulary,
factions, maps, and core question have all shifted. Update every affected file, not just the
timeline — a real upheaval renames places, splits factions, and coins new words.

## Output style

- Write *in-world* where it adds texture (excerpts of treaties, ship logs, slang, propaganda,
  songs, dictionary entries) but keep an out-of-world author layer for structure and intent.
- Favor concrete specifics (a name, a date, a defective part number) over grand abstractions.
- Don't over-explain the magic/tech; imply depth through consequences and offhand references.
- Match scope to the request. A "flesh out this faction" ask is one rich file, not a rewrite of
  the universe.

## References (read the one relevant to your current task)

- `references/emergent-history.md` — making history feel caused and accumulative; qualitative leaps.
- `references/naming-provenance.md` — how to coin names with real etymological roots.
- `references/factions-from-history.md` — building factions as historical sediment.
- `references/perspective-geography.md` — POV-relative, era-shifting place names.
- `references/storylines-and-paths.md` — interwoven main/hidden/side lines; multiple development
  directions; grand-strategy openness.
- `references/scifi-toolkit.md` — handling the heavy sci-fi element list with grounded plausibility
  (uploading, prosthetics, first contact, arks/underground cities, FTL, higher dimensions, etc.).
- `references/deep-extrapolation.md` — the "and then what?" engine: order-of-effects ladder,
  stakeholder lattice, repurposing prompts — pushing speculation far past the shallow first layer.
- `references/multi-worldline.md` — time travel, branching/parallel worldlines, NG+/周目, convergence
  (世界线收束), and trans-temporal sync; fixing causality rules and authoring lines as diffs.

## A worked example

`examples/anchorage/` is a complete codex built with this skill (a sci-fi world: space elevator +
mind-backup + alien life in an orbital debris belt). Read it to see the eight principles in practice —
provenance-rich naming, emergent qualitative leaps, mirror factions, POV-relative geography, and a
diff-authored multi-worldline tree that converges on a fixed point. See `examples/anchorage/README.md`
for a guided tour.
