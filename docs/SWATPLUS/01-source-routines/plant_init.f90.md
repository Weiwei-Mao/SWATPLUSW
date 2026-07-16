---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: plant_init.f90
note_file: plant_init.f90
subroutine: plant_init
module:
  - hru_module
  - soil_module
  - plant_module
  - hydrograph_module
  - climate_module
  - time_module
  - maximum_data_module
  - plant_data_module
  - landuse_data_module
  - mgt_operations_module
  - urban_data_module
  - conditional_module
  - organic_mineral_mass_module
calls:
  - xmon
  - pl_root_gro
  - pl_seed_gro
  - pl_partition
  - pl_rootfr
reads: []
writes: []
purpose: ""
---

# plant_init

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `plant_init.f90`
- **Modules used**: [[hru_module.f90]], [[soil_module.f90]], [[plant_module.f90]], [[hydrograph_module.f90]], [[climate_module.f90]], [[time_module.f90]], [[maximum_data_module.f90]], [[plant_data_module.f90]], [[landuse_data_module.f90]], [[mgt_operations_module.f90]], [[urban_data_module.f90]], [[conditional_module.f90]], [[organic_mineral_mass_module.f90]]
- **Subroutine calls**: 5 | **Files read**: 0 | **Files written**: 0

## Call Relationships
**This routine calls:**

- [[xmon.f90]]
- [[pl_root_gro.f90]]
- [[pl_seed_gro.f90]]
- [[pl_partition.f90]]
- [[pl_rootfr.f90]]

**Called by** (live Dataview back-query):

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
