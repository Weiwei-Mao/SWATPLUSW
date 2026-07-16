---
type: input
tags:
  - swat/input
  - swat/auxiliary-input
file: scen_dtl.upd
ext: upd
cio_field: []
read_by:
  - cal_cond_read.f90
purpose: ""
---

# scen_dtl.upd

> [!info] Input File
> Referenced directly by source code or by a default file-name constant outside the main `file.cio` list.

## Overview
- **Declared in `file.cio` field**: not listed directly; referenced by source code or a default file-name constant.
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[cal_cond_read.f90]]

## File Structure
- [[cal_cond_read.f90]] source line 44: reads `titldum`
- [[cal_cond_read.f90]] source line 46: reads `num_dtls`
- [[cal_cond_read.f90]] source line 52: reads `header`
- [[cal_cond_read.f90]] source line 56: reads `upd_cond(i)%max_hits`, `upd_cond(i)%typ`, `upd_cond(i)%dtbl`

## Parameters
| Parameter | Type | Units | Meaning | Source | Reader line |
|---|---|---|---|---|---:|
| `num_dtls` | `integer` | none | end of loop | `cal_cond_read.f90:31` | [[cal_cond_read.f90]]:46 |
| `upd_cond%max_hits` | `integer` |  | maximum number of times the table will be executed | [[calibration_data_module.f90#upd_cond]] | [[cal_cond_read.f90]]:56 |
| `upd_cond%typ` | `character(len=25)` |  | type of table- "lu_change" checks all hru; "hru_fr_change" sets all hru fractions | [[calibration_data_module.f90#upd_cond]] | [[cal_cond_read.f90]]:56 |
| `upd_cond%dtbl` | `character(len=25)` |  | points to ruleset in conditional.ctl for scheduling the update | [[calibration_data_module.f90#upd_cond]] | [[cal_cond_read.f90]]:56 |
