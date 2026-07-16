---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: cbn_zhang2.f90
note_file: cbn_zhang2.f90
subroutine: cbn_zhang2
module:
  - hru_module
  - soil_module
  - basin_module
  - organic_mineral_mass_module
  - carbon_module
  - output_landscape_module
  - tillage_data_module
calls:
  - nut_np_flow
reads: []
writes: []
purpose: ""
---

# cbn_zhang2

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `cbn_zhang2.f90`
- **Modules used**: [[hru_module.f90]], [[soil_module.f90]], [[basin_module.f90]], [[organic_mineral_mass_module.f90]], [[carbon_module.f90]], [[output_landscape_module.f90]], [[tillage_data_module.f90]]
- **Subroutine calls**: 1 | **Files read**: 0 | **Files written**: 0

## Call Relationships
**This routine calls:**

- [[nut_np_flow.f90]]

**Called by** (live Dataview back-query):

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
