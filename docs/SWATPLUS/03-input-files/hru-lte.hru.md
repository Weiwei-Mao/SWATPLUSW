---
type: input
tags:
  - swat/input
file: hru-lte.hru
ext: hru
cio_field: hru_ez
read_by:
  - hru_lte_read.f90
purpose: ""
---

# hru-lte.hru

> [!info] Input File
> Declared in `file.cio` field `hru_ez`. See [[file.cio]] for the controlling file map.

## Overview
- **Declared in `file.cio` field**: `hru_ez`
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[hru_lte_read.f90]]

## File Structure
- [[hru_lte_read.f90]] source line 75: reads `titldum`
- [[hru_lte_read.f90]] source line 77: reads `header`
- [[hru_lte_read.f90]] source line 80: reads `i`
- [[hru_lte_read.f90]] source line 108: reads `titldum`
- [[hru_lte_read.f90]] source line 110: reads `header`
- [[hru_lte_read.f90]] source line 114: reads `i`
- [[hru_lte_read.f90]] source line 117: reads `k`, `hlt_db(i)`

## Parameters
| Parameter | Type | Units | Meaning | Source | Reader line |
|---|---|---|---|---|---:|
| `i` | `integer` |  |  | `hru_lte_read.f90:33` | [[hru_lte_read.f90]]:80 |
| `k` | `integer` |  |  | `hru_lte_read.f90:35` | [[hru_lte_read.f90]]:117 |
| `hlt_db%name` | `character(len=16)` |  |  | [[hru_lte_module.f90#hlt_db]] | [[hru_lte_read.f90]]:117 |
| `hlt_db%dakm2` | `real` | km^2 | drainage area | [[hru_lte_module.f90#hlt_db]] | [[hru_lte_read.f90]]:117 |
| `hlt_db%cn2` | `real` | none | condition II curve number | [[hru_lte_module.f90#hlt_db]] | [[hru_lte_read.f90]]:117 |
| `hlt_db%cn3_swf` | `real` | none | soil water factor for cn3 (used in calibration) 0 = fc; 1 = saturation (porosity) | [[hru_lte_module.f90#hlt_db]] | [[hru_lte_read.f90]]:117 |
| `hlt_db%tc` | `real` | min | time of concentration | [[hru_lte_module.f90#hlt_db]] | [[hru_lte_read.f90]]:117 |
| `hlt_db%soildep` | `real` | mm | soil profile depth | [[hru_lte_module.f90#hlt_db]] | [[hru_lte_read.f90]]:117 |
| `hlt_db%perco` | `real` |  | soil percolation coefficient | [[hru_lte_module.f90#hlt_db]] | [[hru_lte_read.f90]]:117 |
| `hlt_db%slope` | `real` | m/m | land surface slope | [[hru_lte_module.f90#hlt_db]] | [[hru_lte_read.f90]]:117 |
| `hlt_db%slopelen` | `real` | m | land surface slope length | [[hru_lte_module.f90#hlt_db]] | [[hru_lte_read.f90]]:117 |
| `hlt_db%etco` | `real` |  | et coefficient - use with pet and aet | [[hru_lte_module.f90#hlt_db]] | [[hru_lte_read.f90]]:117 |
| `hlt_db%sy` | `real` | mm | specific yld of the shallow aquifer | [[hru_lte_module.f90#hlt_db]] | [[hru_lte_read.f90]]:117 |
| `hlt_db%abf` | `real` |  | alpha factor groundwater | [[hru_lte_module.f90#hlt_db]] | [[hru_lte_read.f90]]:117 |
| `hlt_db%revapc` | `real` |  | revap coefficient amt of et from shallow aquifer | [[hru_lte_module.f90#hlt_db]] | [[hru_lte_read.f90]]:117 |
| `hlt_db%percc` | `real` |  | percolation coeff from shallow to deep | [[hru_lte_module.f90#hlt_db]] | [[hru_lte_read.f90]]:117 |
| `hlt_db%sw` | `real` | frac | initial soil water (frac of awc) | [[hru_lte_module.f90#hlt_db]] | [[hru_lte_read.f90]]:117 |
| `hlt_db%gw` | `real` | mm | initial shallow aquifer storage | [[hru_lte_module.f90#hlt_db]] | [[hru_lte_read.f90]]:117 |
| `hlt_db%gwflow` | `real` | mm | initial shallow aquifer flow | [[hru_lte_module.f90#hlt_db]] | [[hru_lte_read.f90]]:117 |
| `hlt_db%gwdeep` | `real` | mm | initial deep aquifer flow | [[hru_lte_module.f90#hlt_db]] | [[hru_lte_read.f90]]:117 |
| `hlt_db%snow` | `real` | mm | initial snow water equivalent | [[hru_lte_module.f90#hlt_db]] | [[hru_lte_read.f90]]:117 |
| `hlt_db%xlat` | `real` |  | latitude | [[hru_lte_module.f90#hlt_db]] | [[hru_lte_read.f90]]:117 |
| `hlt_db%text` | `character(len=16)` |  | soil texture 1=sand 2=loamy_sand 3=sandy_loam 4=loam 5=silt_loam 6=silt 7=silty_clay 8=clay_loam 9=sandy_clay_loam 10=sandy_clay 11=silty_clay 12=clay | [[hru_lte_module.f90#hlt_db]] | [[hru_lte_read.f90]]:117 |
| `hlt_db%tropical` | `character(len=16)` |  | (0)="non_trop" (1)="trop" | [[hru_lte_module.f90#hlt_db]] | [[hru_lte_read.f90]]:117 |
| `hlt_db%igrow1` | `character(len=16)` |  | start of growing season for non-tropical (pl_grow_sum) start of monsoon initialization period for tropical | [[hru_lte_module.f90#hlt_db]] | [[hru_lte_read.f90]]:117 |
| `hlt_db%igrow2` | `character(len=16)` |  | end of growing season for non-tropical (pl_end_sum) end of monsoon initialization period for tropical | [[hru_lte_module.f90#hlt_db]] | [[hru_lte_read.f90]]:117 |
| `hlt_db%plant` | `character(len=16)` |  | plant type (as listed in plants.plt) | [[hru_lte_module.f90#hlt_db]] | [[hru_lte_read.f90]]:117 |
| `hlt_db%stress` | `real` | frac | plant stress - pest, root restriction, soil quality, nutrient, (non water, temp) | [[hru_lte_module.f90#hlt_db]] | [[hru_lte_read.f90]]:117 |
| `hlt_db%ipet` | `character(len=16)` |  | potential ET method (0="harg"; 1="p_t") | [[hru_lte_module.f90#hlt_db]] | [[hru_lte_read.f90]]:117 |
| `hlt_db%irr` | `character(len=16)` |  | irrigation code 0="no_irr"; 1="irr" | [[hru_lte_module.f90#hlt_db]] | [[hru_lte_read.f90]]:117 |
| `hlt_db%irrsrc` | `character(len=16)` |  | irrigation source 0="outside_bsn"; 1="shal_aqu" 2="deep_aqu" | [[hru_lte_module.f90#hlt_db]] | [[hru_lte_read.f90]]:117 |
| `hlt_db%tdrain` | `real` | hr | design subsurface tile drain time | [[hru_lte_module.f90#hlt_db]] | [[hru_lte_read.f90]]:117 |
| `hlt_db%uslek` | `real` |  | usle soil erodibility factor | [[hru_lte_module.f90#hlt_db]] | [[hru_lte_read.f90]]:117 |
| `hlt_db%uslec` | `real` |  | usle cover factor | [[hru_lte_module.f90#hlt_db]] | [[hru_lte_read.f90]]:117 |
| `hlt_db%uslep` | `real` | none | USLE equation support practice (P) factor | [[hru_lte_module.f90#hlt_db]] | [[hru_lte_read.f90]]:117 |
| `hlt_db%uslels` | `real` | none | USLE equation length slope (LS) factor | [[hru_lte_module.f90#hlt_db]] | [[hru_lte_read.f90]]:117 |
