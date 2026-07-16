---
type: module
tags:
  - swat/module
  - swat/to-read
file: soil_nutcarb_module.f90
note_file: soil_nutcarb_module.f90
module_name: soil_nutcarb_module
defines_types:
  - organic_carbon_header
  - total_carbon_header
  - organic_carbon_units
  - total_carbon_units
defines_vars:
  - orgc_hdr
  - totc_hdr
  - orgc_units
  - totc_units
defines_subroutines: []
defines_functions: []
defines_procedures: []
purpose: ""
---

# soil_nutcarb_module

> [!info] Module
> Defines derived types and module-level variables.

## Defined Types
### organic_carbon_header

- **Defined in source**: `soil_nutcarb_module.f90:5`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `day_mo` | `character (len=12)` | 6 |  |
| `yrc` | `character (len=12)` | 7 |  |
| `hru` | `character (len=12)` | 8 |  |
| `str_c` | `character (len=18)` | 9 |  |
| `lig_c` | `character (len=15)` | 10 |  |
| `meta_c` | `character (len=15)` | 11 |  |
| `man_c` | `character (len=15)` | 12 |  |
| `hum_c` | `character (len=15)` | 13 |  |
| `phum_c` | `character (len=15)` | 14 |  |
| `mb_c` | `character (len=12)` | 15 |  |

### total_carbon_header

- **Defined in source**: `soil_nutcarb_module.f90:19`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `day` | `character (len=12)` | 20 |  |
| `yrc` | `character (len=12)` | 21 |  |
| `isd` | `character (len=12)` | 22 |  |
| `soil_org_c` | `character (len=14)` | 23 |  |
| `plm_com_c` | `character (len=14)` | 24 |  |
| `rsd_com_c` | `character (len=14)` | 25 |  |

### organic_carbon_units

- **Defined in source**: `soil_nutcarb_module.f90:29`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `day` | `character (len=12)` | 30 |  |
| `yrc` | `character (len=12)` | 31 |  |
| `isd` | `character (len=12)` | 32 |  |
| `str_c` | `character (len=18)` | 33 |  |
| `lig_c` | `character (len=15)` | 34 |  |
| `meta_c` | `character (len=15)` | 35 |  |
| `man_c` | `character (len=15)` | 36 |  |
| `hum_c` | `character (len=15)` | 37 |  |
| `phum_c` | `character (len=15)` | 38 |  |
| `mb_c` | `character (len=15)` | 39 |  |

### total_carbon_units

- **Defined in source**: `soil_nutcarb_module.f90:43`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `day` | `character (len=12)` | 44 |  |
| `yrc` | `character (len=12)` | 45 |  |
| `isd` | `character (len=12)` | 46 |  |
| `soil_org_c` | `character (len=14)` | 47 |  |
| `plm_com_c` | `character (len=14)` | 48 |  |
| `rsd_com_c` | `character (len=14)` | 49 |  |

## Variables Defined
### orgc_hdr

- **Type**: `organic_carbon_header`
- **Defined in source**: `soil_nutcarb_module.f90:17`

### totc_hdr

- **Type**: `total_carbon_header`
- **Defined in source**: `soil_nutcarb_module.f90:27`

### orgc_units

- **Type**: `organic_carbon_units`
- **Defined in source**: `soil_nutcarb_module.f90:41`

### totc_units

- **Type**: `total_carbon_units`
- **Defined in source**: `soil_nutcarb_module.f90:51`

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
