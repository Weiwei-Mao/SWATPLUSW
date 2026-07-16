---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: header_aquifer.f90
note_file: header_aquifer.f90
subroutine: header_aquifer
module:
  - aquifer_module
  - basin_module
  - hydrograph_module
  - output_path_module
calls:
  - open_output_file
reads: []
writes: []
purpose: ""
---

# header_aquifer

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `header_aquifer.f90`
- **Modules used**: [[aquifer_module.f90]], [[basin_module.f90]], [[hydrograph_module.f90]], [[output_path_module.f90]]
- **Subroutine calls**: 1 | **Files read**: 0 | **Files written**: 0

## Call Relationships
**This routine calls:**

- `open_output_file`

**Called by** (live Dataview back-query):

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
