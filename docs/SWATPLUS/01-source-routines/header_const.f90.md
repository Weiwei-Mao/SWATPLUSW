---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: header_const.f90
note_file: header_const.f90
subroutine: header_const
module:
  - basin_module
  - reservoir_module
  - hydrograph_module
  - constituent_mass_module
  - ch_cs_module
  - res_cs_module
  - cs_module
  - cs_aquifer
  - output_path_module
calls:
  - open_output_file
uses_variables:
  - basin_module.f90#bsn
  - basin_module.f90#pco
  - basin_module.f90#prog
  - ch_cs_module.f90#chcs_hdr
  - constituent_mass_module.f90#cs_aqu
  - constituent_mass_module.f90#cs_db
  - constituent_mass_module.f90#rucsb_hdr
  - cs_aquifer.f90#cs_hdr_aqu
  - cs_module.f90#cs_hdr_hru
  - cs_module.f90#csb_hdr
  - hydrograph_module.f90#aqu
  - hydrograph_module.f90#res
  - hydrograph_module.f90#sp_ob
  - res_cs_module.f90#rescs_hdr
input_variables: []
reads: []
writes:
  - basin_cs_day.txt
  - basin_cs_mon.txt
  - basin_cs_yr.txt
  - basin_cs_aa.txt
  - hru_cs_day.txt
  - hru_cs_day.csv
  - hru_cs_mon.txt
  - hru_cs_mon.csv
  - hru_cs_yr.txt
  - hru_cs_yr.csv
  - hru_cs_aa.txt
  - hru_cs_aa.csv
  - aquifer_cs_day.txt
  - aquifer_cs_day.csv
  - aquifer_cs_mon.txt
  - aquifer_cs_mon.csv
  - aquifer_cs_yr.txt
  - aquifer_cs_yr.csv
  - aquifer_cs_aa.txt
  - aquifer_cs_aa.csv
  - channel_cs_day.txt
  - channel_cs_day.csv
  - channel_cs_mon.txt
  - channel_cs_mon.csv
  - channel_cs_yr.txt
  - channel_cs_yr.csv
  - channel_cs_aa.txt
  - channel_cs_aa.csv
  - reservoir_cs_day.txt
  - reservoir_cs_day.csv
  - reservoir_cs_mon.txt
  - reservoir_cs_mon.csv
  - reservoir_cs_yr.txt
  - reservoir_cs_yr.csv
  - reservoir_cs_aa.txt
  - reservoir_cs_aa.csv
  - rout_unit_cs_day.txt
  - rout_unit_cs_day.csv
  - rout_unit_cs_mon.txt
  - rout_unit_cs_mon.csv
  - rout_unit_cs_yr.txt
  - rout_unit_cs_yr.csv
  - rout_unit_cs_aa.txt
  - rout_unit_cs_aa.csv
  - wetland_cs_day.txt
  - wetland_cs_day.csv
  - wetland_cs_mon.txt
  - wetland_cs_mon.csv
  - wetland_cs_yr.txt
  - wetland_cs_yr.csv
  - wetland_cs_aa.txt
  - wetland_cs_aa.csv
purpose: ""
---

# header_const

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `header_const.f90`
- **Modules used**:
  - [[basin_module.f90]]
  - [[reservoir_module.f90]]
  - [[hydrograph_module.f90]]
  - [[constituent_mass_module.f90]]
  - [[ch_cs_module.f90]]
  - [[res_cs_module.f90]]
  - [[cs_module.f90]]
  - [[cs_aquifer.f90]]
  - [[output_path_module.f90]]
- **Subroutine calls**: 1 | **Files read**: 0 | **Files written**: 52

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
- [[ch_cs_module.f90#chcs_hdr]] - `ch_cs_header`
- [[constituent_mass_module.f90#cs_aqu]] - `constituent_mass`
- [[constituent_mass_module.f90#cs_db]] - `constituents`
- [[constituent_mass_module.f90#rucsb_hdr]] - `output_rucsb_header`
- [[cs_aquifer.f90#cs_hdr_aqu]] - `output_cs_header`
- [[cs_module.f90#cs_hdr_hru]] - `output_cs_hdr_hru`
- [[cs_module.f90#csb_hdr]] - `output_csbal_header`
- [[hydrograph_module.f90#aqu]] - `hyd_output`
- [[hydrograph_module.f90#res]] - `hyd_output`
- [[hydrograph_module.f90#sp_ob]] - `spatial_objects`
- [[res_cs_module.f90#rescs_hdr]] - `res_cs_header`

## File I/O
- **Writes**:
  - [[basin_cs_day.txt]]
  - [[basin_cs_mon.txt]]
  - [[basin_cs_yr.txt]]
  - [[basin_cs_aa.txt]]
  - [[hru_cs_day.txt]]
  - [[hru_cs_day.csv]]
  - [[hru_cs_mon.txt]]
  - [[hru_cs_mon.csv]]
  - [[hru_cs_yr.txt]]
  - [[hru_cs_yr.csv]]
  - [[hru_cs_aa.txt]]
  - [[hru_cs_aa.csv]]
  - [[aquifer_cs_day.txt]]
  - [[aquifer_cs_day.csv]]
  - [[aquifer_cs_mon.txt]]
  - [[aquifer_cs_mon.csv]]
  - [[aquifer_cs_yr.txt]]
  - [[aquifer_cs_yr.csv]]
  - [[aquifer_cs_aa.txt]]
  - [[aquifer_cs_aa.csv]]
  - [[channel_cs_day.txt]]
  - [[channel_cs_day.csv]]
  - [[channel_cs_mon.txt]]
  - [[channel_cs_mon.csv]]
  - [[channel_cs_yr.txt]]
  - [[channel_cs_yr.csv]]
  - [[channel_cs_aa.txt]]
  - [[channel_cs_aa.csv]]
  - [[reservoir_cs_day.txt]]
  - [[reservoir_cs_day.csv]]
  - [[reservoir_cs_mon.txt]]
  - [[reservoir_cs_mon.csv]]
  - [[reservoir_cs_yr.txt]]
  - [[reservoir_cs_yr.csv]]
  - [[reservoir_cs_aa.txt]]
  - [[reservoir_cs_aa.csv]]
  - [[rout_unit_cs_day.txt]]
  - [[rout_unit_cs_day.csv]]
  - [[rout_unit_cs_mon.txt]]
  - [[rout_unit_cs_mon.csv]]
  - [[rout_unit_cs_yr.txt]]
  - [[rout_unit_cs_yr.csv]]
  - [[rout_unit_cs_aa.txt]]
  - [[rout_unit_cs_aa.csv]]
  - [[wetland_cs_day.txt]]
  - [[wetland_cs_day.csv]]
  - [[wetland_cs_mon.txt]]
  - [[wetland_cs_mon.csv]]
  - [[wetland_cs_yr.txt]]
  - [[wetland_cs_yr.csv]]
  - [[wetland_cs_aa.txt]]
  - [[wetland_cs_aa.csv]]

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
