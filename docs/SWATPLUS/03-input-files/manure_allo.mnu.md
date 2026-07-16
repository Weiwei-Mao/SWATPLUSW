---
type: input
tags:
  - swat/input
  - swat/auxiliary-input
file: manure_allo.mnu
ext: mnu
cio_field: []
read_by:
  - manure_allocation_read.f90
purpose: ""
---

# manure_allo.mnu

> [!info] Input File
> Referenced directly by source code or by a default file-name constant outside the main `file.cio` list.

## Overview
- **Declared in `file.cio` field**: not listed directly; referenced by source code or a default file-name constant.
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[manure_allocation_read.f90]]

## File Structure
- [[manure_allocation_read.f90]] source line 40: reads `titldum`
- [[manure_allocation_read.f90]] source line 42: reads `imax`
- [[manure_allocation_read.f90]] source line 49: reads `header`
- [[manure_allocation_read.f90]] source line 51: reads `mallo(imro)%name`, `mallo(imro)%rule_typ`, `mallo(imro)%src_obs`, `mallo(imro)%trn_obs`
- [[manure_allocation_read.f90]] source line 54: reads `header`
- [[manure_allocation_read.f90]] source line 63: reads `i`
- [[manure_allocation_read.f90]] source line 67: reads `k`, `mallo(imro)%src(i)%mois_typ`, `mallo(imro)%src(i)%manure_typ`, `mallo(imro)%src(i)%lat`, `mallo(imro)%src(i)%long`, `mallo(imro)%src(i)%stor_init`, `mallo(imro)%src(i)%stor_max`, `mallo(imro)%src(i)%prod_mon`
- [[manure_allocation_read.f90]] source line 81: reads `header`
- [[manure_allocation_read.f90]] source line 90: reads `i`
- [[manure_allocation_read.f90]] source line 94: reads `k`, `mallo(imro)%trn(i)%ob_typ`, `mallo(imro)%trn(i)%ob_num`, `mallo(imro)%trn(i)%dtbl`, `mallo(imro)%trn(i)%right`

## Parameters
| Parameter | Type | Units | Meaning | Source | Reader line |
|---|---|---|---|---|---:|
| `imax` | `integer` | none | determine max number for array (imax) and total number in file | `manure_allocation_read.f90:17` | [[manure_allocation_read.f90]]:42 |
| `mallo%name` | `character (len=25)` |  | name of the water allocation object | [[manure_allocation_module.f90#mallo]] | [[manure_allocation_read.f90]]:51 |
| `mallo%rule_typ` | `character (len=25)` |  | rule type to allocate water | [[manure_allocation_module.f90#mallo]] | [[manure_allocation_read.f90]]:51 |
| `mallo%src_obs` | `integer` |  | number of source objects | [[manure_allocation_module.f90#mallo]] | [[manure_allocation_read.f90]]:51 |
| `mallo%trn_obs` | `integer` |  | number of demand objects | [[manure_allocation_module.f90#mallo]] | [[manure_allocation_read.f90]]:51 |
| `i` | `integer` | none | counter | `manure_allocation_read.f90:19` | [[manure_allocation_read.f90]]:63 |
| `k` | `integer` | none | counter | `manure_allocation_read.f90:20` | [[manure_allocation_read.f90]]:67 |
| `mallo%src%mois_typ` | `character (len=3)` |  | dimension by source objects / wet or dry | [[manure_allocation_module.f90#mallo]] | [[manure_allocation_read.f90]]:67 |
| `mallo%src%manure_typ` | `character (len=25)` |  | dimension by source objects / points to fertilizer.frt | [[manure_allocation_module.f90#mallo]] | [[manure_allocation_read.f90]]:67 |
| `mallo%src%lat` | `real` |  | dimension by source objects / latitude | [[manure_allocation_module.f90#mallo]] | [[manure_allocation_read.f90]]:67 |
| `mallo%src%long` | `real` |  | dimension by source objects / longitude | [[manure_allocation_module.f90#mallo]] | [[manure_allocation_read.f90]]:67 |
| `mallo%src%stor_init` | `real` |  | dimension by source objects / initial storage - tons | [[manure_allocation_module.f90#mallo]] | [[manure_allocation_read.f90]]:67 |
| `mallo%src%stor_max` | `real` |  | dimension by source objects / maximum storage - tons | [[manure_allocation_module.f90#mallo]] | [[manure_allocation_read.f90]]:67 |
| `mallo%src%prod_mon` | `real, dimension (12)` |  | dimension by source objects / average monthly manure produced - tons/month | [[manure_allocation_module.f90#mallo]] | [[manure_allocation_read.f90]]:67 |
| `mallo%trn%ob_typ` | `character (len=10)` |  | dimension by demand objects / hru (for application) or muni (treatmentb) or divert (interbasin diversion) | [[manure_allocation_module.f90#mallo]] | [[manure_allocation_read.f90]]:94 |
| `mallo%trn%ob_num` | `integer` |  | dimension by demand objects / number of the object type | [[manure_allocation_module.f90#mallo]] | [[manure_allocation_read.f90]]:94 |
| `mallo%trn%dtbl` | `character (len=25)` |  | dimension by demand objects / decision table name for manure/fert application | [[manure_allocation_module.f90#mallo]] | [[manure_allocation_read.f90]]:94 |
| `mallo%trn%right` | `character (len=2)` |  | dimension by demand objects / manure right (sr -senior or jr - junior right | [[manure_allocation_module.f90#mallo]] | [[manure_allocation_read.f90]]:94 |
