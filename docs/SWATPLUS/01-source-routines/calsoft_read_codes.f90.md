---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: calsoft_read_codes.f90
note_file: calsoft_read_codes.f90
subroutine: calsoft_read_codes
module:
  - calibration_data_module
  - plant_data_module
  - input_file_module
  - soil_module
  - plant_module
  - hydrograph_module
  - hru_lte_module
  - sd_channel_module
  - organic_mineral_mass_module
  - mgt_operations_module
  - conditional_module
calls: []
uses_variables:
  - calibration_data_module.f90#cal_codes
  - calibration_data_module.f90#cal_soft
  - hydrograph_module.f90#res
  - input_file_module.f90#in_chg
input_variables:
  - calibration_data_module.f90#cal_codes
reads:
  - in_chg%codes_sft
writes: []
purpose: ""
---

# calsoft_read_codes

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `calsoft_read_codes.f90`
- **Modules used**:
  - [[calibration_data_module.f90]]
  - [[plant_data_module.f90]]
  - [[input_file_module.f90]]
  - [[soil_module.f90]]
  - [[plant_module.f90]]
  - [[hydrograph_module.f90]]
  - [[hru_lte_module.f90]]
  - [[sd_channel_module.f90]]
  - [[organic_mineral_mass_module.f90]]
  - [[mgt_operations_module.f90]]
  - [[conditional_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 1 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by:**

- [[proc_cal.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[calibration_data_module.f90#cal_codes]] - `soft_calibration_codes`
- [[calibration_data_module.f90#cal_soft]] - `character (len=1)`
- [[hydrograph_module.f90#res]] - `hyd_output`
- [[input_file_module.f90#in_chg]] - `input_chg`

**Populated by file reads:**

- [[calibration_data_module.f90#cal_codes]]

## File I/O
- **Reads**:
  - [[codes.sft]]

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
