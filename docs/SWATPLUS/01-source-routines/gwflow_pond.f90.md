---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: gwflow_pond.f90
note_file: gwflow_pond.f90
subroutine: gwflow_pond
module:
  - gwflow_module
  - hydrograph_module
  - time_module
  - constituent_mass_module
  - water_allocation_module
  - climate_module
calls: []
reads: []
writes: []
purpose: "this subroutine calculates the volume of seepage from recharge ponds;; removes water from source channel or canal diversion;; writes out recharge pond water balance"
---

# gwflow_pond

> [!info] Summary
> this subroutine calculates the volume of seepage from recharge ponds;; removes water from source channel or canal diversion;; writes out recharge pond water balance

## Basic Information
- **Type**: `subroutine`
- **Source file**: `gwflow_pond.f90`
- **Modules used**: [[gwflow_module.f90]], [[hydrograph_module.f90]], [[time_module.f90]], [[constituent_mass_module.f90]], [[water_allocation_module.f90]], [[climate_module.f90]]
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
