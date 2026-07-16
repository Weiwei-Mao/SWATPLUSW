---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: ru_read.f90
note_file: ru_read.f90
subroutine: ru_read
module:
  - basin_module
  - input_file_module
  - time_module
  - ru_module
  - hydrograph_module
  - maximum_data_module
  - topography_data_module
  - constituent_mass_module
  - salt_module
  - cs_module
calls: []
reads:
  - in_ru%ru
writes: []
purpose: ""
---

# ru_read

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `ru_read.f90`
- **Modules used**: [[basin_module.f90]], [[input_file_module.f90]], [[time_module.f90]], [[ru_module.f90]], [[hydrograph_module.f90]], [[maximum_data_module.f90]], [[topography_data_module.f90]], [[constituent_mass_module.f90]], [[salt_module.f90]], [[cs_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 1 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by** (live Dataview back-query):

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## File I/O
- **Reads**: `in_ru%ru` _(variable; see file.cio)_

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
