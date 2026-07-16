---
type: input
tags:
  - swat/input
file: hydrology.res
ext: res
cio_field: hyd_res
read_by:
  - res_read_hyd.f90
purpose: ""
---

# hydrology.res

> [!info] Input File
> Declared in `file.cio` field `hyd_res`. See [[file.cio]] for the controlling file map.

## Overview
- **Declared in `file.cio` field**: `hyd_res`
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[res_read_hyd.f90]]

## File Structure
- [[res_read_hyd.f90]] source line 26: reads `titldum`
- [[res_read_hyd.f90]] source line 28: reads `header`
- [[res_read_hyd.f90]] source line 31: reads `titldum`
- [[res_read_hyd.f90]] source line 40: reads `titldum`
- [[res_read_hyd.f90]] source line 42: reads `header`
- [[res_read_hyd.f90]] source line 49: reads `res_hyddb(ires)`

## Parameters
| Parameter | Type | Units | Meaning | Source | Reader line |
|---|---|---|---|---|---:|
| `res_hyddb%name` | `character(len=25)` |  |  | [[reservoir_data_module.f90#res_hyddb]] | [[res_read_hyd.f90]]:49 |
| `res_hyddb%iyres` | `integer` | none | year of the sim that the res becomes operational | [[reservoir_data_module.f90#res_hyddb]] | [[res_read_hyd.f90]]:49 |
| `res_hyddb%mores` | `integer` | none | month the res becomes operational | [[reservoir_data_module.f90#res_hyddb]] | [[res_read_hyd.f90]]:49 |
| `res_hyddb%psa` | `real` | ha | res surface area when res is filled to princ spillway | [[reservoir_data_module.f90#res_hyddb]] | [[res_read_hyd.f90]]:49 |
| `res_hyddb%pvol` | `real` | ha-m | vol of water needed to fill the res to the princ spillway (read in as ha-m and converted to m^3) | [[reservoir_data_module.f90#res_hyddb]] | [[res_read_hyd.f90]]:49 |
| `res_hyddb%esa` | `real` | ha | res surface area when res is filled to emerg spillway | [[reservoir_data_module.f90#res_hyddb]] | [[res_read_hyd.f90]]:49 |
| `res_hyddb%evol` | `real` | ha-m | vol of water needed to fill the res to the emerg spillway (read in as ha-m and converted to m^3) | [[reservoir_data_module.f90#res_hyddb]] | [[res_read_hyd.f90]]:49 |
| `res_hyddb%k` | `real` | mm/hr | hydraulic conductivity of the res bottom | [[reservoir_data_module.f90#res_hyddb]] | [[res_read_hyd.f90]]:49 |
| `res_hyddb%evrsv` | `real` | none | lake evap coeff | [[reservoir_data_module.f90#res_hyddb]] | [[res_read_hyd.f90]]:49 |
| `res_hyddb%br1` | `real` | none | vol-surface area coefficient for reservoirs (model estimates if zero) | [[reservoir_data_module.f90#res_hyddb]] | [[res_read_hyd.f90]]:49 |
| `res_hyddb%br2` | `real` | none | vol-surface area coefficient for reservoirs (model estimates if zero) | [[reservoir_data_module.f90#res_hyddb]] | [[res_read_hyd.f90]]:49 |
