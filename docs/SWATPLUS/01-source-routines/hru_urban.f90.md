---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: hru_urban.f90
note_file: hru_urban.f90
subroutine: hru_urban
module:
  - hru_module
  - urban_data_module
  - hydrograph_module
  - climate_module
calls: []
reads: []
writes: []
purpose: "this subroutine computes loadings from urban areas using the; USGS regression equations or a build-up/wash-off algorithm"
---

# hru_urban

> [!info] Summary
> this subroutine computes loadings from urban areas using the; USGS regression equations or a build-up/wash-off algorithm

## Basic Information
- **Type**: `subroutine`
- **Source file**: `hru_urban.f90`
- **Modules used**: [[hru_module.f90]], [[urban_data_module.f90]], [[hydrograph_module.f90]], [[climate_module.f90]]
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
