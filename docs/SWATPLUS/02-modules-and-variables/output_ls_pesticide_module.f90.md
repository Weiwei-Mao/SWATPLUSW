---
type: module
tags:
  - swat/module
  - swat/to-read
file: output_ls_pesticide_module.f90
note_file: output_ls_pesticide_module.f90
module_name: output_ls_pesticide_module
defines_types:
  - pesticide_balance
  - object_pesticide_balance
  - output_pestbal_header
defines_vars:
  - pestbz
  - hpestb_d
  - hpestb_m
  - hpestb_y
  - hpestb_a
  - rupestb_d
  - rupestb_m
  - rupestb_y
  - rupestb_a
  - bpestb_d
  - bpestb_m
  - bpestb_y
  - bpestb_a
  - pestb_hdr
defines_subroutines: []
defines_functions:
  - hruout_pestbal_add
  - hruout_pestbal_mult
  - hruout_pestbal_div
  - hruout_pestbal_ave
defines_procedures:
  - hruout_pestbal_add
  - hruout_pestbal_mult
  - hruout_pestbal_div
  - hruout_pestbal_ave
purpose: ""
---

# output_ls_pesticide_module

> [!info] Module
> Defines derived types and module-level variables.

## Defined Types
### pesticide_balance

- **Defined in source**: `output_ls_pesticide_module.f90:5`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `plant` | `real` | 8 | \|kg/ha \|pesticide on plant foliage |
| `soil` | `real` | 9 | \|kg/ha \|pesticide in soil |
| `sed` | `real` | 10 | \|kg/ha \|pesticide loading from HRU sorbed onto sediment |
| `surq` | `real` | 11 | \|kg/ha \|amount of pesticide type lost in surface runoff in HRU |
| `latq` | `real` | 12 | \|kg/ha \|amount of pesticide in lateral flow in HRU |
| `tileq` | `real` | 13 | \|kg/ha \|amount of pesticide in tile flow in HRU |
| `perc` | `real` | 14 | \|kg/ha \|amount of pesticide leached past bottom of soil |
| `apply_s` | `real` | 15 | \|kg/ha \|amount of pesticide applied on soil |
| `apply_f` | `real` | 16 | \|kg/ha \|amount of pesticide applied on foliage |
| `decay_s` | `real` | 17 | \|kg/ha \|amount of pesticide decayed on soil |
| `decay_f` | `real` | 18 | \|kg/ha \|amount of pesticide decayed on foliage |
| `wash` | `real` | 19 | \|kg/ha \|amount of pesticide washed off from plant to soil |
| `metab_s` | `real` | 20 | \|kg/ha \|amount of pesticide metabolized from parent in soil |
| `metab_f` | `real` | 21 | \|kg/ha \|amount of pesticide metabolized from parent on foilage |
| `pl_uptake` | `real` | 22 | \|kg/ha \|amount of pesticide taken up by plants |
| `in_plant` | `real` | 23 | \|kg/ha \|pesticide in plant foliage |

### object_pesticide_balance

- **Defined in source**: `output_ls_pesticide_module.f90:27`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `pest` | `pesticide_balance` | 28 |  |

### output_pestbal_header

- **Defined in source**: `output_ls_pesticide_module.f90:46`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `day` | `character (len=5)` | 47 |  |
| `mo` | `character (len=6)` | 48 |  |
| `day_mo` | `character (len=6)` | 49 |  |
| `yrc` | `character (len=6)` | 50 |  |
| `isd` | `character (len=8)` | 51 |  |
| `id` | `character (len=8)` | 52 |  |
| `name` | `character (len=16)` | 53 |  |
| `pest` | `character (len=16)` | 54 |  |
| `on_plant` | `character (len=15)` | 55 |  |
| `soil` | `character (len=15)` | 56 |  |
| `sed` | `character (len=15)` | 57 |  |
| `surq` | `character (len=15)` | 58 |  |
| `latq` | `character (len=15)` | 59 |  |
| `tileq` | `character (len=15)` | 60 |  |
| `perc` | `character (len=15)` | 61 |  |
| `apply_s` | `character (len=15)` | 62 |  |
| `apply_f` | `character (len=15)` | 63 |  |
| `decay_s` | `character (len=15)` | 64 |  |
| `decay_f` | `character (len=15)` | 65 |  |
| `wash` | `character (len=15)` | 66 |  |
| `metab_s` | `character (len=15)` | 67 |  |
| `metab_f` | `character (len=15)` | 68 |  |
| `uptake` | `character (len=15)` | 69 |  |
| `in_plant` | `character (len=15)` | 70 |  |

## Variables Defined
### pestbz

- **Type**: `pesticide_balance`
- **Defined in source**: `output_ls_pesticide_module.f90:25`

### hpestb_d

- **Type**: `object_pesticide_balance`
- **Defined in source**: `output_ls_pesticide_module.f90:31`

### hpestb_m

- **Type**: `object_pesticide_balance`
- **Defined in source**: `output_ls_pesticide_module.f90:32`

### hpestb_y

- **Type**: `object_pesticide_balance`
- **Defined in source**: `output_ls_pesticide_module.f90:33`

### hpestb_a

- **Type**: `object_pesticide_balance`
- **Defined in source**: `output_ls_pesticide_module.f90:34`

### rupestb_d

- **Type**: `object_pesticide_balance`
- **Defined in source**: `output_ls_pesticide_module.f90:36`

### rupestb_m

- **Type**: `object_pesticide_balance`
- **Defined in source**: `output_ls_pesticide_module.f90:37`

### rupestb_y

- **Type**: `object_pesticide_balance`
- **Defined in source**: `output_ls_pesticide_module.f90:38`

### rupestb_a

- **Type**: `object_pesticide_balance`
- **Defined in source**: `output_ls_pesticide_module.f90:39`

### bpestb_d

- **Type**: `object_pesticide_balance`
- **Defined in source**: `output_ls_pesticide_module.f90:41`

### bpestb_m

- **Type**: `object_pesticide_balance`
- **Defined in source**: `output_ls_pesticide_module.f90:42`

### bpestb_y

- **Type**: `object_pesticide_balance`
- **Defined in source**: `output_ls_pesticide_module.f90:43`

### bpestb_a

- **Type**: `object_pesticide_balance`
- **Defined in source**: `output_ls_pesticide_module.f90:44`

### pestb_hdr

- **Type**: `output_pestbal_header`
- **Defined in source**: `output_ls_pesticide_module.f90:72`

## Subroutines Defined
(No subroutines detected.)

## Functions Defined
### hruout_pestbal_add

### hruout_pestbal_mult

### hruout_pestbal_div

### hruout_pestbal_ave

## Used By Source Routines

```dataview
LIST file.link
WHERE type = "source" AND contains(module, this.module_name)
```

<!-- USER-NOTES-START -->
## Notes
Use this section for type and variable meanings, units, and allowed values. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
