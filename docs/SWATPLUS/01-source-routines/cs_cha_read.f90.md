---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: cs_cha_read.f90
note_file: cs_cha_read.f90
subroutine: cs_cha_read
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
  - cs_channel.ini
  - cs_streamobs
writes:
  - cs_streamobs_output
purpose: ""
---

# cs_cha_read

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `cs_cha_read.f90`
- **Modules used**: [[constituent_mass_module.f90]], [[input_file_module.f90]], [[maximum_data_module.f90]], [[channel_data_module.f90]], [[hydrograph_module.f90]], [[sd_channel_module.f90]], [[organic_mineral_mass_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 2 | **Files written**: 1

## Call Relationships
(No call statements; leaf node.)

**Called by** (live Dataview back-query):

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## File I/O
- **Writes**: `cs_streamobs_output`
- **Reads**: `cs_channel.ini`, `cs_streamobs` _(variable; see file.cio)_

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
