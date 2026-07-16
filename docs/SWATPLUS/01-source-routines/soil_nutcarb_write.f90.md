---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: soil_nutcarb_write.f90
note_file: soil_nutcarb_write.f90
subroutine: soil_nutcarb_write
module:
  - soil_module
  - organic_mineral_mass_module
  - hydrograph_module
  - calibration_data_module
  - carbon_module
  - basin_module
  - plant_module
calls:
  - cb_soil_snap_emit
  - cb_cbn_lyr_emit
  - cb_n_p_pool_emit
  - cb_plc_stat_emit
  - cb_soil_snap_period
  - cb_cflux_stat_emit
  - cb_cpool_stat_emit
  - cb_write_depth_row
  - cb_write_var_block
  - cb_emit_row_id_csv
  - cb_emit_row_id_txt
  - cb_cflux_emit_blocks
reads: []
writes: []
purpose: "this subroutine writes soil carbon output."
---

# soil_nutcarb_write

> [!info] Summary
> this subroutine writes soil carbon output.

## Basic Information
- **Type**: `subroutine`
- **Source file**: `soil_nutcarb_write.f90`
- **Modules used**: [[soil_module.f90]], [[organic_mineral_mass_module.f90]], [[hydrograph_module.f90]], [[calibration_data_module.f90]], [[carbon_module.f90]], [[basin_module.f90]], [[plant_module.f90]]
- **Subroutine calls**: 12 | **Files read**: 0 | **Files written**: 0

## Call Relationships
**This routine calls:**

- `cb_soil_snap_emit`
- `cb_cbn_lyr_emit`
- `cb_n_p_pool_emit`
- `cb_plc_stat_emit`
- `cb_soil_snap_period`
- `cb_cflux_stat_emit`
- `cb_cpool_stat_emit`
- `cb_write_depth_row`
- `cb_write_var_block`
- `cb_emit_row_id_csv`
- `cb_emit_row_id_txt`
- `cb_cflux_emit_blocks`

**Called by** (live Dataview back-query):

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
