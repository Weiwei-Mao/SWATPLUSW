---
type: input
tags:
  - swat/input
  - swat/auxiliary-input
file: manure_om.frt
ext: frt
cio_field: []
read_by:
  - manure_orgmin_read.f90
purpose: ""
---

# manure_om.frt

> [!info] Input File
> Referenced directly by source code or by a default file-name constant outside the main `file.cio` list.

## Overview
- **Declared in `file.cio` field**: not listed directly; referenced by source code or a default file-name constant.
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[manure_orgmin_read.f90]]

## File Structure
- [[manure_orgmin_read.f90]] source line 28: reads `titldum`
- [[manure_orgmin_read.f90]] source line 30: reads `header`
- [[manure_orgmin_read.f90]] source line 33: reads `titldum`
- [[manure_orgmin_read.f90]] source line 41: reads `titldum`
- [[manure_orgmin_read.f90]] source line 43: reads `header`
- [[manure_orgmin_read.f90]] source line 47: reads `manure_om(it)%name`, `manure_om(it)%frac_water`, `manure_om(it)%fcbn`, `manure_om(it)%fminn`, `manure_om(it)%fminp`, `manure_om(it)%forgn`, `manure_om(it)%forgp`, `manure_om(it)%fnh3n`, `manure_om(it)%description`

## Parameters
| Parameter | Type | Units | Meaning | Source | Reader line |
|---|---|---|---|---|---:|
| `manure_om%name` | `character(len=64)` |  | Identifier used to crosswalk fertilizer entries, constructed from manure_region, manure_source, and manure_type | [[fertilizer_data_module.f90#manure_om]] | [[manure_orgmin_read.f90]]:47 |
| `manure_om%frac_water` | `real` | kg water/(kg manure + kg_water) | frac of manure which is water | [[fertilizer_data_module.f90#manure_om]] | [[manure_orgmin_read.f90]]:47 |
| `manure_om%fcbn` | `real` | kg C/kg frt | frac of fert which is carbon | [[fertilizer_data_module.f90#manure_om]] | [[manure_orgmin_read.f90]]:47 |
| `manure_om%fminn` | `real` | kg minN/kg frt | frac of fert which is mineral nitrogen (NO3+NH3) | [[fertilizer_data_module.f90#manure_om]] | [[manure_orgmin_read.f90]]:47 |
| `manure_om%fminp` | `real` | kg minN/kg frt | frac of fert which is mineral phoshorus | [[fertilizer_data_module.f90#manure_om]] | [[manure_orgmin_read.f90]]:47 |
| `manure_om%forgn` | `real` | kg orgN/kg frt | frac of fert which is org N | [[fertilizer_data_module.f90#manure_om]] | [[manure_orgmin_read.f90]]:47 |
| `manure_om%forgp` | `real` | kg orgP/kg frt | frac of fert which is org P | [[fertilizer_data_module.f90#manure_om]] | [[manure_orgmin_read.f90]]:47 |
| `manure_om%fnh3n` | `real` | kg NH3-N/kg N | frac of mineral N content of fert which is NH3 | [[fertilizer_data_module.f90#manure_om]] | [[manure_orgmin_read.f90]]:47 |
| `manure_om%description` | `character(len=64)` | na | description of manure type | [[fertilizer_data_module.f90#manure_om]] | [[manure_orgmin_read.f90]]:47 |
