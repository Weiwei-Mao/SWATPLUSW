---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: pl_fert.f90
note_file: pl_fert.f90
subroutine: pl_fert
module:
  - mgt_operations_module
  - fertilizer_data_module
  - basin_module
  - organic_mineral_mass_module
  - hru_module
calls: []
reads: []
writes: []
purpose: "this subroutine applies N and P specified by date and; amount in the management file (.mgt)"
---

# pl_fert

> [!info] Summary
> this subroutine applies N and P specified by date and; amount in the management file (.mgt)

## Basic Information
- **Type**: `subroutine`
- **Source file**: `pl_fert.f90`
- **Modules used**: [[mgt_operations_module.f90]], [[fertilizer_data_module.f90]], [[basin_module.f90]], [[organic_mineral_mass_module.f90]], [[hru_module.f90]]
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
