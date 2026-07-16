---
type: module
tags:
  - swat/module
  - swat/to-read
file: fertilizer_data_module.f90
note_file: fertilizer_data_module.f90
module_name: fertilizer_data_module
defines_types:
  - fertilizer_db
  - manure_database
  - manure_attributes
defines_vars:
  - fertdb
  - manure_db
  - manure_om
defines_subroutines: []
defines_functions: []
defines_procedures: []
purpose: ""
---

# fertilizer_data_module

> [!info] Module
> Defines derived types and module-level variables.

## Defined Types
### fertilizer_db

- **Defined in source**: `fertilizer_data_module.f90:5`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `fertnm` | `character(len=16)` | 6 |  |
| `fminn` | `real` | 7 | kg minN/kg frt \|fract of fert which is mineral nit (NO3+NH3) |
| `fminp` | `real` | 8 | kg minN/kg frt \|frac of fert which is mineral phos |
| `forgn` | `real` | 9 | kg orgN/kg frt \|frac of fert which is org n |
| `forgp` | `real` | 10 | kg orgP/kg frt \|frac of fert which is org p |
| `fnh3n` | `real` | 11 | kg NH3-N/kg N \|frac of mineral N content of fert which is NH3 |

### manure_database

- **Defined in source**: `fertilizer_data_module.f90:16`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `name` | `character (len=25)` | 17 | name of manure type |
| `org_min` | `character (len=25)` | 18 | sediment, carbon, and nutrients |
| `pests` | `character (len=25)` | 19 | pesticides - ppm |
| `paths` | `character (len=25)` | 20 | pathogens - cfu |
| `hmets` | `character (len=25)` | 21 | heavy metals - ppm |
| `salts` | `character (len=25)` | 22 | salt ions - ppm |
| `constit` | `character (len=25)` | 23 | other constituents - ppm |
| `descrip` | `character (len=80)` | 24 | description |
| `iorg_min` | `integer` | 25 | sediment, carbon, and nutrients - pointer to |
| `ipests` | `integer` | 26 | pesticides - pointer to |
| `ipaths` | `integer` | 27 | pathogens - pointer to |
| `imets` | `integer` | 28 | heavy metals - pointer to |
| `isalts` | `integer` | 29 | salt ions - pointer to |
| `iconstit` | `integer` | 30 | other constituents - pointer to |

### manure_attributes

- **Defined in source**: `fertilizer_data_module.f90:35`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `name` | `character(len=64)` | 36 | Identifier used to crosswalk fertilizer entries, constructed from manure_region, manure_source, and manure_type |
| `frac_water` | `real` | 38 | kg water/(kg manure + kg_water) \|frac of manure which is water |
| `fcbn` | `real` | 39 | kg C/kg frt \|frac of fert which is carbon |
| `fminn` | `real` | 40 | kg minN/kg frt \|frac of fert which is mineral nitrogen (NO3+NH3) |
| `fminp` | `real` | 41 | kg minN/kg frt \|frac of fert which is mineral phoshorus |
| `forgn` | `real` | 42 | kg orgN/kg frt \|frac of fert which is org N |
| `forgp` | `real` | 43 | kg orgP/kg frt \|frac of fert which is org P |
| `fnh3n` | `real` | 44 | kg NH3-N/kg N \|frac of mineral N content of fert which is NH3 |
| `description` | `character(len=64)` | 45 | na \|description of manure type |

## Variables Defined
### fertdb

- **Type**: `fertilizer_db`
- **Defined in source**: `fertilizer_data_module.f90:13`

### manure_db

- **Type**: `manure_database`
- **Defined in source**: `fertilizer_data_module.f90:32`

### manure_om

- **Type**: `manure_attributes`
- **Defined in source**: `fertilizer_data_module.f90:47`

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
