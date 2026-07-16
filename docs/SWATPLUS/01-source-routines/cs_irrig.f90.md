---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: cs_irrig.f90
note_file: cs_irrig.f90
subroutine: cs_irrig
module:
  - water_allocation_module
  - water_body_module
  - aquifer_module
  - reservoir_data_module
  - hydrograph_module
  - hru_module
  - cs_module
  - cs_aquifer
  - ch_cs_module
  - res_cs_module
  - basin_module
  - constituent_mass_module
calls: []
reads: []
writes: []
purpose: "this subroutine adds constituent mass from irrigation water into the soil profile, and removes constituent mass; from the source object"
---

# cs_irrig

> [!info] Summary
> this subroutine adds constituent mass from irrigation water into the soil profile, and removes constituent mass; from the source object

## Basic Information
- **Type**: `subroutine`
- **Source file**: `cs_irrig.f90`
- **Modules used**: [[water_allocation_module.f90]], [[water_body_module.f90]], [[aquifer_module.f90]], [[reservoir_data_module.f90]], [[hydrograph_module.f90]], [[hru_module.f90]], [[cs_module.f90]], [[cs_aquifer.f90]], [[ch_cs_module.f90]], [[res_cs_module.f90]], [[basin_module.f90]], [[constituent_mass_module.f90]]
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
