---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: cs_fert_read.f90
note_file: cs_fert_read.f90
subroutine: cs_fert_read
module:
  - constituent_mass_module
  - input_file_module
  - maximum_data_module
  - cs_module
calls: []
reads:
  - fertilizer.frt_cs
writes: []
purpose: "this subroutine reads constituent fertilizer loading (kg/ha) for various fertilizer types"
---

# cs_fert_read

> [!info] Summary
> this subroutine reads constituent fertilizer loading (kg/ha) for various fertilizer types

## Basic Information
- **Type**: `subroutine`
- **Source file**: `cs_fert_read.f90`
- **Modules used**: [[constituent_mass_module.f90]], [[input_file_module.f90]], [[maximum_data_module.f90]], [[cs_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 1 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by** (live Dataview back-query):

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## File I/O
- **Reads**: `fertilizer.frt_cs`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
