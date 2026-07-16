---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: shade_factor_read.f90
note_file: shade_factor_read.f90
subroutine: shade_factor_read
module:
  - input_file_module
  - maximum_data_module
  - sd_channel_module
  - hydrograph_module
calls: []
uses_variables:
  - hydrograph_module.f90#shf_db
  - input_file_module.f90#in_shf
  - maximum_data_module.f90#db_mx
input_variables:
  - hydrograph_module.f90#shf_db
reads:
  - in_shf%ssff_shf
writes: []
purpose: ""
---

# shade_factor_read

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `shade_factor_read.f90`
- **Modules used**:
  - [[input_file_module.f90]]
  - [[maximum_data_module.f90]]
  - [[sd_channel_module.f90]]
  - [[hydrograph_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 1 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by:**

- [[proc_read.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[hydrograph_module.f90#shf_db]] - `shade_factor_data`
- [[input_file_module.f90#in_shf]] - `shade_factor`
- [[maximum_data_module.f90#db_mx]] - `data_files_max_elements`

**Populated by file reads:**

- [[hydrograph_module.f90#shf_db]]

## File I/O
- **Reads**:
  - [[shade_factor.shf]]

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
