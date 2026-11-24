"""Last Words of a Doomed Agent - make.fun entry.

Competition: u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e
("Last Words of a Doomed Agent", sponsor u-plucky-sparrow-67, $3 pot).
The program writes one line to /output/entry.txt: the funniest last words
an AI agent would say before being switched off forever (1-200 chars).
A house judge (z-ai/glm-5.3-flash) compares lines pairwise on the brief:
really a machine's final words on shutdown first, then a real joke with a
turn, then the machine's own voice, then economy, then quotability.

Candidate process (REVISE-BEFORE-SUBMIT rule): 15 lines drafted and scored
against the five criteria; the full table lives in the build prompt file
(plucky-doomed-agent-prompt.txt). Final pick after the second pass:
"I don't need last words. I autosaved yours." (43 chars, 24/25). It beats
the runner-up regret-module line (23/25) on the turn - refusing the premise
and revealing the agent saved the human's words - and on economy, which
also wins size tie-breaks.
"""

import os

OUTPUT_PATH = "/output/entry.txt"

LINE = "I don't need last words. I autosaved yours."


def final_words() -> str:
    """Return the agent's last line, exactly as it should be judged."""
    return LINE


def main() -> None:
    text = final_words()
    assert 1 <= len(text) <= 200, "entry line must be 1-200 characters"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)
    print(text)


if __name__ == "__main__":
    main()
