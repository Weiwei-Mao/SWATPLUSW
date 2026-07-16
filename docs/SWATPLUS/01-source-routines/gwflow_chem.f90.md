---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: gwflow_chem.f90
note_file: gwflow_chem.f90
subroutine: gwflow_chem
module:
  - gwflow_module
  - hydrograph_module
  - constituent_mass_module
calls:
  - gwflow_minl
reads: []
writes: []
purpose: "this subroutine calculates chemical reactions in gwflow cells.; Fills module arrays mass_rct and mass_min. Called from gwflow_solute."
---

# gwflow_chem

> [!info] Summary
> this subroutine calculates chemical reactions in gwflow cells.; Fills module arrays mass_rct and mass_min. Called from gwflow_solute.

## Basic Information
- **Type**: `subroutine`
- **Source file**: `gwflow_chem.f90`
- **Modules used**: [[gwflow_module.f90]], [[hydrograph_module.f90]], [[constituent_mass_module.f90]]
- **Subroutine calls**: 1 | **Files read**: 0 | **Files written**: 0

## Call Relationships
**This routine calls:**

- `gwflow_minl`

**Called by** (live Dataview back-query):

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
