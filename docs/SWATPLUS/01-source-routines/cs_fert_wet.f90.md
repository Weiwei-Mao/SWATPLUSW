---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: cs_fert_wet.f90
note_file: cs_fert_wet.f90
subroutine: cs_fert_wet
module:
  - mgt_operations_module
  - cs_module
  - constituent_mass_module
  - fertilizer_data_module
  - hru_module
  - res_cs_module
calls: []
reads: []
writes: []
purpose: "this subroutine adds constituent fertilizer to a wetland"
---

# cs_fert_wet

> [!info] Summary
> this subroutine adds constituent fertilizer to a wetland

## Basic Information
- **Type**: `subroutine`
- **Source file**: `cs_fert_wet.f90`
- **Modules used**: [[mgt_operations_module.f90]], [[cs_module.f90]], [[constituent_mass_module.f90]], [[fertilizer_data_module.f90]], [[hru_module.f90]], [[res_cs_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 0 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by** (live Dataview back-query):

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
