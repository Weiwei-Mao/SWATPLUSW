---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: gwflow_simulate.f90
note_file: gwflow_simulate.f90
subroutine: gwflow_simulate
module:
  - gwflow_module
  - hydrograph_module
  - hru_module
  - sd_channel_module
  - time_module
  - soil_module
calls:
  - gwflow_rech
  - gwflow_gwet
  - gwflow_phreatophyte
  - gwflow_pump_ext
  - gwflow_canal_ext
  - gwflow_pond
  - gwflow_canal_div
  - gwflow_lateral
  - gwflow_output_day
  - gwflow_output_mon
  - gwflow_output_yr
  - gwflow_output_aa
reads: []
writes: []
purpose: "this subroutine calculates new groundwater storage and solute mass for each gwflow grid cell;; also, computes and write out daily/annual/average annual fluxes and mass balance error"
---

# gwflow_simulate

> [!info] Summary
> this subroutine calculates new groundwater storage and solute mass for each gwflow grid cell;; also, computes and write out daily/annual/average annual fluxes and mass balance error

## Basic Information
- **Type**: `subroutine`
- **Source file**: `gwflow_simulate.f90`
- **Modules used**: [[gwflow_module.f90]], [[hydrograph_module.f90]], [[hru_module.f90]], [[sd_channel_module.f90]], [[time_module.f90]], [[soil_module.f90]]
- **Subroutine calls**: 12 | **Files read**: 0 | **Files written**: 0

## Call Relationships
**This routine calls:**

- [[gwflow_rech.f90]]
- [[gwflow_gwet.f90]]
- [[gwflow_phreatophyte.f90]]
- [[gwflow_pump_ext.f90]]
- [[gwflow_canal_ext.f90]]
- [[gwflow_pond.f90]]
- [[gwflow_canal_div.f90]]
- [[gwflow_lateral.f90]]
- `gwflow_output_day`
- `gwflow_output_mon`
- `gwflow_output_yr`
- `gwflow_output_aa`

**Called by** (live Dataview back-query):

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
