---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: salt_chem_hru.f90
note_file: salt_chem_hru.f90
subroutine: salt_chem_hru
module:
  - hru_module
  - basin_module
  - constituent_mass_module
  - salt_data_module
  - soil_module
  - salt_module
  - time_module
  - organic_mineral_mass_module
calls:
  - ionic_strength
  - activity_coefficient
  - caco3
  - mgco3
  - caso4
  - mgso4
  - nacl
  - cationexchange
reads: []
writes: []
purpose: "this subroutine calculates salt ion concentrations based on equilibrium chemical reactions, for an HRU; (precipitation-dissolution, complexation, cation exchange)"
---

# salt_chem_hru

> [!info] Summary
> this subroutine calculates salt ion concentrations based on equilibrium chemical reactions, for an HRU; (precipitation-dissolution, complexation, cation exchange)

## Basic Information
- **Type**: `subroutine`
- **Source file**: `salt_chem_hru.f90`
- **Modules used**: [[hru_module.f90]], [[basin_module.f90]], [[constituent_mass_module.f90]], [[salt_data_module.f90]], [[soil_module.f90]], [[salt_module.f90]], [[time_module.f90]], [[organic_mineral_mass_module.f90]]
- **Subroutine calls**: 8 | **Files read**: 0 | **Files written**: 0

## Call Relationships
**This routine calls:**

- `ionic_strength`
- `activity_coefficient`
- `caco3`
- `mgco3`
- `caso4`
- `mgso4`
- `nacl`
- `cationexchange`

**Called by** (live Dataview back-query):

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
