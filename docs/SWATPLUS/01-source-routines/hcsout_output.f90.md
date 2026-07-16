---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: hcsout_output.f90
note_file: hcsout_output.f90
subroutine: hcsout_output
module:
  - hydrograph_module
  - time_module
  - constituent_mass_module
calls: []
uses_variables:
  - constituent_mass_module.f90#cs_db
  - constituent_mass_module.f90#hcs1
  - constituent_mass_module.f90#obcs
  - hydrograph_module.f90#ob
  - hydrograph_module.f90#sp_ob
  - time_module.f90#time
input_variables: []
reads: []
writes: []
purpose: ""
---

# hcsout_output

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `hcsout_output.f90`
- **Modules used**:
  - [[hydrograph_module.f90]]
  - [[time_module.f90]]
  - [[constituent_mass_module.f90]]
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
- [[constituent_mass_module.f90#cs_db]] - `constituents`
- [[constituent_mass_module.f90#hcs1]] - `constituent_mass`
- [[constituent_mass_module.f90#obcs]] - `all_constituent_hydrograph`
- [[hydrograph_module.f90#ob]] - `object_connectivity`
- [[hydrograph_module.f90#sp_ob]] - `spatial_objects`
- [[time_module.f90#time]] - `time_current`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
