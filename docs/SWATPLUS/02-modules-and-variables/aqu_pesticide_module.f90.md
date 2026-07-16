---
type: module
tags:
  - swat/module
  - swat/to-read
file: aqu_pesticide_module.f90
note_file: aqu_pesticide_module.f90
module_name: aqu_pesticide_module
defines_types:
  - aqu_pesticide_processes
  - aqu_pesticide_output
  - aqu_pesticide_header
defines_vars:
  - aqu_pestbz
  - aqupst_d
  - aqupst_m
  - aqupst_y
  - aqupst_a
  - baqupst_d
  - baqupst_m
  - baqupst_y
  - baqupst_a
  - aqupst
  - aqupstz
  - aqupest_hdr
defines_subroutines: []
defines_functions:
  - aqupest_add
  - aqupest_add_all
  - aqupest_div
  - aqupest_ave
defines_procedures:
  - aqupest_add
  - aqupest_add_all
  - aqupest_div
  - aqupest_ave
purpose: ""
---

# aqu_pesticide_module

> [!info] Module
> Defines derived types and module-level variables.

## Defined Types
### aqu_pesticide_processes

- **Defined in source**: `aqu_pesticide_module.f90:5`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `tot_in` | `real` | 6 | kg !total pesticide into aquifer |
| `sol_flo` | `real` | 7 | kg !soluble pesticide out of aquifer |
| `sor_flo` | `real` | 8 | kg !sorbed pesticide out of aquifer |
| `sol_perc` | `real` | 9 | kg !sorbed pesticide out of aquifer |
| `react` | `real` | 10 | kg !pesticide lost through reactions |
| `metab` | `real` | 11 | kg !amount of pesticide metabolized from parent |
| `stor_ave` | `real` | 12 | kg !average end of day pesticide in aquifer during the time period |
| `stor_init` | `real` | 13 | kg !pesticide in aquifer at the start of the day |
| `stor_final` | `real` | 14 | kg !pesticide in aquifer at the end of the day |

### aqu_pesticide_output

- **Defined in source**: `aqu_pesticide_module.f90:17`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `pest` | `aqu_pesticide_processes` | 18 | pesticide hydrographs |

### aqu_pesticide_header

- **Defined in source**: `aqu_pesticide_module.f90:32`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `day` | `character (len=6)` | 33 |  |
| `mo` | `character (len=6)` | 34 |  |
| `day_mo` | `character (len=6)` | 35 |  |
| `yrc` | `character (len=6)` | 36 |  |
| `isd` | `character (len=8)` | 37 |  |
| `id` | `character (len=8)` | 38 |  |
| `name` | `character (len=16)` | 39 |  |
| `pest` | `character (len=16)` | 40 |  |
| `tot_in` | `character(len=13)` | 41 | (mg) |
| `sol_out` | `character(len=13)` | 42 | (mg) |
| `sor_out` | `character(len=13)` | 43 | (mg) |
| `sol_perc` | `character(len=13)` | 44 | (mg) |
| `react` | `character(len=13)` | 45 | (mg) |
| `metab` | `character(len=13)` | 46 | (mg) |
| `stor_ave` | `character(len=13)` | 47 | (mg) |
| `stor_init` | `character(len=13)` | 48 | (mg) |
| `stor_final` | `character(len=13)` | 49 | (mg) |

## Variables Defined
### aqu_pestbz

- **Type**: `aqu_pesticide_processes`
- **Defined in source**: `aqu_pesticide_module.f90:20`

### aqupst_d

- **Type**: `aqu_pesticide_output`
- **Defined in source**: `aqu_pesticide_module.f90:22`

### aqupst_m

- **Type**: `aqu_pesticide_output`
- **Defined in source**: `aqu_pesticide_module.f90:23`

### aqupst_y

- **Type**: `aqu_pesticide_output`
- **Defined in source**: `aqu_pesticide_module.f90:24`

### aqupst_a

- **Type**: `aqu_pesticide_output`
- **Defined in source**: `aqu_pesticide_module.f90:25`

### baqupst_d

- **Type**: `aqu_pesticide_output`
- **Defined in source**: `aqu_pesticide_module.f90:26`

### baqupst_m

- **Type**: `aqu_pesticide_output`
- **Defined in source**: `aqu_pesticide_module.f90:27`

### baqupst_y

- **Type**: `aqu_pesticide_output`
- **Defined in source**: `aqu_pesticide_module.f90:28`

### baqupst_a

- **Type**: `aqu_pesticide_output`
- **Defined in source**: `aqu_pesticide_module.f90:29`

### aqupst

- **Type**: `aqu_pesticide_output`
- **Defined in source**: `aqu_pesticide_module.f90:30`

### aqupstz

- **Type**: `aqu_pesticide_output`
- **Defined in source**: `aqu_pesticide_module.f90:30`

### aqupest_hdr

- **Type**: `aqu_pesticide_header`
- **Defined in source**: `aqu_pesticide_module.f90:51`

## Subroutines Defined
(No subroutines detected.)

## Functions Defined
### aqupest_add

### aqupest_add_all

### aqupest_div

### aqupest_ave

## Used By Source Routines

```dataview
LIST file.link
WHERE type = "source" AND contains(module, this.module_name)
```

<!-- USER-NOTES-START -->
## Notes
Use this section for type and variable meanings, units, and allowed values. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
