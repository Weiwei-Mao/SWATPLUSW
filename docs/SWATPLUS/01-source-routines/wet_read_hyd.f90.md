---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: wet_read_hyd.f90
note_file: wet_read_hyd.f90
subroutine: wet_read_hyd
module:
  - basin_module
  - input_file_module
  - maximum_data_module
  - reservoir_data_module
  - output_landscape_module
  - gwflow_module
calls: []
uses_variables:
  - basin_module.f90#bsn_cc
  - gwflow_module.f90#in_wet_cell
  - gwflow_module.f90#out_gw
  - input_file_module.f90#in_res
  - maximum_data_module.f90#db_mx
  - reservoir_data_module.f90#wet_hyd
  - reservoir_data_module.f90#wet_hyddb
input_variables:
  - reservoir_data_module.f90#wet_hyddb
reads:
  - in_res%hyd_wet
  - gwflow.wetland
writes: []
purpose: ""
---

# wet_read_hyd

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `wet_read_hyd.f90`
- **Modules used**:
  - [[basin_module.f90]]
  - [[input_file_module.f90]]
  - [[maximum_data_module.f90]]
  - [[reservoir_data_module.f90]]
  - [[output_landscape_module.f90]]
  - [[gwflow_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 2 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by:**

- [[main.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[basin_module.f90#bsn_cc]] - `basin_control_codes`
- [[gwflow_module.f90#in_wet_cell]] - `integer`
- [[gwflow_module.f90#out_gw]] - `integer`
- [[input_file_module.f90#in_res]] - `input_res`
- [[maximum_data_module.f90#db_mx]] - `data_files_max_elements`
- [[reservoir_data_module.f90#wet_hyd]] - `wetland_hyd_data`
- [[reservoir_data_module.f90#wet_hyddb]] - `wetland_hyd_data`

**Populated by file reads:**

- [[reservoir_data_module.f90#wet_hyddb]]

## File I/O
- **Reads**:
  - [[hydrology.wet]]
  - [[gwflow.wetland]]

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
