---
type: input
tags:
  - swat/input
file: filterstrip.str
ext: str
cio_field: fstrip_str
read_by:
  - scen_read_filtstrip.f90
purpose: ""
---

# filterstrip.str

> [!info] Input File
> Declared in `file.cio` field `fstrip_str`. See [[file.cio]] for the controlling file map.

## Overview
- **Declared in `file.cio` field**: `fstrip_str`
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[scen_read_filtstrip.f90]]

## File Structure
- [[scen_read_filtstrip.f90]] source line 26: reads `titldum`
- [[scen_read_filtstrip.f90]] source line 28: reads `header`
- [[scen_read_filtstrip.f90]] source line 31: reads `titldum`
- [[scen_read_filtstrip.f90]] source line 39: reads `titldum`
- [[scen_read_filtstrip.f90]] source line 41: reads `header`
- [[scen_read_filtstrip.f90]] source line 45: reads `filtstrip_db(ifiltop)`

## Parameters
| Parameter | Type | Units | Meaning | Source | Reader line |
|---|---|---|---|---|---:|
| `filtstrip_db%name` | `character (len=40)` |  |  | [[mgt_operations_module.f90#filtstrip_db]] | [[scen_read_filtstrip.f90]]:45 |
| `filtstrip_db%vfsi` | `integer` |  | on/off flag for vegetative filter strip | [[mgt_operations_module.f90#filtstrip_db]] | [[scen_read_filtstrip.f90]]:45 |
| `filtstrip_db%vfsratio` | `real` |  | contouring USLE P factor | [[mgt_operations_module.f90#filtstrip_db]] | [[scen_read_filtstrip.f90]]:45 |
| `filtstrip_db%vfscon` | `real` |  | fraction of the total runoff from the entire field | [[mgt_operations_module.f90#filtstrip_db]] | [[scen_read_filtstrip.f90]]:45 |
| `filtstrip_db%vfsch` | `real` |  | fraction of flow entering the most concentrated 10% of the VFS. which is fully channelized | [[mgt_operations_module.f90#filtstrip_db]] | [[scen_read_filtstrip.f90]]:45 |
