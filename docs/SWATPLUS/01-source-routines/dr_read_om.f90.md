---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: dr_read_om.f90
note_file: dr_read_om.f90
subroutine: dr_read_om
module:
  - dr_module
  - constituent_mass_module
  - hydrograph_module
  - input_file_module
  - organic_mineral_mass_module
  - maximum_data_module
calls: []
reads:
  - in_delr%om
writes: []
purpose: ""
---

# dr_read_om

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `dr_read_om.f90`
- **Modules used**: [[dr_module.f90]], [[constituent_mass_module.f90]], [[hydrograph_module.f90]], [[input_file_module.f90]], [[organic_mineral_mass_module.f90]], [[maximum_data_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 1 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by** (live Dataview back-query):

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## File I/O
- **Reads**: `in_delr%om` _(variable; see file.cio)_

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
