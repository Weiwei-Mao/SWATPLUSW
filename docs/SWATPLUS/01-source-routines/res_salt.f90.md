---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: res_salt.f90
note_file: res_salt.f90
subroutine: res_salt
module:
  - reservoir_data_module
  - reservoir_module
  - water_body_module
  - hydrograph_module
  - constituent_mass_module
  - res_salt_module
calls: []
uses_variables:
  - constituent_mass_module.f90#cs_db
  - constituent_mass_module.f90#obcs
  - constituent_mass_module.f90#res_water
  - hydrograph_module.f90#hd
  - hydrograph_module.f90#ht2
  - hydrograph_module.f90#icmd
  - hydrograph_module.f90#ob
  - hydrograph_module.f90#res
  - res_salt_module.f90#ressalt_d
  - reservoir_module.f90#res_ob
  - water_body_module.f90#res_wat_d
input_variables: []
reads: []
writes: []
purpose: "this subroutine computes the reservoir salt ion balance"
---

# res_salt

> [!info] Summary
> this subroutine computes the reservoir salt ion balance

## Basic Information
- **Type**: `subroutine`
- **Source file**: `res_salt.f90`
- **Modules used**:
  - [[reservoir_data_module.f90]]
  - [[reservoir_module.f90]]
  - [[water_body_module.f90]]
  - [[hydrograph_module.f90]]
  - [[constituent_mass_module.f90]]
  - [[res_salt_module.f90]]
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
- [[constituent_mass_module.f90#obcs]] - `all_constituent_hydrograph`
- [[constituent_mass_module.f90#res_water]] - `constituent_mass`
- [[hydrograph_module.f90#hd]] - `hyd_output`
- [[hydrograph_module.f90#ht2]] - `hyd_output`
- [[hydrograph_module.f90#icmd]] - `integer`
- [[hydrograph_module.f90#ob]] - `object_connectivity`
- [[hydrograph_module.f90#res]] - `hyd_output`
- [[res_salt_module.f90#ressalt_d]] - `res_salt_output`
- [[reservoir_module.f90#res_ob]] - `reservoir`
- [[water_body_module.f90#res_wat_d]] - `water_body`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
