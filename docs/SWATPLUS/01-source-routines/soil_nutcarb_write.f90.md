---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: soil_nutcarb_write.f90
note_file: soil_nutcarb_write.f90
subroutine: soil_nutcarb_write
module:
  - soil_module
  - organic_mineral_mass_module
  - hydrograph_module
  - calibration_data_module
  - carbon_module
  - basin_module
  - plant_module
calls:
  - cb_soil_snap_emit
  - cb_cbn_lyr_emit
  - cb_n_p_pool_emit
  - cb_plc_stat_emit
  - cb_soil_snap_period
  - cb_cflux_stat_emit
  - cb_cpool_stat_emit
  - cb_write_depth_row
  - cb_write_var_block
  - cb_emit_row_id_csv
  - cb_emit_row_id_txt
  - cb_cflux_emit_blocks
uses_variables:
  - basin_module.f90#bsn_cc
  - basin_module.f90#pco
  - calibration_data_module.f90#lsu_elem
  - carbon_module.f90#cb_n_layers
  - hydrograph_module.f90#ob
  - hydrograph_module.f90#sp_ob
  - hydrograph_module.f90#sp_ob1
  - organic_mineral_mass_module.f90#bsn_mn
  - organic_mineral_mass_module.f90#bsn_mp
  - organic_mineral_mass_module.f90#bsn_org_pl
  - organic_mineral_mass_module.f90#bsn_org_rsd
  - organic_mineral_mass_module.f90#bsn_org_soil
  - organic_mineral_mass_module.f90#orgz
  - organic_mineral_mass_module.f90#pl_mass
  - organic_mineral_mass_module.f90#soil1
  - organic_mineral_mass_module.f90#soil_org_z
  - organic_mineral_mass_module.f90#soil_prof_hact
  - organic_mineral_mass_module.f90#soil_prof_hp
  - organic_mineral_mass_module.f90#soil_prof_hs
  - organic_mineral_mass_module.f90#soil_prof_hsta
  - organic_mineral_mass_module.f90#soil_prof_lig
  - organic_mineral_mass_module.f90#soil_prof_man
  - organic_mineral_mass_module.f90#soil_prof_meta
  - organic_mineral_mass_module.f90#soil_prof_microb
  - organic_mineral_mass_module.f90#soil_prof_nonlig
  - organic_mineral_mass_module.f90#soil_prof_root
  - organic_mineral_mass_module.f90#soil_prof_root_frac
  - organic_mineral_mass_module.f90#soil_prof_rsd
  - organic_mineral_mass_module.f90#soil_prof_seq_hp
  - organic_mineral_mass_module.f90#soil_prof_seq_hs
  - organic_mineral_mass_module.f90#soil_prof_seq_microb
  - organic_mineral_mass_module.f90#soil_prof_str
  - organic_mineral_mass_module.f90#soil_prof_water
  - plant_module.f90#pcom
  - soil_module.f90#soil
input_variables: []
reads: []
writes: []
purpose: "this subroutine writes soil carbon output."
---

# soil_nutcarb_write

> [!info] Summary
> this subroutine writes soil carbon output.

## Basic Information
- **Type**: `subroutine`
- **Source file**: `soil_nutcarb_write.f90`
- **Modules used**:
  - [[soil_module.f90]]
  - [[organic_mineral_mass_module.f90]]
  - [[hydrograph_module.f90]]
  - [[calibration_data_module.f90]]
  - [[carbon_module.f90]]
  - [[basin_module.f90]]
  - [[plant_module.f90]]
- **Subroutine calls**: 12 | **Files read**: 0 | **Files written**: 0

## Call Relationships
**This routine calls:**

- `cb_soil_snap_emit`
- `cb_cbn_lyr_emit`
- `cb_n_p_pool_emit`
- `cb_plc_stat_emit`
- `cb_soil_snap_period`
- `cb_cflux_stat_emit`
- `cb_cpool_stat_emit`
- [[carbon_module.f90#cb_write_depth_row]]
- [[carbon_module.f90#cb_write_var_block]]
- `cb_emit_row_id_csv`
- `cb_emit_row_id_txt`
- `cb_cflux_emit_blocks`

**Called by:**

- [[command.f90]]
- [[hru_output.f90]]
- [[output_landscape_init.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[basin_module.f90#bsn_cc]] - `basin_control_codes`
- [[basin_module.f90#pco]] - `basin_print_codes`
- [[calibration_data_module.f90#lsu_elem]] - `landscape_elements`
- [[carbon_module.f90#cb_n_layers]] - `integer`
- [[hydrograph_module.f90#ob]] - `object_connectivity`
- [[hydrograph_module.f90#sp_ob]] - `spatial_objects`
- [[hydrograph_module.f90#sp_ob1]] - `spatial_objects`
- [[organic_mineral_mass_module.f90#bsn_mn]] - `real`
- [[organic_mineral_mass_module.f90#bsn_mp]] - `real`
- [[organic_mineral_mass_module.f90#bsn_org_pl]] - `organic_mass`
- [[organic_mineral_mass_module.f90#bsn_org_rsd]] - `organic_mass`
- [[organic_mineral_mass_module.f90#bsn_org_soil]] - `organic_mass`
- [[organic_mineral_mass_module.f90#orgz]] - `organic_mass`
- [[organic_mineral_mass_module.f90#pl_mass]] - `plant_community_mass`
- [[organic_mineral_mass_module.f90#soil1]] - `soil_profile_mass`
- [[organic_mineral_mass_module.f90#soil_org_z]] - `organic_mass`
- [[organic_mineral_mass_module.f90#soil_prof_hact]] - `organic_mass`
- [[organic_mineral_mass_module.f90#soil_prof_hp]] - `organic_mass`
- [[organic_mineral_mass_module.f90#soil_prof_hs]] - `organic_mass`
- [[organic_mineral_mass_module.f90#soil_prof_hsta]] - `organic_mass`
- [[organic_mineral_mass_module.f90#soil_prof_lig]] - `organic_mass`
- [[organic_mineral_mass_module.f90#soil_prof_man]] - `organic_mass`
- [[organic_mineral_mass_module.f90#soil_prof_meta]] - `organic_mass`
- [[organic_mineral_mass_module.f90#soil_prof_microb]] - `organic_mass`
- [[organic_mineral_mass_module.f90#soil_prof_nonlig]] - `organic_mass`
- [[organic_mineral_mass_module.f90#soil_prof_root]] - `organic_mass`
- [[organic_mineral_mass_module.f90#soil_prof_root_frac]] - `real`
- [[organic_mineral_mass_module.f90#soil_prof_rsd]] - `organic_mass`
- [[organic_mineral_mass_module.f90#soil_prof_seq_hp]] - `organic_mass`
- [[organic_mineral_mass_module.f90#soil_prof_seq_hs]] - `organic_mass`
- [[organic_mineral_mass_module.f90#soil_prof_seq_microb]] - `organic_mass`
- [[organic_mineral_mass_module.f90#soil_prof_str]] - `organic_mass`
- [[organic_mineral_mass_module.f90#soil_prof_water]] - `organic_mass`
- [[plant_module.f90#pcom]] - `plant_community`
- [[soil_module.f90#soil]] - `soil_profile`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
