---
type: module
tags:
  - swat/module
  - swat/to-read
file: salt_data_module.f90
note_file: salt_data_module.f90
module_name: salt_data_module
defines_types: []
defines_vars:
  - salt_tol_sim
  - salt_soil_type
  - salt_effect
  - salt_tds_ec
  - salt_stress_a
  - salt_stress_b
  - Sul_Conc
  - Cal_Conc
  - Mg_Conc
  - Sod_Conc
  - Pot_Conc
  - Cl_Conc
  - Car_Conc
  - BiCar_Conc
  - c11
  - c22
  - salt_c3
  - salt_c4
  - c5
  - salt_K1
  - salt_K2
  - salt_K3
  - salt_K4
  - salt_K5
  - Ksp11
  - Ksp21
  - Ksp31
  - Ksp41
  - Ksp51
  - Ksp12
  - Ksp22
  - Ksp32
  - Ksp42
  - Ksp52
  - upion1
  - upion2
  - upion3
  - upion4
  - upion5
  - upion6
  - upion7
  - upion8
  - Sol_CaCO3
  - Sol_MgCO3
  - Sol_CaSO4
  - Sol_MgSO4
  - Sol_NaCl
  - LAMDA
  - soil_salt_conc
defines_subroutines: []
defines_functions: []
defines_procedures: []
purpose: ""
---

# salt_data_module

> [!info] Module
> Defines derived types and module-level variables.

## Defined Types
(No type definitions detected.)

## Variables Defined
### salt_tol_sim

- **Type**: `integer`
- **Defined in source**: `salt_data_module.f90:5`
- **Source note**: |flag to simulate salt effect on plant growth

### salt_soil_type

- **Type**: `integer`
- **Defined in source**: `salt_data_module.f90:6`
- **Source note**: |soil type (1 = CaSO4 soils; 2 = NaCl soils)

### salt_effect

- **Type**: `integer`
- **Defined in source**: `salt_data_module.f90:7`
- **Source note**: |1 = applied after other stresses; 2 = included with other stresses (min)

### salt_tds_ec

- **Type**: `real`
- **Defined in source**: `salt_data_module.f90:8`
- **Source note**: |total dissolved solids to electrical conductivity conversion factor

### salt_stress_a

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `salt_data_module.f90:9`
- **Source note**: |a and b parameters in salinity relative yield equations

### salt_stress_b

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `salt_data_module.f90:10`
- **Source note**: |a and b parameters in salinity relative yield equations

### Sul_Conc

- **Type**: `double precision`
- **Defined in source**: `salt_data_module.f90:12`

### Cal_Conc

- **Type**: `double precision`
- **Defined in source**: `salt_data_module.f90:12`

### Mg_Conc

- **Type**: `double precision`
- **Defined in source**: `salt_data_module.f90:12`

### Sod_Conc

- **Type**: `double precision`
- **Defined in source**: `salt_data_module.f90:13`

### Pot_Conc

- **Type**: `double precision`
- **Defined in source**: `salt_data_module.f90:13`

### Cl_Conc

- **Type**: `double precision`
- **Defined in source**: `salt_data_module.f90:13`

### Car_Conc

- **Type**: `double precision`
- **Defined in source**: `salt_data_module.f90:14`

### BiCar_Conc

- **Type**: `double precision`
- **Defined in source**: `salt_data_module.f90:14`

### c11

- **Type**: `integer`
- **Defined in source**: `salt_data_module.f90:15`

### c22

- **Type**: `integer`
- **Defined in source**: `salt_data_module.f90:16`

### salt_c3

- **Type**: `integer`
- **Defined in source**: `salt_data_module.f90:17`

### salt_c4

- **Type**: `integer`
- **Defined in source**: `salt_data_module.f90:18`

### c5

- **Type**: `integer`
- **Defined in source**: `salt_data_module.f90:19`

### salt_K1

- **Type**: `double precision`
- **Defined in source**: `salt_data_module.f90:20`

### salt_K2

- **Type**: `double precision`
- **Defined in source**: `salt_data_module.f90:20`

### salt_K3

- **Type**: `double precision`
- **Defined in source**: `salt_data_module.f90:20`

### salt_K4

- **Type**: `double precision`
- **Defined in source**: `salt_data_module.f90:20`

### salt_K5

- **Type**: `double precision`
- **Defined in source**: `salt_data_module.f90:20`

### Ksp11

- **Type**: `double precision`
- **Defined in source**: `salt_data_module.f90:22`

### Ksp21

- **Type**: `double precision`
- **Defined in source**: `salt_data_module.f90:23`

### Ksp31

- **Type**: `double precision`
- **Defined in source**: `salt_data_module.f90:24`

### Ksp41

- **Type**: `double precision`
- **Defined in source**: `salt_data_module.f90:25`

### Ksp51

- **Type**: `double precision`
- **Defined in source**: `salt_data_module.f90:26`

### Ksp12

- **Type**: `double precision`
- **Defined in source**: `salt_data_module.f90:28`

### Ksp22

- **Type**: `double precision`
- **Defined in source**: `salt_data_module.f90:29`

### Ksp32

- **Type**: `double precision`
- **Defined in source**: `salt_data_module.f90:30`

### Ksp42

- **Type**: `double precision`
- **Defined in source**: `salt_data_module.f90:31`

### Ksp52

- **Type**: `double precision`
- **Defined in source**: `salt_data_module.f90:32`

### upion1

- **Type**: `double precision`
- **Defined in source**: `salt_data_module.f90:33`

### upion2

- **Type**: `double precision`
- **Defined in source**: `salt_data_module.f90:33`

### upion3

- **Type**: `double precision`
- **Defined in source**: `salt_data_module.f90:33`

### upion4

- **Type**: `double precision`
- **Defined in source**: `salt_data_module.f90:33`

### upion5

- **Type**: `double precision`
- **Defined in source**: `salt_data_module.f90:33`

### upion6

- **Type**: `double precision`
- **Defined in source**: `salt_data_module.f90:33`

### upion7

- **Type**: `double precision`
- **Defined in source**: `salt_data_module.f90:33`

### upion8

- **Type**: `double precision`
- **Defined in source**: `salt_data_module.f90:33`

### Sol_CaCO3

- **Type**: `double precision`
- **Defined in source**: `salt_data_module.f90:34`

### Sol_MgCO3

- **Type**: `double precision`
- **Defined in source**: `salt_data_module.f90:34`

### Sol_CaSO4

- **Type**: `double precision`
- **Defined in source**: `salt_data_module.f90:34`

### Sol_MgSO4

- **Type**: `double precision`
- **Defined in source**: `salt_data_module.f90:34`

### Sol_NaCl

- **Type**: `double precision`
- **Defined in source**: `salt_data_module.f90:34`

### LAMDA

- **Type**: `double precision`
- **Defined in source**: `salt_data_module.f90:35`

### soil_salt_conc

- **Type**: `real`
- **Defined in source**: `salt_data_module.f90:37`
- **Source note**: generic array to hold salt ion concentrations

## Subroutines Defined
(No subroutines detected.)

## Functions Defined
(No functions detected.)

## Used By Source Routines

```dataview
LIST file.link
WHERE type = "source" AND contains(module, this.module_name)
```

<!-- USER-NOTES-START -->
## Notes
Use this section for type and variable meanings, units, and allowed values. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
