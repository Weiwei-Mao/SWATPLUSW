---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: time_control.f90
note_file: time_control.f90
subroutine: time_control
module:
  - maximum_data_module
  - calibration_data_module
  - plant_data_module
  - mgt_operations_module
  - hru_module
  - plant_module
  - soil_module
  - time_module
  - climate_module
  - basin_module
  - sd_channel_module
  - hru_lte_module
  - hydrograph_module
  - output_landscape_module
  - conditional_module
  - constituent_mass_module
  - output_ls_pesticide_module
  - water_body_module
  - water_allocation_module
calls:
  - xmon
  - cli_precip_control
  - basin_sw_init
  - aqu_pest_output_init
  - date_and_time
  - sim_initday
  - climate_control
  - cli_atmodep_time_control
  - conditions
  - actions
  - mallo_control
  - command
  - calsoft_sum_output
  - mgt_newtillmix_cswat0
  - calsoft_ave_output
reads: []
writes: []
purpose: "this subroutine contains the loops governing the modeling of processes; in the watershed"
---

# time_control

> [!info] Summary
> this subroutine contains the loops governing the modeling of processes; in the watershed

## Basic Information
- **Type**: `subroutine`
- **Source file**: `time_control.f90`
- **Modules used**: [[maximum_data_module.f90]], [[calibration_data_module.f90]], [[plant_data_module.f90]], [[mgt_operations_module.f90]], [[hru_module.f90]], [[plant_module.f90]], [[soil_module.f90]], [[time_module.f90]], [[climate_module.f90]], [[basin_module.f90]], [[sd_channel_module.f90]], [[hru_lte_module.f90]], [[hydrograph_module.f90]], [[output_landscape_module.f90]], [[conditional_module.f90]], [[constituent_mass_module.f90]], [[output_ls_pesticide_module.f90]], [[water_body_module.f90]], [[water_allocation_module.f90]]
- **Subroutine calls**: 15 | **Files read**: 0 | **Files written**: 0

## Call Relationships
**This routine calls:**

- [[xmon.f90]]
- [[cli_precip_control.f90]]
- [[basin_sw_init.f90]]
- [[aqu_pest_output_init.f90]]
- `date_and_time`
- [[sim_initday.f90]]
- [[climate_control.f90]]
- [[cli_atmodep_time_control.f90]]
- [[conditions.f90]]
- [[actions.f90]]
- [[mallo_control.f90]]
- [[command.f90]]
- [[calsoft_sum_output.f90]]
- [[mgt_newtillmix_cswat0.f90]]
- [[calsoft_ave_output.f90]]

**Called by** (live Dataview back-query):

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
