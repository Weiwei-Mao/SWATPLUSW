---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: sd_channel_control3.f90
note_file: sd_channel_control3.f90
subroutine: sd_channel_control3
module:
  - sd_channel_module
  - channel_velocity_module
  - basin_module
  - hydrograph_module
  - constituent_mass_module
  - conditional_module
  - channel_data_module
  - channel_module
  - ch_pesticide_module
  - climate_module
  - water_body_module
  - time_module
  - ch_salt_module
  - ch_cs_module
  - gwflow_module
  - water_allocation_module
  - maximum_data_module
calls:
  - cli_lapse
  - gwflow_channel_exch
  - gwflow_canal
  - gwflow_tile
  - gwflow_satexcess
  - sd_channel_sediment3
  - ch_rtmusk
  - ch_rtpest
  - ch_rtpath
  - rcurv_interp_flo
  - ch_watqual4
  - wallo_control
  - ch_temp
reads: []
writes: []
purpose: ""
---

# sd_channel_control3

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `sd_channel_control3.f90`
- **Modules used**: [[sd_channel_module.f90]], [[channel_velocity_module.f90]], [[basin_module.f90]], [[hydrograph_module.f90]], [[constituent_mass_module.f90]], [[conditional_module.f90]], [[channel_data_module.f90]], [[channel_module.f90]], [[ch_pesticide_module.f90]], [[climate_module.f90]], [[water_body_module.f90]], [[time_module.f90]], [[ch_salt_module.f90]], [[ch_cs_module.f90]], [[gwflow_module.f90]], [[water_allocation_module.f90]], [[maximum_data_module.f90]]
- **Subroutine calls**: 13 | **Files read**: 0 | **Files written**: 0

## Call Relationships
**This routine calls:**

- [[cli_lapse.f90]]
- [[gwflow_channel_exch.f90]]
- [[gwflow_canal.f90]]
- [[gwflow_tile.f90]]
- [[gwflow_satexcess.f90]]
- [[sd_channel_sediment3.f90]]
- [[ch_rtmusk.f90]]
- [[ch_rtpest.f90]]
- [[ch_rtpath.f90]]
- [[rcurv_interp_flo.f90]]
- [[ch_watqual4.f90]]
- [[wallo_control.f90]]
- [[ch_temp.f90]]

**Called by** (live Dataview back-query):

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
