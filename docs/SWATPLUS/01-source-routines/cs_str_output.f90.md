---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: cs_str_output.f90
note_file: cs_str_output.f90
subroutine: cs_str_output
module:
  - hydrograph_module
  - constituent_mass_module
  - ch_cs_module
  - time_module
calls: []
reads: []
writes: []
purpose: "this subroutine prints out daily constituent data for specified channels"
---

# cs_str_output

> [!info] Summary
> this subroutine prints out daily constituent data for specified channels

## Basic Information
- **Type**: `subroutine`
- **Source file**: `cs_str_output.f90`
- **Modules used**: [[hydrograph_module.f90]], [[constituent_mass_module.f90]], [[ch_cs_module.f90]], [[time_module.f90]]
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
