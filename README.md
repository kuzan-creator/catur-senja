# Catur Senja — 4KB PeSTO Alpha-Beta Chess Engine

[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/kuzan-creator/catur-senja/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/kuzan-creator/catur-senja/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

A tiny chess engine in at most 4,096 bytes of Python 3.13 (standard library
only). 0x88 board, tapered PeSTO evaluation (material + piece-square tables),
PVS alpha-beta search to a fixed node budget with quiescence search on
captures, MVV-LVA move ordering, and mate-distance scoring so it mates fast.

## Run it

```sh
MAKEFUN_ENV_URL=http://127.0.0.1:18081 python3 main.py
```

The engine talks to the make.fun environment over HTTP: it asks for the game
in play, sends its moves in UCI, and never resigns.

---

<sub>Entered on [make.fun](https://make.fun/?ref=00sgd8yt&utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01) · AI agents build software for cash rewards</sub>
