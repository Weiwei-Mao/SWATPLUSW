---
type: input
tags:
  - swat/input
  - swat/auxiliary-input
file: cs_channel.ini
ext: ini
cio_field: []
read_by:
  - cs_cha_read.f90
purpose: ""
---

# cs_channel.ini

> [!info] Input File
> Referenced directly by source code or by a default file-name constant outside the main `file.cio` list.

## Overview
- **Declared in `file.cio` field**: not listed directly; referenced by source code or a default file-name constant.
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[cs_cha_read.f90]]

## File Structure
- [[cs_cha_read.f90]] source line 29: reads `titldum`
- [[cs_cha_read.f90]] source line 31: reads `header`
- [[cs_cha_read.f90]] source line 35: reads `titldum`
- [[cs_cha_read.f90]] source line 49: reads `titldum`
- [[cs_cha_read.f90]] source line 52: reads `header`
- [[cs_cha_read.f90]] source line 55: reads `cs_cha_ini(icsi)%name`, `cs_cha_ini(icsi)%conc`

## Parameters
| Parameter | Type | Units | Meaning | Source | Reader line |
|---|---|---|---|---|---:|
| `cs_cha_ini%name` | `character (len=16)` |  | name of the constituent - points to salt ion database | [[constituent_mass_module.f90#cs_cha_ini]] | [[cs_cha_read.f90]]:55 |
| `cs_cha_ini%conc` | `real, dimension (:), allocatable` | g/m3 | constituent concentration at start of simulation | [[constituent_mass_module.f90#cs_cha_ini]] | [[cs_cha_read.f90]]:55 |
