---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: lsu_carbon_output.f90
note_file: lsu_carbon_output.f90
subroutine: lsu_carbon_output
module:
  - time_module
  - basin_module
  - maximum_data_module
  - calibration_data_module
  - hydrograph_module
  - carbon_module
  - plant_module
  - organic_mineral_mass_module
  - output_landscape_module
calls: []
reads: []
writes: []
purpose: "area-weighted LSU aggregations of three HRU-level carbon families:; lsu_carb_gl_* (gain/loss; soil + residue + plant flux); lsu_scf_* (HRU C transformations)"
---

# lsu_carbon_output

> [!info] Summary
> area-weighted LSU aggregations of three HRU-level carbon families:; lsu_carb_gl_*    (gain/loss; soil + residue + plant flux); lsu_scf_*        (HRU C transformations)

## Basic Information
- **Type**: `subroutine`
- **Source file**: `lsu_carbon_output.f90`
- **Modules used**: [[time_module.f90]], [[basin_module.f90]], [[maximum_data_module.f90]], [[calibration_data_module.f90]], [[hydrograph_module.f90]], [[carbon_module.f90]], [[plant_module.f90]], [[organic_mineral_mass_module.f90]], [[output_landscape_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 0 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by** (live Dataview back-query):

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
