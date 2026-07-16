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
- **Modules used**: [[basin_module.f90]], [[reservoir_data_module.f90]], [[time_module.f90]], [[reservoir_module.f90]], [[climate_module.f90]], [[hydrograph_module.f90]], [[conditional_module.f90]], [[water_body_module.f90]], [[constituent_mass_module.f90]]
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

**Called by** (live Dataview back-query):

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
