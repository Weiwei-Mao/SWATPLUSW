---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: define_unit_elements.f90
note_file: define_unit_elements.f90
subroutine: define_unit_elements
module:
  - hydrograph_module
calls: []
uses_variables:
  - hydrograph_module.f90#defunit_num
  - hydrograph_module.f90#elem_cnt
input_variables: []
reads: []
writes: []
purpose: ""
---

# define_unit_elements

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `define_unit_elements.f90`
- **Modules used**:
  - [[hydrograph_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 0 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by:**

- [[aqu2d_read.f90]]
- [[aqu_read_elements.f90]]
- [[cal_parmchg_read.f90]]
- [[ch_read_elements.f90]]
- [[lsu_read_elements.f90]]
- [[pl_read_parms_cal.f90]]
- [[pl_read_regions_cal.f90]]
- [[rec_read_elements.f90]]
- [[reg_read_elements.f90]]
- [[res_read_elements.f90]]
- [[ru_read_elements.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[hydrograph_module.f90#defunit_num]] - `integer, dimension (:), allocatable`
- [[hydrograph_module.f90#elem_cnt]] - `integer, dimension (:), allocatable`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
