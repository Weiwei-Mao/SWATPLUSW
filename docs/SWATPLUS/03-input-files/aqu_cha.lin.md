---
type: input
tags:
  - swat/input
file: aqu_cha.lin
ext: lin
cio_field: aqu_cha
read_by:
  - aqu2d_read.f90
purpose: ""
---

# aqu_cha.lin

> [!info] Input File
> Declared in `file.cio` field `aqu_cha`. See [[file.cio]] for the controlling file map.

## Overview
- **Declared in `file.cio` field**: `aqu_cha`
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[aqu2d_read.f90]]

## File Structure
- [[aqu2d_read.f90]] source line 36: reads `titldum`
- [[aqu2d_read.f90]] source line 38: reads `header`
- [[aqu2d_read.f90]] source line 42: reads `i`
- [[aqu2d_read.f90]] source line 51: reads `titldum`
- [[aqu2d_read.f90]] source line 52: reads `header`
- [[aqu2d_read.f90]] source line 56: reads `iaq`, `namedum`, `nspu`
- [[aqu2d_read.f90]] source line 62: reads `numb`, `aq_ch(iaq)%name`, `nspu`, `(elem_cnt(isp), isp = 1, nspu)`

## Parameters
| Parameter | Type | Units | Meaning | Source | Reader line |
|---|---|---|---|---|---:|
| `i` | `integer` | none | counter | `aqu2d_read.f90:18` | [[aqu2d_read.f90]]:42 |
| `iaq` | `integer` | none | counter | `aqu2d_read.f90:21` | [[aqu2d_read.f90]]:56 |
| `namedum` | `character (len=16)` |  |  | `aqu2d_read.f90:13` | [[aqu2d_read.f90]]:56 |
| `nspu` | `integer` |  |  | `aqu2d_read.f90:16` | [[aqu2d_read.f90]]:56 |
| `numb` | `integer` |  |  | `aqu2d_read.f90:20` | [[aqu2d_read.f90]]:62 |
| `aq_ch%name` | `character(len=16)` |  |  | [[hydrograph_module.f90#aq_ch]] | [[aqu2d_read.f90]]:62 |
| `elem_cnt` | `integer, dimension (:), allocatable` |  |  | [[hydrograph_module.f90#elem_cnt]] | [[aqu2d_read.f90]]:62 |
