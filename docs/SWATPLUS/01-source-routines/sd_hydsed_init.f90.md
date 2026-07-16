---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: sd_hydsed_init.f90
note_file: sd_hydsed_init.f90
subroutine: sd_hydsed_init
module:
  - input_file_module
  - sd_channel_module
  - channel_velocity_module
  - maximum_data_module
  - hydrograph_module
  - constituent_mass_module
  - pesticide_data_module
  - basin_module
calls:
  - sd_rating_curve
  - rcurv_interp_dep
  - hyd_convert_conc_to_mass
reads: []
writes: []
purpose: ""
---

# sd_hydsed_init

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `sd_hydsed_init.f90`
- **Modules used**: [[input_file_module.f90]], [[sd_channel_module.f90]], [[channel_velocity_module.f90]], [[maximum_data_module.f90]], [[hydrograph_module.f90]], [[constituent_mass_module.f90]], [[pesticide_data_module.f90]], [[basin_module.f90]]
- **Subroutine calls**: 3 | **Files read**: 0 | **Files written**: 0

## Call Relationships
**This routine calls:**

- [[sd_rating_curve.f90]]
- [[rcurv_interp_dep.f90]]
- `hyd_convert_conc_to_mass`

**Called by** (live Dataview back-query):

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
