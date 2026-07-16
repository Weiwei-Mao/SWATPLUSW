---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: pl_waterup.f90
note_file: pl_waterup.f90
subroutine: pl_waterup
module:
  - plant_data_module
  - basin_module
  - hru_module
  - soil_module
  - plant_module
  - urban_data_module
  - constituent_mass_module
  - salt_data_module
calls:
  - salt_chem_soil_single
reads: []
writes: []
purpose: "this subroutine distributes potential plant evaporation through; the root zone and calculates actual plant water use based on soil; water availability. Also estimates water stress factor."
---

# pl_waterup

> [!info] Summary
> this subroutine distributes potential plant evaporation through; the root zone and calculates actual plant water use based on soil; water availability. Also estimates water stress factor.

## Basic Information
- **Type**: `subroutine`
- **Source file**: `pl_waterup.f90`
- **Modules used**: [[plant_data_module.f90]], [[basin_module.f90]], [[hru_module.f90]], [[soil_module.f90]], [[plant_module.f90]], [[urban_data_module.f90]], [[constituent_mass_module.f90]], [[salt_data_module.f90]]
- **Subroutine calls**: 1 | **Files read**: 0 | **Files written**: 0

## Call Relationships
**This routine calls:**

- [[salt_chem_soil_single.f90]]

**Called by** (live Dataview back-query):

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
