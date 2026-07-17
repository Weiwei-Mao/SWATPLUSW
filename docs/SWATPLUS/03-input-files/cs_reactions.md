---
type: input
tags:
  - swat/input
  - swat/auxiliary-input
file: cs_reactions
ext: 
cio_field: []
read_by:
  - cs_reactions_read.f90
purpose: ""
---

# cs_reactions

> [!info] Input File
> Referenced directly by source code or by a default file-name constant outside the main `file.cio` list.

## Overview
- **Declared in `file.cio` field**: not listed directly; referenced by source code or a default file-name constant.
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[cs_reactions_read.f90]]

## File Structure
- [[cs_reactions_read.f90]] source line 35: reads `titldum`
- [[cs_reactions_read.f90]] source line 42: reads `header`
- [[cs_reactions_read.f90]] source line 43: reads `num_rct`, `num_groups`
- [[cs_reactions_read.f90]] source line 46: reads `(rct(icount,igroup),igroup=1,num_groups)`
- [[cs_reactions_read.f90]] source line 50: reads `header`
- [[cs_reactions_read.f90]] source line 51: reads `num_geol_shale`
- [[cs_reactions_read.f90]] source line 54: reads `(rct_shale(icount,irct),irct=1,3)`
- [[cs_reactions_read.f90]] source line 58: reads `header`
- [[cs_reactions_read.f90]] source line 64: reads `hru_dum`, `group`, `(shale_fractions(ishale),ishale=1,num_geol_shale)`
- [[cs_reactions_read.f90]] source line 82: reads `header`
- [[cs_reactions_read.f90]] source line 88: reads `aqu_dum`, `group`, `(shale_fractions(ishale),ishale=1,num_geol_shale)`

## Parameters
| Parameter | Type | Units | Meaning | Source | Reader line |
|---|---|---|---|---|---:|
| `num_rct` | `integer` |  | number of reaction parameters | `cs_reactions_read.f90:22` | [[cs_reactions_read.f90]]:43 |
| `num_groups` | `integer` |  | number of reaction groups | `cs_reactions_read.f90:23` | [[cs_reactions_read.f90]]:43 |
| `rct` | `real, dimension(:,:), allocatable` |  | reaction parameters | [[cs_data_module.f90#rct]] | [[cs_reactions_read.f90]]:46 |
| `num_geol_shale` | `integer` |  |  | [[cs_data_module.f90#num_geol_shale]] | [[cs_reactions_read.f90]]:51 |
| `rct_shale` | `real, dimension(:,:), allocatable` |  | reaction parameters for shale | [[cs_data_module.f90#rct_shale]] | [[cs_reactions_read.f90]]:54 |
| `hru_dum` | `integer` |  |  | `cs_reactions_read.f90:18` | [[cs_reactions_read.f90]]:64 |
| `group` | `integer` |  |  | `cs_reactions_read.f90:17` | [[cs_reactions_read.f90]]:64 |
| `shale_fractions` | `real` |  | fraction of shale that covers an area's object | `cs_reactions_read.f90:24` | [[cs_reactions_read.f90]]:64 |
| `aqu_dum` | `integer` |  |  | `cs_reactions_read.f90:19` | [[cs_reactions_read.f90]]:88 |
