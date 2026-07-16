---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: cn2_init.f90
note_file: cn2_init.f90
subroutine: cn2_init
module:
  - hru_module
  - soil_module
  - maximum_data_module
  - landuse_data_module
calls:
  - curno
uses_variables:
  - hru_module.f90#cn2
  - hru_module.f90#hru
  - hru_module.f90#isol
  - landuse_data_module.f90#cn
  - landuse_data_module.f90#lum_str
  - soil_module.f90#soil
  - soil_module.f90#sol
input_variables: []
reads: []
writes: []
purpose: ""
---

# cn2_init

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `cn2_init.f90`
- **Modules used**:
  - [[hru_module.f90]]
  - [[soil_module.f90]]
  - [[maximum_data_module.f90]]
  - [[landuse_data_module.f90]]
- **Subroutine calls**: 1 | **Files read**: 0 | **Files written**: 0

## Call Relationships
**This routine calls:**

- [[curno.f90]]

**Called by:**

- [[actions.f90]]
- [[cn2_init_all.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[hru_module.f90#cn2]] - `real, dimension (:), allocatable`
- [[hru_module.f90#hru]] - `hydrologic_response_unit`
- [[hru_module.f90#isol]] - `integer`
- [[landuse_data_module.f90#cn]] - `curvenumber_table`
- [[landuse_data_module.f90#lum_str]] - `land_use_structures`
- [[soil_module.f90#soil]] - `soil_profile`
- [[soil_module.f90#sol]] - `soil_hru_database`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
