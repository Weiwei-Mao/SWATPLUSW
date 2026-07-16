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
- **Modules used**: [[basin_module.f90]], [[time_module.f90]], [[hydrograph_module.f90]], [[hru_module.f90]], [[soil_module.f90]], [[urban_data_module.f90]], [[output_landscape_module.f90]]
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

**Called by** (live Dataview back-query):

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
