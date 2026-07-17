---
type: input
tags:
  - swat/input
  - swat/auxiliary-input
file: cs_streamobs
ext: 
cio_field: []
read_by:
  - cs_cha_read.f90
purpose: ""
---

# cs_streamobs

> [!info] Input File
> Referenced directly by source code or by a default file-name constant outside the main `file.cio` list.

## Overview
- **Declared in `file.cio` field**: not listed directly; referenced by source code or a default file-name constant.
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[cs_cha_read.f90]]

## File Structure
- [[cs_cha_read.f90]] source line 67: reads (no targets parsed)
- [[cs_cha_read.f90]] source line 68: reads `cs_str_nobs`
- [[cs_cha_read.f90]] source line 71: reads `cs_str_obs(i)`

## Parameters
| Parameter | Type | Units | Meaning | Source | Reader line |
|---|---|---|---|---|---:|
| `cs_str_nobs` | `integer` |  | number of channels for daily output | [[constituent_mass_module.f90#cs_str_nobs]] | [[cs_cha_read.f90]]:68 |
| `cs_str_obs` | `integer, dimension (:), allocatable` |  | list of channels for daily output | [[constituent_mass_module.f90#cs_str_obs]] | [[cs_cha_read.f90]]:71 |
