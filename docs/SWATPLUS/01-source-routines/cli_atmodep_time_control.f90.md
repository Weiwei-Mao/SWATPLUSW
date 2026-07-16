---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: cli_atmodep_time_control.f90
note_file: cli_atmodep_time_control.f90
subroutine: cli_atmodep_time_control
module:
  - climate_module
  - time_module
calls: []
uses_variables:
  - climate_module.f90#atmodep_cont
  - time_module.f90#time
input_variables: []
reads: []
writes: []
purpose: ""
---

# cli_atmodep_time_control

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `cli_atmodep_time_control.f90`
- **Modules used**:
  - [[climate_module.f90]]
  - [[time_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 0 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by:**

- [[time_control.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[climate_module.f90#atmodep_cont]] - `atmospheric_deposition_control`
- [[time_module.f90#time]] - `time_current`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
