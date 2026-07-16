---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: soil_awc_init.f90
note_file: soil_awc_init.f90
subroutine: soil_awc_init
module:
  - soil_module
  - basin_module
  - time_module
calls: []
reads: []
writes: []
purpose: "this subroutine initializes soil parameters based on awc"
---

# soil_awc_init

> [!info] Summary
> this subroutine initializes soil parameters based on awc

## Basic Information
- **Type**: `subroutine`
- **Source file**: `soil_awc_init.f90`
- **Modules used**: [[soil_module.f90]], [[basin_module.f90]], [[time_module.f90]]
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
