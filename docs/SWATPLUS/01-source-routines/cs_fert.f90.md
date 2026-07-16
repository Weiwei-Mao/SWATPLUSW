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
- **Modules used**: [[mgt_operations_module.f90]], [[cs_module.f90]], [[constituent_mass_module.f90]], [[fertilizer_data_module.f90]]
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
