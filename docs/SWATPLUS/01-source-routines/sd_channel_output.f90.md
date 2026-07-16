---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: sd_channel_output.f90
note_file: sd_channel_output.f90
subroutine: sd_channel_output
module:
  - sd_channel_module
  - basin_module
  - time_module
  - hydrograph_module
  - water_body_module
calls: []
reads: []
writes: []
purpose: ""
---

# sd_channel_output

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `sd_channel_output.f90`
- **Modules used**: [[sd_channel_module.f90]], [[basin_module.f90]], [[time_module.f90]], [[hydrograph_module.f90]], [[water_body_module.f90]]
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
