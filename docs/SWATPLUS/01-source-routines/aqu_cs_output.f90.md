---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: aqu_cs_output.f90
note_file: aqu_cs_output.f90
subroutine: aqu_cs_output
module:
  - time_module
  - basin_module
  - aquifer_module
  - hydrograph_module
  - cs_aquifer
  - constituent_mass_module
calls: []
reads: []
writes: []
purpose: "this subroutine outputs constituent mass loadings and concentrations in aquifers"
---

# aqu_cs_output

> [!info] Summary
> this subroutine outputs constituent mass loadings and concentrations in aquifers

## Basic Information
- **Type**: `subroutine`
- **Source file**: `aqu_cs_output.f90`
- **Modules used**: [[time_module.f90]], [[basin_module.f90]], [[aquifer_module.f90]], [[hydrograph_module.f90]], [[cs_aquifer.f90]], [[constituent_mass_module.f90]]
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
