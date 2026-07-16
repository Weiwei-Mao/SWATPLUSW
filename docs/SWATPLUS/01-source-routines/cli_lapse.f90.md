---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: cli_lapse.f90
note_file: cli_lapse.f90
subroutine: cli_lapse
module:
  - basin_module
  - climate_module
  - hydrograph_module
calls: []
reads: []
writes: []
purpose: "this subroutine adjusts precip and temperature for elevation"
---

# cli_lapse

> [!info] Summary
> this subroutine adjusts precip and temperature for elevation

## Basic Information
- **Type**: `subroutine`
- **Source file**: `cli_lapse.f90`
- **Modules used**: [[basin_module.f90]], [[climate_module.f90]], [[hydrograph_module.f90]]
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
