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
- **Modules used**: [[input_file_module.f90]], [[basin_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 2 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by** (live Dataview back-query):

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## File I/O
- **Reads**: `in_basin%codes_bas` _(variable; see file.cio)_, `pet.cli`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.

- use: `input_file_module`, [[basin_module.f90]]
- Line 13-28: Reads from `codes.bsn`: `bsn_cc`(basin control codes)
- Line 30-40: If `bsn_cc%pet == 3`(input potential evapotranspiration)，checks whether input file `pet.cli` exists
<!-- USER-NOTES-END -->
