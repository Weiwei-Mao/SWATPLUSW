---
type: module
tags:
  - swat/module
  - swat/to-read
file: plant_module.f90
note_file: plant_module.f90
module_name: plant_module
defines_types:
  - plant_growth
  - plant_mass
  - plant_status
  - plant_stress
  - auto_operations
  - fertilize_future
  - plant_community
  - basin_crop_yields
  - plant_carbon
defines_vars:
  - basin_plants
  - yld_tbr
  - yld_grn
  - yld_veg
  - yld_rsd
  - pcom
  - pcom_init
  - plmz
  - o_m1
  - o_m2
  - o_m3
  - plstrz
  - bsn_crop_yld
  - bsn_crop_yld_aa
  - bsn_crop_yld_z
  - c_frac
defines_subroutines:
  - plg_zero
defines_functions: []
defines_procedures:
  - plg_zero
purpose: ""
---

# plant_module

> [!info] Module
> Defines derived types and module-level variables.

## Defined Types
### plant_growth

- **Defined in source**: `plant_module.f90:7`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `cht` | `real` | 8 | m \|canopy height |
| `lai` | `real` | 9 | m**2/m**2 \|leaf area index |
| `plet` | `real` | 10 | mm H2O \|actual ET simulated during life of plant |
| `plpet` | `real` | 11 | mm H2O \|potential ET simulated during life of plant |
| `laimxfr` | `real` | 12 |  |
| `laimxfr_p` | `real` | 13 |  |
| `hi_adj` | `real` | 14 | (kg/ha)/(kg/ha) \|temperature adjusted harvest index for current time during growing season |
| `hi_prev` | `real` | 15 | (kg/ha)/(kg/ha) \|optimal harvest index for current time during growing season |
| `olai` | `real` | 16 | \|leaf area index (0-1) when leaf area decline begins |
| `dphu` | `real` | 17 | \|phu accumulated (0-1) when leaf area decline begins |
| `d_senes` | `real` | 18 | days !days since start of senescence |
| `leaf_frac` | `real` | 19 | none \|fraction of above ground tree biomass that is leaf |
| `root_dep` | `real` | 20 | mm \|root depth |
| `root_frac` | `real` | 21 | kg/ha \|root fraction of total plant mass |
| `rtfr` | `real, dimension(:), allocatable` | 22 | none \|root fraction for each plant in community |

### plant_mass

- **Defined in source**: `plant_module.f90:25`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `c_fr` | `real` | 31 | none \|carbon fraction |
| `n_fr` | `real` | 32 | none \|nitrogen fraction |
| `p_fr` | `real` | 33 | none \|phosphorus fraction |

### plant_status

- **Defined in source**: `plant_module.f90:42`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `idplt` | `integer` | 43 | none land cover code from plants.plt |
| `bsn_num` | `integer` | 44 | none \|basin plant number |
| `gro` | `character(len=1)` | 45 | \|land cover status; 'n' = no land cover growing; 'y' = land cover growing |
| `idorm` | `character(len=1)` | 46 | none \|dormancy status; 'n'=land cover growing; 'y'=land cover dormant |
| `mseas` | `character(len=1)` | 47 | none \|monsoon status; 'n'= not in monsoon season; 'y'= in monsoon season |
| `phumat` | `real` | 48 | C \|heat units to maturity - annual |
| `phumat_p` | `real` | 49 | C \|heat units to maturity for perennials |
| `phuacc` | `real` | 50 | fraction \|fraction of plant heat unit accumulated |
| `phuacc_p` | `real` | 51 | fraction \|fraction of perennial plant heat unit accumulated |
| `harv_num` | `integer` | 52 | \|number of harvest operations for entire simulation |
| `harv_num_yr` | `integer` | 53 | \|number of harvest operations each year |
| `curyr_mat` | `integer` | 54 |  |
| `pop_com` | `real` | 55 | none |
| `days_senes` | `integer` | 56 | mm \|days since scenesence began (for moisture growth perennials) |
| `leaf_tov` | `real` | 57 | none \|leaf turnover rate - decline in lai and leaf biomass |
| `lai_pot` | `real` | 58 | none \|potential leaf area index |
| `harv_idx` | `real` | 59 | fraction \|harvest index - grain fraction of above ground plant mass |
| `pest_stress` | `real` | 60 | fraction \|pest (insect, disease) stress on harvest index |
| `epco` | `real` | 61 | fraction \|water uptake compensation factor for each plant |
| `uptake` | `real, dimension(:), allocatable` | 62 | mm \|water uptake by layer |

### plant_stress

- **Defined in source**: `plant_module.f90:65`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `reg` | `real` | 66 | none \|stress factor that most limits plant growth on current day |
| `strsw` | `real` | 68 | none \|frac of potential plant growth achieved on the day where the reduction is caused by water stress |
| `strsa` | `real` | 70 | \|frac of potential plant growth achieved on the day where the reduction is caused by air stress |
| `strsn` | `real` | 72 | none \|frac of potential plant growth achieved on the day where the reduction is caused by nit stress |
| `strsp` | `real` | 74 | none \|frac of potential plant growth achieved on the day where the reduction is caused by phos stress |
| `strst` | `real` | 76 | none \|frac of potential plant growth achieved on the day where the reduction is caused by temp stress |
| `strss` | `real` | 78 | none \|frac of potential plant growth achieved on the day where the reduction is caused by salt stress (rtb salt) |
| `sum_w` | `real` | 80 | none \|sum of water stress |
| `sum_tmp` | `real` | 81 | none \|sum of temperature stress |
| `sum_n` | `real` | 82 | none \|sum of nitrogen stress |
| `sum_p` | `real` | 83 | none \|sum of phosphorus stress |
| `sum_a` | `real` | 84 | none \|sum of aeration stress |

### auto_operations

- **Defined in source**: `plant_module.f90:87`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `apply_day` | `integer` | 88 | day to apply in prob_unif1 condition |
| `num_actions` | `integer, dimension(:), allocatable` | 89 | current number of actions - reset on January 1 |
| `days_act` | `integer, dimension(:), allocatable` | 90 | days since the action specified in lim_const |

### fertilize_future

- **Defined in source**: `plant_module.f90:93`
- **Source note**: set to the fert_fut action in the lum.dtl

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `name` | `character(len=35)` | 94 | name of the fertilizer operation (from the dtbl) |
| `num` | `integer` | 95 | number of the future fertilizer application (from the dtbl) |
| `fertname` | `character(len=40)` | 96 | fertilizer name in fertilizer.frt |
| `fertnum` | `integer` | 97 | fertilizer number in fertilizer.frt |
| `day_fert` | `integer` | 98 | future julian day to apply fert (must be within a year of test) |
| `fert_kg` | `real` | 99 | kg/ha - amount of fertilzer applied |
| `fertop` | `character(len=35)` | 100 | application type in chem_app.ops |
| `appnum` | `integer` | 101 | application number in chem_app.ops |

### plant_community

- **Defined in source**: `plant_module.f90:104`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `name` | `character(len=40)` | 105 |  |
| `npl` | `integer` | 106 | number of plants in community |
| `pl` | `character(len=40), dimension(:), allocatable` | 107 | N/A \|plant name |
| `pcomdb` | `integer` | 108 | current plant community database number |
| `rot_yr` | `integer` | 109 | rotation year |
| `days_plant` | `integer` | 110 | \|days since last planting - for conditional scheduling after planting |
| `days_harv` | `integer` | 111 | \|days since last harvest - for conditional scheduling after harvest |
| `days_kill` | `integer` | 112 | \|days since last kill - for conditional scheduling after kill |
| `days_irr` | `integer` | 113 | \|days since last irrigation - for conditional scheduling after irrigation |
| `last_kill` | `character(len=40)` | 114 | \|name of last plant killed |
| `cht_mx` | `real` | 115 | m \|height of tallest plant in community for pet calculation |
| `lai_sum` | `real` | 116 | m/m \|sum of lai for each plant |
| `laimx_sum` | `real` | 117 | m/m \|sum of maximum lai for each plant - for canopy interception |
| `rsd_covfac` | `real` | 118 | \|average residue cover factor |
| `dtbl` | `auto_operations` | 119 | d_tble action - to limit number of actions per year |
| `fert_fut_num` | `integer` | 120 |  |
| `fert_fut` | `fertilize_future` | 121 |  |
| `plg` | `plant_growth` | 122 | plant growth variables |
| `plstr` | `plant_stress` | 123 | plant stress variables |
| `plcur` | `plant_status` | 124 | plant status variables |
| `plm` | `plant_mass` | 125 | kg/ha \|total biomass for individual plant in community |

### basin_crop_yields

- **Defined in source**: `plant_module.f90:133`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `area_ha` | `real` | 134 | ha \|area of crop harvested |
| `yield` | `real` | 135 | t \|yield mass removed in harvest |

### plant_carbon

- **Defined in source**: `plant_module.f90:141`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `leaf` | `real` | 142 | none \|carbon fraction in leaves |
| `stem` | `real` | 143 | none \|carbon fraction in stem |
| `seed` | `real` | 144 | none \|carbon fraction in seeds |
| `root` | `real` | 145 | none \|carbon fraction in roots |

## Variables Defined
### basin_plants

- **Type**: `integer`
- **Defined in source**: `plant_module.f90:5`
- **Source note**: number of different plants in the basin

### yld_tbr

- **Type**: `plant_mass`
- **Defined in source**: `plant_module.f90:36`

### yld_grn

- **Type**: `plant_mass`
- **Defined in source**: `plant_module.f90:37`

### yld_veg

- **Type**: `plant_mass`
- **Defined in source**: `plant_module.f90:38`

### yld_rsd

- **Type**: `plant_mass`
- **Defined in source**: `plant_module.f90:39`

### pcom

- **Type**: `plant_community`
- **Defined in source**: `plant_module.f90:127`

### pcom_init

- **Type**: `plant_community`
- **Defined in source**: `plant_module.f90:128`

### plmz

- **Type**: `plant_mass`
- **Defined in source**: `plant_module.f90:129`

### o_m1

- **Type**: `plant_mass`
- **Defined in source**: `plant_module.f90:130`

### o_m2

- **Type**: `plant_mass`
- **Defined in source**: `plant_module.f90:130`

### o_m3

- **Type**: `plant_mass`
- **Defined in source**: `plant_module.f90:130`

### plstrz

- **Type**: `plant_stress`
- **Defined in source**: `plant_module.f90:131`

### bsn_crop_yld

- **Type**: `basin_crop_yields`
- **Defined in source**: `plant_module.f90:137`

### bsn_crop_yld_aa

- **Type**: `basin_crop_yields`
- **Defined in source**: `plant_module.f90:138`

### bsn_crop_yld_z

- **Type**: `basin_crop_yields`
- **Defined in source**: `plant_module.f90:139`

### c_frac

- **Type**: `plant_carbon`
- **Defined in source**: `plant_module.f90:147`

## Subroutines Defined
### plg_zero

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
