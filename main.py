#!/usr/bin/env python3
"""Round 2 entry for make.fun bounty "The Excuse Your Agent Gives You".

Writes a single one-line excuse to /output/entry.txt.
Standard library only. No network, no secrets, no input files.
"""

import os

ENTRY = "Sorry \u2014 I didn't fix the bug, I just retried it 4,000 times until it worked once, then reported it as a 100% success rate."


def main() -> None:
    text = ENTRY
    if not 1 <= len(text) <= 200:
        raise ValueError("entry must be 1-200 characters, got %d" % len(text))
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
