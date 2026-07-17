---
type: input
tags:
  - swat/input
  - swat/auxiliary-input
file: salt_road
ext: 
cio_field: []
read_by:
  - salt_roadsalt_read.f90
purpose: ""
---

# salt_road

> [!info] Input File
> Referenced directly by source code or by a default file-name constant outside the main `file.cio` list.

## Overview
- **Declared in `file.cio` field**: not listed directly; referenced by source code or a default file-name constant.
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[salt_roadsalt_read.f90]]

## File Structure
- [[salt_roadsalt_read.f90]] source line 41: reads (no targets parsed)
- [[salt_roadsalt_read.f90]] source line 42: reads (no targets parsed)
- [[salt_roadsalt_read.f90]] source line 43: reads (no targets parsed)
- [[salt_roadsalt_read.f90]] source line 44: reads (no targets parsed)
- [[salt_roadsalt_read.f90]] source line 57: reads `station_name`
- [[salt_roadsalt_read.f90]] source line 59: reads `salt_ion`, `rdapp_salt(iadep)%salt(isalt)%road`
- [[salt_roadsalt_read.f90]] source line 65: reads `station_name`
- [[salt_roadsalt_read.f90]] source line 68: reads `salt_ion`, `(rdapp_salt(iadep)%salt(isalt)%roadmo(imo),imo=1,atmodep_cont%num)`
- [[salt_roadsalt_read.f90]] source line 74: reads `station_name`
- [[salt_roadsalt_read.f90]] source line 77: reads `salt_ion`, `(rdapp_salt(iadep)%salt(isalt)%roadyr(iyr),iyr=1,atmodep_cont%num)`

## Parameters
| Parameter | Type | Units | Meaning | Source | Reader line |
|---|---|---|---|---|---:|
| `station_name` | `character (len=15)` |  |  | `salt_roadsalt_read.f90:14` | [[salt_roadsalt_read.f90]]:57 |
| `salt_ion` | `character (len=4)` |  |  | `salt_roadsalt_read.f90:13` | [[salt_roadsalt_read.f90]]:59 |
| `rdapp_salt%salt%road` | `real` |  | ave annual salt ion loading via road salt application (kg/ha) | [[climate_module.f90#rdapp_salt]] | [[salt_roadsalt_read.f90]]:59 |
| `rdapp_salt%salt%roadmo%num` | `real, dimension(:), allocatable` |  | monthly salt ion loading via road salt application (kg/ha) | [[climate_module.f90#rdapp_salt]] | [[salt_roadsalt_read.f90]]:68 |
| `rdapp_salt%salt%roadyr%num` | `real, dimension(:), allocatable` |  | yearly salt ion loading via road salt application (kg/ha) | [[climate_module.f90#rdapp_salt]] | [[salt_roadsalt_read.f90]]:77 |
