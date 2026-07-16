---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: hru_cs_output.f90
note_file: hru_cs_output.f90
subroutine: hru_cs_output
module:
  - time_module
  - basin_module
  - hydrograph_module
  - cs_module
  - constituent_mass_module
calls: []
reads: []
writes: []
purpose: "this subroutine outputs constituent mass loadings and concentrations from HRUs"
---

# hru_cs_output

> [!info] Summary
> this subroutine outputs constituent mass loadings and concentrations from HRUs

## Basic Information
- **Type**: `subroutine`
- **Source file**: `hru_cs_output.f90`
- **Modules used**: [[time_module.f90]], [[basin_module.f90]], [[hydrograph_module.f90]], [[cs_module.f90]], [[constituent_mass_module.f90]]
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
