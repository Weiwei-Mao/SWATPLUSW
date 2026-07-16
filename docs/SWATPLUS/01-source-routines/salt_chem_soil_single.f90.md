---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: salt_chem_soil_single.f90
note_file: salt_chem_soil_single.f90
subroutine: salt_chem_soil_single
module:
  - basin_module
  - constituent_mass_module
  - salt_data_module
  - soil_module
  - salt_module
  - time_module
calls:
  - ionic_strength
  - activity_coefficient
  - caco3
  - mgco3
  - caso4
  - mgso4
  - nacl
reads: []
writes: []
purpose: "this subroutine calculates salt ion concentrations based on equilibrium chemical reactions; (precipitation-dissolution, complexation, cation exchange), for a specified HRU, for a specified layer"
---

# salt_chem_soil_single

> [!info] Summary
> this subroutine calculates salt ion concentrations based on equilibrium chemical reactions; (precipitation-dissolution, complexation, cation exchange), for a specified HRU, for a specified layer

## Basic Information
- **Type**: `subroutine`
- **Source file**: `salt_chem_soil_single.f90`
- **Modules used**: [[basin_module.f90]], [[constituent_mass_module.f90]], [[salt_data_module.f90]], [[soil_module.f90]], [[salt_module.f90]], [[time_module.f90]]
- **Subroutine calls**: 7 | **Files read**: 0 | **Files written**: 0

## Call Relationships
**This routine calls:**

- `ionic_strength`
- `activity_coefficient`
- `caco3`
- `mgco3`
- `caso4`
- `mgso4`
- `nacl`

**Called by** (live Dataview back-query):

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
