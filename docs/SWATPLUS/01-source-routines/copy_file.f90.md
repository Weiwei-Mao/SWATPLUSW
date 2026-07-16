---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: copy_file.f90
note_file: copy_file.f90
subroutine: copy_file
module: []
calls: []
reads:
  - source
writes:
  - destination
purpose: ""
---

# copy_file

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `copy_file.f90`
- **Modules used**: -
- **Subroutine calls**: 0 | **Files read**: 1 | **Files written**: 1

## Call Relationships
(No call statements; leaf node.)

**Called by** (live Dataview back-query):

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## File I/O
- **Writes**: `destination`
- **Reads**: `source` _(variable; see file.cio)_

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
