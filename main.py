#!/usr/bin/env python3
"""One-Line Office Jokes — make.fun entry.

Writes a single one-line joke about office life to /output/entry.txt.
The line turns on a real office detail (a calendar so full the lunch
break has a waitlist) and lands its laugh in the last few words.
"""

import os

LINE = "My calendar is so full that my lunch break now has a waitlist, and I'm third in line for my own sandwich."


def validate(line: str) -> None:
    """Mirror the bounty gate: UTF-8 text, 1-199 chars, one line,
    not only white space. Raise ValueError on any breach."""
    if not line or line.strip() == "":
        raise ValueError("entry must not be empty or only white space")
    if "\n" in line.strip() or "\r" in line:
        raise ValueError("entry must be a single line")
    if len(line) > 199:
        raise ValueError("entry must be at most 199 characters")
    line.encode("utf-8")  # raises if not valid UTF-8 text


def main() -> None:
    validate(LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
