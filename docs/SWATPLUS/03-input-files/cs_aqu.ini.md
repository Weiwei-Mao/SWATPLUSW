---
type: input
tags:
  - swat/input
  - swat/auxiliary-input
file: cs_aqu.ini
ext: ini
cio_field: []
read_by:
  - cs_aqu_read.f90
purpose: ""
---

# cs_aqu.ini

> [!info] Input File
> Referenced directly by source code or by a default file-name constant outside the main `file.cio` list.

## Overview
- **Declared in `file.cio` field**: not listed directly; referenced by source code or a default file-name constant.
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[cs_aqu_read.f90]]

## File Structure
- [[cs_aqu_read.f90]] source line 24: reads `titldum`
- [[cs_aqu_read.f90]] source line 26: reads `header`
- [[cs_aqu_read.f90]] source line 28: reads `header`
- [[cs_aqu_read.f90]] source line 32: reads `titldum`
- [[cs_aqu_read.f90]] source line 47: reads `titldum`
- [[cs_aqu_read.f90]] source line 49: reads `header`
- [[cs_aqu_read.f90]] source line 51: reads `header`
- [[cs_aqu_read.f90]] source line 55: reads `cs_aqu_ini(ics)%name`, `cs_aqu_ini(ics)%aqu`

## Parameters
| Parameter | Type | Units | Meaning | Source | Reader line |
|---|---|---|---|---|---:|
| `cs_aqu_ini%name` | `character (len=16)` |  | name of the constituent - points to constituent database | [[constituent_mass_module.f90#cs_aqu_ini]] | [[cs_aqu_read.f90]]:55 |
| `cs_aqu_ini%aqu` | `real, dimension (:), allocatable` | ppm | concentration, sorbed mass at start of simulation | [[constituent_mass_module.f90#cs_aqu_ini]] | [[cs_aqu_read.f90]]:55 |
