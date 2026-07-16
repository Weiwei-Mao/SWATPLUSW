---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: ru_read_elements.f90
note_file: ru_read_elements.f90
subroutine: ru_read_elements
module:
  - hydrograph_module
  - input_file_module
  - maximum_data_module
  - dr_module
calls:
  - define_unit_elements
reads:
  - in_ru%ru_ele
  - in_ru%ru_def
writes: []
purpose: ""
---

# ru_read_elements

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `ru_read_elements.f90`
- **Modules used**: [[hydrograph_module.f90]], [[input_file_module.f90]], [[maximum_data_module.f90]], [[dr_module.f90]]
- **Subroutine calls**: 1 | **Files read**: 2 | **Files written**: 0

## Call Relationships
**This routine calls:**

- [[define_unit_elements.f90]]

**Called by** (live Dataview back-query):

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## File I/O
- **Reads**: `in_ru%ru_ele` _(variable; see file.cio)_, `in_ru%ru_def` _(variable; see file.cio)_

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
