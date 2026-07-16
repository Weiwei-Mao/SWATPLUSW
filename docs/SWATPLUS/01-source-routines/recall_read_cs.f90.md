---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: recall_read_cs.f90
note_file: recall_read_cs.f90
subroutine: recall_read_cs
module:
  - hydrograph_module
  - input_file_module
  - organic_mineral_mass_module
  - constituent_mass_module
  - maximum_data_module
  - time_module
  - exco_module
calls: []
reads:
  - cs_recall.rec
  - rec_cs(i
writes: []
purpose: ""
---

# recall_read_cs

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `recall_read_cs.f90`
- **Modules used**: [[hydrograph_module.f90]], [[input_file_module.f90]], [[organic_mineral_mass_module.f90]], [[constituent_mass_module.f90]], [[maximum_data_module.f90]], [[time_module.f90]], [[exco_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 2 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by** (live Dataview back-query):

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## File I/O
- **Reads**: `cs_recall.rec`, `rec_cs(i` _(variable; see file.cio)_

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
