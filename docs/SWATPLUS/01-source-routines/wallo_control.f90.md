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
uses_variables:
  - basin_module.f90#pco
  - constituent_mass_module.f90#cs_db
  - hru_module.f90#hru
  - hru_module.f90#mo
  - hru_module.f90#phubase
  - hru_module.f90#sol_sumno3
  - hru_module.f90#sol_sumsolp
  - hydrograph_module.f90#aqu
  - hydrograph_module.f90#canal_om_stor
  - hydrograph_module.f90#hd
  - hydrograph_module.f90#hz
  - hydrograph_module.f90#irrig
  - hydrograph_module.f90#ob
  - hydrograph_module.f90#orcv_om
  - hydrograph_module.f90#res
  - hydrograph_module.f90#wal_omd
  - hydrograph_module.f90#wdraw_om
  - hydrograph_module.f90#wdraw_om_tot
  - hydrograph_module.f90#wtow_om_stor
  - hydrograph_module.f90#wtp_om_stor
  - hydrograph_module.f90#wuse_om_stor
  - organic_mineral_mass_module.f90#pl_mass
  - plant_module.f90#pcom
  - reservoir_module.f90#res_ob
  - sd_channel_module.f90#sd_ch
  - soil_module.f90#soil
  - time_module.f90#time
  - water_allocation_module.f90#trn_m3
  - water_allocation_module.f90#wallo
  - water_allocation_module.f90#wallod_out
  - water_allocation_module.f90#walloz
input_variables: []
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
- **Modules used**:
  - [[water_allocation_module.f90]]
  - [[hydrograph_module.f90]]
  - [[hru_module.f90]]
  - [[basin_module.f90]]
  - [[time_module.f90]]
  - [[plant_module.f90]]
  - [[soil_module.f90]]
  - [[reservoir_module.f90]]
  - [[sd_channel_module.f90]]
  - [[organic_mineral_mass_module.f90]]
  - [[constituent_mass_module.f90]]
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

**Called by:**

- [[command.f90]]
- [[sd_channel_control3.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[basin_module.f90#pco]] - `basin_print_codes`
- [[constituent_mass_module.f90#cs_db]] - `constituents`
- [[hru_module.f90#hru]] - `hydrologic_response_unit`
- [[hru_module.f90#mo]] - `integer`
- [[hru_module.f90#phubase]] - `real, dimension (:), allocatable`
- [[hru_module.f90#sol_sumno3]] - `real, dimension (:), allocatable`
- [[hru_module.f90#sol_sumsolp]] - `real, dimension (:), allocatable`
- [[hydrograph_module.f90#aqu]] - `hyd_output`
- [[hydrograph_module.f90#canal_om_stor]] - `hyd_output`
- [[hydrograph_module.f90#hd]] - `hyd_output`
- [[hydrograph_module.f90#hz]] - `hyd_output`
- [[hydrograph_module.f90#irrig]] - `irrigation_water_transfer`
- [[hydrograph_module.f90#ob]] - `object_connectivity`
- [[hydrograph_module.f90#orcv_om]] - `hyd_output`
- [[hydrograph_module.f90#res]] - `hyd_output`
- [[hydrograph_module.f90#wal_omd]] - `water_allocation_object`
- [[hydrograph_module.f90#wdraw_om]] - `hyd_output`
- [[hydrograph_module.f90#wdraw_om_tot]] - `hyd_output`
- [[hydrograph_module.f90#wtow_om_stor]] - `hyd_output`
- [[hydrograph_module.f90#wtp_om_stor]] - `hyd_output`
- [[hydrograph_module.f90#wuse_om_stor]] - `hyd_output`
- [[organic_mineral_mass_module.f90#pl_mass]] - `plant_community_mass`
- [[plant_module.f90#pcom]] - `plant_community`
- [[reservoir_module.f90#res_ob]] - `reservoir`
- [[sd_channel_module.f90#sd_ch]] - `swatdeg_channel_dynamic`
- [[soil_module.f90#soil]] - `soil_profile`
- [[time_module.f90#time]] - `time_current`
- [[water_allocation_module.f90#trn_m3]] - `real`
- [[water_allocation_module.f90#wallo]] - `water_allocation`
- [[water_allocation_module.f90#wallod_out]] - `water_allocation_output`
- [[water_allocation_module.f90#walloz]] - `source_output`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
