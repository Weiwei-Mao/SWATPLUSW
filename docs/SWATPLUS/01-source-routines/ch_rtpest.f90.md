---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: ch_rtpest.f90
note_file: ch_rtpest.f90
subroutine: ch_rtpest
module:
  - channel_data_module
  - channel_module
  - sd_channel_module
  - ch_pesticide_module
  - hydrograph_module
  - constituent_mass_module
  - pesticide_data_module
calls: []
reads: []
writes: []
purpose: "this subroutine computes the daily stream pesticide balance; (soluble and sorbed)"
---

# ch_rtpest

> [!info] Summary
> this subroutine computes the daily stream pesticide balance; (soluble and sorbed)

## Basic Information
- **Type**: `subroutine`
- **Source file**: `ch_rtpest.f90`
- **Modules used**: [[channel_data_module.f90]], [[channel_module.f90]], [[sd_channel_module.f90]], [[ch_pesticide_module.f90]], [[hydrograph_module.f90]], [[constituent_mass_module.f90]], [[pesticide_data_module.f90]]
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
