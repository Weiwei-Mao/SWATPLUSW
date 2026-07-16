---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: pl_fert_wet.f90
note_file: pl_fert_wet.f90
subroutine: pl_fert_wet
module:
  - mgt_operations_module
  - fertilizer_data_module
  - basin_module
  - organic_mineral_mass_module
  - hru_module
  - hydrograph_module
calls: []
uses_variables:
  - basin_module.f90#bsn_cc
  - fertilizer_data_module.f90#fertdb
  - hru_module.f90#fertn
  - hru_module.f90#fertnh3
  - hru_module.f90#fertno3
  - hru_module.f90#fertorgn
  - hru_module.f90#fertorgp
  - hru_module.f90#fertp
  - hru_module.f90#fertsolp
  - hru_module.f90#ihru
  - hydrograph_module.f90#wet
input_variables: []
reads: []
writes: []
purpose: "this subroutine applies N and P specified by date and; amount in the management file (.mgt) for rice fields during ponding periods; Jaehak 2022"
---

# pl_fert_wet

> [!info] Summary
> this subroutine applies N and P specified by date and; amount in the management file (.mgt) for rice fields during ponding periods; Jaehak 2022

## Basic Information
- **Type**: `subroutine`
- **Source file**: `pl_fert_wet.f90`
- **Modules used**:
  - [[mgt_operations_module.f90]]
  - [[fertilizer_data_module.f90]]
  - [[basin_module.f90]]
  - [[organic_mineral_mass_module.f90]]
  - [[hru_module.f90]]
  - [[hydrograph_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 0 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by:**

- [[actions.f90]]
- [[mgt_sched.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[basin_module.f90#bsn_cc]] - `basin_control_codes`
- [[fertilizer_data_module.f90#fertdb]] - `fertilizer_db`
- [[hru_module.f90#fertn]] - `real`
- [[hru_module.f90#fertnh3]] - `real`
- [[hru_module.f90#fertno3]] - `real`
- [[hru_module.f90#fertorgn]] - `real`
- [[hru_module.f90#fertorgp]] - `real`
- [[hru_module.f90#fertp]] - `real`
- [[hru_module.f90#fertsolp]] - `real`
- [[hru_module.f90#ihru]] - `integer`
- [[hydrograph_module.f90#wet]] - `hyd_output`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
