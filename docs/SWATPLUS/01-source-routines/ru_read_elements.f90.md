---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: ru_read_elements.f90
note_file: ru_read_elements.f90
subroutine: ru_read_elements
module:
  - hydrograph_module
  - input_file_module
  - maximum_data_module
  - dr_module
calls:
  - define_unit_elements
uses_variables:
  - dr_module.f90#dr_db
  - dr_module.f90#dr_om_num
  - hydrograph_module.f90#defunit_num
  - hydrograph_module.f90#dr
  - hydrograph_module.f90#elem_cnt
  - hydrograph_module.f90#exco
  - hydrograph_module.f90#ielem_ru
  - hydrograph_module.f90#ob
  - hydrograph_module.f90#res
  - hydrograph_module.f90#ru_def
  - hydrograph_module.f90#ru_elem
  - hydrograph_module.f90#sp_ob
  - hydrograph_module.f90#sp_ob1
  - input_file_module.f90#in_ru
  - maximum_data_module.f90#db_mx
input_variables:
  - hydrograph_module.f90#ru_def
  - hydrograph_module.f90#ru_elem
reads:
  - in_ru%ru_ele
  - in_ru%ru_def
writes: []
purpose: ""
---

# ru_read_elements

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `ru_read_elements.f90`
- **Modules used**:
  - [[hydrograph_module.f90]]
  - [[input_file_module.f90]]
  - [[maximum_data_module.f90]]
  - [[dr_module.f90]]
- **Subroutine calls**: 1 | **Files read**: 2 | **Files written**: 0

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
- [[dr_module.f90#dr_db]] - `delivery_ratio_datafiles`
- [[dr_module.f90#dr_om_num]] - `integer, dimension(:), allocatable`
- [[hydrograph_module.f90#defunit_num]] - `integer, dimension (:), allocatable`
- [[hydrograph_module.f90#dr]] - `hyd_output`
- [[hydrograph_module.f90#elem_cnt]] - `integer, dimension (:), allocatable`
- [[hydrograph_module.f90#exco]] - `hyd_output`
- [[hydrograph_module.f90#ielem_ru]] - `integer, dimension(:), allocatable`
- [[hydrograph_module.f90#ob]] - `object_connectivity`
- [[hydrograph_module.f90#res]] - `hyd_output`
- [[hydrograph_module.f90#ru_def]] - `routing_unit_data`
- [[hydrograph_module.f90#ru_elem]] - `routing_unit_elements`
- [[hydrograph_module.f90#sp_ob]] - `spatial_objects`
- [[hydrograph_module.f90#sp_ob1]] - `spatial_objects`
- [[input_file_module.f90#in_ru]] - `input_ru`
- [[maximum_data_module.f90#db_mx]] - `data_files_max_elements`

**Populated by file reads:**

- [[hydrograph_module.f90#ru_def]]
- [[hydrograph_module.f90#ru_elem]]

## File I/O
- **Reads**:
  - [[rout_unit.ele]]
  - [[rout_unit.def]]

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
