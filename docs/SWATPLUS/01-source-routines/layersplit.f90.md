---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: layersplit.f90
note_file: layersplit.f90
subroutine: layersplit
module:
  - hru_module
  - soil_module
  - organic_mineral_mass_module
  - constituent_mass_module
calls: []
uses_variables:
  - hru_module.f90#ihru
  - soil_module.f90#layer1
  - soil_module.f90#phys1
  - soil_module.f90#soil
input_variables: []
reads: []
writes: []
purpose: ""
---

# layersplit

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `layersplit.f90`
- **Modules used**:
  - [[hru_module.f90]]
  - [[soil_module.f90]]
  - [[organic_mineral_mass_module.f90]]
  - [[constituent_mass_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 0 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by:**

- [[soils_init.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[hru_module.f90#ihru]] - `integer`
- [[soil_module.f90#layer1]] - `soilayer`
- [[soil_module.f90#phys1]] - `soil_physical_properties`
- [[soil_module.f90#soil]] - `soil_profile`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
