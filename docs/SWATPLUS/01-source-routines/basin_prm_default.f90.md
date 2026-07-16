---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: basin_prm_default.f90
note_file: basin_prm_default.f90
subroutine: basin_prm_default
module:
  - basin_module
  - hru_module
  - utils
calls: []
uses_variables:
  - basin_module.f90#bsn_prm
  - hru_module.f90#uptake
input_variables: []
reads: []
writes: []
purpose: ""
---

# basin_prm_default

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `basin_prm_default.f90`
- **Modules used**:
  - [[basin_module.f90]]
  - [[hru_module.f90]]
  - [[utils.f90]]
- **Subroutine calls**: 0 | **Files read**: 0 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by:**

- [[proc_bsn.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[basin_module.f90#bsn_prm]] - `basin_parms`
- [[hru_module.f90#uptake]] - `uptake_parameters`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
- Set the default value of [[basin_module.f90#bsn_prm]]
<!-- USER-NOTES-END -->
