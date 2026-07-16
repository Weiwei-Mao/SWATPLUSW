---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: water_tower_read.f90
note_file: water_tower_read.f90
subroutine: water_tower_read
module:
  - input_file_module
  - water_allocation_module
  - mgt_operations_module
  - maximum_data_module
  - hydrograph_module
  - constituent_mass_module
calls: []
uses_variables:
  - constituent_mass_module.f90#wtow_cs_stor
  - hydrograph_module.f90#wtow_om_out
  - hydrograph_module.f90#wtow_om_stor
  - water_allocation_module.f90#wtow
input_variables:
  - water_allocation_module.f90#wtow
reads:
  - water_tower.wal
writes: []
purpose: ""
---

# water_tower_read

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `water_tower_read.f90`
- **Modules used**:
  - [[input_file_module.f90]]
  - [[water_allocation_module.f90]]
  - [[mgt_operations_module.f90]]
  - [[maximum_data_module.f90]]
  - [[hydrograph_module.f90]]
  - [[constituent_mass_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 1 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by:**

- [[main.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[constituent_mass_module.f90#wtow_cs_stor]] - `constituent_mass`
- [[hydrograph_module.f90#wtow_om_out]] - `hyd_output`
- [[hydrograph_module.f90#wtow_om_stor]] - `hyd_output`
- [[water_allocation_module.f90#wtow]] - `water_transfer_data`

**Populated by file reads:**

- [[water_allocation_module.f90#wtow]]

## File I/O
- **Reads**:
  - [[water_tower.wal]]

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
