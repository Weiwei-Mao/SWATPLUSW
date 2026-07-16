---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: nut_nminrl.f90
note_file: nut_nminrl.f90
subroutine: nut_nminrl
module:
  - septic_data_module
  - basin_module
  - organic_mineral_mass_module
  - hru_module
  - soil_module
  - plant_module
  - plant_data_module
  - output_landscape_module
calls: []
uses_variables:
  - basin_module.f90#bsn_prm
  - hru_module.f90#hru
  - hru_module.f90#i_sep
  - hru_module.f90#ihru
  - hru_module.f90#ipl
  - hru_module.f90#isep
  - organic_mineral_mass_module.f90#decomp
  - organic_mineral_mass_module.f90#soil1
  - output_landscape_module.f90#hnb_d
  - plant_data_module.f90#pldb
  - plant_module.f90#pcom
  - septic_data_module.f90#sep
  - soil_module.f90#soil
input_variables: []
reads: []
writes: []
purpose: "this subroutine estimates daily nitrogen and phosphorus; mineralization and immobilization considering fresh organic; material (plant residue) and active and stable humus material"
---

# nut_nminrl

> [!info] Summary
> this subroutine estimates daily nitrogen and phosphorus; mineralization and immobilization considering fresh organic; material (plant residue) and active and stable humus material

## Basic Information
- **Type**: `subroutine`
- **Source file**: `nut_nminrl.f90`
- **Modules used**:
  - [[septic_data_module.f90]]
  - [[basin_module.f90]]
  - [[organic_mineral_mass_module.f90]]
  - [[hru_module.f90]]
  - [[soil_module.f90]]
  - [[plant_module.f90]]
  - [[plant_data_module.f90]]
  - [[output_landscape_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 0 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by:**

- [[hru_control.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[basin_module.f90#bsn_prm]] - `basin_parms`
- [[hru_module.f90#hru]] - `hydrologic_response_unit`
- [[hru_module.f90#i_sep]] - `integer, dimension (:), allocatable`
- [[hru_module.f90#ihru]] - `integer`
- [[hru_module.f90#ipl]] - `integer`
- [[hru_module.f90#isep]] - `integer`
- [[organic_mineral_mass_module.f90#decomp]] - `organic_mass`
- [[organic_mineral_mass_module.f90#soil1]] - `soil_profile_mass`
- [[output_landscape_module.f90#hnb_d]] - `output_nutbal`
- [[plant_data_module.f90#pldb]] - `plant_db`
- [[plant_module.f90#pcom]] - `plant_community`
- [[septic_data_module.f90#sep]] - `septic_system`
- [[soil_module.f90#soil]] - `soil_profile`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
