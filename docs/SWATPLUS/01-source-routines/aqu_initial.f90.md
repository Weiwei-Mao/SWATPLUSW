---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: aqu_initial.f90
note_file: aqu_initial.f90
subroutine: aqu_initial
module:
  - aquifer_module
  - hydrograph_module
  - constituent_mass_module
  - aqu_pesticide_module
  - salt_module
  - salt_aquifer
  - cs_module
  - cs_aquifer
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
  - aquifer_module.f90#aqu_a
  - aquifer_module.f90#aqu_d
  - aquifer_module.f90#aqu_dat
  - aquifer_module.f90#aqu_m
  - aquifer_module.f90#aqu_om_init
  - aquifer_module.f90#aqu_prm
  - aquifer_module.f90#aqu_y
  - aquifer_module.f90#aqudb
  - constituent_mass_module.f90#cs_aqu
  - constituent_mass_module.f90#cs_db
  - cs_aquifer.f90#acsb_a
  - cs_aquifer.f90#acsb_d
  - cs_aquifer.f90#acsb_m
  - cs_aquifer.f90#acsb_y
  - hydrograph_module.f90#aqu
  - hydrograph_module.f90#ob
  - hydrograph_module.f90#sp_ob
  - hydrograph_module.f90#sp_ob1
  - salt_aquifer.f90#asaltb_a
  - salt_aquifer.f90#asaltb_d
  - salt_aquifer.f90#asaltb_m
  - salt_aquifer.f90#asaltb_y
input_variables: []
reads: []
writes: []
purpose: ""
---

# aqu_initial

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `aqu_initial.f90`
- **Modules used**:
  - [[aquifer_module.f90]]
  - [[hydrograph_module.f90]]
  - [[constituent_mass_module.f90]]
  - [[aqu_pesticide_module.f90]]
  - [[salt_module.f90]]
  - [[salt_aquifer.f90]]
  - [[cs_module.f90]]
  - [[cs_aquifer.f90]]
- **Subroutine calls**: 0 | **Files read**: 0 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by:**

- [[proc_aqu.f90]]

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
- [[aquifer_module.f90#aqu_a]] - `aquifer_dynamic`
- [[aquifer_module.f90#aqu_d]] - `aquifer_dynamic`
- [[aquifer_module.f90#aqu_dat]] - `aquifer_database`
- [[aquifer_module.f90#aqu_m]] - `aquifer_dynamic`
- [[aquifer_module.f90#aqu_om_init]] - `aquifer_dynamic`
- [[aquifer_module.f90#aqu_prm]] - `aquifer_data_parameters`
- [[aquifer_module.f90#aqu_y]] - `aquifer_dynamic`
- [[aquifer_module.f90#aqudb]] - `aquifer_database`
- [[constituent_mass_module.f90#cs_aqu]] - `constituent_mass`
- [[constituent_mass_module.f90#cs_db]] - `constituents`
- [[cs_aquifer.f90#acsb_a]] - `object_cs_balance_aqu`
- [[cs_aquifer.f90#acsb_d]] - `object_cs_balance_aqu`
- [[cs_aquifer.f90#acsb_m]] - `object_cs_balance_aqu`
- [[cs_aquifer.f90#acsb_y]] - `object_cs_balance_aqu`
- [[hydrograph_module.f90#aqu]] - `hyd_output`
- [[hydrograph_module.f90#ob]] - `object_connectivity`
- [[hydrograph_module.f90#sp_ob]] - `spatial_objects`
- [[hydrograph_module.f90#sp_ob1]] - `spatial_objects`
- [[salt_aquifer.f90#asaltb_a]] - `object_salt_balance_aqu`
- [[salt_aquifer.f90#asaltb_d]] - `object_salt_balance_aqu`
- [[salt_aquifer.f90#asaltb_m]] - `object_salt_balance_aqu`
- [[salt_aquifer.f90#asaltb_y]] - `object_salt_balance_aqu`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
