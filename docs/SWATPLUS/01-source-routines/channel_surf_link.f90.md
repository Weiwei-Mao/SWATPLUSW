---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: channel_surf_link.f90
note_file: channel_surf_link.f90
subroutine: channel_surf_link
module:
  - hydrograph_module
  - channel_module
  - ru_module
  - maximum_data_module
  - hru_module
calls: []
reads: []
writes: []
purpose: ""
---

# channel_surf_link

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `channel_surf_link.f90`
- **Modules used**: [[hydrograph_module.f90]], [[channel_module.f90]], [[ru_module.f90]], [[maximum_data_module.f90]], [[hru_module.f90]]
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
