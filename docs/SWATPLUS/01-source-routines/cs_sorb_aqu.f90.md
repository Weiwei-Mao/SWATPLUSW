---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: cs_sorb_aqu.f90
note_file: cs_sorb_aqu.f90
subroutine: cs_sorb_aqu
module:
  - hydrograph_module
  - aquifer_module
  - organic_mineral_mass_module
  - constituent_mass_module
  - cs_aquifer
  - cs_data_module
calls: []
uses_variables:
  - aquifer_module.f90#aqu_d
  - aquifer_module.f90#aqu_dat
  - aquifer_module.f90#aqudb
  - constituent_mass_module.f90#cs_aqu
  - cs_aquifer.f90#acsb_d
  - cs_data_module.f90#cs_rct_aqu
  - hydrograph_module.f90#icmd
  - hydrograph_module.f90#ob
input_variables: []
reads: []
writes: []
purpose: "this subroutine updates constituent concentrations based on sorption in the aquifer"
---

# cs_sorb_aqu

> [!info] Summary
> this subroutine updates constituent concentrations based on sorption in the aquifer

## Basic Information
- **Type**: `subroutine`
- **Source file**: `cs_sorb_aqu.f90`
- **Modules used**:
  - [[hydrograph_module.f90]]
  - [[aquifer_module.f90]]
  - [[organic_mineral_mass_module.f90]]
  - [[constituent_mass_module.f90]]
  - [[cs_aquifer.f90]]
  - [[cs_data_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 0 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by:**

- [[aqu_1d_control.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[aquifer_module.f90#aqu_d]] - `aquifer_dynamic`
- [[aquifer_module.f90#aqu_dat]] - `aquifer_database`
- [[aquifer_module.f90#aqudb]] - `aquifer_database`
- [[constituent_mass_module.f90#cs_aqu]] - `constituent_mass`
- [[cs_aquifer.f90#acsb_d]] - `object_cs_balance_aqu`
- [[cs_data_module.f90#cs_rct_aqu]] - `constituent_rct`
- [[hydrograph_module.f90#icmd]] - `integer`
- [[hydrograph_module.f90#ob]] - `object_connectivity`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
