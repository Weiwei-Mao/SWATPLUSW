---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: theta.f90
note_file: theta.f90
subroutine: theta
module: []
calls: []
reads: []
writes: []
purpose: "this function corrects rate constants for temperature; Equation is III-52 from QUAL2E"
---

# theta

> [!info] Summary
> this function corrects rate constants for temperature; Equation is III-52 from QUAL2E

## Basic Information
- **Type**: `subroutine`
- **Source file**: `theta.f90`
- **Modules used**: -
- **Subroutine calls**: 0 | **Files read**: 0 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by** (live Dataview back-query):

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
