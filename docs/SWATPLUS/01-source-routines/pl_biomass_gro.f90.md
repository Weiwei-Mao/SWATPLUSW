---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: pl_biomass_gro.f90
note_file: pl_biomass_gro.f90
subroutine: pl_biomass_gro
module:
  - plant_data_module
  - basin_module
  - hru_module
  - plant_module
  - carbon_module
  - organic_mineral_mass_module
  - climate_module
  - hydrograph_module
  - constituent_mass_module
  - salt_module
  - salt_data_module
  - output_landscape_module
calls:
  - pl_tstr
  - pl_nup
  - pl_pup
  - salt_uptake
  - cs_uptake
reads: []
writes: []
purpose: ""
---

# pl_biomass_gro

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `pl_biomass_gro.f90`
- **Modules used**: [[plant_data_module.f90]], [[basin_module.f90]], [[hru_module.f90]], [[plant_module.f90]], [[carbon_module.f90]], [[organic_mineral_mass_module.f90]], [[climate_module.f90]], [[hydrograph_module.f90]], [[constituent_mass_module.f90]], [[salt_module.f90]], [[salt_data_module.f90]], [[output_landscape_module.f90]]
- **Subroutine calls**: 5 | **Files read**: 0 | **Files written**: 0

## Call Relationships
**This routine calls:**

- [[pl_tstr.f90]]
- [[pl_nup.f90]]
- [[pl_pup.f90]]
- [[salt_uptake.f90]]
- [[cs_uptake.f90]]

**Called by** (live Dataview back-query):

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
