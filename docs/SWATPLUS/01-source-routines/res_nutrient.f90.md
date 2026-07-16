---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: res_nutrient.f90
note_file: res_nutrient.f90
subroutine: res_nutrient
module:
  - reservoir_data_module
  - time_module
  - reservoir_module
  - hydrograph_module
  - climate_module
calls: []
reads: []
writes: []
purpose: ""
---

# res_nutrient

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `res_nutrient.f90`
- **Modules used**: [[reservoir_data_module.f90]], [[time_module.f90]], [[reservoir_module.f90]], [[hydrograph_module.f90]], [[climate_module.f90]]
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
