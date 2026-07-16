---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: cs_balance.f90
note_file: cs_balance.f90
subroutine: cs_balance
module:
  - hydrograph_module
  - organic_mineral_mass_module
  - output_landscape_module
  - aquifer_module
  - hru_module
  - soil_module
  - time_module
  - constituent_mass_module
  - cs_module
  - cs_aquifer
  - res_cs_module
  - ch_cs_module
  - gwflow_module
calls: []
reads: []
writes: []
purpose: "this subroutine calculates total constituent mass in system and writes out data to perform; a system-wide constituent mass balance"
---

# cs_balance

> [!info] Summary
> this subroutine calculates total constituent mass in system and writes out data to perform; a system-wide constituent mass balance

## Basic Information
- **Type**: `subroutine`
- **Source file**: `cs_balance.f90`
- **Modules used**: [[hydrograph_module.f90]], [[organic_mineral_mass_module.f90]], [[output_landscape_module.f90]], [[aquifer_module.f90]], [[hru_module.f90]], [[soil_module.f90]], [[time_module.f90]], [[constituent_mass_module.f90]], [[cs_module.f90]], [[cs_aquifer.f90]], [[res_cs_module.f90]], [[ch_cs_module.f90]], [[gwflow_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 0 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by** (live Dataview back-query):

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
