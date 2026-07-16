---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: carbon_layers_read.f90
note_file: carbon_layers_read.f90
subroutine: carbon_layers_read
module:
  - carbon_module
calls: []
reads:
  - carbon_layers.prt
writes: []
purpose: ""
---

# carbon_layers_read

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `carbon_layers_read.f90`
- **Modules used**: [[carbon_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 1 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by** (live Dataview back-query):

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## File I/O
- **Reads**: `carbon_layers.prt`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
