---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: pl_waterup.f90
note_file: pl_waterup.f90
subroutine: pl_waterup
module:
  - plant_data_module
  - basin_module
  - hru_module
  - soil_module
  - plant_module
  - urban_data_module
  - constituent_mass_module
  - salt_data_module
calls:
  - salt_chem_soil_single
uses_variables:
  - constituent_mass_module.f90#cs_db
  - constituent_mass_module.f90#cs_soil
  - hru_module.f90#ep_day
  - hru_module.f90#epmax
  - hru_module.f90#hru
  - hru_module.f90#ihru
  - hru_module.f90#ipl
  - hru_module.f90#luse
  - hru_module.f90#ulu
  - hru_module.f90#uptake
  - plant_data_module.f90#pldb
  - plant_module.f90#pcom
  - salt_data_module.f90#salt_soil_type
  - salt_data_module.f90#salt_stress_a
  - salt_data_module.f90#salt_stress_b
  - salt_data_module.f90#salt_tds_ec
  - salt_data_module.f90#salt_tol_sim
  - salt_data_module.f90#soil_salt_conc
  - soil_module.f90#soil
input_variables: []
reads: []
writes: []
purpose: "this subroutine distributes potential plant evaporation through; the root zone and calculates actual plant water use based on soil; water availability. Also estimates water stress factor."
---

# pl_waterup

> [!info] Summary
> this subroutine distributes potential plant evaporation through; the root zone and calculates actual plant water use based on soil; water availability. Also estimates water stress factor.

## Basic Information
- **Type**: `subroutine`
- **Source file**: `pl_waterup.f90`
- **Modules used**:
  - [[plant_data_module.f90]]
  - [[basin_module.f90]]
  - [[hru_module.f90]]
  - [[soil_module.f90]]
  - [[plant_module.f90]]
  - [[urban_data_module.f90]]
  - [[constituent_mass_module.f90]]
  - [[salt_data_module.f90]]
- **Subroutine calls**: 1 | **Files read**: 0 | **Files written**: 0

## Call Relationships
**This routine calls:**

- [[salt_chem_soil_single.f90]]

**Called by:**

- [[pl_community.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[constituent_mass_module.f90#cs_db]] - `constituents`
- [[constituent_mass_module.f90#cs_soil]] - `soil_constituent_mass`
- [[hru_module.f90#ep_day]] - `real`
- [[hru_module.f90#epmax]] - `real, dimension (:), allocatable`
- [[hru_module.f90#hru]] - `hydrologic_response_unit`
- [[hru_module.f90#ihru]] - `integer`
- [[hru_module.f90#ipl]] - `integer`
- [[hru_module.f90#luse]] - `landuse`
- [[hru_module.f90#ulu]] - `integer`
- [[hru_module.f90#uptake]] - `uptake_parameters`
- [[plant_data_module.f90#pldb]] - `plant_db`
- [[plant_module.f90#pcom]] - `plant_community`
- [[salt_data_module.f90#salt_soil_type]] - `integer`
- [[salt_data_module.f90#salt_stress_a]] - `real, dimension (:), allocatable`
- [[salt_data_module.f90#salt_stress_b]] - `real, dimension (:), allocatable`
- [[salt_data_module.f90#salt_tds_ec]] - `real`
- [[salt_data_module.f90#salt_tol_sim]] - `integer`
- [[salt_data_module.f90#soil_salt_conc]] - `real`
- [[soil_module.f90#soil]] - `soil_profile`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
