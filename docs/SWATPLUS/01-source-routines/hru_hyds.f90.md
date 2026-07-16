---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: hru_hyds.f90
note_file: hru_hyds.f90
subroutine: hru_hyds
module:
  - hru_module
  - hydrograph_module
  - basin_module
  - time_module
  - constituent_mass_module
  - output_landscape_module
  - output_ls_pesticide_module
  - climate_module
calls:
  - flow_hyd_ru_hru
reads: []
writes: []
purpose: "this subroutine summarizes data for subbasins with multiple HRUs and; prints the daily output.hru file"
---

# hru_hyds

> [!info] Summary
> this subroutine summarizes data for subbasins with multiple HRUs and; prints the daily output.hru file

## Basic Information
- **Type**: `subroutine`
- **Source file**: `hru_hyds.f90`
- **Modules used**: [[hru_module.f90]], [[hydrograph_module.f90]], [[basin_module.f90]], [[time_module.f90]], [[constituent_mass_module.f90]], [[output_landscape_module.f90]], [[output_ls_pesticide_module.f90]], [[climate_module.f90]]
- **Subroutine calls**: 1 | **Files read**: 0 | **Files written**: 0

## Call Relationships
**This routine calls:**

- [[flow_hyd_ru_hru.f90]]

**Called by** (live Dataview back-query):

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
