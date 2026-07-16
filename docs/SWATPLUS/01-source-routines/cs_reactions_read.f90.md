---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: cs_reactions_read.f90
note_file: cs_reactions_read.f90
subroutine: cs_reactions_read
module:
  - hydrograph_module
  - constituent_mass_module
  - cs_data_module
calls: []
reads:
  - cs_reactions
writes: []
purpose: ""
---

# cs_reactions_read

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `cs_reactions_read.f90`
- **Modules used**: [[hydrograph_module.f90]], [[constituent_mass_module.f90]], [[cs_data_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 1 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by** (live Dataview back-query):

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## File I/O
- **Reads**: `cs_reactions` _(variable; see file.cio)_

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
