---
type: module
tags:
  - swat/module
  - swat/to-read
file: ch_pesticide_module.f90
note_file: ch_pesticide_module.f90
module_name: ch_pesticide_module
defines_types:
  - ch_pesticide_processes
  - ch_pesticide_output
  - ch_pesticide_header
defines_vars:
  - frsol
  - frsrb
  - ch_pestbz
  - chpst_d
  - chpst_m
  - chpst_y
  - chpst_a
  - bchpst_d
  - bchpst_m
  - bchpst_y
  - bchpst_a
  - chpst
  - chpstz
  - chpest_hdr
defines_subroutines: []
defines_functions:
  - chpest_add
  - chpest_div
  - chpest_ave
defines_procedures:
  - chpest_add
  - chpest_div
  - chpest_ave
purpose: ""
---

# ch_pesticide_module

> [!info] Module
> Defines derived types and module-level variables.

## Defined Types
### ch_pesticide_processes

- **Defined in source**: `ch_pesticide_module.f90:10`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `tot_in` | `real` | 11 | kg !total pesticide into reservoir |
| `sol_out` | `real` | 12 | kg !soluble pesticide out of reservoir |
| `sor_out` | `real` | 13 | kg !sorbed pesticide out of reservoir |
| `react` | `real` | 14 | kg !pesticide lost through reactions in water layer |
| `metab` | `real` | 15 | kg !pesticide metabolized from parent in water layer |
| `volat` | `real` | 16 | kg !pesticide lost through volatilization |
| `settle` | `real` | 17 | kg !pesticide settling to sediment layer |
| `resus` | `real` | 18 | kg !pesticide resuspended into lake water |
| `difus` | `real` | 19 | kg !pesticide diffusing from sediment to water |
| `react_bot` | `real` | 20 | kg !pesticide lost from benthic sediment by reactions |
| `metab_bot` | `real` | 21 | kg !pesticide metabolized from parent in water layer |
| `bury` | `real` | 22 | kg !pesticide lost from benthic sediment by burial |
| `water` | `real` | 23 | kg !pesticide in water at end of day |
| `benthic` | `real` | 24 | kg !pesticide in benthic sediment at tend of day |

### ch_pesticide_output

- **Defined in source**: `ch_pesticide_module.f90:27`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `pest` | `ch_pesticide_processes` | 28 | pesticide hydrographs |

### ch_pesticide_header

- **Defined in source**: `ch_pesticide_module.f90:42`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `day` | `character (len=6)` | 43 |  |
| `mo` | `character (len=6)` | 44 |  |
| `day_mo` | `character (len=6)` | 45 |  |
| `yrc` | `character (len=6)` | 46 |  |
| `isd` | `character (len=8)` | 47 |  |
| `id` | `character (len=8)` | 48 |  |
| `name` | `character (len=16)` | 49 |  |
| `pest` | `character (len=16)` | 50 |  |
| `tot_in` | `character(len=13)` | 51 | (kg) |
| `sol_out` | `character(len=13)` | 52 | (kg) |
| `sor_out` | `character(len=14)` | 53 | (kg) |
| `react` | `character(len=13)` | 54 | (kg) |
| `metab` | `character(len=13)` | 55 | (kg) |
| `volat` | `character(len=12)` | 56 | (kg) |
| `settle` | `character(len=12)` | 57 | (kg) |
| `resus` | `character(len=13)` | 58 | (kg) |
| `difus` | `character(len=12)` | 59 | (kg) |
| `react_bot` | `character(len=15)` | 60 | (kg) |
| `metab_bot` | `character(len=15)` | 61 | (kg) |
| `bury` | `character(len=14)` | 62 | (kg) |
| `water` | `character(len=14)` | 63 | (kg) |
| `benthic` | `character(len=12)` | 64 | (kg) |

## Variables Defined
### frsol

- **Type**: `real`
- **Defined in source**: `ch_pesticide_module.f90:7`
- **Source note**: none          |fraction of pesticide in reach that is soluble

### frsrb

- **Type**: `real`
- **Defined in source**: `ch_pesticide_module.f90:8`
- **Source note**: none          |fraction of pesticide in reach that is sorbed

### ch_pestbz

- **Type**: `ch_pesticide_processes`
- **Defined in source**: `ch_pesticide_module.f90:30`

### chpst_d

- **Type**: `ch_pesticide_output`
- **Defined in source**: `ch_pesticide_module.f90:32`

### chpst_m

- **Type**: `ch_pesticide_output`
- **Defined in source**: `ch_pesticide_module.f90:33`

### chpst_y

- **Type**: `ch_pesticide_output`
- **Defined in source**: `ch_pesticide_module.f90:34`

### chpst_a

- **Type**: `ch_pesticide_output`
- **Defined in source**: `ch_pesticide_module.f90:35`

### bchpst_d

- **Type**: `ch_pesticide_output`
- **Defined in source**: `ch_pesticide_module.f90:36`

### bchpst_m

- **Type**: `ch_pesticide_output`
- **Defined in source**: `ch_pesticide_module.f90:37`

### bchpst_y

- **Type**: `ch_pesticide_output`
- **Defined in source**: `ch_pesticide_module.f90:38`

### bchpst_a

- **Type**: `ch_pesticide_output`
- **Defined in source**: `ch_pesticide_module.f90:39`

### chpst

- **Type**: `ch_pesticide_output`
- **Defined in source**: `ch_pesticide_module.f90:40`

### chpstz

- **Type**: `ch_pesticide_output`
- **Defined in source**: `ch_pesticide_module.f90:40`

### chpest_hdr

- **Type**: `ch_pesticide_header`
- **Defined in source**: `ch_pesticide_module.f90:66`

## Subroutines Defined
(No subroutines detected.)

## Functions Defined
### chpest_add

### chpest_div

### chpest_ave

## Used By Source Routines

```dataview
LIST file.link
WHERE type = "source" AND contains(module, this.module_name)
```

<!-- USER-NOTES-START -->
## Notes
Use this section for type and variable meanings, units, and allowed values. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
