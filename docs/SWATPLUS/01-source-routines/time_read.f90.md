---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: time_read.f90
note_file: time_read.f90
subroutine: time_read
module:
  - time_module
  - input_file_module
calls:
  - xmon
uses_variables:
  - input_file_module.f90#in_sim
  - time_module.f90#time
input_variables:
  - time_module.f90#time
reads:
  - in_sim%time
writes: []
purpose: ""
---

# time_read

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `time_read.f90`
- **Modules used**:
  - [[time_module.f90]]
  - [[input_file_module.f90]]
- **Subroutine calls**: 1 | **Files read**: 1 | **Files written**: 0

## Call Relationships
**This routine calls:**

- [[xmon.f90]]

**Called by:**

- [[proc_bsn.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[input_file_module.f90#in_sim]] - `input_sim`
- [[time_module.f90#time]] - `time_current`

**Populated by file reads:**

- [[time_module.f90#time]]

## File I/O
- **Reads**:
  - [[time.sim]]

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.

- Line 20-43, Read input file [[time.sim]], from variable *[[input_file_module.f90#in_sim]]* get the file name
	- Read variable [[time_module.f90#time]],
		- Day start
		- Year start
		- Day end
		- Year end
		- Time step
- End
<!-- USER-NOTES-END -->
