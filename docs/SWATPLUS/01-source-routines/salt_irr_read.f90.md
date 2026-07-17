---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: salt_irr_read.f90
note_file: salt_irr_read.f90
subroutine: salt_irr_read
module:
  - constituent_mass_module
  - input_file_module
  - maximum_data_module
calls: []
uses_variables:
  - constituent_mass_module.f90#cs_db
  - constituent_mass_module.f90#salt_water_irr
input_variables:
  - constituent_mass_module.f90#salt_water_irr
reads:
  - salt_irrigation
writes: []
purpose: ""
---

# salt_irr_read

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `salt_irr_read.f90`
- **Modules used**:
  - [[constituent_mass_module.f90]]
  - [[input_file_module.f90]]
  - [[maximum_data_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 1 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by:**

- [[proc_read.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[constituent_mass_module.f90#cs_db]] - `constituents`
- [[constituent_mass_module.f90#salt_water_irr]] - `cs_irrigation_concentrations`

**Populated by file reads:**

- [[constituent_mass_module.f90#salt_water_irr]]

## File I/O
- **Reads**:
  - [[salt_irrigation]]

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
