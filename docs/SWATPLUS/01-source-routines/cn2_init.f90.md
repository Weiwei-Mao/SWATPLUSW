---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: cn2_init.f90
note_file: cn2_init.f90
subroutine: cn2_init
module:
  - hru_module
  - soil_module
  - maximum_data_module
  - landuse_data_module
calls:
  - curno
reads: []
writes: []
purpose: ""
---

# cn2_init

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `cn2_init.f90`
- **Modules used**: [[hru_module.f90]], [[soil_module.f90]], [[maximum_data_module.f90]], [[landuse_data_module.f90]]
- **Subroutine calls**: 1 | **Files read**: 0 | **Files written**: 0

## Call Relationships
**This routine calls:**

- [[curno.f90]]

**Called by** (live Dataview back-query):

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
