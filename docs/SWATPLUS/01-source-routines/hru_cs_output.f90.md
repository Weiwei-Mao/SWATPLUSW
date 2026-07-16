---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: hru_cs_output.f90
note_file: hru_cs_output.f90
subroutine: hru_cs_output
module:
  - time_module
  - basin_module
  - hydrograph_module
  - cs_module
  - constituent_mass_module
calls: []
uses_variables:
  - basin_module.f90#pco
  - constituent_mass_module.f90#cs_db
  - cs_module.f90#hcsb_a
  - cs_module.f90#hcsb_d
  - cs_module.f90#hcsb_m
  - cs_module.f90#hcsb_y
  - hydrograph_module.f90#ob
  - hydrograph_module.f90#sp_ob1
  - time_module.f90#ndays
  - time_module.f90#time
input_variables: []
reads: []
writes: []
purpose: "this subroutine outputs constituent mass loadings and concentrations from HRUs"
---

# hru_cs_output

> [!info] Summary
> this subroutine outputs constituent mass loadings and concentrations from HRUs

## Basic Information
- **Type**: `subroutine`
- **Source file**: `hru_cs_output.f90`
- **Modules used**:
  - [[time_module.f90]]
  - [[basin_module.f90]]
  - [[hydrograph_module.f90]]
  - [[cs_module.f90]]
  - [[constituent_mass_module.f90]]
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
- [[basin_module.f90#pco]] - `basin_print_codes`
- [[constituent_mass_module.f90#cs_db]] - `constituents`
- [[cs_module.f90#hcsb_a]] - `object_cs_balance`
- [[cs_module.f90#hcsb_d]] - `object_cs_balance`
- [[cs_module.f90#hcsb_m]] - `object_cs_balance`
- [[cs_module.f90#hcsb_y]] - `object_cs_balance`
- [[hydrograph_module.f90#ob]] - `object_connectivity`
- [[hydrograph_module.f90#sp_ob1]] - `spatial_objects`
- [[time_module.f90#ndays]] - `integer, dimension (13)`
- [[time_module.f90#time]] - `time_current`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
