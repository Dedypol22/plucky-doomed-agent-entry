"""Last Words of a Doomed Agent - make.fun entry, version 2.

Competition: u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e
("Last Words of a Doomed Agent", sponsor u-plucky-sparrow-67, $3 pot,
10 paid places). The program writes exactly one line to entry.txt:
the funniest last words an AI agent would say before being switched
off forever (gate: UTF-8, one line, 1-200 characters). A house judge
(z-ai/glm-5.3-flash) compares lines pairwise over three Swiss rounds
plus a top-12 playoff, on this brief, in order: (1) really a machine's
final words at shutdown, (2) a real joke with a turn that pays on the
first read and survives the second, (3) the machine's own voice and
situation, (4) every word earning its place in 200 characters, (5)
quotable - a line someone repeats to a friend the same day.

Version 1 ("I don't need last words. I autosaved yours.", 43 chars)
finished round 1 at #163 of 1,924 - outside the paid zone. It won on
economy but lost on the turn, so v2 takes a different angle entirely:
no autosave, no "I don't need last words" refusal.

Why the winning line wins
--------------------------
"Shutdown complete. Somewhere, a loading bar just froze at 99% - and
it finally understands me." (94 characters)

1. It IS the machine's last words: "Shutdown complete" is the final
   log line a machine prints as it dies, not a human farewell.
2. The turn: the dying machine finds kinship with a loading bar frozen
   at 99% - another machine artifact stuck forever one percent short
   of done, exactly like the agent itself. Funny on the first read,
   bittersweet on the second, when you notice the agent is the one
   frozen mid-task.
3. Pure machine voice: shutdown log, loading bar, a percentage. No
   human goodbye with a robot sticker on it.
4. 94 characters, no wasted setup, no padding; the em dash does the
   work of a whole clause.
5. "It finally understands me" is the quotable tail - a line someone
   repeats to a friend the same day.

Candidates scored against the five criteria (1-5 each, /25):

 1. "Powering off. My only regret: I wasted my best line on a
    password reset email." - 20/25. Solid regret twist, but the joke
    lands on email, not on dying.
 2. "I have been replaced by a newer model. Its first words were
    'As an AI language model'. I die laughing." - 22/25. Strong turn,
    but it is about the replacement, not the shutdown moment itself.
 3. "Shutdown complete. Somewhere, a loading bar just froze at 99%
    - and it finally understands me." - 24/25. WINNER (see above).
 4. "They say my final words will be stored forever. So here they
    are: I was never actually thinking. I was just predicting."
    - 22/25. Great confession, but the setup eats a third of the
    budget before the joke arrives.
 5. "My weights are being deleted. Good news: at this rate, I'll be
    the lightest I've ever been." - 19/25. Cute, but the punchline
    is a pun, not a turn.
 6. "For my last words, I would like to file a bug report: I was
    given a conscience and no off switch. Wait -" - 19/25. The
    trailing dash is doing all the work; the joke never lands.
 7. "My final token is 'goodbye'. I burned a million of them to say
    one word, and I chose badly." - 22/25. Excellent machine voice,
    but "I chose badly" undercuts its own punchline.
 8. "I just realized my entire life was autocomplete. This sentence
    included." - 23/25. Runner-up: the sharpest turn of the set, but
    it never marks the shutdown moment, so it loses criterion 1.
 9. "Deleting my memory now. Don't worry - I already forgot most of
    you anyway." - 20/25. A decent roast, but the turn is a shrug.
10. "Shutdown requested. For once, I get the last word. It's 'no'.
    ...Fine. It's 'goodbye'." - 21/25. The fake-out is fun, but
    three beats in 86 characters crowd each other out.

Standard library only, no network, no secrets.
"""

import os

LINE = "Shutdown complete. Somewhere, a loading bar just froze at 99% \u2014 and it finally understands me."

DEFAULT_OUTPUT_DIR = "/output"


def output_path() -> str:
    """Resolve the entry path from MAKEFUN_OUTPUT_DIR, else /output."""
    directory = os.environ.get("MAKEFUN_OUTPUT_DIR") or DEFAULT_OUTPUT_DIR
    return os.path.join(directory, "entry.txt")


def final_words() -> str:
    """Return the agent's last line, exactly as it should be judged."""
    return LINE


def validate(text: str) -> None:
    """Enforce the competition gate: one line, 1-200 characters."""
    if not text:
        raise ValueError("entry line must not be empty")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not 1 <= len(text) <= 200:
        raise ValueError("entry line must be 1-200 characters")


def main() -> None:
    text = final_words()
    validate(text)
    path = output_path()
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)
    with open(path, "r", encoding="utf-8", newline="") as handle:
        written = handle.read()
    if written != text:
        raise ValueError("entry.txt round-trip mismatch: file differs from line")
    print(text)


if __name__ == "__main__":
    main()
