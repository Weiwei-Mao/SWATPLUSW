---
type: module
tags:
  - swat/module
  - swat/to-read
file: calibration_data_module.f90
note_file: calibration_data_module.f90
module_name: calibration_data_module
defines_types:
  - calibration_parameters
  - calibration_conditions
  - update_parameters
  - update_conditional
  - soft_calibration_codes
  - soft_calib_parms
  - soft_calib_ls_adjust
  - soft_calib_ls_processes
  - ls_calib_regions
  - soft_data_calib_landscape
  - pl_parms_cal
  - pl_parm_region
  - cataloging_units
  - landscape_units
  - landscape_region_elements
  - landscape_elements
  - soft_calib_pl_adjust
  - soft_calib_pl_processes
  - pl_calib_regions
  - soft_data_calib_plant
  - soft_calib_chan_adjust
  - soft_calib_chan_processes
  - chan_calib_regions
  - soft_data_calib_channel
defines_vars:
  - chg
  - cal_codes
  - lscal_z
  - meas
  - sim
  - aa
  - prev
  - prm
  - prm_prev
  - prm_lim
  - pcur
  - phi
  - plo
  - scur
  - shi
  - slo
  - plcal_z
  - prm_uplim
  - prm_lowlim
  - chcal_z
  - name
  - ob_typ
  - units
  - var
  - alt
  - targc
  - chg_typ
  - typ
  - dtbl
  - hyd_hru
  - hyd_hrul
  - plt
  - sed
  - nut
  - chsed
  - chnut
  - res
  - cal_soft
  - cal_hard
  - obtyp
purpose: ""
---

# calibration_data_module

> [!info] Module
> Defines derived types and module-level variables.

## Defined Types
| Type | Notes |
|---|---|
| `calibration_parameters` |  |
| `calibration_conditions` |  |
| `update_parameters` |  |
| `update_conditional` |  |
| `soft_calibration_codes` |  |
| `soft_calib_parms` |  |
| `soft_calib_ls_adjust` |  |
| `soft_calib_ls_processes` |  |
| `ls_calib_regions` |  |
| `soft_data_calib_landscape` |  |
| `pl_parms_cal` |  |
| `pl_parm_region` |  |
| `cataloging_units` |  |
| `landscape_units` |  |
| `landscape_region_elements` |  |
| `landscape_elements` |  |
| `soft_calib_pl_adjust` |  |
| `soft_calib_pl_processes` |  |
| `pl_calib_regions` |  |
| `soft_data_calib_plant` |  |
| `soft_calib_chan_adjust` |  |
| `soft_calib_chan_processes` |  |
| `chan_calib_regions` |  |
| `soft_data_calib_channel` |  |

## Module-Level Variables
| Variable | Type | Meaning |
|---|---|---|
| `chg` |  |  |
| `cal_codes` |  |  |
| `lscal_z` |  |  |
| `meas` |  |  |
| `sim` |  |  |
| `aa` |  |  |
| `prev` |  |  |
| `prm` |  |  |
| `prm_prev` |  |  |
| `prm_lim` |  |  |
| `pcur` |  |  |
| `phi` |  |  |
| `plo` |  |  |
| `scur` |  |  |
| `shi` |  |  |
| `slo` |  |  |
| `plcal_z` |  |  |
| `prm_uplim` |  |  |
| `prm_lowlim` |  |  |
| `chcal_z` |  |  |
| `name` |  |  |
| `ob_typ` |  |  |
| `units` |  |  |
| `var` |  |  |
| `alt` |  |  |
| `targc` |  |  |
| `chg_typ` |  |  |
| `typ` |  |  |
| `dtbl` |  |  |
| `hyd_hru` |  |  |
| `hyd_hrul` |  |  |
| `plt` |  |  |
| `sed` |  |  |
| `nut` |  |  |
| `chsed` |  |  |
| `chnut` |  |  |
| `res` |  |  |
| `cal_soft` |  |  |
| `cal_hard` |  |  |
| `obtyp` |  |  |

## Used By Source Routines

```dataview
LIST file.link
WHERE type = "source" AND contains(module, this.module_name)
```

<!-- USER-NOTES-START -->
## Notes
Use this section for type and variable meanings, units, and allowed values. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
