---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: mgt_biomix.f90
note_file: mgt_biomix.f90
subroutine: mgt_biomix
module:
  - tillage_data_module
  - basin_module
  - organic_mineral_mass_module
  - soil_module
  - constituent_mass_module
  - plant_module
  - plant_data_module
  - hru_module
calls:
  - mgt_tillfactor
reads: []
writes: []
purpose: "this subroutine mixes residue and nutrients from biological mixing; New version developed by Armen R. Kemanian in collaboration with Stefan Julich and Cole Rossi; A subroutine to simulate stimulation of organic matter decomposition was added"
---

# mgt_biomix

> [!info] Summary
> this subroutine mixes residue and nutrients from biological mixing; New version developed by Armen R. Kemanian in collaboration with Stefan Julich and Cole Rossi; A subroutine to simulate stimulation of organic matter decomposition was added

## Basic Information
- **Type**: `subroutine`
- **Source file**: `mgt_biomix.f90`
- **Modules used**: [[tillage_data_module.f90]], [[basin_module.f90]], [[organic_mineral_mass_module.f90]], [[soil_module.f90]], [[constituent_mass_module.f90]], [[plant_module.f90]], [[plant_data_module.f90]], [[hru_module.f90]]
- **Subroutine calls**: 1 | **Files read**: 0 | **Files written**: 0

## Call Relationships
**This routine calls:**

- [[mgt_tillfactor.f90]]

**Called by** (live Dataview back-query):

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
