---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: aqu_cs_output.f90
note_file: aqu_cs_output.f90
subroutine: aqu_cs_output
module:
  - time_module
  - basin_module
  - aquifer_module
  - hydrograph_module
  - cs_aquifer
  - constituent_mass_module
calls: []
uses_variables:
  - basin_module.f90#pco
  - constituent_mass_module.f90#cs_aqu
  - constituent_mass_module.f90#cs_db
  - cs_aquifer.f90#acsb_a
  - cs_aquifer.f90#acsb_d
  - cs_aquifer.f90#acsb_m
  - cs_aquifer.f90#acsb_y
  - hydrograph_module.f90#aqu
  - hydrograph_module.f90#ob
  - hydrograph_module.f90#sp_ob1
  - time_module.f90#ndays
  - time_module.f90#time
input_variables: []
reads: []
writes: []
purpose: "this subroutine outputs constituent mass loadings and concentrations in aquifers"
---

# aqu_cs_output

> [!info] Summary
> this subroutine outputs constituent mass loadings and concentrations in aquifers

## Basic Information
- **Type**: `subroutine`
- **Source file**: `aqu_cs_output.f90`
- **Modules used**:
  - [[time_module.f90]]
  - [[basin_module.f90]]
  - [[aquifer_module.f90]]
  - [[hydrograph_module.f90]]
  - [[cs_aquifer.f90]]
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
- [[constituent_mass_module.f90#cs_aqu]] - `constituent_mass`
- [[constituent_mass_module.f90#cs_db]] - `constituents`
- [[cs_aquifer.f90#acsb_a]] - `object_cs_balance_aqu`
- [[cs_aquifer.f90#acsb_d]] - `object_cs_balance_aqu`
- [[cs_aquifer.f90#acsb_m]] - `object_cs_balance_aqu`
- [[cs_aquifer.f90#acsb_y]] - `object_cs_balance_aqu`
- [[hydrograph_module.f90#aqu]] - `hyd_output`
- [[hydrograph_module.f90#ob]] - `object_connectivity`
- [[hydrograph_module.f90#sp_ob1]] - `spatial_objects`
- [[time_module.f90#ndays]] - `integer, dimension (13)`
- [[time_module.f90#time]] - `time_current`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
