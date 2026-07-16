---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: sd_channel_surf_link.f90
note_file: sd_channel_surf_link.f90
subroutine: sd_channel_surf_link
module:
  - hydrograph_module
  - sd_channel_module
  - ru_module
  - hru_module
  - topography_data_module
calls: []
reads: []
writes: []
purpose: ""
---

# sd_channel_surf_link

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `sd_channel_surf_link.f90`
- **Modules used**: [[hydrograph_module.f90]], [[sd_channel_module.f90]], [[ru_module.f90]], [[hru_module.f90]], [[topography_data_module.f90]]
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
