---
type: input
tags:
  - swat/input
file: codes.bsn
ext: bsn
cio_field: codes_bas
read_by:
  - basin_read_cc.f90
purpose: ""
---

# codes.bsn

> [!info] Input File
> Declared in `file.cio` field `codes_bas`. See [[file.cio]] for the controlling file map.

## Overview
- **Declared in `file.cio` field**: `codes_bas`
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[basin_read_cc.f90]]

## File Structure
- [[basin_read_cc.f90]] source line 20: reads `titldum`
- [[basin_read_cc.f90]] source line 22: reads `header`
- [[basin_read_cc.f90]] source line 24: reads `bsn_cc`

## Parameters
| Parameter | Type | Units | Meaning | Source | Reader line |
|---|---|---|---|---|---:|
| `bsn_cc%petfile` | `character(len=16)` |  | potential et filename | [[basin_module.f90#bsn_cc]] | [[basin_read_cc.f90]]:24 |
| `bsn_cc%wwqfile` | `character(len=16)` |  | watershed stream water quality filename | [[basin_module.f90#bsn_cc]] | [[basin_read_cc.f90]]:24 |
| `bsn_cc%pet` | `integer` |  | potential ET method code 0 = Priestley-Taylor 1 = Penman-Monteith 2 = Hargreaves method | [[basin_module.f90#bsn_cc]] | [[basin_read_cc.f90]]:24 |
| `bsn_cc%nam1` | `integer` |  | not used | [[basin_module.f90#bsn_cc]] | [[basin_read_cc.f90]]:24 |
| `bsn_cc%crk` | `integer` |  | crack flow code 1 = compute flow in cracks | [[basin_module.f90#bsn_cc]] | [[basin_read_cc.f90]]:24 |
| `bsn_cc%swift_out` | `integer` |  | write to SWIFT input file 0 = do not write 1 = write to swift_hru.inp | [[basin_module.f90#bsn_cc]] | [[basin_read_cc.f90]]:24 |
| `bsn_cc%sed_det` | `integer` |  | peak rate method 0 = NRCS dimensionless hydrograph with PRF 1 = half hour rainfall intensity method | [[basin_module.f90#bsn_cc]] | [[basin_read_cc.f90]]:24 |
| `bsn_cc%rte` | `integer` |  | water routing method 0 variable storage method 1 Muskingum method | [[basin_module.f90#bsn_cc]] | [[basin_read_cc.f90]]:24 |
| `bsn_cc%deg` | `integer` |  | not used | [[basin_module.f90#bsn_cc]] | [[basin_read_cc.f90]]:24 |
| `bsn_cc%wq` | `integer` |  | not used | [[basin_module.f90#bsn_cc]] | [[basin_read_cc.f90]]:24 |
| `bsn_cc%nostress` | `integer` |  | redefined to the sequence number -- changed to no nutrient stress 0 = all stresses applied 1 = turn off all plant stress 2 = turn off nutrient plant stress only | [[basin_module.f90#bsn_cc]] | [[basin_read_cc.f90]]:24 |
| `bsn_cc%cn` | `integer` |  | not used | [[basin_module.f90#bsn_cc]] | [[basin_read_cc.f90]]:24 |
| `bsn_cc%cfac` | `integer` |  | not used | [[basin_module.f90#bsn_cc]] | [[basin_read_cc.f90]]:24 |
| `bsn_cc%cswat` | `integer` |  | carbon code: 0 = off (static), 1 = C-FARM (reserved, not implemented), 2 = dynamic CENTURY/SWAT-C model. numbering aligned with legacy SWAT as directed by Srinivasan. = 0 Static soil carbon (old mineralization routines) = 1 C-FARM one carbon pool model = 2 Century model | [[basin_module.f90#bsn_cc]] | [[basin_read_cc.f90]]:24 |
| `bsn_cc%lapse` | `integer` |  | precip and temperature lapse rate control 0 = do not adjust for elevation 1 = adjust for elevation | [[basin_module.f90#bsn_cc]] | [[basin_read_cc.f90]]:24 |
| `bsn_cc%uhyd` | `integer` |  | Unit hydrograph method: 0 = triangular UH 1 = gamma function UH | [[basin_module.f90#bsn_cc]] | [[basin_read_cc.f90]]:24 |
| `bsn_cc%sed_ch` | `integer` |  | not used | [[basin_module.f90#bsn_cc]] | [[basin_read_cc.f90]]:24 |
| `bsn_cc%tdrn` | `integer` |  | tile drainage eq code 0 = tile flow using drawdown days equation 1 = tile flow using drainmod equations | [[basin_module.f90#bsn_cc]] | [[basin_read_cc.f90]]:24 |
| `bsn_cc%wtdn` | `integer` |  | shallow water table depth algorithms code 0 = depth using orig water table depth routine - fill to upper limit 1 = depth using drainmod water table depth routine | [[basin_module.f90#bsn_cc]] | [[basin_read_cc.f90]]:24 |
| `bsn_cc%sol_p_model` | `integer` |  | 0 = original soil P model in SWAT documentation 1 = new soil P model in Vadas and White (2010) | [[basin_module.f90#bsn_cc]] | [[basin_read_cc.f90]]:24 |
| `bsn_cc%gampt` | `integer` |  | 0 = curve number; 1 = Green and Ampt | [[basin_module.f90#bsn_cc]] | [[basin_read_cc.f90]]:24 |
| `bsn_cc%atmo` | `character(len=1)` |  | not used | [[basin_module.f90#bsn_cc]] | [[basin_read_cc.f90]]:24 |
| `bsn_cc%smax` | `integer` |  | not used | [[basin_module.f90#bsn_cc]] | [[basin_read_cc.f90]]:24 |
| `bsn_cc%qual2e` | `integer` |  | 0 = instream nutrient routing using QUAL2E 1 = instream nutrient routing using QUAL2E - with simplified nutrient transformations | [[basin_module.f90#bsn_cc]] | [[basin_read_cc.f90]]:24 |
| `bsn_cc%gwflow` | `integer` |  | 0 = gwflow module not active; 1 = gwflow module active | [[basin_module.f90#bsn_cc]] | [[basin_read_cc.f90]]:24 |
| `bsn_cc%idc_till` | `integer` |  | 1 = Use dssat tillage method to use if cswat = 2 2 = Use epic tillage method to use if cswat = 2 3 = Use Kemanian tillage method to use if cswat = 2 4 = Use dndc tillage method to use if cswat = 2 | [[basin_module.f90#bsn_cc]] | [[basin_read_cc.f90]]:24 |
