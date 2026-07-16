---
type: module
tags:
  - swat/module
  - swat/to-read
file: ch_salt_module.f90
note_file: ch_salt_module.f90
module_name: ch_salt_module
defines_types:
  - ch_salt_balance
  - ch_salt_output
  - ch_salt_header
defines_vars:
  - ch_saltbz
  - chsalt_d
  - chsalt_m
  - chsalt_y
  - chsalt_a
  - chsalt_hdr
defines_subroutines: []
defines_functions: []
defines_procedures: []
purpose: ""
---

# ch_salt_module

> [!info] Module
> Defines derived types and module-level variables.

## Defined Types
### ch_salt_balance

- **Defined in source**: `ch_salt_module.f90:7`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `tot_in` | `real` | 8 | kg !total salt ion entering the channel |
| `gw_in` | `real` | 9 | kg !total salt ion entering the channel from groundwater |
| `tot_out` | `real` | 10 | kg !total salt ion leaving the channel |
| `seep` | `real` | 11 | kg !total salt ion leaving the channel via seepage |
| `irr` | `real` | 12 | kg !salt ion mass leaving the channel via irrigation |
| `div` | `real` | 13 | kg !salt ion mass added to or removed from the channel via diversion |
| `water` | `real` | 14 | kg !total salt ion in water at end of day |
| `conc` | `real` | 15 | mg/L !salt ion concentration in channel water at end of day |

### ch_salt_output

- **Defined in source**: `ch_salt_module.f90:18`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `salt` | `ch_salt_balance` | 19 | salt hydrographs |

### ch_salt_header

- **Defined in source**: `ch_salt_module.f90:28`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `day` | `character (len=6)` | 29 |  |
| `mo` | `character (len=6)` | 30 |  |
| `day_mo` | `character (len=6)` | 31 |  |
| `yrc` | `character (len=6)` | 32 |  |
| `isd` | `character (len=8)` | 33 |  |
| `id` | `character (len=12)` | 34 |  |
| `so4in` | `character(len=18)` | 35 |  |
| `cain` | `character(len=18)` | 36 |  |
| `mgin` | `character(len=18)` | 37 |  |
| `nain` | `character(len=18)` | 38 |  |
| `kin` | `character(len=18)` | 39 |  |
| `clin` | `character(len=18)` | 40 |  |
| `co3in` | `character(len=18)` | 41 |  |
| `hco3in` | `character(len=18)` | 42 |  |
| `so4gw` | `character(len=18)` | 43 |  |
| `cagw` | `character(len=18)` | 44 |  |
| `mggw` | `character(len=18)` | 45 |  |
| `nagw` | `character(len=18)` | 46 |  |
| `kgw` | `character(len=18)` | 47 |  |
| `clgw` | `character(len=18)` | 48 |  |
| `co3gw` | `character(len=18)` | 49 |  |
| `hco3gw` | `character(len=18)` | 50 |  |
| `so4out` | `character(len=18)` | 51 |  |
| `caout` | `character(len=18)` | 52 |  |
| `mgout` | `character(len=18)` | 53 |  |
| `naout` | `character(len=18)` | 54 |  |
| `kout` | `character(len=18)` | 55 |  |
| `clout` | `character(len=18)` | 56 |  |
| `co3out` | `character(len=18)` | 57 |  |
| `hco3out` | `character(len=18)` | 58 |  |
| `so4seep` | `character(len=18)` | 59 |  |
| `caseep` | `character(len=18)` | 60 |  |
| `mgseep` | `character(len=18)` | 61 |  |
| `naseep` | `character(len=18)` | 62 |  |
| `kseep` | `character(len=18)` | 63 |  |
| `clseep` | `character(len=18)` | 64 |  |
| `co3seep` | `character(len=18)` | 65 |  |
| `hco3seep` | `character(len=18)` | 66 |  |
| `so4irr` | `character(len=18)` | 67 |  |
| `cairr` | `character(len=18)` | 68 |  |
| `mgirr` | `character(len=18)` | 69 |  |
| `nairr` | `character(len=18)` | 70 |  |
| `kirr` | `character(len=18)` | 71 |  |
| `clirr` | `character(len=18)` | 72 |  |
| `co3irr` | `character(len=18)` | 73 |  |
| `hco3irr` | `character(len=18)` | 74 |  |
| `so4div` | `character(len=18)` | 75 |  |
| `cadiv` | `character(len=18)` | 76 |  |
| `mgdiv` | `character(len=18)` | 77 |  |
| `nadiv` | `character(len=18)` | 78 |  |
| `kdiv` | `character(len=18)` | 79 |  |
| `cldiv` | `character(len=18)` | 80 |  |
| `co3div` | `character(len=18)` | 81 |  |
| `hco3div` | `character(len=18)` | 82 |  |
| `so4` | `character(len=18)` | 83 |  |
| `ca` | `character(len=18)` | 84 |  |
| `mg` | `character(len=18)` | 85 |  |
| `na` | `character(len=18)` | 86 |  |
| `k` | `character(len=18)` | 87 |  |
| `cl` | `character(len=18)` | 88 |  |
| `co3` | `character(len=18)` | 89 |  |
| `hco3` | `character(len=18)` | 90 |  |
| `so4c` | `character(len=18)` | 91 |  |
| `cac` | `character(len=18)` | 92 |  |
| `mgc` | `character(len=18)` | 93 |  |
| `nac` | `character(len=18)` | 94 |  |
| `kc` | `character(len=18)` | 95 |  |
| `clc` | `character(len=18)` | 96 |  |
| `co3c` | `character(len=18)` | 97 |  |
| `hco3c` | `character(len=18)` | 98 |  |

## Variables Defined
### ch_saltbz

- **Type**: `ch_salt_balance`
- **Defined in source**: `ch_salt_module.f90:21`

### chsalt_d

- **Type**: `ch_salt_output`
- **Defined in source**: `ch_salt_module.f90:23`

### chsalt_m

- **Type**: `ch_salt_output`
- **Defined in source**: `ch_salt_module.f90:24`

### chsalt_y

- **Type**: `ch_salt_output`
- **Defined in source**: `ch_salt_module.f90:25`

### chsalt_a

- **Type**: `ch_salt_output`
- **Defined in source**: `ch_salt_module.f90:26`

### chsalt_hdr

- **Type**: `ch_salt_header`
- **Defined in source**: `ch_salt_module.f90:100`

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
