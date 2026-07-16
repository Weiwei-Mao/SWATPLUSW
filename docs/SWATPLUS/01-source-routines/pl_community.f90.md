---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: pl_community.f90
note_file: pl_community.f90
subroutine: pl_community
module:
  - hru_module
  - soil_module
  - plant_module
  - plant_data_module
  - organic_mineral_mass_module
  - time_module
  - climate_module
calls:
  - pl_waterup
reads: []
writes: []
purpose: "this subroutine predicts daily potential growth of total plant; biomass and roots and calculates leaf area index. Incorporates; residue for tillage functions and decays residue on ground"
---

# pl_community

> [!info] Summary
> this subroutine predicts daily potential growth of total plant; biomass and roots and calculates leaf area index. Incorporates; residue for tillage functions and decays residue on ground

## Basic Information
- **Type**: `subroutine`
- **Source file**: `pl_community.f90`
- **Modules used**: [[hru_module.f90]], [[soil_module.f90]], [[plant_module.f90]], [[plant_data_module.f90]], [[organic_mineral_mass_module.f90]], [[time_module.f90]], [[climate_module.f90]]
- **Subroutine calls**: 1 | **Files read**: 0 | **Files written**: 0

## Call Relationships
**This routine calls:**

- [[pl_waterup.f90]]

**Called by** (live Dataview back-query):

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
