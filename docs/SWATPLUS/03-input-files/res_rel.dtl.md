---
type: input
tags:
  - swat/input
file: res_rel.dtl
ext: dtl
cio_field: dtbl_res
read_by:
  - dtbl_res_read.f90
purpose: ""
---

# res_rel.dtl

> [!info] Input File
> Declared in `file.cio` field `dtbl_res`. See [[file.cio]] for the controlling file map.

## Overview
- **Declared in `file.cio` field**: `dtbl_res`
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[dtbl_res_read.f90]]

## File Structure
- [[dtbl_res_read.f90]] source line 37: reads `titldum`
- [[dtbl_res_read.f90]] source line 39: reads `mdtbl`
- [[dtbl_res_read.f90]] source line 41: reads (no targets parsed)
- [[dtbl_res_read.f90]] source line 46: reads `header`
- [[dtbl_res_read.f90]] source line 48: reads `dtbl_res(i)%name`, `dtbl_res(i)%conds`, `dtbl_res(i)%alts`, `dtbl_res(i)%acts`
- [[dtbl_res_read.f90]] source line 59: reads `header`
- [[dtbl_res_read.f90]] source line 62: reads `dtbl_res(i)%cond(ic)`, `(dtbl_res(i)%alt(ic,ial), ial = 1, dtbl_res(i)%alts)`
- [[dtbl_res_read.f90]] source line 67: reads `header`
- [[dtbl_res_read.f90]] source line 70: reads `dtbl_res(i)%act(iac)`, `(dtbl_res(i)%act_outcomes(iac,ial), ial = 1, dtbl_res(i)%alts)`
- [[dtbl_res_read.f90]] source line 73: reads (no targets parsed)

## Parameters
| Parameter | Type | Units | Meaning | Source | Reader line |
|---|---|---|---|---|---:|
| `mdtbl` | `integer` | none | ending of loop | `dtbl_res_read.f90:20` | [[dtbl_res_read.f90]]:39 |
| `dtbl_res%name` | `character (len=40)` |  | name of the decision table | [[conditional_module.f90#dtbl_res]] | [[dtbl_res_read.f90]]:48 |
| `dtbl_res%conds` | `integer` |  | number of conditions | [[conditional_module.f90#dtbl_res]] | [[dtbl_res_read.f90]]:48 |
| `dtbl_res%alts` | `integer` |  | number of alternatives | [[conditional_module.f90#dtbl_res]] | [[dtbl_res_read.f90]]:48 |
| `dtbl_res%acts` | `integer` |  | number of actions | [[conditional_module.f90#dtbl_res]] | [[dtbl_res_read.f90]]:48 |
| `dtbl_res%cond` | `conditions_var` |  | conditions | [[conditional_module.f90#dtbl_res]] | [[dtbl_res_read.f90]]:62 |
| `dtbl_res%alt%alts` | `character(len=25), dimension(:,:), allocatable` |  | condition alternatives | [[conditional_module.f90#dtbl_res]] | [[dtbl_res_read.f90]]:62 |
| `dtbl_res%act` | `actions_var` |  | actions | [[conditional_module.f90#dtbl_res]] | [[dtbl_res_read.f90]]:70 |
| `dtbl_res%act_outcomes%alts` | `character(len=1), dimension(:,:), allocatable` |  | action outcomes ("y" to perform action; "n" to not perform) | [[conditional_module.f90#dtbl_res]] | [[dtbl_res_read.f90]]:70 |
