---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: cli_tmeas.f90
note_file: cli_tmeas.f90
subroutine: cli_tmeas
module:
  - input_file_module
  - climate_module
  - maximum_data_module
  - time_module
calls:
  - xmon
reads:
  - in_cli%tmp_cli
  - tmp(i
  - TRIM(ADJUSTL(in_path_tmp%tmp
writes: []
purpose: ""
---

# cli_tmeas

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `cli_tmeas.f90`
- **Modules used**: [[input_file_module.f90]], [[climate_module.f90]], [[maximum_data_module.f90]], [[time_module.f90]]
- **Subroutine calls**: 1 | **Files read**: 3 | **Files written**: 0

## Call Relationships
**This routine calls:**

- [[xmon.f90]]

**Called by** (live Dataview back-query):

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## File I/O
- **Reads**: `in_cli%tmp_cli` _(variable; see file.cio)_, `tmp(i` _(variable; see file.cio)_, `TRIM(ADJUSTL(in_path_tmp%tmp` _(variable; see file.cio)_

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
