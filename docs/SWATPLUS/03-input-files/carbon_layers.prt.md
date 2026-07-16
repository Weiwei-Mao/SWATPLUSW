---
type: input
tags:
  - swat/input
  - swat/auxiliary-input
file: carbon_layers.prt
ext: prt
cio_field: []
read_by:
  - carbon_layers_read.f90
purpose: ""
---

# carbon_layers.prt

> [!info] Input File
> Referenced directly by source code or by a default file-name constant outside the main `file.cio` list.

## Overview
- **Declared in `file.cio` field**: not listed directly; referenced by source code or a default file-name constant.
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[carbon_layers_read.f90]]

## File Structure
- [[carbon_layers_read.f90]] source line 32: reads `titldum`
- [[carbon_layers_read.f90]] source line 34: reads `header`
- [[carbon_layers_read.f90]] source line 37: reads `n_lyr`

## Parameters
| Parameter | Type | Units | Meaning | Source | Reader line |
|---|---|---|---|---|---:|
| `n_lyr` | `integer` |  |  | `carbon_layers_read.f90:23` | [[carbon_layers_read.f90]]:37 |
