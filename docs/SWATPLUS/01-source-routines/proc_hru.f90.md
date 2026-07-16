---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: proc_hru.f90
note_file: proc_hru.f90
subroutine: proc_hru
module:
  - hydrograph_module
  - maximum_data_module
  - hru_module
  - soil_module
  - constituent_mass_module
  - landuse_data_module
  - erosion_module
  - output_path_module
calls:
  - hru_allo
  - hru_read
  - hrudb_init
  - hru_lum_init_all
  - topohyd_init
  - hru_output_allo
  - structure_set_parms
  - soils_init
  - structure_init
  - plant_all_init
  - cn2_init_all
  - hydro_init
  - pesticide_init
  - pathogen_init
  - salt_hru_init
  - cs_hru_init
  - open_output_file
  - rte_read_nut
uses_variables:
  - constituent_mass_module.f90#cs_db
  - erosion_module.f90#ero_hdr
  - erosion_module.f90#ero_hdr_units
  - erosion_module.f90#ero_output
  - hru_module.f90#hru
  - hydrograph_module.f90#chk_hdr
  - hydrograph_module.f90#chk_unit
  - hydrograph_module.f90#sp_ob
  - landuse_data_module.f90#lum
  - landuse_data_module.f90#lum_str
  - soil_module.f90#soil
input_variables: []
reads: []
writes:
  - erosion.out
  - checker.out
purpose: ""
---

# proc_hru

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `proc_hru.f90`
- **Modules used**:
  - [[hydrograph_module.f90]]
  - [[maximum_data_module.f90]]
  - [[hru_module.f90]]
  - [[soil_module.f90]]
  - [[constituent_mass_module.f90]]
  - [[landuse_data_module.f90]]
  - [[erosion_module.f90]]
  - [[output_path_module.f90]]
- **Subroutine calls**: 18 | **Files read**: 0 | **Files written**: 2

## Call Relationships
**This routine calls:**

- [[hru_allo.f90]]
- [[hru_read.f90]]
- [[hrudb_init.f90]]
- [[hru_lum_init_all.f90]]
- [[topohyd_init.f90]]
- [[hru_output_allo.f90]]
- [[structure_set_parms.f90]]
- [[soils_init.f90]]
- [[structure_init.f90]]
- [[plant_all_init.f90]]
- [[cn2_init_all.f90]]
- [[hydro_init.f90]]
- [[pesticide_init.f90]]
- [[pathogen_init.f90]]
- [[salt_hru_init.f90]]
- [[cs_hru_init.f90]]
- [[output_path_module.f90#open_output_file]]
- [[rte_read_nut.f90]]

**Called by:**

- [[main.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[constituent_mass_module.f90#cs_db]] - `constituents`
- [[erosion_module.f90#ero_hdr]] - `erosion_output_header`
- [[erosion_module.f90#ero_hdr_units]] - `erosion_header_units`
- [[erosion_module.f90#ero_output]] - `erosion_output`
- [[hru_module.f90#hru]] - `hydrologic_response_unit`
- [[hydrograph_module.f90#chk_hdr]] - `output_checker_header`
- [[hydrograph_module.f90#chk_unit]] - `output_checker_unit`
- [[hydrograph_module.f90#sp_ob]] - `spatial_objects`
- [[landuse_data_module.f90#lum]] - `land_use_management`
- [[landuse_data_module.f90#lum_str]] - `land_use_structures`
- [[soil_module.f90#soil]] - `soil_profile`

## File I/O
- **Writes**:
  - [[erosion.out]]
  - [[checker.out]]

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
