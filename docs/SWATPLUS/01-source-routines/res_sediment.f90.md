---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: res_sediment.f90
note_file: res_sediment.f90
subroutine: res_sediment
module:
  - reservoir_data_module
  - reservoir_module
  - conditional_module
  - climate_module
  - time_module
  - hydrograph_module
  - water_body_module
calls: []
uses_variables:
  - hydrograph_module.f90#ht2
  - hydrograph_module.f90#hz
  - hydrograph_module.f90#wbody
  - reservoir_data_module.f90#wbody_prm
input_variables: []
reads: []
writes: []
purpose: ""
---

# res_sediment

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `res_sediment.f90`
- **Modules used**:
  - [[reservoir_data_module.f90]]
  - [[reservoir_module.f90]]
  - [[conditional_module.f90]]
  - [[climate_module.f90]]
  - [[time_module.f90]]
  - [[hydrograph_module.f90]]
  - [[water_body_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 0 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by:**

- [[res_control.f90]]
- [[wetland_control.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[hydrograph_module.f90#ht2]] - `hyd_output`
- [[hydrograph_module.f90#hz]] - `hyd_output`
- [[hydrograph_module.f90#wbody]] - `hyd_output`
- [[reservoir_data_module.f90#wbody_prm]] - `water_body_data_parameters`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
