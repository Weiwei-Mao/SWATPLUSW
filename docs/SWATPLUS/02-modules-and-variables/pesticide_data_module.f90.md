---
type: module
tags:
  - swat/module
  - swat/to-read
file: pesticide_data_module.f90
note_file: pesticide_data_module.f90
module_name: pesticide_data_module
defines_types:
  - pesticide_db
  - daughter_decay_fractions
  - pesticide_cp
defines_vars:
  - pestdb
  - pestcp
defines_subroutines: []
defines_functions: []
defines_procedures: []
purpose: ""
---

# pesticide_data_module

> [!info] Module
> Defines derived types and module-level variables.

## Defined Types
### pesticide_db

- **Defined in source**: `pesticide_data_module.f90:5`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `name` | `character(len=16)` | 6 | \|pesticide name |
| `koc` | `real` | 7 | (mL/g) \|soil adsorption coeff normalized for soil org carbon content |
| `washoff` | `real` | 8 | none \|frac of pesticide on foliage which is washed off by rainfall event |
| `foliar_hlife` | `real` | 9 | days \|half-life of pest on foliage |
| `soil_hlife` | `real` | 10 | days \|half-life of pest in soil |
| `solub` | `real` | 11 | mg/L (ppm) \|solubility of chemical in water |
| `aq_hlife` | `real` | 12 | days \|aquatic half-life |
| `aq_volat` | `real` | 13 | m/day \|aquatic volatilization coeff |
| `mol_wt` | `real` | 14 | g/mol \|molecular weight - to calculate mixing velocity |
| `aq_resus` | `real` | 15 | m/day \|aquatic resuspension velocity for pesticide sorbed to sediment |
| `aq_settle` | `real` | 16 | m/day \|aquatic settling velocity for pesticide sorbed to sediment |
| `ben_act_dep` | `real` | 17 | m \|depth of active benthic layer |
| `ben_bury` | `real` | 18 | m/day \|burial velocity in benthic sediment |
| `ben_hlife` | `real` | 19 | days \|half-life of pest in benthic sediment |
| `pl_uptake` | `real` | 20 | none \|fraction taken up by plant |
| `descrip` | `character(len=32)` | 21 | pesticide description |

### daughter_decay_fractions

- **Defined in source**: `pesticide_data_module.f90:25`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `name` | `character(len=16)` | 26 | daughter pesticide name |
| `num` | `integer` | 27 | sequential pesticide number in simulation |
| `foliar_fr` | `real` | 28 | 0-1 \|fraction of parent foilar degrading to daughter |
| `soil_fr` | `real` | 29 | 0-1 \|fraction of parent soil degrading to daughter |
| `aq_fr` | `real` | 30 | 0-1 \|fraction of parent aquatic degrading to daughter |
| `ben_fr` | `real` | 31 | 0-1 \|fraction of parent benthic degrading to daughter |

### pesticide_cp

- **Defined in source**: `pesticide_data_module.f90:34`
- **Source note**: calculated parameters from input parms

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `num_metab` | `integer` | 35 | number of metabolites |
| `daughter` | `daughter_decay_fractions` | 36 |  |
| `decay_f` | `real` | 37 | none \|exp of the rate const for degradation of the pest on foliage |
| `decay_s` | `real` | 38 | none \|exp of the rate const for degradation of the pest in soil |
| `decay_a` | `real` | 39 | none \|exp of the rate const for degradation of the pest in aquatic |
| `decay_b` | `real` | 40 | none \|exp of the rate const for degradation of the pest in benthic layer |

## Variables Defined
### pestdb

- **Type**: `pesticide_db`
- **Defined in source**: `pesticide_data_module.f90:23`

### pestcp

- **Type**: `pesticide_cp`
- **Defined in source**: `pesticide_data_module.f90:42`

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
