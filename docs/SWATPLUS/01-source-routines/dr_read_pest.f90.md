---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: dr_read_pest.f90
note_file: dr_read_pest.f90
subroutine: dr_read_pest
module:
  - hydrograph_module
  - dr_module
  - input_file_module
  - organic_mineral_mass_module
  - constituent_mass_module
  - maximum_data_module
calls: []
reads:
  - in_delr%pest
writes: []
purpose: ""
---

# dr_read_pest

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `dr_read_pest.f90`
- **Modules used**: [[hydrograph_module.f90]], [[dr_module.f90]], [[input_file_module.f90]], [[organic_mineral_mass_module.f90]], [[constituent_mass_module.f90]], [[maximum_data_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 1 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by** (live Dataview back-query):

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## File I/O
- **Reads**: `in_delr%pest` _(variable; see file.cio)_

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
