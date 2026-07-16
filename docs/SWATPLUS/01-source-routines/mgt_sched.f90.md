---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: mgt_sched.f90
note_file: mgt_sched.f90
subroutine: mgt_sched
module:
  - plant_data_module
  - mgt_operations_module
  - tillage_data_module
  - basin_module
  - hydrograph_module
  - hru_module
  - soil_module
  - plant_module
  - time_module
  - constituent_mass_module
  - organic_mineral_mass_module
  - calibration_data_module
  - reservoir_data_module
  - reservoir_module
  - maximum_data_module
  - aquifer_module
calls:
  - mgt_plantop
  - mgt_transplant
  - mgt_harvbiomass
  - mgt_harvgrain
  - mgt_harvresidue
  - mgt_harvtuber
  - mgt_killop
  - mgt_newtillmix_cswat1
  - mgt_newtillmix_cswat0
  - pl_fert_wet
  - salt_fert_wet
  - cs_fert_wet
  - pl_fert
  - pl_manure
  - salt_fert
  - cs_fert
  - pest_apply
  - curno
  - pl_burnop
  - mgt_newtillmix_wet
reads: []
writes: []
purpose: ""
---

# mgt_sched

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `mgt_sched.f90`
- **Modules used**: [[plant_data_module.f90]], [[mgt_operations_module.f90]], [[tillage_data_module.f90]], [[basin_module.f90]], [[hydrograph_module.f90]], [[hru_module.f90]], [[soil_module.f90]], [[plant_module.f90]], [[time_module.f90]], [[constituent_mass_module.f90]], [[organic_mineral_mass_module.f90]], [[calibration_data_module.f90]], [[reservoir_data_module.f90]], [[reservoir_module.f90]], [[maximum_data_module.f90]], [[aquifer_module.f90]]
- **Subroutine calls**: 20 | **Files read**: 0 | **Files written**: 0

## Call Relationships
**This routine calls:**

- [[mgt_plantop.f90]]
- [[mgt_transplant.f90]]
- [[mgt_harvbiomass.f90]]
- [[mgt_harvgrain.f90]]
- [[mgt_harvresidue.f90]]
- [[mgt_harvtuber.f90]]
- [[mgt_killop.f90]]
- [[mgt_newtillmix_cswat1.f90]]
- [[mgt_newtillmix_cswat0.f90]]
- [[pl_fert_wet.f90]]
- [[salt_fert_wet.f90]]
- [[cs_fert_wet.f90]]
- [[pl_fert.f90]]
- [[pl_manure.f90]]
- [[salt_fert.f90]]
- [[cs_fert.f90]]
- [[pest_apply.f90]]
- [[curno.f90]]
- [[pl_burnop.f90]]
- [[mgt_newtillmix_wet.f90]]

**Called by** (live Dataview back-query):

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
