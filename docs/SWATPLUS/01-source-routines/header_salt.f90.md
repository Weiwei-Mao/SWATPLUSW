---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: header_salt.f90
note_file: header_salt.f90
subroutine: header_salt
module:
  - basin_module
  - reservoir_module
  - hydrograph_module
  - constituent_mass_module
  - ch_salt_module
  - res_salt_module
  - salt_module
  - salt_aquifer
  - output_path_module
calls:
  - open_output_file
uses_variables:
  - basin_module.f90#bsn
  - basin_module.f90#pco
  - basin_module.f90#prog
  - ch_salt_module.f90#chsalt_hdr
  - constituent_mass_module.f90#cs_db
  - constituent_mass_module.f90#rusaltb_hdr
  - hydrograph_module.f90#aqu
  - hydrograph_module.f90#res
  - hydrograph_module.f90#sp_ob
  - res_salt_module.f90#ressalt_hdr
  - salt_aquifer.f90#salt_hdr_aqu
  - salt_module.f90#salt_hdr_hru
  - salt_module.f90#saltb_hdr
input_variables: []
reads: []
writes:
  - basin_salt_day.txt
  - basin_salt_mon.txt
  - basin_salt_yr.txt
  - basin_salt_aa.txt
  - hru_salt_day.txt
  - hru_salt_day.csv
  - hru_salt_mon.txt
  - hru_salt_mon.csv
  - hru_salt_yr.txt
  - hru_salt_yr.csv
  - hru_salt_aa.txt
  - hru_salt_aa.csv
  - aquifer_salt_day.txt
  - aquifer_salt_day.csv
  - aquifer_salt_mon.txt
  - aquifer_salt_mon.csv
  - aquifer_salt_yr.txt
  - aquifer_salt_yr.csv
  - aquifer_salt_aa.txt
  - aquifer_salt_aa.csv
  - channel_salt_day.txt
  - channel_salt_day.csv
  - channel_salt_mon.txt
  - channel_salt_mon.csv
  - channel_salt_yr.txt
  - channel_salt_yr.csv
  - channel_salt_aa.txt
  - channel_salt_aa.csv
  - reservoir_salt_day.txt
  - reservoir_salt_day.csv
  - reservoir_salt_mon.txt
  - reservoir_salt_mon.csv
  - reservoir_salt_yr.txt
  - reservoir_salt_yr.csv
  - reservoir_salt_aa.txt
  - reservoir_salt_aa.csv
  - rout_unit_salt_day.txt
  - rout_unit_salt_day.csv
  - rout_unit_salt_mon.txt
  - rout_unit_salt_mon.csv
  - rout_unit_salt_yr.txt
  - rout_unit_salt_yr.csv
  - rout_unit_salt_aa.txt
  - rout_unit_salt_aa.csv
  - wetland_salt_day.txt
  - wetland_salt_day.csv
  - wetland_salt_mon.txt
  - wetland_salt_mon.csv
  - wetland_salt_yr.txt
  - wetland_salt_yr.csv
  - wetland_salt_aa.txt
  - wetland_salt_aa.csv
purpose: ""
---

# header_salt

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `header_salt.f90`
- **Modules used**:
  - [[basin_module.f90]]
  - [[reservoir_module.f90]]
  - [[hydrograph_module.f90]]
  - [[constituent_mass_module.f90]]
  - [[ch_salt_module.f90]]
  - [[res_salt_module.f90]]
  - [[salt_module.f90]]
  - [[salt_aquifer.f90]]
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
- [[ch_salt_module.f90#chsalt_hdr]] - `ch_salt_header`
- [[constituent_mass_module.f90#cs_db]] - `constituents`
- [[constituent_mass_module.f90#rusaltb_hdr]] - `output_rusaltb_header`
- [[hydrograph_module.f90#aqu]] - `hyd_output`
- [[hydrograph_module.f90#res]] - `hyd_output`
- [[hydrograph_module.f90#sp_ob]] - `spatial_objects`
- [[res_salt_module.f90#ressalt_hdr]] - `res_salt_header`
- [[salt_aquifer.f90#salt_hdr_aqu]] - `output_salt_header`
- [[salt_module.f90#salt_hdr_hru]] - `output_salt_hdr_hru`
- [[salt_module.f90#saltb_hdr]] - `output_saltbal_header`

## File I/O
- **Writes**:
  - [[basin_salt_day.txt]]
  - [[basin_salt_mon.txt]]
  - [[basin_salt_yr.txt]]
  - [[basin_salt_aa.txt]]
  - [[hru_salt_day.txt]]
  - [[hru_salt_day.csv]]
  - [[hru_salt_mon.txt]]
  - [[hru_salt_mon.csv]]
  - [[hru_salt_yr.txt]]
  - [[hru_salt_yr.csv]]
  - [[hru_salt_aa.txt]]
  - [[hru_salt_aa.csv]]
  - [[aquifer_salt_day.txt]]
  - [[aquifer_salt_day.csv]]
  - [[aquifer_salt_mon.txt]]
  - [[aquifer_salt_mon.csv]]
  - [[aquifer_salt_yr.txt]]
  - [[aquifer_salt_yr.csv]]
  - [[aquifer_salt_aa.txt]]
  - [[aquifer_salt_aa.csv]]
  - [[channel_salt_day.txt]]
  - [[channel_salt_day.csv]]
  - [[channel_salt_mon.txt]]
  - [[channel_salt_mon.csv]]
  - [[channel_salt_yr.txt]]
  - [[channel_salt_yr.csv]]
  - [[channel_salt_aa.txt]]
  - [[channel_salt_aa.csv]]
  - [[reservoir_salt_day.txt]]
  - [[reservoir_salt_day.csv]]
  - [[reservoir_salt_mon.txt]]
  - [[reservoir_salt_mon.csv]]
  - [[reservoir_salt_yr.txt]]
  - [[reservoir_salt_yr.csv]]
  - [[reservoir_salt_aa.txt]]
  - [[reservoir_salt_aa.csv]]
  - [[rout_unit_salt_day.txt]]
  - [[rout_unit_salt_day.csv]]
  - [[rout_unit_salt_mon.txt]]
  - [[rout_unit_salt_mon.csv]]
  - [[rout_unit_salt_yr.txt]]
  - [[rout_unit_salt_yr.csv]]
  - [[rout_unit_salt_aa.txt]]
  - [[rout_unit_salt_aa.csv]]
  - [[wetland_salt_day.txt]]
  - [[wetland_salt_day.csv]]
  - [[wetland_salt_mon.txt]]
  - [[wetland_salt_mon.csv]]
  - [[wetland_salt_yr.txt]]
  - [[wetland_salt_yr.csv]]
  - [[wetland_salt_aa.txt]]
  - [[wetland_salt_aa.csv]]

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
