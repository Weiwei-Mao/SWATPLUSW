---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: ch_read.f90
note_file: ch_read.f90
subroutine: ch_read
module:
  - basin_module
  - input_file_module
  - channel_data_module
  - maximum_data_module
  - hydrograph_module
  - pesticide_data_module
calls: []
uses_variables:
  - channel_data_module.f90#ch_dat
  - channel_data_module.f90#ch_dat_c
  - channel_data_module.f90#ch_hyd
  - channel_data_module.f90#ch_init
  - channel_data_module.f90#ch_nut
  - channel_data_module.f90#ch_sed
  - input_file_module.f90#in_cha
  - maximum_data_module.f90#db_mx
input_variables:
  - channel_data_module.f90#ch_dat_c
reads:
  - in_cha%dat
writes: []
purpose: ""
---

# ch_read

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `ch_read.f90`
- **Modules used**:
  - [[basin_module.f90]]
  - [[input_file_module.f90]]
  - [[channel_data_module.f90]]
  - [[maximum_data_module.f90]]
  - [[hydrograph_module.f90]]
  - [[pesticide_data_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 1 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by:**

- [[proc_cha.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[channel_data_module.f90#ch_dat]] - `channel_data`
- [[channel_data_module.f90#ch_dat_c]] - `channel_data_char_input`
- [[channel_data_module.f90#ch_hyd]] - `channel_hyd_data`
- [[channel_data_module.f90#ch_init]] - `channel_init_datafiles`
- [[channel_data_module.f90#ch_nut]] - `channel_nut_data`
- [[channel_data_module.f90#ch_sed]] - `channel_sed_data`
- [[input_file_module.f90#in_cha]] - `input_cha`
- [[maximum_data_module.f90#db_mx]] - `data_files_max_elements`

**Populated by file reads:**

- [[channel_data_module.f90#ch_dat_c]]

## File I/O
- **Reads**:
  - [[channel.cha]]

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
