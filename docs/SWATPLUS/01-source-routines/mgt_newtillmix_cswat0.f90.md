---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: mgt_newtillmix_cswat0.f90
note_file: mgt_newtillmix_cswat0.f90
subroutine: mgt_newtillmix_cswat0
module:
  - tillage_data_module
  - basin_module
  - organic_mineral_mass_module
  - hru_module
  - soil_module
  - constituent_mass_module
  - plant_module
calls: []
uses_variables:
  - constituent_mass_module.f90#cs_db
  - hru_module.f90#ipl
  - hru_module.f90#tillage_days
  - hru_module.f90#tillage_depth
  - hru_module.f90#tillage_switch
  - organic_mineral_mass_module.f90#mix_mn
  - organic_mineral_mass_module.f90#mix_mp
  - organic_mineral_mass_module.f90#mix_org
  - organic_mineral_mass_module.f90#mnz
  - organic_mineral_mass_module.f90#mpz
  - organic_mineral_mass_module.f90#orgz
  - organic_mineral_mass_module.f90#pl_mass
  - organic_mineral_mass_module.f90#soil1
  - plant_module.f90#pcom
  - soil_module.f90#soil
  - tillage_data_module.f90#tilldb
input_variables: []
reads: []
writes: []
purpose: "this subroutine mixes residue and nutrients during tillage and; biological mixing; New version developed by Armen R. Kemanian in collaboration with Stefan Julich and Cole Rossi"
---

# mgt_newtillmix_cswat0

> [!info] Summary
> this subroutine mixes residue and nutrients during tillage and; biological mixing; New version developed by Armen R. Kemanian in collaboration with Stefan Julich and Cole Rossi

## Basic Information
- **Type**: `subroutine`
- **Source file**: `mgt_newtillmix_cswat0.f90`
- **Modules used**:
  - [[tillage_data_module.f90]]
  - [[basin_module.f90]]
  - [[organic_mineral_mass_module.f90]]
  - [[hru_module.f90]]
  - [[soil_module.f90]]
  - [[constituent_mass_module.f90]]
  - [[plant_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 0 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by:**

- [[actions.f90]]
- [[mgt_sched.f90]]
- [[time_control.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[constituent_mass_module.f90#cs_db]] - `constituents`
- [[hru_module.f90#ipl]] - `integer`
- [[hru_module.f90#tillage_days]] - `integer, dimension(:), allocatable`
- [[hru_module.f90#tillage_depth]] - `real, dimension(:), allocatable`
- [[hru_module.f90#tillage_switch]] - `integer, dimension(:), allocatable`
- [[organic_mineral_mass_module.f90#mix_mn]] - `mineral_nitrogen`
- [[organic_mineral_mass_module.f90#mix_mp]] - `mineral_phosphorus`
- [[organic_mineral_mass_module.f90#mix_org]] - `organic_mixing_mass`
- [[organic_mineral_mass_module.f90#mnz]] - `mineral_nitrogen`
- [[organic_mineral_mass_module.f90#mpz]] - `mineral_phosphorus`
- [[organic_mineral_mass_module.f90#orgz]] - `organic_mass`
- [[organic_mineral_mass_module.f90#pl_mass]] - `plant_community_mass`
- [[organic_mineral_mass_module.f90#soil1]] - `soil_profile_mass`
- [[plant_module.f90#pcom]] - `plant_community`
- [[soil_module.f90#soil]] - `soil_profile`
- [[tillage_data_module.f90#tilldb]] - `tillage_db`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
