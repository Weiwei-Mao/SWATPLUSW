---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: climate_control.f90
note_file: climate_control.f90
subroutine: climate_control
module:
  - climate_module
  - basin_module
  - time_module
  - hydrograph_module
  - maximum_data_module
calls:
  - cli_precip_control
  - cli_weatgn
  - cli_tgen
  - cli_bounds_check
  - cli_clgen
  - cli_slrgen
  - cli_rhgen
  - cli_wndgen
reads: []
writes: []
purpose: "this subroutine controls weather inputs to SWAT. Precipitation and; temperature data is read in and the weather generator is called to; fill in radiation, wind speed and relative humidity as well as"
---

# climate_control

> [!info] Summary
> this subroutine controls weather inputs to SWAT. Precipitation and; temperature data is read in and the weather generator is called to; fill in radiation, wind speed and relative humidity as well as

## Basic Information
- **Type**: `subroutine`
- **Source file**: `climate_control.f90`
- **Modules used**: [[climate_module.f90]], [[basin_module.f90]], [[time_module.f90]], [[hydrograph_module.f90]], [[maximum_data_module.f90]]
- **Subroutine calls**: 8 | **Files read**: 0 | **Files written**: 0

## Call Relationships
**This routine calls:**

- [[cli_precip_control.f90]]
- [[cli_weatgn.f90]]
- [[cli_tgen.f90]]
- [[cli_bounds_check.f90]]
- [[cli_clgen.f90]]
- [[cli_slrgen.f90]]
- [[cli_rhgen.f90]]
- [[cli_wndgen.f90]]

**Called by** (live Dataview back-query):

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
