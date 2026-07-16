---
type: module
tags:
  - swat/module
  - swat/to-read
file: cs_data_module.f90
note_file: cs_data_module.f90
module_name: cs_data_module
defines_types:
  - constituent_rct
defines_vars:
  - cs_rct_soil
  - cs_rct_aqu
  - rct
  - rct_shale
  - num_geol_shale
  - bor_tol_sim
  - bor_stress_a
  - bor_stress_b
defines_subroutines: []
defines_functions: []
defines_procedures: []
purpose: ""
---

# cs_data_module

> [!info] Module
> Defines derived types and module-level variables.

## Defined Types
### constituent_rct

- **Defined in source**: `cs_data_module.f90:7`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `kd_seo4` | `real` | 8 | \| \|sorption partition coefficient for seo4 |
| `kd_seo3` | `real` | 9 | \| \|sorption partition coefficient for seo3 |
| `kd_born` | `real` | 10 | \| \|sorption partition coefficient for boron |
| `kseo4` | `real` | 11 | \|1/day \|first-order rate constant for seo4 reduction to seo3 |
| `kseo3` | `real` | 12 | \|1/day \|first-order rate constant for seo3 reduction to elemental se |
| `se_ino3` | `real` | 13 | \| \|selenium reduction inhibition factor |
| `oxy_soil` | `real` | 14 | \|mg/L \|oxygen concentration in soil water |
| `oxy_aqu` | `real` | 15 | \|mg/L \|oxygen concentration in groundwater |
| `shale` | `real, dimension(:), allocatable` | 16 | \| \|fraction of object area that is occupied by shale formations (source of se) |
| `sseratio` | `real, dimension(:), allocatable` | 17 | \| \|sulfur/se ratio in shale material |
| `ko2a` | `real, dimension(:), allocatable` | 18 | \|1/day \|first-order rate constant for autotrophic reduction of dissolved oxygen |
| `kno3a` | `real, dimension(:), allocatable` | 19 | \|1/day \|first-order rate constant for autotrophic reduction of no3 |

## Variables Defined
### cs_rct_soil

- **Type**: `constituent_rct`
- **Defined in source**: `cs_data_module.f90:23`

### cs_rct_aqu

- **Type**: `constituent_rct`
- **Defined in source**: `cs_data_module.f90:24`

### rct

- **Type**: `real, dimension(:,:), allocatable`
- **Defined in source**: `cs_data_module.f90:27`
- **Source note**: reaction parameters

### rct_shale

- **Type**: `real, dimension(:,:), allocatable`
- **Defined in source**: `cs_data_module.f90:28`
- **Source note**: reaction parameters for shale

### num_geol_shale

- **Type**: `integer`
- **Defined in source**: `cs_data_module.f90:31`

### bor_tol_sim

- **Type**: `integer`
- **Defined in source**: `cs_data_module.f90:34`
- **Source note**: |flag to simulate boron effect on plant growth

### bor_stress_a

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `cs_data_module.f90:35`
- **Source note**: |a and b parameters in boron relative yield equations

### bor_stress_b

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `cs_data_module.f90:36`
- **Source note**: |a and b parameters in boron relative yield equations

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
