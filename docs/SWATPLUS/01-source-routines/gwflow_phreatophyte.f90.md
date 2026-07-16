---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: gwflow_phreatophyte.f90
note_file: gwflow_phreatophyte.f90
subroutine: gwflow_phreatophyte
module:
  - gwflow_module
calls: []
reads: []
writes: []
purpose: "this subroutine calculates the water removed from the aquifer via phreatophyte extraction; (extraction volumes are used in gwflow_simulate, in groundwater balance equations)"
---

# gwflow_phreatophyte

> [!info] Summary
> this subroutine calculates the water removed from the aquifer via phreatophyte extraction; (extraction volumes are used in gwflow_simulate, in groundwater balance equations)

## Basic Information
- **Type**: `subroutine`
- **Source file**: `gwflow_phreatophyte.f90`
- **Modules used**: [[gwflow_module.f90]]
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
