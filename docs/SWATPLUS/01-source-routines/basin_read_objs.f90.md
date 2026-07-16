---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: basin_read_objs.f90
note_file: basin_read_objs.f90
subroutine: basin_read_objs
module:
  - hydrograph_module
  - input_file_module
  - organic_mineral_mass_module
  - constituent_mass_module
  - basin_module
  - gwflow_module
calls: []
reads:
  - in_sim%object_cnt
  - chancell.gw
  - gwflow_record
writes: []
purpose: "reads in the routing information from the watershed configuration; input file (.fig) and calculates the number of subbasins, reaches,; and reservoirs"
---

# basin_read_objs

> [!info] Summary
> reads in the routing information from the watershed configuration; input file (.fig) and calculates the number of subbasins, reaches,; and reservoirs

## Basic Information
- **Type**: `subroutine`
- **Source file**: `basin_read_objs.f90`
- **Modules used**: [[hydrograph_module.f90]], [[input_file_module.f90]], [[organic_mineral_mass_module.f90]], [[constituent_mass_module.f90]], [[basin_module.f90]], [[gwflow_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 3 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by** (live Dataview back-query):

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## File I/O
- **Reads**: `in_sim%object_cnt` _(variable; see file.cio)_, `chancell.gw`, `gwflow_record` _(variable; see file.cio)_

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
