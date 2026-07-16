---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: hru_urbanhr.f90
note_file: hru_urbanhr.f90
subroutine: hru_urbanhr
module:
  - hru_module
  - plant_module
  - urban_data_module
  - climate_module
  - time_module
calls:
  - hru_sweep
reads: []
writes: []
purpose: "this subroutine computes loadings from urban areas using the; a build-up/wash-off algorithm at subdaily time intervals"
---

# hru_urbanhr

> [!info] Summary
> this subroutine computes loadings from urban areas using the; a build-up/wash-off algorithm at subdaily time intervals

## Basic Information
- **Type**: `subroutine`
- **Source file**: `hru_urbanhr.f90`
- **Modules used**: [[hru_module.f90]], [[plant_module.f90]], [[urban_data_module.f90]], [[climate_module.f90]], [[time_module.f90]]
- **Subroutine calls**: 1 | **Files read**: 0 | **Files written**: 0

## Call Relationships
**This routine calls:**

- [[hru_sweep.f90]]

**Called by** (live Dataview back-query):

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
