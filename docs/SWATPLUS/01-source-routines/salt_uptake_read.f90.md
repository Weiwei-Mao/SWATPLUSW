---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: salt_uptake_read.f90
note_file: salt_uptake_read.f90
subroutine: salt_uptake_read
module:
  - basin_module
  - input_file_module
  - climate_module
  - time_module
  - maximum_data_module
  - constituent_mass_module
  - hydrograph_module
  - salt_module
calls: []
uses_variables:
  - constituent_mass_module.f90#cs_db
  - maximum_data_module.f90#db_mx
  - salt_module.f90#salt_uptake_kg
  - salt_module.f90#salt_uptake_on
input_variables: []
reads:
  - salt_uptake
writes: []
purpose: ""
---

# salt_uptake_read

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `salt_uptake_read.f90`
- **Modules used**:
  - [[basin_module.f90]]
  - [[input_file_module.f90]]
  - [[climate_module.f90]]
  - [[time_module.f90]]
  - [[maximum_data_module.f90]]
  - [[constituent_mass_module.f90]]
  - [[hydrograph_module.f90]]
  - [[salt_module.f90]]
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
- [[constituent_mass_module.f90#cs_db]] - `constituents`
- [[maximum_data_module.f90#db_mx]] - `data_files_max_elements`
- [[salt_module.f90#salt_uptake_kg]] - `real, dimension(:,:), allocatable`
- [[salt_module.f90#salt_uptake_on]] - `integer`

## File I/O
- **Reads**:
  - `salt_uptake` _(variable; see [[file.cio]])_

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
