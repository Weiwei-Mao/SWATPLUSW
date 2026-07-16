---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: ch_rchinit.f90
note_file: ch_rchinit.f90
subroutine: ch_rchinit
module:
  - channel_module
  - hydrograph_module
calls: []
uses_variables:
  - channel_module.f90#ch
  - channel_module.f90#peakr
  - channel_module.f90#rch_cla
  - channel_module.f90#rch_gra
  - channel_module.f90#rch_lag
  - channel_module.f90#rch_sag
  - channel_module.f90#rch_san
  - channel_module.f90#rch_sil
  - channel_module.f90#rcharea
  - channel_module.f90#rchdep
  - channel_module.f90#rtevp
  - channel_module.f90#rttime
  - channel_module.f90#rttlc
  - channel_module.f90#rtwtr
  - channel_module.f90#sdti
  - channel_module.f90#sedrch
  - hydrograph_module.f90#jrch
input_variables: []
reads: []
writes: []
purpose: "this subroutine initializes variables for the daily simulation of the; channel routing command loop"
---

# ch_rchinit

> [!info] Summary
> this subroutine initializes variables for the daily simulation of the; channel routing command loop

## Basic Information
- **Type**: `subroutine`
- **Source file**: `ch_rchinit.f90`
- **Modules used**:
  - [[channel_module.f90]]
  - [[hydrograph_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 0 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by:**

(No static callers detected.)

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[channel_module.f90#ch]] - `channel`
- [[channel_module.f90#peakr]] - `real`
- [[channel_module.f90#rch_cla]] - `real`
- [[channel_module.f90#rch_gra]] - `real`
- [[channel_module.f90#rch_lag]] - `real`
- [[channel_module.f90#rch_sag]] - `real`
- [[channel_module.f90#rch_san]] - `real`
- [[channel_module.f90#rch_sil]] - `real`
- [[channel_module.f90#rcharea]] - `real`
- [[channel_module.f90#rchdep]] - `real`
- [[channel_module.f90#rtevp]] - `real`
- [[channel_module.f90#rttime]] - `real`
- [[channel_module.f90#rttlc]] - `real`
- [[channel_module.f90#rtwtr]] - `real`
- [[channel_module.f90#sdti]] - `real`
- [[channel_module.f90#sedrch]] - `real`
- [[hydrograph_module.f90#jrch]] - `integer`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
