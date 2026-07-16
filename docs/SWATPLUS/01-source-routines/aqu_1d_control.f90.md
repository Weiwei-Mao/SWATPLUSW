---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: aqu_1d_control.f90
note_file: aqu_1d_control.f90
subroutine: aqu_1d_control
module:
  - aquifer_module
  - time_module
  - hydrograph_module
  - climate_module
  - maximum_data_module
  - constituent_mass_module
  - pesticide_data_module
  - aqu_pesticide_module
  - salt_module
  - salt_aquifer
  - cs_aquifer
  - ch_pesticide_module
calls:
  - salt_chem_aqu
  - cs_rctn_aqu
  - cs_sorb_aqu
uses_variables:
  - aqu_pesticide_module.f90#aqupst_d
  - aquifer_module.f90#aqu_d
  - aquifer_module.f90#aqu_dat
  - aquifer_module.f90#aqu_prm
  - climate_module.f90#wst
  - constituent_mass_module.f90#aq_chcs
  - constituent_mass_module.f90#cs_aqu
  - constituent_mass_module.f90#cs_db
  - constituent_mass_module.f90#hin_csz
  - constituent_mass_module.f90#obcs
  - cs_aquifer.f90#acsb_d
  - hydrograph_module.f90#aq_ch
  - hydrograph_module.f90#hd
  - hydrograph_module.f90#hz
  - hydrograph_module.f90#icmd
  - hydrograph_module.f90#iwst
  - hydrograph_module.f90#ob
  - hydrograph_module.f90#ts
  - maximum_data_module.f90#db_mx
  - pesticide_data_module.f90#pestcp
  - pesticide_data_module.f90#pestdb
  - salt_aquifer.f90#asaltb_d
  - time_module.f90#time
input_variables: []
reads: []
writes: []
purpose: ""
---

# aqu_1d_control

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `aqu_1d_control.f90`
- **Modules used**:
  - [[aquifer_module.f90]]
  - [[time_module.f90]]
  - [[hydrograph_module.f90]]
  - [[climate_module.f90]]
  - [[maximum_data_module.f90]]
  - [[constituent_mass_module.f90]]
  - [[pesticide_data_module.f90]]
  - [[aqu_pesticide_module.f90]]
  - [[salt_module.f90]]
  - [[salt_aquifer.f90]]
  - [[cs_aquifer.f90]]
  - [[ch_pesticide_module.f90]]
- **Subroutine calls**: 3 | **Files read**: 0 | **Files written**: 0

## Call Relationships
**This routine calls:**

- [[salt_chem_aqu.f90]]
- [[cs_rctn_aqu.f90]]
- [[cs_sorb_aqu.f90]]

**Called by:**

- [[command.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[aqu_pesticide_module.f90#aqupst_d]] - `aqu_pesticide_output`
- [[aquifer_module.f90#aqu_d]] - `aquifer_dynamic`
- [[aquifer_module.f90#aqu_dat]] - `aquifer_database`
- [[aquifer_module.f90#aqu_prm]] - `aquifer_data_parameters`
- [[climate_module.f90#wst]] - `weather_station`
- [[constituent_mass_module.f90#aq_chcs]] - `gw_load_hydrograph`
- [[constituent_mass_module.f90#cs_aqu]] - `constituent_mass`
- [[constituent_mass_module.f90#cs_db]] - `constituents`
- [[constituent_mass_module.f90#hin_csz]] - `constituent_mass`
- [[constituent_mass_module.f90#obcs]] - `all_constituent_hydrograph`
- [[cs_aquifer.f90#acsb_d]] - `object_cs_balance_aqu`
- [[hydrograph_module.f90#aq_ch]] - `channel_aquifer_elements`
- [[hydrograph_module.f90#hd]] - `hyd_output`
- [[hydrograph_module.f90#hz]] - `hyd_output`
- [[hydrograph_module.f90#icmd]] - `integer`
- [[hydrograph_module.f90#iwst]] - `integer`
- [[hydrograph_module.f90#ob]] - `object_connectivity`
- [[hydrograph_module.f90#ts]] - `timestep`
- [[maximum_data_module.f90#db_mx]] - `data_files_max_elements`
- [[pesticide_data_module.f90#pestcp]] - `pesticide_cp`
- [[pesticide_data_module.f90#pestdb]] - `pesticide_db`
- [[salt_aquifer.f90#asaltb_d]] - `object_salt_balance_aqu`
- [[time_module.f90#time]] - `time_current`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
