---
type: module
tags:
  - swat/module
  - swat/to-read
file: soil_module.f90
note_file: soil_module.f90
module_name: soil_module
defines_types:
  - soilayer
  - soil_physical_properties
  - soil_test
  - soil_profile
  - soil_hru_database
defines_vars:
  - layer1
  - phys1
  - sol_test
  - nmbr_soil_test_layers
  - soil
  - soil_init
  - sol
defines_subroutines: []
defines_functions: []
defines_procedures: []
purpose: ""
---

# soil_module

> [!info] Module
> Defines derived types and module-level variables.

## Defined Types
### soilayer

- **Defined in source**: `soil_module.f90:8`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `ec` | `real` | 9 |  |
| `cal` | `real` | 10 |  |
| `ph` | `real` | 11 |  |
| `alb` | `real` | 12 | none albedo when soil is moist |
| `usle_k` | `real` | 13 | USLE equation soil erodibility (K) factor |
| `conk` | `real` | 14 | mm/hr lateral saturated hydraulic conductivity for each profile layer in a give HRU. |
| `flat` | `real` | 15 | mm H2O lateral flow storage array |
| `prk` | `real` | 16 | mm H2O percolation from soil layer on current day |
| `volcr` | `real` | 17 | mm crack volume for soil layer |
| `tillagef` | `real` | 18 |  |
| `tillagef_biomix` | `real` | 19 |  |
| `tillagef_tillmix` | `real` | 20 |  |
| `bmix` | `real` | 21 |  |
| `init_bmix` | `real` | 22 |  |
| `watp` | `real` | 23 |  |
| `a_days` | `integer` | 24 |  |
| `b_days` | `integer` | 25 |  |
| `psp_store` | `real` | 26 |  |
| `ssp_store` | `real` | 27 |  |
| `percc` | `real` | 28 |  |
| `latc` | `real` | 29 |  |
| `vwt` | `real` | 30 |  |

### soil_physical_properties

- **Defined in source**: `soil_module.f90:34`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `d` | `real` | 35 | mm ! depth to bottom of soil layer |
| `thick` | `real` | 36 | mm ! thickness of soil layer |
| `bd` | `real` | 37 | Mg/m**3 ! bulk density of the soil |
| `k` | `real` | 38 | mm/hr ! saturated hydraulic conductivity of soil layer. Index:(layer,HRU) |
| `cbn` | `real` | 39 | mm/hr ! percent organic carbon of soil layer |
| `clay` | `real` | 40 | % ! percent clay content in soil material (UNIT CHANGE!) |
| `silt` | `real` | 41 | % ! percent silt content in soil material |
| `sand` | `real` | 42 | % ! percent of sand in soil material |
| `rock` | `real` | 43 | % ! percent of rock fragments in soil layer |
| `conv_wt` | `real` | 44 | none ! factor which converts kg/kg to kg/ha |
| `crdep` | `real` | 45 | mm ! maximum or potential crack volume |
| `awc` | `real` | 46 | mm H20/mm \| soil available water capacity of soil layer |
| `fc` | `real` | 47 | mm H2O \| amount of water available to plants in soil layer at field capacity (fc - wp),Index:(layer,HRU) |
| `hk` | `real` | 48 | none ! beta coefficient to calculate hydraulic conductivity |
| `por` | `real` | 49 | none ! total porosity of soil layer expressed as a fraction of the total volume, Index:(layer,HRU) |
| `st` | `real` | 50 | mm H2O ! amount of water stored in the soil layer on any given day (less wp water) |
| `tmp` | `real` | 51 | deg C ! daily average temperature of second soil layer |
| `ul` | `real` | 52 | mm H2O ! amount of water held in the soil layer at saturation (sat - wp water) |
| `up` | `real` | 53 | mm H2O/mm ! soil water content of soil at -0.033 MPa (field capacity) |
| `wp` | `real` | 54 | mm H20/mm ! soil water content of soil at -1.5 MPa (wilting point) |
| `wpmm` | `real` | 55 | mm H20 ! water content of soil at -1.5 MPa (wilting point) |
| `tot_sw` | `real` | 56 | mm H20 ! total soil water content in mm/mm by layer that includes wilting point water content |

### soil_test

- **Defined in source**: `soil_module.f90:60`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `snam` | `character(len=16)` | 61 | NA soil series name |
| `d` | `real` | 62 | mm ! depth in mm of soil carbon test |
| `bd` | `real` | 63 | Mg/m^3 \| bulk density soil test |
| `cbn` | `real` | 64 | % ! percent organic carbon from soil test |
| `sand` | `real` | 65 | % \| percent sand |
| `silt` | `real` | 66 | % \| percent silt |
| `clay` | `real` | 67 | % \| percent clay |

### soil_profile

- **Defined in source**: `soil_module.f90:72`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `snam` | `character(len=16)` | 73 | NA soil series name |
| `hydgrp` | `character(len=16)` | 74 | NA hydrologic soil group |
| `texture` | `character(len=16)` | 75 |  |
| `nly` | `integer` | 76 | none number of soil layers |
| `phys` | `soil_physical_properties` | 77 |  |
| `ly` | `soilayer` | 78 |  |
| `pest` | `real, dimension(:),allocatable` | 79 | kg/ha total pesticide in the soil profile |
| `zmx` | `real` | 80 | mm maximum rooting depth in soil |
| `anion_excl` | `real` | 81 | none fraction of porosity from which anions are excluded |
| `crk` | `real` | 82 | none crack volume potential of soil |
| `alb` | `real` | 83 | none albedo when soil is moist |
| `usle_k` | `real` | 84 | USLE equation soil erodibility (K) factor |
| `det_san` | `real` | 85 |  |
| `det_sil` | `real` | 86 |  |
| `det_cla` | `real` | 87 |  |
| `det_sag` | `real` | 88 |  |
| `det_lag` | `real` | 89 |  |
| `sumul` | `real` | 90 | mm H2O amount of water held in soil profile at saturation |
| `sumfc` | `real` | 91 | mm H2O amount of water held in the soil profile at field capacity |
| `sw` | `real` | 92 | mm H2O amount of water stored in soil profile |
| `sw_300` | `real` | 93 | mm H2O amount of water stored to 300 mm |
| `sumwp` | `real` | 94 |  |
| `swpwt` | `real` | 95 |  |
| `ffc` | `real` | 96 | none initial HRU soil water content expressed as fraction of field capacity |
| `wat_tbl` | `real` | 97 |  |
| `avpor` | `real` | 98 | none average porosity for entire soil profile |
| `avbd` | `real` | 99 | Mg/m^3 average bulk density for soil profile |
| `tmp_srf` | `real` | 100 | celsius surface temperature of the soil |

### soil_hru_database

- **Defined in source**: `soil_module.f90:105`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `snam` | `character(len=16)` | 106 | NA soil series name |
| `hydgrp` | `character(len=16)` | 107 | NA hydrologic soil group |
| `texture` | `character(len=16)` | 108 |  |
| `s` | `soil_profile` | 109 |  |
| `phys` | `soil_physical_properties` | 110 |  |
| `ly` | `soilayer` | 111 |  |

## Variables Defined
### layer1

- **Type**: `soilayer`
- **Defined in source**: `soil_module.f90:32`

### phys1

- **Type**: `soil_physical_properties`
- **Defined in source**: `soil_module.f90:58`

### sol_test

- **Type**: `soil_test`
- **Defined in source**: `soil_module.f90:69`

### nmbr_soil_test_layers

- **Type**: `integer`
- **Defined in source**: `soil_module.f90:70`
- **Source note**: none         |number of soil carbon tests

### soil

- **Type**: `soil_profile`
- **Defined in source**: `soil_module.f90:102`

### soil_init

- **Type**: `soil_profile`
- **Defined in source**: `soil_module.f90:103`

### sol

- **Type**: `soil_hru_database`
- **Defined in source**: `soil_module.f90:113`

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
