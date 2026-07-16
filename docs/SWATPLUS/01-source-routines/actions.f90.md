---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: actions.f90
note_file: actions.f90
subroutine: actions
module:
  - conditional_module
  - climate_module
  - time_module
  - aquifer_module
  - hru_module
  - soil_module
  - plant_module
  - plant_data_module
  - mgt_operations_module
  - landuse_data_module
  - tillage_data_module
  - reservoir_module
  - sd_channel_module
  - septic_data_module
  - hru_lte_module
  - basin_module
  - organic_mineral_mass_module
  - hydrograph_module
  - output_landscape_module
  - constituent_mass_module
  - calibration_data_module
  - fertilizer_data_module
  - maximum_data_module
  - tiles_data_module
  - water_body_module
  - reservoir_data_module
  - manure_allocation_module
  - water_allocation_module
calls:
  - pl_fert_wet
  - pl_fert
  - pl_manure
  - salt_fert
  - cs_fert
  - mgt_newtillmix_cswat1
  - mgt_newtillmix_cswat0
  - mgt_transplant
  - mgt_harvbiomass
  - mgt_harvgrain
  - mgt_harvresidue
  - mgt_harvtuber
  - mgt_killop
  - pest_apply
  - pl_graze
  - wet_initial
  - mgt_newtillmix_wet
  - hru_fr_change
  - hru_lum_init
  - plant_init
  - cn2_init
  - structure_set_parms
  - pl_burnop
  - curno
reads: []
writes: []
purpose: ""
---

# actions

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `actions.f90`
- **Modules used**: [[conditional_module.f90]], [[climate_module.f90]], [[time_module.f90]], [[aquifer_module.f90]], [[hru_module.f90]], [[soil_module.f90]], [[plant_module.f90]], [[plant_data_module.f90]], [[mgt_operations_module.f90]], [[landuse_data_module.f90]], [[tillage_data_module.f90]], [[reservoir_module.f90]], [[sd_channel_module.f90]], [[septic_data_module.f90]], [[hru_lte_module.f90]], [[basin_module.f90]], [[organic_mineral_mass_module.f90]], [[hydrograph_module.f90]], [[output_landscape_module.f90]], [[constituent_mass_module.f90]], [[calibration_data_module.f90]], [[fertilizer_data_module.f90]], [[maximum_data_module.f90]], [[tiles_data_module.f90]], [[water_body_module.f90]], [[reservoir_data_module.f90]], [[manure_allocation_module.f90]], [[water_allocation_module.f90]]
- **Subroutine calls**: 24 | **Files read**: 0 | **Files written**: 0

## Call Relationships
**This routine calls:**

- [[pl_fert_wet.f90]]
- [[pl_fert.f90]]
- [[pl_manure.f90]]
- [[salt_fert.f90]]
- [[cs_fert.f90]]
- [[mgt_newtillmix_cswat1.f90]]
- [[mgt_newtillmix_cswat0.f90]]
- [[mgt_transplant.f90]]
- [[mgt_harvbiomass.f90]]
- [[mgt_harvgrain.f90]]
- [[mgt_harvresidue.f90]]
- [[mgt_harvtuber.f90]]
- [[mgt_killop.f90]]
- [[pest_apply.f90]]
- [[pl_graze.f90]]
- [[wet_initial.f90]]
- [[mgt_newtillmix_wet.f90]]
- [[hru_fr_change.f90]]
- [[hru_lum_init.f90]]
- [[plant_init.f90]]
- [[cn2_init.f90]]
- [[structure_set_parms.f90]]
- [[pl_burnop.f90]]
- [[curno.f90]]

**Called by** (live Dataview back-query):

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
