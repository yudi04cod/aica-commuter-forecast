"""Aica Commuter Forecast — entry for make.fun bounty
u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e.

Writes one line of weather (at most 140 characters) for a city that
does not exist to /output/entry.txt. Python standard library only.
"""

import os

ENTRY = (
    "Cloudhaven: light strawberry snow this morning, buses run on time "
    "for once, and every commuter gets a free second sunrise before nine."
)


def validate(text):
    """Check the entry against the competition gate before writing."""
    if not text or not text.strip():
        raise ValueError("entry must not be empty or only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if len(text) > 140:
        raise ValueError(f"entry is {len(text)} characters, over the 140 limit")
    if len(text) < 1:
        raise ValueError("entry must be at least 1 character")
    return True


def main():
    validate(ENTRY)
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
