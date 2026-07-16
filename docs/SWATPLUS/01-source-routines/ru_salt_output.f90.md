---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: ru_salt_output.f90
note_file: ru_salt_output.f90
subroutine: ru_salt_output
module:
  - time_module
  - basin_module
  - hydrograph_module
  - salt_module
  - constituent_mass_module
calls: []
uses_variables:
  - basin_module.f90#pco
  - constituent_mass_module.f90#cs_db
  - constituent_mass_module.f90#rusaltb_a
  - constituent_mass_module.f90#rusaltb_d
  - constituent_mass_module.f90#rusaltb_m
  - constituent_mass_module.f90#rusaltb_y
  - hydrograph_module.f90#hd
  - hydrograph_module.f90#ob
  - hydrograph_module.f90#sp_ob1
  - salt_module.f90#ru_hru_saltb_a
  - salt_module.f90#ru_hru_saltb_d
  - salt_module.f90#ru_hru_saltb_m
  - salt_module.f90#ru_hru_saltb_y
  - time_module.f90#time
input_variables: []
reads: []
writes: []
purpose: "this subroutine outputs salt mass loadings and concentrations from routing units"
---

# ru_salt_output

> [!info] Summary
> this subroutine outputs salt mass loadings and concentrations from routing units

## Basic Information
- **Type**: `subroutine`
- **Source file**: `ru_salt_output.f90`
- **Modules used**:
  - [[time_module.f90]]
  - [[basin_module.f90]]
  - [[hydrograph_module.f90]]
  - [[salt_module.f90]]
  - [[constituent_mass_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 0 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by:**

- [[command.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[basin_module.f90#pco]] - `basin_print_codes`
- [[constituent_mass_module.f90#cs_db]] - `constituents`
- [[constituent_mass_module.f90#rusaltb_a]] - `all_constituent_hydrograph`
- [[constituent_mass_module.f90#rusaltb_d]] - `all_constituent_hydrograph`
- [[constituent_mass_module.f90#rusaltb_m]] - `all_constituent_hydrograph`
- [[constituent_mass_module.f90#rusaltb_y]] - `all_constituent_hydrograph`
- [[hydrograph_module.f90#hd]] - `hyd_output`
- [[hydrograph_module.f90#ob]] - `object_connectivity`
- [[hydrograph_module.f90#sp_ob1]] - `spatial_objects`
- [[salt_module.f90#ru_hru_saltb_a]] - `object_salt_balance`
- [[salt_module.f90#ru_hru_saltb_d]] - `object_salt_balance`
- [[salt_module.f90#ru_hru_saltb_m]] - `object_salt_balance`
- [[salt_module.f90#ru_hru_saltb_y]] - `object_salt_balance`
- [[time_module.f90#time]] - `time_current`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
