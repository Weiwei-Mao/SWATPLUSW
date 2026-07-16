---
type: input
tags:
  - swat/input
file: water_allocation.wro
ext: wro
cio_field: transfer_wro
read_by:
  - water_allocation_read.f90
purpose: ""
---

# water_allocation.wro

> [!info] Input File
> Declared in `file.cio` field `transfer_wro`. See [[file.cio]] for the controlling file map.

## Overview
- **Declared in `file.cio` field**: `transfer_wro`
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[water_allocation_read.f90]]

## File Structure
- [[water_allocation_read.f90]] source line 48: reads `titldum`
- [[water_allocation_read.f90]] source line 50: reads `imax`
- [[water_allocation_read.f90]] source line 65: reads `header`
- [[water_allocation_read.f90]] source line 67: reads `wallo(iwro)%name`, `wallo(iwro)%rule_typ`, `wallo(iwro)%trn_obs`
- [[water_allocation_read.f90]] source line 70: reads `header`
- [[water_allocation_read.f90]] source line 88: reads `i`
- [[water_allocation_read.f90]] source line 92: reads `k`, `wallo(iwro)%trn(i)%trn_typ`, `wallo(iwro)%trn(i)%trn_typ_name`, `wallo(iwro)%trn(i)%amount`, `wallo(iwro)%trn(i)%right`, `wallo(iwro)%trn(i)%src_num`
- [[water_allocation_read.f90]] source line 139: reads `k`, `wallo(iwro)%trn(i)%trn_typ`, `wallo(iwro)%trn(i)%trn_typ_name`, `wallo(iwro)%trn(i)%amount`, `wallo(iwro)%trn(i)%right`, `wallo(iwro)%trn(i)%src_num`, `wallo(iwro)%trn(i)%dtbl_src`, `(wallo(iwro)%trn(i)%src(isrc), isrc = 1, num_src)`, `wallo(iwro)%trn(i)%rcv`

## Parameters
| Parameter | Type | Units | Meaning | Source | Reader line |
|---|---|---|---|---|---:|
| `imax` | `integer` | none | determine max number for array (imax) and total number in file | `water_allocation_read.f90:20` | [[water_allocation_read.f90]]:50 |
| `wallo%name` | `character (len=25)` |  | name of the water allocation object | [[water_allocation_module.f90#wallo]] | [[water_allocation_read.f90]]:67 |
| `wallo%rule_typ` | `character (len=25)` |  | rule type to allocate water | [[water_allocation_module.f90#wallo]] | [[water_allocation_read.f90]]:67 |
| `wallo%trn_obs` | `integer` |  | number of transfer objects | [[water_allocation_module.f90#wallo]] | [[water_allocation_read.f90]]:67 |
| `i` | `integer` | none | counter | `water_allocation_read.f90:22` | [[water_allocation_read.f90]]:88 |
| `k` | `integer` | none | counter | `water_allocation_read.f90:23` | [[water_allocation_read.f90]]:92 |
| `wallo%trn%trn_typ` | `character (len=10)` |  | dimension by transfer objects / transfer type - decision table, recall, ave daily | [[water_allocation_module.f90#wallo]] | [[water_allocation_read.f90]]:92 |
| `wallo%trn%trn_typ_name` | `character (len=40)` |  | dimension by transfer objects / transfer type name of table or recall | [[water_allocation_module.f90#wallo]] | [[water_allocation_read.f90]]:92 |
| `wallo%trn%amount` | `real` |  | dimension by transfer objects / m3 per day for urban objects and mm for hru | [[water_allocation_module.f90#wallo]] | [[water_allocation_read.f90]]:92 |
| `wallo%trn%right` | `character (len=2)` |  | dimension by transfer objects / water right (sr -senior or jr - junior right) | [[water_allocation_module.f90#wallo]] | [[water_allocation_read.f90]]:92 |
| `wallo%trn%src_num` | `integer` |  | dimension by transfer objects / number of source objects | [[water_allocation_module.f90#wallo]] | [[water_allocation_read.f90]]:92 |
| `wallo%trn%dtbl_src` | `character (len=25)` |  | dimension by transfer objects / decision table name to allocate sources | [[water_allocation_module.f90#wallo]] | [[water_allocation_read.f90]]:139 |
| `wallo%trn%src` | `transfer_source_objects` |  | dimension by transfer objects / sequential source objects as listed in wallo object | [[water_allocation_module.f90#wallo]] | [[water_allocation_read.f90]]:139 |
| `wallo%trn%rcv` | `transfer_receiving_objects` |  | dimension by transfer objects / receiving object | [[water_allocation_module.f90#wallo]] | [[water_allocation_read.f90]]:139 |
