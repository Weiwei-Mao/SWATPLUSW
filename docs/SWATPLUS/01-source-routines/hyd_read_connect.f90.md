---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: hyd_read_connect.f90
note_file: hyd_read_connect.f90
subroutine: hyd_read_connect
module:
  - hydrograph_module
  - constituent_mass_module
  - time_module
  - climate_module
  - maximum_data_module
  - basin_module
calls:
  - search
reads:
  - con_file
writes: []
purpose: ""
---

# hyd_read_connect

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `hyd_read_connect.f90`
- **Modules used**: [[hydrograph_module.f90]], [[constituent_mass_module.f90]], [[time_module.f90]], [[climate_module.f90]], [[maximum_data_module.f90]], [[basin_module.f90]]
- **Subroutine calls**: 1 | **Files read**: 1 | **Files written**: 0

## Call Relationships
**This routine calls:**

- [[search.f90]]

**Called by** (live Dataview back-query):

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## File I/O
- **Reads**: `con_file` _(variable; see file.cio)_

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
