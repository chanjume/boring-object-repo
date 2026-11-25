#!/usr/bin/env python3
"""Most Boring Object Reviewed in One Line.

Writes a single funny, true one-line review of the dullest everyday
object we could name — a doorstop — to /output/entry.txt.
The review must be 1-200 characters (the sealed gate).
"""
import os

ENTRY = (
    "The doorstop: five stars. It has done exactly one job, "
    "perfectly, silently, since 2019 — and never asked for a raise."
)


def main():
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, must be 1-200"
    assert text.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")  # one line, trailing newline only
    print(text)
    print(f"characters: {len(text)}")


if __name__ == "__main__":
    main()
