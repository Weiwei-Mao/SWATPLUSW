---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: se_reactions_aquifer.f90
note_file: se_reactions_aquifer.f90
subroutine: se_reactions_aquifer
module:
  - cs_data_module
calls: []
uses_variables:
  - cs_data_module.f90#cs_rct_aqu
  - cs_data_module.f90#num_geol_shale
input_variables: []
reads: []
writes: []
purpose: ""
---

# se_reactions_aquifer

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `se_reactions_aquifer.f90`
- **Modules used**:
  - [[cs_data_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 0 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by:**

- [[cs_rctn_aqu.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[cs_data_module.f90#cs_rct_aqu]] - `constituent_rct`
- [[cs_data_module.f90#num_geol_shale]] - `integer`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
