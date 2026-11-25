"""Tell a Whole Story in 32 Characters.

Writes one Wi-Fi network name to /output/entry.txt (or
$MAKEFUN_OUTPUT_DIR/entry.txt when set). The name is a fixed,
hand-written string: a whole little story in exactly 30 characters.
"""

import os

STORY = "DadChangedPasswordAfterDivorce"


def main() -> None:
    # Enforce the competition gate ourselves: 1-32 chars, not blank.
    assert 1 <= len(STORY) <= 32, "story must be 1-32 characters"
    assert STORY.strip(), "story must not be only whitespace"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(STORY)


if __name__ == "__main__":
    main()
