---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: aqu_pest_output_init.f90
note_file: aqu_pest_output_init.f90
subroutine: aqu_pest_output_init
module:
  - aqu_pesticide_module
  - constituent_mass_module
  - hydrograph_module
calls: []
uses_variables:
  - aqu_pesticide_module.f90#aqupst_a
  - aqu_pesticide_module.f90#aqupst_d
  - aqu_pesticide_module.f90#aqupst_m
  - aqu_pesticide_module.f90#aqupst_y
  - aqu_pesticide_module.f90#baqupst_a
  - aqu_pesticide_module.f90#baqupst_d
  - aqu_pesticide_module.f90#baqupst_m
  - aqu_pesticide_module.f90#baqupst_y
  - constituent_mass_module.f90#cs_aqu
  - constituent_mass_module.f90#cs_db
  - hydrograph_module.f90#aqu
  - hydrograph_module.f90#sp_ob
input_variables: []
reads: []
writes: []
purpose: ""
---

# aqu_pest_output_init

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `aqu_pest_output_init.f90`
- **Modules used**:
  - [[aqu_pesticide_module.f90]]
  - [[constituent_mass_module.f90]]
  - [[hydrograph_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 0 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by:**

- [[time_control.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[aqu_pesticide_module.f90#aqupst_a]] - `aqu_pesticide_output`
- [[aqu_pesticide_module.f90#aqupst_d]] - `aqu_pesticide_output`
- [[aqu_pesticide_module.f90#aqupst_m]] - `aqu_pesticide_output`
- [[aqu_pesticide_module.f90#aqupst_y]] - `aqu_pesticide_output`
- [[aqu_pesticide_module.f90#baqupst_a]] - `aqu_pesticide_output`
- [[aqu_pesticide_module.f90#baqupst_d]] - `aqu_pesticide_output`
- [[aqu_pesticide_module.f90#baqupst_m]] - `aqu_pesticide_output`
- [[aqu_pesticide_module.f90#baqupst_y]] - `aqu_pesticide_output`
- [[constituent_mass_module.f90#cs_aqu]] - `constituent_mass`
- [[constituent_mass_module.f90#cs_db]] - `constituents`
- [[hydrograph_module.f90#aqu]] - `hyd_output`
- [[hydrograph_module.f90#sp_ob]] - `spatial_objects`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
