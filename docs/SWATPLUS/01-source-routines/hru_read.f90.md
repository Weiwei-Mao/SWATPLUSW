---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: hru_read.f90
note_file: hru_read.f90
subroutine: hru_read
module:
  - maximum_data_module
  - reservoir_data_module
  - landuse_data_module
  - hydrology_data_module
  - topography_data_module
  - soil_data_module
  - input_file_module
  - hru_module
  - constituent_mass_module
calls:
  - allocate_parms
reads:
  - in_hru%hru_data
writes: []
purpose: ""
---

# hru_read

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `hru_read.f90`
- **Modules used**: [[maximum_data_module.f90]], [[reservoir_data_module.f90]], [[landuse_data_module.f90]], [[hydrology_data_module.f90]], [[topography_data_module.f90]], [[soil_data_module.f90]], [[input_file_module.f90]], [[hru_module.f90]], [[constituent_mass_module.f90]]
- **Subroutine calls**: 1 | **Files read**: 1 | **Files written**: 0

## Call Relationships
**This routine calls:**

- [[allocate_parms.f90]]

**Called by** (live Dataview back-query):

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## File I/O
- **Reads**: `in_hru%hru_data` _(variable; see file.cio)_

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
