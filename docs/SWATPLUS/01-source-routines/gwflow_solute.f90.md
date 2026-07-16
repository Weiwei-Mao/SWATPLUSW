---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: gwflow_solute.f90
note_file: gwflow_solute.f90
subroutine: gwflow_solute
module:
  - gwflow_module
  - time_module
calls:
  - gwflow_chem
reads: []
writes: []
purpose: "this subroutine calculates solute advection, dispersion, chemical; reactions, and sorption for groundwater solute transport. Called from; gwflow_lateral once per flow time step. Contains its own sub-timestep"
---

# gwflow_solute

> [!info] Summary
> this subroutine calculates solute advection, dispersion, chemical; reactions, and sorption for groundwater solute transport. Called from; gwflow_lateral once per flow time step. Contains its own sub-timestep

## Basic Information
- **Type**: `subroutine`
- **Source file**: `gwflow_solute.f90`
- **Modules used**: [[gwflow_module.f90]], [[time_module.f90]]
- **Subroutine calls**: 1 | **Files read**: 0 | **Files written**: 0

## Call Relationships
**This routine calls:**

- [[gwflow_chem.f90]]

**Called by** (live Dataview back-query):

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
