---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: pest_apply.f90
note_file: pest_apply.f90
subroutine: pest_apply
module:
  - mgt_operations_module
  - basin_module
  - soil_module
  - plant_module
  - output_ls_pesticide_module
  - constituent_mass_module
calls: []
uses_variables:
  - constituent_mass_module.f90#cs_pl
  - constituent_mass_module.f90#cs_soil
  - mgt_operations_module.f90#chemapp_db
  - output_ls_pesticide_module.f90#hpestb_d
  - plant_module.f90#pcom
input_variables: []
reads: []
writes: []
purpose: "this subroutine applies pesticide"
---

# pest_apply

> [!info] Summary
> this subroutine applies pesticide

## Basic Information
- **Type**: `subroutine`
- **Source file**: `pest_apply.f90`
- **Modules used**:
  - [[mgt_operations_module.f90]]
  - [[basin_module.f90]]
  - [[soil_module.f90]]
  - [[plant_module.f90]]
  - [[output_ls_pesticide_module.f90]]
  - [[constituent_mass_module.f90]]
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
- [[constituent_mass_module.f90#cs_pl]] - `plant_constituent_mass`
- [[constituent_mass_module.f90#cs_soil]] - `soil_constituent_mass`
- [[mgt_operations_module.f90#chemapp_db]] - `chemical_application_operation`
- [[output_ls_pesticide_module.f90#hpestb_d]] - `object_pesticide_balance`
- [[plant_module.f90#pcom]] - `plant_community`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
