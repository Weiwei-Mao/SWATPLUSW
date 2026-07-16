---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: co2_read.f90
note_file: co2_read.f90
subroutine: co2_read
module:
  - input_file_module
  - basin_module
  - time_module
  - climate_module
  - output_path_module
calls:
  - open_output_file
reads:
  - co2_yr.dat
writes: []
purpose: ""
---

# co2_read

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `co2_read.f90`
- **Modules used**: [[input_file_module.f90]], [[basin_module.f90]], [[time_module.f90]], [[climate_module.f90]], [[output_path_module.f90]]
- **Subroutine calls**: 1 | **Files read**: 1 | **Files written**: 0

## Call Relationships
**This routine calls:**

- `open_output_file`

**Called by** (live Dataview back-query):

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## File I/O
- **Reads**: `co2_yr.dat`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
