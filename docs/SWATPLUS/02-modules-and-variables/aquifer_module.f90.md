---
type: module
tags:
  - swat/module
  - swat/to-read
file: aquifer_module.f90
note_file: aquifer_module.f90
module_name: aquifer_module
defines_types:
  - aquifer_database
  - aquifer_data_parameters
  - aquifer_dynamic
  - aquifer_init_data_char
  - aquifer_init_data_char_cs
  - aquifer_init_data
  - aqu_header
  - aqu_header_units
defines_vars:
  - aqudb
  - aqu_dat
  - aqu_prm
  - aqu_om_init
  - aqu_d
  - aqu_m
  - aqu_y
  - aqu_a
  - saqu_d
  - saqu_m
  - saqu_y
  - saqu_a
  - baqu_d
  - baqu_m
  - baqu_y
  - baqu_a
  - aquz
  - aqu_init_dat_c
  - aqu_init_dat_c_cs
  - aqu_init
  - aqu_hdr
  - aqu_hdr_units
defines_subroutines: []
defines_functions:
  - aqu_add
  - aqu_div
  - aqu_mult
defines_procedures:
  - aqu_add
  - aqu_div
  - aqu_mult
purpose: ""
---

# aquifer_module

> [!info] Module
> Defines derived types and module-level variables.

## Defined Types
### aquifer_database

- **Defined in source**: `aquifer_module.f90:5`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `aqunm` | `character(len=16)` | 6 | aquifer name |
| `aqu_ini` | `character(len=16)` | 7 | initial aquifer data- points to name in initial.aqu |
| `flo` | `real` | 8 | mm \|flow from aquifer in current time step |
| `dep_bot` | `real` | 9 | m \|depth - mid-slope surface to bottom of aquifer |
| `dep_wt` | `real` | 10 | m \|depth - mid-slope surface to water table (initial) |
| `no3` | `real` | 11 | ppm NO3-N \|nitrate-N concentration in aquifer (initial) |
| `minp` | `real` | 12 | ppm P \|mineral phosphorus concentration in aquifer (initial) |
| `cbn` | `real` | 13 | percent \|organic carbon in aquifer (initial) |
| `flo_dist` | `real` | 14 | m \|average flow distance to stream or object |
| `bf_max` | `real` | 15 | mm \|maximum daily baseflow - when all channels are contributing |
| `alpha` | `real` | 16 | 1/days \|lag factor for groundwater recession curve |
| `revap_co` | `real` | 17 | \|revap oefficient - evap=pet*revap_co |
| `seep` | `real` | 18 | frac \|fraction of recharge that seeps from aquifer |
| `spyld` | `real` | 19 | m^3/m^3 \|specific yield of aquifer |
| `hlife_n` | `real` | 20 | days \|half-life of nitrogen in groundwater |
| `flo_min` | `real` | 21 | m \|water table depth for return flow to occur |
| `revap_min` | `real` | 22 | m \|water table depth for revap to occur |

### aquifer_data_parameters

- **Defined in source**: `aquifer_module.f90:27`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `area_ha` | `real` | 28 | ha \|surface area of aquifer |
| `alpha_e` | `real` | 29 | days \|Exp(-alpha) |
| `nloss` | `real` | 30 | frac \|nloss based on half life |
| `rchrg_prev` | `real` | 31 | m^3 \|previous days recharge |
| `rchrgn_prev` | `real` | 32 | m^3 \|previous days n recharge |

### aquifer_dynamic

- **Defined in source**: `aquifer_module.f90:36`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `flo` | `real` | 37 | mm \|lateral flow from aquifer |
| `dep_wt` | `real` | 38 | m \|average depth from average surface elevation to water table |
| `stor` | `real` | 39 | mm \|average water storage in aquifer in timestep |
| `rchrg` | `real` | 40 | mm \|recharge entering aquifer from other objects |
| `seep` | `real` | 41 | mm \|seepage from bottom of aquifer |
| `revap` | `real` | 42 | mm \|plant water uptake and evaporation |
| `no3_st` | `real` | 43 | kg/ha N \|current total NO3-N mass in aquifer |
| `minp` | `real` | 44 | kg/ha P \|mineral phosphorus transported in return (lateral) flow |
| `cbn` | `real` | 45 | percent \|organic carbon in aquifer - currently static |
| `orgn` | `real` | 46 | kg/ha P \|organic nitrogen in aquifer - currently static |
| `no3_rchg` | `real` | 47 | kg/ha N \|nitrate NO3-N flowing into aquifer from another object |
| `no3_loss` | `real` | 48 | kg/ha \|nitrate NO3-N loss |
| `no3_lat` | `real` | 49 | kg/ha N \|nitrate loading to reach in groundwater |
| `no3_seep` | `real` | 50 | kg/ha N \|seepage of no3 to next object |
| `flo_cha` | `real` | 51 | mm H2O \|surface runoff flowing into channels |
| `flo_res` | `real` | 52 | mm H2O \|surface runoff flowing into reservoirs |
| `flo_ls` | `real` | 53 | mm H2O \|surface runoff flowing into a landscape element (hru or ru) |

### aquifer_init_data_char

- **Defined in source**: `aquifer_module.f90:74`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `name` | `character (len=16)` | 75 | xwalk with aqudb(iaqu)%aqu_ini |
| `org_min` | `character (len=16)` | 76 | points to initial organic-mineral input file |
| `pest` | `character (len=16)` | 77 | points to initial pesticide input file |
| `path` | `character (len=16)` | 78 | points to initial pathogen input file |
| `hmet` | `character (len=16)` | 79 | points to initial heavy metals input file |
| `salt` | `character (len=16)` | 80 | points to initial salt input file |

### aquifer_init_data_char_cs

- **Defined in source**: `aquifer_module.f90:85`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `name` | `character (len=16)` | 86 | xwalk with aqudb(iaqu)%aqu_ini |
| `pest` | `character (len=16)` | 87 | points to initial pesticide input file |
| `path` | `character (len=16)` | 88 | points to initial pathogen input file |
| `hmet` | `character (len=16)` | 89 | points to initial heavy metals input file |
| `salt` | `character (len=16)` | 90 | points to initial salt input file (salt_aqu.ini) |
| `cs` | `character (len=16)` | 91 | points to initial constituent input file (cs_aqu.ini) |

### aquifer_init_data

- **Defined in source**: `aquifer_module.f90:95`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `org_min` | `integer` | 96 | points to initial organic-mineral input file |
| `pest` | `integer` | 97 | points to initial pesticide input file |
| `path` | `integer` | 98 | points to initial pathogen input file |
| `hmet` | `integer` | 99 | points to initial heavy metals input file |
| `salt` | `integer` | 100 | points to initial salt input file |
| `cs` | `integer` | 101 | points to initial constituent input file (rtb cs) |

### aqu_header

- **Defined in source**: `aquifer_module.f90:105`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `day` | `character (len=6)` | 106 |  |
| `mo` | `character (len=6)` | 107 |  |
| `day_mo` | `character (len=6)` | 108 |  |
| `yrc` | `character (len=6)` | 109 |  |
| `isd` | `character (len=8)` | 110 |  |
| `id` | `character (len=8)` | 111 |  |
| `name` | `character (len=16)` | 112 |  |
| `flo` | `character(len=16)` | 113 | (mm) |
| `dep_wt` | `character(len=16)` | 114 | (m) |
| `stor` | `character(len=15)` | 115 | (mm) |
| `rchrg` | `character(len=15)` | 116 | (mm) |
| `seep` | `character(len=15)` | 117 | (mm) |
| `revap` | `character(len=15)` | 118 | (mm) |
| `no3_st` | `character(len=15)` | 119 | (kg/ha N) |
| `minp` | `character(len=15)` | 120 | (kg/ha P) |
| `orgn` | `character(len=15)` | 121 | (kg/ha N) |
| `orgp` | `character(len=15)` | 122 | (kg/ha P) |
| `no3_rchg` | `character(len=15)` | 123 | (kg/ha N) |
| `no3_loss` | `character(len=15)` | 124 | (kg/ha N) |
| `no3_lat` | `character(len=15)` | 125 | (kg N/ha) |
| `no3_seep` | `character(len=15)` | 126 | (kg N/ha) |
| `flo_cha` | `character(len=15)` | 127 | (mm) |
| `flo_res` | `character(len=15)` | 128 | (mm) |
| `flo_ls` | `character(len=15)` | 129 | (mm) |

### aqu_header_units

- **Defined in source**: `aquifer_module.f90:133`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `day` | `character (len=6)` | 134 |  |
| `mo` | `character (len=6)` | 135 |  |
| `day_mo` | `character (len=6)` | 136 |  |
| `yrc` | `character (len=6)` | 137 |  |
| `isd` | `character (len=8)` | 138 |  |
| `id` | `character (len=8)` | 139 |  |
| `name` | `character (len=16)` | 140 |  |
| `flo` | `character(len=16)` | 141 | (mm) |
| `depwt` | `character (len=16)` | 142 | (m) |
| `stor` | `character(len=15)` | 143 | (mm) |
| `rchrg` | `character(len=15)` | 144 | (mm) |
| `seep` | `character(len=15)` | 145 | (mm) |
| `revap` | `character(len=15)` | 146 | (mm) |
| `no3_st` | `character(len=15)` | 147 | (kg/ha N) |
| `minp` | `character(len=15)` | 148 | (kg/ha P) |
| `orgn` | `character(len=15)` | 149 | (kg/ha N) |
| `orgp` | `character(len=15)` | 150 | (kg/ha P) |
| `no3_rchg` | `character(len=15)` | 151 | (kg/ha N) |
| `no3_loss` | `character(len=15)` | 152 | (kg/ha N) |
| `no3_lat` | `character(len=15)` | 153 | (kg N/ha) |
| `no3_seep` | `character(len=15)` | 154 | (kg N/ha) |
| `flo_cha` | `character(len=15)` | 155 | (mm) |
| `flo_res` | `character(len=15)` | 156 | (mm) |
| `flo_ls` | `character(len=15)` | 157 | (mm) |

## Variables Defined
### aqudb

- **Type**: `aquifer_database`
- **Defined in source**: `aquifer_module.f90:24`

### aqu_dat

- **Type**: `aquifer_database`
- **Defined in source**: `aquifer_module.f90:25`

### aqu_prm

- **Type**: `aquifer_data_parameters`
- **Defined in source**: `aquifer_module.f90:34`

### aqu_om_init

- **Type**: `aquifer_dynamic`
- **Defined in source**: `aquifer_module.f90:55`

### aqu_d

- **Type**: `aquifer_dynamic`
- **Defined in source**: `aquifer_module.f90:56`

### aqu_m

- **Type**: `aquifer_dynamic`
- **Defined in source**: `aquifer_module.f90:57`

### aqu_y

- **Type**: `aquifer_dynamic`
- **Defined in source**: `aquifer_module.f90:58`

### aqu_a

- **Type**: `aquifer_dynamic`
- **Defined in source**: `aquifer_module.f90:59`

### saqu_d

- **Type**: `aquifer_dynamic`
- **Defined in source**: `aquifer_module.f90:60`

### saqu_m

- **Type**: `aquifer_dynamic`
- **Defined in source**: `aquifer_module.f90:61`

### saqu_y

- **Type**: `aquifer_dynamic`
- **Defined in source**: `aquifer_module.f90:62`

### saqu_a

- **Type**: `aquifer_dynamic`
- **Defined in source**: `aquifer_module.f90:63`

### baqu_d

- **Type**: `aquifer_dynamic`
- **Defined in source**: `aquifer_module.f90:68`

### baqu_m

- **Type**: `aquifer_dynamic`
- **Defined in source**: `aquifer_module.f90:69`

### baqu_y

- **Type**: `aquifer_dynamic`
- **Defined in source**: `aquifer_module.f90:70`

### baqu_a

- **Type**: `aquifer_dynamic`
- **Defined in source**: `aquifer_module.f90:71`

### aquz

- **Type**: `aquifer_dynamic`
- **Defined in source**: `aquifer_module.f90:72`

### aqu_init_dat_c

- **Type**: `aquifer_init_data_char`
- **Defined in source**: `aquifer_module.f90:82`

### aqu_init_dat_c_cs

- **Type**: `aquifer_init_data_char_cs`
- **Defined in source**: `aquifer_module.f90:93`

### aqu_init

- **Type**: `aquifer_init_data`
- **Defined in source**: `aquifer_module.f90:103`

### aqu_hdr

- **Type**: `aqu_header`
- **Defined in source**: `aquifer_module.f90:131`

### aqu_hdr_units

- **Type**: `aqu_header_units`
- **Defined in source**: `aquifer_module.f90:159`

## Subroutines Defined
(No subroutines detected.)

## Functions Defined
### aqu_add

### aqu_div

### aqu_mult

## Used By Source Routines

```dataview
LIST file.link
WHERE type = "source" AND contains(module, this.module_name)
```

<!-- USER-NOTES-START -->
## Notes
Use this section for type and variable meanings, units, and allowed values. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
