---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: header_aquifer.f90
note_file: header_aquifer.f90
subroutine: header_aquifer
module:
  - aquifer_module
  - basin_module
  - hydrograph_module
  - output_path_module
calls:
  - open_output_file
uses_variables:
  - aquifer_module.f90#aqu_hdr
  - aquifer_module.f90#aqu_hdr_units
  - basin_module.f90#bsn
  - basin_module.f90#pco
  - basin_module.f90#prog
  - hydrograph_module.f90#aqu
  - hydrograph_module.f90#sp_ob
input_variables: []
reads: []
writes:
  - aquifer_day.txt
  - aquifer_day.csv
  - aquifer_mon.txt
  - aquifer_mon.csv
  - aquifer_yr.txt
  - aquifer_yr.csv
  - aquifer_aa.txt
  - aquifer_aa.csv
purpose: ""
---

# header_aquifer

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `header_aquifer.f90`
- **Modules used**:
  - [[aquifer_module.f90]]
  - [[basin_module.f90]]
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
- [[aquifer_module.f90#aqu_hdr]] - `aqu_header`
- [[aquifer_module.f90#aqu_hdr_units]] - `aqu_header_units`
- [[basin_module.f90#bsn]] - `basin_inputs`
- [[basin_module.f90#pco]] - `basin_print_codes`
- [[basin_module.f90#prog]] - `character(len=80)`
- [[hydrograph_module.f90#aqu]] - `hyd_output`
- [[hydrograph_module.f90#sp_ob]] - `spatial_objects`

## File I/O
- **Writes**:
  - [[aquifer_day.txt]]
  - [[aquifer_day.csv]]
  - [[aquifer_mon.txt]]
  - [[aquifer_mon.csv]]
  - [[aquifer_yr.txt]]
  - [[aquifer_yr.csv]]
  - [[aquifer_aa.txt]]
  - [[aquifer_aa.csv]]

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
