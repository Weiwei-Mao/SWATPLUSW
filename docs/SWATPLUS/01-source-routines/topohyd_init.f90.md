---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: topohyd_init.f90
note_file: topohyd_init.f90
subroutine: topohyd_init
module:
  - hydrograph_module
  - hru_module
  - hydrology_data_module
  - topography_data_module
  - soil_data_module
  - plant_module
calls:
  - ascrv
uses_variables:
  - hru_module.f90#hru
  - hru_module.f90#ihru
  - hru_module.f90#snocov1
  - hru_module.f90#snocov2
  - hru_module.f90#snodb
  - hydrograph_module.f90#ob
  - hydrograph_module.f90#sp_ob
  - hydrograph_module.f90#sp_ob1
  - hydrology_data_module.f90#hyd_db
  - topography_data_module.f90#field_db
  - topography_data_module.f90#topo_db
input_variables: []
reads: []
writes: []
purpose: ""
---

# topohyd_init

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `topohyd_init.f90`
- **Modules used**:
  - [[hydrograph_module.f90]]
  - [[hru_module.f90]]
  - [[hydrology_data_module.f90]]
  - [[topography_data_module.f90]]
  - [[soil_data_module.f90]]
  - [[plant_module.f90]]
- **Subroutine calls**: 1 | **Files read**: 0 | **Files written**: 0

## Call Relationships
**This routine calls:**

- [[ascrv.f90]]

**Called by:**

- [[proc_hru.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[hru_module.f90#hru]] - `hydrologic_response_unit`
- [[hru_module.f90#ihru]] - `integer`
- [[hru_module.f90#snocov1]] - `real`
- [[hru_module.f90#snocov2]] - `real`
- [[hru_module.f90#snodb]] - `snow_parameters`
- [[hydrograph_module.f90#ob]] - `object_connectivity`
- [[hydrograph_module.f90#sp_ob]] - `spatial_objects`
- [[hydrograph_module.f90#sp_ob1]] - `spatial_objects`
- [[hydrology_data_module.f90#hyd_db]] - `hydrology_db`
- [[topography_data_module.f90#field_db]] - `fields_db`
- [[topography_data_module.f90#topo_db]] - `topography_db`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
