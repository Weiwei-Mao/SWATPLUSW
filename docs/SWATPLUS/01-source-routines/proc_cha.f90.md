---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: proc_cha.f90
note_file: proc_cha.f90
subroutine: proc_cha
module:
  - hydrograph_module
calls:
  - ch_read_init
  - ch_read_init_cs
  - sd_hydsed_read
  - ch_read_hyd
  - ch_read_sed
  - ch_read_nut
  - ch_read
  - sd_channel_read
  - sd_hydsed_init
  - aqu2d_init
  - ch_ttcoef
  - ch_initial
  - overbank_read
  - sd_channel_surf_link
  - time_conc_init
uses_variables:
  - hydrograph_module.f90#ich
  - hydrograph_module.f90#ob
  - hydrograph_module.f90#sp_ob
  - hydrograph_module.f90#sp_ob1
input_variables: []
reads: []
writes: []
purpose: ""
---

# proc_cha

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `proc_cha.f90`
- **Modules used**:
  - [[hydrograph_module.f90]]
- **Subroutine calls**: 15 | **Files read**: 0 | **Files written**: 0

## Call Relationships
**This routine calls:**

- [[ch_read_init.f90]]
- [[ch_read_init_cs.f90]]
- [[sd_hydsed_read.f90]]
- [[ch_read_hyd.f90]]
- [[ch_read_sed.f90]]
- [[ch_read_nut.f90]]
- [[ch_read.f90]]
- [[sd_channel_read.f90]]
- [[sd_hydsed_init.f90]]
- [[aqu2d_init.f90]]
- [[ch_ttcoef.f90]]
- [[ch_initial.f90]]
- [[overbank_read.f90]]
- [[sd_channel_surf_link.f90]]
- [[time_conc_init.f90]]

**Called by:**

- [[main.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[hydrograph_module.f90#ich]] - `integer`
- [[hydrograph_module.f90#ob]] - `object_connectivity`
- [[hydrograph_module.f90#sp_ob]] - `spatial_objects`
- [[hydrograph_module.f90#sp_ob1]] - `spatial_objects`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
