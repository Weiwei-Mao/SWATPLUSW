---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: wet_fp_init.f90
note_file: wet_fp_init.f90
subroutine: wet_fp_init
module:
  - sd_channel_module
  - hydrograph_module
calls: []
uses_variables:
  - hydrograph_module.f90#hz
  - hydrograph_module.f90#jrch
  - hydrograph_module.f90#sp_ob
  - hydrograph_module.f90#wet
  - hydrograph_module.f90#wet_stor
  - sd_channel_module.f90#sd_ch
input_variables: []
reads: []
writes: []
purpose: "this subroutine routes computes the initial storage in flood plain wetlands"
---

# wet_fp_init

> [!info] Summary
> this subroutine routes computes the initial storage in flood plain wetlands

## Basic Information
- **Type**: `subroutine`
- **Source file**: `wet_fp_init.f90`
- **Modules used**:
  - [[sd_channel_module.f90]]
  - [[hydrograph_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 0 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by:**

- [[main.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[hydrograph_module.f90#hz]] - `hyd_output`
- [[hydrograph_module.f90#jrch]] - `integer`
- [[hydrograph_module.f90#sp_ob]] - `spatial_objects`
- [[hydrograph_module.f90#wet]] - `hyd_output`
- [[hydrograph_module.f90#wet_stor]] - `hyd_output`
- [[sd_channel_module.f90#sd_ch]] - `swatdeg_channel_dynamic`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
