---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: wet_salt.f90
note_file: wet_salt.f90
subroutine: wet_salt
module:
  - reservoir_data_module
  - reservoir_module
  - water_body_module
  - hydrograph_module
  - hru_module
  - constituent_mass_module
  - res_salt_module
  - climate_module
calls: []
reads: []
writes: []
purpose: "this subroutine computes the wetland salt ion mass balance"
---

# wet_salt

> [!info] Summary
> this subroutine computes the wetland salt ion mass balance

## Basic Information
- **Type**: `subroutine`
- **Source file**: `wet_salt.f90`
- **Modules used**: [[reservoir_data_module.f90]], [[reservoir_module.f90]], [[water_body_module.f90]], [[hydrograph_module.f90]], [[hru_module.f90]], [[constituent_mass_module.f90]], [[res_salt_module.f90]], [[climate_module.f90]]
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
