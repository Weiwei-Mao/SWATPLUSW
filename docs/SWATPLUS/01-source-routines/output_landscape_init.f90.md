---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: output_landscape_init.f90
note_file: output_landscape_init.f90
subroutine: output_landscape_init
module:
  - hydrograph_module
  - channel_module
  - sd_channel_module
  - basin_module
  - maximum_data_module
  - calibration_data_module
  - aquifer_module
  - output_landscape_module
  - time_module
  - carbon_module
  - output_path_module
  - soil_module
  - carbon_legacy_module
calls:
  - open_output_file
  - open_cb_banner_pair
  - open_cb_wide_pair
  - soil_nutcarb_write
  - open_cb_flat_pair
  - carbon_legacy_open
  - cb_write_wide_header
  - cb_write_flat_header
  - cb_write_cbn_lyr_header
reads: []
writes: []
purpose: ""
---

# output_landscape_init

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `output_landscape_init.f90`
- **Modules used**: [[hydrograph_module.f90]], [[channel_module.f90]], [[sd_channel_module.f90]], [[basin_module.f90]], [[maximum_data_module.f90]], [[calibration_data_module.f90]], [[aquifer_module.f90]], [[output_landscape_module.f90]], [[time_module.f90]], [[carbon_module.f90]], [[output_path_module.f90]], [[soil_module.f90]], [[carbon_legacy_module.f90]]
- **Subroutine calls**: 9 | **Files read**: 0 | **Files written**: 0

## Call Relationships
**This routine calls:**

- `open_output_file`
- `open_cb_banner_pair`
- `open_cb_wide_pair`
- [[soil_nutcarb_write.f90]]
- `open_cb_flat_pair`
- `carbon_legacy_open`
- `cb_write_wide_header`
- `cb_write_flat_header`
- `cb_write_cbn_lyr_header`

**Called by** (live Dataview back-query):

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
