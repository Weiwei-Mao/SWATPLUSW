---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: recall_read.f90
note_file: recall_read.f90
subroutine: recalldb_read
module:
  - water_allocation_module
  - maximum_data_module
  - recall_module
  - hydrograph_module
  - input_file_module
  - organic_mineral_mass_module
  - constituent_mass_module
  - time_module
  - exco_module
calls:
  - recall_read
uses_variables:
  - constituent_mass_module.f90#rec_pest
  - hydrograph_module.f90#hd
  - hydrograph_module.f90#ht1
  - hydrograph_module.f90#rec_a
  - hydrograph_module.f90#rec_d
  - hydrograph_module.f90#rec_m
  - hydrograph_module.f90#rec_y
  - hydrograph_module.f90#recall
  - maximum_data_module.f90#db_mx
  - recall_module.f90#recall_db
  - time_module.f90#time
input_variables:
  - constituent_mass_module.f90#rec_pest
  - hydrograph_module.f90#ht1
  - hydrograph_module.f90#recall
  - recall_module.f90#recall_db
reads:
  - recall_db.rec
  - pest.com
writes: []
purpose: ""
---

# recalldb_read

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `recall_read.f90`
- **Modules used**:
  - [[water_allocation_module.f90]]
  - [[maximum_data_module.f90]]
  - [[recall_module.f90]]
  - [[hydrograph_module.f90]]
  - [[input_file_module.f90]]
  - [[organic_mineral_mass_module.f90]]
  - [[constituent_mass_module.f90]]
  - [[time_module.f90]]
  - [[exco_module.f90]]
- **Subroutine calls**: 1 | **Files read**: 2 | **Files written**: 0

## Call Relationships
**This routine calls:**

- `recall_read`

**Called by:**

- [[main.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[constituent_mass_module.f90#rec_pest]] - `recall_pesticide_inputs`
- [[hydrograph_module.f90#hd]] - `hyd_output`
- [[hydrograph_module.f90#ht1]] - `hyd_output`
- [[hydrograph_module.f90#rec_a]] - `hyd_output`
- [[hydrograph_module.f90#rec_d]] - `hyd_output`
- [[hydrograph_module.f90#rec_m]] - `hyd_output`
- [[hydrograph_module.f90#rec_y]] - `hyd_output`
- [[hydrograph_module.f90#recall]] - `recall_hydrograph_inputs`
- [[maximum_data_module.f90#db_mx]] - `data_files_max_elements`
- [[recall_module.f90#recall_db]] - `recall_databases`
- [[time_module.f90#time]] - `time_current`

**Populated by file reads:**

- [[constituent_mass_module.f90#rec_pest]]
- [[hydrograph_module.f90#ht1]]
- [[hydrograph_module.f90#recall]]
- [[recall_module.f90#recall_db]]

## File I/O
- **Reads**:
  - [[recall_db.rec]]
  - [[pest.com]]

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
