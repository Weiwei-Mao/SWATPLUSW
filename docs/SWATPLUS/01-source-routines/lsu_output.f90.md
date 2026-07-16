---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: lsu_output.f90
note_file: lsu_output.f90
subroutine: lsu_output
module:
  - time_module
  - basin_module
  - maximum_data_module
  - calibration_data_module
  - hydrograph_module
  - output_landscape_module
calls: []
reads: []
writes: []
purpose: ""
---

# lsu_output

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `lsu_output.f90`
- **Modules used**: [[time_module.f90]], [[basin_module.f90]], [[maximum_data_module.f90]], [[calibration_data_module.f90]], [[hydrograph_module.f90]], [[output_landscape_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 0 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by** (live Dataview back-query):

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
