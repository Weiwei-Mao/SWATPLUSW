---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: cs_rctn_aqu.f90
note_file: cs_rctn_aqu.f90
subroutine: cs_rctn_aqu
module:
  - hydrograph_module
  - aquifer_module
  - constituent_mass_module
  - cs_data_module
  - organic_mineral_mass_module
  - cs_module
  - cs_aquifer
calls:
  - se_reactions_aquifer
reads: []
writes: []
purpose: "this subroutine updates constituent concentrations based on chemical reactions in groundwater"
---

# cs_rctn_aqu

> [!info] Summary
> this subroutine updates constituent concentrations based on chemical reactions in groundwater

## Basic Information
- **Type**: `subroutine`
- **Source file**: `cs_rctn_aqu.f90`
- **Modules used**: [[hydrograph_module.f90]], [[aquifer_module.f90]], [[constituent_mass_module.f90]], [[cs_data_module.f90]], [[organic_mineral_mass_module.f90]], [[cs_module.f90]], [[cs_aquifer.f90]]
- **Subroutine calls**: 1 | **Files read**: 0 | **Files written**: 0

## Call Relationships
**This routine calls:**

- [[se_reactions_aquifer.f90]]

**Called by** (live Dataview back-query):

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
