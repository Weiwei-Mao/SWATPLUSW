---
type: input
tags:
  - swat/input
file: lum.dtl
ext: dtl
cio_field: dtbl_lum
read_by:
  - dtbl_lum_read.f90
purpose: ""
---

# lum.dtl

> [!info] Input File
> Declared in `file.cio` field `dtbl_lum`. See [[file.cio]] for the controlling file map.

## Overview
- **Declared in `file.cio` field**: `dtbl_lum`
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[dtbl_lum_read.f90]]

## File Structure
- [[dtbl_lum_read.f90]] source line 42: reads `titldum`
- [[dtbl_lum_read.f90]] source line 44: reads `mdtbl`
- [[dtbl_lum_read.f90]] source line 46: reads (no targets parsed)
- [[dtbl_lum_read.f90]] source line 51: reads `header`
- [[dtbl_lum_read.f90]] source line 53: reads `dtbl_lum(i)%name`, `dtbl_lum(i)%conds`, `dtbl_lum(i)%alts`, `dtbl_lum(i)%acts`
- [[dtbl_lum_read.f90]] source line 67: reads `header`
- [[dtbl_lum_read.f90]] source line 70: reads `dtbl_lum(i)%cond(ic)`, `(dtbl_lum(i)%alt(ic,ial), ial = 1, dtbl_lum(i)%alts)`
- [[dtbl_lum_read.f90]] source line 74: reads `dtbl_lum(i)%cond(ic)%var`, `dtbl_lum(i)%frac_app`
- [[dtbl_lum_read.f90]] source line 93: reads `header`
- [[dtbl_lum_read.f90]] source line 96: reads `dtbl_lum(i)%act(iac)`, `(dtbl_lum(i)%act_outcomes(iac,ial), ial = 1, dtbl_lum(i)%alts)`

## Parameters
| Parameter | Type | Units | Meaning | Source | Reader line |
|---|---|---|---|---|---:|
| `mdtbl` | `integer` | none | ending of loop | `dtbl_lum_read.f90:23` | [[dtbl_lum_read.f90]]:44 |
| `dtbl_lum%name` | `character (len=40)` |  | name of the decision table | [[conditional_module.f90#dtbl_lum]] | [[dtbl_lum_read.f90]]:53 |
| `dtbl_lum%conds` | `integer` |  | number of conditions | [[conditional_module.f90#dtbl_lum]] | [[dtbl_lum_read.f90]]:53 |
| `dtbl_lum%alts` | `integer` |  | number of alternatives | [[conditional_module.f90#dtbl_lum]] | [[dtbl_lum_read.f90]]:53 |
| `dtbl_lum%acts` | `integer` |  | number of actions | [[conditional_module.f90#dtbl_lum]] | [[dtbl_lum_read.f90]]:53 |
| `dtbl_lum%cond` | `conditions_var` |  | conditions | [[conditional_module.f90#dtbl_lum]] | [[dtbl_lum_read.f90]]:70 |
| `dtbl_lum%alt%alts` | `character(len=25), dimension(:,:), allocatable` |  | condition alternatives | [[conditional_module.f90#dtbl_lum]] | [[dtbl_lum_read.f90]]:70 |
| `dtbl_lum%cond%var` | `character(len=25)` |  | conditions / condition variable (ie volume, flow, sw, time, etc) | [[conditional_module.f90#dtbl_lum]] | [[dtbl_lum_read.f90]]:74 |
| `dtbl_lum%frac_app` | `real` |  | fraction of time (during each window) the application occurs | [[conditional_module.f90#dtbl_lum]] | [[dtbl_lum_read.f90]]:74 |
| `dtbl_lum%act` | `actions_var` |  | actions | [[conditional_module.f90#dtbl_lum]] | [[dtbl_lum_read.f90]]:96 |
| `dtbl_lum%act_outcomes%alts` | `character(len=1), dimension(:,:), allocatable` |  | action outcomes ("y" to perform action; "n" to not perform) | [[conditional_module.f90#dtbl_lum]] | [[dtbl_lum_read.f90]]:96 |
