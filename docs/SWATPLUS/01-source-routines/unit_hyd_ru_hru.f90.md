---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: unit_hyd_ru_hru.f90
note_file: unit_hyd_ru_hru.f90
subroutine: unit_hyd_ru_hru
module:
  - hru_module
  - ru_module
  - hydrograph_module
  - time_module
calls:
  - unit_hyd
uses_variables:
  - hru_module.f90#hru
  - hru_module.f90#tconc
  - hydrograph_module.f90#ob
  - hydrograph_module.f90#sp_ob
  - hydrograph_module.f90#sp_ob1
  - ru_module.f90#ru
  - ru_module.f90#ru_tc
  - time_module.f90#time
input_variables: []
reads: []
writes: []
purpose: ""
---

# unit_hyd_ru_hru

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `unit_hyd_ru_hru.f90`
- **Modules used**:
  - [[hru_module.f90]]
  - [[ru_module.f90]]
  - [[hydrograph_module.f90]]
  - [[time_module.f90]]
- **Subroutine calls**: 1 | **Files read**: 0 | **Files written**: 0

## Call Relationships
**This routine calls:**

- [[unit_hyd.f90]]

**Called by:**

- [[main.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[hru_module.f90#hru]] - `hydrologic_response_unit`
- [[hru_module.f90#tconc]] - `real, dimension (:), allocatable`
- [[hydrograph_module.f90#ob]] - `object_connectivity`
- [[hydrograph_module.f90#sp_ob]] - `spatial_objects`
- [[hydrograph_module.f90#sp_ob1]] - `spatial_objects`
- [[ru_module.f90#ru]] - `ru_parameters`
- [[ru_module.f90#ru_tc]] - `real, dimension (:), allocatable`
- [[time_module.f90#time]] - `time_current`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
