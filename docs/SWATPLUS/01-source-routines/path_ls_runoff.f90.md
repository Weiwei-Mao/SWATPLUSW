---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: path_ls_runoff.f90
note_file: path_ls_runoff.f90
subroutine: path_ls_runoff
module:
  - pathogen_data_module
  - constituent_mass_module
  - output_ls_pathogen_module
  - hru_module
  - soil_module
calls: []
uses_variables:
  - constituent_mass_module.f90#cs_db
  - constituent_mass_module.f90#cs_soil
  - hru_module.f90#enratio
  - hru_module.f90#hru
  - hru_module.f90#ihru
  - hru_module.f90#qday
  - hru_module.f90#sedyld
  - hru_module.f90#sol_plt_ini
  - output_ls_pathogen_module.f90#hpath_bal
  - pathogen_data_module.f90#path_db
  - soil_module.f90#soil
input_variables: []
reads: []
writes: []
purpose: ""
---

# path_ls_runoff

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `path_ls_runoff.f90`
- **Modules used**:
  - [[pathogen_data_module.f90]]
  - [[constituent_mass_module.f90]]
  - [[output_ls_pathogen_module.f90]]
  - [[hru_module.f90]]
  - [[soil_module.f90]]
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
- [[constituent_mass_module.f90#cs_db]] - `constituents`
- [[constituent_mass_module.f90#cs_soil]] - `soil_constituent_mass`
- [[hru_module.f90#enratio]] - `real`
- [[hru_module.f90#hru]] - `hydrologic_response_unit`
- [[hru_module.f90#ihru]] - `integer`
- [[hru_module.f90#qday]] - `real`
- [[hru_module.f90#sedyld]] - `real, dimension (:), allocatable`
- [[hru_module.f90#sol_plt_ini]] - `soil_plant_initialize`
- [[output_ls_pathogen_module.f90#hpath_bal]] - `object_pathogen_balance`
- [[pathogen_data_module.f90#path_db]] - `pathogen_db`
- [[soil_module.f90#soil]] - `soil_profile`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
