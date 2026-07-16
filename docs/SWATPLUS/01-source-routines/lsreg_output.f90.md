---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: lsreg_output.f90
note_file: lsreg_output.f90
subroutine: lsreg_output
module:
  - time_module
  - basin_module
  - maximum_data_module
  - calibration_data_module
  - plant_data_module
  - landuse_data_module
  - hru_module
  - plant_module
  - output_landscape_module
  - organic_mineral_mass_module
calls: []
reads: []
writes: []
purpose: "! PRINT CODES: \"avann\" = average annual (always print); \"year\" = yearly; \"mon\" = monthly"
---

# lsreg_output

> [!info] Summary
> !    PRINT CODES: "avann" = average annual (always print); "year"  = yearly; "mon"   = monthly

## Basic Information
- **Type**: `subroutine`
- **Source file**: `lsreg_output.f90`
- **Modules used**: [[time_module.f90]], [[basin_module.f90]], [[maximum_data_module.f90]], [[calibration_data_module.f90]], [[plant_data_module.f90]], [[landuse_data_module.f90]], [[hru_module.f90]], [[plant_module.f90]], [[output_landscape_module.f90]], [[organic_mineral_mass_module.f90]]
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
