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
uses_variables:
  - basin_module.f90#bsn_cc
  - basin_module.f90#pco
  - calibration_data_module.f90#cal_codes
  - calibration_data_module.f90#plcal
  - constituent_mass_module.f90#cs_db
  - hru_module.f90#cn2
  - hru_module.f90#fertnh3
  - hru_module.f90#fertno3
  - hru_module.f90#fertorgn
  - hru_module.f90#fertorgp
  - hru_module.f90#fertsolp
  - hru_module.f90#grz_days
  - hru_module.f90#hru
  - hru_module.f90#igrz
  - hru_module.f90#ihru
  - hru_module.f90#ipl
  - hru_module.f90#mgt_ops
  - hru_module.f90#mo
  - hru_module.f90#ndeat
  - hru_module.f90#phubase
  - hru_module.f90#sol_sumno3
  - hru_module.f90#sol_sumsolp
  - hru_module.f90#sweepeff
  - hru_module.f90#yr_skip
  - hydrograph_module.f90#irrig
  - hydrograph_module.f90#sp_ob
  - hydrograph_module.f90#wet
  - maximum_data_module.f90#db_mx
  - mgt_operations_module.f90#chemapp_db
  - mgt_operations_module.f90#graze
  - mgt_operations_module.f90#grazeop_db
  - mgt_operations_module.f90#harvop_db
  - mgt_operations_module.f90#irrop_db
  - mgt_operations_module.f90#mgt
  - mgt_operations_module.f90#pudl_db
  - mgt_operations_module.f90#sched
  - mgt_operations_module.f90#sweepop
  - mgt_operations_module.f90#sweepop_db
  - organic_mineral_mass_module.f90#manure
  - organic_mineral_mass_module.f90#pl_mass
  - organic_mineral_mass_module.f90#pl_yield
  - plant_data_module.f90#pcomdb
  - plant_data_module.f90#pldb
  - plant_data_module.f90#transpl
  - plant_module.f90#bsn_crop_yld
  - plant_module.f90#pcom
  - plant_module.f90#plstrz
  - reservoir_data_module.f90#res_weir
  - reservoir_module.f90#wet_ob
  - soil_module.f90#soil
  - tillage_data_module.f90#tilldb
  - time_module.f90#time
input_variables: []
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
- **Modules used**:
  - [[plant_data_module.f90]]
  - [[mgt_operations_module.f90]]
  - [[tillage_data_module.f90]]
  - [[basin_module.f90]]
  - [[hydrograph_module.f90]]
  - [[hru_module.f90]]
  - [[soil_module.f90]]
  - [[plant_module.f90]]
  - [[time_module.f90]]
  - [[constituent_mass_module.f90]]
  - [[organic_mineral_mass_module.f90]]
  - [[calibration_data_module.f90]]
  - [[reservoir_data_module.f90]]
  - [[reservoir_module.f90]]
  - [[maximum_data_module.f90]]
  - [[aquifer_module.f90]]
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

**Called by:**

- [[mgt_operatn.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[basin_module.f90#bsn_cc]] - `basin_control_codes`
- [[basin_module.f90#pco]] - `basin_print_codes`
- [[calibration_data_module.f90#cal_codes]] - `soft_calibration_codes`
- [[calibration_data_module.f90#plcal]] - `soft_data_calib_plant`
- [[constituent_mass_module.f90#cs_db]] - `constituents`
- [[hru_module.f90#cn2]] - `real, dimension (:), allocatable`
- [[hru_module.f90#fertnh3]] - `real`
- [[hru_module.f90#fertno3]] - `real`
- [[hru_module.f90#fertorgn]] - `real`
- [[hru_module.f90#fertorgp]] - `real`
- [[hru_module.f90#fertsolp]] - `real`
- [[hru_module.f90#grz_days]] - `integer, dimension (:), allocatable`
- [[hru_module.f90#hru]] - `hydrologic_response_unit`
- [[hru_module.f90#igrz]] - `integer, dimension (:), allocatable`
- [[hru_module.f90#ihru]] - `integer`
- [[hru_module.f90#ipl]] - `integer`
- [[hru_module.f90#mgt_ops]] - `integer, dimension (:,:), allocatable`
- [[hru_module.f90#mo]] - `integer`
- [[hru_module.f90#ndeat]] - `integer, dimension (:), allocatable`
- [[hru_module.f90#phubase]] - `real, dimension (:), allocatable`
- [[hru_module.f90#sol_sumno3]] - `real, dimension (:), allocatable`
- [[hru_module.f90#sol_sumsolp]] - `real, dimension (:), allocatable`
- [[hru_module.f90#sweepeff]] - `real`
- [[hru_module.f90#yr_skip]] - `integer, dimension (:), allocatable`
- [[hydrograph_module.f90#irrig]] - `irrigation_water_transfer`
- [[hydrograph_module.f90#sp_ob]] - `spatial_objects`
- [[hydrograph_module.f90#wet]] - `hyd_output`
- [[maximum_data_module.f90#db_mx]] - `data_files_max_elements`
- [[mgt_operations_module.f90#chemapp_db]] - `chemical_application_operation`
- [[mgt_operations_module.f90#graze]] - `grazing_operation`
- [[mgt_operations_module.f90#grazeop_db]] - `grazing_operation`
- [[mgt_operations_module.f90#harvop_db]] - `harvest_operation`
- [[mgt_operations_module.f90#irrop_db]] - `irrigation_operation`
- [[mgt_operations_module.f90#mgt]] - `management_ops`
- [[mgt_operations_module.f90#pudl_db]] - `puddle_operation`
- [[mgt_operations_module.f90#sched]] - `management_schedule`
- [[mgt_operations_module.f90#sweepop]] - `streetsweep_operation`
- [[mgt_operations_module.f90#sweepop_db]] - `streetsweep_operation`
- [[organic_mineral_mass_module.f90#manure]] - `organic_mass`
- [[organic_mineral_mass_module.f90#pl_mass]] - `plant_community_mass`
- [[organic_mineral_mass_module.f90#pl_yield]] - `organic_mass`
- [[plant_data_module.f90#pcomdb]] - `plant_community_db`
- [[plant_data_module.f90#pldb]] - `plant_db`
- [[plant_data_module.f90#transpl]] - `plant_transplant_db`
- [[plant_module.f90#bsn_crop_yld]] - `basin_crop_yields`
- [[plant_module.f90#pcom]] - `plant_community`
- [[plant_module.f90#plstrz]] - `plant_stress`
- [[reservoir_data_module.f90#res_weir]] - `reservoir_weir_outflow`
- [[reservoir_module.f90#wet_ob]] - `wetland`
- [[soil_module.f90#soil]] - `soil_profile`
- [[tillage_data_module.f90#tilldb]] - `tillage_db`
- [[time_module.f90#time]] - `time_current`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
