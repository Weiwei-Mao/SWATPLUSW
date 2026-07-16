---
type: module
tags:
  - swat/module
  - swat/to-read
file: output_ls_pathogen_module.f90
note_file: output_ls_pathogen_module.f90
module_name: output_ls_pathogen_module
defines_types:
  - pathogen_balance
  - object_pathogen_balance
  - output_pathbal_header
defines_vars:
  - pathbz
  - hpath_bal
  - hpathb_m
  - hpathb_y
  - hpathb_a
  - rupathb_d
  - rupathb_m
  - rupathb_y
  - rupathb_a
  - bpathb_d
  - bpathb_m
  - bpathb_y
  - bpathb_a
  - pathb_hdr
defines_subroutines: []
defines_functions:
  - hruout_pathbal_add
  - hruout_pathbal_div
  - hruout_pathbal_ave
defines_procedures:
  - hruout_pathbal_add
  - hruout_pathbal_div
  - hruout_pathbal_ave
purpose: ""
---

# output_ls_pathogen_module

> [!info] Module
> Defines derived types and module-level variables.

## Defined Types
### pathogen_balance

- **Defined in source**: `output_ls_pathogen_module.f90:5`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `plant` | `real` | 8 | \|kg/ha \|pathogen on plant foliage |
| `soil` | `real` | 9 | \|kg/ha \|pathogen enrichment ratio |
| `sed` | `real` | 10 | \|kg/ha \|pathogen loading from HRU sorbed onto sediment |
| `surq` | `real` | 11 | \|kg/ha \|amount of pathogen type lost in surface runoff on current day in HRU |
| `latq` | `real` | 12 | \|kg/ha \|amount of pathogen in lateral flow in HRU for the day |
| `perc1` | `real` | 13 | \|kg/ha \|amount of pathogen leached past first layer |
| `apply_sol` | `real` | 14 | \|kg/ha \|amount of pathogen applied to soil |
| `apply_plt` | `real` | 15 | \|kg/ha \|amount of pathogen applied to plant |
| `regro` | `real` | 16 | \|kg/ha \|amount of pathogen regrowth |
| `die_off` | `real` | 17 | \|kg/ha \|amount of pathogen die-off |
| `wash` | `real` | 18 | \|kg/ha \|amount of pathogen washed off from plant to soil |

### object_pathogen_balance

- **Defined in source**: `output_ls_pathogen_module.f90:22`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `path` | `pathogen_balance` | 23 |  |

### output_pathbal_header

- **Defined in source**: `output_ls_pathogen_module.f90:41`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `day` | `character (len=5)` | 42 |  |
| `mo` | `character (len=6)` | 43 |  |
| `day_mo` | `character (len=6)` | 44 |  |
| `yrc` | `character (len=6)` | 45 |  |
| `isd` | `character (len=8)` | 46 |  |
| `id` | `character (len=8)` | 47 |  |
| `name` | `character (len=16)` | 48 |  |
| `plant` | `character (len=14)` | 49 |  |
| `soil` | `character (len=12)` | 50 |  |
| `sed` | `character (len=12)` | 51 |  |
| `surq` | `character (len=12)` | 52 |  |
| `latq` | `character (len=12)` | 53 |  |
| `perc` | `character (len=12)` | 54 |  |
| `apply` | `character (len=12)` | 55 |  |
| `decay` | `character (len=12)` | 56 |  |

## Variables Defined
### pathbz

- **Type**: `pathogen_balance`
- **Defined in source**: `output_ls_pathogen_module.f90:20`

### hpath_bal

- **Type**: `object_pathogen_balance`
- **Defined in source**: `output_ls_pathogen_module.f90:26`

### hpathb_m

- **Type**: `object_pathogen_balance`
- **Defined in source**: `output_ls_pathogen_module.f90:27`

### hpathb_y

- **Type**: `object_pathogen_balance`
- **Defined in source**: `output_ls_pathogen_module.f90:28`

### hpathb_a

- **Type**: `object_pathogen_balance`
- **Defined in source**: `output_ls_pathogen_module.f90:29`

### rupathb_d

- **Type**: `object_pathogen_balance`
- **Defined in source**: `output_ls_pathogen_module.f90:31`

### rupathb_m

- **Type**: `object_pathogen_balance`
- **Defined in source**: `output_ls_pathogen_module.f90:32`

### rupathb_y

- **Type**: `object_pathogen_balance`
- **Defined in source**: `output_ls_pathogen_module.f90:33`

### rupathb_a

- **Type**: `object_pathogen_balance`
- **Defined in source**: `output_ls_pathogen_module.f90:34`

### bpathb_d

- **Type**: `object_pathogen_balance`
- **Defined in source**: `output_ls_pathogen_module.f90:36`

### bpathb_m

- **Type**: `object_pathogen_balance`
- **Defined in source**: `output_ls_pathogen_module.f90:37`

### bpathb_y

- **Type**: `object_pathogen_balance`
- **Defined in source**: `output_ls_pathogen_module.f90:38`

### bpathb_a

- **Type**: `object_pathogen_balance`
- **Defined in source**: `output_ls_pathogen_module.f90:39`

### pathb_hdr

- **Type**: `output_pathbal_header`
- **Defined in source**: `output_ls_pathogen_module.f90:58`

## Subroutines Defined
(No subroutines detected.)

## Functions Defined
### hruout_pathbal_add

### hruout_pathbal_div

### hruout_pathbal_ave

## Used By Source Routines

```dataview
LIST file.link
WHERE type = "source" AND contains(module, this.module_name)
```

<!-- USER-NOTES-START -->
## Notes
Use this section for type and variable meanings, units, and allowed values. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
