---
type: module
tags:
  - swat/module
  - swat/to-read
file: ch_cs_module.f90
note_file: ch_cs_module.f90
module_name: ch_cs_module
defines_types:
  - ch_cs_balance
  - ch_cs_output
  - ch_cs_header
defines_vars:
  - ch_csbz
  - chcs_d
  - chcs_m
  - chcs_y
  - chcs_a
  - chcs_hdr
defines_subroutines: []
defines_functions: []
defines_procedures: []
purpose: ""
---

# ch_cs_module

> [!info] Module
> Defines derived types and module-level variables.

## Defined Types
### ch_cs_balance

- **Defined in source**: `ch_cs_module.f90:7`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `tot_in` | `real` | 8 | kg !total constituent entering the channel |
| `gw_in` | `real` | 9 | kg !total constituent entering the channel from groundwater |
| `tot_out` | `real` | 10 | kg !total constituent leaving the channel |
| `seep` | `real` | 11 | kg !constituent mass leaving the channel via seepage |
| `irr` | `real` | 12 | kg !constituent mass leaving the channel via irrigation |
| `div` | `real` | 13 | kg !constituent mass added to or removed from the channel via diversion |
| `water` | `real` | 14 | kg !total constituent in water at end of day |
| `conc` | `real` | 15 | mg/L !constituent concentration in channel water at end of day |

### ch_cs_output

- **Defined in source**: `ch_cs_module.f90:18`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `cs` | `ch_cs_balance` | 19 | cs hydrographs |

### ch_cs_header

- **Defined in source**: `ch_cs_module.f90:28`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `day` | `character (len=6)` | 29 |  |
| `mo` | `character (len=6)` | 30 |  |
| `day_mo` | `character (len=6)` | 31 |  |
| `yrc` | `character (len=6)` | 32 |  |
| `isd` | `character (len=8)` | 33 |  |
| `id` | `character (len=12)` | 34 |  |
| `seo4in` | `character(len=18)` | 35 |  |
| `seo3in` | `character(len=18)` | 36 |  |
| `bornin` | `character(len=18)` | 37 |  |
| `seo4gw` | `character(len=18)` | 38 |  |
| `seo3gw` | `character(len=18)` | 39 |  |
| `borngw` | `character(len=18)` | 40 |  |
| `seo4out` | `character(len=18)` | 41 |  |
| `seo3out` | `character(len=18)` | 42 |  |
| `bornout` | `character(len=18)` | 43 |  |
| `seo4seep` | `character(len=18)` | 44 |  |
| `seo3seep` | `character(len=18)` | 45 |  |
| `bornseep` | `character(len=18)` | 46 |  |
| `seo4irr` | `character(len=18)` | 47 |  |
| `seo3irr` | `character(len=18)` | 48 |  |
| `bornirr` | `character(len=18)` | 49 |  |
| `seo4div` | `character(len=18)` | 50 |  |
| `seo3div` | `character(len=18)` | 51 |  |
| `borndiv` | `character(len=18)` | 52 |  |
| `seo4` | `character(len=18)` | 53 |  |
| `seo3` | `character(len=18)` | 54 |  |
| `born` | `character(len=18)` | 55 |  |
| `seo4c` | `character(len=18)` | 56 |  |
| `seo3c` | `character(len=18)` | 57 |  |
| `bornc` | `character(len=18)` | 58 |  |

## Variables Defined
### ch_csbz

- **Type**: `ch_cs_balance`
- **Defined in source**: `ch_cs_module.f90:21`

### chcs_d

- **Type**: `ch_cs_output`
- **Defined in source**: `ch_cs_module.f90:23`

### chcs_m

- **Type**: `ch_cs_output`
- **Defined in source**: `ch_cs_module.f90:24`

### chcs_y

- **Type**: `ch_cs_output`
- **Defined in source**: `ch_cs_module.f90:25`

### chcs_a

- **Type**: `ch_cs_output`
- **Defined in source**: `ch_cs_module.f90:26`

### chcs_hdr

- **Type**: `ch_cs_header`
- **Defined in source**: `ch_cs_module.f90:60`

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
