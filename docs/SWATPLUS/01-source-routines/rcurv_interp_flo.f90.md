---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: rcurv_interp_flo.f90
note_file: rcurv_interp_flo.f90
subroutine: rcurv_interp_flo
module:
  - sd_channel_module
calls:
  - chrc_interp
uses_variables:
  - sd_channel_module.f90#ch_rcurv
  - sd_channel_module.f90#rcurv
input_variables: []
reads: []
writes: []
purpose: "this subroutine interpolates between points on a rating curve given flow rate"
---

# rcurv_interp_flo

> [!info] Summary
> this subroutine interpolates between points on a rating curve given flow rate

## Basic Information
- **Type**: `subroutine`
- **Source file**: `rcurv_interp_flo.f90`
- **Modules used**:
  - [[sd_channel_module.f90]]
- **Subroutine calls**: 1 | **Files read**: 0 | **Files written**: 0

## Call Relationships
**This routine calls:**

- [[sd_channel_module.f90#chrc_interp]]

**Called by:**

- [[ch_rtmusk.f90]]
- [[ch_watqual4.f90]]
- [[sd_channel_control3.f90]]
- [[sd_channel_sediment3.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[sd_channel_module.f90#ch_rcurv]] - `channel_rating_curve`
- [[sd_channel_module.f90#rcurv]] - `channel_rating_curve_parameters`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
