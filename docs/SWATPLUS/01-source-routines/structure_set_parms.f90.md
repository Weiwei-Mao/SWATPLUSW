---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: structure_set_parms.f90
note_file: structure_set_parms.f90
subroutine: structure_set_parms
module:
  - mgt_operations_module
  - hru_module
  - soil_module
calls:
  - ttcoef_wway
uses_variables:
  - hru_module.f90#hru
  - hru_module.f90#iseptic
  - hru_module.f90#sdr
  - hru_module.f90#t_ov
  - hru_module.f90#tc_gwat
  - mgt_operations_module.f90#bmpuser_db
  - mgt_operations_module.f90#filtstrip_db
  - mgt_operations_module.f90#grwaterway_db
  - soil_module.f90#soil
input_variables: []
reads: []
writes: []
purpose: "this subroutine controls the simulation of the land phase of the; hydrologic cycle"
---

# structure_set_parms

> [!info] Summary
> this subroutine controls the simulation of the land phase of the; hydrologic cycle

## Basic Information
- **Type**: `subroutine`
- **Source file**: `structure_set_parms.f90`
- **Modules used**:
  - [[mgt_operations_module.f90]]
  - [[hru_module.f90]]
  - [[soil_module.f90]]
- **Subroutine calls**: 1 | **Files read**: 0 | **Files written**: 0

## Call Relationships
**This routine calls:**

- [[ttcoef_wway.f90]]

**Called by:**

- [[actions.f90]]
- [[proc_hru.f90]]
- [[structure_init.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[hru_module.f90#hru]] - `hydrologic_response_unit`
- [[hru_module.f90#iseptic]] - `integer, dimension (:), allocatable`
- [[hru_module.f90#sdr]] - `subsurface_drainage_parameters`
- [[hru_module.f90#t_ov]] - `real, dimension (:), allocatable`
- [[hru_module.f90#tc_gwat]] - `real, dimension (:), allocatable`
- [[mgt_operations_module.f90#bmpuser_db]] - `bmpuser_operation`
- [[mgt_operations_module.f90#filtstrip_db]] - `filtstrip_operation`
- [[mgt_operations_module.f90#grwaterway_db]] - `grwaterway_operation`
- [[soil_module.f90#soil]] - `soil_profile`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
