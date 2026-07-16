---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: wallo_canal.f90
note_file: wallo_canal.f90
subroutine: wallo_canal
module:
  - water_allocation_module
  - hydrograph_module
  - constituent_mass_module
  - basin_module
  - aquifer_module
  - gwflow_module
calls: []
reads: []
writes: []
purpose: "Routes water through a wallo canal: computes outflow, applies loss,; and distributes canal seepage to aquifer (gwflow grid cells or 1-D aquifer)."
---

# wallo_canal

> [!info] Summary
> Routes water through a wallo canal: computes outflow, applies loss,; and distributes canal seepage to aquifer (gwflow grid cells or 1-D aquifer).

## Basic Information
- **Type**: `subroutine`
- **Source file**: `wallo_canal.f90`
- **Modules used**: [[water_allocation_module.f90]], [[hydrograph_module.f90]], [[constituent_mass_module.f90]], [[basin_module.f90]], [[aquifer_module.f90]], [[gwflow_module.f90]]
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
