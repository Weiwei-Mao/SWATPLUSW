---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: aqu_initial.f90
note_file: aqu_initial.f90
subroutine: aqu_initial
module:
  - aquifer_module
  - hydrograph_module
  - constituent_mass_module
  - aqu_pesticide_module
  - salt_module
  - salt_aquifer
  - cs_module
  - cs_aquifer
calls: []
reads: []
writes: []
purpose: ""
---

# aqu_initial

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `aqu_initial.f90`
- **Modules used**: [[aquifer_module.f90]], [[hydrograph_module.f90]], [[constituent_mass_module.f90]], [[aqu_pesticide_module.f90]], [[salt_module.f90]], [[salt_aquifer.f90]], [[cs_module.f90]], [[cs_aquifer.f90]]
- **Subroutine calls**: 0 | **Files read**: 0 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by** (live Dataview back-query):

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
