---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: hru_output.f90
note_file: hru_output.f90
subroutine: hru_output
module:
  - plant_module
  - plant_data_module
  - time_module
  - basin_module
  - output_landscape_module
  - hydrograph_module
  - organic_mineral_mass_module
  - soil_module
  - carbon_module
  - hru_module
  - landuse_data_module
calls:
  - soil_nutcarb_write
  - soil_nutcarb_write_legacy
reads: []
writes: []
purpose: "this subroutine outputs HRU variables on daily, monthly and annual time steps"
---

# hru_output

> [!info] Summary
> this subroutine outputs HRU variables on daily, monthly and annual time steps

## Basic Information
- **Type**: `subroutine`
- **Source file**: `hru_output.f90`
- **Modules used**: [[plant_module.f90]], [[plant_data_module.f90]], [[time_module.f90]], [[basin_module.f90]], [[output_landscape_module.f90]], [[hydrograph_module.f90]], [[organic_mineral_mass_module.f90]], [[soil_module.f90]], [[carbon_module.f90]], [[hru_module.f90]], [[landuse_data_module.f90]]
- **Subroutine calls**: 2 | **Files read**: 0 | **Files written**: 0

## Call Relationships
**This routine calls:**

- [[soil_nutcarb_write.f90]]
- [[soil_nutcarb_write_legacy.f90]]

**Called by** (live Dataview back-query):

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
