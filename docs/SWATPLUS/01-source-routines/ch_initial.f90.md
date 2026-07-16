---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: ch_initial.f90
note_file: ch_initial.f90
subroutine: ch_initial
module:
  - channel_data_module
  - channel_module
calls: []
uses_variables:
  - channel_data_module.f90#ch_dat
  - channel_data_module.f90#ch_sed
  - channel_module.f90#ch
input_variables: []
reads: []
writes: []
purpose: ""
---

# ch_initial

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `ch_initial.f90`
- **Modules used**:
  - [[channel_data_module.f90]]
  - [[channel_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 0 | **Files written**: 0

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
- [[channel_data_module.f90#ch_sed]] - `channel_sed_data`
- [[channel_module.f90#ch]] - `channel`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
