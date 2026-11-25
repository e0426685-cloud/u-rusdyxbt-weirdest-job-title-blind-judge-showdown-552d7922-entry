"""Senior Apologizer for Elevators That Give Up.

One job title, 60 characters or fewer, for the weirdest-job-title
blind-judge showdown. The title sounds like a real senior role
until the twist lands: the apologizing is aimed at elevators
that simply give up. Deadpan, specific, and one line only.

The program writes the title to /output/entry.txt, then reads
it back and checks it matches. Python standard library only,
fully deterministic.
"""

import os

MAX_CHARS = 60

LINE = "Senior Apologizer for Elevators That Give Up"


def validate(text: str) -> None:
    """Check the entry is one line of 1-60 characters, nothing else."""
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if text != text.strip():
        raise ValueError("entry must not start or end with whitespace")
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(
            f"entry must be 1-{MAX_CHARS} chars, got {len(text)}"
        )


def main() -> None:
    validate(LINE)
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    os.chmod(path, 0o644)
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != LINE:
        raise ValueError("written entry does not match the title")
    validate(written)
    print(f"Wrote {path} ({len(written)} characters)")


if __name__ == "__main__":
    main()

