---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: mgt_harvresidue.f90
note_file: mgt_harvresidue.f90
subroutine: mgt_harvresidue
module:
  - plant_module
  - carbon_module
  - mgt_operations_module
  - organic_mineral_mass_module
calls: []
reads: []
writes: []
purpose: "this subroutine performs the harvest residue operation"
---

# mgt_harvresidue

> [!info] Summary
> this subroutine performs the harvest residue operation

## Basic Information
- **Type**: `subroutine`
- **Source file**: `mgt_harvresidue.f90`
- **Modules used**: [[plant_module.f90]], [[carbon_module.f90]], [[mgt_operations_module.f90]], [[organic_mineral_mass_module.f90]]
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
