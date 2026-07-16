---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: recall_salt.f90
note_file: recall_salt.f90
subroutine: recall_salt
module:
  - basin_module
  - hydrograph_module
  - time_module
  - constituent_mass_module
  - ch_salt_module
  - gwflow_module
calls: []
uses_variables:
  - ch_salt_module.f90#chsalt_d
  - constituent_mass_module.f90#ch_water
  - constituent_mass_module.f90#cs_db
  - constituent_mass_module.f90#hin_csz
  - constituent_mass_module.f90#obcs
  - constituent_mass_module.f90#rec_salt
  - constituent_mass_module.f90#recoutsaltb_d
  - constituent_mass_module.f90#recsaltb_d
  - gwflow_module.f90#div_conc_salt
  - hydrograph_module.f90#ch_stor
  - hydrograph_module.f90#hd
  - hydrograph_module.f90#icmd
  - hydrograph_module.f90#ob
  - hydrograph_module.f90#recall
  - time_module.f90#time
input_variables: []
reads: []
writes: []
purpose: ""
---

# recall_salt

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `recall_salt.f90`
- **Modules used**:
  - [[basin_module.f90]]
  - [[hydrograph_module.f90]]
  - [[time_module.f90]]
  - [[constituent_mass_module.f90]]
  - [[ch_salt_module.f90]]
  - [[gwflow_module.f90]]
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
- [[ch_salt_module.f90#chsalt_d]] - `ch_salt_output`
- [[constituent_mass_module.f90#ch_water]] - `constituent_mass`
- [[constituent_mass_module.f90#cs_db]] - `constituents`
- [[constituent_mass_module.f90#hin_csz]] - `constituent_mass`
- [[constituent_mass_module.f90#obcs]] - `all_constituent_hydrograph`
- [[constituent_mass_module.f90#rec_salt]] - `recall_salt_inputs`
- [[constituent_mass_module.f90#recoutsaltb_d]] - `constituent_mass`
- [[constituent_mass_module.f90#recsaltb_d]] - `constituent_mass`
- [[gwflow_module.f90#div_conc_salt]] - `real, allocatable`
- [[hydrograph_module.f90#ch_stor]] - `hyd_output`
- [[hydrograph_module.f90#hd]] - `hyd_output`
- [[hydrograph_module.f90#icmd]] - `integer`
- [[hydrograph_module.f90#ob]] - `object_connectivity`
- [[hydrograph_module.f90#recall]] - `recall_hydrograph_inputs`
- [[time_module.f90#time]] - `time_current`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
