---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: aqu2d_read.f90
note_file: aqu2d_read.f90
subroutine: aqu2d_read
module:
  - hydrograph_module
  - input_file_module
  - maximum_data_module
calls:
  - define_unit_elements
uses_variables:
  - hydrograph_module.f90#aq_ch
  - hydrograph_module.f90#aqu
  - hydrograph_module.f90#aqu_cha
  - hydrograph_module.f90#defunit_num
  - hydrograph_module.f90#elem_cnt
  - hydrograph_module.f90#sp_ob
  - input_file_module.f90#in_link
  - maximum_data_module.f90#db_mx
input_variables:
  - hydrograph_module.f90#aq_ch
reads:
  - in_link%aqu_cha
writes: []
purpose: ""
---

# aqu2d_read

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `aqu2d_read.f90`
- **Modules used**:
  - [[hydrograph_module.f90]]
  - [[input_file_module.f90]]
  - [[maximum_data_module.f90]]
- **Subroutine calls**: 1 | **Files read**: 1 | **Files written**: 0

## Call Relationships
**This routine calls:**

- [[define_unit_elements.f90]]

**Called by:**

- [[hyd_connect.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[hydrograph_module.f90#aq_ch]] - `channel_aquifer_elements`
- [[hydrograph_module.f90#aqu]] - `hyd_output`
- [[hydrograph_module.f90#aqu_cha]] - `geomorphic_baseflow_channel_data`
- [[hydrograph_module.f90#defunit_num]] - `integer, dimension (:), allocatable`
- [[hydrograph_module.f90#elem_cnt]] - `integer, dimension (:), allocatable`
- [[hydrograph_module.f90#sp_ob]] - `spatial_objects`
- [[input_file_module.f90#in_link]] - `input_link`
- [[maximum_data_module.f90#db_mx]] - `data_files_max_elements`

**Populated by file reads:**

- [[hydrograph_module.f90#aq_ch]]

## File I/O
- **Reads**:
  - [[aqu_cha.lin]]

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
