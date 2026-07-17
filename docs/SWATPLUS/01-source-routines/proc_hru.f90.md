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

- Line 24: call [[hru_allo.f90]], allocation HRU related runtime arrays
- Line 25: call [[hru_read.f90]], read [[hru-data.hru]] and resolve text names to database indexes
- Line 26: call [[hrudb_init.f90]], Copy selected database pointers/settings from hru_db into actual hru() objects
- Line 27: call [[hru_lum_init_all.f90]], Initialize land-use-management settings for every HRU
- Line 28: call [[topohyd_init.f90]], Initialize topography, hydrology, field, and snow parameters for every HRU
- Line 29: call [[hru_output_allo.f90]], Allocate HRU output accumulator arrays

	- [[object.cnt]] defines number of HRUs
	- [[hru.con]] defines each HRU object and its properties pointer, the column 8, hru, is the property pointer, ob(i)%props
	- [[hru-data.hru]] this is the database associated with tppo, hydro, soil, lu_mgt, soil_plant_init, surf_stor, snow, and field. [[hru_read.f90]] resolves text names to integer pointers
	- [[hrudb_init.f90]] copies selected hru_db record into actual hru()
	- Later init routines build soil, plant, topo, hydrology, snow, wetland state

- Line 31-37, septic  is set before soils are initialized

- Line 39: call [[soils_init.f90]], Build HRU soil state
- Line 40: call [[structure_init.f90]], Apply structural BMP/management features
- Line 41: call [[plant_all_init.f90]], it allocates the basin-level accumulators, delegates per-HRU community setup to plant_init, then does a dedup + cross-reference pass so that later, when a plant yields biomass anywhere in the basin, the result can be aggregated by species across the whole basin via the bsn_num index.
- Line 42: call [[cn2_init_all.f90]], Initialize runoff curve numbers
- Line 43: call [[hydro_init.f90]], computes variables related to the watershed hydrology: the time of concentration for the subbasins, lagged surface runoff, the coefficient for the peak runoff rate equation, and lateral flow travel time.
- Line 44: call [[pesticide_init.f90]], optional
- Line 45: call [[pathogen_init.f90]], optional
- Line 46: call [[salt_hru_init.f90]], optional
- Line 47: call [[cs_hru_init.f90]], optional

- Line 49-54, write table title to [[erosion.out]]
- Line 56-62, write table title to [[checker.out]]
- Line 63-67, write hru information to [[checker.out]]

- Line 72: call [[rte_read_nut.f90]], read data from the lake water quality input file.
- End
<!-- USER-NOTES-END -->
