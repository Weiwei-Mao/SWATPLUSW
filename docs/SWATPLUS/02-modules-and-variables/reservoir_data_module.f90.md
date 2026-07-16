---
type: module
tags:
  - swat/module
  - swat/to-read
file: reservoir_data_module.f90
note_file: reservoir_data_module.f90
module_name: reservoir_data_module
defines_types:
  - reservoir_data_char_input
  - reservoir_data_char_input_cs
  - reservoir_data
  - reservoir_init_data_char
  - reservoir_init_data
  - reservoir_hyd_data
  - wetland_hyd_data
  - reservoir_sed_data
  - reservoir_nut_data
  - water_body_data_parameters
  - reservoir_weir_outflow
defines_vars:
  - res_dat_c
  - wet_dat_c
  - res_dat_c_cs
  - wet_dat_c_cs
  - res_dat
  - wet_dat
  - res_datz
  - res_init_dat_c
  - res_init
  - wet_init
  - res_hyd
  - res_hyddb
  - wet_hyd
  - wet_hyddb
  - res_sed
  - res_nut
  - res_prm
  - wet_prm
  - wbody_prm
  - res_weir
defines_subroutines: []
defines_functions: []
defines_procedures: []
purpose: ""
---

# reservoir_data_module

> [!info] Module
> Defines derived types and module-level variables.

## Defined Types
### reservoir_data_char_input

- **Defined in source**: `reservoir_data_module.f90:5`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `name` | `character (len=25)` | 6 |  |
| `init` | `character (len=25)` | 7 | initial data-points to initial.res |
| `hyd` | `character (len=25)` | 8 | points to hydrology.res for hydrology inputs |
| `release` | `character (len=25)` | 9 | 0=simulated; 1=measured outflow |
| `sed` | `character (len=25)` | 10 | sediment inputs-points to sediment.res |
| `nut` | `character (len=25)` | 11 | nutrient inputs-points to nutrient.res |

### reservoir_data_char_input_cs

- **Defined in source**: `reservoir_data_module.f90:17`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `pst` | `character (len=25)` | 18 | pesticide inputs-points to pesticide.res |
| `weir` | `character (len=25)` | 19 | weir inputs-points to weir.res Jaehak 2022 |
| `salt` | `character (len=25)` | 20 | salt inputs - points to salt_res rtb salt |
| `cs` | `character (len=25)` | 21 | constituent inputs - points to cs_res rtb cs |

### reservoir_data

- **Defined in source**: `reservoir_data_module.f90:26`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `name` | `character(len=25)` | 27 |  |
| `init` | `integer` | 28 | initial data-points to initial.res |
| `hyd` | `integer` | 29 | points to hydrology.res for hydrology inputs |
| `release` | `integer` | 30 | 0=simulated; 1=measured outflow |
| `sed` | `integer` | 31 | sediment inputs-points to sediment.res |
| `nut` | `integer` | 32 | nutrient inputs-points to nutrient.res |
| `pst` | `integer` | 33 | pesticide inputs-points to pesticide.res |
| `salt` | `integer` | 34 | salt input-points to salt.res |
| `cs` | `integer` | 35 | constituent inputs-points to cs.res |
| `weir` | `character (len=25)` | 36 | weir inputs-points to weir.res Jaehak 2022 |

### reservoir_init_data_char

- **Defined in source**: `reservoir_data_module.f90:42`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `init` | `character (len=25)` | 43 | initial data-points to initial.cha |
| `org_min` | `character (len=25)` | 44 | points to initial organic-mineral input file |
| `pest` | `character (len=25)` | 45 | points to initial pesticide input file |
| `path` | `character (len=25)` | 46 | points to initial pathogen input file |
| `hmet` | `character (len=25)` | 47 | points to initial heavy metals input file |
| `salt` | `character (len=25)` | 48 | points to initial salt input file |

### reservoir_init_data

- **Defined in source**: `reservoir_data_module.f90:52`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `init` | `integer` | 53 | initial data-points to initial.cha |
| `org_min` | `integer` | 54 | points to initial organic-mineral input file |
| `pest` | `integer` | 55 | points to initial pesticide input file |
| `path` | `integer` | 56 | points to initial pathogen input file |
| `hmet` | `integer` | 57 | points to initial heavy metals input file |
| `salt` | `integer` | 58 | points to initial salt input file |
| `cs` | `integer` | 59 | points to initial constituent input file (rtb cs) |

### reservoir_hyd_data

- **Defined in source**: `reservoir_data_module.f90:64`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `name` | `character(len=25)` | 65 |  |
| `iyres` | `integer` | 66 | none \|year of the sim that the res becomes operational |
| `mores` | `integer` | 67 | none \|month the res becomes operational |
| `psa` | `real` | 68 | ha \|res surface area when res is filled to princ spillway |
| `pvol` | `real` | 69 | ha-m \|vol of water needed to fill the res to the princ spillway (read in as ha-m and converted to m^3) |
| `esa` | `real` | 71 | ha \|res surface area when res is filled to emerg spillway |
| `evol` | `real` | 72 | ha-m \|vol of water needed to fill the res to the emerg spillway (read in as ha-m and converted to m^3) |
| `k` | `real` | 74 | mm/hr \|hydraulic conductivity of the res bottom |
| `evrsv` | `real` | 75 | none \|lake evap coeff |
| `br1` | `real` | 76 | none \|vol-surface area coefficient for reservoirs (model estimates if zero) |
| `br2` | `real` | 77 | none \|vol-surface area coefficient for reservoirs (model estimates if zero) |

### wetland_hyd_data

- **Defined in source**: `reservoir_data_module.f90:82`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `name` | `character(len=25)` | 83 |  |
| `psa` | `real` | 84 | frac \|fraction of hru area at principal spillway (ie: when surface inlet riser flow starts) |
| `pdep` | `real` | 85 | mm \|average depth of water at principal spillway |
| `esa` | `real` | 86 | frac \|fraction of hru area at emergency spillway (ie: when starts to spill into ditch) |
| `edep` | `real` | 87 | mm \|average depth of water at emergency spillway |
| `k` | `real` | 88 | mm/hr \|hydraulic conductivity of the wetland bottom |
| `evrsv` | `real` | 89 | none \|wetland evap coeff |
| `acoef` | `real` | 90 | none \|vol-surface area coefficient for hru impoundment |
| `bcoef` | `real` | 91 | none \|vol-depth coefficient for hru impoundment |
| `ccoef` | `real` | 92 | none \|vol-depth coefficient for hru impoundment |
| `frac` | `real` | 93 | none \|fraction of hru that drains into impoundment |

### reservoir_sed_data

- **Defined in source**: `reservoir_data_module.f90:98`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `name` | `character(len=25)` | 99 |  |
| `nsed` | `real` | 100 | kg/L \|normal amt of sed in res (read in as mg/L and convert to kg/L) |
| `d50` | `real` | 101 | um \|median particle size of suspended and benthic sediment |
| `carbon` | `real` | 102 | % \|organic carbon in suspended and benthic sediment |
| `bd` | `real` | 103 | t/m^3 \|bulk density of benthic sediment |
| `sed_stlr` | `real` | 104 | none \|sediment settling rate |
| `velsetlr` | `real` | 105 | m/d \|sediment settling velocity |

### reservoir_nut_data

- **Defined in source**: `reservoir_data_module.f90:109`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `name` | `character(len=25)` | 110 |  |
| `ires1` | `integer` | 111 | none \|beg of mid-year nutrient settling "season" |
| `ires2` | `integer` | 112 | none \|end of mid-year nutrient settling "season" |
| `nsetlr1` | `real` | 113 | frac \|nit mass loss rate for mid-year period |
| `nsetlr2` | `real` | 114 | frac \|nit mass loss rate for remainder of year |
| `psetlr1` | `real` | 115 | frac \|phos mass loss rate for mid-year period |
| `psetlr2` | `real` | 116 | frac \|phos mass loss rate for remainder of year |
| `nsolr` | `real` | 117 | none \|loss rate for souble n - no3, nh3, no2 |
| `psolr` | `real` | 118 | none \|loss rate for soluble p |
| `theta_n` | `real` | 119 | none \|temperature adjustment for nitrogen loss (settling) |
| `theta_p` | `real` | 120 | none \|temperature adjustment for phosphorus loss (settling) |
| `conc_nmin` | `real` | 121 | ppm \|minimum nitrogen concentration for settling |
| `conc_pmin` | `real` | 122 | ppm \|minimum phosphorus concentration for settling |

### water_body_data_parameters

- **Defined in source**: `reservoir_data_module.f90:126`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `sed` | `reservoir_sed_data` | 127 |  |
| `nut` | `reservoir_nut_data` | 128 |  |
| `sed_stlr_co` | `real` | 129 | none \| |
| `soln_stl_fr` | `real` | 130 | none \| |
| `solp_stl_fr` | `real` | 131 | none \| |

### reservoir_weir_outflow

- **Defined in source**: `reservoir_data_module.f90:137`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `name` | `character(len=25)` | 138 |  |
| `c` | `real` | 139 | none \|weir discharge linear coefficient |
| `k` | `real` | 140 | none \|weir discharge exponential coefficient |
| `w` | `real` | 141 | m \|width |
| `h` | `real` | 142 | m \|height of weir above bottoom of impoundment |

## Variables Defined
### res_dat_c

- **Type**: `reservoir_data_char_input`
- **Defined in source**: `reservoir_data_module.f90:13`

### wet_dat_c

- **Type**: `reservoir_data_char_input`
- **Defined in source**: `reservoir_data_module.f90:14`

### res_dat_c_cs

- **Type**: `reservoir_data_char_input_cs`
- **Defined in source**: `reservoir_data_module.f90:23`

### wet_dat_c_cs

- **Type**: `reservoir_data_char_input_cs`
- **Defined in source**: `reservoir_data_module.f90:24`

### res_dat

- **Type**: `reservoir_data`
- **Defined in source**: `reservoir_data_module.f90:38`

### wet_dat

- **Type**: `reservoir_data`
- **Defined in source**: `reservoir_data_module.f90:39`

### res_datz

- **Type**: `reservoir_data`
- **Defined in source**: `reservoir_data_module.f90:40`

### res_init_dat_c

- **Type**: `reservoir_init_data_char`
- **Defined in source**: `reservoir_data_module.f90:50`

### res_init

- **Type**: `reservoir_init_data`
- **Defined in source**: `reservoir_data_module.f90:61`

### wet_init

- **Type**: `reservoir_init_data`
- **Defined in source**: `reservoir_data_module.f90:62`

### res_hyd

- **Type**: `reservoir_hyd_data`
- **Defined in source**: `reservoir_data_module.f90:79`

### res_hyddb

- **Type**: `reservoir_hyd_data`
- **Defined in source**: `reservoir_data_module.f90:80`

### wet_hyd

- **Type**: `wetland_hyd_data`
- **Defined in source**: `reservoir_data_module.f90:95`

### wet_hyddb

- **Type**: `wetland_hyd_data`
- **Defined in source**: `reservoir_data_module.f90:96`

### res_sed

- **Type**: `reservoir_sed_data`
- **Defined in source**: `reservoir_data_module.f90:107`

### res_nut

- **Type**: `reservoir_nut_data`
- **Defined in source**: `reservoir_data_module.f90:124`

### res_prm

- **Type**: `water_body_data_parameters`
- **Defined in source**: `reservoir_data_module.f90:133`

### wet_prm

- **Type**: `water_body_data_parameters`
- **Defined in source**: `reservoir_data_module.f90:134`

### wbody_prm

- **Type**: `water_body_data_parameters`
- **Defined in source**: `reservoir_data_module.f90:135`
- **Source note**: used for reservoir and wetlands

### res_weir

- **Type**: `reservoir_weir_outflow`
- **Defined in source**: `reservoir_data_module.f90:144`

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
