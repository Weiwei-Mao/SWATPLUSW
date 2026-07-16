---
type: module
tags:
  - swat/module
  - swat/to-read
file: tillage_data_module.f90
note_file: tillage_data_module.f90
module_name: tillage_data_module
defines_types:
  - tillage_db
defines_vars:
  - bmix_idtill
  - till_eff_days
  - bmix_eff
  - bmix_depth
  - dtill
  - bmix_a
  - bmix_b
  - bmix_c
  - tillmix_a
  - tillmix_b
  - tillmix_c
  - bio_consf
  - till_consf
  - tilldb
defines_subroutines: []
defines_functions: []
defines_procedures: []
purpose: ""
---

# tillage_data_module

> [!info] Module
> Defines derived types and module-level variables.

## Defined Types
### tillage_db

- **Defined in source**: `tillage_data_module.f90:19`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `tillnm` | `character(len=16)` | 20 |  |
| `effmix` | `real` | 21 | none \|mixing efficiency of tillage operation |
| `deptil` | `real` | 22 | mm \|depth of mixing caused by tillage |
| `ranrns` | `real` | 23 | mm \|random roughness |
| `ridge_ht` | `real` | 24 | mm \|ridge height |
| `ridge_sp` | `real` | 25 | mm \|ridge interval (or row spacing) |

## Variables Defined
### bmix_idtill

- **Type**: `integer`
- **Defined in source**: `tillage_data_module.f90:5`
- **Source note**: |none          |the tilldb index of the biomix tillage.

### till_eff_days

- **Type**: `integer`
- **Defined in source**: `tillage_data_module.f90:6`
- **Source note**: |none          |length of days a tillage operation will have an effect

### bmix_eff

- **Type**: `real`
- **Defined in source**: `tillage_data_module.f90:7`
- **Source note**: |none          |biological mixing efficieny

### bmix_depth

- **Type**: `real`
- **Defined in source**: `tillage_data_module.f90:8`
- **Source note**: |mm            |maximum potential biological mixing depth

### dtill

- **Type**: `real`
- **Defined in source**: `tillage_data_module.f90:9`
- **Source note**: |mm            |actual biological or tillage mixing  mixing depth

### bmix_a

- **Type**: `real`
- **Defined in source**: `tillage_data_module.f90:10`
- **Source note**: |none          !Base intercept in zz equation in mgt_tillfactor.f90 for biomixing

### bmix_b

- **Type**: `real`
- **Defined in source**: `tillage_data_module.f90:11`
- **Source note**: |none          !slope of in zz equation in mgt_tillfactor.f90 for biomixing

### bmix_c

- **Type**: `real`
- **Defined in source**: `tillage_data_module.f90:12`
- **Source note**: |none          !exponent multiplier in zz equation in mgt_tillfactor.f90 for biomixing

### tillmix_a

- **Type**: `real`
- **Defined in source**: `tillage_data_module.f90:13`
- **Source note**: |none          !Base intercept in zz equation in mgt_tillfactor.f90 for tillage mixing

### tillmix_b

- **Type**: `real`
- **Defined in source**: `tillage_data_module.f90:14`
- **Source note**: |none          !slope of in zz equation in mgt_tillfactor.f90 for tillage mixing

### tillmix_c

- **Type**: `real`
- **Defined in source**: `tillage_data_module.f90:15`
- **Source note**: |none          !exponent multiplier in zz equation in mgt_tillfactor.f90 for tillage mixing

### bio_consf

- **Type**: `real`
- **Defined in source**: `tillage_data_module.f90:16`

### till_consf

- **Type**: `real`
- **Defined in source**: `tillage_data_module.f90:17`

### tilldb

- **Type**: `tillage_db`
- **Defined in source**: `tillage_data_module.f90:27`

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
