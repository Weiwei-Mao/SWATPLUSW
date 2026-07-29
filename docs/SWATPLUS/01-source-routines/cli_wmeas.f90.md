---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: cli_wmeas.f90
note_file: cli_wmeas.f90
subroutine: cli_wmeas
module:
  - input_file_module
  - climate_module
  - maximum_data_module
  - time_module
calls: []
uses_variables:
  - climate_module.f90#wnd
  - climate_module.f90#wnd_n
  - input_file_module.f90#in_cli
  - input_file_module.f90#in_path_wnd
  - maximum_data_module.f90#db_mx
  - time_module.f90#time
input_variables:
  - climate_module.f90#wnd
  - climate_module.f90#wnd_n
reads:
  - in_cli%wnd_cli
writes: []
purpose: ""
---

# cli_wmeas

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `cli_wmeas.f90`
- **Modules used**:
  - [[input_file_module.f90]]
  - [[climate_module.f90]]
  - [[maximum_data_module.f90]]
  - [[time_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 1 | **Files written**: 0

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
- [[climate_module.f90#wnd]] - `climate_measured_data`
- [[climate_module.f90#wnd_n]] - `character(len=50), dimension(:), allocatable`
- [[input_file_module.f90#in_cli]] - `input_cli`
- [[input_file_module.f90#in_path_wnd]] - `input_path_wnd`
- [[maximum_data_module.f90#db_mx]] - `data_files_max_elements`
- [[time_module.f90#time]] - `time_current`

**Populated by file reads:**

- [[climate_module.f90#wnd]]
- [[climate_module.f90#wnd_n]]

## File I/O
- **Reads**:
  - [[wnd.cli]]

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
