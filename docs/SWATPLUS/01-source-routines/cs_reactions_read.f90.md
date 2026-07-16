---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: cs_reactions_read.f90
note_file: cs_reactions_read.f90
subroutine: cs_reactions_read
module:
  - hydrograph_module
  - constituent_mass_module
  - cs_data_module
calls: []
uses_variables:
  - cs_data_module.f90#cs_rct_aqu
  - cs_data_module.f90#cs_rct_soil
  - cs_data_module.f90#num_geol_shale
  - cs_data_module.f90#rct
  - cs_data_module.f90#rct_shale
  - hydrograph_module.f90#aqu
  - hydrograph_module.f90#sp_ob
input_variables:
  - cs_data_module.f90#num_geol_shale
reads:
  - cs_reactions
writes: []
purpose: ""
---

# cs_reactions_read

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `cs_reactions_read.f90`
- **Modules used**:
  - [[hydrograph_module.f90]]
  - [[constituent_mass_module.f90]]
  - [[cs_data_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 1 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by:**

- [[proc_read.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[cs_data_module.f90#cs_rct_aqu]] - `constituent_rct`
- [[cs_data_module.f90#cs_rct_soil]] - `constituent_rct`
- [[cs_data_module.f90#num_geol_shale]] - `integer`
- [[cs_data_module.f90#rct]] - `real, dimension(:,:), allocatable`
- [[cs_data_module.f90#rct_shale]] - `real, dimension(:,:), allocatable`
- [[hydrograph_module.f90#aqu]] - `hyd_output`
- [[hydrograph_module.f90#sp_ob]] - `spatial_objects`

**Populated by file reads:**

- [[cs_data_module.f90#num_geol_shale]]

## File I/O
- **Reads**:
  - `cs_reactions` _(variable; see [[file.cio]])_

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
