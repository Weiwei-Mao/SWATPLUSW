---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: obj_output.f90
note_file: obj_output.f90
subroutine: obj_output
module:
  - time_module
  - hydrograph_module
  - soil_module
  - hru_module
  - organic_mineral_mass_module
  - plant_module
calls: []
uses_variables:
  - hru_module.f90#hru
  - hru_module.f90#ihru
  - hru_module.f90#ipl
  - hru_module.f90#mo
  - hydrograph_module.f90#ch_fp_wb
  - hydrograph_module.f90#hd
  - hydrograph_module.f90#jrch
  - hydrograph_module.f90#mobj_out
  - hydrograph_module.f90#ob
  - hydrograph_module.f90#ob_out
  - hydrograph_module.f90#sp_ob
  - organic_mineral_mass_module.f90#mnz
  - organic_mineral_mass_module.f90#mpz
  - organic_mineral_mass_module.f90#orgz
  - organic_mineral_mass_module.f90#pl_mass
  - organic_mineral_mass_module.f90#soil1
  - organic_mineral_mass_module.f90#soil_org_z
  - organic_mineral_mass_module.f90#soil_prof_hact
  - organic_mineral_mass_module.f90#soil_prof_hp
  - organic_mineral_mass_module.f90#soil_prof_hs
  - organic_mineral_mass_module.f90#soil_prof_hsta
  - organic_mineral_mass_module.f90#soil_prof_microb
  - organic_mineral_mass_module.f90#soil_prof_mn
  - organic_mineral_mass_module.f90#soil_prof_mp
  - organic_mineral_mass_module.f90#soil_prof_rsd
  - organic_mineral_mass_module.f90#soil_prof_somc
  - plant_module.f90#pcom
  - soil_module.f90#soil
  - time_module.f90#time
input_variables: []
reads: []
writes: []
purpose: ""
---

# obj_output

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `obj_output.f90`
- **Modules used**:
  - [[time_module.f90]]
  - [[hydrograph_module.f90]]
  - [[soil_module.f90]]
  - [[hru_module.f90]]
  - [[organic_mineral_mass_module.f90]]
  - [[plant_module.f90]]
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
- [[hru_module.f90#hru]] - `hydrologic_response_unit`
- [[hru_module.f90#ihru]] - `integer`
- [[hru_module.f90#ipl]] - `integer`
- [[hru_module.f90#mo]] - `integer`
- [[hydrograph_module.f90#ch_fp_wb]] - `channel_floodplain_water_balance`
- [[hydrograph_module.f90#hd]] - `hyd_output`
- [[hydrograph_module.f90#jrch]] - `integer`
- [[hydrograph_module.f90#mobj_out]] - `integer`
- [[hydrograph_module.f90#ob]] - `object_connectivity`
- [[hydrograph_module.f90#ob_out]] - `object_output`
- [[hydrograph_module.f90#sp_ob]] - `spatial_objects`
- [[organic_mineral_mass_module.f90#mnz]] - `mineral_nitrogen`
- [[organic_mineral_mass_module.f90#mpz]] - `mineral_phosphorus`
- [[organic_mineral_mass_module.f90#orgz]] - `organic_mass`
- [[organic_mineral_mass_module.f90#pl_mass]] - `plant_community_mass`
- [[organic_mineral_mass_module.f90#soil1]] - `soil_profile_mass`
- [[organic_mineral_mass_module.f90#soil_org_z]] - `organic_mass`
- [[organic_mineral_mass_module.f90#soil_prof_hact]] - `organic_mass`
- [[organic_mineral_mass_module.f90#soil_prof_hp]] - `organic_mass`
- [[organic_mineral_mass_module.f90#soil_prof_hs]] - `organic_mass`
- [[organic_mineral_mass_module.f90#soil_prof_hsta]] - `organic_mass`
- [[organic_mineral_mass_module.f90#soil_prof_microb]] - `organic_mass`
- [[organic_mineral_mass_module.f90#soil_prof_mn]] - `mineral_nitrogen`
- [[organic_mineral_mass_module.f90#soil_prof_mp]] - `mineral_phosphorus`
- [[organic_mineral_mass_module.f90#soil_prof_rsd]] - `organic_mass`
- [[organic_mineral_mass_module.f90#soil_prof_somc]] - `organic_mass`
- [[plant_module.f90#pcom]] - `plant_community`
- [[soil_module.f90#soil]] - `soil_profile`
- [[time_module.f90#time]] - `time_current`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
