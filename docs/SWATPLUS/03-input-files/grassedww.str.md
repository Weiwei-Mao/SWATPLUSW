---
type: input
tags:
  - swat/input
file: grassedww.str
ext: str
cio_field: grassww_str
read_by:
  - scen_read_grwway.f90
purpose: ""
---

# grassedww.str

> [!info] Input File
> Declared in `file.cio` field `grassww_str`. See [[file.cio]] for the controlling file map.

## Overview
- **Declared in `file.cio` field**: `grassww_str`
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[scen_read_grwway.f90]]

## File Structure
- [[scen_read_grwway.f90]] source line 26: reads `titldum`
- [[scen_read_grwway.f90]] source line 28: reads `header`
- [[scen_read_grwway.f90]] source line 31: reads `titldum`
- [[scen_read_grwway.f90]] source line 39: reads `titldum`
- [[scen_read_grwway.f90]] source line 41: reads `header`
- [[scen_read_grwway.f90]] source line 45: reads `grwaterway_db(igrwwop)`

## Parameters
| Parameter | Type | Units | Meaning | Source | Reader line |
|---|---|---|---|---|---:|
| `grwaterway_db%name` | `character (len=40)` |  |  | [[mgt_operations_module.f90#grwaterway_db]] | [[scen_read_grwway.f90]]:45 |
| `grwaterway_db%grwat_i` | `integer` | none | On/off Flag for waterway simulation | [[mgt_operations_module.f90#grwaterway_db]] | [[scen_read_grwway.f90]]:45 |
| `grwaterway_db%grwat_n` | `real` | none | Mannings"s n for grassed waterway | [[mgt_operations_module.f90#grwaterway_db]] | [[scen_read_grwway.f90]]:45 |
| `grwaterway_db%grwat_spcon` | `real` | none | sediment transport coefficant defined by user | [[mgt_operations_module.f90#grwaterway_db]] | [[scen_read_grwway.f90]]:45 |
| `grwaterway_db%grwat_d` | `real` | m | depth of Grassed waterway | [[mgt_operations_module.f90#grwaterway_db]] | [[scen_read_grwway.f90]]:45 |
| `grwaterway_db%grwat_w` | `real` | none | width of grass waterway | [[mgt_operations_module.f90#grwaterway_db]] | [[scen_read_grwway.f90]]:45 |
| `grwaterway_db%grwat_l` | `real` | km | length of Grass Waterway | [[mgt_operations_module.f90#grwaterway_db]] | [[scen_read_grwway.f90]]:45 |
| `grwaterway_db%grwat_s` | `real` | m/m | slope of grass waterway | [[mgt_operations_module.f90#grwaterway_db]] | [[scen_read_grwway.f90]]:45 |
