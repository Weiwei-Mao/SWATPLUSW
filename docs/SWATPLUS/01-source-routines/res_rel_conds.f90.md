---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: res_rel_conds.f90
note_file: res_rel_conds.f90
subroutine: res_rel_conds
module:
  - reservoir_conditions_module
  - time_module
  - hydrograph_module
calls:
  - cond_real_c
  - cond_integer_c
uses_variables:
  - hydrograph_module.f90#ht2
  - reservoir_conditions_module.f90#ctbl
  - reservoir_conditions_module.f90#day
  - reservoir_conditions_module.f90#hit
  - reservoir_conditions_module.f90#release
input_variables: []
reads: []
writes: []
purpose: ""
---

# res_rel_conds

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `res_rel_conds.f90`
- **Modules used**:
  - [[reservoir_conditions_module.f90]]
  - [[time_module.f90]]
  - [[hydrograph_module.f90]]
- **Subroutine calls**: 2 | **Files read**: 0 | **Files written**: 0

## Call Relationships
**This routine calls:**

- [[cond_real_c.f90]]
- [[cond_integer_c.f90]]

**Called by:**

- [[res_control.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[hydrograph_module.f90#ht2]] - `hyd_output`
- [[reservoir_conditions_module.f90#ctbl]] - `reservoir_condition_tables`
- [[reservoir_conditions_module.f90#day]] - `integer`
- [[reservoir_conditions_module.f90#hit]] - `character(1)`
- [[reservoir_conditions_module.f90#release]] - `real`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
