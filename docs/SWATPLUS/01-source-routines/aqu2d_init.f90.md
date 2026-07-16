---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: aqu2d_init.f90
note_file: aqu2d_init.f90
subroutine: aqu2d_init
module:
  - hydrograph_module
  - sd_channel_module
  - maximum_data_module
  - constituent_mass_module
calls: []
reads: []
writes: []
purpose: ""
---

# aqu2d_init

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `aqu2d_init.f90`
- **Modules used**: [[hydrograph_module.f90]], [[sd_channel_module.f90]], [[maximum_data_module.f90]], [[constituent_mass_module.f90]]
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
