---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: carbon_bsn_read.f90
note_file: carbon_bsn_read.f90
subroutine: carbon_bsn_read
module:
  - carbon_module
  - basin_module
  - tillage_data_module
  - plant_data_module
  - input_file_module
calls: []
reads:
  - in_basin%carbon_bsn
  - carbon_lyr
writes: []
purpose: ""
---

# carbon_bsn_read

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `carbon_bsn_read.f90`
- **Modules used**: [[carbon_module.f90]], [[basin_module.f90]], [[tillage_data_module.f90]], [[plant_data_module.f90]], [[input_file_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 2 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by** (live Dataview back-query):

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## File I/O
- **Reads**: `in_basin%carbon_bsn` _(variable; see file.cio)_, `carbon_lyr` _(variable; see file.cio)_

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
