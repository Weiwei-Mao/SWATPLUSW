---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: dr_ru.f90
note_file: dr_ru.f90
subroutine: dr_ru
module:
  - hydrograph_module
  - hru_lte_module
  - ru_module
  - hru_module
calls: []
uses_variables:
  - hru_lte_module.f90#hlt_db
  - hru_module.f90#ihru
  - hru_module.f90#tconc
  - hydrograph_module.f90#dr
  - hydrograph_module.f90#hz
  - hydrograph_module.f90#ru_def
  - hydrograph_module.f90#ru_elem
  - hydrograph_module.f90#sp_ob
  - ru_module.f90#iru
  - ru_module.f90#ru
  - ru_module.f90#ru_tc
input_variables: []
reads: []
writes: []
purpose: ""
---

# dr_ru

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `dr_ru.f90`
- **Modules used**:
  - [[hydrograph_module.f90]]
  - [[hru_lte_module.f90]]
  - [[ru_module.f90]]
  - [[hru_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 0 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by:**

- [[main.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[hru_lte_module.f90#hlt_db]] - `swatdeg_hru_data`
- [[hru_module.f90#ihru]] - `integer`
- [[hru_module.f90#tconc]] - `real, dimension (:), allocatable`
- [[hydrograph_module.f90#dr]] - `hyd_output`
- [[hydrograph_module.f90#hz]] - `hyd_output`
- [[hydrograph_module.f90#ru_def]] - `routing_unit_data`
- [[hydrograph_module.f90#ru_elem]] - `routing_unit_elements`
- [[hydrograph_module.f90#sp_ob]] - `spatial_objects`
- [[ru_module.f90#iru]] - `integer`
- [[ru_module.f90#ru]] - `ru_parameters`
- [[ru_module.f90#ru_tc]] - `real, dimension (:), allocatable`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
