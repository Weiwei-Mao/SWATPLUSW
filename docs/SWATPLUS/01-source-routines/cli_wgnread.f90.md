---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: cli_wgnread.f90
note_file: cli_wgnread.f90
subroutine: cli_wgnread
module:
  - input_file_module
  - time_module
  - maximum_data_module
  - climate_module
calls:
  - gcycl
  - cli_initwgn
reads:
  - in_cli%weat_wgn
writes: []
purpose: ""
---

# cli_wgnread

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `cli_wgnread.f90`
- **Modules used**: [[input_file_module.f90]], [[time_module.f90]], [[maximum_data_module.f90]], [[climate_module.f90]]
- **Subroutine calls**: 2 | **Files read**: 1 | **Files written**: 0

## Call Relationships
**This routine calls:**

- [[gcycl.f90]]
- [[cli_initwgn.f90]]

**Called by** (live Dataview back-query):

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## File I/O
- **Reads**: `in_cli%weat_wgn` _(variable; see file.cio)_

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
