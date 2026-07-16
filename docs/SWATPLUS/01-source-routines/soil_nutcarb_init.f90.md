---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: soil_nutcarb_init.f90
note_file: soil_nutcarb_init.f90
subroutine: soil_nutcarb_init
module:
  - hru_module
  - soil_module
  - soil_data_module
  - basin_module
  - organic_mineral_mass_module
  - carbon_module
  - tillage_data_module
calls: []
reads: []
writes: []
purpose: "this subroutine initializes soil chemical properties; and intial soil layer bmix efficiency"
---

# soil_nutcarb_init

> [!info] Summary
> this subroutine initializes soil chemical properties; and intial soil layer bmix efficiency

## Basic Information
- **Type**: `subroutine`
- **Source file**: `soil_nutcarb_init.f90`
- **Modules used**: [[hru_module.f90]], [[soil_module.f90]], [[soil_data_module.f90]], [[basin_module.f90]], [[organic_mineral_mass_module.f90]], [[carbon_module.f90]], [[tillage_data_module.f90]]
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
