---
type: module
tags:
  - swat/module
  - swat/to-read
file: gwflow_module.f90
note_file: gwflow_module.f90
module_name: gwflow_module
defines_types:
  - groundwater_state
  - groundwater_transit
  - groundwater_ss
  - cell_channel_info
  - satx_channel_info
  - cell_connections
  - tile_channel_info
  - cell_reservoir_info
  - cell_floodplain_info
  - canal_chan_info
  - cell_canal_info
  - cell_canal_out_info
  - cell_canal_div_info
  - canal_info
  - cell_pond_info
  - groundwater_heat_state
  - solute_state
  - object_solute_state
  - minl_state
  - solute_chem
  - solute_ss
  - object_solute_ss
  - solute_ss_sum
  - object_solute_ss_sum
defines_vars:
  - gw_hyd_grid_mo
  - gw_hyd_grid_yr
  - gw_hyd_grid_aa
  - gw_heat_grid_mo
  - gw_heat_grid_yr
  - gw_heat_grid_aa
  - grid_type
  - gwsol_nm
purpose: ""
---

# gwflow_module

> [!info] Module
> Defines derived types and module-level variables.

## Defined Types
| Type | Notes |
|---|---|
| `groundwater_state` |  |
| `groundwater_transit` |  |
| `groundwater_ss` |  |
| `cell_channel_info` |  |
| `satx_channel_info` |  |
| `cell_connections` |  |
| `tile_channel_info` |  |
| `cell_reservoir_info` |  |
| `cell_floodplain_info` |  |
| `canal_chan_info` |  |
| `cell_canal_info` |  |
| `cell_canal_out_info` |  |
| `cell_canal_div_info` |  |
| `canal_info` |  |
| `cell_pond_info` |  |
| `groundwater_heat_state` |  |
| `solute_state` |  |
| `object_solute_state` |  |
| `minl_state` |  |
| `solute_chem` |  |
| `solute_ss` |  |
| `object_solute_ss` |  |
| `solute_ss_sum` |  |
| `object_solute_ss_sum` |  |

## Module-Level Variables
| Variable | Type | Meaning |
|---|---|---|
| `gw_hyd_grid_mo` |  |  |
| `gw_hyd_grid_yr` |  |  |
| `gw_hyd_grid_aa` |  |  |
| `gw_heat_grid_mo` |  |  |
| `gw_heat_grid_yr` |  |  |
| `gw_heat_grid_aa` |  |  |
| `grid_type` |  |  |
| `gwsol_nm` |  |  |

## Used By Source Routines

```dataview
LIST file.link
WHERE type = "source" AND contains(module, this.module_name)
```

<!-- USER-NOTES-START -->
## Notes
Use this section for type and variable meanings, units, and allowed values. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
