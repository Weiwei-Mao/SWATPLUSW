---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: topohyd_init.f90
note_file: topohyd_init.f90
subroutine: topohyd_init
module:
  - hydrograph_module
  - hru_module
  - hydrology_data_module
  - topography_data_module
  - soil_data_module
  - plant_module
calls:
  - ascrv
reads: []
writes: []
purpose: ""
---

# topohyd_init

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `topohyd_init.f90`
- **Modules used**: [[hydrograph_module.f90]], [[hru_module.f90]], [[hydrology_data_module.f90]], [[topography_data_module.f90]], [[soil_data_module.f90]], [[plant_module.f90]]
- **Subroutine calls**: 1 | **Files read**: 0 | **Files written**: 0

## Call Relationships
**This routine calls:**

- [[ascrv.f90]]

**Called by** (live Dataview back-query):

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
