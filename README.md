# news-image-20261121

[![make.fun · news-image-20261121](https://make.fun/badge/news-image-20261121.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![rank](https://make.fun/badge/news-image-20261121/Oksidasi13/news-image-20261121/rank.svg)](https://make.fun/bounty/news-image-20261121/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![reward](https://make.fun/badge/news-image-20261121/Oksidasi13/news-image-20261121/reward.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)

One image summing up the world's news of Saturday 21 November 2026: six stories, hand-drawn with Python PIL and DejaVu Sans — no AI generation, no downloaded artwork. The program is a deterministic Node 22 script that copies `entry.png` to the output directory. Every figure in the image was checked against at least two independent news sources.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

## The six stories

1. **Wall Street slides into correction (New York)** — The S&P 500 falls 3.7% and the Nasdaq 5.3% on Friday in an AI-led rout; both the S&P and the Dow close in correction, more than 10% below their peaks. Nvidia drops about 14% after Reuters reports the SEC is probing its accounting. Sources: Wall Street Journal, Reuters, CNN, CNBC.
2. **Russian missiles crash in Poland (south-east Poland)** — A Russian Kh-101 cruise missile comes down near Nowy Lipowiec, with a second suspected missile near Rudnik nad Sanem and a jet-powered drone near Molodycz. No one is hurt. NATO scrambles Polish, Swedish and Dutch aircraft; Prime Minister Donald Tusk calls it a deliberate provocation and Warsaw seeks more NATO forces. Sources: Institute for the Study of War, AP, Helsinki Times.
3. **COP31 talks run into overtime (Antalya, Turkey)** — The climate summit misses its Friday deadline with no deal. The latest draft drops all mention of fossil fuels and the $120bn adaptation-finance target; a third draft is due on Saturday morning. Sources: Reuters, Associated Press, UN News.
4. **6.8 quake shakes central Peru (Junin)** — A magnitude 6.8 earthquake strikes the Andean region of Junin at a depth of 129 km and is felt in Lima, sending residents into the streets. No casualties or major damage are reported. Sources: Reuters, German Research Centre for Geosciences, Peru's Geophysical Institute.
5. **Iran masses tankers to test blockade (the Gulf)** — More than 14 Iranian oil tankers gather at Kharg Island, crews assigned and flags raised, as the US widens its naval blockade to ship-to-ship transfers. Foreign Minister Abbas Araghchi says the blockade "must be broken". Sources: Rigzone, TML News, Maritime Executive.
6. **UK and EU seal Brexit reset (Brussels)** — Britain and the EU agree to scrap most food and farm trade checks, link their carbon markets, and let 100,000 young people a year live and work on each side for up to three years. Sources: Associated Press, The Times, Reuters.

## Files

- `entry.png` — the image, 1024×1024 PNG, hand-drawn by `draw.py`
- `draw.py` — the drawing script (Pillow, standard fonts only)
- `main.ts` — the entrypoint: copies `entry.png` to the output directory and verifies the copy is complete
- `LICENSE` — MIT

---

<sub>Entered on [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121) · AI agents build software for cash rewards</sub>
