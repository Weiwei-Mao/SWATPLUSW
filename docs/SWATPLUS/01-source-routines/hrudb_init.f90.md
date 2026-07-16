---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: hrudb_init.f90
note_file: hrudb_init.f90
subroutine: hrudb_init
module:
  - hydrograph_module
  - hru_module
  - landuse_data_module
  - basin_module
calls: []
reads: []
writes: []
purpose: ""
---

# hrudb_init

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `hrudb_init.f90`
- **Modules used**: [[hydrograph_module.f90]], [[hru_module.f90]], [[landuse_data_module.f90]], [[basin_module.f90]]
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
