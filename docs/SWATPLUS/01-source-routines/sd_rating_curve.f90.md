---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: sd_rating_curve.f90
note_file: sd_rating_curve.f90
subroutine: sd_rating_curve
module:
  - sd_channel_module
  - channel_velocity_module
  - maximum_data_module
calls: []
reads: []
writes: []
purpose: ""
---

# sd_rating_curve

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `sd_rating_curve.f90`
- **Modules used**: [[sd_channel_module.f90]], [[channel_velocity_module.f90]], [[maximum_data_module.f90]]
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
