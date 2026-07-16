---
type: module
tags:
  - swat/module
  - swat/to-read
file: sd_channel_module.f90
note_file: sd_channel_module.f90
module_name: sd_channel_module
defines_types:
  - swatdeg_hydsed_data
  - swatdeg_sednut_data
  - channel_sediment_budget_output
  - channel_morphology_output
  - gully_data
  - swatdeg_init_datafiles
  - swatdeg_datafiles
  - floodplain_parameters
  - muskingum_parameters
  - swatdeg_channel_dynamic
  - channel_rating_curve_parameters
  - channel_rating_curve
  - sd_ch_output
  - sdch_header
  - sdch_header_units
  - sdch_bud
  - sdch_bud_units
  - sdch_header_sub
  - sdch_header_units_sub
  - sd_chd_header
defines_vars:
  - ch_sed_budz
  - bch_sed_bud_d
  - bch_sed_bud_m
  - bch_sed_bud_y
  - bch_sed_bud_a
  - msk
  - fp
  - rcurv
  - rcz
  - in1
  - in2
  - out1
  - out2
  - bchsd_d
  - bchsd_m
  - bchsd_y
  - bchsd_a
  - chsdz
  - sdch_hdr
  - sdch_hdr_units
  - sdch_bud_hdr
  - sdch_bud_hdr_units
  - sdch_hdr_subday
  - sdch_hdr_units_sub
  - sd_chd_hdr
  - name
  - order
  - initc
  - hydc
  - sedc
  - nutc
  - region
  - overbank
  - day
  - mo
  - day_mo
  - yrc
  - isd
  - id
  - flo_in
  - aqu_in
  - flo
  - peakr
  - sed_in
  - sed_out
  - washld
  - bedld
  - dep
  - deg_btm
  - deg_bank
  - hc_sed
  - width
  - depth
  - slope
  - deg_btm_m
  - deg_bank_m
  - hc_len
  - flo_in_mm
  - aqu_in_mm
  - flo_mm
  - sed_stor
  - n_tot
  - p_tot
  - dep_bf
  - velav_bf
  - in_sed
  - out_sed
  - fp_dep
  - ch_dep
  - bank_ero
  - bed_ero
  - in_no3
  - in_orgn
  - out_no3
  - out_orgn
  - fp_no3
  - bank_no3
  - bed_no3
  - fp_orgn
  - ch_orgn
  - bank_orgn
  - bed_orgn
  - in_solp
  - in_orgp
  - out_solp
  - out_orgp
  - fp_solp
  - bank_solp
  - bed_solp
  - fp_orgp
  - ch_orgp
  - bank_orgp
  - bed_orgp
  - no3_orgn
  - solp_orgp
  - no3_orgp
  - ii
  - hyd_flo
  - chw
  - chd
  - chs
  - chl
  - chn
  - chk
  - cherod
  - cov
  - sinu
  - chseq
  - d50
  - ch_clay
  - carbon
  - ch_bd
  - chss
  - bankfull_flo
  - fps
  - fpn
  - n_conc
  - p_conc
  - p_bio
purpose: ""
---

# sd_channel_module

> [!info] Module
> Defines derived types and module-level variables.

## Defined Types
| Type | Notes |
|---|---|
| `swatdeg_hydsed_data` |  |
| `swatdeg_sednut_data` |  |
| `channel_sediment_budget_output` |  |
| `channel_morphology_output` |  |
| `gully_data` |  |
| `swatdeg_init_datafiles` |  |
| `swatdeg_datafiles` |  |
| `floodplain_parameters` |  |
| `muskingum_parameters` |  |
| `swatdeg_channel_dynamic` |  |
| `channel_rating_curve_parameters` |  |
| `channel_rating_curve` |  |
| `sd_ch_output` |  |
| `sdch_header` |  |
| `sdch_header_units` |  |
| `sdch_bud` |  |
| `sdch_bud_units` |  |
| `sdch_header_sub` |  |
| `sdch_header_units_sub` |  |
| `sd_chd_header` |  |

## Module-Level Variables
| Variable | Type | Meaning |
|---|---|---|
| `ch_sed_budz` |  |  |
| `bch_sed_bud_d` |  |  |
| `bch_sed_bud_m` |  |  |
| `bch_sed_bud_y` |  |  |
| `bch_sed_bud_a` |  |  |
| `msk` |  |  |
| `fp` |  |  |
| `rcurv` |  |  |
| `rcz` |  |  |
| `in1` |  |  |
| `in2` |  |  |
| `out1` |  |  |
| `out2` |  |  |
| `bchsd_d` |  |  |
| `bchsd_m` |  |  |
| `bchsd_y` |  |  |
| `bchsd_a` |  |  |
| `chsdz` |  |  |
| `sdch_hdr` |  |  |
| `sdch_hdr_units` |  |  |
| `sdch_bud_hdr` |  |  |
| `sdch_bud_hdr_units` |  |  |
| `sdch_hdr_subday` |  |  |
| `sdch_hdr_units_sub` |  |  |
| `sd_chd_hdr` |  |  |
| `name` |  |  |
| `order` |  |  |
| `initc` |  |  |
| `hydc` |  |  |
| `sedc` |  |  |
| `nutc` |  |  |
| `region` |  |  |
| `overbank` |  |  |
| `day` |  |  |
| `mo` |  |  |
| `day_mo` |  |  |
| `yrc` |  |  |
| `isd` |  |  |
| `id` |  |  |
| `flo_in` |  |  |

*(Showing first 40 of 119 variables.)*

## Used By Source Routines

```dataview
LIST file.link
WHERE type = "source" AND contains(module, this.module_name)
```

<!-- USER-NOTES-START -->
## Notes
Use this section for type and variable meanings, units, and allowed values. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
