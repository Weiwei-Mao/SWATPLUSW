---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: ch_rtpath.f90
note_file: ch_rtpath.f90
subroutine: ch_rtpath
module:
  - basin_module
  - time_module
  - pathogen_data_module
  - channel_module
  - hydrograph_module
  - climate_module
  - constituent_mass_module
calls: []
reads: []
writes: []
purpose: "this subroutine routes bacteria through the stream network"
---

# ch_rtpath

> [!info] Summary
> this subroutine routes bacteria through the stream network

## Basic Information
- **Type**: `subroutine`
- **Source file**: `ch_rtpath.f90`
- **Modules used**: [[basin_module.f90]], [[time_module.f90]], [[pathogen_data_module.f90]], [[channel_module.f90]], [[hydrograph_module.f90]], [[climate_module.f90]], [[constituent_mass_module.f90]]
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
