---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: constit_hyd_mult.f90
note_file: constit_hyd_mult.f90
subroutine: constit_hyd_mult
module:
  - constituent_mass_module
  - dr_module
calls: []
uses_variables:
  - constituent_mass_module.f90#cs_db
  - constituent_mass_module.f90#dr_hmet
  - constituent_mass_module.f90#dr_path
  - constituent_mass_module.f90#dr_pest
  - constituent_mass_module.f90#dr_salt
  - constituent_mass_module.f90#obcs
  - dr_module.f90#dr_hmet_num
  - dr_module.f90#dr_path_num
  - dr_module.f90#dr_pest_num
  - dr_module.f90#dr_salt_num
input_variables: []
reads: []
writes: []
purpose: ""
---

# constit_hyd_mult

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `constit_hyd_mult.f90`
- **Modules used**:
  - [[constituent_mass_module.f90]]
  - [[dr_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 0 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by:**

- [[command.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[constituent_mass_module.f90#cs_db]] - `constituents`
- [[constituent_mass_module.f90#dr_hmet]] - `dr_heavy_metals`
- [[constituent_mass_module.f90#dr_path]] - `dr_pathogens`
- [[constituent_mass_module.f90#dr_pest]] - `dr_pesticide`
- [[constituent_mass_module.f90#dr_salt]] - `dr_salts`
- [[constituent_mass_module.f90#obcs]] - `all_constituent_hydrograph`
- [[dr_module.f90#dr_hmet_num]] - `integer, dimension(:), allocatable`
- [[dr_module.f90#dr_path_num]] - `integer, dimension(:), allocatable`
- [[dr_module.f90#dr_pest_num]] - `integer, dimension(:), allocatable`
- [[dr_module.f90#dr_salt_num]] - `integer, dimension(:), allocatable`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
