---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: wallo_control.f90
note_file: wallo_control.f90
subroutine: wallo_control
module:
  - water_allocation_module
  - hydrograph_module
  - hru_module
  - basin_module
  - time_module
  - plant_module
  - soil_module
  - reservoir_module
  - sd_channel_module
  - organic_mineral_mass_module
  - constituent_mass_module
calls:
  - wallo_demand
  - wallo_withdraw
  - wallo_transfer
  - salt_irrig
  - cs_irrig
  - res_control
  - wallo_treatment
  - wallo_use
  - wallo_canal
reads: []
writes: []
purpose: ""
---

# wallo_control

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `wallo_control.f90`
- **Modules used**: [[water_allocation_module.f90]], [[hydrograph_module.f90]], [[hru_module.f90]], [[basin_module.f90]], [[time_module.f90]], [[plant_module.f90]], [[soil_module.f90]], [[reservoir_module.f90]], [[sd_channel_module.f90]], [[organic_mineral_mass_module.f90]], [[constituent_mass_module.f90]]
- **Subroutine calls**: 9 | **Files read**: 0 | **Files written**: 0

## Call Relationships
**This routine calls:**

- [[wallo_demand.f90]]
- [[wallo_withdraw.f90]]
- [[wallo_transfer.f90]]
- [[salt_irrig.f90]]
- [[cs_irrig.f90]]
- [[res_control.f90]]
- [[wallo_treatment.f90]]
- [[wallo_use.f90]]
- [[wallo_canal.f90]]

**Called by** (live Dataview back-query):

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
