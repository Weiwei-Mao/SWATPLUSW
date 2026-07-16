---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: sq_volq.f90
note_file: sq_volq.f90
subroutine: sq_volq
module:
  - basin_module
calls:
  - sq_daycn
  - sq_greenampt
uses_variables:
  - basin_module.f90#bsn_cc
input_variables: []
reads: []
writes: []
purpose: "Call subroutines to calculate the current day\"s CN for the HRU and; to calculate surface runoff"
---

# sq_volq

> [!info] Summary
> Call subroutines to calculate the current day"s CN for the HRU and; to calculate surface runoff

## Basic Information
- **Type**: `subroutine`
- **Source file**: `sq_volq.f90`
- **Modules used**:
  - [[basin_module.f90]]
- **Subroutine calls**: 2 | **Files read**: 0 | **Files written**: 0

## Call Relationships
**This routine calls:**

- [[sq_daycn.f90]]
- [[sq_greenampt.f90]]

**Called by:**

- [[surface.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[basin_module.f90#bsn_cc]] - `basin_control_codes`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
