---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: header_hyd.f90
note_file: header_hyd.f90
subroutine: header_hyd
module:
  - basin_module
  - hydrograph_module
  - output_path_module
calls:
  - open_output_file
uses_variables:
  - basin_module.f90#bsn
  - basin_module.f90#pco
  - basin_module.f90#prog
  - hydrograph_module.f90#hyd_hdr
  - hydrograph_module.f90#hyd_hdr_obj
  - hydrograph_module.f90#hyd_hdr_time
  - hydrograph_module.f90#hyd_hdr_units
  - hydrograph_module.f90#hyd_hdr_units2
input_variables: []
reads: []
writes:
  - hydcon.out
  - hydcon.csv
  - hydout_day.txt
  - hydout_day.csv
  - hydout_mon.txt
  - hydout_mon.csv
  - hydout_yr.txt
  - hydout_yr.csv
  - hydout_aa.txt
  - hydout_aa.csv
  - hydin_day.txt
  - hydin_day.csv
  - hydin_mon.txt
  - hydin_mon.csv
  - hydin_yr.txt
  - hydin_yr.csv
  - hydin_aa.txt
  - hydin_aa.csv
  - deposition_day.txt
  - deposition_day.csv
  - deposition_mon.txt
  - deposition_mon.csv
  - deposition_yr.txt
  - deposition_yr.csv
  - deposition_aa.txt
  - deposition_aa.csv
purpose: ""
---

# header_hyd

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `header_hyd.f90`
- **Modules used**:
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
- [[hydrograph_module.f90#hyd_hdr]] - `hyd_header`
- [[hydrograph_module.f90#hyd_hdr_obj]] - `hyd_header_obj`
- [[hydrograph_module.f90#hyd_hdr_time]] - `hyd_header_time`
- [[hydrograph_module.f90#hyd_hdr_units]] - `hyd_header_units`
- [[hydrograph_module.f90#hyd_hdr_units2]] - `hyd_header_units2`

## File I/O
- **Writes**:
  - [[hydcon.out]]
  - [[hydcon.csv]]
  - [[hydout_day.txt]]
  - [[hydout_day.csv]]
  - [[hydout_mon.txt]]
  - [[hydout_mon.csv]]
  - [[hydout_yr.txt]]
  - [[hydout_yr.csv]]
  - [[hydout_aa.txt]]
  - [[hydout_aa.csv]]
  - [[hydin_day.txt]]
  - [[hydin_day.csv]]
  - [[hydin_mon.txt]]
  - [[hydin_mon.csv]]
  - [[hydin_yr.txt]]
  - [[hydin_yr.csv]]
  - [[hydin_aa.txt]]
  - [[hydin_aa.csv]]
  - [[deposition_day.txt]]
  - [[deposition_day.csv]]
  - [[deposition_mon.txt]]
  - [[deposition_mon.csv]]
  - [[deposition_yr.txt]]
  - [[deposition_yr.csv]]
  - [[deposition_aa.txt]]
  - [[deposition_aa.csv]]

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
