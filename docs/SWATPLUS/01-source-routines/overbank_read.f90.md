---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: overbank_read.f90
note_file: overbank_read.f90
subroutine: overbank_read
module:
  - hydrograph_module
  - input_file_module
  - maximum_data_module
  - sd_channel_module
calls: []
uses_variables:
  - hydrograph_module.f90#ch_sur
  - input_file_module.f90#in_link
  - maximum_data_module.f90#db_mx
  - sd_channel_module.f90#sd_ch
input_variables:
  - sd_channel_module.f90#sd_ch
reads:
  - in_link%chan_surf
writes: []
purpose: ""
---

# overbank_read

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `overbank_read.f90`
- **Modules used**:
  - [[hydrograph_module.f90]]
  - [[input_file_module.f90]]
  - [[maximum_data_module.f90]]
  - [[sd_channel_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 1 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by:**

- [[hyd_connect.f90]]
- [[proc_cha.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[hydrograph_module.f90#ch_sur]] - `channel_surface_elements`
- [[input_file_module.f90#in_link]] - `input_link`
- [[maximum_data_module.f90#db_mx]] - `data_files_max_elements`
- [[sd_channel_module.f90#sd_ch]] - `swatdeg_channel_dynamic`

**Populated by file reads:**

- [[sd_channel_module.f90#sd_ch]]

## File I/O
- **Reads**:
  - [[chan-surf.lin]]

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
