---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: stor_surfstor.f90
note_file: stor_surfstor.f90
subroutine: stor_surfstor
module:
  - septic_data_module
  - basin_module
  - time_module
  - constituent_mass_module
  - output_ls_pesticide_module
  - hru_module
calls: []
reads: []
writes: []
purpose: "this subroutine stores and lags sediment and nutrients in surface runoff"
---

# stor_surfstor

> [!info] Summary
> this subroutine stores and lags sediment and nutrients in surface runoff

## Basic Information
- **Type**: `subroutine`
- **Source file**: `stor_surfstor.f90`
- **Modules used**: [[septic_data_module.f90]], [[basin_module.f90]], [[time_module.f90]], [[constituent_mass_module.f90]], [[output_ls_pesticide_module.f90]], [[hru_module.f90]]
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
