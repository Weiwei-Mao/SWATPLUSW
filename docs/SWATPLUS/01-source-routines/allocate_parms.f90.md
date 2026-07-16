---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: allocate_parms.f90
note_file: allocate_parms.f90
subroutine: allocate_parms
module:
  - hru_module
  - time_module
  - hydrograph_module
  - constituent_mass_module
calls:
  - zero0
  - zero1
  - zero2
  - zeroini
reads: []
writes: []
purpose: "this subroutine allocates array sizes"
---

# allocate_parms

> [!info] Summary
> this subroutine allocates array sizes

## Basic Information
- **Type**: `subroutine`
- **Source file**: `allocate_parms.f90`
- **Modules used**: [[hru_module.f90]], [[time_module.f90]], [[hydrograph_module.f90]], [[constituent_mass_module.f90]]
- **Subroutine calls**: 4 | **Files read**: 0 | **Files written**: 0

## Call Relationships
**This routine calls:**

- [[zero0.f90]]
- [[zero1.f90]]
- [[zero2.f90]]
- [[zeroini.f90]]

**Called by** (live Dataview back-query):

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
