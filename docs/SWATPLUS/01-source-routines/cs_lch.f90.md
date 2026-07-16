---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: cs_lch.f90
note_file: cs_lch.f90
subroutine: cs_lch
module:
  - hru_module
  - basin_module
  - constituent_mass_module
  - soil_module
  - gwflow_module
calls: []
reads: []
writes: []
purpose: "this subroutine simulates the loss of constituent mass via surface runoff,; lateral flow, tile flow, and percolation out of the profile"
---

# cs_lch

> [!info] Summary
> this subroutine simulates the loss of constituent mass via surface runoff,; lateral flow, tile flow, and percolation out of the profile

## Basic Information
- **Type**: `subroutine`
- **Source file**: `cs_lch.f90`
- **Modules used**: [[hru_module.f90]], [[basin_module.f90]], [[constituent_mass_module.f90]], [[soil_module.f90]], [[gwflow_module.f90]]
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
