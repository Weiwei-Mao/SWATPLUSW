---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: cs_urban_read.f90
note_file: cs_urban_read.f90
subroutine: cs_urban_read
module:
  - maximum_data_module
  - urban_data_module
  - constituent_mass_module
  - cs_module
calls: []
reads:
  - cs_urban
writes: []
purpose: ""
---

# cs_urban_read

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `cs_urban_read.f90`
- **Modules used**: [[maximum_data_module.f90]], [[urban_data_module.f90]], [[constituent_mass_module.f90]], [[cs_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 1 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by** (live Dataview back-query):

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## File I/O
- **Reads**: `cs_urban` _(variable; see file.cio)_

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
