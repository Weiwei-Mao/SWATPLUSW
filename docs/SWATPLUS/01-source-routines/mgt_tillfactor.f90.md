---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: mgt_tillfactor.f90
note_file: mgt_tillfactor.f90
subroutine: mgt_tillfactor
module:
  - soil_module
  - basin_module
  - hru_module
  - tillage_data_module
  - utils
calls: []
uses_variables:
  - hru_module.f90#tillage_days
  - hru_module.f90#tillage_depth
  - hru_module.f90#tillage_switch
  - soil_module.f90#soil
  - tillage_data_module.f90#bmix_a
  - tillage_data_module.f90#bmix_b
  - tillage_data_module.f90#bmix_c
  - tillage_data_module.f90#till_consf
  - tillage_data_module.f90#tillmix_a
  - tillage_data_module.f90#tillmix_b
  - tillage_data_module.f90#tillmix_c
input_variables: []
reads: []
writes: []
purpose: ""
---

# mgt_tillfactor

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `mgt_tillfactor.f90`
- **Modules used**:
  - [[soil_module.f90]]
  - [[basin_module.f90]]
  - [[hru_module.f90]]
  - [[tillage_data_module.f90]]
  - [[utils.f90]]
- **Subroutine calls**: 0 | **Files read**: 0 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by:**

- [[mgt_biomix.f90]]
- [[mgt_newtillmix_cswat1.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[hru_module.f90#tillage_days]] - `integer, dimension(:), allocatable`
- [[hru_module.f90#tillage_depth]] - `real, dimension(:), allocatable`
- [[hru_module.f90#tillage_switch]] - `integer, dimension(:), allocatable`
- [[soil_module.f90#soil]] - `soil_profile`
- [[tillage_data_module.f90#bmix_a]] - `real`
- [[tillage_data_module.f90#bmix_b]] - `real`
- [[tillage_data_module.f90#bmix_c]] - `real`
- [[tillage_data_module.f90#till_consf]] - `real`
- [[tillage_data_module.f90#tillmix_a]] - `real`
- [[tillage_data_module.f90#tillmix_b]] - `real`
- [[tillage_data_module.f90#tillmix_c]] - `real`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
