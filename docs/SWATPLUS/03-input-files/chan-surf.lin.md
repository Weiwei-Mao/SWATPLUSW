---
type: input
tags:
  - swat/input
file: chan-surf.lin
ext: lin
cio_field: chan_surf
read_by:
  - overbank_read.f90
purpose: ""
---

# chan-surf.lin

> [!info] Input File
> Declared in `file.cio` field `chan_surf`. See [[file.cio]] for the controlling file map.

## Overview
- **Declared in `file.cio` field**: `chan_surf`
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[overbank_read.f90]]

## File Structure
- [[overbank_read.f90]] source line 32: reads `titldum`
- [[overbank_read.f90]] source line 34: reads `mcha_sp`
- [[overbank_read.f90]] source line 36: reads `header`
- [[overbank_read.f90]] source line 40: reads `i`
- [[overbank_read.f90]] source line 48: reads `titldum`
- [[overbank_read.f90]] source line 50: reads `mcha_sp`
- [[overbank_read.f90]] source line 52: reads `header`
- [[overbank_read.f90]] source line 58: reads `i`, `namedum`, `nspu`
- [[overbank_read.f90]] source line 65: reads `numb`, `sd_ch(i)%fp%name`, `sd_ch(i)%fp%obj_tot`, `(sd_ch(i)%fp%obtyp(isp), sd_ch(i)%fp%obtypno(isp), isp = 1, nspu)`

## Parameters
| Parameter | Type | Units | Meaning | Source | Reader line |
|---|---|---|---|---|---:|
| `mcha_sp` | `integer` |  |  | `overbank_read.f90:18` | [[overbank_read.f90]]:34 |
| `i` | `integer` | none | counter | `overbank_read.f90:19` | [[overbank_read.f90]]:40 |
| `namedum` | `character (len=16)` |  |  | `overbank_read.f90:12` | [[overbank_read.f90]]:58 |
| `nspu` | `integer` |  |  | `overbank_read.f90:15` | [[overbank_read.f90]]:58 |
| `numb` | `integer` |  |  | `overbank_read.f90:21` | [[overbank_read.f90]]:65 |
| `sd_ch%fp%name` | `character(len=25)` |  | name of flood plain | [[sd_channel_module.f90#sd_ch]] | [[overbank_read.f90]]:65 |
| `sd_ch%fp%obj_tot` | `integer` |  | number of objects (hru and/or ru) in the flood plain | [[sd_channel_module.f90#sd_ch]] | [[overbank_read.f90]]:65 |
| `sd_ch%fp%obtyp%fp%obtypno` | `character (len=3), dimension(:), allocatable` |  | object type- 1=hru, 2=hru_lte, 11=export coef, etc | [[sd_channel_module.f90#sd_ch]] | [[overbank_read.f90]]:65 |
