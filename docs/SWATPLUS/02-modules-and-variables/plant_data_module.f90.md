---
type: module
tags:
  - swat/module
  - swat/to-read
file: plant_data_module.f90
note_file: plant_data_module.f90
module_name: plant_data_module
defines_types:
  - residue_partition_fracs
  - lignin_derived_partition_fracs
  - plant_db
  - plant_cp
  - plant_init_db
  - plant_community_db
  - plant_transplant_db
defines_vars:
  - plts_bsn
  - pl_class
  - photo_degrade_factor
  - cswat_1_part_fracs
  - pldb
  - pl_db
  - plcp
  - pl_cp
  - pcomdb
  - transpl
defines_subroutines: []
defines_functions: []
defines_procedures: []
purpose: ""
---

# plant_data_module

> [!info] Module
> Defines derived types and module-level variables.

## Defined Types
### residue_partition_fracs

- **Defined in source**: `plant_data_module.f90:9`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `meta_frac` | `real` | 14 | none \|reads plants.plt avg_lig_frac |
| `str_frac` | `real` | 15 | none \|reads plants.plt ab_lig_frac (used as above-ground lignin) |
| `lig_frac` | `real` | 16 | none \|reads plants.plt bg_lig_frac (used as below-ground lignin) |

### lignin_derived_partition_fracs

- **Defined in source**: `plant_data_module.f90:19`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `meta_frac_abg` | `real` | 20 | none \|fraction of above ground (abg) biomass that is metabolic |
| `str_frac_abg` | `real` | 21 | none \|fraction of above ground (abg) biomass that is structural |
| `lig_frac_abg` | `real` | 22 | none \|fraction of above ground (abg) biomass that is lignin |
| `meta_frac_blg` | `real` | 23 | none \|fraction of below ground (blg) biomass that is metabolic |
| `str_frac_blg` | `real` | 24 | none \|fraction of below ground (blg) biomass that is structural |
| `lig_frac_blg` | `real` | 25 | none \|fraction of below ground (blg) biomass that is lignin |

### plant_db

- **Defined in source**: `plant_data_module.f90:30`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `plantnm` | `character(len=40)` | 31 | none \|crop name |
| `typ` | `character(len=18)` | 32 | none \|plant category warm_annual cold_annual warm_annual_tuber cold_annual_tuber perennial |
| `trig` | `character(len=18)` | 38 | none \|phenology trigger moisture_gro temp_gro |
| `nfix_co` | `real` | 41 | none \|n fixation coefficient (0.5 legume; 0 non-legume) |
| `days_mat` | `integer` | 42 | days \|days to maturity - if zero use hu for entire growing season |
| `bio_e` | `real` | 43 | (kg/ha/(MJ/m**2) \|biomass-energy ratio |
| `hvsti` | `real` | 44 | (kg/ha)/(kg/ha) \|harvest index: crop yield/aboveground biomass |
| `blai` | `real` | 45 | none \|max (potential) leaf area index |
| `frgrw1` | `real` | 46 | none \|fraction of the growing season corresponding to the 1st point on optimal leaf area development curve |
| `laimx1` | `real` | 48 | none \|frac of max leaf area index corresponding to the 1st point on optimal leaf area development curve |
| `frgrw2` | `real` | 50 | none \|fraction of the growing season corresponding to the 2nd point on optimal leaf area development curve |
| `laimx2` | `real` | 52 | none \|fraction of max leaf area index corresponding to the 2nd point on optimal leaf area development curve |
| `dlai` | `real` | 54 | none \|frac of growing season when leaf are declines |
| `dlai_rate` | `real` | 55 | none \|exponent that governs lai decline rate |
| `chtmx` | `real` | 56 | m \|maximum canopy height |
| `rdmx` | `real` | 57 | m \|maximum root depth |
| `t_opt` | `real` | 58 | deg C \|optimal temp for plant growth |
| `t_base` | `real` | 59 | deg C \|minimum temp for plant growth |
| `cnyld` | `real` | 60 | kg N/kg yld \|frac of nitrogen in yield |
| `cpyld` | `real` | 61 | kg P/kg yld \|frac of phosphorus in yield |
| `pltnfr1` | `real` | 62 | kg N/kg biomass \|nitrogen uptake parm #1 |
| `pltnfr2` | `real` | 63 | kg N/kg biomass \|nitrogen uptake parm #2 |
| `pltnfr3` | `real` | 64 | kg N/kg/biomass \|nitrogen uptake parm #3 |
| `pltpfr1` | `real` | 65 | kg P/kg/biomass \|phoshorus uptake parm #1 |
| `pltpfr2` | `real` | 66 | kg P/kg/biomass \|phoshorus uptake parm #2 |
| `pltpfr3` | `real` | 67 | kg P/kg/biomass \|phoshorus uptake parm #3 |
| `wsyf` | `real` | 68 | (kg/ha)/(kg/ha) \|value of harvest index bet 0 and HVSTI |
| `usle_c` | `real` | 69 | none \|minimum value of the USLE C factor for water erosion |
| `gsi` | `real` | 70 | m/s \|maximum stomatal conductance |
| `vpdfr` | `real` | 71 | kPa \|vapor pressure deficit at which GMAXFR is valid |
| `gmaxfr` | `real` | 72 | none \|fraction of max stomatal conductance that is achieved at the vapor pressure deficit defined by VPDFR |
| `wavp` | `real` | 74 | none \|rate of decline in radiation use efficiency |
| `co2hi` | `real` | 75 | uL CO2/L air \|CO2 concentration higher than the ambient corresponding to the 2nd point on radiation use efficiency curve |
| `bioehi` | `real` | 77 | (kg/ha)/(MJ/m**2) \|biomass-energy ratio when plant is in an environment with CO2 level equal to the value of CO2HI. |
| `rsdco_pl` | `real` | 79 | none \|plant residue decomposition coeff |
| `alai_min` | `real` | 80 | m**2/m**2 \|min LAI during winter dormant period |
| `laixco_tree` | `real` | 81 | none \|coefficient to estimate max lai during tree growth |
| `mat_yrs` | `integer` | 82 | years \|years to maturity |
| `bmx_peren` | `real` | 83 | metric tons/ha \|max biomass for forest |
| `ext_coef` | `real` | 84 | \|light extinction coefficient |
| `leaf_tov_min` | `real` | 85 | months \|perennial leaf turnover rate with minimum stress (complete turnover in 12 mon) |
| `leaf_tov_max` | `real` | 86 | months \|perennial leaf turnover rate with maximum stress (complete turnover in 3 mon) |
| `bm_dieoff` | `real` | 87 | frac \|above ground biomass that dies off at dormancy |
| `rsr1` | `real` | 89 | frac \|initial root to shoot ratio at the beg of growing season |
| `rsr2` | `real` | 90 | frac \|root to shoot ratio at the end of the growing season |
| `pop1` | `real` | 91 | plants/m^2 \|plant population corresponding to the 1st point on the population lai curve |
| `frlai1` | `real` | 93 | frac \|frac of max leaf area index corresponding to the 1st point on the leaf area development curve |
| `pop2` | `real` | 95 | plants/m^2 \|plant population corresponding to the 2nd point on the population lai curve |
| `frlai2` | `real` | 97 | frac \|frac of max leaf area index corresponding to the 2nd point on the leaf area development curve |
| `frsw_gro` | `real` | 99 | frac \|30 day sum of P-PET to initiate growth of tropical plants during monsoon season - pcom()%plcur()%iseason |
| `aeration` | `real` | 101 | \|aeration stress factor |
| `rsd_pctcov` | `real` | 102 | \|residue factor for percent cover equation |
| `rsd_covfac` | `real` | 103 | \|residue factor for surface cover (C factor) equation |
| `res_part_fracs` | `residue_partition_fracs` | 105 |  |

### plant_cp

- **Defined in source**: `plant_data_module.f90:110`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `popsc1` | `real` | 111 |  |
| `popsc2` | `real` | 112 |  |
| `leaf1` | `real` | 113 | none \|1st shape parameter for leaf area |
| `leaf2` | `real` | 114 | none \|2nd leaf parameter for leaf area |
| `ruc1` | `real` | 115 | none \|1st shape parameter for radiation use efficiency equation |
| `ruc2` | `real` | 116 | none \|2nd shape parameter for radiation use efficiency equation |
| `nup1` | `real` | 117 | none \|1st shape parameter for plant N uptake equation |
| `nup2` | `real` | 118 | none \|2nd shape parameter for plant N uptake equation |
| `pup1` | `real` | 119 | none \|1st shape parameter for plant P uptake equation |
| `pup2` | `real` | 120 | none \|2nd shape parameter for plant P uptake equation |
| `gmaxfr` | `real` | 121 | none \|fraction of max stomatal conductance that is achieved at the vapor pressure deficit defined by VPDFR |
| `vpdfr` | `real` | 123 | kPa \|vapor pressure deficit at which GMAXFR is valid |
| `cvm` | `real` | 124 | frac \|fraction of the maximum leaf area index corresponding to the second point of the optimal leaf area dev curve |
| `vpd2` | `real` | 126 | kPa \|vapor pressure deficit corresponding to the second point on the stomatal conductance curve |

### plant_init_db

- **Defined in source**: `plant_data_module.f90:132`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `cpnm` | `character(len=40)` | 133 |  |
| `db_num` | `integer` | 134 | \|plant object |
| `igro` | `character(len=1)` | 135 | \|land cover status n = no land cover growing y = land cover growing |
| `lai` | `real` | 138 | m**2/m**2 \|leaf area index |
| `bioms` | `real` | 139 | kg/ha \|land cover/crop biomass |
| `phuacc` | `real` | 140 | \|frac of plant heat unit acc. |
| `pop` | `real` | 141 |  |
| `fr_yrmat` | `real` | 142 | years \|fraction of current year of growth to years to maturity |
| `rsdin` | `real` | 143 | kg/ha \|initial residue cover |

### plant_community_db

- **Defined in source**: `plant_data_module.f90:146`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `name` | `character(len=40)` | 147 |  |
| `plants_com` | `integer` | 148 |  |
| `rot_yr_ini` | `integer` | 149 |  |
| `pl` | `plant_init_db` | 150 |  |

### plant_transplant_db

- **Defined in source**: `plant_data_module.f90:154`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `name` | `character(len=40)` | 155 |  |
| `lai` | `real` | 156 | m**2/m**2 \|leaf area index |
| `bioms` | `real` | 157 | kg/ha \|land cover/crop biomass |
| `phuacc` | `real` | 158 | frac \|frac of plant heat unit acc. |
| `fr_yrmat` | `real` | 159 | years \|fraction of current year of growth to years to maturity |
| `pop` | `real` | 160 | plants/m^2 \|plant population |

## Variables Defined
### plts_bsn

- **Type**: `character(len=40), dimension (:), allocatable`
- **Defined in source**: `plant_data_module.f90:5`
- **Source note**: none      |plant names simulated in current run

### pl_class

- **Type**: `character(len=25), dimension(:), allocatable`
- **Defined in source**: `plant_data_module.f90:6`
- **Source note**: none      |plant class - row crop, tree, grass, etc

### photo_degrade_factor

- **Type**: `real`
- **Defined in source**: `plant_data_module.f90:7`
- **Source note**: none  |fraction to reduce surface residue due to photo degradation

### cswat_1_part_fracs

- **Type**: `lignin_derived_partition_fracs`
- **Defined in source**: `plant_data_module.f90:27`

### pldb

- **Type**: `plant_db`
- **Defined in source**: `plant_data_module.f90:107`

### pl_db

- **Type**: `plant_db`
- **Defined in source**: `plant_data_module.f90:108`

### plcp

- **Type**: `plant_cp`
- **Defined in source**: `plant_data_module.f90:129`

### pl_cp

- **Type**: `plant_cp`
- **Defined in source**: `plant_data_module.f90:130`

### pcomdb

- **Type**: `plant_community_db`
- **Defined in source**: `plant_data_module.f90:152`

### transpl

- **Type**: `plant_transplant_db`
- **Defined in source**: `plant_data_module.f90:162`

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
