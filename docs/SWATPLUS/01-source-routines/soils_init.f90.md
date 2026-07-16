---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: soils_init.f90
note_file: soils_init.f90
subroutine: soils_init
module:
  - hru_module
  - soil_module
  - plant_module
  - maximum_data_module
  - soil_data_module
  - organic_mineral_mass_module
  - constituent_mass_module
  - hydrograph_module
  - time_module
  - basin_module
  - septic_data_module
calls:
  - soils_test_adjust
  - soil_phys_init
  - layersplit
reads:
  - soil_lyr_depths.sol
writes: []
purpose: ""
---

# soils_init

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `soils_init.f90`
- **Modules used**: [[hru_module.f90]], [[soil_module.f90]], [[plant_module.f90]], [[maximum_data_module.f90]], [[soil_data_module.f90]], [[organic_mineral_mass_module.f90]], [[constituent_mass_module.f90]], [[hydrograph_module.f90]], [[time_module.f90]], [[basin_module.f90]], [[septic_data_module.f90]]
- **Subroutine calls**: 3 | **Files read**: 1 | **Files written**: 0

## Call Relationships
**This routine calls:**

- [[soils_test_adjust.f90]]
- [[soil_phys_init.f90]]
- [[layersplit.f90]]

**Called by** (live Dataview back-query):

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## File I/O
- **Reads**: `soil_lyr_depths.sol`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
