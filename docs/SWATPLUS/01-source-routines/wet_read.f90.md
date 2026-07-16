---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: wet_read.f90
note_file: wet_read.f90
subroutine: wet_read
module:
  - basin_module
  - input_file_module
  - maximum_data_module
  - reservoir_data_module
  - reservoir_module
  - hydrograph_module
  - constituent_mass_module
  - pesticide_data_module
  - res_salt_module
  - res_cs_module
calls: []
reads:
  - in_res%wet
writes: []
purpose: ""
---

# wet_read

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `wet_read.f90`
- **Modules used**: [[basin_module.f90]], [[input_file_module.f90]], [[maximum_data_module.f90]], [[reservoir_data_module.f90]], [[reservoir_module.f90]], [[hydrograph_module.f90]], [[constituent_mass_module.f90]], [[pesticide_data_module.f90]], [[res_salt_module.f90]], [[res_cs_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 1 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by** (live Dataview back-query):

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## File I/O
- **Reads**: `in_res%wet` _(variable; see file.cio)_

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
