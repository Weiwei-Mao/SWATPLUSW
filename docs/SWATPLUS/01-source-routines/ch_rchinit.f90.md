---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: ch_rchinit.f90
note_file: ch_rchinit.f90
subroutine: ch_rchinit
module:
  - channel_module
  - hydrograph_module
calls: []
reads: []
writes: []
purpose: "this subroutine initializes variables for the daily simulation of the; channel routing command loop"
---

# ch_rchinit

> [!info] Summary
> this subroutine initializes variables for the daily simulation of the; channel routing command loop

## Basic Information
- **Type**: `subroutine`
- **Source file**: `ch_rchinit.f90`
- **Modules used**: [[channel_module.f90]], [[hydrograph_module.f90]]
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
