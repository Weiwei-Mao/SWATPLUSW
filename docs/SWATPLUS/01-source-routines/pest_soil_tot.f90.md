---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: pest_soil_tot.f90
note_file: pest_soil_tot.f90
subroutine: pest_soil_tot
module:
  - pesticide_data_module
  - hru_module
  - soil_module
  - constituent_mass_module
  - output_ls_pesticide_module
  - plant_module
calls: []
reads: []
writes: []
purpose: "this subroutine calculates the total amount of pesticide in the soil"
---

# pest_soil_tot

> [!info] Summary
> this subroutine calculates the total amount of pesticide in the soil

## Basic Information
- **Type**: `subroutine`
- **Source file**: `pest_soil_tot.f90`
- **Modules used**: [[pesticide_data_module.f90]], [[hru_module.f90]], [[soil_module.f90]], [[constituent_mass_module.f90]], [[output_ls_pesticide_module.f90]], [[plant_module.f90]]
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
