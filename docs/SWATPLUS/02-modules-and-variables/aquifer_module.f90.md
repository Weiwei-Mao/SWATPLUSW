---
type: module
tags:
  - swat/module
  - swat/to-read
file: aquifer_module.f90
note_file: aquifer_module.f90
module_name: aquifer_module
defines_types:
  - aquifer_database
  - aquifer_data_parameters
  - aquifer_dynamic
  - aquifer_init_data_char
  - aquifer_init_data_char_cs
  - aquifer_init_data
  - aqu_header
  - aqu_header_units
defines_vars:
  - baqu_d
  - baqu_m
  - baqu_y
  - baqu_a
  - aquz
  - aqu_hdr
  - aqu_hdr_units
  - aqunm
  - aqu_ini
  - name
  - org_min
  - pest
  - path
  - hmet
  - salt
  - cs
  - day
  - mo
  - day_mo
  - yrc
  - isd
  - id
  - flo
  - dep_wt
  - stor
  - rchrg
  - seep
  - revap
  - no3_st
  - minp
  - orgn
  - orgp
  - no3_rchg
  - no3_loss
  - no3_lat
  - no3_seep
  - flo_cha
  - flo_res
  - flo_ls
  - depwt
purpose: ""
---

# aquifer_module

> [!info] Module
> Defines derived types and module-level variables.

## Defined Types
| Type | Notes |
|---|---|
| `aquifer_database` |  |
| `aquifer_data_parameters` |  |
| `aquifer_dynamic` |  |
| `aquifer_init_data_char` |  |
| `aquifer_init_data_char_cs` |  |
| `aquifer_init_data` |  |
| `aqu_header` |  |
| `aqu_header_units` |  |

## Module-Level Variables
| Variable | Type | Meaning |
|---|---|---|
| `baqu_d` |  |  |
| `baqu_m` |  |  |
| `baqu_y` |  |  |
| `baqu_a` |  |  |
| `aquz` |  |  |
| `aqu_hdr` |  |  |
| `aqu_hdr_units` |  |  |
| `aqunm` |  |  |
| `aqu_ini` |  |  |
| `name` |  |  |
| `org_min` |  |  |
| `pest` |  |  |
| `path` |  |  |
| `hmet` |  |  |
| `salt` |  |  |
| `cs` |  |  |
| `day` |  |  |
| `mo` |  |  |
| `day_mo` |  |  |
| `yrc` |  |  |
| `isd` |  |  |
| `id` |  |  |
| `flo` |  |  |
| `dep_wt` |  |  |
| `stor` |  |  |
| `rchrg` |  |  |
| `seep` |  |  |
| `revap` |  |  |
| `no3_st` |  |  |
| `minp` |  |  |
| `orgn` |  |  |
| `orgp` |  |  |
| `no3_rchg` |  |  |
| `no3_loss` |  |  |
| `no3_lat` |  |  |
| `no3_seep` |  |  |
| `flo_cha` |  |  |
| `flo_res` |  |  |
| `flo_ls` |  |  |
| `depwt` |  |  |

## Used By Source Routines

```dataview
LIST file.link
WHERE type = "source" AND contains(module, this.module_name)
```

<!-- USER-NOTES-START -->
## Notes
Use this section for type and variable meanings, units, and allowed values. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
