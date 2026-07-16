---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: ch_read_init_cs.f90
note_file: ch_read_init_cs.f90
subroutine: ch_read_init_cs
module:
  - basin_module
  - input_file_module
  - maximum_data_module
  - channel_data_module
  - sd_channel_module
calls: []
uses_variables:
  - channel_data_module.f90#ch_init_cs
  - maximum_data_module.f90#db_mx
input_variables:
  - channel_data_module.f90#ch_init_cs
reads:
  - initial.cha_cs
writes: []
purpose: ""
---

# ch_read_init_cs

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `ch_read_init_cs.f90`
- **Modules used**:
  - [[basin_module.f90]]
  - [[input_file_module.f90]]
  - [[maximum_data_module.f90]]
  - [[channel_data_module.f90]]
  - [[sd_channel_module.f90]]
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
- [[channel_data_module.f90#ch_init_cs]] - `channel_init_datafiles_cs`
- [[maximum_data_module.f90#db_mx]] - `data_files_max_elements`

**Populated by file reads:**

- [[channel_data_module.f90#ch_init_cs]]

## File I/O
- **Reads**:
  - [[initial.cha_cs]]

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
