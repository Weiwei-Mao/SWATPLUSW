---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: hyd_read_connect.f90
note_file: hyd_read_connect.f90
subroutine: hyd_read_connect
module:
  - hydrograph_module
  - constituent_mass_module
  - time_module
  - climate_module
  - maximum_data_module
  - basin_module
calls:
  - search
uses_variables:
  - basin_module.f90#bsn_cc
  - climate_module.f90#wst
  - climate_module.f90#wst_n
  - constituent_mass_module.f90#cs_db
  - constituent_mass_module.f90#obcs
  - constituent_mass_module.f90#obcs_alloc
  - hydrograph_module.f90#hd
  - hydrograph_module.f90#hz
  - hydrograph_module.f90#ob
  - hydrograph_module.f90#sp_ob
  - hydrograph_module.f90#ts
  - maximum_data_module.f90#db_mx
  - time_module.f90#time
input_variables:
  - hydrograph_module.f90#ob
reads:
  - con_file
writes: []
purpose: ""
---

# hyd_read_connect

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `hyd_read_connect.f90`
- **Modules used**:
  - [[hydrograph_module.f90]]
  - [[constituent_mass_module.f90]]
  - [[time_module.f90]]
  - [[climate_module.f90]]
  - [[maximum_data_module.f90]]
  - [[basin_module.f90]]
- **Subroutine calls**: 1 | **Files read**: 1 | **Files written**: 0

## Call Relationships
**This routine calls:**

- [[search.f90]]

**Called by:**

- [[hyd_connect.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[basin_module.f90#bsn_cc]] - `basin_control_codes`
- [[climate_module.f90#wst]] - `weather_station`
- [[climate_module.f90#wst_n]] - `character(len=50), dimension(:), allocatable`
- [[constituent_mass_module.f90#cs_db]] - `constituents`
- [[constituent_mass_module.f90#obcs]] - `all_constituent_hydrograph`
- [[constituent_mass_module.f90#obcs_alloc]] - `integer, dimension (:), allocatable`
- [[hydrograph_module.f90#hd]] - `hyd_output`
- [[hydrograph_module.f90#hz]] - `hyd_output`
- [[hydrograph_module.f90#ob]] - `object_connectivity`
- [[hydrograph_module.f90#sp_ob]] - `spatial_objects`
- [[hydrograph_module.f90#ts]] - `timestep`
- [[maximum_data_module.f90#db_mx]] - `data_files_max_elements`
- [[time_module.f90#time]] - `time_current`

**Populated by file reads:**

- [[hydrograph_module.f90#ob]]

## File I/O
- **Reads**:
  - `con_file` _(variable; see [[file.cio]])_

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
