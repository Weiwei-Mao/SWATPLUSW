---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: wet_read_hyd.f90
note_file: wet_read_hyd.f90
subroutine: wet_read_hyd
module:
  - basin_module
  - input_file_module
  - maximum_data_module
  - reservoir_data_module
  - output_landscape_module
  - gwflow_module
calls: []
reads:
  - in_res%hyd_wet
  - gwflow.wetland
writes: []
purpose: ""
---

# wet_read_hyd

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `wet_read_hyd.f90`
- **Modules used**: [[basin_module.f90]], [[input_file_module.f90]], [[maximum_data_module.f90]], [[reservoir_data_module.f90]], [[output_landscape_module.f90]], [[gwflow_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 2 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by** (live Dataview back-query):

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## File I/O
- **Reads**: `in_res%hyd_wet` _(variable; see file.cio)_, `gwflow.wetland`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
