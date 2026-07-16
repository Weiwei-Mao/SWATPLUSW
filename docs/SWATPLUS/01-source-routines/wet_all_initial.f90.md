---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: wet_all_initial.f90
note_file: wet_all_initial.f90
subroutine: wet_all_initial
module:
  - hru_module
  - hydrograph_module
calls:
  - wet_initial
reads: []
writes: []
purpose: ""
---

# wet_all_initial

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `wet_all_initial.f90`
- **Modules used**: [[hru_module.f90]], [[hydrograph_module.f90]]
- **Subroutine calls**: 1 | **Files read**: 0 | **Files written**: 0

## Call Relationships
**This routine calls:**

- [[wet_initial.f90]]

**Called by** (live Dataview back-query):

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
