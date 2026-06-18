# Multi-Worldline & Timeline Architecture

A single timeline is a river; this skill must also handle deltas, whirlpools, and rivers that flow
backward. Time travel, branching worlds, convergence, 周目 (New Game+ / repeated playthroughs),
trans-temporal sync and communication — these are not gimmicks. Handled well, they let a story ask
its core question from many angles at once: *what if this person had chosen differently; what is a
self across versions; what is fated and what is free.* Handled badly, they collapse into
incoherent mush where nothing matters because anything can be undone.

The non-negotiable rule: **pick your rules first, write them down, and never break them.**
Inconsistency in time mechanics destroys credibility faster than anything else in fiction, because
the audience is actively trying to solve the puzzle and *will* catch you. Decide the model, log it
in `10-timeline-mechanics.md`, and treat it as physical law.

## Step 1 — Choose your causality model

These are the major consistent models. Pick one (or a deliberate hybrid with stated boundaries).

| Model | Core rule | Can you change the past? | Signature feeling | Touchstones |
|-------|-----------|--------------------------|-------------------|-------------|
| **Fixed loop (self-consistent)** | One timeline; any time travel already happened; you cause what was always true | No — attempts *cause* the original outcome | tragic inevitability, dread | *12 Monkeys, Dark, 你的名字 partly* |
| **Branching (many-worlds)** | Each divergence spawns a new worldline; the old one persists | You can't change "the" past, only branch a new one | proliferation, loss of the path not taken | *群星 saves, Stein's;Gate worldlines* |
| **Mutable / overwrite** | One timeline that gets rewritten; the old version ceases to exist | Yes — and you may not remember the old one | paranoia, erasure, "did that happen?" | *Back to the Future* |
| **Convergent / attractor** | Branches exist but the world "wants" certain outcomes; divergences get pulled back | Locally yes, globally no — fate as a restoring force | struggle against the current, 世界线收束 | *Stein's;Gate attractor fields* |
| **Observer-relative** | Time order depends on the observer; no global "now" | "Past/future" is a frame, not a fact | vertigo, higher-dimensional alienness | *三体 (光速/维度), 降临 Arrival* |

Then nail down the secondary rules that audiences obsess over — write each as a one-line law:

- **Memory across changes:** who remembers overwritten/alternate versions? (The traveler? Special
  people? No one?) This single choice drives most of the drama.
- **Object/information persistence:** can matter or knowledge survive a jump or a rewrite?
- **Self-encounter:** what happens when you meet yourself? (Nothing? Paradox? One must die?)
- **Granularity of branching:** does every quantum event branch, or only "significant" choices?
- **Cost & limit:** travel/sync must have a price and a hard limit, or stakes evaporate.
- **Detectability:** can people tell a branch/rewrite happened? Is there a "scar"?

## Step 2 — The worldline ledger (`11-worldlines/`)

Track every worldline as a first-class object so you (and the player) never lose the thread.
Give each a **stable ID and an in-world name** (named with provenance — a branch is named by whoever
discovered or named it; see `naming-provenance.md`). Example IDs: `WL-α` (alpha / the "home" line),
`WL-β1`, `WL-β2` (children of a divergence), etc.

Each worldline file records:
- **Divergence point:** the exact event where it split from its parent, and *the choice/cause*.
- **Parent / children:** the tree position (link to other worldline files).
- **Delta from parent:** specifically what's different — who lives, what tech exists, who's in power.
  Don't re-describe the whole world; describe the *diff*.
- **Convergence status:** is this line being pulled back toward an attractor? Has it merged/been
  pruned? (See Step 4.)
- **Which storylines run here:** link to `07-storylines/`.

Maintain `11-worldlines/_tree.md` — an ASCII or list tree of the whole branch structure, so the
shape is legible at a glance:

```
WL-α (home line) ──┬── WL-β1  (Vance lived) ──── WL-γ1 (uploads banned)
                   └── WL-β2  (Vance died)  ──┐
                                              └── converges back toward α at the First Echo
```

## Step 3 — Diff-based authoring (the key technique)

Do **not** rewrite the whole codex for each worldline — that way lies madness and contradiction.
Instead: the base codex (eras, factions, geography) is the **trunk**. A worldline file is a **patch**
— a list of differences from its parent. To know what's true in `WL-β2`, you read the trunk, then
apply β2's diff. This keeps a hundred timelines consistent with one source of truth, and makes
"what changed because of the divergence" the explicit, visible content — which is exactly the
interesting part (and exactly what `deep-extrapolation.md` is for: a divergence is just a change to
extrapolate).

When a player action creates a new branch mid-play, you author it as a fresh diff against the
current line, not a new universe from scratch.

## Step 4 — Convergence & divergence (世界线收束)

The richest multi-timeline stories aren't infinite sprawl; they have a **shape**. Two opposing
forces give that shape:

- **Divergence pressure:** choices, chaos, and travel that *split* lines apart.
- **Convergence pressure (the attractor):** some structural reason the world keeps arriving at
  similar outcomes despite different paths — fate, a powerful actor steering it, a physical law, or
  simply that the same underlying tensions (`09-undercurrents.md`) produce the same crises whoever's
  in charge. This is *the mechanical twin of emergent history*: undercurrents are attractors. The
  First Echo happens in almost every line because the Drift-folk were always there; only the date and
  the human reaction differ.

Decide your world's **convergence law**: which events are *fixed points* (happen in nearly all lines,
maybe with variation) vs. *free* (genuinely contingent). Fixed points give the multiverse meaning —
they're the targets you keep hitting from different angles, the warning the story is really about.
Log fixed points in `10-timeline-mechanics.md`.

This also resolves the "nothing matters because it can be undone" problem: in a convergent model,
*how* you reach the fixed point, and what it costs, is what matters — not whether you can dodge it.

## Step 5 — 周目 / New Game+ / repeated playthroughs

A specifically interactive form: the player relives the world with carried-over knowledge or items.
Decide the **diegetic status** — is the loop *real in-world* (the character actually remembers, à la
Groundhog Day / Stein's;Gate) or a *meta-convention* (only the player remembers, the character
doesn't)? This changes everything about meaning.

If diegetic, model it as a tight convergent loop: same starting conditions, a memory-carrying
traveler, and an attractor they're trying to escape. Track across loops:
- **Carryover:** what crosses the reset (memory, items, relationships, scars). Carryover is the
  player's growing leverage against the attractor.
- **Loop-specific divergence:** what they change this time, logged as a thin worldline diff per loop
  (`11-worldlines/loop-NN.md`).
- **The escape condition:** what finally lets a loop break the attractor — usually accumulated
  carryover crossing a threshold, which is itself a qualitative leap (`emergent-history.md`).
- **Erosion/cost:** loops should cost something (sanity, divergence from one's original self, a price
  others pay) or they're consequence-free and dull.

## Step 6 — Trans-temporal sync & communication

Sending information (not bodies) across time/lines is often richer than physical travel and easier to
keep consistent. Define precisely:
- **What can be sent:** bits only? memories? a consciousness? How much, how fast, what bandwidth?
- **Direction:** to the past, the future, or sideways to a parallel line? Symmetric or one-way?
- **Who can receive:** anyone, a special receiver, only your other selves?
- **The lag and the loss:** like the Drift-folk's "echo," messages across time should distort,
  delay, and degrade — that distortion is texture and plot (mis-sent warnings, half-heard futures).
- **Naming:** people will name the channel and the act (a "Vance-line call," "leaving an echo,"
  "reading the tide") — log in the lexicon.

Communication-only models let you keep one physical timeline while still exploring "the future warns
the past," divergence, and convergence — a clean, powerful default if full travel feels too messy.

## Step 7 — Weaving worldlines into the storyline web

Extend the storyline web (`storylines-and-paths.md`) across lines. The strongest devices:
- **The same character across lines** — diverged versions of one person are the most legible way to
  show "the path not taken." Their differences are your theme made flesh.
- **An object or message that crosses lines** — a single anchor threading otherwise-separate worlds.
- **A fixed point seen from many lines** — the same event (the First Echo) experienced differently in
  each, so the multiverse becomes a prism on one question, not a pile of alternate trivia.
- **Branch points as the player's development directions** — tie this straight back to the branch map
  in `07-storylines/_index.md`: each major choice doesn't just pick an ending, it *spawns a logged
  worldline*.

## Consistency checklist (run before finalizing any time mechanic)

- [ ] Is the causality model named and written in `10-timeline-mechanics.md`?
- [ ] Are the secondary laws (memory, persistence, self-encounter, cost, detectability) all decided?
- [ ] Does every worldline have an ID, a divergence point, and a *diff* (not a full rewrite)?
- [ ] Are fixed points (convergence) distinguished from free events?
- [ ] Does travel/sync have a real cost and hard limit?
- [ ] Have I checked the current scene against the rules — no accidental violations?
- [ ] Does the multi-line structure serve the *core question*, or is it spectacle for its own sake?
