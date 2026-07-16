---
type: input
tags:
  - swat/input
file: hydrology.wet
ext: wet
cio_field: hyd_wet
read_by:
  - wet_read_hyd.f90
purpose: ""
---

# hydrology.wet

> [!info] Input File
> Declared in `file.cio` field `hyd_wet`. See [[file.cio]] for the controlling file map.

## Overview
- **Declared in `file.cio` field**: `hyd_wet`
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[wet_read_hyd.f90]]

## File Structure
- [[wet_read_hyd.f90]] source line 33: reads `titldum`
- [[wet_read_hyd.f90]] source line 35: reads `header`
- [[wet_read_hyd.f90]] source line 38: reads `titldum`
- [[wet_read_hyd.f90]] source line 47: reads `titldum`
- [[wet_read_hyd.f90]] source line 49: reads `header`
- [[wet_read_hyd.f90]] source line 53: reads `titldum`
- [[wet_read_hyd.f90]] source line 56: reads `wet_hyddb(ires)`

## Parameters
| Parameter | Type | Units | Meaning | Source | Reader line |
|---|---|---|---|---|---:|
| `wet_hyddb%name` | `character(len=25)` |  |  | [[reservoir_data_module.f90#wet_hyddb]] | [[wet_read_hyd.f90]]:56 |
| `wet_hyddb%psa` | `real` | frac | fraction of hru area at principal spillway (ie: when surface inlet riser flow starts) | [[reservoir_data_module.f90#wet_hyddb]] | [[wet_read_hyd.f90]]:56 |
| `wet_hyddb%pdep` | `real` | mm | average depth of water at principal spillway | [[reservoir_data_module.f90#wet_hyddb]] | [[wet_read_hyd.f90]]:56 |
| `wet_hyddb%esa` | `real` | frac | fraction of hru area at emergency spillway (ie: when starts to spill into ditch) | [[reservoir_data_module.f90#wet_hyddb]] | [[wet_read_hyd.f90]]:56 |
| `wet_hyddb%edep` | `real` | mm | average depth of water at emergency spillway | [[reservoir_data_module.f90#wet_hyddb]] | [[wet_read_hyd.f90]]:56 |
| `wet_hyddb%k` | `real` | mm/hr | hydraulic conductivity of the wetland bottom | [[reservoir_data_module.f90#wet_hyddb]] | [[wet_read_hyd.f90]]:56 |
| `wet_hyddb%evrsv` | `real` | none | wetland evap coeff | [[reservoir_data_module.f90#wet_hyddb]] | [[wet_read_hyd.f90]]:56 |
| `wet_hyddb%acoef` | `real` | none | vol-surface area coefficient for hru impoundment | [[reservoir_data_module.f90#wet_hyddb]] | [[wet_read_hyd.f90]]:56 |
| `wet_hyddb%bcoef` | `real` | none | vol-depth coefficient for hru impoundment | [[reservoir_data_module.f90#wet_hyddb]] | [[wet_read_hyd.f90]]:56 |
| `wet_hyddb%ccoef` | `real` | none | vol-depth coefficient for hru impoundment | [[reservoir_data_module.f90#wet_hyddb]] | [[wet_read_hyd.f90]]:56 |
| `wet_hyddb%frac` | `real` | none | fraction of hru that drains into impoundment | [[reservoir_data_module.f90#wet_hyddb]] | [[wet_read_hyd.f90]]:56 |
