---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: ttcoef_wway.f90
note_file: ttcoef_wway.f90
subroutine: ttcoef_wway
module:
  - hru_module
  - channel_velocity_module
calls: []
uses_variables:
  - channel_velocity_module.f90#grwway_vel
  - hru_module.f90#hru
input_variables: []
reads: []
writes: []
purpose: "this subroutine computes travel time coefficients for routing; along the main channel - grassed waterways"
---

# ttcoef_wway

> [!info] Summary
> this subroutine computes travel time coefficients for routing; along the main channel - grassed waterways

## Basic Information
- **Type**: `subroutine`
- **Source file**: `ttcoef_wway.f90`
- **Modules used**:
  - [[hru_module.f90]]
  - [[channel_velocity_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 0 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by:**

- [[structure_set_parms.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[channel_velocity_module.f90#grwway_vel]] - `channel_velocity_parameters`
- [[hru_module.f90#hru]] - `hydrologic_response_unit`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
