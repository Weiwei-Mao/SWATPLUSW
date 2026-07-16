---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: cs_sorb_hru.f90
note_file: cs_sorb_hru.f90
subroutine: cs_sorb_hru
module:
  - hru_module
  - soil_module
  - organic_mineral_mass_module
  - constituent_mass_module
  - cs_module
  - cs_data_module
calls: []
reads: []
writes: []
purpose: "this subroutine updates constituent concentrations based on sorption in the soil profile"
---

# cs_sorb_hru

> [!info] Summary
> this subroutine updates constituent concentrations based on sorption in the soil profile

## Basic Information
- **Type**: `subroutine`
- **Source file**: `cs_sorb_hru.f90`
- **Modules used**: [[hru_module.f90]], [[soil_module.f90]], [[organic_mineral_mass_module.f90]], [[constituent_mass_module.f90]], [[cs_module.f90]], [[cs_data_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 0 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by** (live Dataview back-query):

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
