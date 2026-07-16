---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: header_write.f90
note_file: header_write.f90
subroutine: header_write
module:
  - basin_module
  - aquifer_module
  - channel_module
  - reservoir_module
  - hydrograph_module
  - sd_channel_module
  - maximum_data_module
  - calibration_data_module
  - output_path_module
calls:
  - open_output_file
uses_variables:
  - aquifer_module.f90#aqu_hdr
  - aquifer_module.f90#aqu_hdr_units
  - basin_module.f90#bsn
  - basin_module.f90#pco
  - basin_module.f90#prog
  - calibration_data_module.f90#cal_codes
  - calibration_data_module.f90#cal_soft
  - channel_module.f90#ch_hdr
  - channel_module.f90#ch_hdr_units
  - hydrograph_module.f90#calb_hdr
  - hydrograph_module.f90#ch_wbod_hdr
  - hydrograph_module.f90#ch_wbod_hdr_units
  - hydrograph_module.f90#fdc_hdr
  - hydrograph_module.f90#hyd_hdr
  - hydrograph_module.f90#hyd_hdr_time
  - hydrograph_module.f90#hyd_hdr_units
  - hydrograph_module.f90#hyd_hdr_units1
  - hydrograph_module.f90#hyd_hdr_units3
  - hydrograph_module.f90#hyd_in_hdr
  - hydrograph_module.f90#hyd_out_hdr
  - hydrograph_module.f90#hyd_stor_hdr
  - hydrograph_module.f90#rec_hdr_time
  - hydrograph_module.f90#recall
  - sd_channel_module.f90#sdch_bud_hdr
  - sd_channel_module.f90#sdch_bud_hdr_units
  - sd_channel_module.f90#sdch_hdr
  - sd_channel_module.f90#sdch_hdr_units
input_variables: []
reads:
  - hydrology-cal.hyd
writes:
  - flow_duration_curve.out
  - basin_aqu_day.txt
  - basin_aqu_day.csv
  - basin_aqu_mon.txt
  - basin_aqu_mon.csv
  - basin_aqu_yr.txt
  - basin_aqu_yr.csv
  - basin_aqu_aa.txt
  - basin_aqu_aa.csv
  - basin_res_day.txt
  - basin_res_day.csv
  - basin_res_mon.txt
  - basin_res_mon.csv
  - basin_res_yr.txt
  - basin_res_yr.csv
  - basin_res_aa.txt
  - basin_res_aa.csv
  - recall_day.txt
  - recall_day.csv
  - recall_mon.txt
  - recall_mon.csv
  - recall_yr.txt
  - recall_yr.csv
  - recall_aa.txt
  - recall_aa.csv
  - basin_cha_day.txt
  - basin_cha_day.csv
  - basin_cha_mon.txt
  - basin_cha_mon.csv
  - basin_cha_yr.txt
  - basin_cha_yr.csv
  - basin_cha_aa.txt
  - basin_cha_aa.csv
  - basin_sd_cha_day.txt
  - basin_sd_cha_day.csv
  - basin_sd_cha_mon.txt
  - basin_sd_cha_mon.csv
  - basin_sd_cha_yr.txt
  - basin_sd_cha_yr.csv
  - basin_sd_cha_aa.txt
  - basin_sd_cha_aa.csv
  - basin_sd_chamorph_day.txt
  - basin_sd_chamorph_day.csv
  - basin_sd_chamorph_mon.txt
  - basin_sd_chamorph_mon.csv
  - basin_sd_chamorph_yr.txt
  - basin_sd_chamorph_yr.csv
  - basin_sd_chamorph_aa.txt
  - basin_sd_chamorph_aa.csv
  - basin_sd_chanbud_day.txt
  - basin_sd_chanbud_day.csv
  - basin_sd_chanbud_mon.txt
  - basin_sd_chanbud_mon.csv
  - basin_sd_chanbud_yr.txt
  - basin_sd_chanbud_yr.csv
  - basin_sd_chanbud_aa.txt
  - basin_sd_chanbud_aa.csv
  - basin_psc_day.txt
  - basin_psc_day.csv
  - basin_psc_mon.txt
  - basin_psc_mon.csv
  - basin_psc_yr.txt
  - basin_psc_yr.csv
  - basin_psc_aa.txt
  - basin_psc_aa.csv
  - ru_day.txt
  - ru_day.csv
  - ru_mon.txt
  - ru_mon.csv
  - ru_yr.txt
  - ru_yr.csv
  - ru_aa.txt
  - ru_aa.csv
  - hru-out.cal
  - hru-new.cal
purpose: ""
---

# header_write

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `header_write.f90`
- **Modules used**:
  - [[basin_module.f90]]
  - [[aquifer_module.f90]]
  - [[channel_module.f90]]
  - [[reservoir_module.f90]]
  - [[hydrograph_module.f90]]
  - [[sd_channel_module.f90]]
  - [[maximum_data_module.f90]]
  - [[calibration_data_module.f90]]
  - [[output_path_module.f90]]
- **Subroutine calls**: 1 | **Files read**: 1 | **Files written**: 75

## Call Relationships
**This routine calls:**

- [[output_path_module.f90#open_output_file]]

**Called by:**

- [[proc_open.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[aquifer_module.f90#aqu_hdr]] - `aqu_header`
- [[aquifer_module.f90#aqu_hdr_units]] - `aqu_header_units`
- [[basin_module.f90#bsn]] - `basin_inputs`
- [[basin_module.f90#pco]] - `basin_print_codes`
- [[basin_module.f90#prog]] - `character(len=80)`
- [[calibration_data_module.f90#cal_codes]] - `soft_calibration_codes`
- [[calibration_data_module.f90#cal_soft]] - `character (len=1)`
- [[channel_module.f90#ch_hdr]] - `ch_header`
- [[channel_module.f90#ch_hdr_units]] - `ch_header_units`
- [[hydrograph_module.f90#calb_hdr]] - `calibration_header`
- [[hydrograph_module.f90#ch_wbod_hdr]] - `ch_watbod_header`
- [[hydrograph_module.f90#ch_wbod_hdr_units]] - `ch_watbod_header_units`
- [[hydrograph_module.f90#fdc_hdr]] - `output_flow_duration_header`
- [[hydrograph_module.f90#hyd_hdr]] - `hyd_header`
- [[hydrograph_module.f90#hyd_hdr_time]] - `hyd_header_time`
- [[hydrograph_module.f90#hyd_hdr_units]] - `hyd_header_units`
- [[hydrograph_module.f90#hyd_hdr_units1]] - `hyd_header_units1`
- [[hydrograph_module.f90#hyd_hdr_units3]] - `hyd_header_units3`
- [[hydrograph_module.f90#hyd_in_hdr]] - `hyd_in_header`
- [[hydrograph_module.f90#hyd_out_hdr]] - `hyd_out_header`
- [[hydrograph_module.f90#hyd_stor_hdr]] - `hyd_stor_header`
- [[hydrograph_module.f90#rec_hdr_time]] - `rec_header_time`
- [[hydrograph_module.f90#recall]] - `recall_hydrograph_inputs`
- [[sd_channel_module.f90#sdch_bud_hdr]] - `sdch_bud`
- [[sd_channel_module.f90#sdch_bud_hdr_units]] - `sdch_bud_units`
- [[sd_channel_module.f90#sdch_hdr]] - `sdch_header`
- [[sd_channel_module.f90#sdch_hdr_units]] - `sdch_header_units`

## File I/O
- **Writes**:
  - [[flow_duration_curve.out]]
  - [[basin_aqu_day.txt]]
  - [[basin_aqu_day.csv]]
  - [[basin_aqu_mon.txt]]
  - [[basin_aqu_mon.csv]]
  - [[basin_aqu_yr.txt]]
  - [[basin_aqu_yr.csv]]
  - [[basin_aqu_aa.txt]]
  - [[basin_aqu_aa.csv]]
  - [[basin_res_day.txt]]
  - [[basin_res_day.csv]]
  - [[basin_res_mon.txt]]
  - [[basin_res_mon.csv]]
  - [[basin_res_yr.txt]]
  - [[basin_res_yr.csv]]
  - [[basin_res_aa.txt]]
  - [[basin_res_aa.csv]]
  - [[recall_day.txt]]
  - [[recall_day.csv]]
  - [[recall_mon.txt]]
  - [[recall_mon.csv]]
  - [[recall_yr.txt]]
  - [[recall_yr.csv]]
  - [[recall_aa.txt]]
  - [[recall_aa.csv]]
  - [[basin_cha_day.txt]]
  - [[basin_cha_day.csv]]
  - [[basin_cha_mon.txt]]
  - [[basin_cha_mon.csv]]
  - [[basin_cha_yr.txt]]
  - [[basin_cha_yr.csv]]
  - [[basin_cha_aa.txt]]
  - [[basin_cha_aa.csv]]
  - [[basin_sd_cha_day.txt]]
  - [[basin_sd_cha_day.csv]]
  - [[basin_sd_cha_mon.txt]]
  - [[basin_sd_cha_mon.csv]]
  - [[basin_sd_cha_yr.txt]]
  - [[basin_sd_cha_yr.csv]]
  - [[basin_sd_cha_aa.txt]]
  - [[basin_sd_cha_aa.csv]]
  - [[basin_sd_chamorph_day.txt]]
  - [[basin_sd_chamorph_day.csv]]
  - [[basin_sd_chamorph_mon.txt]]
  - [[basin_sd_chamorph_mon.csv]]
  - [[basin_sd_chamorph_yr.txt]]
  - [[basin_sd_chamorph_yr.csv]]
  - [[basin_sd_chamorph_aa.txt]]
  - [[basin_sd_chamorph_aa.csv]]
  - [[basin_sd_chanbud_day.txt]]
  - [[basin_sd_chanbud_day.csv]]
  - [[basin_sd_chanbud_mon.txt]]
  - [[basin_sd_chanbud_mon.csv]]
  - [[basin_sd_chanbud_yr.txt]]
  - [[basin_sd_chanbud_yr.csv]]
  - [[basin_sd_chanbud_aa.txt]]
  - [[basin_sd_chanbud_aa.csv]]
  - [[basin_psc_day.txt]]
  - [[basin_psc_day.csv]]
  - [[basin_psc_mon.txt]]
  - [[basin_psc_mon.csv]]
  - [[basin_psc_yr.txt]]
  - [[basin_psc_yr.csv]]
  - [[basin_psc_aa.txt]]
  - [[basin_psc_aa.csv]]
  - [[ru_day.txt]]
  - [[ru_day.csv]]
  - [[ru_mon.txt]]
  - [[ru_mon.csv]]
  - [[ru_yr.txt]]
  - [[ru_yr.csv]]
  - [[ru_aa.txt]]
  - [[ru_aa.csv]]
  - [[hru-out.cal]]
  - [[hru-new.cal]]
- **Reads**:
  - [[hydrology-cal.hyd]]

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
