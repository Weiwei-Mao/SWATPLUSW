---
type: module
tags:
  - swat/module
  - swat/to-read
file: urban_data_module.f90
note_file: urban_data_module.f90
module_name: urban_data_module
defines_types:
  - urban_db
defines_vars:
  - urbdb
defines_subroutines: []
defines_functions: []
defines_procedures: []
purpose: ""
---

# urban_data_module

> [!info] Module
> Defines derived types and module-level variables.

## Defined Types
### urban_db

- **Defined in source**: `urban_data_module.f90:5`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `urbnm` | `character(len=16)` | 6 |  |
| `fimp` | `real` | 7 | fraction \|fraction of HRU area that is imp |
| `fcimp` | `real` | 8 | fraction \|fraction of HRU that is classified as directly connected imp |
| `curbden` | `real` | 9 | km/ha \|curb length density |
| `urbcoef` | `real` | 10 | 1/mm \|wash-off coefficient for removal of constituents from an imp surface |
| `dirtmx` | `real` | 11 | kg/curb km \|max amt of solids allowed to build up on imp surfaces |
| `thalf` | `real` | 12 | days \|time for the amt of solids on imp areas to build up to 1/2 max level |
| `tnconc` | `real` | 13 | mg N/kg sed \|conc of total nitrogen in suspended solid load from imp areas |
| `tpconc` | `real` | 14 | mg P/kg sed \|conc of total phosphorus in suspened solid load from imp areas |
| `tno3conc` | `real` | 15 | mg NO3-N/kg sed \|conc of NO3-N in suspended solid load from imp areas |
| `urbcn2` | `real` | 16 | none \|moisture condition II curve number for imp areas |

## Variables Defined
### urbdb

- **Type**: `urban_db`
- **Defined in source**: `urban_data_module.f90:18`

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
