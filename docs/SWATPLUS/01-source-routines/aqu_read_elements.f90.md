---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: aqu_read_elements.f90
note_file: aqu_read_elements.f90
subroutine: aqu_read_elements
module:
  - input_file_module
  - calibration_data_module
  - hydrograph_module
  - aquifer_module
  - maximum_data_module
calls:
  - define_unit_elements
reads:
  - in_regs%def_aqu
  - in_regs%def_aqu
  - in_regs%ele_aqu
writes: []
purpose: ""
---

# aqu_read_elements

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `aqu_read_elements.f90`
- **Modules used**: [[input_file_module.f90]], [[calibration_data_module.f90]], [[hydrograph_module.f90]], [[aquifer_module.f90]], [[maximum_data_module.f90]]
- **Subroutine calls**: 1 | **Files read**: 3 | **Files written**: 0

## Call Relationships
**This routine calls:**

- [[define_unit_elements.f90]]

**Called by** (live Dataview back-query):

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## File I/O
- **Reads**: `in_regs%def_aqu` _(variable; see file.cio)_, `in_regs%def_aqu` _(variable; see file.cio)_, `in_regs%ele_aqu` _(variable; see file.cio)_

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
