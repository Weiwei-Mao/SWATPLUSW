---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: manure_allocation_read.f90
note_file: manure_allocation_read.f90
subroutine: manure_allocation_read
module:
  - input_file_module
  - manure_allocation_module
  - mgt_operations_module
  - maximum_data_module
  - hydrograph_module
  - sd_channel_module
  - conditional_module
  - hru_module
calls: []
uses_variables:
  - conditional_module.f90#dtbl_lum
  - hru_module.f90#hru
  - hru_module.f90#ihru
  - manure_allocation_module.f90#mallo
  - maximum_data_module.f90#db_mx
  - mgt_operations_module.f90#chemapp_db
input_variables:
  - manure_allocation_module.f90#mallo
reads:
  - manure_allo.mnu
writes: []
purpose: ""
---

# manure_allocation_read

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `manure_allocation_read.f90`
- **Modules used**:
  - [[input_file_module.f90]]
  - [[manure_allocation_module.f90]]
  - [[mgt_operations_module.f90]]
  - [[maximum_data_module.f90]]
  - [[hydrograph_module.f90]]
  - [[sd_channel_module.f90]]
  - [[conditional_module.f90]]
  - [[hru_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 1 | **Files written**: 0

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
- [[conditional_module.f90#dtbl_lum]] - `decision_table`
- [[hru_module.f90#hru]] - `hydrologic_response_unit`
- [[hru_module.f90#ihru]] - `integer`
- [[manure_allocation_module.f90#mallo]] - `manure_allocation`
- [[maximum_data_module.f90#db_mx]] - `data_files_max_elements`
- [[mgt_operations_module.f90#chemapp_db]] - `chemical_application_operation`

**Populated by file reads:**

- [[manure_allocation_module.f90#mallo]]

## File I/O
- **Reads**:
  - [[manure_allo.mnu]]

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
