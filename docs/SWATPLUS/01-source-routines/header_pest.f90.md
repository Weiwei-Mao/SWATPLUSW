---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: header_pest.f90
note_file: header_pest.f90
subroutine: header_pest
module:
  - basin_module
  - reservoir_module
  - hydrograph_module
  - output_ls_pesticide_module
  - constituent_mass_module
  - ch_pesticide_module
  - res_pesticide_module
  - aqu_pesticide_module
  - output_path_module
calls:
  - open_output_file
uses_variables:
  - aqu_pesticide_module.f90#aqupest_hdr
  - basin_module.f90#bsn
  - basin_module.f90#pco
  - basin_module.f90#prog
  - ch_pesticide_module.f90#chpest_hdr
  - constituent_mass_module.f90#cs_db
  - hydrograph_module.f90#aqu
  - hydrograph_module.f90#res
  - hydrograph_module.f90#sp_ob
  - output_ls_pesticide_module.f90#pestb_hdr
  - res_pesticide_module.f90#respest_hdr
input_variables: []
reads: []
writes:
  - hru_pest_day.txt
  - hru_pest_day.csv
  - hru_pest_mon.txt
  - hru_pest_mon.csv
  - hru_pest_yr.txt
  - hru_pest_yr.csv
  - hru_pest_aa.txt
  - hru_pest_aa.csv
  - channel_pest_day.txt
  - channel_pest_day.csv
  - channel_pest_mon.txt
  - channel_pest_mon.csv
  - channel_pest_yr.txt
  - channel_pest_yr.csv
  - channel_pest_aa.txt
  - channel_pest_aa.csv
  - reservoir_pest_day.txt
  - reservoir_pest_day.csv
  - reservoir_pest_mon.txt
  - reservoir_pest_mon.csv
  - reservoir_pest_yr.txt
  - reservoir_pest_yr.csv
  - reservoir_pest_aa.txt
  - reservoir_pest_aa.csv
  - basin_aqu_pest_day.txt
  - basin_aqu_pest_day.csv
  - basin_aqu_pest_mon.txt
  - basin_aqu_pest_mon.csv
  - basin_aqu_pest_yr.txt
  - basin_aqu_pest_yr.csv
  - basin_aqu_pest_aa.txt
  - basin_aqu_pest_aa.csv
  - aquifer_pest_day.txt
  - aquifer_pest_day.csv
  - aquifer_pest_mon.txt
  - aquifer_pest_mon.csv
  - aquifer_pest_yr.txt
  - aquifer_pest_yr.csv
  - aquifer_pest_aa.txt
  - aquifer_pest_aa.csv
  - basin_ch_pest_day.txt
  - basin_ch_pest_day.csv
  - basin_ch_pest_mon.txt
  - basin_ch_pest_mon.csv
  - basin_ch_pest_yr.txt
  - basin_ch_pest_yr.csv
  - basin_ch_pest_aa.txt
  - basin_ch_pest_aa.csv
  - basin_res_pest_day.txt
  - basin_res_pest_day.csv
  - basin_res_pest_mon.txt
  - basin_res_pest_mon.csv
  - basin_res_pest_yr.txt
  - basin_res_pest_yr.csv
  - basin_res_pest_aa.txt
  - basin_res_pest_aa.csv
  - basin_ls_pest_day.txt
  - basin_ls_pest_day.csv
  - basin_ls_pest_mon.txt
  - basin_ls_pest_mon.csv
  - basin_ls_pest_yr.txt
  - basin_ls_pest_yr.csv
  - basin_ls_pest_aa.txt
  - basin_ls_pest_aa.csv
purpose: ""
---

# header_pest

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `header_pest.f90`
- **Modules used**:
  - [[basin_module.f90]]
  - [[reservoir_module.f90]]
  - [[hydrograph_module.f90]]
  - [[output_ls_pesticide_module.f90]]
  - [[constituent_mass_module.f90]]
  - [[ch_pesticide_module.f90]]
  - [[res_pesticide_module.f90]]
  - [[aqu_pesticide_module.f90]]
  - [[output_path_module.f90]]
- **Subroutine calls**: 1 | **Files read**: 0 | **Files written**: 64

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
- [[aqu_pesticide_module.f90#aqupest_hdr]] - `aqu_pesticide_header`
- [[basin_module.f90#bsn]] - `basin_inputs`
- [[basin_module.f90#pco]] - `basin_print_codes`
- [[basin_module.f90#prog]] - `character(len=80)`
- [[ch_pesticide_module.f90#chpest_hdr]] - `ch_pesticide_header`
- [[constituent_mass_module.f90#cs_db]] - `constituents`
- [[hydrograph_module.f90#aqu]] - `hyd_output`
- [[hydrograph_module.f90#res]] - `hyd_output`
- [[hydrograph_module.f90#sp_ob]] - `spatial_objects`
- [[output_ls_pesticide_module.f90#pestb_hdr]] - `output_pestbal_header`
- [[res_pesticide_module.f90#respest_hdr]] - `res_pesticide_header`

## File I/O
- **Writes**:
  - [[hru_pest_day.txt]]
  - [[hru_pest_day.csv]]
  - [[hru_pest_mon.txt]]
  - [[hru_pest_mon.csv]]
  - [[hru_pest_yr.txt]]
  - [[hru_pest_yr.csv]]
  - [[hru_pest_aa.txt]]
  - [[hru_pest_aa.csv]]
  - [[channel_pest_day.txt]]
  - [[channel_pest_day.csv]]
  - [[channel_pest_mon.txt]]
  - [[channel_pest_mon.csv]]
  - [[channel_pest_yr.txt]]
  - [[channel_pest_yr.csv]]
  - [[channel_pest_aa.txt]]
  - [[channel_pest_aa.csv]]
  - [[reservoir_pest_day.txt]]
  - [[reservoir_pest_day.csv]]
  - [[reservoir_pest_mon.txt]]
  - [[reservoir_pest_mon.csv]]
  - [[reservoir_pest_yr.txt]]
  - [[reservoir_pest_yr.csv]]
  - [[reservoir_pest_aa.txt]]
  - [[reservoir_pest_aa.csv]]
  - [[basin_aqu_pest_day.txt]]
  - [[basin_aqu_pest_day.csv]]
  - [[basin_aqu_pest_mon.txt]]
  - [[basin_aqu_pest_mon.csv]]
  - [[basin_aqu_pest_yr.txt]]
  - [[basin_aqu_pest_yr.csv]]
  - [[basin_aqu_pest_aa.txt]]
  - [[basin_aqu_pest_aa.csv]]
  - [[aquifer_pest_day.txt]]
  - [[aquifer_pest_day.csv]]
  - [[aquifer_pest_mon.txt]]
  - [[aquifer_pest_mon.csv]]
  - [[aquifer_pest_yr.txt]]
  - [[aquifer_pest_yr.csv]]
  - [[aquifer_pest_aa.txt]]
  - [[aquifer_pest_aa.csv]]
  - [[basin_ch_pest_day.txt]]
  - [[basin_ch_pest_day.csv]]
  - [[basin_ch_pest_mon.txt]]
  - [[basin_ch_pest_mon.csv]]
  - [[basin_ch_pest_yr.txt]]
  - [[basin_ch_pest_yr.csv]]
  - [[basin_ch_pest_aa.txt]]
  - [[basin_ch_pest_aa.csv]]
  - [[basin_res_pest_day.txt]]
  - [[basin_res_pest_day.csv]]
  - [[basin_res_pest_mon.txt]]
  - [[basin_res_pest_mon.csv]]
  - [[basin_res_pest_yr.txt]]
  - [[basin_res_pest_yr.csv]]
  - [[basin_res_pest_aa.txt]]
  - [[basin_res_pest_aa.csv]]
  - [[basin_ls_pest_day.txt]]
  - [[basin_ls_pest_day.csv]]
  - [[basin_ls_pest_mon.txt]]
  - [[basin_ls_pest_mon.csv]]
  - [[basin_ls_pest_yr.txt]]
  - [[basin_ls_pest_yr.csv]]
  - [[basin_ls_pest_aa.txt]]
  - [[basin_ls_pest_aa.csv]]

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
