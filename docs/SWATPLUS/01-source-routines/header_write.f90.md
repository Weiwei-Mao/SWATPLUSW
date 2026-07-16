---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: header_write.f90
note_file: header_write.f90
subroutine: header_write
module:
  - basin_module
  - aquifer_module
  - channel_module
  - reservoir_module
  - hydrograph_module
  - sd_channel_module
  - maximum_data_module
  - calibration_data_module
  - output_path_module
calls:
  - open_output_file
reads:
  - hydrology-cal.hyd
writes:
  - hru-out.cal
  - hru-new.cal
purpose: ""
---

# header_write

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `header_write.f90`
- **Modules used**: [[basin_module.f90]], [[aquifer_module.f90]], [[channel_module.f90]], [[reservoir_module.f90]], [[hydrograph_module.f90]], [[sd_channel_module.f90]], [[maximum_data_module.f90]], [[calibration_data_module.f90]], [[output_path_module.f90]]
- **Subroutine calls**: 1 | **Files read**: 1 | **Files written**: 2

## Call Relationships
**This routine calls:**

- `open_output_file`

**Called by** (live Dataview back-query):

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## File I/O
- **Writes**: `hru-out.cal`, `hru-new.cal`
- **Reads**: `hydrology-cal.hyd`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
