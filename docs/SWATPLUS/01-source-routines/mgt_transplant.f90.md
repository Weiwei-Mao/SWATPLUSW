---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: mgt_transplant.f90
note_file: mgt_transplant.f90
subroutine: mgt_transplant
module:
  - hru_module
  - plant_module
  - plant_data_module
  - organic_mineral_mass_module
calls:
  - pl_root_gro
  - pl_seed_gro
  - pl_partition
reads: []
writes: []
purpose: ""
---

# mgt_transplant

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `mgt_transplant.f90`
- **Modules used**: [[hru_module.f90]], [[plant_module.f90]], [[plant_data_module.f90]], [[organic_mineral_mass_module.f90]]
- **Subroutine calls**: 3 | **Files read**: 0 | **Files written**: 0

## Call Relationships
**This routine calls:**

- [[pl_root_gro.f90]]
- [[pl_seed_gro.f90]]
- [[pl_partition.f90]]

**Called by** (live Dataview back-query):

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
