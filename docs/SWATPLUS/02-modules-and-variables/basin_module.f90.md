---
type: module
tags:
  - swat/module
  - swat/to-read
file: basin_module.f90
note_file: basin_module.f90
module_name: basin_module
defines_types:
  - basin_inputs
  - basin_control_codes
  - basin_parms
  - print_interval
  - basin_print_codes
  - basin_sediment_budget
  - mgt_header
  - mgt_header_unit1
  - basin_yld_header
defines_vars:
  - bsn
  - bsn_cc
  - bsn_prm
  - wb_bsn
  - nb_bsn
  - ls_bsn
  - pw_bsn
  - aqu_bsn
  - res_bsn
  - chan_bsn
  - sd_chan_bsn
  - recall_bsn
  - wb_reg
  - nb_reg
  - ls_reg
  - pw_reg
  - aqu_reg
  - res_reg
  - sd_chan_reg
  - recall_reg
  - water_allo
  - wb_lsu
  - nb_lsu
  - ls_lsu
  - pw_lsu
  - wb_hru
  - nb_hru
  - ls_hru
  - pw_hru
  - cb_hru
  - cb_vars_hru
  - cb_gl_hru
  - cb_trf_hru
  - cb_lyr_hru
  - cb_cpool_hru
  - cb_npool_hru
  - cb_plt_hru
  - cb_flux_hru
  - cb_drv_hru
  - cb_dyn_hru
  - cb_snap_hru
  - cb_gl_lsu
  - cb_trf_lsu
  - cb_plt_lsu
  - wb_sd
  - nb_sd
  - ls_sd
  - pw_sd
  - chan
  - sd_chan
  - aqu
  - res
  - recall
  - hyd
  - ru
  - pest
  - salt_basin
  - salt_hru
  - salt_ru
  - salt_aqu
  - salt_chn
  - salt_res
  - salt_wet
  - cs_basin
  - cs_hru
  - cs_ru
  - cs_aqu
  - cs_chn
  - cs_res
  - cs_wet
  - gwflow_wb
  - gwflow_flux
  - gwflow_heat
  - gwflow_solute
  - gwflow_obs
  - gwflow_pump
  - pco
  - pco_init
  - bsn_sedbud
  - mgt_hdr
  - mgt_hdr_unt1
  - bsn_yld_hdr
  - prog
  - name
  - petfile
  - wwqfile
  - atmo
  - d
  - m
  - y
  - a
  - day_print
  - day_print_over
  - sw_init
  - csvout
  - use_obj_labels
  - cdfout
  - crop_yld
  - mgtout
  - hydcon
  - fdcout
  - hru
  - year
  - mon
  - day
  - crop
  - oper
  - phub
  - phua
  - sw
  - bio
  - rsd
  - solno3
  - solp
  - op_var
  - var1
  - var2
  - var3
  - var4
  - var5
  - var6
  - var7
  - plant_no
  - plant_name
  - area_ha
  - yield_t
  - yield_tha
purpose: ""
---

# basin_module

> [!info] Module
> Defines derived types and module-level variables.

## Defined Types
| Type | Notes |
|---|---|
| `basin_inputs` |  |
| `basin_control_codes` |  |
| `basin_parms` |  |
| `print_interval` |  |
| `basin_print_codes` |  |
| `basin_sediment_budget` |  |
| `mgt_header` |  |
| `mgt_header_unit1` |  |
| `basin_yld_header` |  |

## Module-Level Variables
| Variable | Type | Meaning |
|---|---|---|
| `bsn` |  |  |
| `bsn_cc` |  |  |
| `bsn_prm` |  |  |
| `wb_bsn` |  |  |
| `nb_bsn` |  |  |
| `ls_bsn` |  |  |
| `pw_bsn` |  |  |
| `aqu_bsn` |  |  |
| `res_bsn` |  |  |
| `chan_bsn` |  |  |
| `sd_chan_bsn` |  |  |
| `recall_bsn` |  |  |
| `wb_reg` |  |  |
| `nb_reg` |  |  |
| `ls_reg` |  |  |
| `pw_reg` |  |  |
| `aqu_reg` |  |  |
| `res_reg` |  |  |
| `sd_chan_reg` |  |  |
| `recall_reg` |  |  |
| `water_allo` |  |  |
| `wb_lsu` |  |  |
| `nb_lsu` |  |  |
| `ls_lsu` |  |  |
| `pw_lsu` |  |  |
| `wb_hru` |  |  |
| `nb_hru` |  |  |
| `ls_hru` |  |  |
| `pw_hru` |  |  |
| `cb_hru` |  |  |
| `cb_vars_hru` |  |  |
| `cb_gl_hru` |  |  |
| `cb_trf_hru` |  |  |
| `cb_lyr_hru` |  |  |
| `cb_cpool_hru` |  |  |
| `cb_npool_hru` |  |  |
| `cb_plt_hru` |  |  |
| `cb_flux_hru` |  |  |
| `cb_drv_hru` |  |  |
| `cb_dyn_hru` |  |  |

*(Showing first 40 of 127 variables.)*

## Used By Source Routines

```dataview
LIST file.link
WHERE type = "source" AND contains(module, this.module_name)
```

<!-- USER-NOTES-START -->
## Notes
Use this section for type and variable meanings, units, and allowed values. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
