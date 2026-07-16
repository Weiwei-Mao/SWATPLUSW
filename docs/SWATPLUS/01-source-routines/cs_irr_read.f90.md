---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: cs_irr_read.f90
note_file: cs_irr_read.f90
subroutine: cs_irr_read
module:
  - constituent_mass_module
  - input_file_module
  - maximum_data_module
calls: []
reads:
  - cs_irrigation
writes: []
purpose: ""
---

# cs_irr_read

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `cs_irr_read.f90`
- **Modules used**: [[constituent_mass_module.f90]], [[input_file_module.f90]], [[maximum_data_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 1 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by** (live Dataview back-query):

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## File I/O
- **Reads**: `cs_irrigation` _(variable; see file.cio)_

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
