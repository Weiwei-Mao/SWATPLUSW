---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: res_pesticide_output.f90
note_file: res_pesticide_output.f90
subroutine: res_pesticide_output
module:
  - output_ls_pesticide_module
  - res_pesticide_module
  - plant_module
  - plant_data_module
  - time_module
  - basin_module
  - output_landscape_module
  - constituent_mass_module
  - hydrograph_module
calls: []
reads: []
writes: []
purpose: "this subroutine outputs HRU variables on daily, monthly and annual time steps"
---

# res_pesticide_output

> [!info] Summary
> this subroutine outputs HRU variables on daily, monthly and annual time steps

## Basic Information
- **Type**: `subroutine`
- **Source file**: `res_pesticide_output.f90`
- **Modules used**: [[output_ls_pesticide_module.f90]], [[res_pesticide_module.f90]], [[plant_module.f90]], [[plant_data_module.f90]], [[time_module.f90]], [[basin_module.f90]], [[output_landscape_module.f90]], [[constituent_mass_module.f90]], [[hydrograph_module.f90]]
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
