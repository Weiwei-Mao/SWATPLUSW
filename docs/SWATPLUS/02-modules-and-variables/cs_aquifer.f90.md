---
type: module
tags:
  - swat/module
  - swat/to-read
file: cs_aquifer.f90
note_file: cs_aquifer.f90
module_name: cs_aquifer
defines_types:
  - cs_balance_aqu
  - object_cs_balance_aqu
  - output_cs_header
defines_vars:
  - acsb_d
  - acsb_m
  - acsb_y
  - acsb_a
  - bacs_d
  - bacs_m
  - bacs_y
  - bacs_a
  - csbz_aqu
  - cs_hdr_aqu
defines_subroutines: []
defines_functions: []
defines_procedures: []
purpose: ""
---

# cs_aquifer

> [!info] Module
> Defines derived types and module-level variables.

## Defined Types
### cs_balance_aqu

- **Defined in source**: `cs_aquifer.f90:6`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `csgw` | `real` | 7 | \|kg \|mass loaded to streams from the aquifer |
| `rchrg` | `real` | 8 | \|kg \|mass reaching the water table (recharge) |
| `seep` | `real` | 9 | \|kg \|mass seepage out of aquifer |
| `irr` | `real` | 10 | \|kg \|mass removed via irrigation (groundwater pumping) |
| `div` | `real` | 11 | \|kg \|mass removed or added via diversion |
| `sorb` | `real` | 12 | \|kg \|mass transferred from sorbed phase to dissolved phase |
| `rctn` | `real` | 13 | \|kg \|mass transferred by chemical reaction |
| `mass` | `real` | 14 | \|kg !mass stored in aquifer |
| `conc` | `real` | 15 | \|g/m3 \|concentration in groundwater |
| `srbd` | `real` | 16 | \|kg \|mass sorbed to aquifer material |

### object_cs_balance_aqu

- **Defined in source**: `cs_aquifer.f90:19`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `cs` | `cs_balance_aqu` | 20 |  |

### output_cs_header

- **Defined in source**: `cs_aquifer.f90:37`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `day` | `character (len=6)` | 38 |  |
| `mo` | `character (len=6)` | 39 |  |
| `day_mo` | `character (len=6)` | 40 |  |
| `yrc` | `character (len=6)` | 41 |  |
| `isd` | `character (len=8)` | 42 |  |
| `id` | `character (len=12)` | 43 |  |
| `seo4` | `character(len=18)` | 44 |  |
| `seo3` | `character(len=18)` | 45 |  |
| `born` | `character(len=18)` | 46 |  |
| `seo4r` | `character(len=18)` | 47 |  |
| `seo3r` | `character(len=18)` | 48 |  |
| `bornr` | `character(len=18)` | 49 |  |
| `seo4s` | `character(len=18)` | 50 |  |
| `seo3s` | `character(len=18)` | 51 |  |
| `borns` | `character(len=18)` | 52 |  |
| `seo4i` | `character(len=18)` | 53 |  |
| `seo3i` | `character(len=18)` | 54 |  |
| `borni` | `character(len=18)` | 55 |  |
| `seo4v` | `character(len=18)` | 56 |  |
| `seo3v` | `character(len=18)` | 57 |  |
| `bornv` | `character(len=18)` | 58 |  |
| `seo4b` | `character(len=18)` | 59 |  |
| `seo3b` | `character(len=18)` | 60 |  |
| `bornb` | `character(len=18)` | 61 |  |
| `seo4t` | `character(len=18)` | 62 |  |
| `seo3t` | `character(len=18)` | 63 |  |
| `bornt` | `character(len=18)` | 64 |  |
| `seo4m` | `character(len=18)` | 65 |  |
| `seo3m` | `character(len=18)` | 66 |  |
| `bornm` | `character(len=18)` | 67 |  |
| `seo4c` | `character(len=18)` | 68 |  |
| `seo3c` | `character(len=18)` | 69 |  |
| `bornc` | `character(len=18)` | 70 |  |
| `seo4d` | `character(len=18)` | 71 |  |
| `seo3d` | `character(len=18)` | 72 |  |
| `bornd` | `character(len=18)` | 73 |  |

## Variables Defined
### acsb_d

- **Type**: `object_cs_balance_aqu`
- **Defined in source**: `cs_aquifer.f90:24`

### acsb_m

- **Type**: `object_cs_balance_aqu`
- **Defined in source**: `cs_aquifer.f90:25`

### acsb_y

- **Type**: `object_cs_balance_aqu`
- **Defined in source**: `cs_aquifer.f90:26`

### acsb_a

- **Type**: `object_cs_balance_aqu`
- **Defined in source**: `cs_aquifer.f90:27`

### bacs_d

- **Type**: `object_cs_balance_aqu`
- **Defined in source**: `cs_aquifer.f90:30`

### bacs_m

- **Type**: `object_cs_balance_aqu`
- **Defined in source**: `cs_aquifer.f90:31`

### bacs_y

- **Type**: `object_cs_balance_aqu`
- **Defined in source**: `cs_aquifer.f90:32`

### bacs_a

- **Type**: `object_cs_balance_aqu`
- **Defined in source**: `cs_aquifer.f90:33`

### csbz_aqu

- **Type**: `object_cs_balance_aqu`
- **Defined in source**: `cs_aquifer.f90:34`

### cs_hdr_aqu

- **Type**: `output_cs_header`
- **Defined in source**: `cs_aquifer.f90:75`

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
