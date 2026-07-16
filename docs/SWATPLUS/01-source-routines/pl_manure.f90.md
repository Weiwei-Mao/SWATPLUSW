---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: pl_manure.f90
note_file: pl_manure.f90
subroutine: pl_manure
module:
  - mgt_operations_module
  - fertilizer_data_module
  - basin_module
  - soil_module
  - organic_mineral_mass_module
  - hru_module
calls: []
uses_variables:
  - basin_module.f90#bsn_cc
  - fertilizer_data_module.f90#manure_om
  - hru_module.f90#fertn
  - hru_module.f90#fertnh3
  - hru_module.f90#fertno3
  - hru_module.f90#fertorgn
  - hru_module.f90#fertorgp
  - hru_module.f90#fertp
  - hru_module.f90#fertsolp
  - hru_module.f90#ihru
  - mgt_operations_module.f90#chemapp_db
  - organic_mineral_mass_module.f90#soil1
  - soil_module.f90#soil
input_variables: []
reads: []
writes: []
purpose: "this subroutine applies N and P specified by date and; amount in the management file (.mgt)"
---

# pl_manure

> [!info] Summary
> this subroutine applies N and P specified by date and; amount in the management file (.mgt)

## Basic Information
- **Type**: `subroutine`
- **Source file**: `pl_manure.f90`
- **Modules used**:
  - [[mgt_operations_module.f90]]
  - [[fertilizer_data_module.f90]]
  - [[basin_module.f90]]
  - [[soil_module.f90]]
  - [[organic_mineral_mass_module.f90]]
  - [[hru_module.f90]]
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
- [[fertilizer_data_module.f90#manure_om]] - `manure_attributes`
- [[hru_module.f90#fertn]] - `real`
- [[hru_module.f90#fertnh3]] - `real`
- [[hru_module.f90#fertno3]] - `real`
- [[hru_module.f90#fertorgn]] - `real`
- [[hru_module.f90#fertorgp]] - `real`
- [[hru_module.f90#fertp]] - `real`
- [[hru_module.f90#fertsolp]] - `real`
- [[hru_module.f90#ihru]] - `integer`
- [[mgt_operations_module.f90#chemapp_db]] - `chemical_application_operation`
- [[organic_mineral_mass_module.f90#soil1]] - `soil_profile_mass`
- [[soil_module.f90#soil]] - `soil_profile`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
