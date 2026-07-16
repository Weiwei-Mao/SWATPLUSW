---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: mgt_read_sweepops.f90
note_file: mgt_read_sweepops.f90
subroutine: mgt_read_sweepops
module:
  - input_file_module
  - maximum_data_module
  - mgt_operations_module
calls: []
reads:
  - in_ops%sweep_ops
writes: []
purpose: ""
---

# mgt_read_sweepops

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `mgt_read_sweepops.f90`
- **Modules used**: [[input_file_module.f90]], [[maximum_data_module.f90]], [[mgt_operations_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 1 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by** (live Dataview back-query):

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## File I/O
- **Reads**: `in_ops%sweep_ops` _(variable; see file.cio)_

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
