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
uses_variables:
  - aquifer_module.f90#aqu_d
  - aquifer_module.f90#aqu_prm
  - basin_module.f90#bsn_cc
  - basin_module.f90#pco
  - calibration_data_module.f90#cal_codes
  - calibration_data_module.f90#plcal
  - conditional_module.f90#d_tbl
  - constituent_mass_module.f90#ch_water
  - constituent_mass_module.f90#cs_aqu
  - constituent_mass_module.f90#cs_db
  - constituent_mass_module.f90#cs_irr
  - hru_lte_module.f90#hlt
  - hru_module.f90#cn2
  - hru_module.f90#fertnh3
  - hru_module.f90#fertno3
  - hru_module.f90#fertorgn
  - hru_module.f90#fertorgp
  - hru_module.f90#fertsolp
  - hru_module.f90#hru
  - hru_module.f90#ihru
  - hru_module.f90#ilu
  - hru_module.f90#ipl
  - hru_module.f90#isol
  - hru_module.f90#mgt_ops
  - hru_module.f90#mo
  - hru_module.f90#phubase
  - hru_module.f90#qtile
  - hru_module.f90#sdr
  - hru_module.f90#snodb
  - hru_module.f90#sol_sumno3
  - hru_module.f90#sol_sumsolp
  - hydrograph_module.f90#ch_stor
  - hydrograph_module.f90#ht2
  - hydrograph_module.f90#hz
  - hydrograph_module.f90#ich
  - hydrograph_module.f90#irrig
  - hydrograph_module.f90#ob
  - hydrograph_module.f90#res
  - hydrograph_module.f90#wet
  - landuse_data_module.f90#lum
  - manure_allocation_module.f90#mallo
  - manure_allocation_module.f90#manure_amtz
  - maximum_data_module.f90#db_mx
  - mgt_operations_module.f90#bmpuser_db
  - mgt_operations_module.f90#chemapp_db
  - mgt_operations_module.f90#filtstrip_db
  - mgt_operations_module.f90#graze
  - mgt_operations_module.f90#grazeop_db
  - mgt_operations_module.f90#grwaterway_db
  - mgt_operations_module.f90#harvop_db
  - mgt_operations_module.f90#irrop_db
  - mgt_operations_module.f90#mgt
  - mgt_operations_module.f90#pudl_db
  - mgt_operations_module.f90#sched
  - organic_mineral_mass_module.f90#pl_mass
  - organic_mineral_mass_module.f90#pl_yield
  - plant_data_module.f90#pcomdb
  - plant_data_module.f90#pldb
  - plant_data_module.f90#plts_bsn
  - plant_module.f90#basin_plants
  - plant_module.f90#bsn_crop_yld
  - plant_module.f90#bsn_crop_yld_aa
  - plant_module.f90#bsn_crop_yld_z
  - plant_module.f90#pcom
  - reservoir_data_module.f90#wet_dat
  - reservoir_module.f90#res_ob
  - reservoir_module.f90#wet_ob
  - sd_channel_module.f90#sd_ch
  - septic_data_module.f90#sep
  - soil_module.f90#soil
  - tillage_data_module.f90#tilldb
  - time_module.f90#time
  - water_allocation_module.f90#trn_m3
  - water_body_module.f90#wbodz
  - water_body_module.f90#wet_wat_d
input_variables: []
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
- **Modules used**:
  - [[conditional_module.f90]]
  - [[climate_module.f90]]
  - [[time_module.f90]]
  - [[aquifer_module.f90]]
  - [[hru_module.f90]]
  - [[soil_module.f90]]
  - [[plant_module.f90]]
  - [[plant_data_module.f90]]
  - [[mgt_operations_module.f90]]
  - [[landuse_data_module.f90]]
  - [[tillage_data_module.f90]]
  - [[reservoir_module.f90]]
  - [[sd_channel_module.f90]]
  - [[septic_data_module.f90]]
  - [[hru_lte_module.f90]]
  - [[basin_module.f90]]
  - [[organic_mineral_mass_module.f90]]
  - [[hydrograph_module.f90]]
  - [[output_landscape_module.f90]]
  - [[constituent_mass_module.f90]]
  - [[calibration_data_module.f90]]
  - [[fertilizer_data_module.f90]]
  - [[maximum_data_module.f90]]
  - [[tiles_data_module.f90]]
  - [[water_body_module.f90]]
  - [[reservoir_data_module.f90]]
  - [[manure_allocation_module.f90]]
  - [[water_allocation_module.f90]]
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

**Called by:**

- [[hru_control.f90]]
- [[hru_lte_control.f90]]
- [[mallo_control.f90]]
- [[time_control.f90]]
- [[wallo_demand.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[aquifer_module.f90#aqu_d]] - `aquifer_dynamic`
- [[aquifer_module.f90#aqu_prm]] - `aquifer_data_parameters`
- [[basin_module.f90#bsn_cc]] - `basin_control_codes`
- [[basin_module.f90#pco]] - `basin_print_codes`
- [[calibration_data_module.f90#cal_codes]] - `soft_calibration_codes`
- [[calibration_data_module.f90#plcal]] - `soft_data_calib_plant`
- [[conditional_module.f90#d_tbl]] - `decision_table`
- [[constituent_mass_module.f90#ch_water]] - `constituent_mass`
- [[constituent_mass_module.f90#cs_aqu]] - `constituent_mass`
- [[constituent_mass_module.f90#cs_db]] - `constituents`
- [[constituent_mass_module.f90#cs_irr]] - `constituent_mass`
- [[hru_lte_module.f90#hlt]] - `swatdeg_hru_dynamic`
- [[hru_module.f90#cn2]] - `real, dimension (:), allocatable`
- [[hru_module.f90#fertnh3]] - `real`
- [[hru_module.f90#fertno3]] - `real`
- [[hru_module.f90#fertorgn]] - `real`
- [[hru_module.f90#fertorgp]] - `real`
- [[hru_module.f90#fertsolp]] - `real`
- [[hru_module.f90#hru]] - `hydrologic_response_unit`
- [[hru_module.f90#ihru]] - `integer`
- [[hru_module.f90#ilu]] - `integer`
- [[hru_module.f90#ipl]] - `integer`
- [[hru_module.f90#isol]] - `integer`
- [[hru_module.f90#mgt_ops]] - `integer, dimension (:,:), allocatable`
- [[hru_module.f90#mo]] - `integer`
- [[hru_module.f90#phubase]] - `real, dimension (:), allocatable`
- [[hru_module.f90#qtile]] - `real`
- [[hru_module.f90#sdr]] - `subsurface_drainage_parameters`
- [[hru_module.f90#snodb]] - `snow_parameters`
- [[hru_module.f90#sol_sumno3]] - `real, dimension (:), allocatable`
- [[hru_module.f90#sol_sumsolp]] - `real, dimension (:), allocatable`
- [[hydrograph_module.f90#ch_stor]] - `hyd_output`
- [[hydrograph_module.f90#ht2]] - `hyd_output`
- [[hydrograph_module.f90#hz]] - `hyd_output`
- [[hydrograph_module.f90#ich]] - `integer`
- [[hydrograph_module.f90#irrig]] - `irrigation_water_transfer`
- [[hydrograph_module.f90#ob]] - `object_connectivity`
- [[hydrograph_module.f90#res]] - `hyd_output`
- [[hydrograph_module.f90#wet]] - `hyd_output`
- [[landuse_data_module.f90#lum]] - `land_use_management`
- [[manure_allocation_module.f90#mallo]] - `manure_allocation`
- [[manure_allocation_module.f90#manure_amtz]] - `manure_demand_amount`
- [[maximum_data_module.f90#db_mx]] - `data_files_max_elements`
- [[mgt_operations_module.f90#bmpuser_db]] - `bmpuser_operation`
- [[mgt_operations_module.f90#chemapp_db]] - `chemical_application_operation`
- [[mgt_operations_module.f90#filtstrip_db]] - `filtstrip_operation`
- [[mgt_operations_module.f90#graze]] - `grazing_operation`
- [[mgt_operations_module.f90#grazeop_db]] - `grazing_operation`
- [[mgt_operations_module.f90#grwaterway_db]] - `grwaterway_operation`
- [[mgt_operations_module.f90#harvop_db]] - `harvest_operation`
- [[mgt_operations_module.f90#irrop_db]] - `irrigation_operation`
- [[mgt_operations_module.f90#mgt]] - `management_ops`
- [[mgt_operations_module.f90#pudl_db]] - `puddle_operation`
- [[mgt_operations_module.f90#sched]] - `management_schedule`
- [[organic_mineral_mass_module.f90#pl_mass]] - `plant_community_mass`
- [[organic_mineral_mass_module.f90#pl_yield]] - `organic_mass`
- [[plant_data_module.f90#pcomdb]] - `plant_community_db`
- [[plant_data_module.f90#pldb]] - `plant_db`
- [[plant_data_module.f90#plts_bsn]] - `character(len=40), dimension (:), allocatable`
- [[plant_module.f90#basin_plants]] - `integer`
- [[plant_module.f90#bsn_crop_yld]] - `basin_crop_yields`
- [[plant_module.f90#bsn_crop_yld_aa]] - `basin_crop_yields`
- [[plant_module.f90#bsn_crop_yld_z]] - `basin_crop_yields`
- [[plant_module.f90#pcom]] - `plant_community`
- [[reservoir_data_module.f90#wet_dat]] - `reservoir_data`
- [[reservoir_module.f90#res_ob]] - `reservoir`
- [[reservoir_module.f90#wet_ob]] - `wetland`
- [[sd_channel_module.f90#sd_ch]] - `swatdeg_channel_dynamic`
- [[septic_data_module.f90#sep]] - `septic_system`
- [[soil_module.f90#soil]] - `soil_profile`
- [[tillage_data_module.f90#tilldb]] - `tillage_db`
- [[time_module.f90#time]] - `time_current`
- [[water_allocation_module.f90#trn_m3]] - `real`
- [[water_body_module.f90#wbodz]] - `water_body`
- [[water_body_module.f90#wet_wat_d]] - `water_body`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
