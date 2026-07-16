---
type: input
tags:
  - swat/input
  - swat/auxiliary-input
file: chancell.gw
ext: gw
cio_field: []
read_by:
  - basin_read_objs.f90
  - gwflow_chan_read.f90
purpose: ""
---

# chancell.gw

> [!info] Input File
> Referenced directly by source code or by a default file-name constant outside the main `file.cio` list.

## Overview
- **Declared in `file.cio` field**: not listed directly; referenced by source code or a default file-name constant.
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[basin_read_objs.f90]]
- [[gwflow_chan_read.f90]]

## File Structure
- [[basin_read_objs.f90]] source line 53: reads `header`
- [[basin_read_objs.f90]] source line 55: reads (no targets parsed)
- [[basin_read_objs.f90]] source line 56: reads `header`
- [[basin_read_objs.f90]] source line 62: reads `riv_id`
- [[gwflow_chan_read.f90]] source line 52: reads (no targets parsed)
- [[gwflow_chan_read.f90]] source line 53: reads (no targets parsed)
- [[gwflow_chan_read.f90]] source line 56: reads `') line_buf`

## Parameters
| Parameter | Type | Units | Meaning | Source | Reader line |
|---|---|---|---|---|---:|
| `riv_id` | `integer` |  | id of gwflow river cell | `basin_read_objs.f90:21` | [[basin_read_objs.f90]]:62 |
