---
type: input
tags:
  - swat/input
file: scen_lu.dtl
ext: dtl
cio_field: dtbl_scen
read_by:
  - dtbl_scen_read.f90
purpose: ""
---

# scen_lu.dtl

> [!info] Input File
> Declared in `file.cio` field `dtbl_scen`. See [[file.cio]] for the controlling file map.

## Overview
- **Declared in `file.cio` field**: `dtbl_scen`
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[dtbl_scen_read.f90]]

## File Structure
- [[dtbl_scen_read.f90]] source line 36: reads `titldum`
- [[dtbl_scen_read.f90]] source line 38: reads `mdtbl`
- [[dtbl_scen_read.f90]] source line 40: reads (no targets parsed)
- [[dtbl_scen_read.f90]] source line 45: reads `header`
- [[dtbl_scen_read.f90]] source line 47: reads `dtbl_scen(i)%name`, `dtbl_scen(i)%conds`, `dtbl_scen(i)%alts`, `dtbl_scen(i)%acts`
- [[dtbl_scen_read.f90]] source line 61: reads `header`
- [[dtbl_scen_read.f90]] source line 64: reads `dtbl_scen(i)%cond(ic)`, `(dtbl_scen(i)%alt(ic,ial), ial = 1, dtbl_scen(i)%alts)`
- [[dtbl_scen_read.f90]] source line 69: reads `header`
- [[dtbl_scen_read.f90]] source line 72: reads `dtbl_scen(i)%act(iac)`, `(dtbl_scen(i)%act_outcomes(iac,ial), ial = 1, dtbl_scen(i)%alts)`
- [[dtbl_scen_read.f90]] source line 75: reads (no targets parsed)

## Parameters
| Parameter | Type | Units | Meaning | Source | Reader line |
|---|---|---|---|---|---:|
| `mdtbl` | `integer` | none | ending of loop | `dtbl_scen_read.f90:19` | [[dtbl_scen_read.f90]]:38 |
| `dtbl_scen%name` | `character (len=40)` |  | name of the decision table | [[conditional_module.f90#dtbl_scen]] | [[dtbl_scen_read.f90]]:47 |
| `dtbl_scen%conds` | `integer` |  | number of conditions | [[conditional_module.f90#dtbl_scen]] | [[dtbl_scen_read.f90]]:47 |
| `dtbl_scen%alts` | `integer` |  | number of alternatives | [[conditional_module.f90#dtbl_scen]] | [[dtbl_scen_read.f90]]:47 |
| `dtbl_scen%acts` | `integer` |  | number of actions | [[conditional_module.f90#dtbl_scen]] | [[dtbl_scen_read.f90]]:47 |
| `dtbl_scen%cond` | `conditions_var` |  | conditions | [[conditional_module.f90#dtbl_scen]] | [[dtbl_scen_read.f90]]:64 |
| `dtbl_scen%alt%alts` | `character(len=25), dimension(:,:), allocatable` |  | condition alternatives | [[conditional_module.f90#dtbl_scen]] | [[dtbl_scen_read.f90]]:64 |
| `dtbl_scen%act` | `actions_var` |  | actions | [[conditional_module.f90#dtbl_scen]] | [[dtbl_scen_read.f90]]:72 |
| `dtbl_scen%act_outcomes%alts` | `character(len=1), dimension(:,:), allocatable` |  | action outcomes ("y" to perform action; "n" to not perform) | [[conditional_module.f90#dtbl_scen]] | [[dtbl_scen_read.f90]]:72 |
