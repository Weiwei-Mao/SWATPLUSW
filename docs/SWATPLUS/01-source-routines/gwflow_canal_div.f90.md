---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: gwflow_canal_div.f90
note_file: gwflow_canal_div.f90
subroutine: gwflow_canal_div
module:
  - gwflow_module
  - hydrograph_module
  - time_module
  - constituent_mass_module
  - hru_module
  - res_salt_module
  - res_cs_module
  - salt_module
  - cs_module
calls: []
reads: []
writes: []
purpose: "this subroutine calculates the water exchange volume between irrigation canals and connected grid cells; for canals that are connected to a point source diversion (recall object); seepage water should be; removed from the diverted water volume."
---

# gwflow_canal_div

> [!info] Summary
> this subroutine calculates the water exchange volume between irrigation canals and connected grid cells; for canals that are connected to a point source diversion (recall object); seepage water should be; removed from the diverted water volume.

## Basic Information
- **Type**: `subroutine`
- **Source file**: `gwflow_canal_div.f90`
- **Modules used**: [[gwflow_module.f90]], [[hydrograph_module.f90]], [[time_module.f90]], [[constituent_mass_module.f90]], [[hru_module.f90]], [[res_salt_module.f90]], [[res_cs_module.f90]], [[salt_module.f90]], [[cs_module.f90]]
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
