---
type: module
tags:
  - swat/module
  - swat/to-read
file: water_body_module.f90
note_file: water_body_module.f90
module_name: water_body_module
defines_types:
  - water_body
defines_vars:
  - wbodz
  - res_wat_d
  - res_wat_m
  - res_wat_y
  - res_wat_a
  - wet_wat_d
  - wet_wat_m
  - wet_wat_y
  - wet_wat_a
  - ch_wat_d
  - ch_wat_m
  - ch_wat_y
  - ch_wat_a
  - bch_wat_d
  - bch_wat_m
  - bch_wat_y
  - bch_wat_a
  - bres_wat_d
  - bres_wat_m
  - bres_wat_y
  - bres_wat_a
  - wbody_wb
defines_subroutines: []
defines_functions:
  - watbod_add
  - watbod_div
  - watbod_ave
defines_procedures:
  - watbod_add
  - watbod_div
  - watbod_ave
purpose: ""
---

# water_body_module

> [!info] Module
> Defines derived types and module-level variables.

## Defined Types
### water_body

- **Defined in source**: `water_body_module.f90:7`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `area_ha` | `real` | 8 | ha \|water body surface area |
| `precip` | `real` | 9 | m3 \|precip on the water body |
| `evap` | `real` | 10 | m3 \|evaporation from the water surface |
| `seep` | `real` | 11 | m3 \|seepage from bottom of water body |

## Variables Defined
### wbodz

- **Type**: `water_body`
- **Defined in source**: `water_body_module.f90:19`

### res_wat_d

- **Type**: `water_body`
- **Defined in source**: `water_body_module.f90:21`

### res_wat_m

- **Type**: `water_body`
- **Defined in source**: `water_body_module.f90:22`

### res_wat_y

- **Type**: `water_body`
- **Defined in source**: `water_body_module.f90:23`

### res_wat_a

- **Type**: `water_body`
- **Defined in source**: `water_body_module.f90:24`

### wet_wat_d

- **Type**: `water_body`
- **Defined in source**: `water_body_module.f90:25`

### wet_wat_m

- **Type**: `water_body`
- **Defined in source**: `water_body_module.f90:26`

### wet_wat_y

- **Type**: `water_body`
- **Defined in source**: `water_body_module.f90:27`

### wet_wat_a

- **Type**: `water_body`
- **Defined in source**: `water_body_module.f90:28`

### ch_wat_d

- **Type**: `water_body`
- **Defined in source**: `water_body_module.f90:29`

### ch_wat_m

- **Type**: `water_body`
- **Defined in source**: `water_body_module.f90:30`

### ch_wat_y

- **Type**: `water_body`
- **Defined in source**: `water_body_module.f90:31`

### ch_wat_a

- **Type**: `water_body`
- **Defined in source**: `water_body_module.f90:32`

### bch_wat_d

- **Type**: `water_body`
- **Defined in source**: `water_body_module.f90:33`

### bch_wat_m

- **Type**: `water_body`
- **Defined in source**: `water_body_module.f90:34`

### bch_wat_y

- **Type**: `water_body`
- **Defined in source**: `water_body_module.f90:35`

### bch_wat_a

- **Type**: `water_body`
- **Defined in source**: `water_body_module.f90:36`

### bres_wat_d

- **Type**: `water_body`
- **Defined in source**: `water_body_module.f90:37`

### bres_wat_m

- **Type**: `water_body`
- **Defined in source**: `water_body_module.f90:38`

### bres_wat_y

- **Type**: `water_body`
- **Defined in source**: `water_body_module.f90:39`

### bres_wat_a

- **Type**: `water_body`
- **Defined in source**: `water_body_module.f90:40`

### wbody_wb

- **Type**: `water_body`
- **Defined in source**: `water_body_module.f90:41`
- **Source note**: used for reservoir and wetlands

## Subroutines Defined
(No subroutines detected.)

## Functions Defined
### watbod_add

### watbod_div

### watbod_ave

## Used By Source Routines

```dataview
LIST file.link
WHERE type = "source" AND contains(module, this.module_name)
```

<!-- USER-NOTES-START -->
## Notes
Use this section for type and variable meanings, units, and allowed values. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
