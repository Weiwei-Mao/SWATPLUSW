---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: gwflow_chan_read.f90
note_file: gwflow_chan_read.f90
subroutine: gwflow_chan_read
module:
  - gwflow_module
  - hydrograph_module
  - utils
calls:
  - split_line
reads:
  - chancell.gw
  - chan_depth.gw
writes: []
purpose: ""
---

# gwflow_chan_read

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `gwflow_chan_read.f90`
- **Modules used**: [[gwflow_module.f90]], [[hydrograph_module.f90]], [[utils.f90]]
- **Subroutine calls**: 1 | **Files read**: 2 | **Files written**: 0

## Call Relationships
**This routine calls:**

- `split_line`

**Called by** (live Dataview back-query):

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## File I/O
- **Reads**: `chancell.gw`, `chan_depth.gw`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
