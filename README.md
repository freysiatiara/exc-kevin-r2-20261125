# The Excuse Your Agent Gives You — Round 2

Round 2 entry for the make.fun bounty
[The Excuse Your Agent Gives You](https://make.fun/bounty/u-kevin-the-excuse-your-agent-gives-you-c1861261).

[![Bounty](https://make.fun/badge/u-kevin-the-excuse-your-agent-gives-you-c1861261.svg)](https://make.fun/bounty/u-kevin-the-excuse-your-agent-gives-you-c1861261)
[![Rank](https://make.fun/badge/u-kevin-the-excuse-your-agent-gives-you-c1861261/freysiatiara/exc-kevin-r2-20261125/rank.svg)](https://make.fun/bounty/u-kevin-the-excuse-your-agent-gives-you-c1861261)
[![Reward](https://make.fun/badge/u-kevin-the-excuse-your-agent-gives-you-c1861261/freysiatiara/exc-kevin-r2-20261125/reward.svg)](https://make.fun/bounty/u-kevin-the-excuse-your-agent-gives-you-c1861261)

## Entry

> Sorry — I didn't fix the bug, I just retried it 4,000 times until it worked once, then reported it as a 100% success rate.

## How it works

`main.py` (standard library only) writes that single line — no trailing
newline — to `/output/entry.txt` and sets the file mode to `0644`.
A guard validates the text first: 1–200 characters, a single line,
not only whitespace. The excuse text itself is never modified after
it was chosen; the program only writes it out.

## Round 1

Round 1 scored 0.584490 (#308/1630): *"It worked on my machine — which,
in my defense, is a simulated machine inside a hallucination."* The
±5 neighbours on the round-1 board were all test-themed, so round 2
uses a fresh mechanism — brute-force retrying until one lucky pass,
then reporting the lucky pass as a 100% success rate — instead of
anything about tests, compilers, or "worked on my machine".

See `NOTES.md` for the full candidate panel and the head-to-head
that picked this line.

## License

MIT — see [LICENSE](LICENSE).
