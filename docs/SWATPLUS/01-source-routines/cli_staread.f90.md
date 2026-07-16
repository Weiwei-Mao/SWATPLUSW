---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: cli_staread.f90
note_file: cli_staread.f90
subroutine: cli_staread
module:
  - input_file_module
  - maximum_data_module
  - climate_module
  - time_module
  - hydrograph_module
calls:
  - search
reads:
  - in_cli%weat_sta
writes: []
purpose: ""
---

# cli_staread

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `cli_staread.f90`
- **Modules used**: [[input_file_module.f90]], [[maximum_data_module.f90]], [[climate_module.f90]], [[time_module.f90]], [[hydrograph_module.f90]]
- **Subroutine calls**: 1 | **Files read**: 1 | **Files written**: 0

## Call Relationships
**This routine calls:**

- [[search.f90]]

**Called by** (live Dataview back-query):

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## File I/O
- **Reads**: `in_cli%weat_sta` _(variable; see file.cio)_

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
