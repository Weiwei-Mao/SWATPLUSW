---
type: source
subtype: program
tags:
  - swat/source
  - swat/read
file: main.f90
note_file: main.f90
subroutine: main
module:
  - time_module
  - hydrograph_module
  - maximum_data_module
  - calibration_data_module
  - hru_module
calls:
  - proc_bsn
  - proc_date_time
  - proc_db
  - proc_read
  - hyd_connect
  - recalldb_read
  - exco_db_read
  - dr_db_read
  - cli_lapse
  - object_read_output
  - om_water_init
  - pest_cha_res_read
  - path_cha_res_read
  - salt_cha_read
  - cs_cha_read
  - lsu_read_elements
  - proc_hru
  - proc_cha
  - proc_aqu
  - dtbl_lum_read
  - hru_lte_read
  - proc_cond
  - res_read_weir
  - dtbl_res_read
  - dtbl_scen_read
  - cal_cond_read
  - manure_allocation_read
  - dtbl_flocon_read
  - om_treat_read
  - om_use_read
  - om_osrc_read
  - water_treatment_read
  - water_use_read
  - water_tower_read
  - water_pipe_read
  - water_canal_read
  - water_allocation_read
  - hru_dtbl_actions_init
  - proc_res
  - wet_read_hyd
  - wet_read
  - wet_read_salt_cs
  - wet_all_initial
  - wet_fp_init
  - proc_cal
  - soil_nutcarb_init
  - proc_open
  - unit_hyd_ru_hru
  - dr_ru
  - hyd_connect_out
  - command
  - time_control
  - calsoft_control
  - cal_parmchg_read
  - calhard_control
  - swift_output
  - date_and_time
uses_variables:
  - calibration_data_module.f90#cal_hard
  - calibration_data_module.f90#cal_soft
  - calibration_data_module.f90#cal_upd
  - hru_module.f90#hru
  - hru_module.f90#ihru
  - hru_module.f90#isol
  - hydrograph_module.f90#icmd
  - hydrograph_module.f90#ob
  - hydrograph_module.f90#sp_ob
  - hydrograph_module.f90#sp_ob1
  - maximum_data_module.f90#db_mx
  - time_module.f90#time
  - time_module.f90#time_init
input_variables: []
reads: []
writes:
  - simulation.out
  - erosion.txt
  - success.fin
purpose: "Orchestrates SWAT+ startup, input loading, object setup, calibration initialization, simulation dispatch, and completion output."
---

# main

> [!info] Summary
> Main program startup path: opens top-level outputs, calls the basin/date/database/read orchestration routines, builds connectivity and objects, initializes optional calibration paths, runs the simulation control path, and writes completion output.

## Basic Information
- **Type**: `program`
- **Source file**: `main.f90`
- **Modules used**:
  - [[time_module.f90]]
  - [[hydrograph_module.f90]]
  - [[maximum_data_module.f90]]
  - [[calibration_data_module.f90]]
  - [[hru_module.f90]]
- **Subroutine calls**: 57 | **Files read**: 0 | **Files written**: 3

## Call Relationships
**This routine calls:**

- [[proc_bsn.f90]]
- [[proc_date_time.f90]]
- [[proc_db.f90]]
- [[proc_read.f90]]
- [[hyd_connect.f90]]
- [[recall_read.f90]]
- [[exco_db_read.f90]]
- [[dr_db_read.f90]]
- [[cli_lapse.f90]]
- [[object_read_output.f90]]
- [[om_water_init.f90]]
- [[pest_cha_res_read.f90]]
- [[path_cha_res_read.f90]]
- [[salt_cha_read.f90]]
- [[cs_cha_read.f90]]
- [[lsu_read_elements.f90]]
- [[proc_hru.f90]]
- [[proc_cha.f90]]
- [[proc_aqu.f90]]
- [[dtbl_lum_read.f90]]
- [[hru_lte_read.f90]]
- [[proc_cond.f90]]
- [[res_read_weir.f90]]
- [[dtbl_res_read.f90]]
- [[dtbl_scen_read.f90]]
- [[cal_cond_read.f90]]
- [[manure_allocation_read.f90]]
- [[dtbl_flocon_read.f90]]
- [[om_treat_read.f90]]
- [[om_use_read.f90]]
- [[om_osrc_read.f90]]
- [[water_treatment_read.f90]]
- [[water_use_read.f90]]
- [[water_tower_read.f90]]
- [[water_pipe_read.f90]]
- [[water_canal_read.f90]]
- [[water_allocation_read.f90]]
- [[hru_dtbl_actions_init.f90]]
- [[proc_res.f90]]
- [[wet_read_hyd.f90]]
- [[wet_read.f90]]
- [[wet_read_salt_cs.f90]]
- [[wet_all_initial.f90]]
- [[wet_fp_init.f90]]
- [[proc_cal.f90]]
- [[soil_nutcarb_init.f90]]
- [[proc_open.f90]]
- [[unit_hyd_ru_hru.f90]]
- [[dr_ru.f90]]
- [[hyd_connect_out.f90]]
- [[command.f90]]
- [[time_control.f90]]
- [[calsoft_control.f90]]
- [[cal_parmchg_read.f90]]
- [[calhard_control.f90]]
- [[swift_output.f90]]
- `date_and_time`

**Called by:**

(No static callers detected.)

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[calibration_data_module.f90#cal_hard]] - `character (len=1)`
- [[calibration_data_module.f90#cal_soft]] - `character (len=1)`
- [[calibration_data_module.f90#cal_upd]] - `update_parameters`
- [[hru_module.f90#hru]] - `hydrologic_response_unit`
- [[hru_module.f90#ihru]] - `integer`
- [[hru_module.f90#isol]] - `integer`
- [[hydrograph_module.f90#icmd]] - `integer`
- [[hydrograph_module.f90#ob]] - `object_connectivity`
- [[hydrograph_module.f90#sp_ob]] - `spatial_objects`
- [[hydrograph_module.f90#sp_ob1]] - `spatial_objects`
- [[maximum_data_module.f90#db_mx]] - `data_files_max_elements`
- [[time_module.f90#time]] - `time_current`
- [[time_module.f90#time_init]] - `time_current`

## File I/O
- **Writes**:
  - [[simulation.out]]
  - [[erosion.txt]]
  - [[success.fin]]

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.

- Line 30: Opens file [[simulation.out]] (unit 9003)
- Line 38: Opens file [[erosion.txt]] (unit 888, recl 1500)
- Line 40: call [[proc_bsn.f90]]
- Line 41: call [[proc_date_time.f90]], input weather data
- Line 42: call [[proc_db.f90]], reads the shared parameter databases and structural/management libraries
- Line 43: call [[proc_read.f90]], reads the main environmental and object input data needed to build the model state
- Line 45: call [[hyd_connect.f90]], connection files
- Line 46: call [[recall_read.f90]], recall is a user-defined **time-series source or sink**.
- Line 47: call [[exco_db_read.f90]], export coefficient is a user-defined **loading source/coefficient**, not normally a sink.
- Line 48: call [[dr_db_read.f90]], delivery ratio. The `dr` object **receives an inflow hydrograph**, multiplies each component by user-defined delivery ratios, then sends the reduced/modified hydrograph downstream.
- Define icmd
- Line 59: call [[cli_lapse.f90]], Adjusts precip and temperature based on elevation for each [[hydrograph_module.f90#ob]]
- Line 60: call [[object_read_output.f90]], is for **specific output for specific objects**

- Line 62: call [[om_water_init.f90]], Initial organic-mineral state of stored water (channel/reservoir/wetland/aquifer)
- Line 63: call [[pest_cha_res_read.f90]], Reads pesticide initial water and benthic concentrations from [[pest_water.ini]]
- Line 64: call [[path_cha_res_read.f90]], Reads pathogen initial water and benthic concentrations from [[[path_water.ini]]
- Line 65: call [[salt_cha_read.f90]], Reads initial channel-water salt concentrations from [[salt_channel.ini]]
- Line 66: call [[cs_cha_read.f90]], Reads initial channel-water concentrations for generic constituents from [[cs_channel.ini]]. It also optionally sets up [[cs_streamobs]] output. These two files are out of [[file.cio]]

- Line 68: call [[lsu_read_elements.f90]], read landscape cataloging unit definitions for output
- Line 70: call [[proc_hru.f90]], read HRU databases, allocate HRU arrays, copy selected `hru_db` records into active `hru(:)`, initialize soil/plant/hydro/topo state
- Line 71: call [[proc_cha.f90]], read channel databases, allocate/init regular channels and SWAT-DEG channels, build rating curves, initialize channel routing state
- Line 72: call [[proc_aqu.f90]], read aquifer database, allocate active aquifer arrays, copy selected `aqudb` records into active aquifer state

- Line 75: call [[dtbl_lum_read.f90]], read decision table data for conditional management, [[lum.dtl]]
- Line 77: call [[hru_lte_read.f90]]
- Line 79: call [[proc_cond.f90]], crosswalks auto-management names from `management.sch` to `dtbl_lum(:)` indexes
- Line 81: call [[res_read_weir.f90]], read [[weir.res]], reads weir equation parameters into `res_weir(:)`
- Line 82: call [[dtbl_res_read.f90]], read [[res_rel.dtl]], reads reservoir/wetland release decision tables into `dtbl_res(:)`
- Line 83: call [[dtbl_scen_read.f90]], read [[scen_lu.dtl]], reads scenario decision tables, mainly `lu_change` and `snow_change`
- Line 85: call [[cal_cond_read.f90]], read [[scen_dtl.upd]], out of [[file.cio]], reads conditional update schedule and points it to `dtbl_scen(:)`
- Line 88: call [[manure_allocation_read.f90]], read [[manure_allo.mnu]], out of [[file.cio]], reads manure source/demand allocation objects into `mallo(:)`
- Line 90: call [[dtbl_flocon_read.f90]], read [[flo_con.dtl]], reads flow-control decision tables into `dtbl_flo(:)`

- Line 93: call [[om_treat_read.f90]], read file [[om_treat.wal]], out of [[file.cio]]
- Line 94: call [[om_use_read.f90]], read file [[om_use.wal]], out of [[file.cio]]
- Line 95: call [[om_osrc_read.f90]], read file [[om_osrc.wal]], out of [[file.cio]]
- Line 96: call [[water_treatment_read.f90]], read file [[water_treat.wal]], out of [[file.cio]]
- Line 97: call [[water_use_read.f90]], call file [[water_use.wal]], out of [[file.cio]]
- Line 99: read [[water_tower_read.f90]],
- Line 100: read [[water_pipe_read.f90]]
- Line 101: read [[water_canal_read.f90]]
- Line 102: read [[water_allocation_read.f90]]
- Line 104: read [[hru_dtbl_actions_init.f90]]

- Line 118: call [[proc_cal.f90]], set calibration and soft calibration

- Line 120-124, iteration based on hru
	- isol, soil pointer in input file [[soils.sol]]
	- Call [[soil_nutcarb_init.f90]]

- Line 126: call [[proc_open.f90]], write headers in output files
- Line 130: call [[unit_hyd_ru_hru.f90]]
- Line 132: call [[dr_ru.f90]], calculate delivery ratio for each routing unit
- Line 134: call [[hyd_connect_out.f90]]

- Line 140-151, time iteration
	- Line 150: call [[time_control.f90]]
-


<!-- USER-NOTES-END -->
