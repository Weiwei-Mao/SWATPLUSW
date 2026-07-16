---
type: input
tags:
  - swat/input
file: sweep.ops
ext: ops
cio_field: sweep_ops
read_by:
  - mgt_read_sweepops.f90
purpose: ""
---

# sweep.ops

> [!info] Input File
> Declared in `file.cio` field `sweep_ops`. See [[file.cio]] for the controlling file map.

## Overview
- **Declared in `file.cio` field**: `sweep_ops`
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[mgt_read_sweepops.f90]]

## File Structure
- [[mgt_read_sweepops.f90]] source line 28: reads `titldum`
- [[mgt_read_sweepops.f90]] source line 30: reads `header`
- [[mgt_read_sweepops.f90]] source line 33: reads `titldum`
- [[mgt_read_sweepops.f90]] source line 41: reads `titldum`
- [[mgt_read_sweepops.f90]] source line 43: reads `header`
- [[mgt_read_sweepops.f90]] source line 47: reads `sweepop_db(isweepop)`

## Parameters
| Parameter | Type | Units | Meaning | Source | Reader line |
|---|---|---|---|---|---:|
| `sweepop_db%name` | `character (len=40)` |  |  | [[mgt_operations_module.f90#sweepop_db]] | [[mgt_read_sweepops.f90]]:47 |
| `sweepop_db%eff` | `real` | none | removal efficiency of sweeping operation | [[mgt_operations_module.f90#sweepop_db]] | [[mgt_read_sweepops.f90]]:47 |
| `sweepop_db%fr_curb` | `real` | none | availability factor, the fraction of the curb length that is sweepable | [[mgt_operations_module.f90#sweepop_db]] | [[mgt_read_sweepops.f90]]:47 |
