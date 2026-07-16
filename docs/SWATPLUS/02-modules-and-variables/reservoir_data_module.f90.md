---
type: module
tags:
  - swat/module
  - swat/to-read
file: reservoir_data_module.f90
note_file: reservoir_data_module.f90
module_name: reservoir_data_module
defines_types:
  - reservoir_data_char_input
  - reservoir_data_char_input_cs
  - reservoir_data
  - reservoir_init_data_char
  - reservoir_init_data
  - reservoir_hyd_data
  - wetland_hyd_data
  - reservoir_sed_data
  - reservoir_nut_data
  - water_body_data_parameters
  - reservoir_weir_outflow
defines_vars:
  - res_datz
  - sed
  - nut
  - name
  - init
  - hyd
  - release
  - sed
  - nut
  - pst
  - weir
  - salt
  - cs
  - org_min
  - pest
  - path
  - hmet
purpose: ""
---

# reservoir_data_module

> [!info] Module
> Defines derived types and module-level variables.

## Defined Types
| Type | Notes |
|---|---|
| `reservoir_data_char_input` |  |
| `reservoir_data_char_input_cs` |  |
| `reservoir_data` |  |
| `reservoir_init_data_char` |  |
| `reservoir_init_data` |  |
| `reservoir_hyd_data` |  |
| `wetland_hyd_data` |  |
| `reservoir_sed_data` |  |
| `reservoir_nut_data` |  |
| `water_body_data_parameters` |  |
| `reservoir_weir_outflow` |  |

## Module-Level Variables
| Variable | Type | Meaning |
|---|---|---|
| `res_datz` |  |  |
| `sed` |  |  |
| `nut` |  |  |
| `name` |  |  |
| `init` |  |  |
| `hyd` |  |  |
| `release` |  |  |
| `sed` |  |  |
| `nut` |  |  |
| `pst` |  |  |
| `weir` |  |  |
| `salt` |  |  |
| `cs` |  |  |
| `org_min` |  |  |
| `pest` |  |  |
| `path` |  |  |
| `hmet` |  |  |

## Used By Source Routines

```dataview
LIST file.link
WHERE type = "source" AND contains(module, this.module_name)
```

<!-- USER-NOTES-START -->
## Notes
Use this section for type and variable meanings, units, and allowed values. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
