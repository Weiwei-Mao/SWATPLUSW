---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: exco_read_hmet.f90
note_file: exco_read_hmet.f90
subroutine: exco_read_hmet
module:
  - hydrograph_module
  - input_file_module
  - organic_mineral_mass_module
  - constituent_mass_module
  - exco_module
  - maximum_data_module
calls: []
reads:
  - in_exco%hmet
writes: []
purpose: ""
---

# exco_read_hmet

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `exco_read_hmet.f90`
- **Modules used**: [[hydrograph_module.f90]], [[input_file_module.f90]], [[organic_mineral_mass_module.f90]], [[constituent_mass_module.f90]], [[exco_module.f90]], [[maximum_data_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 1 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by** (live Dataview back-query):

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## File I/O
- **Reads**: `in_exco%hmet` _(variable; see file.cio)_

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
