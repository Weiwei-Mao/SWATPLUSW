---
type: input
tags:
  - swat/input
  - swat/auxiliary-input
file: salt_channel.ini
ext: ini
cio_field: []
read_by:
  - salt_cha_read.f90
purpose: ""
---

# salt_channel.ini

> [!info] Input File
> Referenced directly by source code or by a default file-name constant outside the main `file.cio` list.

## Overview
- **Declared in `file.cio` field**: not listed directly; referenced by source code or a default file-name constant.
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[salt_cha_read.f90]]

## File Structure
- [[salt_cha_read.f90]] source line 28: reads `titldum`
- [[salt_cha_read.f90]] source line 30: reads `header`
- [[salt_cha_read.f90]] source line 34: reads `titldum`
- [[salt_cha_read.f90]] source line 48: reads `titldum`
- [[salt_cha_read.f90]] source line 51: reads `header`
- [[salt_cha_read.f90]] source line 54: reads `salt_cha_ini(isalti)%name`, `salt_cha_ini(isalti)%conc`

## Parameters
| Parameter | Type | Units | Meaning | Source | Reader line |
|---|---|---|---|---|---:|
| `salt_cha_ini%name` | `character (len=16)` |  | name of the constituent - points to salt ion database | [[constituent_mass_module.f90#salt_cha_ini]] | [[salt_cha_read.f90]]:54 |
| `salt_cha_ini%conc` | `real, dimension (:), allocatable` | g/m3 | salt ion concentration at start of simulation | [[constituent_mass_module.f90#salt_cha_ini]] | [[salt_cha_read.f90]]:54 |
