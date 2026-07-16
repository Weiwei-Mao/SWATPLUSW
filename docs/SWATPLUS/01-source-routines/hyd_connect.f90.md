---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: hyd_connect.f90
note_file: hyd_connect.f90
subroutine: hyd_connect
module:
  - hydrograph_module
  - input_file_module
  - recall_module
  - organic_mineral_mass_module
  - constituent_mass_module
  - ru_module
  - basin_module
calls:
  - hyd_read_connect
  - ru_read
  - ru_read_elements
  - aqu2d_read
  - overbank_read
  - dr_db_read
  - gwflow_chan_read
  - gwflow_read
  - exit
reads: []
writes:
  - looping.con
purpose: "reads in the routing information from the watershed configuration; input file (.fig) and calculates the number of subbasins, reaches,; and reservoirs"
---

# hyd_connect

> [!info] Summary
> reads in the routing information from the watershed configuration; input file (.fig) and calculates the number of subbasins, reaches,; and reservoirs

## Basic Information
- **Type**: `subroutine`
- **Source file**: `hyd_connect.f90`
- **Modules used**: [[hydrograph_module.f90]], [[input_file_module.f90]], [[recall_module.f90]], [[organic_mineral_mass_module.f90]], [[constituent_mass_module.f90]], [[ru_module.f90]], [[basin_module.f90]]
- **Subroutine calls**: 9 | **Files read**: 0 | **Files written**: 1

## Call Relationships
**This routine calls:**

- [[hyd_read_connect.f90]]
- [[ru_read.f90]]
- [[ru_read_elements.f90]]
- [[aqu2d_read.f90]]
- [[overbank_read.f90]]
- [[dr_db_read.f90]]
- [[gwflow_chan_read.f90]]
- [[gwflow_read.f90]]
- `exit`

**Called by** (live Dataview back-query):

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## File I/O
- **Writes**: `looping.con`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
