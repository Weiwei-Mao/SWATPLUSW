---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: recall_read_cs.f90
note_file: recall_read_cs.f90
subroutine: recall_read_cs
module:
  - hydrograph_module
  - input_file_module
  - organic_mineral_mass_module
  - constituent_mass_module
  - maximum_data_module
  - time_module
  - exco_module
calls: []
uses_variables:
  - constituent_mass_module.f90#cs_db
  - constituent_mass_module.f90#rec_cs
  - constituent_mass_module.f90#reccsb_a
  - constituent_mass_module.f90#reccsb_d
  - constituent_mass_module.f90#reccsb_m
  - constituent_mass_module.f90#reccsb_y
  - constituent_mass_module.f90#recoutcsb_a
  - constituent_mass_module.f90#recoutcsb_d
  - constituent_mass_module.f90#recoutcsb_m
  - constituent_mass_module.f90#recoutcsb_y
  - input_file_module.f90#in_rec
  - time_module.f90#time
input_variables:
  - constituent_mass_module.f90#rec_cs
reads:
  - cs_recall.rec
writes: []
purpose: ""
---

# recall_read_cs

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `recall_read_cs.f90`
- **Modules used**:
  - [[hydrograph_module.f90]]
  - [[input_file_module.f90]]
  - [[organic_mineral_mass_module.f90]]
  - [[constituent_mass_module.f90]]
  - [[maximum_data_module.f90]]
  - [[time_module.f90]]
  - [[exco_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 1 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by:**

(No static callers detected.)

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[constituent_mass_module.f90#cs_db]] - `constituents`
- [[constituent_mass_module.f90#rec_cs]] - `recall_cs_inputs`
- [[constituent_mass_module.f90#reccsb_a]] - `constituent_mass`
- [[constituent_mass_module.f90#reccsb_d]] - `constituent_mass`
- [[constituent_mass_module.f90#reccsb_m]] - `constituent_mass`
- [[constituent_mass_module.f90#reccsb_y]] - `constituent_mass`
- [[constituent_mass_module.f90#recoutcsb_a]] - `constituent_mass`
- [[constituent_mass_module.f90#recoutcsb_d]] - `constituent_mass`
- [[constituent_mass_module.f90#recoutcsb_m]] - `constituent_mass`
- [[constituent_mass_module.f90#recoutcsb_y]] - `constituent_mass`
- [[input_file_module.f90#in_rec]] - `input_rec`
- [[time_module.f90#time]] - `time_current`

**Populated by file reads:**

- [[constituent_mass_module.f90#rec_cs]]

## File I/O
- **Reads**:
  - [[cs_recall.rec]]

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
