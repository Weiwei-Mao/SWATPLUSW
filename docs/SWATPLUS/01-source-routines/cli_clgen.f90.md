---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: cli_clgen.f90
note_file: cli_clgen.f90
subroutine: cli_clgen
module:
  - basin_module
  - climate_module
  - time_module
  - hydrograph_module
calls: []
reads: []
writes: []
purpose: "this subroutine calculates the daylength, distribution of; radiation throughout the day and maximum radiation for day"
---

# cli_clgen

> [!info] Summary
> this subroutine calculates the daylength, distribution of; radiation throughout the day and maximum radiation for day

## Basic Information
- **Type**: `subroutine`
- **Source file**: `cli_clgen.f90`
- **Modules used**: [[basin_module.f90]], [[climate_module.f90]], [[time_module.f90]], [[hydrograph_module.f90]]
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
