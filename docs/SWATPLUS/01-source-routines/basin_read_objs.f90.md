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
uses_variables:
  - basin_module.f90#bsn
  - basin_module.f90#bsn_cc
  - constituent_mass_module.f90#obcs
  - constituent_mass_module.f90#obcs_alloc
  - gwflow_module.f90#out_gw
  - hydrograph_module.f90#aqu
  - hydrograph_module.f90#ob
  - hydrograph_module.f90#sp_ob
  - input_file_module.f90#in_con
  - input_file_module.f90#in_sim
  - organic_mineral_mass_module.f90#obom
input_variables:
  - basin_module.f90#bsn
  - hydrograph_module.f90#sp_ob
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
- **Modules used**:
  - [[hydrograph_module.f90]]
  - [[input_file_module.f90]]
  - [[organic_mineral_mass_module.f90]]
  - [[constituent_mass_module.f90]]
  - [[basin_module.f90]]
  - [[gwflow_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 3 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by:**

- [[proc_bsn.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[basin_module.f90#bsn]] - `basin_inputs`
- [[basin_module.f90#bsn_cc]] - `basin_control_codes`
- [[constituent_mass_module.f90#obcs]] - `all_constituent_hydrograph`
- [[constituent_mass_module.f90#obcs_alloc]] - `integer, dimension (:), allocatable`
- [[gwflow_module.f90#out_gw]] - `integer`
- [[hydrograph_module.f90#aqu]] - `hyd_output`
- [[hydrograph_module.f90#ob]] - `object_connectivity`
- [[hydrograph_module.f90#sp_ob]] - `spatial_objects`
- [[input_file_module.f90#in_con]] - `input_con`
- [[input_file_module.f90#in_sim]] - `input_sim`
- [[organic_mineral_mass_module.f90#obom]] - `spatial_object_hydrographs`

**Populated by file reads:**

- [[basin_module.f90#bsn]]
- [[hydrograph_module.f90#sp_ob]]

## File I/O
- **Reads**:
  - [[object.cnt]]
  - [[chancell.gw]]
  - `gwflow_record` _(variable; see [[file.cio]])_

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.

- Line 24-43, Read input file[[object.cnt]], from variable *[[input_file_module.f90#in_sim]]* get the file name
	- Read variable *[[basin_module.f90#bsn]]*, first 3 parameters
	- Read variable *[[hydrograph_module.f90#sp_ob]]*, other parameters
- Line 45-88, if gwflow is open
- Line 91-95, allocation of variables
- End
<!-- USER-NOTES-END -->
