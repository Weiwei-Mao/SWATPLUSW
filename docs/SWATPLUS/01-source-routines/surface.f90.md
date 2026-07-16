---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: surface.f90
note_file: surface.f90
subroutine: surface
module:
  - basin_module
  - time_module
  - hydrograph_module
  - hru_module
  - soil_module
  - urban_data_module
  - output_landscape_module
calls:
  - sq_dailycn
  - sq_volq
  - sq_crackflow
  - ero_pkq
  - ero_eiusle
  - ero_ovrsed
  - ero_cfactor
  - ero_ysed
uses_variables:
  - basin_module.f90#bsn_cc
  - hru_module.f90#hru
  - hru_module.f90#ihru
  - hru_module.f90#luse
  - hru_module.f90#precip_eff
  - hru_module.f90#qday
  - hru_module.f90#qp_cms
  - hru_module.f90#surfq
  - hru_module.f90#ulu
  - hydrograph_module.f90#irrig
input_variables: []
reads: []
writes: []
purpose: "this subroutine models surface hydrology at any desired time step"
---

# surface

> [!info] Summary
> this subroutine models surface hydrology at any desired time step

## Basic Information
- **Type**: `subroutine`
- **Source file**: `surface.f90`
- **Modules used**:
  - [[basin_module.f90]]
  - [[time_module.f90]]
  - [[hydrograph_module.f90]]
  - [[hru_module.f90]]
  - [[soil_module.f90]]
  - [[urban_data_module.f90]]
  - [[output_landscape_module.f90]]
- **Subroutine calls**: 8 | **Files read**: 0 | **Files written**: 0

## Call Relationships
**This routine calls:**

- [[sq_dailycn.f90]]
- [[sq_volq.f90]]
- [[sq_crackflow.f90]]
- [[ero_pkq.f90]]
- [[ero_eiusle.f90]]
- [[ero_ovrsed.f90]]
- [[ero_cfactor.f90]]
- [[ero_ysed.f90]]

**Called by:**

- [[hru_control.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[basin_module.f90#bsn_cc]] - `basin_control_codes`
- [[hru_module.f90#hru]] - `hydrologic_response_unit`
- [[hru_module.f90#ihru]] - `integer`
- [[hru_module.f90#luse]] - `landuse`
- [[hru_module.f90#precip_eff]] - `real`
- [[hru_module.f90#qday]] - `real`
- [[hru_module.f90#qp_cms]] - `real`
- [[hru_module.f90#surfq]] - `real, dimension (:), allocatable`
- [[hru_module.f90#ulu]] - `integer`
- [[hydrograph_module.f90#irrig]] - `irrigation_water_transfer`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
