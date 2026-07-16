---
type: input
tags:
  - swat/input
  - swat/auxiliary-input
file: puddle.ops
ext: ops
cio_field: []
read_by:
  - mgt_read_puddle.f90
purpose: ""
---

# puddle.ops

> [!info] Input File
> Referenced directly by source code or by a default file-name constant outside the main `file.cio` list.

## Overview
- **Declared in `file.cio` field**: not listed directly; referenced by source code or a default file-name constant.
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[mgt_read_puddle.f90]]

## File Structure
- [[mgt_read_puddle.f90]] source line 24: reads `titldum`
- [[mgt_read_puddle.f90]] source line 26: reads `header`
- [[mgt_read_puddle.f90]] source line 29: reads `titldum`
- [[mgt_read_puddle.f90]] source line 36: reads `titldum`
- [[mgt_read_puddle.f90]] source line 38: reads `header`
- [[mgt_read_puddle.f90]] source line 42: reads `pudl_db(ic)`

## Parameters
| Parameter | Type | Units | Meaning | Source | Reader line |
|---|---|---|---|---|---:|
| `pudl_db%name` | `character (len=40)` |  |  | [[mgt_operations_module.f90#pudl_db]] | [[mgt_read_puddle.f90]]:42 |
| `pudl_db%wet_hc` | `real` | mm/h | hydraulic conductivity of upper layer of soil after puddling | [[mgt_operations_module.f90#pudl_db]] | [[mgt_read_puddle.f90]]:42 |
| `pudl_db%sed` | `real` | ppm | sediment concentration after puddling | [[mgt_operations_module.f90#pudl_db]] | [[mgt_read_puddle.f90]]:42 |
| `pudl_db%orgn` | `real` | ppm | organic N concentration after puddling | [[mgt_operations_module.f90#pudl_db]] | [[mgt_read_puddle.f90]]:42 |
| `pudl_db%sedp` | `real` | ppm | organic P concentration after puddling | [[mgt_operations_module.f90#pudl_db]] | [[mgt_read_puddle.f90]]:42 |
| `pudl_db%no3` | `real` | ppm | NO3-N concentration after puddling | [[mgt_operations_module.f90#pudl_db]] | [[mgt_read_puddle.f90]]:42 |
| `pudl_db%solp` | `real` | ppm | mineral (soluble P) concentration after puddling | [[mgt_operations_module.f90#pudl_db]] | [[mgt_read_puddle.f90]]:42 |
| `pudl_db%nh3` | `real` | ppm | NH3 concentration after puddling | [[mgt_operations_module.f90#pudl_db]] | [[mgt_read_puddle.f90]]:42 |
| `pudl_db%no2` | `real` | ppm | NO2 concentration after puddling | [[mgt_operations_module.f90#pudl_db]] | [[mgt_read_puddle.f90]]:42 |
