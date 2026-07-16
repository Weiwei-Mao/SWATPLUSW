---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: rls_routesoil.f90
note_file: rls_routesoil.f90
subroutine: rls_routesoil
module:
  - hru_module
  - soil_module
  - hydrograph_module
calls: []
reads: []
writes: []
purpose: ""
---

# rls_routesoil

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `rls_routesoil.f90`
- **Modules used**: [[hru_module.f90]], [[soil_module.f90]], [[hydrograph_module.f90]]
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
