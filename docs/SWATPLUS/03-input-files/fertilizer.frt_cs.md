---
type: input
tags:
  - swat/input
  - swat/auxiliary-input
file: fertilizer.frt_cs
ext: frt_cs
cio_field: []
read_by:
  - cs_fert_read.f90
purpose: ""
---

# fertilizer.frt_cs

> [!info] Input File
> Referenced directly by source code or by a default file-name constant outside the main `file.cio` list.

## Overview
- **Declared in `file.cio` field**: not listed directly; referenced by source code or a default file-name constant.
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[cs_fert_read.f90]]

## File Structure
- [[cs_fert_read.f90]] source line 26: reads `titldum`
- [[cs_fert_read.f90]] source line 27: reads `header`
- [[cs_fert_read.f90]] source line 37: reads `fert_cs(icsi)`

## Parameters
| Parameter | Type | Units | Meaning | Source | Reader line |
|---|---|---|---|---|---:|
| `fert_cs%fertnm` | `character(len=16)` |  |  | [[cs_module.f90#fert_cs]] | [[cs_fert_read.f90]]:37 |
| `fert_cs%seo4` | `real` | kg seo4/ha | fertilizer load of seo4 (kg/ha) | [[cs_module.f90#fert_cs]] | [[cs_fert_read.f90]]:37 |
| `fert_cs%seo3` | `real` | kg seo3/ha | fertilizer load of seo3 (kg/ha) | [[cs_module.f90#fert_cs]] | [[cs_fert_read.f90]]:37 |
| `fert_cs%boron` | `real` | kg boron/ha | fertilizer load of boron (kg/ha) | [[cs_module.f90#fert_cs]] | [[cs_fert_read.f90]]:37 |
