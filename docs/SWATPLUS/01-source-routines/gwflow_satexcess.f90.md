---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: gwflow_satexcess.f90
note_file: gwflow_satexcess.f90
subroutine: gwflow_satexcess
module:
  - gwflow_module
  - hydrograph_module
  - constituent_mass_module
calls: []
reads: []
writes: []
purpose: "this subroutine calculates the groundwater volume that enters the channel via saturation excess flow; (exchange volumes are used in gwflow_simulate, in groundwater balance equations)"
---

# gwflow_satexcess

> [!info] Summary
> this subroutine calculates the groundwater volume that enters the channel via saturation excess flow; (exchange volumes are used in gwflow_simulate, in groundwater balance equations)

## Basic Information
- **Type**: `subroutine`
- **Source file**: `gwflow_satexcess.f90`
- **Modules used**: [[gwflow_module.f90]], [[hydrograph_module.f90]], [[constituent_mass_module.f90]]
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
