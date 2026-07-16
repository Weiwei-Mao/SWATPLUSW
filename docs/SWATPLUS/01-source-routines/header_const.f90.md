---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: header_const.f90
note_file: header_const.f90
subroutine: header_const
module:
  - basin_module
  - reservoir_module
  - hydrograph_module
  - constituent_mass_module
  - ch_cs_module
  - res_cs_module
  - cs_module
  - cs_aquifer
  - output_path_module
calls:
  - open_output_file
reads: []
writes: []
purpose: ""
---

# header_const

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `header_const.f90`
- **Modules used**: [[basin_module.f90]], [[reservoir_module.f90]], [[hydrograph_module.f90]], [[constituent_mass_module.f90]], [[ch_cs_module.f90]], [[res_cs_module.f90]], [[cs_module.f90]], [[cs_aquifer.f90]], [[output_path_module.f90]]
- **Subroutine calls**: 1 | **Files read**: 0 | **Files written**: 0

## Call Relationships
**This routine calls:**

- `open_output_file`

**Called by** (live Dataview back-query):

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
