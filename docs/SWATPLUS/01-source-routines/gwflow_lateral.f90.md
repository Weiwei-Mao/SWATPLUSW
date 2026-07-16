---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: gwflow_lateral.f90
note_file: gwflow_lateral.f90
subroutine: gwflow_lateral
module:
  - gwflow_module
  - time_module
calls:
  - gwflow_heat
  - gwflow_solute
reads: []
writes: []
purpose: "this subroutine calculates lateral groundwater flow between adjacent cells; using Darcy's Law, then updates head and storage; (extracted from gwflow_simulate)"
---

# gwflow_lateral

> [!info] Summary
> this subroutine calculates lateral groundwater flow between adjacent cells; using Darcy's Law, then updates head and storage; (extracted from gwflow_simulate)

## Basic Information
- **Type**: `subroutine`
- **Source file**: `gwflow_lateral.f90`
- **Modules used**: [[gwflow_module.f90]], [[time_module.f90]]
- **Subroutine calls**: 2 | **Files read**: 0 | **Files written**: 0

## Call Relationships
**This routine calls:**

- [[gwflow_heat.f90]]
- [[gwflow_solute.f90]]

**Called by** (live Dataview back-query):

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
