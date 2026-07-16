---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: pl_nut_demand.f90
note_file: pl_nut_demand.f90
subroutine: pl_nut_demand
module:
  - hru_module
  - soil_module
  - plant_module
  - plant_data_module
  - organic_mineral_mass_module
  - climate_module
calls:
  - pl_nupd
  - pl_pupd
reads: []
writes: []
purpose: "this subroutine predicts daily potential growth of total plant; biomass and roots and calculates leaf area index. Incorporates; residue for tillage functions and decays residue on ground"
---

# pl_nut_demand

> [!info] Summary
> this subroutine predicts daily potential growth of total plant; biomass and roots and calculates leaf area index. Incorporates; residue for tillage functions and decays residue on ground

## Basic Information
- **Type**: `subroutine`
- **Source file**: `pl_nut_demand.f90`
- **Modules used**: [[hru_module.f90]], [[soil_module.f90]], [[plant_module.f90]], [[plant_data_module.f90]], [[organic_mineral_mass_module.f90]], [[climate_module.f90]]
- **Subroutine calls**: 2 | **Files read**: 0 | **Files written**: 0

## Call Relationships
**This routine calls:**

- [[pl_nupd.f90]]
- [[pl_pupd.f90]]

**Called by** (live Dataview back-query):

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
