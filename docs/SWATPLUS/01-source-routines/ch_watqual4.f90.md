---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: ch_watqual4.f90
note_file: ch_watqual4.f90
subroutine: ch_watqual4
module:
  - channel_module
  - hydrograph_module
  - climate_module
  - channel_data_module
  - sd_channel_module
  - water_body_module
calls:
  - rcurv_interp_flo
reads: []
writes: []
purpose: "this subroutine performs in-stream nutrient transformations and water; quality calculations"
---

# ch_watqual4

> [!info] Summary
> this subroutine performs in-stream nutrient transformations and water; quality calculations

## Basic Information
- **Type**: `subroutine`
- **Source file**: `ch_watqual4.f90`
- **Modules used**: [[channel_module.f90]], [[hydrograph_module.f90]], [[climate_module.f90]], [[channel_data_module.f90]], [[sd_channel_module.f90]], [[water_body_module.f90]]
- **Subroutine calls**: 1 | **Files read**: 0 | **Files written**: 0

## Call Relationships
**This routine calls:**

- [[rcurv_interp_flo.f90]]

**Called by** (live Dataview back-query):

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
