---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: salt_plant_read.f90
note_file: salt_plant_read.f90
subroutine: salt_plant_read
module:
  - constituent_mass_module
  - input_file_module
  - maximum_data_module
  - salt_data_module
calls: []
reads:
  - salt_plants
writes: []
purpose: ""
---

# salt_plant_read

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `salt_plant_read.f90`
- **Modules used**: [[constituent_mass_module.f90]], [[input_file_module.f90]], [[maximum_data_module.f90]], [[salt_data_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 1 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by** (live Dataview back-query):

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## File I/O
- **Reads**: `salt_plants` _(variable; see file.cio)_

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
