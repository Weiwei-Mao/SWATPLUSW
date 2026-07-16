---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: gwflow_pump_allo.f90
note_file: gwflow_pump_allo.f90
subroutine: gwflow_pump_allo
module:
  - gwflow_module
  - organic_mineral_mass_module
  - hru_module
  - hydrograph_module
  - soil_module
  - constituent_mass_module
  - res_salt_module
  - res_cs_module
  - salt_module
  - cs_module
calls: []
reads: []
writes: []
purpose: "this subroutine determines the volume of groundwater that is extracted; from gwflow grid cells; (pumping volume are used in gwflow_simulate, in groundwater balance equations)"
---

# gwflow_pump_allo

> [!info] Summary
> this subroutine determines the volume of groundwater that is extracted; from gwflow grid cells; (pumping volume are used in gwflow_simulate, in groundwater balance equations)

## Basic Information
- **Type**: `subroutine`
- **Source file**: `gwflow_pump_allo.f90`
- **Modules used**: [[gwflow_module.f90]], [[organic_mineral_mass_module.f90]], [[hru_module.f90]], [[hydrograph_module.f90]], [[soil_module.f90]], [[constituent_mass_module.f90]], [[res_salt_module.f90]], [[res_cs_module.f90]], [[salt_module.f90]], [[cs_module.f90]]
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
