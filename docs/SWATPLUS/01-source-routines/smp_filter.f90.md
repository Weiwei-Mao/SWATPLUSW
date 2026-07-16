---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: smp_filter.f90
note_file: smp_filter.f90
subroutine: smp_filter
module:
  - basin_module
  - hru_module
  - soil_module
  - constituent_mass_module
  - time_module
  - output_ls_pesticide_module
calls: []
reads: []
writes: []
purpose: "this subroutine calculates the reduction of pollutants in surface runoff; due to an edge of field filter or buffer strip"
---

# smp_filter

> [!info] Summary
> this subroutine calculates the reduction of pollutants in surface runoff; due to an edge of field filter or buffer strip

## Basic Information
- **Type**: `subroutine`
- **Source file**: `smp_filter.f90`
- **Modules used**: [[basin_module.f90]], [[hru_module.f90]], [[soil_module.f90]], [[constituent_mass_module.f90]], [[time_module.f90]], [[output_ls_pesticide_module.f90]]
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
