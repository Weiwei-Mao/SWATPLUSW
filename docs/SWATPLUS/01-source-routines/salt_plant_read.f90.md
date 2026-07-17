---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: salt_plant_read.f90
note_file: salt_plant_read.f90
subroutine: salt_plant_read
module:
  - constituent_mass_module
  - input_file_module
  - maximum_data_module
  - salt_data_module
calls: []
uses_variables:
  - maximum_data_module.f90#db_mx
  - salt_data_module.f90#salt_effect
  - salt_data_module.f90#salt_soil_type
  - salt_data_module.f90#salt_stress_a
  - salt_data_module.f90#salt_stress_b
  - salt_data_module.f90#salt_tds_ec
  - salt_data_module.f90#salt_tol_sim
input_variables:
  - salt_data_module.f90#salt_effect
  - salt_data_module.f90#salt_soil_type
  - salt_data_module.f90#salt_stress_a
  - salt_data_module.f90#salt_stress_b
  - salt_data_module.f90#salt_tds_ec
  - salt_data_module.f90#salt_tol_sim
reads:
  - salt_plants
writes: []
purpose: ""
---

# salt_plant_read

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `salt_plant_read.f90`
- **Modules used**:
  - [[constituent_mass_module.f90]]
  - [[input_file_module.f90]]
  - [[maximum_data_module.f90]]
  - [[salt_data_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 1 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by:**

- [[proc_read.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[maximum_data_module.f90#db_mx]] - `data_files_max_elements`
- [[salt_data_module.f90#salt_effect]] - `integer`
- [[salt_data_module.f90#salt_soil_type]] - `integer`
- [[salt_data_module.f90#salt_stress_a]] - `real, dimension (:), allocatable`
- [[salt_data_module.f90#salt_stress_b]] - `real, dimension (:), allocatable`
- [[salt_data_module.f90#salt_tds_ec]] - `real`
- [[salt_data_module.f90#salt_tol_sim]] - `integer`

**Populated by file reads:**

- [[salt_data_module.f90#salt_effect]]
- [[salt_data_module.f90#salt_soil_type]]
- [[salt_data_module.f90#salt_stress_a]]
- [[salt_data_module.f90#salt_stress_b]]
- [[salt_data_module.f90#salt_tds_ec]]
- [[salt_data_module.f90#salt_tol_sim]]

## File I/O
- **Reads**:
  - [[salt_plants]]

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
