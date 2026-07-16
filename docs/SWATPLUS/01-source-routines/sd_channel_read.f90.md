---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: sd_channel_read.f90
note_file: sd_channel_read.f90
subroutine: sd_channel_read
module:
  - basin_module
  - input_file_module
  - maximum_data_module
  - channel_data_module
  - channel_velocity_module
  - ch_pesticide_module
  - ch_salt_module
  - ch_cs_module
  - sd_channel_module
  - hydrograph_module
  - constituent_mass_module
  - pesticide_data_module
  - pathogen_data_module
  - water_body_module
calls: []
reads:
  - in_cha%chan_ez
writes: []
purpose: ""
---

# sd_channel_read

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `sd_channel_read.f90`
- **Modules used**: [[basin_module.f90]], [[input_file_module.f90]], [[maximum_data_module.f90]], [[channel_data_module.f90]], [[channel_velocity_module.f90]], [[ch_pesticide_module.f90]], [[ch_salt_module.f90]], [[ch_cs_module.f90]], [[sd_channel_module.f90]], [[hydrograph_module.f90]], [[constituent_mass_module.f90]], [[pesticide_data_module.f90]], [[pathogen_data_module.f90]], [[water_body_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 1 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by** (live Dataview back-query):

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## File I/O
- **Reads**: `in_cha%chan_ez` _(variable; see file.cio)_

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
