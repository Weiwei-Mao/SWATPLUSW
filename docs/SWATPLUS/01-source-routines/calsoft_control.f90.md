---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: calsoft_control.f90
note_file: calsoft_control.f90
subroutine: calsoft_control
module:
  - sd_channel_module
  - hru_lte_module
  - maximum_data_module
  - calibration_data_module
  - time_module
  - basin_module
  - hru_module
  - hydrograph_module
  - soil_module
calls:
  - calsoft_hyd
  - calsoft_hyd_bfr
  - caltsoft_hyd
  - calsoft_plant
  - calsoft_sed
  - pl_write_parms_cal
reads: []
writes: []
purpose: ""
---

# calsoft_control

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `calsoft_control.f90`
- **Modules used**: [[sd_channel_module.f90]], [[hru_lte_module.f90]], [[maximum_data_module.f90]], [[calibration_data_module.f90]], [[time_module.f90]], [[basin_module.f90]], [[hru_module.f90]], [[hydrograph_module.f90]], [[soil_module.f90]]
- **Subroutine calls**: 6 | **Files read**: 0 | **Files written**: 0

## Call Relationships
**This routine calls:**

- [[calsoft_hyd.f90]]
- [[calsoft_hyd_bfr.f90]]
- [[caltsoft_hyd.f90]]
- [[calsoft_plant.f90]]
- [[calsoft_sed.f90]]
- [[pl_write_parms_cal.f90]]

**Called by** (live Dataview back-query):

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
