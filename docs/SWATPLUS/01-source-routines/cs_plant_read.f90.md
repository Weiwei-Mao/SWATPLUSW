---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: cs_plant_read.f90
note_file: cs_plant_read.f90
subroutine: cs_plant_read
module:
  - constituent_mass_module
  - input_file_module
  - maximum_data_module
  - cs_data_module
calls: []
uses_variables:
  - cs_data_module.f90#bor_stress_a
  - cs_data_module.f90#bor_stress_b
  - cs_data_module.f90#bor_tol_sim
  - maximum_data_module.f90#db_mx
input_variables:
  - cs_data_module.f90#bor_stress_a
  - cs_data_module.f90#bor_stress_b
  - cs_data_module.f90#bor_tol_sim
reads:
  - cs_plants_boron
writes: []
purpose: ""
---

# cs_plant_read

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `cs_plant_read.f90`
- **Modules used**:
  - [[constituent_mass_module.f90]]
  - [[input_file_module.f90]]
  - [[maximum_data_module.f90]]
  - [[cs_data_module.f90]]
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
- [[cs_data_module.f90#bor_stress_a]] - `real, dimension (:), allocatable`
- [[cs_data_module.f90#bor_stress_b]] - `real, dimension (:), allocatable`
- [[cs_data_module.f90#bor_tol_sim]] - `integer`
- [[maximum_data_module.f90#db_mx]] - `data_files_max_elements`

**Populated by file reads:**

- [[cs_data_module.f90#bor_stress_a]]
- [[cs_data_module.f90#bor_stress_b]]
- [[cs_data_module.f90#bor_tol_sim]]

## File I/O
- **Reads**:
  - [[cs_plants_boron]]

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
