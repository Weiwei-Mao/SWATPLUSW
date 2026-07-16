---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: sep_biozone.f90
note_file: sep_biozone.f90
subroutine: sep_biozone
module:
  - septic_data_module
  - basin_module
  - pathogen_data_module
  - organic_mineral_mass_module
  - hru_module
  - soil_module
  - time_module
calls: []
uses_variables:
  - hru_module.f90#bio_bod
  - hru_module.f90#biom
  - hru_module.f90#bz_perc
  - hru_module.f90#fcoli
  - hru_module.f90#hru
  - hru_module.f90#i_sep
  - hru_module.f90#ihru
  - hru_module.f90#isep
  - hru_module.f90#iseptic
  - hru_module.f90#plqm
  - hru_module.f90#qstemm
  - hru_module.f90#rbiom
  - hru_module.f90#sep_tsincefail
  - organic_mineral_mass_module.f90#soil1
  - septic_data_module.f90#sep
  - septic_data_module.f90#sepdb
  - soil_module.f90#soil
input_variables: []
reads: []
writes: []
purpose: "This subroutine conducts biophysical processes occurring; in the biozone layer of a septic HRU."
---

# sep_biozone

> [!info] Summary
> This subroutine conducts biophysical processes occurring; in the biozone layer of a septic HRU.

## Basic Information
- **Type**: `subroutine`
- **Source file**: `sep_biozone.f90`
- **Modules used**:
  - [[septic_data_module.f90]]
  - [[basin_module.f90]]
  - [[pathogen_data_module.f90]]
  - [[organic_mineral_mass_module.f90]]
  - [[hru_module.f90]]
  - [[soil_module.f90]]
  - [[time_module.f90]]
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
- [[hru_module.f90#bio_bod]] - `real, dimension (:), allocatable`
- [[hru_module.f90#biom]] - `real, dimension (:), allocatable`
- [[hru_module.f90#bz_perc]] - `real, dimension (:), allocatable`
- [[hru_module.f90#fcoli]] - `real, dimension (:), allocatable`
- [[hru_module.f90#hru]] - `hydrologic_response_unit`
- [[hru_module.f90#i_sep]] - `integer, dimension (:), allocatable`
- [[hru_module.f90#ihru]] - `integer`
- [[hru_module.f90#isep]] - `integer`
- [[hru_module.f90#iseptic]] - `integer, dimension (:), allocatable`
- [[hru_module.f90#plqm]] - `real, dimension (:), allocatable`
- [[hru_module.f90#qstemm]] - `real, dimension (:), allocatable`
- [[hru_module.f90#rbiom]] - `real, dimension (:), allocatable`
- [[hru_module.f90#sep_tsincefail]] - `integer, dimension (:), allocatable`
- [[organic_mineral_mass_module.f90#soil1]] - `soil_profile_mass`
- [[septic_data_module.f90#sep]] - `septic_system`
- [[septic_data_module.f90#sepdb]] - `septic_db`
- [[soil_module.f90#soil]] - `soil_profile`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
