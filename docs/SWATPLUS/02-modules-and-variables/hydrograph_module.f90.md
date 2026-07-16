---
type: module
tags:
  - swat/module
  - swat/to-read
file: hydrograph_module.f90
note_file: hydrograph_module.f90
module_name: hydrograph_module
defines_types:
  - hyd_output
  - hyd_sep
  - wallo_source_object
  - wallo_transfer_object
  - water_allocation_object
  - object_output
  - channel_floodplain_water_balance
  - timestep
  - sorted_duration_curve
  - duration_curve_points
  - flow_duration_curve
  - inflow_unit_hyds
  - flashiness_index
  - object_connectivity
  - irrigation_water_transfer
  - recall_hydrograph_inputs
  - spatial_objects
  - object_total_hydrographs
  - routing_unit_data
  - routing_unit_elements
  - channel_surface_elements
  - geomorphic_baseflow_channel_data
  - channel_aquifer_elements
  - hyd_header
  - hyd_stor_header
  - hyd_in_header
  - hyd_out_header
  - hyd_inout_header
  - wtmp_out_header
  - sed_hyd_header
  - sd_hyd_header_units
  - sol_header
  - plant_header
  - flood_plain_header
  - ch_watbod_header
  - ch_watbod_header_units
  - ch_watbod_inoutheader
  - ch_watbod_inoutheader_units
  - hyd_header_units1
  - hyd_header_units3
  - hydinout_header_units1
  - wtmp_header_units
  - hyd_header_units
  - hyd_header_units2
  - hyd_header_time
  - rec_header_time
  - hyd_header_obj
  - output_flow_duration_header
  - calibration_header
  - calibration2_header
  - calibration3_header
  - output_checker_header
  - output_checker_unit
  - hru_swift_header_base
  - hru_swift_header_baseunit
  - hru_swift_header_base2
  - hru_swift_header_baseunit2
  - hru_swift_header
  - shade_factor_data
defines_vars:
  - brec_d
  - brec_m
  - brec_y
  - brec_a
  - bru_d
  - bru_m
  - bru_y
  - bru_a
  - binhyd_d
  - hz
  - dr1
  - ht1
  - ht2
  - ht3
  - ht4
  - ht5
  - delrto
  - fp_dep
  - ch_dep
  - bank_ero
  - bed_ero
  - ch_trans
  - hdsep1
  - hdsep2
  - resz
  - chaz
  - bres_in_d
  - bres_in_m
  - bres_in_y
  - bres_in_a
  - bres
  - bres_out_d
  - bres_out_m
  - bres_out_y
  - bres_out_a
  - resmz
  - bwet_in_d
  - bwet_in_m
  - bwet_in_y
  - bwet_in_a
  - bwet_out_d
  - bwet_out_m
  - bwet_out_y
  - bwet_out_a
  - bch_stor_d
  - bch_stor_m
  - bch_stor_y
  - bch_stor_a
  - bch_in_d
  - bch_in_m
  - bch_in_y
  - bch_in_a
  - bch_out_d
  - bch_out_m
  - bch_out_y
  - bch_out_a
  - chomz
  - hd
  - h_tot
  - wdraw_om
  - wdraw_om_tot
  - outflo_om
  - p_md
  - fdc
  - flash_idx
  - hin
  - hin_sur
  - hin_lat
  - hin_til
  - hin_aqu
  - trans
  - hin_tot
  - hout_tot
  - conc_prev
  - hdep_m
  - hdep_y
  - hdep_a
  - hdsep
  - hdsep_in
  - water
  - sp_ob
  - sp_ob1
  - hd_tot
  - dr
  - hyd_hdr
  - hyd_stor_hdr
  - hyd_in_hdr
  - hyd_out_hdr
  - hyd_inout_hdr
  - wtmp_hdr
  - sd_hyd_hdr
  - sd_hyd_hdr_units
  - sol_hdr
  - plt_hdr
  - fp_hdr
  - ch_wbod_hdr
  - ch_wbod_hdr_units
  - ch_wbod_inouthdr
  - ch_wbod_inouthdr_units
  - hyd_hdr_units1
  - hyd_hdr_units3
  - hydinout_hdr_units1
  - wtmp_units
  - hyd_hdr_units
  - hyd_hdr_units2
  - hyd_hdr_time
  - rec_hdr_time
  - hyd_hdr_obj
  - fdc_hdr
  - calb_hdr
  - calb2_hdr
  - calb3_hdr
  - chk_hdr
  - chk_unit
  - base
  - exco
  - exco_unit
  - dr_unit
  - hru_swift_hdr
  - name
  - obtyp
  - hydtyp
  - filename
  - typ
  - wst_c
  - ruleset
  - dr_name
  - flo
  - sed
  - orgn
  - sedp
  - no3
  - solp
  - chla
  - nh3
  - no2
  - cbod
  - dox
  - san
  - sil
  - cla
  - sag
  - lag
  - grv
  - temp
  - flo_stor
  - sed_stor
  - orgn_stor
  - sedp_stor
  - no3_stor
  - solp_stor
  - chla_stor
  - nh3_stor
  - no2_stor
  - cbod_stor
  - dox_stor
  - san_stor
  - sil_stor
  - cla_stor
  - sag_stor
  - lag_stor
  - grv_stor
  - temp_stor
  - flo_in
  - sed_in
  - orgn_in
  - sedp_in
  - no3_in
  - solp_in
  - chla_in
  - nh3_in
  - no2_in
  - cbod_in
  - dox_in
  - san_in
  - sil_in
  - cla_in
  - sag_in
  - lag_in
  - grv_in
  - temp_in
  - flo_out
  - sed_out
  - orgn_out
  - sedp_out
  - no3_out
  - solp_out
  - chla_out
  - nh3_out
  - no2_out
  - cbod_out
  - dox_out
  - san_out
  - sil_out
  - cla_out
  - sag_out
  - lag_out
  - grv_out
  - temp_out
  - water_temp
  - layer1
  - layer2
  - layer3
  - layer4
  - layer5
  - layer6
  - layer7
  - layer8
  - layer9
  - layer10
  - growing
  - dormant
  - lai
  - can_hgt
  - root_dep
  - phuacc
  - tot_m
  - ab_gr_m
  - leaf_m
  - root_m
  - stem_m
  - seed_m
  - inflo
  - outflo
  - tl
  - ev
  - ch_stor_init
  - ch_stor
  - fp_stor_init
  - fp_stor
  - tot_stor_init
  - tot_stor
  - wet_stor_init
  - wet_stor
  - day
  - mo
  - day_mo
  - yrc
  - isd
  - id
  - area_ha
  - precip
  - evap
  - seep
  - gis_id
  - sedp_ouy
  - wtmp
  - otype
  - iotyp
  - iotypno
  - hydio
  - objno
  - blank
  - props
  - area
  - f_idx
  - mean
  - max
  - p01
  - p05
  - p1
  - p2
  - p3
  - p5
  - p10
  - p15
  - p20
  - p25
  - p30
  - p35
  - p40
  - p45
  - p50
  - p55
  - p60
  - p65
  - p70
  - p75
  - p80
  - p85
  - p90
  - p95
  - p97
  - p98
  - p99
  - min
  - ha
  - nbyr
  - prec
  - meas
  - srr
  - lfr
  - pcr
  - etr
  - tfr
  - orgp
  - aa
  - srr_aa
  - lfr_aa
  - pcr_aa
  - etr_aa
  - tfr_aa
  - sed_aa
  - orgn_aa
  - orgp_aa
  - no3_aa
  - solp_aa
  - cn_prm_aa
  - esco
  - lat_len
  - petco
  - slope
  - tconc
  - etco
  - perco
  - revapc
  - cn3_swf
  - dakm2
  - cn2
  - tc
  - soildep
  - perco_co
  - slopelen
  - sy
  - abf
  - percc
  - sw
  - gw
  - gwflow
  - gwdeep
  - snow
  - xlat
  - itext
  - tropical
  - igrow1
  - igrow2
  - plant
  - ipet
  - irr
  - irrsrc
  - tdrain
  - uslek
  - uslec
  - uslep
  - uslels
  - chgtyp
  - val
  - conds
  - lyr1
  - lyr2
  - year1
  - year2
  - day1
  - day2
  - objtot
  - sname
  - hydgrp
  - zmx
  - usle_k
  - sumfc
  - sumul
  - usle_p
  - usle_ls
  - epco
  - latq_co
  - tiledrain
  - unitsed
  - unitorgn
  - unitsedp
  - unitno3
  - unitsolp
  - unitnh3
  - unitno2
  - unitflo
  - hd_type
purpose: ""
---

# hydrograph_module

> [!info] Module
> Defines derived types and module-level variables.

## Defined Types
| Type | Notes |
|---|---|
| `hyd_output` |  |
| `hyd_sep` |  |
| `wallo_source_object` |  |
| `wallo_transfer_object` |  |
| `water_allocation_object` |  |
| `object_output` |  |
| `channel_floodplain_water_balance` |  |
| `timestep` |  |
| `sorted_duration_curve` |  |
| `duration_curve_points` |  |
| `flow_duration_curve` |  |
| `inflow_unit_hyds` |  |
| `flashiness_index` |  |
| `object_connectivity` |  |
| `irrigation_water_transfer` |  |
| `recall_hydrograph_inputs` |  |
| `spatial_objects` |  |
| `object_total_hydrographs` |  |
| `routing_unit_data` |  |
| `routing_unit_elements` |  |
| `channel_surface_elements` |  |
| `geomorphic_baseflow_channel_data` |  |
| `channel_aquifer_elements` |  |
| `hyd_header` |  |
| `hyd_stor_header` |  |
| `hyd_in_header` |  |
| `hyd_out_header` |  |
| `hyd_inout_header` |  |
| `wtmp_out_header` |  |
| `sed_hyd_header` |  |
| `sd_hyd_header_units` |  |
| `sol_header` |  |
| `plant_header` |  |
| `flood_plain_header` |  |
| `ch_watbod_header` |  |
| `ch_watbod_header_units` |  |
| `ch_watbod_inoutheader` |  |
| `ch_watbod_inoutheader_units` |  |
| `hyd_header_units1` |  |
| `hyd_header_units3` |  |
| `hydinout_header_units1` |  |
| `wtmp_header_units` |  |
| `hyd_header_units` |  |
| `hyd_header_units2` |  |
| `hyd_header_time` |  |
| `rec_header_time` |  |
| `hyd_header_obj` |  |
| `output_flow_duration_header` |  |
| `calibration_header` |  |
| `calibration2_header` |  |
| `calibration3_header` |  |
| `output_checker_header` |  |
| `output_checker_unit` |  |
| `hru_swift_header_base` |  |
| `hru_swift_header_baseunit` |  |
| `hru_swift_header_base2` |  |
| `hru_swift_header_baseunit2` |  |
| `hru_swift_header` |  |
| `shade_factor_data` |  |

## Module-Level Variables
| Variable | Type | Meaning |
|---|---|---|
| `brec_d` |  |  |
| `brec_m` |  |  |
| `brec_y` |  |  |
| `brec_a` |  |  |
| `bru_d` |  |  |
| `bru_m` |  |  |
| `bru_y` |  |  |
| `bru_a` |  |  |
| `binhyd_d` |  |  |
| `hz` |  |  |
| `dr1` |  |  |
| `ht1` |  |  |
| `ht2` |  |  |
| `ht3` |  |  |
| `ht4` |  |  |
| `ht5` |  |  |
| `delrto` |  |  |
| `fp_dep` |  |  |
| `ch_dep` |  |  |
| `bank_ero` |  |  |
| `bed_ero` |  |  |
| `ch_trans` |  |  |
| `hdsep1` |  |  |
| `hdsep2` |  |  |
| `resz` |  |  |
| `chaz` |  |  |
| `bres_in_d` |  |  |
| `bres_in_m` |  |  |
| `bres_in_y` |  |  |
| `bres_in_a` |  |  |
| `bres` |  |  |
| `bres_out_d` |  |  |
| `bres_out_m` |  |  |
| `bres_out_y` |  |  |
| `bres_out_a` |  |  |
| `resmz` |  |  |
| `bwet_in_d` |  |  |
| `bwet_in_m` |  |  |
| `bwet_in_y` |  |  |
| `bwet_in_a` |  |  |

*(Showing first 40 of 375 variables.)*

## Used By Source Routines

```dataview
LIST file.link
WHERE type = "source" AND contains(module, this.module_name)
```

<!-- USER-NOTES-START -->
## Notes
Use this section for type and variable meanings, units, and allowed values. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
