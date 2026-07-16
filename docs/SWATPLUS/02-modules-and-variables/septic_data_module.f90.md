---
type: module
tags:
  - swat/module
  - swat/to-read
file: septic_data_module.f90
note_file: septic_data_module.f90
module_name: septic_data_module
defines_types:
  - septic_db
  - septic_system
defines_vars:
  - sepdb
  - sep
defines_subroutines: []
defines_functions: []
defines_procedures: []
purpose: ""
---

# septic_data_module

> [!info] Module
> Defines derived types and module-level variables.

## Defined Types
### septic_db

- **Defined in source**: `septic_data_module.f90:5`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `sepnm` | `character(len=20)` | 6 |  |
| `qs` | `real` | 7 | m3/d \|flow rate of the septic tank effluent per capita (sptq) |
| `bodconcs` | `real` | 8 | mg/l \|biological oxygen demand of the septic tank effluent |
| `tssconcs` | `real` | 9 | mg/l \|concentration of total suspended solid in the septic tank effluent |
| `nh4concs` | `real` | 10 | mg/l \|concentration of total phosphorus in the septic tank effluent |
| `no3concs` | `real` | 11 | mg/l \|concentration of nitrate in the septic tank effluent |
| `no2concs` | `real` | 12 | mg/l \|concentration of nitrite in the septic tank effluent |
| `orgnconcs` | `real` | 13 | mg/l \|concentration of organic nitrogen in the septic tank effluent |
| `minps` | `real` | 14 | mg/l \|concentration of mineral phosphorus in the septic tank effluent |
| `orgps` | `real` | 15 | mg/l \|concentration of organic phosphorus in the septic tank effluent |
| `fcolis` | `real` | 16 | mg/l \|concentration of fecal coliform in the septic tank effluent |

### septic_system

- **Defined in source**: `septic_data_module.f90:20`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `name` | `character(len=13)` | 21 |  |
| `typ` | `integer` | 22 | none \|septic system type |
| `yr` | `integer` | 23 | \|year the septic system became operational |
| `opt` | `integer` | 24 | none \|Septic system operation flag (1=active,2=failing,0=not operated) |
| `cap` | `real` | 25 | none \|Number of permanent residents in the house |
| `area` | `real` | 26 | m^2 \|average area of drainfield of individual septic systems |
| `tfail` | `integer` | 27 | days \|time until falling systems gets fixed |
| `z` | `real` | 28 | mm \|depth to the top of the biozone layer from the ground surface |
| `thk` | `real` | 29 | mm \|thickness of biozone layer |
| `strm_dist` | `real` | 30 | km \|distance to the stream from the septic |
| `density` | `real` | 31 | \|number of septic systems per square kilometer |
| `bd` | `real` | 32 | kg/m^3 \|density of biomass |
| `bod_dc` | `real` | 33 | m^3/day \|BOD decay rate coefficient |
| `bod_conv` | `real` | 34 | \|a conversion factor representing the proportion of mass bacterial growth and mass BOD degraded in the STE. |
| `fc1` | `real` | 36 | none \|Linear coefficient for calculation of field capacity in the biozone |
| `fc2` | `real` | 37 | none \|Exponential coefficient for calculation of field capacity in the biozone |
| `fecal` | `real` | 38 | m^3/day \|fecal coliform bacteria decay rate coefficient |
| `plq` | `real` | 39 | none \|conversion factor for plaque from TDS |
| `mrt` | `real` | 40 | none \|mortality rate coefficient |
| `rsp` | `real` | 41 | none \|respiration rate coefficient |
| `slg1` | `real` | 42 | none \|slough-off calibration parameter |
| `slg2` | `real` | 43 | none \|slough-off calibration parameter |
| `nitr` | `real` | 44 | none \|nitrification rate coefficient |
| `denitr` | `real` | 45 | none \|denitrification rate coefficient |
| `pdistrb` | `real` | 46 | (L/kg) \|Linear P sorption distribution coefficient |
| `psorpmax` | `real` | 47 | (mg P/kg Soil) \|Maximum P sorption capacity |
| `solpslp` | `real` | 48 | \|Slope of the linear effluent soluble P equation |
| `solpintc` | `real` | 49 | \|Intercept of the linear effluent soluble P equation |

## Variables Defined
### sepdb

- **Type**: `septic_db`
- **Defined in source**: `septic_data_module.f90:18`

### sep

- **Type**: `septic_system`
- **Defined in source**: `septic_data_module.f90:51`

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
