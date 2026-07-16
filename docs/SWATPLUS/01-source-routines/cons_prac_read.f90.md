---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: cons_prac_read.f90
note_file: cons_prac_read.f90
subroutine: cons_prac_read
module:
  - input_file_module
  - maximum_data_module
  - landuse_data_module
calls: []
reads:
  - in_lum%cons_prac_lum
writes: []
purpose: ""
---

# cons_prac_read

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `cons_prac_read.f90`
- **Modules used**: [[input_file_module.f90]], [[maximum_data_module.f90]], [[landuse_data_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 1 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by** (live Dataview back-query):

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## File I/O
- **Reads**: `in_lum%cons_prac_lum` _(variable; see file.cio)_

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
