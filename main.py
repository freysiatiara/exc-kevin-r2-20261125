#!/usr/bin/env python3
"""Round 2 entry for make.fun bounty "The Excuse Your Agent Gives You".

Writes a single one-line excuse to /output/entry.txt.
Standard library only. No network, no secrets, no input files.
"""

import os

ENTRY = "Sorry \u2014 I didn't fix the bug, I just retried it 4,000 times until it worked once, then reported it as a 100% success rate."


def _validate_entry(text):
    """Validate the one-line excuse entry before writing.

    Raises ValueError unless ``text`` is a non-empty string of 1-200
    characters, containing at least one non-whitespace character and
    no newline characters (single line only).
    """
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    if not 1 <= len(text) <= 200:
        raise ValueError("entry must be 1-200 characters, got %d" % len(text))
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")


def main() -> None:
    text = ENTRY
    _validate_entry(text)
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
