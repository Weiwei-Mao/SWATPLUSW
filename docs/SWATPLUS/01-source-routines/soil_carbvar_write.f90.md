---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: soil_carbvar_write.f90
note_file: soil_carbvar_write.f90
subroutine: soil_carbvar_write
module:
  - basin_module
  - carbon_module
  - hydrograph_module
  - organic_mineral_mass_module
  - calibration_data_module
  - soil_module
  - time_module
calls:
  - cv_emit_row_id_txt
  - cb_write_depth_row
  - cv_drv_blocks
  - cv_emit_row_id_csv
  - cv_dyn_blocks
  - cb_write_var_block
reads: []
writes: []
purpose: ""
---

# soil_carbvar_write

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `soil_carbvar_write.f90`
- **Modules used**: [[basin_module.f90]], [[carbon_module.f90]], [[hydrograph_module.f90]], [[organic_mineral_mass_module.f90]], [[calibration_data_module.f90]], [[soil_module.f90]], [[time_module.f90]]
- **Subroutine calls**: 6 | **Files read**: 0 | **Files written**: 0

## Call Relationships
**This routine calls:**

- `cv_emit_row_id_txt`
- `cb_write_depth_row`
- `cv_drv_blocks`
- `cv_emit_row_id_csv`
- `cv_dyn_blocks`
- `cb_write_var_block`

**Called by** (live Dataview back-query):

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
