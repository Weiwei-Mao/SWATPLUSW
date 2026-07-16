---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: cli_tgen.f90
note_file: cli_tgen.f90
subroutine: cli_tgen
module:
  - climate_module
  - hydrograph_module
  - time_module
calls: []
reads: []
writes: []
purpose: "this subroutine generates temperature data when the user chooses to; simulate or when data is missing for particular days in the; weather file"
---

# cli_tgen

> [!info] Summary
> this subroutine generates temperature data when the user chooses to; simulate or when data is missing for particular days in the; weather file

## Basic Information
- **Type**: `subroutine`
- **Source file**: `cli_tgen.f90`
- **Modules used**: [[climate_module.f90]], [[hydrograph_module.f90]], [[time_module.f90]]
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
