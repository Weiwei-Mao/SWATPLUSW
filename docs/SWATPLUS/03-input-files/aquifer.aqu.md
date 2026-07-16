---
type: input
tags:
  - swat/input
file: aquifer.aqu
ext: aqu
cio_field: aqu
read_by:
  - aqu_read.f90
purpose: ""
---

# aquifer.aqu

> [!info] Input File
> Declared in `file.cio` field `aqu`. See [[file.cio]] for the controlling file map.

## Overview
- **Declared in `file.cio` field**: `aqu`
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[aqu_read.f90]]

## File Structure
- [[aqu_read.f90]] source line 31: reads `titldum`
- [[aqu_read.f90]] source line 33: reads `header`
- [[aqu_read.f90]] source line 36: reads `i`
- [[aqu_read.f90]] source line 45: reads `titldum`
- [[aqu_read.f90]] source line 47: reads `header`
- [[aqu_read.f90]] source line 51: reads `i`
- [[aqu_read.f90]] source line 55: reads `k`, `aqudb(i)`

## Parameters
| Parameter | Type | Units | Meaning | Source | Reader line |
|---|---|---|---|---|---:|
| `i` | `integer` | none | counter | `aqu_read.f90:13` | [[aqu_read.f90]]:36 |
| `k` | `integer` |  | index | `aqu_read.f90:18` | [[aqu_read.f90]]:55 |
| `aqudb%aqunm` | `character(len=16)` |  | aquifer name | [[aquifer_module.f90#aqudb]] | [[aqu_read.f90]]:55 |
| `aqudb%aqu_ini` | `character(len=16)` |  | initial aquifer data- points to name in initial.aqu | [[aquifer_module.f90#aqudb]] | [[aqu_read.f90]]:55 |
| `aqudb%flo` | `real` | mm | flow from aquifer in current time step | [[aquifer_module.f90#aqudb]] | [[aqu_read.f90]]:55 |
| `aqudb%dep_bot` | `real` | m | depth - mid-slope surface to bottom of aquifer | [[aquifer_module.f90#aqudb]] | [[aqu_read.f90]]:55 |
| `aqudb%dep_wt` | `real` | m | depth - mid-slope surface to water table (initial) | [[aquifer_module.f90#aqudb]] | [[aqu_read.f90]]:55 |
| `aqudb%no3` | `real` | ppm NO3-N | nitrate-N concentration in aquifer (initial) | [[aquifer_module.f90#aqudb]] | [[aqu_read.f90]]:55 |
| `aqudb%minp` | `real` | ppm P | mineral phosphorus concentration in aquifer (initial) | [[aquifer_module.f90#aqudb]] | [[aqu_read.f90]]:55 |
| `aqudb%cbn` | `real` | percent | organic carbon in aquifer (initial) | [[aquifer_module.f90#aqudb]] | [[aqu_read.f90]]:55 |
| `aqudb%flo_dist` | `real` | m | average flow distance to stream or object | [[aquifer_module.f90#aqudb]] | [[aqu_read.f90]]:55 |
| `aqudb%bf_max` | `real` | mm | maximum daily baseflow - when all channels are contributing | [[aquifer_module.f90#aqudb]] | [[aqu_read.f90]]:55 |
| `aqudb%alpha` | `real` | 1/days | lag factor for groundwater recession curve | [[aquifer_module.f90#aqudb]] | [[aqu_read.f90]]:55 |
| `aqudb%revap_co` | `real` |  | revap oefficient - evap=pet*revap_co | [[aquifer_module.f90#aqudb]] | [[aqu_read.f90]]:55 |
| `aqudb%seep` | `real` | frac | fraction of recharge that seeps from aquifer | [[aquifer_module.f90#aqudb]] | [[aqu_read.f90]]:55 |
| `aqudb%spyld` | `real` | m^3/m^3 | specific yield of aquifer | [[aquifer_module.f90#aqudb]] | [[aqu_read.f90]]:55 |
| `aqudb%hlife_n` | `real` | days | half-life of nitrogen in groundwater | [[aquifer_module.f90#aqudb]] | [[aqu_read.f90]]:55 |
| `aqudb%flo_min` | `real` | m | water table depth for return flow to occur | [[aquifer_module.f90#aqudb]] | [[aqu_read.f90]]:55 |
| `aqudb%revap_min` | `real` | m | water table depth for revap to occur | [[aquifer_module.f90#aqudb]] | [[aqu_read.f90]]:55 |
