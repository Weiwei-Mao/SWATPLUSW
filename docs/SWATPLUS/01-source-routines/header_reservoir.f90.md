---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: header_reservoir.f90
note_file: header_reservoir.f90
subroutine: header_reservoir
module:
  - basin_module
  - reservoir_module
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
  - hydrograph_module.f90#hyd_hdr_units3
  - hydrograph_module.f90#hyd_in_hdr
  - hydrograph_module.f90#hyd_out_hdr
  - hydrograph_module.f90#hyd_stor_hdr
  - hydrograph_module.f90#res
  - hydrograph_module.f90#sp_ob
input_variables: []
reads: []
writes:
  - reservoir_day.txt
  - reservoir_day.csv
  - reservoir_mon.txt
  - reservoir_mon.csv
  - reservoir_yr.txt
  - reservoir_yr.csv
  - reservoir_aa.txt
  - reservoir_aa.csv
purpose: ""
---

# header_reservoir

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `header_reservoir.f90`
- **Modules used**:
  - [[basin_module.f90]]
  - [[reservoir_module.f90]]
  - [[hydrograph_module.f90]]
  - [[output_path_module.f90]]
- **Subroutine calls**: 1 | **Files read**: 0 | **Files written**: 8

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
- [[hydrograph_module.f90#hyd_hdr_units3]] - `hyd_header_units3`
- [[hydrograph_module.f90#hyd_in_hdr]] - `hyd_in_header`
- [[hydrograph_module.f90#hyd_out_hdr]] - `hyd_out_header`
- [[hydrograph_module.f90#hyd_stor_hdr]] - `hyd_stor_header`
- [[hydrograph_module.f90#res]] - `hyd_output`
- [[hydrograph_module.f90#sp_ob]] - `spatial_objects`

## File I/O
- **Writes**:
  - [[reservoir_day.txt]]
  - [[reservoir_day.csv]]
  - [[reservoir_mon.txt]]
  - [[reservoir_mon.csv]]
  - [[reservoir_yr.txt]]
  - [[reservoir_yr.csv]]
  - [[reservoir_aa.txt]]
  - [[reservoir_aa.csv]]

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
