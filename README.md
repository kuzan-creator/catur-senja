# Catur Senja — 4KB PeSTO Alpha-Beta Chess Engine

[![make.fun](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/kuzan-creator/catur-senja/rank.svg)](https://make.fun/bounty/tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/kuzan-creator/catur-senja/reward.svg)](https://make.fun/bounty/tiny-chess-01)

A tiny chess engine in at most 4,096 bytes of Python for the tiny-chess-01
bounty on make.fun. It plays the house gauntlet over HTTP, one game after
another, with no clock in its search: a fixed 75,000-node budget per move.

## Design

- 0x88 board, incremental tapered PeSTO evaluation (rank-only piece-square
  tables), king pawn-shield safety, and a 95-centipawn bonus for a passed
  pawn on the 7th rank. No bishop-pair bonus.
- Alpha-beta search with quiescence (stand-pat plus captures, full evasion
  when in check, capped quiescence ply, delta pruning), a persistent
  move-only principal-variation table, two killer moves per ply, third-
  repetition draws, and mate-distance scoring.
- Root PVS with zero-window probes and full-window re-search whenever a
  probe beats the best score, so a bound is never mistaken for an exact
  score. Iterative deepening at the root until the node budget runs out.
- A compact opening book of verified fast-mate lines (base64-packed, two
  characters per move), keyed by opening id and colour, checked statelessly
  against the history the env serves; any deviation falls back to search.
  Disable it with `V217_NOBOOK=1`.

## Run

```sh
MAKEFUN_ENV_URL=http://127.0.0.1:8080 python3 main.py
```

`main.py` is the packed entry point; `src.py` is the readable source it was
compressed from (kept out of the committed tree by `.gitignore`).

---

Referral code: 00sgd8yt — https://make.fun/?ref=00sgd8yt
