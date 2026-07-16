---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: mgt_newtillmix_wet.f90
note_file: mgt_newtillmix_wet.f90
subroutine: mgt_newtillmix_wet
module:
  - tillage_data_module
  - basin_module
  - organic_mineral_mass_module
  - hru_module
  - soil_module
  - constituent_mass_module
  - plant_module
  - reservoir_module
  - hydrograph_module
calls: []
uses_variables:
  - basin_module.f90#bsn_cc
  - constituent_mass_module.f90#cs_db
  - constituent_mass_module.f90#cs_soil
  - hru_module.f90#hru
  - hydrograph_module.f90#wet
  - organic_mineral_mass_module.f90#soil1
  - reservoir_module.f90#wet_ob
  - soil_module.f90#soil
  - tillage_data_module.f90#tilldb
input_variables: []
reads: []
writes: []
purpose: "this subroutine mixes residue and nutrients in soil layers and ponding water during tillage"
---

# mgt_newtillmix_wet

> [!info] Summary
> this subroutine mixes residue and nutrients in soil layers and ponding water during tillage

## Basic Information
- **Type**: `subroutine`
- **Source file**: `mgt_newtillmix_wet.f90`
- **Modules used**:
  - [[tillage_data_module.f90]]
  - [[basin_module.f90]]
  - [[organic_mineral_mass_module.f90]]
  - [[hru_module.f90]]
  - [[soil_module.f90]]
  - [[constituent_mass_module.f90]]
  - [[plant_module.f90]]
  - [[reservoir_module.f90]]
  - [[hydrograph_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 0 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by:**

- [[actions.f90]]
- [[mgt_sched.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[basin_module.f90#bsn_cc]] - `basin_control_codes`
- [[constituent_mass_module.f90#cs_db]] - `constituents`
- [[constituent_mass_module.f90#cs_soil]] - `soil_constituent_mass`
- [[hru_module.f90#hru]] - `hydrologic_response_unit`
- [[hydrograph_module.f90#wet]] - `hyd_output`
- [[organic_mineral_mass_module.f90#soil1]] - `soil_profile_mass`
- [[reservoir_module.f90#wet_ob]] - `wetland`
- [[soil_module.f90#soil]] - `soil_profile`
- [[tillage_data_module.f90#tilldb]] - `tillage_db`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
