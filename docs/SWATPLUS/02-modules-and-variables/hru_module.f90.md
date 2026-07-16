---
type: module
tags:
  - swat/module
  - swat/to-read
file: hru_module.f90
note_file: hru_module.f90
module_name: hru_module
defines_types:
  - uptake_parameters
  - irrigation_sources
  - topography
  - field
  - hydrology
  - snow_parameters
  - subsurface_drainage_parameters
  - saturated_buffer_parameters
  - saturated_buffer
  - landuse
  - soil_plant_initialize
  - hru_databases
  - hru_databases_char
  - hydrologic_response_unit_db
  - land_use_mgt_variables
  - nutrient_parameters
  - hydrologic_response_unit
defines_vars:
  - uptake
  - sb_db
  - dbs
  - dbsc
  - topo
  - field
  - hyd
  - hydcal
  - luse
  - lumv
  - sdr
  - sno
  - nut
  - sb
  - timest
  - name
  - flocon_dtbl
  - urb_ro
  - nutc
  - pestc
  - pathc
  - saltc
  - hmetc
  - csc
  - topo
  - hyd
  - soil
  - land_use_mgt
  - soil_plant_init
  - surf_stor
  - snow
  - field
  - land_use_mgt_c
  - lum_group_c
  - cal_group
  - wet_fp
  - irr_src
  - date
purpose: ""
---

# hru_module

> [!info] Module
> Defines derived types and module-level variables.

## Defined Types
| Type | Notes |
|---|---|
| `uptake_parameters` |  |
| `irrigation_sources` |  |
| `topography` |  |
| `field` |  |
| `hydrology` |  |
| `snow_parameters` |  |
| `subsurface_drainage_parameters` |  |
| `saturated_buffer_parameters` |  |
| `saturated_buffer` |  |
| `landuse` |  |
| `soil_plant_initialize` |  |
| `hru_databases` |  |
| `hru_databases_char` |  |
| `hydrologic_response_unit_db` |  |
| `land_use_mgt_variables` |  |
| `nutrient_parameters` |  |
| `hydrologic_response_unit` |  |

## Module-Level Variables
| Variable | Type | Meaning |
|---|---|---|
| `uptake` |  |  |
| `sb_db` |  |  |
| `dbs` |  |  |
| `dbsc` |  |  |
| `topo` |  |  |
| `field` |  |  |
| `hyd` |  |  |
| `hydcal` |  |  |
| `luse` |  |  |
| `lumv` |  |  |
| `sdr` |  |  |
| `sno` |  |  |
| `nut` |  |  |
| `sb` |  |  |
| `timest` |  |  |
| `name` |  |  |
| `flocon_dtbl` |  |  |
| `urb_ro` |  |  |
| `nutc` |  |  |
| `pestc` |  |  |
| `pathc` |  |  |
| `saltc` |  |  |
| `hmetc` |  |  |
| `csc` |  |  |
| `topo` |  |  |
| `hyd` |  |  |
| `soil` |  |  |
| `land_use_mgt` |  |  |
| `soil_plant_init` |  |  |
| `surf_stor` |  |  |
| `snow` |  |  |
| `field` |  |  |
| `land_use_mgt_c` |  |  |
| `lum_group_c` |  |  |
| `cal_group` |  |  |
| `wet_fp` |  |  |
| `irr_src` |  |  |
| `date` |  |  |

## Used By Source Routines

```dataview
LIST file.link
WHERE type = "source" AND contains(module, this.module_name)
```

<!-- USER-NOTES-START -->
## Notes
Use this section for type and variable meanings, units, and allowed values. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
