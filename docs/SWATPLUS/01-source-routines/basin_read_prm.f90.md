---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: basin_read_prm.f90
note_file: basin_read_prm.f90
subroutine: basin_read_prm
module:
  - input_file_module
  - basin_module
calls: []
uses_variables:
  - basin_module.f90#bsn_prm
  - input_file_module.f90#in_basin
input_variables:
  - basin_module.f90#bsn_prm
reads:
  - in_basin%parms_bas
writes: []
purpose: ""
---

# basin_read_prm

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `basin_read_prm.f90`
- **Modules used**:
  - [[input_file_module.f90]]
  - [[basin_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 1 | **Files written**: 0

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
- [[input_file_module.f90#in_basin]] - `input_basin`

**Populated by file reads:**

- [[basin_module.f90#bsn_prm]]

## File I/O
- **Reads**:
  - [[parameters.bsn]]

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
- Read input file [[parameters.bsn]], from variable *[[input_file_module.f90#in_basin]]* get the file name
	- Read variable *[[basin_module.f90#bsn_prm]]
- End
<!-- USER-NOTES-END -->
