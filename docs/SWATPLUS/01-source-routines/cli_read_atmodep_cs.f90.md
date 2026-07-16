---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: cli_read_atmodep_cs.f90
note_file: cli_read_atmodep_cs.f90
subroutine: cli_read_atmodep_cs
module:
  - basin_module
  - input_file_module
  - climate_module
  - time_module
  - maximum_data_module
  - constituent_mass_module
calls: []
uses_variables:
  - climate_module.f90#atmodep_cont
  - climate_module.f90#atmodep_cs
  - climate_module.f90#cs_atmo
  - constituent_mass_module.f90#cs_db
input_variables:
  - climate_module.f90#atmodep_cs
reads:
  - cs_atmo.cli
writes: []
purpose: ""
---

# cli_read_atmodep_cs

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `cli_read_atmodep_cs.f90`
- **Modules used**:
  - [[basin_module.f90]]
  - [[input_file_module.f90]]
  - [[climate_module.f90]]
  - [[time_module.f90]]
  - [[maximum_data_module.f90]]
  - [[constituent_mass_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 1 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by:**

- [[proc_read.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[climate_module.f90#atmodep_cont]] - `atmospheric_deposition_control`
- [[climate_module.f90#atmodep_cs]] - `object_deposition_cs`
- [[climate_module.f90#cs_atmo]] - `character(len=1)`
- [[constituent_mass_module.f90#cs_db]] - `constituents`

**Populated by file reads:**

- [[climate_module.f90#atmodep_cs]]

## File I/O
- **Reads**:
  - [[cs_atmo.cli]]

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
