---
type: input
tags:
  - swat/input
file: object.prt
ext: prt
cio_field: object_prt
read_by:
  - object_read_output.f90
purpose: ""
---

# object.prt

> [!info] Input File
> Declared in `file.cio` field `object_prt`. See [[file.cio]] for the controlling file map.

## Overview
- **Declared in `file.cio` field**: `object_prt`
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[object_read_output.f90]]

## File Structure
- [[object_read_output.f90]] source line 29: reads `titldum`
- [[object_read_output.f90]] source line 31: reads `header`
- [[object_read_output.f90]] source line 34: reads `i`
- [[object_read_output.f90]] source line 43: reads `titldum`
- [[object_read_output.f90]] source line 45: reads `header`
- [[object_read_output.f90]] source line 49: reads `ii`
- [[object_read_output.f90]] source line 52: reads `k`, `ob_out(ii)%obtyp`, `ob_out(ii)%obtypno`, `ob_out(ii)%hydtyp`, `ob_out(ii)%filename`

## Parameters
| Parameter | Type | Units | Meaning | Source | Reader line |
|---|---|---|---|---|---:|
| `i` | `integer` | none | counter | `object_read_output.f90:14` | [[object_read_output.f90]]:34 |
| `ii` | `integer` |  | none !counter | `object_read_output.f90:15` | [[object_read_output.f90]]:49 |
| `k` | `integer` |  |  | `object_read_output.f90:16` | [[object_read_output.f90]]:52 |
| `ob_out%obtyp` | `character (len=10)` |  | object type: hru,hlt,hs,rxc,dr,out,sdc | [[hydrograph_module.f90#ob_out]] | [[object_read_output.f90]]:52 |
| `ob_out%obtypno` | `integer` |  | object type number: 1=hru, 2=hru_lte, 3=channel | [[hydrograph_module.f90#ob_out]] | [[object_read_output.f90]]:52 |
| `ob_out%hydtyp` | `character (len=20)` |  | hydrograph type: tot,rhg,sur,lat,til | [[hydrograph_module.f90#ob_out]] | [[object_read_output.f90]]:52 |
| `ob_out%filename` | `character (len=26)` |  | file with hydrograph output from the object | [[hydrograph_module.f90#ob_out]] | [[object_read_output.f90]]:52 |
