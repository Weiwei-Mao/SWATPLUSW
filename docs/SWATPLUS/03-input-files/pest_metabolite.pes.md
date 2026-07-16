---
type: input
tags:
  - swat/input
  - swat/auxiliary-input
file: pest_metabolite.pes
ext: pes
cio_field: []
read_by:
  - pest_metabolite_read.f90
purpose: ""
---

# pest_metabolite.pes

> [!info] Input File
> Referenced directly by source code or by a default file-name constant outside the main `file.cio` list.

## Overview
- **Declared in `file.cio` field**: not listed directly; referenced by source code or a default file-name constant.
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[pest_metabolite_read.f90]]

## File Structure
- [[pest_metabolite_read.f90]] source line 30: reads `titldum`
- [[pest_metabolite_read.f90]] source line 32: reads `header`
- [[pest_metabolite_read.f90]] source line 35: reads `titldum`, `num_metab`
- [[pest_metabolite_read.f90]] source line 37: reads `titldum`
- [[pest_metabolite_read.f90]] source line 44: reads `titldum`
- [[pest_metabolite_read.f90]] source line 46: reads `header`
- [[pest_metabolite_read.f90]] source line 50: reads `parent_name`, `num_metab`
- [[pest_metabolite_read.f90]] source line 60: reads `pestcp(ip)%daughter(imeta)%name`, `pestcp(ip)%daughter(imeta)%foliar_fr`, `pestcp(ip)%daughter(imeta)%soil_fr`, `pestcp(ip)%daughter(imeta)%aq_fr`, `pestcp(ip)%daughter(imeta)%ben_fr`

## Parameters
| Parameter | Type | Units | Meaning | Source | Reader line |
|---|---|---|---|---|---:|
| `num_metab` | `integer` | none | number of matabolites for each parent | `pest_metabolite_read.f90:21` | [[pest_metabolite_read.f90]]:35 |
| `parent_name` | `character (len=16)` |  |  | `pest_metabolite_read.f90:13` | [[pest_metabolite_read.f90]]:50 |
| `pestcp%daughter%name` | `character(len=16)` |  | daughter pesticide name | [[pesticide_data_module.f90#pestcp]] | [[pest_metabolite_read.f90]]:60 |
| `pestcp%daughter%foliar_fr` | `real` | 0-1 | fraction of parent foilar degrading to daughter | [[pesticide_data_module.f90#pestcp]] | [[pest_metabolite_read.f90]]:60 |
| `pestcp%daughter%soil_fr` | `real` | 0-1 | fraction of parent soil degrading to daughter | [[pesticide_data_module.f90#pestcp]] | [[pest_metabolite_read.f90]]:60 |
| `pestcp%daughter%aq_fr` | `real` | 0-1 | fraction of parent aquatic degrading to daughter | [[pesticide_data_module.f90#pestcp]] | [[pest_metabolite_read.f90]]:60 |
| `pestcp%daughter%ben_fr` | `real` | 0-1 | fraction of parent benthic degrading to daughter | [[pesticide_data_module.f90#pestcp]] | [[pest_metabolite_read.f90]]:60 |
