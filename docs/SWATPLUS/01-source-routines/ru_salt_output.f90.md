---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: ru_salt_output.f90
note_file: ru_salt_output.f90
subroutine: ru_salt_output
module:
  - time_module
  - basin_module
  - hydrograph_module
  - salt_module
  - constituent_mass_module
calls: []
reads: []
writes: []
purpose: "this subroutine outputs salt mass loadings and concentrations from routing units"
---

# ru_salt_output

> [!info] Summary
> this subroutine outputs salt mass loadings and concentrations from routing units

## Basic Information
- **Type**: `subroutine`
- **Source file**: `ru_salt_output.f90`
- **Modules used**: [[time_module.f90]], [[basin_module.f90]], [[hydrograph_module.f90]], [[salt_module.f90]], [[constituent_mass_module.f90]]
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
