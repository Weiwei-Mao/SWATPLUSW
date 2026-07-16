---
type: input
tags:
  - swat/input
file: flo_con.dtl
ext: dtl
cio_field: dtbl_flo
read_by:
  - dtbl_flocon_read.f90
purpose: ""
---

# flo_con.dtl

> [!info] Input File
> Declared in `file.cio` field `dtbl_flo`. See [[file.cio]] for the controlling file map.

## Overview
- **Declared in `file.cio` field**: `dtbl_flo`
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[dtbl_flocon_read.f90]]

## File Structure
- [[dtbl_flocon_read.f90]] source line 32: reads `titldum`
- [[dtbl_flocon_read.f90]] source line 34: reads `mdtbl`
- [[dtbl_flocon_read.f90]] source line 36: reads (no targets parsed)
- [[dtbl_flocon_read.f90]] source line 41: reads `header`
- [[dtbl_flocon_read.f90]] source line 43: reads `dtbl_flo(i)%name`, `dtbl_flo(i)%conds`, `dtbl_flo(i)%alts`, `dtbl_flo(i)%acts`
- [[dtbl_flocon_read.f90]] source line 54: reads `header`
- [[dtbl_flocon_read.f90]] source line 57: reads `dtbl_flo(i)%cond(ic)`, `(dtbl_flo(i)%alt(ic,ial), ial = 1, dtbl_flo(i)%alts)`
- [[dtbl_flocon_read.f90]] source line 62: reads `header`
- [[dtbl_flocon_read.f90]] source line 65: reads `dtbl_flo(i)%act(iac)`, `(dtbl_flo(i)%act_outcomes(iac,ial), ial = 1, dtbl_flo(i)%alts)`
- [[dtbl_flocon_read.f90]] source line 68: reads (no targets parsed)

## Parameters
| Parameter | Type | Units | Meaning | Source | Reader line |
|---|---|---|---|---|---:|
| `mdtbl` | `integer` | none | ending of loop | `dtbl_flocon_read.f90:14` | [[dtbl_flocon_read.f90]]:34 |
| `dtbl_flo%name` | `character (len=40)` |  | name of the decision table | [[conditional_module.f90#dtbl_flo]] | [[dtbl_flocon_read.f90]]:43 |
| `dtbl_flo%conds` | `integer` |  | number of conditions | [[conditional_module.f90#dtbl_flo]] | [[dtbl_flocon_read.f90]]:43 |
| `dtbl_flo%alts` | `integer` |  | number of alternatives | [[conditional_module.f90#dtbl_flo]] | [[dtbl_flocon_read.f90]]:43 |
| `dtbl_flo%acts` | `integer` |  | number of actions | [[conditional_module.f90#dtbl_flo]] | [[dtbl_flocon_read.f90]]:43 |
| `dtbl_flo%cond` | `conditions_var` |  | conditions | [[conditional_module.f90#dtbl_flo]] | [[dtbl_flocon_read.f90]]:57 |
| `dtbl_flo%alt%alts` | `character(len=25), dimension(:,:), allocatable` |  | condition alternatives | [[conditional_module.f90#dtbl_flo]] | [[dtbl_flocon_read.f90]]:57 |
| `dtbl_flo%act` | `actions_var` |  | actions | [[conditional_module.f90#dtbl_flo]] | [[dtbl_flocon_read.f90]]:65 |
| `dtbl_flo%act_outcomes%alts` | `character(len=1), dimension(:,:), allocatable` |  | action outcomes ("y" to perform action; "n" to not perform) | [[conditional_module.f90#dtbl_flo]] | [[dtbl_flocon_read.f90]]:65 |
