---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: basin_read_cc.f90
note_file: basin_read_cc.f90
subroutine: basin_read_cc
module:
  - input_file_module
  - basin_module
calls: []
uses_variables:
  - basin_module.f90#bsn_cc
  - input_file_module.f90#in_basin
input_variables:
  - basin_module.f90#bsn_cc
reads:
  - in_basin%codes_bas
  - pet.cli
writes: []
purpose: ""
---

# basin_read_cc

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `basin_read_cc.f90`
- **Modules used**:
  - [[input_file_module.f90]]
  - [[basin_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 2 | **Files written**: 0

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
- [[basin_module.f90#bsn_cc]] - `basin_control_codes`
- [[input_file_module.f90#in_basin]] - `input_basin`

**Populated by file reads:**

- [[basin_module.f90#bsn_cc]]

## File I/O
- **Reads**:
  - [[codes.bsn]]
  - [[pet.cli]]

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.

- use:
	- [[input_file_module.f90]]
	- [[basin_module.f90]]
- Line 13-28: Reads from
	- [[codes.bsn]]
	- Variable; *[[basin_module.f90#bsn_cc]]*
- Line 30-40: input potential evapotranspiration
	- If *[[basin_module.f90#bsn_cc]]* == 3), checks whether input file [[pet.cli]] exists or not
- End
<!-- USER-NOTES-END -->
