---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: pl_grow.f90
note_file: pl_grow.f90
subroutine: pl_grow
module:
  - plant_data_module
  - basin_module
  - hru_module
  - plant_module
  - carbon_module
  - organic_mineral_mass_module
  - time_module
  - output_landscape_module
calls:
  - pl_nut_demand
  - pl_dormant
  - pl_biomass_gro
  - pl_root_gro
  - pl_leaf_gro
  - pl_leaf_senes
  - pl_seed_gro
  - pl_partition
  - pl_mortality
reads: []
writes: []
purpose: ""
---

# pl_grow

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `pl_grow.f90`
- **Modules used**: [[plant_data_module.f90]], [[basin_module.f90]], [[hru_module.f90]], [[plant_module.f90]], [[carbon_module.f90]], [[organic_mineral_mass_module.f90]], [[time_module.f90]], [[output_landscape_module.f90]]
- **Subroutine calls**: 9 | **Files read**: 0 | **Files written**: 0

## Call Relationships
**This routine calls:**

- [[pl_nut_demand.f90]]
- [[pl_dormant.f90]]
- [[pl_biomass_gro.f90]]
- [[pl_root_gro.f90]]
- [[pl_leaf_gro.f90]]
- [[pl_leaf_senes.f90]]
- [[pl_seed_gro.f90]]
- [[pl_partition.f90]]
- [[pl_mortality.f90]]

**Called by** (live Dataview back-query):

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
