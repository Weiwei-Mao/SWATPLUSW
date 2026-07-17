---
type: input
tags:
  - swat/input
file: management.sch
ext: sch
cio_field: management_sch
read_by:
  - mgt_read_mgtops.f90
purpose: ""
---

# management.sch

> [!info] Input File
> Declared in `file.cio` field `management_sch`. See [[file.cio]] for the controlling file map.

## Overview
- **Declared in `file.cio` field**: `management_sch`
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[mgt_read_mgtops.f90]]

## File Structure
- [[mgt_read_mgtops.f90]] source line 34: reads `titldum`
- [[mgt_read_mgtops.f90]] source line 36: reads `header`
- [[mgt_read_mgtops.f90]] source line 39: reads `titldum`, `nops`, `nauto`
- [[mgt_read_mgtops.f90]] source line 42: reads `titldum`
- [[mgt_read_mgtops.f90]] source line 46: reads `titldum`
- [[mgt_read_mgtops.f90]] source line 55: reads `titldum`
- [[mgt_read_mgtops.f90]] source line 57: reads `header`
- [[mgt_read_mgtops.f90]] source line 61: reads `sched(isched)%name`, `sched(isched)%num_ops`, `sched(isched)%num_autos`
- [[mgt_read_mgtops.f90]] source line 69: reads `sched(isched)%auto_name(iauto)`
- [[mgt_read_mgtops.f90]] source line 77: reads `sched(isched)%auto_name(iauto)`, `sched(isched)%auto_crop`
- [[mgt_read_mgtops.f90]] source line 83: reads `sched(isched)%auto_name(iauto)`, `sched(isched)%auto_crop`

## Parameters
| Parameter | Type | Units | Meaning | Source | Reader line |
|---|---|---|---|---|---:|
| `nops` | `integer` |  | end of loop | `mgt_read_mgtops.f90:11` | [[mgt_read_mgtops.f90]]:39 |
| `nauto` | `integer` |  | end of loop | `mgt_read_mgtops.f90:18` | [[mgt_read_mgtops.f90]]:39 |
| `sched%name` | `character(len=40)` |  |  | [[mgt_operations_module.f90#sched]] | [[mgt_read_mgtops.f90]]:61 |
| `sched%num_ops` | `integer` |  |  | [[mgt_operations_module.f90#sched]] | [[mgt_read_mgtops.f90]]:61 |
| `sched%num_autos` | `integer` |  |  | [[mgt_operations_module.f90#sched]] | [[mgt_read_mgtops.f90]]:61 |
| `sched%auto_name` | `character(len=40), dimension (:), allocatable` |  |  | [[mgt_operations_module.f90#sched]] | [[mgt_read_mgtops.f90]]:69 |
| `sched%auto_crop` | `character(len=40), dimension (:), allocatable` |  |  | [[mgt_operations_module.f90#sched]] | [[mgt_read_mgtops.f90]]:77 |
