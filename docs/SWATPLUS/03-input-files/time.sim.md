---
type: input
tags:
  - swat/input
file: time.sim
ext: sim
cio_field: time
read_by:
  - time_read.f90
purpose: ""
---

# time.sim

> [!info] Input File
> Declared in `file.cio` field `time`. See [[file.cio]] for the controlling file map.

## Overview
- **Declared in `file.cio` field**: `time`
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[time_read.f90]]

## File Structure
- [[time_read.f90]] source line 24: reads `titldum`
- [[time_read.f90]] source line 26: reads `header`
- [[time_read.f90]] source line 28: reads `time%day_start`, `time%yrc_start`, `time%day_end`, `time%yrc_end`, `time%step`

## Parameters
| Parameter | Type | Units | Meaning | Source | Reader line |
|---|---|---|---|---|---:|
| `time%day_start` | `integer` |  | beginning julian day of simulation | [[time_module.f90#time]] | [[time_read.f90]]:28 |
| `time%yrc_start` | `integer` |  | starting calendar year | [[time_module.f90#time]] | [[time_read.f90]]:28 |
| `time%day_end` | `integer` |  | input ending julian day of simulation | [[time_module.f90#time]] | [[time_read.f90]]:28 |
| `time%yrc_end` | `integer` |  | ending calendar year | [[time_module.f90#time]] | [[time_read.f90]]:28 |
| `time%step` | `integer` |  | number of time steps in a day for rainfall, runoff and routing 0 = daily; 1=increment(12 hrs); 24=hourly; 96=15 mins; 1440=minute; | [[time_module.f90#time]] | [[time_read.f90]]:28 |
