---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: cli_slrgen.f90
note_file: cli_slrgen.f90
subroutine: cli_slrgen
module:
  - hydrograph_module
  - climate_module
calls: []
reads: []
writes: []
purpose: "this subroutine generates solar radiation"
---

# cli_slrgen

> [!info] Summary
> this subroutine generates solar radiation

## Basic Information
- **Type**: `subroutine`
- **Source file**: `cli_slrgen.f90`
- **Modules used**: [[hydrograph_module.f90]], [[climate_module.f90]]
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
