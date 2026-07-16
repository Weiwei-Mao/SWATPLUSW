---
type: module
tags:
  - swat/module
  - swat/to-read
file: conditional_module.f90
note_file: conditional_module.f90
module_name: conditional_module
defines_types:
  - conditions_var
  - actions_var
  - decision_table
defines_vars:
  - dtbl_lum
  - dtbl_res
  - dtbl_scen
  - dtbl_flo
  - d_tbl
defines_subroutines: []
defines_functions: []
defines_procedures: []
purpose: ""
---

# conditional_module

> [!info] Module
> Defines derived types and module-level variables.

## Defined Types
### conditions_var

- **Defined in source**: `conditional_module.f90:7`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `var` | `character(len=25)` | 8 | condition variable (ie volume, flow, sw, time, etc) |
| `ob` | `character(len=25)` | 9 | object variable (ie res, hru, canal, etc) |
| `ob_num` | `integer` | 10 | object number |
| `lim_var` | `character(len=25)` | 11 | limit variable (ie evol, pvol, fc, ul, etc) |
| `lim_op` | `character(len=25)` | 12 | limit operator (*,+,-) |
| `lim_const` | `real` | 13 | limit constant |

### actions_var

- **Defined in source**: `conditional_module.f90:16`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `typ` | `character(len=25)` | 17 | type of action (ie reservoir release, irrigate, fertilize, etc) |
| `ob` | `character(len=25)` | 18 | object variable (ie res, hru, canal, etc) |
| `ob_num` | `integer` | 19 | object number |
| `name` | `character(len=25)` | 20 | name of action |
| `option` | `character(len=40)` | 21 | action option - specific to type of action (ie for reservoir, option to input rate, days of drawdown, weir equation pointer, etc |
| `const` | `real` | 23 | constant used for rate, days, etc |
| `const2` | `real` | 24 | additional constant used for rate, days, etc |
| `file_pointer` | `character(len=25)` | 25 | pointer for option (ie weir equation pointer) |

### decision_table

- **Defined in source**: `conditional_module.f90:28`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `name` | `character (len=40)` | 29 | name of the decision table |
| `conds` | `integer` | 30 | number of conditions |
| `alts` | `integer` | 31 | number of alternatives |
| `acts` | `integer` | 32 | number of actions |
| `cond` | `conditions_var` | 33 | conditions |
| `alt` | `character(len=25), dimension(:,:), allocatable` | 34 | condition alternatives |
| `act` | `actions_var` | 35 | actions |
| `lu_chg_mx` | `integer, dimension(:), allocatable` | 36 | max times lu change can occur |
| `snow_chg_mx` | `integer, dimension(:), allocatable` | 37 | max times snow change can occur |
| `act_outcomes` | `character(len=1), dimension(:,:), allocatable` | 38 | action outcomes ("y" to perform action; "n" to not perform) |
| `act_hit` | `character(len=1), dimension(:), allocatable` | 39 | "y" if all condition alternatives (rules) are met; "n" if not |
| `act_typ` | `integer, dimension(:), allocatable` | 40 | pointer to action type (ie plant, fert type, tillage implement, release type, etc) |
| `act_app` | `integer, dimension(:), allocatable` | 41 | pointer to operation or application type (ie harvest.ops, chem_app.ops, wier shape, etc) |
| `con_act` | `integer, dimension(:), allocatable` | 42 | pointer for days since last action condition to point to appropriate action |
| `hru_lu` | `integer` | 43 | number of hru's in the land_use condition(s) - used for probabilistic mgt operations or lu change |
| `ha_lu` | `real` | 44 | area of land_use in ha |
| `hru_lu_cur` | `integer` | 45 | number of hru's in the land_use condition(s) that have currently been applied |
| `hru_ha_cur` | `real` | 46 | area of land_use in ha that has currently been applied |
| `days_prob` | `integer` | 47 | days since start of application window |
| `day_prev` | `integer` | 48 | to check if same day - don't increment day in application window |
| `prob_cum` | `real` | 49 | cumulative probability of application on current day of window |
| `frac_app` | `real` | 50 | fraction of time (during each window) the application occurs |

## Variables Defined
### dtbl_lum

- **Type**: `decision_table`
- **Defined in source**: `conditional_module.f90:52`

### dtbl_res

- **Type**: `decision_table`
- **Defined in source**: `conditional_module.f90:53`

### dtbl_scen

- **Type**: `decision_table`
- **Defined in source**: `conditional_module.f90:54`

### dtbl_flo

- **Type**: `decision_table`
- **Defined in source**: `conditional_module.f90:55`

### d_tbl

- **Type**: `decision_table`
- **Defined in source**: `conditional_module.f90:56`

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
