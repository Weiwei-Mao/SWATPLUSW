---
type: module
tags:
  - swat/module
  - swat/to-read
file: soil_data_module.f90
note_file: soil_data_module.f90
module_name: soil_data_module
defines_types:
  - soil_lte_database
  - soiltest_db
  - soiltest_db_old
  - soilayer_db
  - soil_profile_db
  - soil_database
defines_vars:
  - soil_lte
  - solt_db
  - soildb
defines_subroutines: []
defines_functions: []
defines_procedures: []
purpose: ""
---

# soil_data_module

> [!info] Module
> Defines derived types and module-level variables.

## Defined Types
### soil_lte_database

- **Defined in source**: `soil_data_module.f90:5`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `texture` | `character(len=16)` | 6 |  |
| `awc` | `real` | 7 |  |
| `por` | `real` | 8 |  |
| `scon` | `real` | 9 |  |

### soiltest_db

- **Defined in source**: `soil_data_module.f90:13`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `name` | `character(len=16)` | 14 |  |
| `exp_co` | `real` | 15 | \|depth coefficient to adjust concentrations for depth |
| `lab_p` | `real` | 16 | ppm \|labile P in soil surface |
| `nitrate` | `real` | 17 | ppm \|nitrate N in soil surface |
| `fr_hum_act` | `real` | 18 | 0-1 \|fraction of soil humus that is active |
| `hum_c_n` | `real` | 19 | ratio \|humus C:N ratio (range 8-12) |
| `hum_c_p` | `real` | 20 | ratio \|humus C:P ratio (range 70-90) |
| `inorgp` | `real` | 21 | ppm \|inorganic P in soil surface - not currently used |
| `watersol_p` | `real` | 22 | ppm \|water soluble P in soil surface - not currently used |
| `h3a_p` | `real` | 23 | ppm \|h3a P in soil surface - not currently used |
| `mehlich_p` | `real` | 24 | ppm \|Mehlich P in soil surface - not currently used |
| `bray_strong_p` | `real` | 25 | ppm \|Bray P in soil surface - not currently used |

### soiltest_db_old

- **Defined in source**: `soil_data_module.f90:30`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `name` | `character(len=16)` | 31 |  |
| `exp_co` | `real` | 32 | \|depth coefficient to adjust concentrations for depth |
| `totaln` | `real` | 33 | ppm \|total N in soil |
| `inorgn` | `real` | 34 | ppm \|inorganic N in soil surface |
| `orgn` | `real` | 35 | ppm \|organic N in soil surface |
| `totalp` | `real` | 36 | ppm \|total P in soil surface |
| `inorgp` | `real` | 37 | ppm \|inorganic P in soil surface |
| `orgp` | `real` | 38 | ppm \|organic P in soil surface |
| `watersol_p` | `real` | 39 | ppm \|water soluble P in soil surface |
| `h3a_p` | `real` | 40 | ppm \|h3a P in soil surface |
| `mehlich_p` | `real` | 41 | ppm \|Mehlich P in soil surface |
| `bray_strong_p` | `real` | 42 | ppm \|Bray P in soil surface |

### soilayer_db

- **Defined in source**: `soil_data_module.f90:46`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `z` | `real` | 47 | mm \|depth to bottom of soil layer |
| `bd` | `real` | 48 | Mg/m**3 \|bulk density of the soil |
| `awc` | `real` | 49 | mm H20/mm soil \|available water capacity of soil layer |
| `k` | `real` | 50 | mm/hr \|saturated hydraulic conductivity of soil layer. Index:(layer,HRU) |
| `cbn` | `real` | 51 | % \|percent organic carbon in soil layer |
| `clay` | `real` | 52 | none \|fraction clay content in soil material (UNIT CHANGE!) |
| `silt` | `real` | 53 | % \|percent silt content in soil material |
| `sand` | `real` | 54 | none \|fraction of sand in soil material |
| `rock` | `real` | 55 | % \|percent of rock fragments in soil layer |
| `alb` | `real` | 56 | none \|albedo when soil is moist |
| `usle_k` | `real` | 57 | \|USLE equation soil erodibility (K) factor |
| `ec` | `real` | 58 | dS/m \|electrical conductivity of soil layer |
| `cal` | `real` | 59 | % \|soil CaCo3 |
| `ph` | `real` | 60 | \|soil Ph |

### soil_profile_db

- **Defined in source**: `soil_data_module.f90:63`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `snam` | `character(len=20)` | 64 | NA \|soil series name |
| `nly` | `integer` | 65 | none \|number of soil layers |
| `hydgrp` | `character(len=16)` | 66 | NA \|hydrologic soil group |
| `zmx` | `real` | 67 | mm \|maximum rooting depth |
| `anion_excl` | `real` | 68 | none \|fraction of porosity from which anions are excluded |
| `crk` | `real` | 69 | none \|crack volume potential of soil |
| `texture` | `character(len=16)` | 70 | \|texture of soil |

### soil_database

- **Defined in source**: `soil_data_module.f90:73`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `s` | `soil_profile_db` | 74 |  |
| `ly` | `soilayer_db` | 75 |  |

## Variables Defined
### soil_lte

- **Type**: `soil_lte_database`
- **Defined in source**: `soil_data_module.f90:11`

### solt_db

- **Type**: `soiltest_db`
- **Defined in source**: `soil_data_module.f90:27`

### soildb

- **Type**: `soil_database`
- **Defined in source**: `soil_data_module.f90:77`

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
