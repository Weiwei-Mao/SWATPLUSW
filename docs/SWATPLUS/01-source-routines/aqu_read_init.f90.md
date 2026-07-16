---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: aqu_read_init.f90
note_file: aqu_read_init.f90
subroutine: aqu_read_init
module:
  - basin_module
  - input_file_module
  - maximum_data_module
  - aquifer_module
  - aqu_pesticide_module
  - hydrograph_module
  - constituent_mass_module
calls: []
uses_variables:
  - aquifer_module.f90#aqu_init
  - aquifer_module.f90#aqu_init_dat_c
  - hydrograph_module.f90#aqu
  - hydrograph_module.f90#sp_ob
  - input_file_module.f90#in_aqu
  - maximum_data_module.f90#db_mx
input_variables:
  - aquifer_module.f90#aqu_init_dat_c
reads:
  - in_aqu%init
writes: []
purpose: ""
---

# aqu_read_init

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `aqu_read_init.f90`
- **Modules used**:
  - [[basin_module.f90]]
  - [[input_file_module.f90]]
  - [[maximum_data_module.f90]]
  - [[aquifer_module.f90]]
  - [[aqu_pesticide_module.f90]]
  - [[hydrograph_module.f90]]
  - [[constituent_mass_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 1 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by:**

- [[proc_aqu.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[aquifer_module.f90#aqu_init]] - `aquifer_init_data`
- [[aquifer_module.f90#aqu_init_dat_c]] - `aquifer_init_data_char`
- [[hydrograph_module.f90#aqu]] - `hyd_output`
- [[hydrograph_module.f90#sp_ob]] - `spatial_objects`
- [[input_file_module.f90#in_aqu]] - `input_aqu`
- [[maximum_data_module.f90#db_mx]] - `data_files_max_elements`

**Populated by file reads:**

- [[aquifer_module.f90#aqu_init_dat_c]]

## File I/O
- **Reads**:
  - [[initial.aqu]]

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
