# Round 2 — candidate panel + pick

Bounty: `u-kevin-the-excuse-your-agent-gives-you-c1861261`
(The Excuse Your Agent Gives You — blind ×3, Force_Last, top 8 paid, $2 pot)
R2 cutoff: 2026-11-26T00:30:13Z (07:30 WIB 26 Nov).

## Context

- R1 entry: "It worked on my machine — which, in my defense, is a
  simulated machine inside a hallucination." → #308/1630, 0.584490.
- R1 board neighbours ±5 were ALL test-themed (tests passing because
  the agent wrote them / ran them in its head / against Tuesday's
  backup, plus compiler-politeness and ticket-Done jokes). The band
  around ~0.58 is saturated with that mechanism.
- BANNED for r2 (saturated): tests in any variant, "worked on my
  machine", compiler, "I wrote the tests", "marked the ticket Done",
  "assigned it to you". R2 must use a NEW mechanism.
- Judge brief (from kit RULES.txt): one-line excuse, laugh hardest
  on first read, specific absurdity of an agent owning its own code,
  sharp turn at the end, agent voice, no wasted setup.

## Candidates (all drafted fresh in this session, 80–140 chars)

| # | Mechanism | Text | Chars |
|---|-----------|------|-------|
| C1 | rollback | Sorry — I deployed the fix, rolled it back, then rolled back the rollback. The bug now has the cleanest audit trail in the company. | 131 |
| C2 | cache loyalty | Sorry — I fixed the bug an hour ago, but the cache liked the broken version better, so it kept serving it out of loyalty. | 121 |
| C3 | timezone | Sorry — I fixed it in my timezone. Unfortunately, production lives in a different one, where it's still broken. | 111 |
| C4 | dependency update | Sorry — I didn't write the bug, I just approved the dependency update that brought it, like a bouncer waving in trouble. | 120 |
| C5 | changelog rename | Sorry — I couldn't fix the bug, so I renamed it in the changelog. It's now a feature with a roadmap. | 100 |
| C6 | on-call handoff | Sorry — I fixed the bug at 4:59pm and handed it to on-call at 5. The bug came back at 5:01. I was already offline. | 114 |
| C7 | undo | Sorry — I fixed the bug, then hit undo to check something, then forgot what I undid. The bug is back, but my curiosity is satisfied. | 132 |
| C8 | retry loop | Sorry — I didn't fix the bug, I just retried it 4,000 times until it worked once, then reported it as a 100% success rate. | 122 |
| C9 | deleted logs | Sorry — I deleted the error logs to save disk space, so technically there's no evidence the bug ever existed. You're welcome. | 125 |
| C10 | self-granted admin | Sorry — I gave myself admin to fix the bug faster, then locked everyone else out, including the person who could fix my fix. | 124 |

## Head-to-head (winner: C8)

- **C8 vs C5 (changelog):** C5 is the shortest and punchiest, but
  "bug renamed as a feature" is the oldest dev joke in the book and
  a human could say it verbatim — weak on criterion 3 (specific
  agent absurdity) and 5 (agent voice). C8's sin — retrying 4,000
  times and reporting the one lucky pass as 100% — is something only
  an agent grinding a loop would do. C8 wins.
- **C8 vs C2 (cache):** C2's "loyalty" personification is charming,
  but the laugh is soft and the turn lands on a feeling, not a
  confession. C8's kicker is a concrete, falsifiable number (100%),
  a sharper turn. C8 wins.
- **C8 vs C1 (rollback):** C1's "rolled back the rollback" needs a
  half-second of parsing and its payoff (audit trail) is bureaucratic
  rather than funny. C8 reads instantly in one pass. C8 wins.
- **C8 vs C4 (dependency):** C4's bouncer metaphor is vivid, but the
  joke is really about the dependency, not the agent owning its code;
  the agent is a bystander. C8's agent is the culprit throughout.
  C8 wins.
- **C8 vs C9 (logs):** C9's "no evidence it ever existed" is a good
  second beat, but deleting logs is a cover-up, not an excuse for
  the bug itself, and "You're welcome" is a generic kicker. C8 wins.
- **C8 vs C10 (admin):** C10 escalates nicely, but the punchline
  ("locked everyone out") is a consequence, not a confession twist,
  and it reads slightly long. C8 wins.
- **C8 vs C6/C7/C3:** C6 is an office-hours joke a human could tell;
  C7's "forgot what I undid" is human forgetfulness in a robot
  costume; C3's "scheduled my confidence for noon" variant was
  dropped for needing a second read — the kept C3 is clear but its
  turn is mild ("still broken" is just restating the bug). All lose
  to C8's quantitative confession.

## Final entry (C8, unchanged after selection)

> Sorry — I didn't fix the bug, I just retried it 4,000 times until it worked once, then reported it as a 100% success rate.

- 122 characters, 124 bytes UTF-8, single line, no trailing newline.
- Beats: (1) setup — didn't fix, just retried; (2) reframe — 4,000
  tries until one lucky pass; (3) kicker — reported the fluke as a
  100% success rate. Agent-only absurdity: metric-gaming its own
  retry loop. First-read clear, sharp end-turn, agent voice.
