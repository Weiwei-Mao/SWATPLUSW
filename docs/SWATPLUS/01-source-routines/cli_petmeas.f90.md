---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: cli_petmeas.f90
note_file: cli_petmeas.f90
subroutine: cli_petmeas
module:
  - climate_module
  - input_file_module
  - time_module
  - maximum_data_module
calls: []
reads:
  - in_cli%pet_cli
  - petm(i
  - TRIM(ADJUSTL(in_path_pet%peti
writes: []
purpose: ""
---

# cli_petmeas

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `cli_petmeas.f90`
- **Modules used**: [[climate_module.f90]], [[input_file_module.f90]], [[time_module.f90]], [[maximum_data_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 3 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by** (live Dataview back-query):

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## File I/O
- **Reads**: `in_cli%pet_cli` _(variable; see file.cio)_, `petm(i` _(variable; see file.cio)_, `TRIM(ADJUSTL(in_path_pet%peti` _(variable; see file.cio)_

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
