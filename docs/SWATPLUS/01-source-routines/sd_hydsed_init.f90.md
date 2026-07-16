---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: sd_hydsed_init.f90
note_file: sd_hydsed_init.f90
subroutine: sd_hydsed_init
module:
  - input_file_module
  - sd_channel_module
  - channel_velocity_module
  - maximum_data_module
  - hydrograph_module
  - constituent_mass_module
  - pesticide_data_module
  - basin_module
calls:
  - sd_rating_curve
  - rcurv_interp_dep
  - hyd_convert_conc_to_mass
uses_variables:
  - basin_module.f90#bsn_cc
  - basin_module.f90#bsn_prm
  - channel_velocity_module.f90#sd_ch_vel
  - constituent_mass_module.f90#ch_benthic
  - constituent_mass_module.f90#ch_water
  - constituent_mass_module.f90#cs_cha_ini
  - constituent_mass_module.f90#cs_db
  - constituent_mass_module.f90#path_water_ini
  - constituent_mass_module.f90#pest_water_ini
  - constituent_mass_module.f90#salt_cha_ini
  - hydrograph_module.f90#ch_om_water_init
  - hydrograph_module.f90#ch_stor
  - hydrograph_module.f90#fp_om_water_init
  - hydrograph_module.f90#fp_stor
  - hydrograph_module.f90#hz
  - hydrograph_module.f90#ich
  - hydrograph_module.f90#icmd
  - hydrograph_module.f90#ob
  - hydrograph_module.f90#om_init_water
  - hydrograph_module.f90#sp_ob
  - hydrograph_module.f90#sp_ob1
  - hydrograph_module.f90#tot_stor
  - pesticide_data_module.f90#pestdb
  - sd_channel_module.f90#ch_rcurv
  - sd_channel_module.f90#gully
  - sd_channel_module.f90#rcurv
  - sd_channel_module.f90#sd_ch
  - sd_channel_module.f90#sd_chd
  - sd_channel_module.f90#sd_chd1
  - sd_channel_module.f90#sd_dat
  - sd_channel_module.f90#sd_init
input_variables: []
reads: []
writes: []
purpose: ""
---

# sd_hydsed_init

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `sd_hydsed_init.f90`
- **Modules used**:
  - [[input_file_module.f90]]
  - [[sd_channel_module.f90]]
  - [[channel_velocity_module.f90]]
  - [[maximum_data_module.f90]]
  - [[hydrograph_module.f90]]
  - [[constituent_mass_module.f90]]
  - [[pesticide_data_module.f90]]
  - [[basin_module.f90]]
- **Subroutine calls**: 3 | **Files read**: 0 | **Files written**: 0

## Call Relationships
**This routine calls:**

- [[sd_rating_curve.f90]]
- [[rcurv_interp_dep.f90]]
- [[hydrograph_module.f90#hyd_convert_conc_to_mass]]

**Called by:**

- [[proc_cha.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[basin_module.f90#bsn_cc]] - `basin_control_codes`
- [[basin_module.f90#bsn_prm]] - `basin_parms`
- [[channel_velocity_module.f90#sd_ch_vel]] - `channel_velocity_parameters`
- [[constituent_mass_module.f90#ch_benthic]] - `constituent_mass`
- [[constituent_mass_module.f90#ch_water]] - `constituent_mass`
- [[constituent_mass_module.f90#cs_cha_ini]] - `cs_cha_init_concentrations`
- [[constituent_mass_module.f90#cs_db]] - `constituents`
- [[constituent_mass_module.f90#path_water_ini]] - `cs_water_init_concentrations`
- [[constituent_mass_module.f90#pest_water_ini]] - `cs_water_init_concentrations`
- [[constituent_mass_module.f90#salt_cha_ini]] - `salt_cha_init_concentrations`
- [[hydrograph_module.f90#ch_om_water_init]] - `hyd_output`
- [[hydrograph_module.f90#ch_stor]] - `hyd_output`
- [[hydrograph_module.f90#fp_om_water_init]] - `hyd_output`
- [[hydrograph_module.f90#fp_stor]] - `hyd_output`
- [[hydrograph_module.f90#hz]] - `hyd_output`
- [[hydrograph_module.f90#ich]] - `integer`
- [[hydrograph_module.f90#icmd]] - `integer`
- [[hydrograph_module.f90#ob]] - `object_connectivity`
- [[hydrograph_module.f90#om_init_water]] - `hyd_output`
- [[hydrograph_module.f90#sp_ob]] - `spatial_objects`
- [[hydrograph_module.f90#sp_ob1]] - `spatial_objects`
- [[hydrograph_module.f90#tot_stor]] - `hyd_output`
- [[pesticide_data_module.f90#pestdb]] - `pesticide_db`
- [[sd_channel_module.f90#ch_rcurv]] - `channel_rating_curve`
- [[sd_channel_module.f90#gully]] - `gully_data`
- [[sd_channel_module.f90#rcurv]] - `channel_rating_curve_parameters`
- [[sd_channel_module.f90#sd_ch]] - `swatdeg_channel_dynamic`
- [[sd_channel_module.f90#sd_chd]] - `swatdeg_hydsed_data`
- [[sd_channel_module.f90#sd_chd1]] - `swatdeg_sednut_data`
- [[sd_channel_module.f90#sd_dat]] - `swatdeg_datafiles`
- [[sd_channel_module.f90#sd_init]] - `swatdeg_init_datafiles`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
