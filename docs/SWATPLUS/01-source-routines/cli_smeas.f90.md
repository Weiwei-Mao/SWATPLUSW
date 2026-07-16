---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: cli_smeas.f90
note_file: cli_smeas.f90
subroutine: cli_smeas
module:
  - climate_module
  - input_file_module
  - time_module
  - maximum_data_module
calls: []
uses_variables:
  - climate_module.f90#slr
  - climate_module.f90#slr_n
  - input_file_module.f90#in_cli
  - input_file_module.f90#in_path_slr
  - maximum_data_module.f90#db_mx
  - time_module.f90#time
input_variables:
  - climate_module.f90#slr
  - climate_module.f90#slr_n
reads:
  - in_cli%slr_cli
  - slr(i
  - TRIM(ADJUSTL(in_path_slr%slr
writes: []
purpose: ""
---

# cli_smeas

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `cli_smeas.f90`
- **Modules used**:
  - [[climate_module.f90]]
  - [[input_file_module.f90]]
  - [[time_module.f90]]
  - [[maximum_data_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 3 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by:**

- [[proc_date_time.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[climate_module.f90#slr]] - `climate_measured_data`
- [[climate_module.f90#slr_n]] - `character(len=50), dimension(:), allocatable`
- [[input_file_module.f90#in_cli]] - `input_cli`
- [[input_file_module.f90#in_path_slr]] - `input_path_slr`
- [[maximum_data_module.f90#db_mx]] - `data_files_max_elements`
- [[time_module.f90#time]] - `time_current`

**Populated by file reads:**

- [[climate_module.f90#slr]]
- [[climate_module.f90#slr_n]]

## File I/O
- **Reads**:
  - [[slr.cli]]
  - `slr(i` _(variable; see [[file.cio]])_
  - `TRIM(ADJUSTL(in_path_slr%slr` _(variable; see [[file.cio]])_

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
