---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: wet_read_salt_cs.f90
note_file: wet_read_salt_cs.f90
subroutine: wet_read_salt_cs
module:
  - maximum_data_module
  - reservoir_data_module
  - constituent_mass_module
  - reservoir_module
  - res_salt_module
  - res_cs_module
calls: []
reads:
  - wetland.wet_cs
writes: []
purpose: ""
---

# wet_read_salt_cs

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `wet_read_salt_cs.f90`
- **Modules used**: [[maximum_data_module.f90]], [[reservoir_data_module.f90]], [[constituent_mass_module.f90]], [[reservoir_module.f90]], [[res_salt_module.f90]], [[res_cs_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 1 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by** (live Dataview back-query):

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## File I/O
- **Reads**: `wetland.wet_cs`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
