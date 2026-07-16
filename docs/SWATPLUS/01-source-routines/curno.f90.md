---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: curno.f90
note_file: curno.f90
subroutine: curno
module:
  - time_module
  - hru_module
  - soil_module
calls:
  - ascrv
uses_variables:
  - hru_module.f90#cn2
  - hru_module.f90#hru
  - hru_module.f90#smx
  - hru_module.f90#wrt
  - soil_module.f90#soil
input_variables: []
reads: []
writes: []
purpose: "this subroutine determines the curve numbers for moisture conditions; I and III and calculates coefficients and shape parameters for the; water retention curve"
---

# curno

> [!info] Summary
> this subroutine determines the curve numbers for moisture conditions; I and III and calculates coefficients and shape parameters for the; water retention curve

## Basic Information
- **Type**: `subroutine`
- **Source file**: `curno.f90`
- **Modules used**:
  - [[time_module.f90]]
  - [[hru_module.f90]]
  - [[soil_module.f90]]
- **Subroutine calls**: 1 | **Files read**: 0 | **Files written**: 0

## Call Relationships
**This routine calls:**

- [[ascrv.f90]]

**Called by:**

- [[actions.f90]]
- [[cal_parm_select.f90]]
- [[calsoft_hyd.f90]]
- [[calsoft_hyd_bfr_surq.f90]]
- [[cn2_init.f90]]
- [[mgt_sched.f90]]
- [[pl_burnop.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[hru_module.f90#cn2]] - `real, dimension (:), allocatable`
- [[hru_module.f90#hru]] - `hydrologic_response_unit`
- [[hru_module.f90#smx]] - `real, dimension (:), allocatable`
- [[hru_module.f90#wrt]] - `real, dimension (:,:), allocatable`
- [[soil_module.f90#soil]] - `soil_profile`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
