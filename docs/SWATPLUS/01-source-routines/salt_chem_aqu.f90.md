---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: salt_chem_aqu.f90
note_file: salt_chem_aqu.f90
subroutine: salt_chem_aqu
module:
  - aquifer_module
  - basin_module
  - constituent_mass_module
  - salt_data_module
  - soil_module
  - hydrograph_module
  - salt_module
  - salt_aquifer
calls:
  - ionic_strength
  - activity_coefficient
  - caco3
  - mgco3
  - caso4
  - mgso4
  - nacl
  - cationexchange
uses_variables:
  - aquifer_module.f90#aqu_d
  - constituent_mass_module.f90#cs_aqu
  - constituent_mass_module.f90#cs_db
  - hydrograph_module.f90#icmd
  - hydrograph_module.f90#ob
  - salt_aquifer.f90#asaltb_d
  - salt_data_module.f90#BiCar_Conc
  - salt_data_module.f90#c11
  - salt_data_module.f90#c22
  - salt_data_module.f90#c5
  - salt_data_module.f90#Cal_Conc
  - salt_data_module.f90#Car_Conc
  - salt_data_module.f90#Cl_Conc
  - salt_data_module.f90#Ksp12
  - salt_data_module.f90#Ksp22
  - salt_data_module.f90#Ksp32
  - salt_data_module.f90#Ksp42
  - salt_data_module.f90#Ksp52
  - salt_data_module.f90#LAMDA
  - salt_data_module.f90#Mg_Conc
  - salt_data_module.f90#Pot_Conc
  - salt_data_module.f90#salt_c3
  - salt_data_module.f90#salt_c4
  - salt_data_module.f90#salt_K1
  - salt_data_module.f90#salt_K2
  - salt_data_module.f90#salt_K3
  - salt_data_module.f90#salt_K4
  - salt_data_module.f90#salt_K5
  - salt_data_module.f90#Sod_Conc
  - salt_data_module.f90#Sol_CaCO3
  - salt_data_module.f90#Sol_CaSO4
  - salt_data_module.f90#Sol_MgCO3
  - salt_data_module.f90#Sol_MgSO4
  - salt_data_module.f90#Sol_NaCl
  - salt_data_module.f90#Sul_Conc
  - salt_data_module.f90#upion1
  - salt_data_module.f90#upion2
  - salt_data_module.f90#upion3
  - salt_data_module.f90#upion4
  - salt_data_module.f90#upion5
  - salt_data_module.f90#upion6
  - salt_data_module.f90#upion7
  - salt_data_module.f90#upion8
input_variables: []
reads: []
writes: []
purpose: "this subroutine calculates salt ion concentrations based on equilibrium chemical reactions, for an HRU; (precipitation-dissolution, complexation, cation exchange)"
---

# salt_chem_aqu

> [!info] Summary
> this subroutine calculates salt ion concentrations based on equilibrium chemical reactions, for an HRU; (precipitation-dissolution, complexation, cation exchange)

## Basic Information
- **Type**: `subroutine`
- **Source file**: `salt_chem_aqu.f90`
- **Modules used**:
  - [[aquifer_module.f90]]
  - [[basin_module.f90]]
  - [[constituent_mass_module.f90]]
  - [[salt_data_module.f90]]
  - [[soil_module.f90]]
  - [[hydrograph_module.f90]]
  - [[salt_module.f90]]
  - [[salt_aquifer.f90]]
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

**Called by:**

- [[aqu_1d_control.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[aquifer_module.f90#aqu_d]] - `aquifer_dynamic`
- [[constituent_mass_module.f90#cs_aqu]] - `constituent_mass`
- [[constituent_mass_module.f90#cs_db]] - `constituents`
- [[hydrograph_module.f90#icmd]] - `integer`
- [[hydrograph_module.f90#ob]] - `object_connectivity`
- [[salt_aquifer.f90#asaltb_d]] - `object_salt_balance_aqu`
- [[salt_data_module.f90#BiCar_Conc]] - `double precision`
- [[salt_data_module.f90#c11]] - `integer`
- [[salt_data_module.f90#c22]] - `integer`
- [[salt_data_module.f90#c5]] - `integer`
- [[salt_data_module.f90#Cal_Conc]] - `double precision`
- [[salt_data_module.f90#Car_Conc]] - `double precision`
- [[salt_data_module.f90#Cl_Conc]] - `double precision`
- [[salt_data_module.f90#Ksp12]] - `double precision`
- [[salt_data_module.f90#Ksp22]] - `double precision`
- [[salt_data_module.f90#Ksp32]] - `double precision`
- [[salt_data_module.f90#Ksp42]] - `double precision`
- [[salt_data_module.f90#Ksp52]] - `double precision`
- [[salt_data_module.f90#LAMDA]] - `double precision`
- [[salt_data_module.f90#Mg_Conc]] - `double precision`
- [[salt_data_module.f90#Pot_Conc]] - `double precision`
- [[salt_data_module.f90#salt_c3]] - `integer`
- [[salt_data_module.f90#salt_c4]] - `integer`
- [[salt_data_module.f90#salt_K1]] - `double precision`
- [[salt_data_module.f90#salt_K2]] - `double precision`
- [[salt_data_module.f90#salt_K3]] - `double precision`
- [[salt_data_module.f90#salt_K4]] - `double precision`
- [[salt_data_module.f90#salt_K5]] - `double precision`
- [[salt_data_module.f90#Sod_Conc]] - `double precision`
- [[salt_data_module.f90#Sol_CaCO3]] - `double precision`
- [[salt_data_module.f90#Sol_CaSO4]] - `double precision`
- [[salt_data_module.f90#Sol_MgCO3]] - `double precision`
- [[salt_data_module.f90#Sol_MgSO4]] - `double precision`
- [[salt_data_module.f90#Sol_NaCl]] - `double precision`
- [[salt_data_module.f90#Sul_Conc]] - `double precision`
- [[salt_data_module.f90#upion1]] - `double precision`
- [[salt_data_module.f90#upion2]] - `double precision`
- [[salt_data_module.f90#upion3]] - `double precision`
- [[salt_data_module.f90#upion4]] - `double precision`
- [[salt_data_module.f90#upion5]] - `double precision`
- [[salt_data_module.f90#upion6]] - `double precision`
- [[salt_data_module.f90#upion7]] - `double precision`
- [[salt_data_module.f90#upion8]] - `double precision`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
