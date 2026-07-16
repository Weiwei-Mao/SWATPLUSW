---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: res_initial.f90
note_file: res_initial.f90
subroutine: res_initial
module:
  - reservoir_module
  - maximum_data_module
  - reservoir_data_module
  - hydrograph_module
  - constituent_mass_module
  - pesticide_data_module
  - water_body_module
  - res_salt_module
  - res_cs_module
calls:
  - res_convert_mass
reads: []
writes: []
purpose: ""
---

# res_initial

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `res_initial.f90`
- **Modules used**: [[reservoir_module.f90]], [[maximum_data_module.f90]], [[reservoir_data_module.f90]], [[hydrograph_module.f90]], [[constituent_mass_module.f90]], [[pesticide_data_module.f90]], [[water_body_module.f90]], [[res_salt_module.f90]], [[res_cs_module.f90]]
- **Subroutine calls**: 1 | **Files read**: 0 | **Files written**: 0

## Call Relationships
**This routine calls:**

- `res_convert_mass`

**Called by** (live Dataview back-query):

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
