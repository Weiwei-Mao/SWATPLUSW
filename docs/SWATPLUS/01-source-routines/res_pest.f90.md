---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: res_pest.f90
note_file: res_pest.f90
subroutine: res_pest
module:
  - reservoir_data_module
  - reservoir_module
  - res_pesticide_module
  - hydrograph_module
  - constituent_mass_module
  - pesticide_data_module
  - water_body_module
calls: []
uses_variables:
  - constituent_mass_module.f90#cs_db
  - constituent_mass_module.f90#hcs2
  - constituent_mass_module.f90#obcs
  - constituent_mass_module.f90#res_benthic
  - constituent_mass_module.f90#res_water
  - hydrograph_module.f90#ht2
  - hydrograph_module.f90#icmd
  - hydrograph_module.f90#ob
  - hydrograph_module.f90#res
  - pesticide_data_module.f90#pestcp
  - pesticide_data_module.f90#pestdb
  - res_pesticide_module.f90#respst_d
  - reservoir_data_module.f90#res_dat
  - reservoir_data_module.f90#res_sed
  - reservoir_module.f90#bury
  - reservoir_module.f90#difus
  - reservoir_module.f90#res_ob
  - reservoir_module.f90#resuspst
  - reservoir_module.f90#setlpst
  - reservoir_module.f90#volatpst
  - water_body_module.f90#res_wat_d
input_variables: []
reads: []
writes: []
purpose: "this subroutine computes the lake hydrologic pesticide balance."
---

# res_pest

> [!info] Summary
> this subroutine computes the lake hydrologic pesticide balance.

## Basic Information
- **Type**: `subroutine`
- **Source file**: `res_pest.f90`
- **Modules used**:
  - [[reservoir_data_module.f90]]
  - [[reservoir_module.f90]]
  - [[res_pesticide_module.f90]]
  - [[hydrograph_module.f90]]
  - [[constituent_mass_module.f90]]
  - [[pesticide_data_module.f90]]
  - [[water_body_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 0 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by:**

- [[res_control.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[constituent_mass_module.f90#cs_db]] - `constituents`
- [[constituent_mass_module.f90#hcs2]] - `constituent_mass`
- [[constituent_mass_module.f90#obcs]] - `all_constituent_hydrograph`
- [[constituent_mass_module.f90#res_benthic]] - `constituent_mass`
- [[constituent_mass_module.f90#res_water]] - `constituent_mass`
- [[hydrograph_module.f90#ht2]] - `hyd_output`
- [[hydrograph_module.f90#icmd]] - `integer`
- [[hydrograph_module.f90#ob]] - `object_connectivity`
- [[hydrograph_module.f90#res]] - `hyd_output`
- [[pesticide_data_module.f90#pestcp]] - `pesticide_cp`
- [[pesticide_data_module.f90#pestdb]] - `pesticide_db`
- [[res_pesticide_module.f90#respst_d]] - `res_pesticide_output`
- [[reservoir_data_module.f90#res_dat]] - `reservoir_data`
- [[reservoir_data_module.f90#res_sed]] - `reservoir_sed_data`
- [[reservoir_module.f90#bury]] - `real`
- [[reservoir_module.f90#difus]] - `real`
- [[reservoir_module.f90#res_ob]] - `reservoir`
- [[reservoir_module.f90#resuspst]] - `real`
- [[reservoir_module.f90#setlpst]] - `real`
- [[reservoir_module.f90#volatpst]] - `real`
- [[water_body_module.f90#res_wat_d]] - `water_body`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
