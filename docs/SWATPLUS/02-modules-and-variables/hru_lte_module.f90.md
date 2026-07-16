---
type: module
tags:
  - swat/module
  - swat/to-read
file: hru_lte_module.f90
note_file: hru_lte_module.f90
module_name: hru_lte_module
defines_types:
  - swatdeg_hru_data
  - swatdeg_hru_dynamic
defines_vars:
  - awct
  - port
  - scon
  - hlt_db
  - hlt
  - hlt_init
defines_subroutines: []
defines_functions: []
defines_procedures: []
purpose: ""
---

# hru_lte_module

> [!info] Module
> Defines derived types and module-level variables.

## Defined Types
### swatdeg_hru_data

- **Defined in source**: `hru_lte_module.f90:9`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `name` | `character(len=16)` | 10 |  |
| `dakm2` | `real` | 11 | km^2 \|drainage area |
| `cn2` | `real` | 12 | none \|condition II curve number |
| `cn3_swf` | `real` | 13 | none \|soil water factor for cn3 (used in calibration) 0 = fc; 1 = saturation (porosity) |
| `tc` | `real` | 15 | min \|time of concentration |
| `soildep` | `real` | 16 | mm \|soil profile depth |
| `perco` | `real` | 17 | \|soil percolation coefficient |
| `slope` | `real` | 18 | m/m \|land surface slope |
| `slopelen` | `real` | 19 | m \|land surface slope length |
| `etco` | `real` | 20 | \|et coefficient - use with pet and aet |
| `sy` | `real` | 21 | mm \|specific yld of the shallow aquifer |
| `abf` | `real` | 22 | \|alpha factor groundwater |
| `revapc` | `real` | 23 | \|revap coefficient amt of et from shallow aquifer |
| `percc` | `real` | 24 | \|percolation coeff from shallow to deep |
| `sw` | `real` | 25 | frac \|initial soil water (frac of awc) |
| `gw` | `real` | 26 | mm \|initial shallow aquifer storage |
| `gwflow` | `real` | 27 | mm \|initial shallow aquifer flow |
| `gwdeep` | `real` | 28 | mm \|initial deep aquifer flow |
| `snow` | `real` | 29 | mm \|initial snow water equivalent |
| `xlat` | `real` | 30 | \|latitude |
| `text` | `character(len=16)` | 31 | \|soil texture 1=sand 2=loamy_sand 3=sandy_loam 4=loam 5=silt_loam 6=silt 7=silty_clay 8=clay_loam 9=sandy_clay_loam 10=sandy_clay 11=silty_clay 12=clay |
| `tropical` | `character(len=16)` | 36 | \|(0)="non_trop" (1)="trop" |
| `igrow1` | `character(len=16)` | 37 | \|start of growing season for non-tropical (pl_grow_sum) start of monsoon initialization period for tropical |
| `igrow2` | `character(len=16)` | 39 | \|end of growing season for non-tropical (pl_end_sum) end of monsoon initialization period for tropical |
| `plant` | `character(len=16)` | 41 | \|plant type (as listed in plants.plt) |
| `stress` | `real` | 42 | frac \|plant stress - pest, root restriction, soil quality, nutrient, (non water, temp) |
| `ipet` | `character(len=16)` | 43 | \|potential ET method (0="harg"; 1="p_t") |
| `irr` | `character(len=16)` | 44 | \|irrigation code 0="no_irr"; 1="irr" |
| `irrsrc` | `character(len=16)` | 45 | irrigation source 0="outside_bsn"; 1="shal_aqu" 2="deep_aqu" |
| `tdrain` | `real` | 46 | hr \|design subsurface tile drain time |
| `uslek` | `real` | 47 | \|usle soil erodibility factor |
| `uslec` | `real` | 48 | \|usle cover factor |
| `uslep` | `real` | 49 | none \|USLE equation support practice (P) factor |
| `uslels` | `real` | 50 | none \|USLE equation length slope (LS) factor |

### swatdeg_hru_dynamic

- **Defined in source**: `hru_lte_module.f90:54`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `name` | `character(len=16)` | 55 |  |
| `props` | `integer` | 56 |  |
| `obj_no` | `integer` | 57 |  |
| `lsu` | `character(len=16)` | 58 | \|landscape unit - character |
| `region` | `character(len=16)` | 59 | \|region - character |
| `plant` | `character(len=16)` | 60 | \|plant type (as listed in plants.plt) |
| `iplant` | `integer` | 62 | \|plant number xwalked from hlt_db()%plant and plants.plt |
| `km2` | `real` | 63 | km^2 \|drainage area |
| `cn2` | `real` | 64 | \|condition II curve number (used in calibration) |
| `cn3_swf` | `real` | 65 | none \|soil water factor for cn3 (used in calibration) 0 = fc; 1 = saturation (porosity) |
| `soildep` | `real` | 67 | mm \|soil profile depth |
| `etco` | `real` | 68 | \|et coefficient - use with pet and aet (used in calibration) |
| `revapc` | `real` | 69 | m/m \|revap from aquifer (used in calibration) |
| `perco` | `real` | 70 | \|soil percolation coefficient (used in calibration) |
| `tdrain` | `real` | 71 | hr \|design subsurface tile drain time (used in calibration) |
| `stress` | `real` | 72 | frac \|plant stress - pest, root restriction, soil quality, nutrient, (non water, temp) (used in calibration) |
| `uslefac` | `real` | 74 | \|USLE slope length factor |
| `wrt1` | `real` | 75 |  |
| `wrt2` | `real` | 76 |  |
| `smx` | `real` | 77 |  |
| `hk` | `real` | 78 |  |
| `yls` | `real` | 79 |  |
| `ylc` | `real` | 80 |  |
| `awc` | `real` | 81 | mm/mm \|available water capacity of soil |
| `g` | `real` | 82 |  |
| `hufh` | `real` | 83 |  |
| `phu` | `real` | 84 |  |
| `por` | `real` | 85 |  |
| `sc` | `real` | 86 |  |
| `sw` | `real` | 87 | mm/mm \|initial soil water storage |
| `gw` | `real` | 88 | mm \|initial shallow aquifer storage |
| `snow` | `real` | 89 | mm \|initial water content of snow |
| `gwflow` | `real` | 90 | mm \|initial groundwater flow |
| `gro` | `character(len=1)` | 91 | \|y=plant growing; n=not growing; |
| `dm` | `real` | 92 | t/ha \|plant biomass |
| `alai` | `real` | 93 | \|leaf area index |
| `yield` | `real` | 94 | t/ha \|plant yield |
| `npp` | `real` | 95 | t/ha \|net primary productivity |
| `lai_mx` | `real` | 96 | \|maximum leaf area index |
| `gwdeep` | `real` | 97 | mm \|deep aquifer storage |
| `aet` | `real` | 98 | mm \|sum of actual et during growing season (for hi water stress) |
| `pet` | `real` | 99 | mm \|sum of potential et during growing season (for hi water stress) |
| `start` | `integer` | 100 |  |
| `end` | `integer` | 101 |  |

## Variables Defined
### awct

- **Type**: `real, dimension(12)`
- **Defined in source**: `hru_lte_module.f90:5`

### port

- **Type**: `real, dimension(12)`
- **Defined in source**: `hru_lte_module.f90:6`

### scon

- **Type**: `real, dimension(12)`
- **Defined in source**: `hru_lte_module.f90:7`

### hlt_db

- **Type**: `swatdeg_hru_data`
- **Defined in source**: `hru_lte_module.f90:52`

### hlt

- **Type**: `swatdeg_hru_dynamic`
- **Defined in source**: `hru_lte_module.f90:103`

### hlt_init

- **Type**: `swatdeg_hru_dynamic`
- **Defined in source**: `hru_lte_module.f90:104`

## Subroutines Defined
(No subroutines detected.)

## Functions Defined
(No functions detected.)

## Used By Source Routines

```dataview
LIST file.link
WHERE type = "source" AND contains(module, this.module_name)
```

<!-- USER-NOTES-START -->
## Notes
Use this section for type and variable meanings, units, and allowed values. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
