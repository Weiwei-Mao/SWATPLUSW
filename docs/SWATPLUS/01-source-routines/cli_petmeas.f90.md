---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: cli_petmeas.f90
note_file: cli_petmeas.f90
subroutine: cli_petmeas
module:
  - climate_module
  - input_file_module
  - time_module
  - maximum_data_module
calls: []
uses_variables:
  - climate_module.f90#petm
  - climate_module.f90#petm_n
  - input_file_module.f90#in_cli
  - input_file_module.f90#in_path_pet
  - maximum_data_module.f90#db_mx
  - time_module.f90#time
input_variables:
  - climate_module.f90#petm
  - climate_module.f90#petm_n
reads:
  - in_cli%pet_cli
writes: []
purpose: ""
---

# cli_petmeas

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `cli_petmeas.f90`
- **Modules used**:
  - [[climate_module.f90]]
  - [[input_file_module.f90]]
  - [[time_module.f90]]
  - [[maximum_data_module.f90]]
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
- [[climate_module.f90#petm]] - `climate_measured_data`
- [[climate_module.f90#petm_n]] - `character(len=50), dimension(:), allocatable`
- [[input_file_module.f90#in_cli]] - `input_cli`
- [[input_file_module.f90#in_path_pet]] - `input_path_pet`
- [[maximum_data_module.f90#db_mx]] - `data_files_max_elements`
- [[time_module.f90#time]] - `time_current`

**Populated by file reads:**

- [[climate_module.f90#petm]]
- [[climate_module.f90#petm_n]]

## File I/O
- **Reads**:
  - [[pet.cli]]

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.

- Line 26, check [[input_file_module.f90#in_cli]] %pet_cli, potential evapotranspiration
	- if it does not exist, return
	- Else, read the file
- End
<!-- USER-NOTES-END -->
