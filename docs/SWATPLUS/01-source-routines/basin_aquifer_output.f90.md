---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: basin_aquifer_output.f90
note_file: basin_aquifer_output.f90
subroutine: basin_aquifer_output
module:
  - time_module
  - basin_module
  - aquifer_module
  - calibration_data_module
  - hydrograph_module
calls: []
uses_variables:
  - aquifer_module.f90#aqu_d
  - aquifer_module.f90#aqu_prm
  - aquifer_module.f90#aquz
  - aquifer_module.f90#baqu_a
  - aquifer_module.f90#baqu_d
  - aquifer_module.f90#baqu_m
  - aquifer_module.f90#baqu_y
  - basin_module.f90#bsn
  - basin_module.f90#pco
  - hydrograph_module.f90#aqu
  - hydrograph_module.f90#sp_ob
  - time_module.f90#ndays
  - time_module.f90#time
input_variables: []
reads: []
writes: []
purpose: ""
---

# basin_aquifer_output

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `basin_aquifer_output.f90`
- **Modules used**:
  - [[time_module.f90]]
  - [[basin_module.f90]]
  - [[aquifer_module.f90]]
  - [[calibration_data_module.f90]]
  - [[hydrograph_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 0 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by:**

- [[command.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[aquifer_module.f90#aqu_d]] - `aquifer_dynamic`
- [[aquifer_module.f90#aqu_prm]] - `aquifer_data_parameters`
- [[aquifer_module.f90#aquz]] - `aquifer_dynamic`
- [[aquifer_module.f90#baqu_a]] - `aquifer_dynamic`
- [[aquifer_module.f90#baqu_d]] - `aquifer_dynamic`
- [[aquifer_module.f90#baqu_m]] - `aquifer_dynamic`
- [[aquifer_module.f90#baqu_y]] - `aquifer_dynamic`
- [[basin_module.f90#bsn]] - `basin_inputs`
- [[basin_module.f90#pco]] - `basin_print_codes`
- [[hydrograph_module.f90#aqu]] - `hyd_output`
- [[hydrograph_module.f90#sp_ob]] - `spatial_objects`
- [[time_module.f90#ndays]] - `integer, dimension (13)`
- [[time_module.f90#time]] - `time_current`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
