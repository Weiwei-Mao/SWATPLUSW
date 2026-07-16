---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: salt_balance.f90
note_file: salt_balance.f90
subroutine: salt_balance
module:
  - hydrograph_module
  - organic_mineral_mass_module
  - output_landscape_module
  - aquifer_module
  - hru_module
  - soil_module
  - time_module
  - salt_module
  - salt_aquifer
  - constituent_mass_module
  - res_salt_module
  - ch_salt_module
  - gwflow_module
calls: []
reads: []
writes: []
purpose: "this subroutine calculates total salt in system and writes out data to perform; a system-wide salt mass balance."
---

# salt_balance

> [!info] Summary
> this subroutine calculates total salt in system and writes out data to perform; a system-wide salt mass balance.

## Basic Information
- **Type**: `subroutine`
- **Source file**: `salt_balance.f90`
- **Modules used**: [[hydrograph_module.f90]], [[organic_mineral_mass_module.f90]], [[output_landscape_module.f90]], [[aquifer_module.f90]], [[hru_module.f90]], [[soil_module.f90]], [[time_module.f90]], [[salt_module.f90]], [[salt_aquifer.f90]], [[constituent_mass_module.f90]], [[res_salt_module.f90]], [[ch_salt_module.f90]], [[gwflow_module.f90]]
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
