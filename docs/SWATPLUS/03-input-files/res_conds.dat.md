---
type: input
tags:
  - swat/input
  - swat/auxiliary-input
file: res_conds.dat
ext: dat
cio_field: []
read_by:
  - res_read_conds.f90
purpose: ""
---

# res_conds.dat

> [!info] Input File
> Referenced directly by source code or by a default file-name constant outside the main `file.cio` list.

## Overview
- **Declared in `file.cio` field**: not listed directly; referenced by source code or a default file-name constant.
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[res_read_conds.f90]]

## File Structure
- [[res_read_conds.f90]] source line 22: reads `title`
- [[res_read_conds.f90]] source line 24: reads `max_table`
- [[res_read_conds.f90]] source line 32: reads `ctbl(ictbl)%name`, `ctbl(ictbl)%num_conds`, `ctbl(ictbl)%num_modules`
- [[res_read_conds.f90]] source line 39: reads `isub_con`
- [[res_read_conds.f90]] source line 42: reads `ctbl(ictbl)%conds(ii)%num_conds`, `(ctbl(ictbl)%conds(ii)%scon(icc), icc = 1, isub_con)`, `ctbl(ictbl)%conds(ii)%action`
- [[res_read_conds.f90]] source line 48: reads `tnum_conds`
- [[res_read_conds.f90]] source line 54: reads `isub_con`
- [[res_read_conds.f90]] source line 57: reads `ctbl(ictbl)%mods(imod)%con(ii)%num_conds`, `(ctbl(ictbl)%mods(imod)%con(ii)%scon(icc), icc = 1, isub_con)`, `ctbl(ictbl)%mods(imod)%con(ii)%action`

## Parameters
| Parameter | Type | Units | Meaning | Source | Reader line |
|---|---|---|---|---|---:|
| `title` | `character (len=80)` |  |  | `res_read_conds.f90:8` | [[res_read_conds.f90]]:22 |
| `max_table` | `integer` |  |  | `res_read_conds.f90:9` | [[res_read_conds.f90]]:24 |
| `ctbl%name` | `character(25)` |  |  | [[reservoir_conditions_module.f90#ctbl]] | [[res_read_conds.f90]]:32 |
| `ctbl%num_conds` | `integer` |  |  | [[reservoir_conditions_module.f90#ctbl]] | [[res_read_conds.f90]]:32 |
| `ctbl%num_modules` | `integer` |  |  | [[reservoir_conditions_module.f90#ctbl]] | [[res_read_conds.f90]]:32 |
| `isub_con` | `integer` |  |  | `res_read_conds.f90:13` | [[res_read_conds.f90]]:39 |
| `ctbl%conds%num_conds` | `integer` |  |  | [[reservoir_conditions_module.f90#ctbl]] | [[res_read_conds.f90]]:42 |
| `ctbl%conds%scon` | `cond` |  |  | [[reservoir_conditions_module.f90#ctbl]] | [[res_read_conds.f90]]:42 |
| `ctbl%conds%action` | `real` |  |  | [[reservoir_conditions_module.f90#ctbl]] | [[res_read_conds.f90]]:42 |
| `tnum_conds` | `integer` |  |  | `res_read_conds.f90:10` | [[res_read_conds.f90]]:48 |
| `ctbl%mods%con%num_conds` | `integer` |  |  | [[reservoir_conditions_module.f90#ctbl]] | [[res_read_conds.f90]]:57 |
| `ctbl%mods%con%scon` | `cond` |  |  | [[reservoir_conditions_module.f90#ctbl]] | [[res_read_conds.f90]]:57 |
| `ctbl%mods%con%action` | `real` |  |  | [[reservoir_conditions_module.f90#ctbl]] | [[res_read_conds.f90]]:57 |
