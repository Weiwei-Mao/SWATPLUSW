---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: ru_control.f90
note_file: ru_control.f90
subroutine: ru_control
module:
  - hru_module
  - ru_module
  - hydrograph_module
  - time_module
  - constituent_mass_module
  - output_landscape_module
  - salt_module
  - cs_module
calls:
  - flow_hyd_ru_hru
reads: []
writes: []
purpose: ""
---

# ru_control

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `ru_control.f90`
- **Modules used**: [[hru_module.f90]], [[ru_module.f90]], [[hydrograph_module.f90]], [[time_module.f90]], [[constituent_mass_module.f90]], [[output_landscape_module.f90]], [[salt_module.f90]], [[cs_module.f90]]
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
