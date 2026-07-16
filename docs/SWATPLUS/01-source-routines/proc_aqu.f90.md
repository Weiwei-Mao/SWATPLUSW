---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: proc_aqu.f90
note_file: proc_aqu.f90
subroutine: proc_aqu
module:
  - hydrograph_module
calls:
  - aqu_read
  - aqu_initial
  - aqu_read_init
  - aqu_read_init_cs
reads: []
writes: []
purpose: ""
---

# proc_aqu

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `proc_aqu.f90`
- **Modules used**: [[hydrograph_module.f90]]
- **Subroutine calls**: 4 | **Files read**: 0 | **Files written**: 0

## Call Relationships
**This routine calls:**

- [[aqu_read.f90]]
- [[aqu_initial.f90]]
- [[aqu_read_init.f90]]
- [[aqu_read_init_cs.f90]]

**Called by** (live Dataview back-query):

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
