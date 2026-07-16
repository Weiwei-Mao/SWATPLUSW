---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: regres.f90
note_file: regres.f90
subroutine: regres
module:
  - hru_module
  - climate_module
  - urban_data_module
calls: []
reads: []
writes: []
purpose: "this function calculates constituent loadings to the main channel using; USGS regression equations"
---

# regres

> [!info] Summary
> this function calculates constituent loadings to the main channel using; USGS regression equations

## Basic Information
- **Type**: `subroutine`
- **Source file**: `regres.f90`
- **Modules used**: [[hru_module.f90]], [[climate_module.f90]], [[urban_data_module.f90]]
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
