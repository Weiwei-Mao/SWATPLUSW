---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: path_cha_res_read.f90
note_file: path_cha_res_read.f90
subroutine: path_cha_res_read
module:
  - constituent_mass_module
  - input_file_module
  - maximum_data_module
  - channel_data_module
  - hydrograph_module
  - sd_channel_module
  - organic_mineral_mass_module
calls: []
reads:
  - in_init%path_water
writes: []
purpose: ""
---

# path_cha_res_read

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `path_cha_res_read.f90`
- **Modules used**: [[constituent_mass_module.f90]], [[input_file_module.f90]], [[maximum_data_module.f90]], [[channel_data_module.f90]], [[hydrograph_module.f90]], [[sd_channel_module.f90]], [[organic_mineral_mass_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 1 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by** (live Dataview back-query):

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## File I/O
- **Reads**: `in_init%path_water` _(variable; see file.cio)_

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
