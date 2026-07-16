---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: aqu_1d_control.f90
note_file: aqu_1d_control.f90
subroutine: aqu_1d_control
module:
  - aquifer_module
  - time_module
  - hydrograph_module
  - climate_module
  - maximum_data_module
  - constituent_mass_module
  - pesticide_data_module
  - aqu_pesticide_module
  - salt_module
  - salt_aquifer
  - cs_aquifer
  - ch_pesticide_module
calls:
  - salt_chem_aqu
  - cs_rctn_aqu
  - cs_sorb_aqu
reads: []
writes: []
purpose: ""
---

# aqu_1d_control

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `aqu_1d_control.f90`
- **Modules used**: [[aquifer_module.f90]], [[time_module.f90]], [[hydrograph_module.f90]], [[climate_module.f90]], [[maximum_data_module.f90]], [[constituent_mass_module.f90]], [[pesticide_data_module.f90]], [[aqu_pesticide_module.f90]], [[salt_module.f90]], [[salt_aquifer.f90]], [[cs_aquifer.f90]], [[ch_pesticide_module.f90]]
- **Subroutine calls**: 3 | **Files read**: 0 | **Files written**: 0

## Call Relationships
**This routine calls:**

- [[salt_chem_aqu.f90]]
- [[cs_rctn_aqu.f90]]
- [[cs_sorb_aqu.f90]]

**Called by** (live Dataview back-query):

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
