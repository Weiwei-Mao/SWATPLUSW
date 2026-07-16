---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: cli_read_atmodep.f90
note_file: cli_read_atmodep.f90
subroutine: cli_read_atmodep
module:
  - basin_module
  - input_file_module
  - climate_module
  - time_module
  - maximum_data_module
calls: []
uses_variables:
  - climate_module.f90#atmo_n
  - climate_module.f90#atmodep
  - climate_module.f90#atmodep_cont
  - input_file_module.f90#in_cli
  - maximum_data_module.f90#db_mx
  - time_module.f90#time
input_variables:
  - climate_module.f90#atmodep
  - climate_module.f90#atmodep_cont
reads:
  - in_cli%atmo_cli
writes: []
purpose: ""
---

# cli_read_atmodep

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `cli_read_atmodep.f90`
- **Modules used**:
  - [[basin_module.f90]]
  - [[input_file_module.f90]]
  - [[climate_module.f90]]
  - [[time_module.f90]]
  - [[maximum_data_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 1 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by:**

- [[proc_read.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[climate_module.f90#atmo_n]] - `character(len=50), dimension(:), allocatable`
- [[climate_module.f90#atmodep]] - `atmospheric_deposition`
- [[climate_module.f90#atmodep_cont]] - `atmospheric_deposition_control`
- [[input_file_module.f90#in_cli]] - `input_cli`
- [[maximum_data_module.f90#db_mx]] - `data_files_max_elements`
- [[time_module.f90#time]] - `time_current`

**Populated by file reads:**

- [[climate_module.f90#atmodep]]
- [[climate_module.f90#atmodep_cont]]

## File I/O
- **Reads**:
  - [[atmodep.cli]]

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
