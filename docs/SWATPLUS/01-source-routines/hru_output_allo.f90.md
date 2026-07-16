---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: hru_output_allo.f90
note_file: hru_output_allo.f90
subroutine: hru_output_allo
module:
  - output_landscape_module
  - maximum_data_module
  - hydrograph_module
  - constituent_mass_module
  - output_ls_pesticide_module
  - output_ls_pathogen_module
  - salt_module
  - cs_module
  - carbon_module
calls: []
reads: []
writes: []
purpose: ""
---

# hru_output_allo

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `hru_output_allo.f90`
- **Modules used**: [[output_landscape_module.f90]], [[maximum_data_module.f90]], [[hydrograph_module.f90]], [[constituent_mass_module.f90]], [[output_ls_pesticide_module.f90]], [[output_ls_pathogen_module.f90]], [[salt_module.f90]], [[cs_module.f90]], [[carbon_module.f90]]
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
