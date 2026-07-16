---
type: module
tags:
  - swat/module
  - swat/to-read
file: landuse_data_module.f90
note_file: landuse_data_module.f90
module_name: landuse_data_module
defines_types:
  - land_use_management
  - land_use_structures
  - curvenumber_table
  - land_use_mgt_groups
  - conservation_practice_table
  - overlandflow_n_table
defines_vars:
  - lum
  - lum_str
  - cn
  - lum_grp
  - cons_prac
  - overland_n
defines_subroutines: []
defines_functions: []
defines_procedures: []
purpose: ""
---

# landuse_data_module

> [!info] Module
> Defines derived types and module-level variables.

## Defined Types
### land_use_management

- **Defined in source**: `landuse_data_module.f90:5`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `name` | `character (len=40)` | 6 | name of the land use and management (from hru-data.hru pointer) |
| `cal_group` | `character (len=40)` | 7 | calibration group (not currently used) |
| `plant_cov` | `character (len=40)` | 8 | plant community initialization (pointer to plants.ini) |
| `mgt_ops` | `character (len=40)` | 9 | management operations (pointer to management.sch) |
| `cn_lu` | `character (len=40)` | 10 | land use for curve number table (pointer to cntable.lum) |
| `cons_prac` | `character (len=40)` | 11 | conservation practice from table (cons_practice.lum) |
| `urb_lu` | `character (len=40)` | 12 | type of urban land use- ie. residential, industrial, etc (urban.urb) |
| `urb_ro` | `character (len=40)` | 13 | urban runoff model "usgs_reg", simulate using USGS regression eqs "buildup_washoff", simulate using build up/wash off alg |
| `ovn` | `character (len=40)` | 16 | Manning"s "n" land use type for overland flow (ovn_table.lum) |
| `tiledrain` | `character (len=40)` | 17 | tile drainage (pointer to tiledrain.str |
| `septic` | `character (len=40)` | 18 | septic tanks (pointer to septic.str) |
| `fstrip` | `character (len=40)` | 19 | filter strips (pointer to filterstrip.str) |
| `grassww` | `character (len=40)` | 20 | grass waterways (pointer to grassedww.str) |
| `bmpuser` | `character (len=40)` | 21 | user specified removal efficiency (pointer to bmpuser.str) |

### land_use_structures

- **Defined in source**: `landuse_data_module.f90:25`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `plant_cov` | `integer` | 26 |  |
| `mgt_ops` | `integer` | 27 |  |
| `cn_lu` | `integer` | 28 |  |
| `cons_prac` | `integer` | 29 |  |
| `tiledrain` | `integer` | 30 |  |
| `septic` | `integer` | 31 |  |
| `fstrip` | `integer` | 32 |  |
| `grassww` | `integer` | 33 |  |
| `bmpuser` | `integer` | 34 |  |

### curvenumber_table

- **Defined in source**: `landuse_data_module.f90:38`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `name` | `character(len=40)` | 39 | name includes abbrev for lu/treatment/condition |
| `cn` | `real, dimension(4)` | 40 | curve number |

### land_use_mgt_groups

- **Defined in source**: `landuse_data_module.f90:44`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `num` | `integer` | 45 |  |
| `name` | `character(len=40), dimension(:), allocatable` | 46 | land use groups |

### conservation_practice_table

- **Defined in source**: `landuse_data_module.f90:50`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `name` | `character(len=40)` | 51 | name of conservation practice |
| `pfac` | `real` | 52 | usle p factor |
| `sl_len_mx` | `real` | 53 | m !maximum slope length |

### overlandflow_n_table

- **Defined in source**: `landuse_data_module.f90:57`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `name` | `character(len=40)` | 58 | name of conservation practice |
| `ovn` | `real` | 59 | overland flow mannings n - mean |
| `ovn_min` | `real` | 60 | overland flow mannings n - min |
| `ovn_max` | `real` | 61 | overland flow mannings n - max |

## Variables Defined
### lum

- **Type**: `land_use_management`
- **Defined in source**: `landuse_data_module.f90:23`

### lum_str

- **Type**: `land_use_structures`
- **Defined in source**: `landuse_data_module.f90:36`

### cn

- **Type**: `curvenumber_table`
- **Defined in source**: `landuse_data_module.f90:42`

### lum_grp

- **Type**: `land_use_mgt_groups`
- **Defined in source**: `landuse_data_module.f90:48`

### cons_prac

- **Type**: `conservation_practice_table`
- **Defined in source**: `landuse_data_module.f90:55`

### overland_n

- **Type**: `overlandflow_n_table`
- **Defined in source**: `landuse_data_module.f90:63`

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
