---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: plant_all_init.f90
note_file: plant_all_init.f90
subroutine: plant_all_init
module:
  - plant_module
  - plant_data_module
  - hru_module
  - hydrograph_module
  - maximum_data_module
calls:
  - plant_init
uses_variables:
  - hru_module.f90#hru
  - hru_module.f90#ilu
  - hru_module.f90#ipl
  - hru_module.f90#isol
  - hydrograph_module.f90#sp_ob
  - maximum_data_module.f90#db_mx
  - plant_data_module.f90#plts_bsn
  - plant_module.f90#basin_plants
  - plant_module.f90#bsn_crop_yld
  - plant_module.f90#bsn_crop_yld_aa
  - plant_module.f90#bsn_crop_yld_z
  - plant_module.f90#pcom
input_variables: []
reads: []
writes: []
purpose: ""
---

# plant_all_init

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `plant_all_init.f90`
- **Modules used**:
  - [[plant_module.f90]]
  - [[plant_data_module.f90]]
  - [[hru_module.f90]]
  - [[hydrograph_module.f90]]
  - [[maximum_data_module.f90]]
- **Subroutine calls**: 1 | **Files read**: 0 | **Files written**: 0

## Call Relationships
**This routine calls:**

- [[plant_init.f90]]

**Called by:**

- [[proc_hru.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[hru_module.f90#hru]] - `hydrologic_response_unit`
- [[hru_module.f90#ilu]] - `integer`
- [[hru_module.f90#ipl]] - `integer`
- [[hru_module.f90#isol]] - `integer`
- [[hydrograph_module.f90#sp_ob]] - `spatial_objects`
- [[maximum_data_module.f90#db_mx]] - `data_files_max_elements`
- [[plant_data_module.f90#plts_bsn]] - `character(len=40), dimension (:), allocatable`
- [[plant_module.f90#basin_plants]] - `integer`
- [[plant_module.f90#bsn_crop_yld]] - `basin_crop_yields`
- [[plant_module.f90#bsn_crop_yld_aa]] - `basin_crop_yields`
- [[plant_module.f90#bsn_crop_yld_z]] - `basin_crop_yields`
- [[plant_module.f90#pcom]] - `plant_community`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
