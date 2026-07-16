---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: cs_str_output.f90
note_file: cs_str_output.f90
subroutine: cs_str_output
module:
  - hydrograph_module
  - constituent_mass_module
  - ch_cs_module
  - time_module
calls: []
uses_variables:
  - ch_cs_module.f90#chcs_d
  - constituent_mass_module.f90#cs_obs_file
  - constituent_mass_module.f90#cs_str_nobs
  - constituent_mass_module.f90#cs_str_obs
  - hydrograph_module.f90#ch_out_d
  - time_module.f90#time
input_variables: []
reads: []
writes: []
purpose: "this subroutine prints out daily constituent data for specified channels"
---

# cs_str_output

> [!info] Summary
> this subroutine prints out daily constituent data for specified channels

## Basic Information
- **Type**: `subroutine`
- **Source file**: `cs_str_output.f90`
- **Modules used**:
  - [[hydrograph_module.f90]]
  - [[constituent_mass_module.f90]]
  - [[ch_cs_module.f90]]
  - [[time_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 0 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by:**

- [[command.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[ch_cs_module.f90#chcs_d]] - `ch_cs_output`
- [[constituent_mass_module.f90#cs_obs_file]] - `integer`
- [[constituent_mass_module.f90#cs_str_nobs]] - `integer`
- [[constituent_mass_module.f90#cs_str_obs]] - `integer, dimension (:), allocatable`
- [[hydrograph_module.f90#ch_out_d]] - `hyd_output`
- [[time_module.f90#time]] - `time_current`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
