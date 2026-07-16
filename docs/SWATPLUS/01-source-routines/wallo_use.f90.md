---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: wallo_use.f90
note_file: wallo_use.f90
subroutine: wallo_use
module:
  - water_allocation_module
  - hydrograph_module
  - constituent_mass_module
calls:
  - hyd_convert_conc_to_mass
  - hydcsout_conc_mass
uses_variables:
  - constituent_mass_module.f90#cs_db
  - constituent_mass_module.f90#outflo_cs
  - constituent_mass_module.f90#wuse_cs_efflu
  - hydrograph_module.f90#hz
  - hydrograph_module.f90#outflo_om
  - hydrograph_module.f90#wal_omd
  - hydrograph_module.f90#wal_use_omd
  - hydrograph_module.f90#wuse_om_efflu
  - hydrograph_module.f90#wuse_om_out
  - water_allocation_module.f90#wuse
input_variables: []
reads: []
writes: []
purpose: ""
---

# wallo_use

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `wallo_use.f90`
- **Modules used**:
  - [[water_allocation_module.f90]]
  - [[hydrograph_module.f90]]
  - [[constituent_mass_module.f90]]
- **Subroutine calls**: 2 | **Files read**: 0 | **Files written**: 0

## Call Relationships
**This routine calls:**

- [[hydrograph_module.f90#hyd_convert_conc_to_mass]]
- [[constituent_mass_module.f90#hydcsout_conc_mass]]

**Called by:**

- [[wallo_control.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[constituent_mass_module.f90#cs_db]] - `constituents`
- [[constituent_mass_module.f90#outflo_cs]] - `constituent_mass`
- [[constituent_mass_module.f90#wuse_cs_efflu]] - `constituent_mass`
- [[hydrograph_module.f90#hz]] - `hyd_output`
- [[hydrograph_module.f90#outflo_om]] - `hyd_output`
- [[hydrograph_module.f90#wal_omd]] - `water_allocation_object`
- [[hydrograph_module.f90#wal_use_omd]] - `hyd_output`
- [[hydrograph_module.f90#wuse_om_efflu]] - `hyd_output`
- [[hydrograph_module.f90#wuse_om_out]] - `hyd_output`
- [[water_allocation_module.f90#wuse]] - `water_treatment_use_data`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
