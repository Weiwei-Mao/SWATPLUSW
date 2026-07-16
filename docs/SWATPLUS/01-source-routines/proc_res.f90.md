---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: proc_res.f90
note_file: proc_res.f90
subroutine: proc_res
module:
  - hydrograph_module
calls:
  - res_read_hyd
  - res_read_sed
  - res_read_nut
  - res_read_init
  - res_read_saltdb
  - res_read_csdb
  - res_read_conds
  - res_allo
  - res_objects
  - res_read
  - res_read_salt_cs
  - res_initial
reads: []
writes: []
purpose: ""
---

# proc_res

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `proc_res.f90`
- **Modules used**: [[hydrograph_module.f90]]
- **Subroutine calls**: 12 | **Files read**: 0 | **Files written**: 0

## Call Relationships
**This routine calls:**

- [[res_read_hyd.f90]]
- [[res_read_sed.f90]]
- [[res_read_nut.f90]]
- [[res_read_init.f90]]
- [[res_read_saltdb.f90]]
- [[res_read_csdb.f90]]
- [[res_read_conds.f90]]
- [[res_allo.f90]]
- [[res_objects.f90]]
- [[res_read.f90]]
- [[res_read_salt_cs.f90]]
- [[res_initial.f90]]

**Called by** (live Dataview back-query):

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
