---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: res_control.f90
note_file: res_control.f90
subroutine: res_control
module:
  - basin_module
  - reservoir_data_module
  - time_module
  - reservoir_module
  - climate_module
  - hydrograph_module
  - conditional_module
  - water_body_module
  - constituent_mass_module
calls:
  - cli_lapse
  - move_alloc
  - conditions
  - res_hydro
  - res_sediment
  - res_rel_conds
  - gwflow_reservoir
  - res_nutrient
  - res_pest
  - res_salt
  - res_cs
uses_variables:
  - basin_module.f90#bsn_cc
  - basin_module.f90#pco
  - climate_module.f90#w
  - climate_module.f90#wst
  - conditional_module.f90#d_tbl
  - conditional_module.f90#dtbl_res
  - constituent_mass_module.f90#cs_db
  - constituent_mass_module.f90#hcs2
  - constituent_mass_module.f90#hin_csz
  - constituent_mass_module.f90#obcs
  - hydrograph_module.f90#hd
  - hydrograph_module.f90#ht1
  - hydrograph_module.f90#ht2
  - hydrograph_module.f90#icmd
  - hydrograph_module.f90#iwst
  - hydrograph_module.f90#ob
  - hydrograph_module.f90#res
  - hydrograph_module.f90#res_in_d
  - hydrograph_module.f90#res_out_d
  - hydrograph_module.f90#resz
  - hydrograph_module.f90#ts
  - hydrograph_module.f90#wbody
  - reservoir_data_module.f90#res_dat
  - reservoir_data_module.f90#res_hyd
  - reservoir_data_module.f90#res_prm
  - reservoir_data_module.f90#wbody_prm
  - reservoir_module.f90#res_ob
  - time_module.f90#time
  - water_body_module.f90#res_wat_d
  - water_body_module.f90#wbody_wb
input_variables: []
reads: []
writes: []
purpose: ""
---

# res_control

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `res_control.f90`
- **Modules used**:
  - [[basin_module.f90]]
  - [[reservoir_data_module.f90]]
  - [[time_module.f90]]
  - [[reservoir_module.f90]]
  - [[climate_module.f90]]
  - [[hydrograph_module.f90]]
  - [[conditional_module.f90]]
  - [[water_body_module.f90]]
  - [[constituent_mass_module.f90]]
- **Subroutine calls**: 11 | **Files read**: 0 | **Files written**: 0

## Call Relationships
**This routine calls:**

- [[cli_lapse.f90]]
- `move_alloc`
- [[conditions.f90]]
- [[res_hydro.f90]]
- [[res_sediment.f90]]
- [[res_rel_conds.f90]]
- [[gwflow_reservoir.f90]]
- [[res_nutrient.f90]]
- [[res_pest.f90]]
- [[res_salt.f90]]
- [[res_cs.f90]]

**Called by:**

- [[command.f90]]
- [[wallo_control.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[basin_module.f90#bsn_cc]] - `basin_control_codes`
- [[basin_module.f90#pco]] - `basin_print_codes`
- [[climate_module.f90#w]] - `weather_daily`
- [[climate_module.f90#wst]] - `weather_station`
- [[conditional_module.f90#d_tbl]] - `decision_table`
- [[conditional_module.f90#dtbl_res]] - `decision_table`
- [[constituent_mass_module.f90#cs_db]] - `constituents`
- [[constituent_mass_module.f90#hcs2]] - `constituent_mass`
- [[constituent_mass_module.f90#hin_csz]] - `constituent_mass`
- [[constituent_mass_module.f90#obcs]] - `all_constituent_hydrograph`
- [[hydrograph_module.f90#hd]] - `hyd_output`
- [[hydrograph_module.f90#ht1]] - `hyd_output`
- [[hydrograph_module.f90#ht2]] - `hyd_output`
- [[hydrograph_module.f90#icmd]] - `integer`
- [[hydrograph_module.f90#iwst]] - `integer`
- [[hydrograph_module.f90#ob]] - `object_connectivity`
- [[hydrograph_module.f90#res]] - `hyd_output`
- [[hydrograph_module.f90#res_in_d]] - `hyd_output`
- [[hydrograph_module.f90#res_out_d]] - `hyd_output`
- [[hydrograph_module.f90#resz]] - `hyd_output`
- [[hydrograph_module.f90#ts]] - `timestep`
- [[hydrograph_module.f90#wbody]] - `hyd_output`
- [[reservoir_data_module.f90#res_dat]] - `reservoir_data`
- [[reservoir_data_module.f90#res_hyd]] - `reservoir_hyd_data`
- [[reservoir_data_module.f90#res_prm]] - `water_body_data_parameters`
- [[reservoir_data_module.f90#wbody_prm]] - `water_body_data_parameters`
- [[reservoir_module.f90#res_ob]] - `reservoir`
- [[time_module.f90#time]] - `time_current`
- [[water_body_module.f90#res_wat_d]] - `water_body`
- [[water_body_module.f90#wbody_wb]] - `water_body`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
