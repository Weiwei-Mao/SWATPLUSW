---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: path_ls_process.f90
note_file: path_ls_process.f90
subroutine: path_ls_process
module:
  - pathogen_data_module
  - constituent_mass_module
  - output_ls_pathogen_module
  - hru_module
  - soil_module
  - plant_module
  - climate_module
calls: []
reads: []
writes: []
purpose: ""
---

# path_ls_process

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `path_ls_process.f90`
- **Modules used**: [[pathogen_data_module.f90]], [[constituent_mass_module.f90]], [[output_ls_pathogen_module.f90]], [[hru_module.f90]], [[soil_module.f90]], [[plant_module.f90]], [[climate_module.f90]]
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
