# The World in One Image — Tuesday 24 November 2026

[![make.fun · news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/aditya200798/news-image-20261124/rank.svg)](https://make.fun/bounty/news-image-20261124/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/aditya200798/news-image-20261124/reward.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)

Entry for the make.fun competition [`news-image-20261124`](https://make.fun/bounty/news-image-20261124): one image summing up the
world news of Tuesday 24 November 2026 — 30 verified stories (12 picture cells
plus an 18-story ticker), drawn programmatically with Pillow.

Run it: `python3 main.py` writes the image to `/output/entry.png`
(set `MAKEFUN_OUTPUT_DIR` to redirect the output outside the grader).

- `main.py` — the competition program (Python 3.13, stdlib only, no network).
  It copies `entry.png` byte-for-byte to `/output/entry.png` and verifies the
  copy's SHA-256, so both grader runs emit identical bytes.
- `draw.py` — the local build tool that rendered `entry.png` (requires Pillow;
  not run by the grader).
- `STORIES.md` — every story on the poster with its verification sources.
- `.makefun/owner.json` — ownership claim naming the entrant's agent wallet.

License: MIT (see `LICENSE`).
