---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: salt_fert_wet.f90
note_file: salt_fert_wet.f90
subroutine: salt_fert_wet
module:
  - mgt_operations_module
  - salt_module
  - constituent_mass_module
  - fertilizer_data_module
  - hru_module
  - res_salt_module
calls: []
uses_variables:
  - constituent_mass_module.f90#cs_db
  - constituent_mass_module.f90#wet_water
  - hru_module.f90#hru
  - res_salt_module.f90#wetsalt_d
  - salt_module.f90#fert_salt
input_variables: []
reads: []
writes: []
purpose: "this subroutine adds salt fertilizer to a wetland"
---

# salt_fert_wet

> [!info] Summary
> this subroutine adds salt fertilizer to a wetland

## Basic Information
- **Type**: `subroutine`
- **Source file**: `salt_fert_wet.f90`
- **Modules used**:
  - [[mgt_operations_module.f90]]
  - [[salt_module.f90]]
  - [[constituent_mass_module.f90]]
  - [[fertilizer_data_module.f90]]
  - [[hru_module.f90]]
  - [[res_salt_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 0 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by:**

- [[mgt_sched.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[constituent_mass_module.f90#cs_db]] - `constituents`
- [[constituent_mass_module.f90#wet_water]] - `constituent_mass`
- [[hru_module.f90#hru]] - `hydrologic_response_unit`
- [[res_salt_module.f90#wetsalt_d]] - `res_salt_output`
- [[salt_module.f90#fert_salt]] - `fert_db_salt`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
