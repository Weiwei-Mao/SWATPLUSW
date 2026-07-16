---
type: module
tags:
  - swat/module
  - swat/to-read
file: output_ls_salt_module.f90
note_file: output_ls_salt_module.f90
module_name: output_ls_salt_module
defines_types:
  - salt_balance
  - object_salt_balance
  - output_saltbal_header
defines_vars:
  - saltbz
  - hsaltb_d
  - hsaltb_m
  - hsaltb_y
  - hsaltb_a
  - rusaltb_d
  - rusaltb_m
  - rusaltb_y
  - rusaltb_a
  - bsaltb_d
  - bsaltb_m
  - bsaltb_y
  - bsaltb_a
  - saltb_hdr
defines_subroutines: []
defines_functions:
  - hruout_saltbal_add
  - hruout_saltbal_div
  - hruout_saltbal_ave
defines_procedures:
  - hruout_saltbal_add
  - hruout_saltbal_div
  - hruout_saltbal_ave
purpose: ""
---

# output_ls_salt_module

> [!info] Module
> Defines derived types and module-level variables.

## Defined Types
### salt_balance

- **Defined in source**: `output_ls_salt_module.f90:5`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `plant` | `real` | 6 | \|kg/ha \|salt in plant foliage |
| `soil` | `real` | 7 | \|kg/ha \|salt in soil |
| `surq` | `real` | 8 | \|kg/ha \|amount of pesticide type lost in surface runoff in HRU |
| `latq` | `real` | 9 | \|kg/ha \|amount of pesticide in lateral flow in HRU |
| `tileq` | `real` | 10 | \|kg/ha \|amount of pesticide in tile flow in HRU |
| `perc` | `real` | 11 | \|kg/ha \|amount of pesticide leached past bottom of soil |
| `irrig` | `real` | 12 | \|kg/ha \|amount of pesticide applied on soil |

### object_salt_balance

- **Defined in source**: `output_ls_salt_module.f90:16`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `salt` | `salt_balance` | 17 |  |

### output_saltbal_header

- **Defined in source**: `output_ls_salt_module.f90:35`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `day` | `character (len=5)` | 36 |  |
| `mo` | `character (len=6)` | 37 |  |
| `day_mo` | `character (len=6)` | 38 |  |
| `yrc` | `character (len=6)` | 39 |  |
| `isd` | `character (len=8)` | 40 |  |
| `id` | `character (len=8)` | 41 |  |
| `name` | `character (len=16)` | 42 |  |
| `salt` | `character (len=16)` | 43 |  |
| `plant` | `character (len=13)` | 44 |  |
| `soil` | `character (len=13)` | 45 |  |
| `surq` | `character (len=13)` | 46 |  |
| `latq` | `character (len=13)` | 47 |  |
| `tileq` | `character (len=13)` | 48 |  |
| `perc` | `character (len=13)` | 49 |  |
| `irrig` | `character (len=16)` | 50 |  |

## Variables Defined
### saltbz

- **Type**: `salt_balance`
- **Defined in source**: `output_ls_salt_module.f90:14`

### hsaltb_d

- **Type**: `object_salt_balance`
- **Defined in source**: `output_ls_salt_module.f90:20`

### hsaltb_m

- **Type**: `object_salt_balance`
- **Defined in source**: `output_ls_salt_module.f90:21`

### hsaltb_y

- **Type**: `object_salt_balance`
- **Defined in source**: `output_ls_salt_module.f90:22`

### hsaltb_a

- **Type**: `object_salt_balance`
- **Defined in source**: `output_ls_salt_module.f90:23`

### rusaltb_d

- **Type**: `object_salt_balance`
- **Defined in source**: `output_ls_salt_module.f90:25`

### rusaltb_m

- **Type**: `object_salt_balance`
- **Defined in source**: `output_ls_salt_module.f90:26`

### rusaltb_y

- **Type**: `object_salt_balance`
- **Defined in source**: `output_ls_salt_module.f90:27`

### rusaltb_a

- **Type**: `object_salt_balance`
- **Defined in source**: `output_ls_salt_module.f90:28`

### bsaltb_d

- **Type**: `object_salt_balance`
- **Defined in source**: `output_ls_salt_module.f90:30`

### bsaltb_m

- **Type**: `object_salt_balance`
- **Defined in source**: `output_ls_salt_module.f90:31`

### bsaltb_y

- **Type**: `object_salt_balance`
- **Defined in source**: `output_ls_salt_module.f90:32`

### bsaltb_a

- **Type**: `object_salt_balance`
- **Defined in source**: `output_ls_salt_module.f90:33`

### saltb_hdr

- **Type**: `output_saltbal_header`
- **Defined in source**: `output_ls_salt_module.f90:52`

## Subroutines Defined
(No subroutines detected.)

## Functions Defined
### hruout_saltbal_add

### hruout_saltbal_div

### hruout_saltbal_ave

## Used By Source Routines

```dataview
LIST file.link
WHERE type = "source" AND contains(module, this.module_name)
```

<!-- USER-NOTES-START -->
## Notes
Use this section for type and variable meanings, units, and allowed values. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
