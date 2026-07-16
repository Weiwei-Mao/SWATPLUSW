---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: caltsoft_hyd.f90
note_file: caltsoft_hyd.f90
subroutine: caltsoft_hyd
module:
  - hydrograph_module
  - ru_module
  - aquifer_module
  - hru_lte_module
  - sd_channel_module
  - basin_module
  - maximum_data_module
  - calibration_data_module
  - conditional_module
  - reservoir_module
calls:
  - ascrv
  - time_control
reads: []
writes: []
purpose: ""
---

# caltsoft_hyd

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `caltsoft_hyd.f90`
- **Modules used**: [[hydrograph_module.f90]], [[ru_module.f90]], [[aquifer_module.f90]], [[hru_lte_module.f90]], [[sd_channel_module.f90]], [[basin_module.f90]], [[maximum_data_module.f90]], [[calibration_data_module.f90]], [[conditional_module.f90]], [[reservoir_module.f90]]
- **Subroutine calls**: 2 | **Files read**: 0 | **Files written**: 0

## Call Relationships
**This routine calls:**

- [[ascrv.f90]]
- [[time_control.f90]]

**Called by** (live Dataview back-query):

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
