---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: sep_biozone.f90
note_file: sep_biozone.f90
subroutine: sep_biozone
module:
  - septic_data_module
  - basin_module
  - pathogen_data_module
  - organic_mineral_mass_module
  - hru_module
  - soil_module
  - time_module
calls: []
reads: []
writes: []
purpose: "This subroutine conducts biophysical processes occurring; in the biozone layer of a septic HRU."
---

# sep_biozone

> [!info] Summary
> This subroutine conducts biophysical processes occurring; in the biozone layer of a septic HRU.

## Basic Information
- **Type**: `subroutine`
- **Source file**: `sep_biozone.f90`
- **Modules used**: [[septic_data_module.f90]], [[basin_module.f90]], [[pathogen_data_module.f90]], [[organic_mineral_mass_module.f90]], [[hru_module.f90]], [[soil_module.f90]], [[time_module.f90]]
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
