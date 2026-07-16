---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: salt_hru_init.f90
note_file: salt_hru_init.f90
subroutine: salt_hru_init
module:
  - hru_module
  - soil_module
  - organic_mineral_mass_module
  - constituent_mass_module
  - output_ls_pesticide_module
  - hydrograph_module
  - plant_module
  - pesticide_data_module
  - salt_module
calls: []
reads: []
writes: []
purpose: "this subroutine calls subroutines which read input data for the; databases and the HRUs"
---

# salt_hru_init

> [!info] Summary
> this subroutine calls subroutines which read input data for the; databases and the HRUs

## Basic Information
- **Type**: `subroutine`
- **Source file**: `salt_hru_init.f90`
- **Modules used**: [[hru_module.f90]], [[soil_module.f90]], [[organic_mineral_mass_module.f90]], [[constituent_mass_module.f90]], [[output_ls_pesticide_module.f90]], [[hydrograph_module.f90]], [[plant_module.f90]], [[pesticide_data_module.f90]], [[salt_module.f90]]
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
