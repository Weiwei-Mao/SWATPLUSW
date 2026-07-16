---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: cs_sorb_hru.f90
note_file: cs_sorb_hru.f90
subroutine: cs_sorb_hru
module:
  - hru_module
  - soil_module
  - organic_mineral_mass_module
  - constituent_mass_module
  - cs_module
  - cs_data_module
calls: []
uses_variables:
  - constituent_mass_module.f90#cs_soil
  - cs_data_module.f90#cs_rct_soil
  - cs_module.f90#hcsb_d
  - hru_module.f90#hru
  - hru_module.f90#ihru
  - soil_module.f90#soil
input_variables: []
reads: []
writes: []
purpose: "this subroutine updates constituent concentrations based on sorption in the soil profile"
---

# cs_sorb_hru

> [!info] Summary
> this subroutine updates constituent concentrations based on sorption in the soil profile

## Basic Information
- **Type**: `subroutine`
- **Source file**: `cs_sorb_hru.f90`
- **Modules used**:
  - [[hru_module.f90]]
  - [[soil_module.f90]]
  - [[organic_mineral_mass_module.f90]]
  - [[constituent_mass_module.f90]]
  - [[cs_module.f90]]
  - [[cs_data_module.f90]]
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
- [[constituent_mass_module.f90#cs_soil]] - `soil_constituent_mass`
- [[cs_data_module.f90#cs_rct_soil]] - `constituent_rct`
- [[cs_module.f90#hcsb_d]] - `object_cs_balance`
- [[hru_module.f90#hru]] - `hydrologic_response_unit`
- [[hru_module.f90#ihru]] - `integer`
- [[soil_module.f90#soil]] - `soil_profile`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
