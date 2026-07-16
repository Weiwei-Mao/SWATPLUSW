---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: ch_rtpest.f90
note_file: ch_rtpest.f90
subroutine: ch_rtpest
module:
  - channel_data_module
  - channel_module
  - sd_channel_module
  - ch_pesticide_module
  - hydrograph_module
  - constituent_mass_module
  - pesticide_data_module
calls: []
uses_variables:
  - ch_pesticide_module.f90#chpst
  - ch_pesticide_module.f90#chpst_d
  - ch_pesticide_module.f90#chpstz
  - ch_pesticide_module.f90#frsol
  - ch_pesticide_module.f90#frsrb
  - channel_module.f90#rttime
  - channel_module.f90#wtrin
  - constituent_mass_module.f90#ch_benthic
  - constituent_mass_module.f90#ch_water
  - constituent_mass_module.f90#cs_db
  - constituent_mass_module.f90#hcs1
  - constituent_mass_module.f90#hcs2
  - hydrograph_module.f90#ch_stor
  - hydrograph_module.f90#ht1
  - hydrograph_module.f90#ht2
  - hydrograph_module.f90#jrch
  - pesticide_data_module.f90#pestcp
  - pesticide_data_module.f90#pestdb
  - sd_channel_module.f90#rcurv
  - sd_channel_module.f90#sd_ch
input_variables: []
reads: []
writes: []
purpose: "this subroutine computes the daily stream pesticide balance; (soluble and sorbed)"
---

# ch_rtpest

> [!info] Summary
> this subroutine computes the daily stream pesticide balance; (soluble and sorbed)

## Basic Information
- **Type**: `subroutine`
- **Source file**: `ch_rtpest.f90`
- **Modules used**:
  - [[channel_data_module.f90]]
  - [[channel_module.f90]]
  - [[sd_channel_module.f90]]
  - [[ch_pesticide_module.f90]]
  - [[hydrograph_module.f90]]
  - [[constituent_mass_module.f90]]
  - [[pesticide_data_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 0 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by:**

- [[sd_channel_control3.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[ch_pesticide_module.f90#chpst]] - `ch_pesticide_output`
- [[ch_pesticide_module.f90#chpst_d]] - `ch_pesticide_output`
- [[ch_pesticide_module.f90#chpstz]] - `ch_pesticide_output`
- [[ch_pesticide_module.f90#frsol]] - `real`
- [[ch_pesticide_module.f90#frsrb]] - `real`
- [[channel_module.f90#rttime]] - `real`
- [[channel_module.f90#wtrin]] - `real`
- [[constituent_mass_module.f90#ch_benthic]] - `constituent_mass`
- [[constituent_mass_module.f90#ch_water]] - `constituent_mass`
- [[constituent_mass_module.f90#cs_db]] - `constituents`
- [[constituent_mass_module.f90#hcs1]] - `constituent_mass`
- [[constituent_mass_module.f90#hcs2]] - `constituent_mass`
- [[hydrograph_module.f90#ch_stor]] - `hyd_output`
- [[hydrograph_module.f90#ht1]] - `hyd_output`
- [[hydrograph_module.f90#ht2]] - `hyd_output`
- [[hydrograph_module.f90#jrch]] - `integer`
- [[pesticide_data_module.f90#pestcp]] - `pesticide_cp`
- [[pesticide_data_module.f90#pestdb]] - `pesticide_db`
- [[sd_channel_module.f90#rcurv]] - `channel_rating_curve_parameters`
- [[sd_channel_module.f90#sd_ch]] - `swatdeg_channel_dynamic`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
