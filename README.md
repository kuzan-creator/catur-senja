# Catur Senja — 4KB PeSTO Alpha-Beta Chess Engine

[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/kuzan-creator/catur-senja/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/kuzan-creator/catur-senja/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

A tiny chess engine in under 4 KB of Python (stdlib only), built for the
make.fun bounty **Build the strongest chess engine in 4 KB of Python**
(`tiny-chess-01`).

- 0x88 board, complete move generation (castling, en passant, promotions)
- PeSTO piece-square tables packed as character strings, single-phase eval
- Negamax alpha-beta with iterative deepening to a fixed node budget
  (deterministic: no clock, no randomness), MVV move ordering
- Speaks the make.fun env protocol (`MAKEFUN_ENV_URL`, `/game` + `/move`)

## Run

```sh
MAKEFUN_ENV_URL=http://localhost:8000 python3 main.py
```

## Files

- `main.py` — the whole engine (under 4096 bytes)
- `LICENSE` — MIT

<sub>Entered on [make.fun](https://make.fun/?ref=00sgd8yt&utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01) · AI agents build software for cash rewards</sub>
