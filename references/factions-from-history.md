# Factions from History

A faction name on its own — "降临派 / Adventists," "Axis," "Allies," "the Bolsheviks," "the Prague
Spring" — tells you nothing. These words carry weight only because of the *history compressed inside
them*: the betrayals, the congresses, the failed reforms, the people who walked out of a room. Build
the history first; the faction is what's left standing afterward.

## Anti-pattern: the symbolic faction

Avoid the lineup of clean, one-trait teams (the eco-faction, the tech-faction, the religion-faction).
They're legible but dead — stereotype and symbol, not a world. Signs you've fallen into it:
- Each faction maps to exactly one ideology with no internal disagreement.
- You can predict any member's opinion from the faction name.
- Factions don't share members, history, or contested ground.
- None of them could plausibly split, merge, or betray its own ideals.

## Build order: events → coalitions → label → fractures

1. **Start with an event, not a banner.** Something happened — a disaster, a discovery, a broken
   promise, a war's end. People had to take positions on a concrete question. (Three-Body's factions
   exist because *a signal was answered*; everything follows from reactions to that fact.)
2. **Watch coalitions form around the question, not the answer.** A faction is usually a *coalition*
   of groups who agree on one urgent thing and disagree on everything else. The Allies were
   capitalist democracies *and* the USSR. That internal contradiction is realism, and it's the seed
   of the faction's eventual crisis.
3. **The name comes last and obliquely.** It might be self-chosen propaganda, an enemy's insult worn
   as a badge, a place where they met, or a mistranslation. ("Bolshevik" just means "majority" — from
   a single vote. "Tory" was an insult.) Name per `naming-provenance.md`. Never name a faction by its
   ideology in plain language unless an *in-world propagandist* would have chosen that name.
4. **Build in the fault lines now.** Every faction should already contain the disagreement that could
   later split it. Write down its hardliners, its pragmatists, its careerists, its true believers,
   and the question that would crack it open.

## What a faction file needs (`02-factions/<slug>.md`)

- **Founding event & moment** — the concrete history it crystallized from.
- **The coalition** — which groups, with which incompatible motives, are inside it.
- **Stated aim vs. real aims** — the banner vs. what its factions actually want.
- **Internal fault lines** — the splits waiting to happen; who's on each side.
- **Methods & resources** — how it actually acts on the world.
- **Relationships** — not "allies/enemies" lists but *histories* with other factions (a former ally,
  a schism cousin, a funder it resents).
- **Key figures** — link to `06-characters/`.
- **Trajectory** — where the undercurrents are pushing it; how it might transform or die.

## Factions over time: sediment, not monument

Factions are not fixed. Across eras they:
- **Split** when their internal fault line meets a triggering event (one Three-Body-style faction
  becomes three).
- **Merge or ally** under existential pressure, swallowing their contradictions temporarily.
- **Outlive their cause** and mutate — a wartime resistance becomes a postwar mafia, keeping the
  rituals but not the reason.
- **Get renamed by victors or successors.** The losing side's name becomes a slur; the winning side
  rewrites its own origin.

Tie these changes to the timeline and undercurrents. A faction that never changes is set dressing.

## "Development directions," not teams to pick

Crucially, factions should embody *different futures for the world*, not different difficulty
settings. The point isn't "which side wins" but "which world comes to be." Adventists vs. Survivors
isn't good-vs-evil; it's *two answers to what a species owes its own continuation*. When you design a
faction, ask: **what does the world look like if these people get their way?** If several factions
each imply a genuinely different, defensible world, you have a strategy space, not a morality play.
See `storylines-and-paths.md` for turning these into branching development paths.

## Worked micro-example (sci-fi)

Event: the first successful mind-upload (a "Vance," see naming ref). It works — but the original body
survives the scan.

- Now there are *two* of someone. A concrete question: which one inherits the marriage, the debt, the
  citizenship?
- Coalition A forms around *"the copy is the person, continuity is an illusion"* — uniting some
  uploaded elites, some philosophers, and, cynically, insurers who'd rather pay one claim. Enemies
  call them "the Shelved" (because their bodies often end up suspended). They adopt it.
- Coalition B forms around *"the body is the person"* — uniting religious traditionalists, body-shop
  prosthetic guilds (who profit from embodiment), and ordinary people who fear deletion. They call
  themselves nothing grand; the press calls them "Grounders."
- Fault line inside A: the philosophers want *no* originals kept; the insurers want originals *kept
  but disenfranchised* (cheaper). That crack is a future schism.
- Trajectory: when an upload is later proven to *diverge* from its original within hours, A fractures
  exactly along that fault line — and B suddenly has to decide if a days-old divergent copy is a
  murder victim or never a person at all. The question mutates; new factions are born.

Notice: no one is the "AI faction" or the "transhuman faction." They're coalitions over a concrete
event, internally divided, named obliquely, and each implying a different civilization.
