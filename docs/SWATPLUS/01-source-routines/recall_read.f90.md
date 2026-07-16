---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: recall_read.f90
note_file: recall_read.f90
subroutine: recalldb_read
module:
  - water_allocation_module
  - maximum_data_module
  - recall_module
  - hydrograph_module
  - input_file_module
  - organic_mineral_mass_module
  - constituent_mass_module
  - time_module
  - exco_module
calls:
  - recall_read
reads:
  - recall_db.rec
  - recall_db(irec
  - pest.com
  - rec_pest(i
writes: []
purpose: ""
---

# recalldb_read

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `recall_read.f90`
- **Modules used**: [[water_allocation_module.f90]], [[maximum_data_module.f90]], [[recall_module.f90]], [[hydrograph_module.f90]], [[input_file_module.f90]], [[organic_mineral_mass_module.f90]], [[constituent_mass_module.f90]], [[time_module.f90]], [[exco_module.f90]]
- **Subroutine calls**: 1 | **Files read**: 4 | **Files written**: 0

## Call Relationships
**This routine calls:**

- [[recall_read.f90]]

**Called by** (live Dataview back-query):

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## File I/O
- **Reads**: `recall_db.rec`, `recall_db(irec` _(variable; see file.cio)_, `pest.com`, `rec_pest(i` _(variable; see file.cio)_

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
