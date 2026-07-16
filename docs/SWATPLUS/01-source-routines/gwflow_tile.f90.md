---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: gwflow_tile.f90
note_file: gwflow_tile.f90
subroutine: gwflow_tile
module:
  - gwflow_module
  - hydrograph_module
  - constituent_mass_module
calls: []
reads: []
writes: []
purpose: "this subroutine calculates the water exchange volume between irrigation canals and connected grid cells; (exchange volumes are used in gwflow_simulate, in groundwater balance equations)"
---

# gwflow_tile

> [!info] Summary
> this subroutine calculates the water exchange volume between irrigation canals and connected grid cells; (exchange volumes are used in gwflow_simulate, in groundwater balance equations)

## Basic Information
- **Type**: `subroutine`
- **Source file**: `gwflow_tile.f90`
- **Modules used**: [[gwflow_module.f90]], [[hydrograph_module.f90]], [[constituent_mass_module.f90]]
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
