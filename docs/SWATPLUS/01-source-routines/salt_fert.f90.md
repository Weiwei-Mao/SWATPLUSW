---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: salt_fert.f90
note_file: salt_fert.f90
subroutine: salt_fert
module:
  - mgt_operations_module
  - salt_module
  - constituent_mass_module
  - fertilizer_data_module
calls: []
uses_variables:
  - constituent_mass_module.f90#cs_db
  - constituent_mass_module.f90#cs_soil
  - fertilizer_data_module.f90#fertdb
  - mgt_operations_module.f90#chemapp_db
  - salt_module.f90#fert_salt
  - salt_module.f90#fert_salt_flag
  - salt_module.f90#hsaltb_d
input_variables: []
reads: []
writes: []
purpose: "this subroutine adds salt fertilizer to the soil profile"
---

# salt_fert

> [!info] Summary
> this subroutine adds salt fertilizer to the soil profile

## Basic Information
- **Type**: `subroutine`
- **Source file**: `salt_fert.f90`
- **Modules used**:
  - [[mgt_operations_module.f90]]
  - [[salt_module.f90]]
  - [[constituent_mass_module.f90]]
  - [[fertilizer_data_module.f90]]
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
- [[constituent_mass_module.f90#cs_db]] - `constituents`
- [[constituent_mass_module.f90#cs_soil]] - `soil_constituent_mass`
- [[fertilizer_data_module.f90#fertdb]] - `fertilizer_db`
- [[mgt_operations_module.f90#chemapp_db]] - `chemical_application_operation`
- [[salt_module.f90#fert_salt]] - `fert_db_salt`
- [[salt_module.f90#fert_salt_flag]] - `integer`
- [[salt_module.f90#hsaltb_d]] - `object_salt_balance`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
