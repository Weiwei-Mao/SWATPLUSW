---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: cs_fert.f90
note_file: cs_fert.f90
subroutine: cs_fert
module:
  - mgt_operations_module
  - cs_module
  - constituent_mass_module
  - fertilizer_data_module
calls: []
uses_variables:
  - constituent_mass_module.f90#cs_db
  - constituent_mass_module.f90#cs_soil
  - cs_module.f90#fert_cs
  - cs_module.f90#fert_cs_flag
  - cs_module.f90#hcsb_d
  - mgt_operations_module.f90#chemapp_db
input_variables: []
reads: []
writes: []
purpose: "this subroutine adds constituent fertilizer to the soil profile"
---

# cs_fert

> [!info] Summary
> this subroutine adds constituent fertilizer to the soil profile

## Basic Information
- **Type**: `subroutine`
- **Source file**: `cs_fert.f90`
- **Modules used**:
  - [[mgt_operations_module.f90]]
  - [[cs_module.f90]]
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
- [[cs_module.f90#fert_cs]] - `fert_db_cs`
- [[cs_module.f90#fert_cs_flag]] - `integer`
- [[cs_module.f90#hcsb_d]] - `object_cs_balance`
- [[mgt_operations_module.f90#chemapp_db]] - `chemical_application_operation`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
