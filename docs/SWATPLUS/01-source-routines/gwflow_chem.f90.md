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
uses_variables:
  - constituent_mass_module.f90#cs_db
  - gwflow_module.f90#gw_state
  - gwflow_module.f90#gwsol_chem
  - gwflow_module.f90#gwsol_cons
  - gwflow_module.f90#gwsol_minl
  - gwflow_module.f90#gwsol_rctn
  - gwflow_module.f90#gwsol_salt
  - gwflow_module.f90#gwsol_state
  - gwflow_module.f90#mass_rct
input_variables: []
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
- **Modules used**:
  - [[gwflow_module.f90]]
  - [[hydrograph_module.f90]]
  - [[constituent_mass_module.f90]]
- **Subroutine calls**: 1 | **Files read**: 0 | **Files written**: 0

## Call Relationships
**This routine calls:**

- `gwflow_minl`

**Called by:**

- [[gwflow_solute.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[constituent_mass_module.f90#cs_db]] - `constituents`
- [[gwflow_module.f90#gw_state]] - `groundwater_state`
- [[gwflow_module.f90#gwsol_chem]] - `solute_chem`
- [[gwflow_module.f90#gwsol_cons]] - `integer`
- [[gwflow_module.f90#gwsol_minl]] - `integer`
- [[gwflow_module.f90#gwsol_rctn]] - `real, allocatable`
- [[gwflow_module.f90#gwsol_salt]] - `integer`
- [[gwflow_module.f90#gwsol_state]] - `object_solute_state`
- [[gwflow_module.f90#mass_rct]] - `real, allocatable`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
