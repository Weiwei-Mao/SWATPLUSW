---
type: input
tags:
  - swat/input
file: tiledrain.str
ext: str
cio_field: tiledrain_str
read_by:
  - sdr_read.f90
purpose: ""
---

# tiledrain.str

> [!info] Input File
> Declared in `file.cio` field `tiledrain_str`. See [[file.cio]] for the controlling file map.

## Overview
- **Declared in `file.cio` field**: `tiledrain_str`
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[sdr_read.f90]]

## File Structure
- [[sdr_read.f90]] source line 26: reads `titldum`
- [[sdr_read.f90]] source line 28: reads `header`
- [[sdr_read.f90]] source line 31: reads `titldum`
- [[sdr_read.f90]] source line 39: reads `titldum`
- [[sdr_read.f90]] source line 41: reads `header`
- [[sdr_read.f90]] source line 45: reads `sdr(isdr)`

## Parameters
| Parameter | Type | Units | Meaning | Source | Reader line |
|---|---|---|---|---|---:|
| `sdr%name` | `character(len=40)` |  |  | [[hru_module.f90#sdr]] | [[sdr_read.f90]]:45 |
| `sdr%depth` | `real` |  | mm \|depth of drain tube from the soil surface | [[hru_module.f90#sdr]] | [[sdr_read.f90]]:45 |
| `sdr%time` | `real` |  | hrs \|time to drain soil to field capacity | [[hru_module.f90#sdr]] | [[sdr_read.f90]]:45 |
| `sdr%lag` | `real` |  | hours \|drain tile lag time | [[hru_module.f90#sdr]] | [[sdr_read.f90]]:45 |
| `sdr%radius` | `real` |  | mm \|effective radius of drains | [[hru_module.f90#sdr]] | [[sdr_read.f90]]:45 |
| `sdr%dist` | `real` |  | mm \|distance between two drain tubes or tiles | [[hru_module.f90#sdr]] | [[sdr_read.f90]]:45 |
| `sdr%drain_co` | `real` |  | mm/day \|drainage coefficient | [[hru_module.f90#sdr]] | [[sdr_read.f90]]:45 |
| `sdr%pumpcap` | `real` |  | mm/hr \|pump capacity | [[hru_module.f90#sdr]] | [[sdr_read.f90]]:45 |
| `sdr%latksat` | `real` | !na | multiplication factor to determine lat sat hyd conductivity for profile | [[hru_module.f90#sdr]] | [[sdr_read.f90]]:45 |
