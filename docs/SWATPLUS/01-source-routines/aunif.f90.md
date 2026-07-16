---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: aunif.f90
note_file: aunif.f90
subroutine: aunif
module: []
calls: []
reads: []
writes: []
purpose: "This function generates random numbers ranging from 0.0 to 1.0.; In the process of calculating the random number, the seed (x1) is; set to a new value."
---

# aunif

> [!info] Summary
> This function generates random numbers ranging from 0.0 to 1.0.; In the process of calculating the random number, the seed (x1) is; set to a new value.

## Basic Information
- **Type**: `subroutine`
- **Source file**: `aunif.f90`
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
