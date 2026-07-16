---
type: input
tags:
  - swat/input
file: weather-sta.cli
ext: cli
cio_field: weat_sta
read_by:
  - cli_staread.f90
purpose: ""
---

# weather-sta.cli

> [!info] Input File
> Declared in `file.cio` field `weat_sta`. See [[file.cio]] for the controlling file map.

## Overview
- **Declared in `file.cio` field**: `weat_sta`
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[cli_staread.f90]]

## File Structure
- [[cli_staread.f90]] source line 35: reads `titldum`
- [[cli_staread.f90]] source line 37: reads `header`
- [[cli_staread.f90]] source line 41: reads `titldum`
- [[cli_staread.f90]] source line 60: reads `titldum`
- [[cli_staread.f90]] source line 62: reads `header`
- [[cli_staread.f90]] source line 65: reads `titldum`
- [[cli_staread.f90]] source line 68: reads `wst(i)%name`, `wst(i)%wco_c`

## Parameters
| Parameter | Type | Units | Meaning | Source | Reader line |
|---|---|---|---|---|---:|
| `wst%name` | `character(len=50)` |  |  | [[climate_module.f90#wst]] | [[cli_staread.f90]]:68 |
| `wst%wco_c` | `weather_codes_station_char` |  |  | [[climate_module.f90#wst]] | [[cli_staread.f90]]:68 |
