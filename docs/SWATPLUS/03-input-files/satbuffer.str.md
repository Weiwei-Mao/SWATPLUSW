---
type: input
tags:
  - swat/input
  - swat/auxiliary-input
file: satbuffer.str
ext: str
cio_field: []
read_by:
  - sat_buff_read.f90
purpose: ""
---

# satbuffer.str

> [!info] Input File
> Referenced directly by source code or by a default file-name constant outside the main `file.cio` list.

## Overview
- **Declared in `file.cio` field**: not listed directly; referenced by source code or a default file-name constant.
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[sat_buff_read.f90]]

## File Structure
- [[sat_buff_read.f90]] source line 35: reads `titldum`
- [[sat_buff_read.f90]] source line 37: reads `header`
- [[sat_buff_read.f90]] source line 40: reads `titldum`
- [[sat_buff_read.f90]] source line 46: reads `titldum`
- [[sat_buff_read.f90]] source line 48: reads `header`
- [[sat_buff_read.f90]] source line 55: reads `satbuff_db(ibuff)`

## Parameters
| Parameter | Type | Units | Meaning | Source | Reader line |
|---|---|---|---|---|---:|
| `satbuff_db%name` | `character(len=40)` |  |  | [[hru_module.f90#satbuff_db]] | [[sat_buff_read.f90]]:55 |
| `satbuff_db%hru_src` | `integer` |  | source of tile inflow | [[hru_module.f90#satbuff_db]] | [[sat_buff_read.f90]]:55 |
| `satbuff_db%frac_src` | `real` |  | fration of source hru contributing to tile flow | [[hru_module.f90#satbuff_db]] | [[sat_buff_read.f90]]:55 |
| `satbuff_db%flocon_dtbl` | `character(len=40)` |  | decision table to control flow into buffer hru | [[hru_module.f90#satbuff_db]] | [[sat_buff_read.f90]]:55 |
| `satbuff_db%hru_rcv` | `integer` |  | receiving (buffer) hru | [[hru_module.f90#satbuff_db]] | [[sat_buff_read.f90]]:55 |
| `satbuff_db%lyr` | `integer` |  | soil layer for incoming tile flow (0 = surface) | [[hru_module.f90#satbuff_db]] | [[sat_buff_read.f90]]:55 |
