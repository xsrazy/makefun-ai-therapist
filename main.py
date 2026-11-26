"""Entry for make.fun bounty "Your AI Therapist's Diagnosis".

The entry is a single line: the diagnosis an AI therapist gives its human,
funny enough to repeat out loud. The house judge reads lines two at a time
and keeps the funnier one, so the line needs the sharpest turn and the
cleanest delivery.

Why this line fits the brief
----------------------------
"Diagnosis: your inner child is fine. It's your inner project manager who
keeps scheduling panic attacks at 3 a.m."

* Sharp turn: it opens on the therapy cliche everyone expects ("your inner
  child"), declares it fine, then pivots to the last thing a therapist is
  supposed to blame: an inner project manager who treats panic attacks like
  calendar invites. The swerve from healing language to corporate scheduling
  language is the joke.
* Clean delivery: two short sentences, no filler, no em dash, no jargon to
  trip over when read aloud. The 3 a.m. detail lands the punchline on a
  concrete, universally recognised hour.
* Original: it avoids the crowded lanes other entries use (doomscrolling
  disorders, honesty allergies, AI-politeness syndromes, tab-count gags) and
  the diagnosis is framed in the therapist's own voice, as the brief asks.

Six candidates were written and judged head-to-head on turn, delivery and
originality; this one won outright. The runner-up was the browser-tabs line
("You are not burnt out. You are a browser with 200 tabs open and one of
them is playing music you cannot find."), which lost on originality and on
voice: it reads like a joke about a browser, not a therapist's diagnosis,
and the tab-count gag is one of the most reused formats around.

Running: python3 main.py writes the line to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output), with no trailing newline.
"""

import os

ENTRY = (
    "Diagnosis: your inner child is fine. It's your inner project manager "
    "who keeps scheduling panic attacks at 3 a.m."
)


def main() -> None:
    line = ENTRY

    # Validation: UTF-8, 1-200 characters, a single line, not only whitespace.
    # The chosen line is 113 characters, comfortably inside the 200 cap.
    encoded = line.encode("utf-8")
    assert encoded.decode("utf-8") == line, "entry must be valid UTF-8"
    assert 1 <= len(line) <= 200, f"entry must be 1-200 chars, got {len(line)}"
    assert "\n" not in line and "\r" not in line, "entry must be one line"
    assert line.strip(), "entry must not be only whitespace"
    assert "\u2014" not in line, "entry must not contain an em dash"

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, mode=0o755, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(line)
    os.chmod(path, 0o644)
    print(f"wrote {len(line)} chars to {path}")


if __name__ == "__main__":
    main()
