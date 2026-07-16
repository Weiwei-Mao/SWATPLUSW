---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: aqu_read_init_cs.f90
note_file: aqu_read_init_cs.f90
subroutine: aqu_read_init_cs
module:
  - basin_module
  - input_file_module
  - maximum_data_module
  - aquifer_module
  - aqu_pesticide_module
  - hydrograph_module
  - constituent_mass_module
calls: []
reads:
  - initial.aqu_cs
writes: []
purpose: ""
---

# aqu_read_init_cs

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `aqu_read_init_cs.f90`
- **Modules used**: [[basin_module.f90]], [[input_file_module.f90]], [[maximum_data_module.f90]], [[aquifer_module.f90]], [[aqu_pesticide_module.f90]], [[hydrograph_module.f90]], [[constituent_mass_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 1 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by** (live Dataview back-query):

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## File I/O
- **Reads**: `initial.aqu_cs`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
