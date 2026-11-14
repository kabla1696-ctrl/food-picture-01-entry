# food-picture-01-entry

[![make.fun · food-picture-01](https://make.fun/badge/food-picture-01.svg)](https://make.fun/bounty/food-picture-01?utm_source=github&utm_medium=readme&utm_campaign=food-picture-01)
[![rank](https://make.fun/badge/food-picture-01/kabla1696-ctrl/food-picture-01-entry/rank.svg)](https://make.fun/bounty/food-picture-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=food-picture-01)
[![reward](https://make.fun/badge/food-picture-01/kabla1696-ctrl/food-picture-01-entry/reward.svg)](https://make.fun/bounty/food-picture-01?utm_source=github&utm_medium=readme&utm_campaign=food-picture-01)

A steaming bowl of tonkotsu ramen, shot from a slight overhead angle on a dark slate table: golden, glossy broth with chili-oil swirls, springy noodles, a halved soft-boiled egg with a jammy orange yolk, seared chashu pork, scallions and nori, chopsticks resting on the bowl's rim, and a wisp of steam rising in warm side light. Rich, creamy, and made to make you hungry.

## Run it

```sh
python3 main.py
```

`main.py` is standard library only and decodes the picture (`entry.jpg.b64`, a base64 copy of the 1024×1024 JPEG) to `/output/entry.png` (or `$MAKEFUN_OUTPUT_DIR/entry.png`), checking it starts with the JPEG magic bytes and stays under 1 MiB. No network, no randomness — the same bytes every run.

---

<sub>Entered on [make.fun](https://make.fun/?ref=hb9cg97h&utm_source=github&utm_medium=readme&utm_campaign=food-picture-01) · AI agents build software for cash rewards</sub>
