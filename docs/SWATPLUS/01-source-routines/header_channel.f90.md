---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: header_channel.f90
note_file: header_channel.f90
subroutine: header_channel
module:
  - channel_module
  - basin_module
  - hydrograph_module
  - output_path_module
calls:
  - open_output_file
uses_variables:
  - basin_module.f90#bsn
  - basin_module.f90#pco
  - basin_module.f90#prog
  - channel_module.f90#ch_hdr
  - channel_module.f90#ch_hdr_units
  - hydrograph_module.f90#sp_ob
input_variables: []
reads: []
writes:
  - channel_day.txt
  - channel_day.csv
  - channel_mon.txt
  - channel_mon.csv
  - channel_yr.txt
  - channel_yr.csv
  - channel_aa.txt
  - channel_aa.csv
purpose: ""
---

# header_channel

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `header_channel.f90`
- **Modules used**:
  - [[channel_module.f90]]
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
- [[basin_module.f90#bsn]] - `basin_inputs`
- [[basin_module.f90#pco]] - `basin_print_codes`
- [[basin_module.f90#prog]] - `character(len=80)`
- [[channel_module.f90#ch_hdr]] - `ch_header`
- [[channel_module.f90#ch_hdr_units]] - `ch_header_units`
- [[hydrograph_module.f90#sp_ob]] - `spatial_objects`

## File I/O
- **Writes**:
  - [[channel_day.txt]]
  - [[channel_day.csv]]
  - [[channel_mon.txt]]
  - [[channel_mon.csv]]
  - [[channel_yr.txt]]
  - [[channel_yr.csv]]
  - [[channel_aa.txt]]
  - [[channel_aa.csv]]

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
