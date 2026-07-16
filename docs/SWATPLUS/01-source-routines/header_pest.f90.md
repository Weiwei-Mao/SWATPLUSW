---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: header_pest.f90
note_file: header_pest.f90
subroutine: header_pest
module:
  - basin_module
  - reservoir_module
  - hydrograph_module
  - output_ls_pesticide_module
  - constituent_mass_module
  - ch_pesticide_module
  - res_pesticide_module
  - aqu_pesticide_module
  - output_path_module
calls:
  - open_output_file
reads: []
writes: []
purpose: ""
---

# header_pest

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `header_pest.f90`
- **Modules used**: [[basin_module.f90]], [[reservoir_module.f90]], [[hydrograph_module.f90]], [[output_ls_pesticide_module.f90]], [[constituent_mass_module.f90]], [[ch_pesticide_module.f90]], [[res_pesticide_module.f90]], [[aqu_pesticide_module.f90]], [[output_path_module.f90]]
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
