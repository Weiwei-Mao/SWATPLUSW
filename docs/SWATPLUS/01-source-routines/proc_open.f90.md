---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: proc_open.f90
note_file: proc_open.f90
subroutine: proc_open
module: []
calls:
  - output_landscape_init
  - header_channel
  - header_aquifer
  - header_sd_channel
  - header_mgt
  - header_lu_change
  - header_yield
  - header_hyd
  - header_reservoir
  - header_wetland
  - header_water_allocation
  - header_pest
  - header_path
  - header_salt
  - header_const
  - header_write
reads: []
writes: []
purpose: ""
---

# proc_open

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `proc_open.f90`
- **Modules used**: -
- **Subroutine calls**: 16 | **Files read**: 0 | **Files written**: 0

## Call Relationships
**This routine calls:**

- [[output_landscape_init.f90]]
- [[header_channel.f90]]
- [[header_aquifer.f90]]
- [[header_sd_channel.f90]]
- [[header_mgt.f90]]
- [[header_lu_change.f90]]
- [[header_yield.f90]]
- [[header_hyd.f90]]
- [[header_reservoir.f90]]
- [[header_wetland.f90]]
- [[header_water_allocation.f90]]
- [[header_pest.f90]]
- [[header_path.f90]]
- [[header_salt.f90]]
- [[header_const.f90]]
- [[header_write.f90]]

**Called by** (live Dataview back-query):

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
