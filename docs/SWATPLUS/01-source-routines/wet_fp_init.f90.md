---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: wet_fp_init.f90
note_file: wet_fp_init.f90
subroutine: wet_fp_init
module:
  - sd_channel_module
  - hydrograph_module
calls: []
reads: []
writes: []
purpose: "this subroutine routes computes the initial storage in flood plain wetlands"
---

# wet_fp_init

> [!info] Summary
> this subroutine routes computes the initial storage in flood plain wetlands

## Basic Information
- **Type**: `subroutine`
- **Source file**: `wet_fp_init.f90`
- **Modules used**: [[sd_channel_module.f90]], [[hydrograph_module.f90]]
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
