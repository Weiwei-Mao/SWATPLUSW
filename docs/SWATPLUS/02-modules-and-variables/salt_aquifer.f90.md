---
type: module
tags:
  - swat/module
  - swat/to-read
file: salt_aquifer.f90
note_file: salt_aquifer.f90
module_name: salt_aquifer
defines_types:
  - salt_balance_aqu
  - object_salt_balance_aqu
  - output_salt_header
defines_vars:
  - testing_aquifer
  - asaltb_d
  - asaltb_m
  - asaltb_y
  - asaltb_a
  - basalt_d
  - basalt_m
  - basalt_y
  - basalt_a
  - saltbz_aqu
  - salt_hdr_aqu
defines_subroutines: []
defines_functions: []
defines_procedures: []
purpose: ""
---

# salt_aquifer

> [!info] Module
> Defines derived types and module-level variables.

## Defined Types
### salt_balance_aqu

- **Defined in source**: `salt_aquifer.f90:7`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `diss` | `real` | 8 | \|kg \|salt ion mass transferred from sorbed phase to dissolved phase |
| `rchrg` | `real` | 9 | \|kg \|salt ion mass reaching the water table (recharge) |
| `seep` | `real` | 10 | \|kg \|salt ion mass seepage out of aquifer |
| `saltgw` | `real` | 11 | \|kg \|salt ion mass loaded to streams from the aquifer |
| `irr` | `real` | 12 | \|kg \|salt ion mass removed via irrigation (groundwater pumping) |
| `div` | `real` | 13 | \|kg \|salt ion mass removed via diversion |
| `mass` | `real` | 14 | \|kg !salt ion mass in aquifer |
| `conc` | `real` | 15 | \|g/m3 \|salt ion mass concentration in groundwater |

### object_salt_balance_aqu

- **Defined in source**: `salt_aquifer.f90:18`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `salt` | `salt_balance_aqu` | 19 |  |

### output_salt_header

- **Defined in source**: `salt_aquifer.f90:36`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `day` | `character (len=6)` | 37 |  |
| `mo` | `character (len=6)` | 38 |  |
| `day_mo` | `character (len=6)` | 39 |  |
| `yrc` | `character (len=6)` | 40 |  |
| `isd` | `character (len=8)` | 41 |  |
| `id` | `character (len=12)` | 42 |  |
| `so4` | `character(len=18)` | 43 |  |
| `ca` | `character(len=18)` | 44 |  |
| `mg` | `character(len=18)` | 45 |  |
| `na` | `character(len=18)` | 46 |  |
| `k` | `character(len=18)` | 47 |  |
| `cl` | `character(len=18)` | 48 |  |
| `co3` | `character(len=18)` | 49 |  |
| `hco3` | `character(len=18)` | 50 |  |
| `so4r` | `character(len=18)` | 51 |  |
| `car` | `character(len=18)` | 52 |  |
| `mgr` | `character(len=18)` | 53 |  |
| `nar` | `character(len=18)` | 54 |  |
| `kr` | `character(len=18)` | 55 |  |
| `clr` | `character(len=18)` | 56 |  |
| `co3r` | `character(len=18)` | 57 |  |
| `hco3r` | `character(len=18)` | 58 |  |
| `so4s` | `character(len=18)` | 59 |  |
| `cas` | `character(len=18)` | 60 |  |
| `mgs` | `character(len=18)` | 61 |  |
| `nas` | `character(len=18)` | 62 |  |
| `ks` | `character(len=18)` | 63 |  |
| `cls` | `character(len=18)` | 64 |  |
| `co3s` | `character(len=18)` | 65 |  |
| `hco3s` | `character(len=18)` | 66 |  |
| `so4i` | `character(len=18)` | 67 |  |
| `cai` | `character(len=18)` | 68 |  |
| `mgi` | `character(len=18)` | 69 |  |
| `nai` | `character(len=18)` | 70 |  |
| `ki` | `character(len=18)` | 71 |  |
| `cli` | `character(len=18)` | 72 |  |
| `co3i` | `character(len=18)` | 73 |  |
| `hco3i` | `character(len=18)` | 74 |  |
| `so4d` | `character(len=18)` | 75 |  |
| `cad` | `character(len=18)` | 76 |  |
| `mgd` | `character(len=18)` | 77 |  |
| `nad` | `character(len=18)` | 78 |  |
| `kd` | `character(len=18)` | 79 |  |
| `cld` | `character(len=18)` | 80 |  |
| `co3d` | `character(len=18)` | 81 |  |
| `hco3d` | `character(len=18)` | 82 |  |
| `so4m` | `character(len=18)` | 83 |  |
| `cam` | `character(len=18)` | 84 |  |
| `mgm` | `character(len=18)` | 85 |  |
| `nam` | `character(len=18)` | 86 |  |
| `km` | `character(len=18)` | 87 |  |
| `clm` | `character(len=18)` | 88 |  |
| `co3m` | `character(len=18)` | 89 |  |
| `hco3m` | `character(len=18)` | 90 |  |
| `so4c` | `character(len=18)` | 91 |  |
| `cac` | `character(len=18)` | 92 |  |
| `mgc` | `character(len=18)` | 93 |  |
| `nac` | `character(len=18)` | 94 |  |
| `kc` | `character(len=18)` | 95 |  |
| `clc` | `character(len=18)` | 96 |  |
| `co3c` | `character(len=18)` | 97 |  |
| `hco3c` | `character(len=18)` | 98 |  |
| `dssl` | `character(len=18)` | 99 |  |

## Variables Defined
### testing_aquifer

- **Type**: `real`
- **Defined in source**: `salt_aquifer.f90:5`

### asaltb_d

- **Type**: `object_salt_balance_aqu`
- **Defined in source**: `salt_aquifer.f90:23`

### asaltb_m

- **Type**: `object_salt_balance_aqu`
- **Defined in source**: `salt_aquifer.f90:24`

### asaltb_y

- **Type**: `object_salt_balance_aqu`
- **Defined in source**: `salt_aquifer.f90:25`

### asaltb_a

- **Type**: `object_salt_balance_aqu`
- **Defined in source**: `salt_aquifer.f90:26`

### basalt_d

- **Type**: `object_salt_balance_aqu`
- **Defined in source**: `salt_aquifer.f90:29`

### basalt_m

- **Type**: `object_salt_balance_aqu`
- **Defined in source**: `salt_aquifer.f90:30`

### basalt_y

- **Type**: `object_salt_balance_aqu`
- **Defined in source**: `salt_aquifer.f90:31`

### basalt_a

- **Type**: `object_salt_balance_aqu`
- **Defined in source**: `salt_aquifer.f90:32`

### saltbz_aqu

- **Type**: `object_salt_balance_aqu`
- **Defined in source**: `salt_aquifer.f90:33`

### salt_hdr_aqu

- **Type**: `output_salt_header`
- **Defined in source**: `salt_aquifer.f90:101`

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
