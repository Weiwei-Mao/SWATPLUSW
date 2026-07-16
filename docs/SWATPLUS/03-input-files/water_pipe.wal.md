---
type: input
tags:
  - swat/input
  - swat/auxiliary-input
file: water_pipe.wal
ext: wal
cio_field: []
read_by:
  - water_pipe_read.f90
purpose: ""
---

# water_pipe.wal

> [!info] Input File
> Referenced directly by source code or by a default file-name constant outside the main `file.cio` list.

## Overview
- **Declared in `file.cio` field**: not listed directly; referenced by source code or a default file-name constant.
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[water_pipe_read.f90]]

## File Structure
- [[water_pipe_read.f90]] source line 33: reads `titldum`
- [[water_pipe_read.f90]] source line 35: reads `imax`
- [[water_pipe_read.f90]] source line 36: reads `header`
- [[water_pipe_read.f90]] source line 43: reads `header`
- [[water_pipe_read.f90]] source line 45: reads `i`, `pipe(ipipe)%name`, `pipe(ipipe)%stor_mx`, `pipe(ipipe)%ddown_days`, `pipe(ipipe)%loss_fr`, `num_aqu`
- [[water_pipe_read.f90]] source line 52: reads `i`, `pipe(ipipe)%name`, `pipe(ipipe)%stor_mx`, `pipe(ipipe)%ddown_days`, `pipe(ipipe)%loss_fr`, `pipe(ipipe)%num_aqu`, `(pipe(ipipe)%aqu_loss(iaq), iaq = 1, num_aqu)`

## Parameters
| Parameter | Type | Units | Meaning | Source | Reader line |
|---|---|---|---|---|---:|
| `imax` | `integer` | none | determine max number for array (imax) and total number in file | `water_pipe_read.f90:15` | [[water_pipe_read.f90]]:35 |
| `i` | `integer` | none | counter | `water_pipe_read.f90:17` | [[water_pipe_read.f90]]:45 |
| `pipe%name` | `character (len=25)` |  | name of the water tower or pipe | [[water_allocation_module.f90#pipe]] | [[water_pipe_read.f90]]:45 |
| `pipe%stor_mx` | `real` |  | m3 !maximum storage in plant | [[water_allocation_module.f90#pipe]] | [[water_pipe_read.f90]]:45 |
| `pipe%ddown_days` | `real` |  | days !days to drawdown the storage to zero | [[water_allocation_module.f90#pipe]] | [[water_pipe_read.f90]]:45 |
| `pipe%loss_fr` | `real` |  | water loss during treament | [[water_allocation_module.f90#pipe]] | [[water_pipe_read.f90]]:45 |
| `num_aqu` | `integer` |  |  | `water_pipe_read.f90:19` | [[water_pipe_read.f90]]:45 |
| `pipe%num_aqu` | `integer` |  | number of aquifers | [[water_allocation_module.f90#pipe]] | [[water_pipe_read.f90]]:52 |
| `pipe%aqu_loss` | `aquifer_loss` |  |  | [[water_allocation_module.f90#pipe]] | [[water_pipe_read.f90]]:52 |
