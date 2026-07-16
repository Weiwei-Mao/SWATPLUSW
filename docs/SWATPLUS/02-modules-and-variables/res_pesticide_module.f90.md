---
type: module
tags:
  - swat/module
  - swat/to-read
file: res_pesticide_module.f90
note_file: res_pesticide_module.f90
module_name: res_pesticide_module
defines_types:
  - res_pesticide_processes
  - res_pesticide_output
  - res_pesticide_header
defines_vars:
  - res_pestbz
  - respst_d
  - respst_m
  - respst_y
  - respst_a
  - brespst_d
  - brespst_m
  - brespst_y
  - brespst_a
  - respst
  - respstz
  - respest_hdr
defines_subroutines: []
defines_functions:
  - respest_add
  - respest_div
  - respest_ave
defines_procedures:
  - respest_add
  - respest_div
  - respest_ave
purpose: ""
---

# res_pesticide_module

> [!info] Module
> Defines derived types and module-level variables.

## Defined Types
### res_pesticide_processes

- **Defined in source**: `res_pesticide_module.f90:5`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `tot_in` | `real` | 6 | kg !total pesticide into reservoir |
| `sol_out` | `real` | 7 | kg !soluble pesticide out of reservoir |
| `sor_out` | `real` | 8 | kg !sorbed pesticide out of reservoir |
| `react` | `real` | 9 | kg !pesticide lost through reactions in water layer |
| `metab` | `real` | 10 | kg !pesticide metabolized from parent in water layer |
| `volat` | `real` | 11 | kg !pesticide lost through volatilization |
| `settle` | `real` | 12 | kg !pesticide settling to sediment layer |
| `resus` | `real` | 13 | kg !pesticide resuspended into lake water |
| `difus` | `real` | 14 | kg !pesticide diffusing from sediment to water |
| `react_bot` | `real` | 15 | kg !pesticide lost from benthic sediment by reactions |
| `metab_bot` | `real` | 16 | kg !pesticide metabolized from parent in water layer |
| `bury` | `real` | 17 | kg !pesticide lost from benthic sediment by burial |
| `water` | `real` | 18 | kg !pesticide in water at end of day |
| `benthic` | `real` | 19 | kg !pesticide in benthic sediment at end of day |

### res_pesticide_output

- **Defined in source**: `res_pesticide_module.f90:22`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `pest` | `res_pesticide_processes` | 23 | pesticide hydrographs |

### res_pesticide_header

- **Defined in source**: `res_pesticide_module.f90:37`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `day` | `character (len=6)` | 38 |  |
| `mo` | `character (len=6)` | 39 |  |
| `day_mo` | `character (len=6)` | 40 |  |
| `yrc` | `character (len=6)` | 41 |  |
| `isd` | `character (len=8)` | 42 |  |
| `id` | `character (len=8)` | 43 |  |
| `name` | `character (len=16)` | 44 |  |
| `pest` | `character (len=16)` | 45 |  |
| `tot_in` | `character(len=13)` | 46 | (kg) |
| `sol_out` | `character(len=13)` | 47 | (kg) |
| `sor_out` | `character(len=14)` | 48 | (kg) |
| `react` | `character(len=13)` | 49 | (kg) |
| `metab` | `character(len=13)` | 50 | (kg) |
| `volat` | `character(len=10)` | 51 | (kg) |
| `settle` | `character(len=10)` | 52 | (kg) |
| `resus` | `character(len=13)` | 53 | (kg) |
| `difus` | `character(len=11)` | 54 | (kg) |
| `react_bot` | `character(len=15)` | 55 | (kg) |
| `metab_bot` | `character(len=15)` | 56 | (kg) |
| `bury` | `character(len=14)` | 57 | (kg) |
| `water` | `character(len=14)` | 58 | (kg) |
| `benthic` | `character(len=13)` | 59 | (kg) |

## Variables Defined
### res_pestbz

- **Type**: `res_pesticide_processes`
- **Defined in source**: `res_pesticide_module.f90:25`

### respst_d

- **Type**: `res_pesticide_output`
- **Defined in source**: `res_pesticide_module.f90:27`

### respst_m

- **Type**: `res_pesticide_output`
- **Defined in source**: `res_pesticide_module.f90:28`

### respst_y

- **Type**: `res_pesticide_output`
- **Defined in source**: `res_pesticide_module.f90:29`

### respst_a

- **Type**: `res_pesticide_output`
- **Defined in source**: `res_pesticide_module.f90:30`

### brespst_d

- **Type**: `res_pesticide_output`
- **Defined in source**: `res_pesticide_module.f90:31`

### brespst_m

- **Type**: `res_pesticide_output`
- **Defined in source**: `res_pesticide_module.f90:32`

### brespst_y

- **Type**: `res_pesticide_output`
- **Defined in source**: `res_pesticide_module.f90:33`

### brespst_a

- **Type**: `res_pesticide_output`
- **Defined in source**: `res_pesticide_module.f90:34`

### respst

- **Type**: `res_pesticide_output`
- **Defined in source**: `res_pesticide_module.f90:35`

### respstz

- **Type**: `res_pesticide_output`
- **Defined in source**: `res_pesticide_module.f90:35`

### respest_hdr

- **Type**: `res_pesticide_header`
- **Defined in source**: `res_pesticide_module.f90:61`

## Subroutines Defined
(No subroutines detected.)

## Functions Defined
### respest_add

### respest_div

### respest_ave

## Used By Source Routines

```dataview
LIST file.link
WHERE type = "source" AND contains(module, this.module_name)
```

<!-- USER-NOTES-START -->
## Notes
Use this section for type and variable meanings, units, and allowed values. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
