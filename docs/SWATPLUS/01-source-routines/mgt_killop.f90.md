---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: mgt_killop.f90
note_file: mgt_killop.f90
subroutine: mgt_killop
module:
  - basin_module
  - organic_mineral_mass_module
  - hru_module
  - soil_module
  - plant_module
  - constituent_mass_module
  - carbon_module
calls:
  - pl_rootfr
  - plg_zero
reads: []
writes: []
purpose: "this subroutine performs the kill operation"
---

# mgt_killop

> [!info] Summary
> this subroutine performs the kill operation

## Basic Information
- **Type**: `subroutine`
- **Source file**: `mgt_killop.f90`
- **Modules used**: [[basin_module.f90]], [[organic_mineral_mass_module.f90]], [[hru_module.f90]], [[soil_module.f90]], [[plant_module.f90]], [[constituent_mass_module.f90]], [[carbon_module.f90]]
- **Subroutine calls**: 2 | **Files read**: 0 | **Files written**: 0

## Call Relationships
**This routine calls:**

- [[pl_rootfr.f90]]
- `plg_zero`

**Called by** (live Dataview back-query):

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
