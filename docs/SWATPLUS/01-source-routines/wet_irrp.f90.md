---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: wet_irrp.f90
note_file: wet_irrp.f90
subroutine: wet_irrp
module:
  - reservoir_data_module
  - reservoir_module
  - hydrograph_module
  - constituent_mass_module
  - aquifer_module
  - mgt_operations_module
  - hru_module
  - climate_module
calls: []
uses_variables:
  - aquifer_module.f90#aqu_d
  - climate_module.f90#w
  - constituent_mass_module.f90#ch_water
  - constituent_mass_module.f90#cs_aqu
  - constituent_mass_module.f90#cs_irr
  - constituent_mass_module.f90#res_water
  - hru_module.f90#hru
  - hru_module.f90#ihru
  - hydrograph_module.f90#ch_stor
  - hydrograph_module.f90#irrig
  - hydrograph_module.f90#ob
  - hydrograph_module.f90#res
  - hydrograph_module.f90#sp_ob
  - reservoir_module.f90#wet_ob
input_variables: []
reads: []
writes: []
purpose: ""
---

# wet_irrp

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `wet_irrp.f90`
- **Modules used**:
  - [[reservoir_data_module.f90]]
  - [[reservoir_module.f90]]
  - [[hydrograph_module.f90]]
  - [[constituent_mass_module.f90]]
  - [[aquifer_module.f90]]
  - [[mgt_operations_module.f90]]
  - [[hru_module.f90]]
  - [[climate_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 0 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by:**

- [[hru_control.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[aquifer_module.f90#aqu_d]] - `aquifer_dynamic`
- [[climate_module.f90#w]] - `weather_daily`
- [[constituent_mass_module.f90#ch_water]] - `constituent_mass`
- [[constituent_mass_module.f90#cs_aqu]] - `constituent_mass`
- [[constituent_mass_module.f90#cs_irr]] - `constituent_mass`
- [[constituent_mass_module.f90#res_water]] - `constituent_mass`
- [[hru_module.f90#hru]] - `hydrologic_response_unit`
- [[hru_module.f90#ihru]] - `integer`
- [[hydrograph_module.f90#ch_stor]] - `hyd_output`
- [[hydrograph_module.f90#irrig]] - `irrigation_water_transfer`
- [[hydrograph_module.f90#ob]] - `object_connectivity`
- [[hydrograph_module.f90#res]] - `hyd_output`
- [[hydrograph_module.f90#sp_ob]] - `spatial_objects`
- [[reservoir_module.f90#wet_ob]] - `wetland`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
