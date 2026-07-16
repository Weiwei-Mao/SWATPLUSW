---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: header_sd_channel.f90
note_file: header_sd_channel.f90
subroutine: header_sd_channel
module:
  - sd_channel_module
  - basin_module
  - hydrograph_module
  - output_path_module
calls:
  - open_output_file
uses_variables:
  - basin_module.f90#bsn
  - basin_module.f90#pco
  - basin_module.f90#prog
  - hydrograph_module.f90#ch_wbod_hdr
  - hydrograph_module.f90#ch_wbod_hdr_units
  - hydrograph_module.f90#hyd_hdr_units1
  - hydrograph_module.f90#hyd_hdr_units3
  - hydrograph_module.f90#hyd_in_hdr
  - hydrograph_module.f90#hyd_out_hdr
  - hydrograph_module.f90#hyd_stor_hdr
  - hydrograph_module.f90#sp_ob
  - hydrograph_module.f90#wtmp_hdr
  - hydrograph_module.f90#wtmp_units
  - sd_channel_module.f90#sdch_bud_hdr
  - sd_channel_module.f90#sdch_bud_hdr_units
  - sd_channel_module.f90#sdch_hdr
  - sd_channel_module.f90#sdch_hdr_subday
  - sd_channel_module.f90#sdch_hdr_units
  - sd_channel_module.f90#sdch_hdr_units_sub
input_variables: []
reads: []
writes:
  - channel_sd_subday.txt
  - channel_sd_subday.csv
  - channel_sd_day.txt
  - channel_sd_day.csv
  - channel_sd_mon.txt
  - channel_sd_mon.csv
  - channel_sd_yr.txt
  - channel_sd_yr.csv
  - channel_sd_aa.txt
  - channel_sd_aa.csv
  - channel_sdmorph_day.txt
  - channel_sdmorph_day.csv
  - channel_sdmorph_mon.txt
  - channel_sdmorph_mon.csv
  - channel_sdmorph_yr.txt
  - channel_sdmorph_yr.csv
  - channel_sdmorph_aa.txt
  - channel_sdmorph_aa.csv
  - sd_chanbud_day.txt
  - sd_chanbud_day.csv
  - sd_chanbud_mon.txt
  - sd_chanbud_mon.csv
  - sd_chanbud_yr.txt
  - sd_chanbud_yr.csv
  - sd_chanbud_aa.txt
  - sd_chanbud_aa.csv
purpose: ""
---

# header_sd_channel

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `header_sd_channel.f90`
- **Modules used**:
  - [[sd_channel_module.f90]]
  - [[basin_module.f90]]
  - [[hydrograph_module.f90]]
  - [[output_path_module.f90]]
- **Subroutine calls**: 1 | **Files read**: 0 | **Files written**: 26

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
- [[basin_module.f90#bsn]] - `basin_inputs`
- [[basin_module.f90#pco]] - `basin_print_codes`
- [[basin_module.f90#prog]] - `character(len=80)`
- [[hydrograph_module.f90#ch_wbod_hdr]] - `ch_watbod_header`
- [[hydrograph_module.f90#ch_wbod_hdr_units]] - `ch_watbod_header_units`
- [[hydrograph_module.f90#hyd_hdr_units1]] - `hyd_header_units1`
- [[hydrograph_module.f90#hyd_hdr_units3]] - `hyd_header_units3`
- [[hydrograph_module.f90#hyd_in_hdr]] - `hyd_in_header`
- [[hydrograph_module.f90#hyd_out_hdr]] - `hyd_out_header`
- [[hydrograph_module.f90#hyd_stor_hdr]] - `hyd_stor_header`
- [[hydrograph_module.f90#sp_ob]] - `spatial_objects`
- [[hydrograph_module.f90#wtmp_hdr]] - `wtmp_out_header`
- [[hydrograph_module.f90#wtmp_units]] - `wtmp_header_units`
- [[sd_channel_module.f90#sdch_bud_hdr]] - `sdch_bud`
- [[sd_channel_module.f90#sdch_bud_hdr_units]] - `sdch_bud_units`
- [[sd_channel_module.f90#sdch_hdr]] - `sdch_header`
- [[sd_channel_module.f90#sdch_hdr_subday]] - `sdch_header_sub`
- [[sd_channel_module.f90#sdch_hdr_units]] - `sdch_header_units`
- [[sd_channel_module.f90#sdch_hdr_units_sub]] - `sdch_header_units`

## File I/O
- **Writes**:
  - [[channel_sd_subday.txt]]
  - [[channel_sd_subday.csv]]
  - [[channel_sd_day.txt]]
  - [[channel_sd_day.csv]]
  - [[channel_sd_mon.txt]]
  - [[channel_sd_mon.csv]]
  - [[channel_sd_yr.txt]]
  - [[channel_sd_yr.csv]]
  - [[channel_sd_aa.txt]]
  - [[channel_sd_aa.csv]]
  - [[channel_sdmorph_day.txt]]
  - [[channel_sdmorph_day.csv]]
  - [[channel_sdmorph_mon.txt]]
  - [[channel_sdmorph_mon.csv]]
  - [[channel_sdmorph_yr.txt]]
  - [[channel_sdmorph_yr.csv]]
  - [[channel_sdmorph_aa.txt]]
  - [[channel_sdmorph_aa.csv]]
  - [[sd_chanbud_day.txt]]
  - [[sd_chanbud_day.csv]]
  - [[sd_chanbud_mon.txt]]
  - [[sd_chanbud_mon.csv]]
  - [[sd_chanbud_yr.txt]]
  - [[sd_chanbud_yr.csv]]
  - [[sd_chanbud_aa.txt]]
  - [[sd_chanbud_aa.csv]]

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
