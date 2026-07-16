---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: wallo_treatment.f90
note_file: wallo_treatment.f90
subroutine: wallo_treatment
module:
  - water_allocation_module
  - hydrograph_module
  - constituent_mass_module
calls:
  - hyd_convert_conc_to_mass
  - hyd_min
  - hydcsout_conc_mass
reads: []
writes: []
purpose: ""
---

# wallo_treatment

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `wallo_treatment.f90`
- **Modules used**: [[water_allocation_module.f90]], [[hydrograph_module.f90]], [[constituent_mass_module.f90]]
- **Subroutine calls**: 3 | **Files read**: 0 | **Files written**: 0

## Call Relationships
**This routine calls:**

- `hyd_convert_conc_to_mass`
- `hyd_min`
- `hydcsout_conc_mass`

**Called by** (live Dataview back-query):

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
