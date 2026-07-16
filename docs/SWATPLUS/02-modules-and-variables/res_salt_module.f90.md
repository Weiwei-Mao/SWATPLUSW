---
type: module
tags:
  - swat/module
  - swat/to-read
file: res_salt_module.f90
note_file: res_salt_module.f90
module_name: res_salt_module
defines_types:
  - res_salt_balance
  - res_salt_output
  - reservoir_salt_data
  - res_salt_header
defines_vars:
  - res_saltbz
  - ressalt_d
  - ressalt_m
  - ressalt_y
  - ressalt_a
  - wetsalt_d
  - wetsalt_m
  - wetsalt_y
  - wetsalt_a
  - res_salt_data
  - ressalt_hdr
defines_subroutines: []
defines_functions: []
defines_procedures: []
purpose: ""
---

# res_salt_module

> [!info] Module
> Defines derived types and module-level variables.

## Defined Types
### res_salt_balance

- **Defined in source**: `res_salt_module.f90:5`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `inflow` | `real` | 6 | kg !salt entering the reservoir via streamflow |
| `outflow` | `real` | 7 | kg !salt leaving the reservoir via streamflow |
| `seep` | `real` | 8 | kg !salt leaving the reservoir via seepage to aquifer |
| `fert` | `real` | 9 | kg !salt added to reservoir (wetland) via fertilizer |
| `irrig` | `real` | 10 | kg !salt removed from the reservoir via irrigation diversion |
| `div` | `real` | 11 | kg !salt mass removed or added via diversion |
| `mass` | `real` | 12 | kg !salt in reservoir water at end of day |
| `conc` | `real` | 13 | g/m3 !salt concentration in reservoir at end of day |
| `volm` | `real` | 14 | m3 !volume of water in the reservoir |

### res_salt_output

- **Defined in source**: `res_salt_module.f90:17`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `salt` | `res_salt_balance` | 18 | salt hydrographs |

### reservoir_salt_data

- **Defined in source**: `res_salt_module.f90:35`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `name` | `character(len=25)` | 36 |  |
| `c_init` | `real, dimension (:), allocatable` | 37 | g/m3 \|initial concentration of each salt ion |

### res_salt_header

- **Defined in source**: `res_salt_module.f90:42`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `day` | `character (len=6)` | 43 |  |
| `mo` | `character (len=6)` | 44 |  |
| `day_mo` | `character (len=6)` | 45 |  |
| `yrc` | `character (len=6)` | 46 |  |
| `isd` | `character (len=8)` | 47 |  |
| `id` | `character (len=12)` | 48 |  |
| `so4in` | `character(len=15)` | 49 |  |
| `cain` | `character(len=15)` | 50 |  |
| `mgin` | `character(len=15)` | 51 |  |
| `nain` | `character(len=15)` | 52 |  |
| `kin` | `character(len=15)` | 53 |  |
| `clin` | `character(len=15)` | 54 |  |
| `co3in` | `character(len=15)` | 55 |  |
| `hco3in` | `character(len=15)` | 56 |  |
| `so4out` | `character(len=15)` | 57 |  |
| `caout` | `character(len=15)` | 58 |  |
| `mgout` | `character(len=15)` | 59 |  |
| `naout` | `character(len=15)` | 60 |  |
| `kout` | `character(len=15)` | 61 |  |
| `clout` | `character(len=15)` | 62 |  |
| `co3out` | `character(len=15)` | 63 |  |
| `hco3out` | `character(len=15)` | 64 |  |
| `so4seep` | `character(len=15)` | 65 |  |
| `caseep` | `character(len=15)` | 66 |  |
| `mgseep` | `character(len=15)` | 67 |  |
| `naseep` | `character(len=15)` | 68 |  |
| `kseep` | `character(len=15)` | 69 |  |
| `clseep` | `character(len=15)` | 70 |  |
| `co3seep` | `character(len=15)` | 71 |  |
| `hco3seep` | `character(len=15)` | 72 |  |
| `so4fert` | `character(len=15)` | 73 |  |
| `cafert` | `character(len=15)` | 74 |  |
| `mgfert` | `character(len=15)` | 75 |  |
| `nafert` | `character(len=15)` | 76 |  |
| `kfert` | `character(len=15)` | 77 |  |
| `clfert` | `character(len=15)` | 78 |  |
| `co3fert` | `character(len=15)` | 79 |  |
| `hco3fert` | `character(len=15)` | 80 |  |
| `so4irr` | `character(len=15)` | 81 |  |
| `cairr` | `character(len=15)` | 82 |  |
| `mgirr` | `character(len=15)` | 83 |  |
| `nairr` | `character(len=15)` | 84 |  |
| `kirr` | `character(len=15)` | 85 |  |
| `clirr` | `character(len=15)` | 86 |  |
| `co3irr` | `character(len=15)` | 87 |  |
| `hco3irr` | `character(len=15)` | 88 |  |
| `so4div` | `character(len=15)` | 89 |  |
| `cadiv` | `character(len=15)` | 90 |  |
| `mgdiv` | `character(len=15)` | 91 |  |
| `nadiv` | `character(len=15)` | 92 |  |
| `kdiv` | `character(len=15)` | 93 |  |
| `cldiv` | `character(len=15)` | 94 |  |
| `co3div` | `character(len=15)` | 95 |  |
| `hco3div` | `character(len=15)` | 96 |  |
| `so4` | `character(len=15)` | 97 |  |
| `ca` | `character(len=15)` | 98 |  |
| `mg` | `character(len=15)` | 99 |  |
| `na` | `character(len=15)` | 100 |  |
| `k` | `character(len=15)` | 101 |  |
| `cl` | `character(len=15)` | 102 |  |
| `co3` | `character(len=15)` | 103 |  |
| `hco3` | `character(len=15)` | 104 |  |
| `so4c` | `character(len=15)` | 105 |  |
| `cac` | `character(len=15)` | 106 |  |
| `mgc` | `character(len=15)` | 107 |  |
| `nac` | `character(len=15)` | 108 |  |
| `kc` | `character(len=15)` | 109 |  |
| `clc` | `character(len=15)` | 110 |  |
| `co3c` | `character(len=15)` | 111 |  |
| `hco3c` | `character(len=15)` | 112 |  |
| `volm` | `character(len=15)` | 113 |  |

## Variables Defined
### res_saltbz

- **Type**: `res_salt_balance`
- **Defined in source**: `res_salt_module.f90:20`

### ressalt_d

- **Type**: `res_salt_output`
- **Defined in source**: `res_salt_module.f90:23`

### ressalt_m

- **Type**: `res_salt_output`
- **Defined in source**: `res_salt_module.f90:24`

### ressalt_y

- **Type**: `res_salt_output`
- **Defined in source**: `res_salt_module.f90:25`

### ressalt_a

- **Type**: `res_salt_output`
- **Defined in source**: `res_salt_module.f90:26`

### wetsalt_d

- **Type**: `res_salt_output`
- **Defined in source**: `res_salt_module.f90:29`

### wetsalt_m

- **Type**: `res_salt_output`
- **Defined in source**: `res_salt_module.f90:30`

### wetsalt_y

- **Type**: `res_salt_output`
- **Defined in source**: `res_salt_module.f90:31`

### wetsalt_a

- **Type**: `res_salt_output`
- **Defined in source**: `res_salt_module.f90:32`

### res_salt_data

- **Type**: `reservoir_salt_data`
- **Defined in source**: `res_salt_module.f90:39`

### ressalt_hdr

- **Type**: `res_salt_header`
- **Defined in source**: `res_salt_module.f90:115`

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
