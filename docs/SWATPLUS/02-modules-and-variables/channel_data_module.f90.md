---
type: module
tags:
  - swat/module
  - swat/to-read
file: channel_data_module.f90
note_file: channel_data_module.f90
module_name: channel_data_module
defines_types:
  - routing_nut_data
  - channel_data_char_input
  - channel_init_datafiles
  - channel_init_datafiles_cs
  - channel_data
  - channel_hyd_data
  - channel_sed_data
  - channel_nut_data
  - channel_temperature_data
  - water_temperature_data
defines_vars:
  - name
  - init
  - hyd
  - sed
  - nut
  - org_min
  - pest
  - path
  - hmet
  - salt
  - cs
purpose: ""
---

# channel_data_module

> [!info] Module
> Defines derived types and module-level variables.

## Defined Types
| Type | Notes |
|---|---|
| `routing_nut_data` |  |
| `channel_data_char_input` |  |
| `channel_init_datafiles` |  |
| `channel_init_datafiles_cs` |  |
| `channel_data` |  |
| `channel_hyd_data` |  |
| `channel_sed_data` |  |
| `channel_nut_data` |  |
| `channel_temperature_data` |  |
| `water_temperature_data` |  |

## Module-Level Variables
| Variable | Type | Meaning |
|---|---|---|
| `name` |  |  |
| `init` |  |  |
| `hyd` |  |  |
| `sed` |  |  |
| `nut` |  |  |
| `org_min` |  |  |
| `pest` |  |  |
| `path` |  |  |
| `hmet` |  |  |
| `salt` |  |  |
| `cs` |  |  |

## Used By Source Routines

```dataview
LIST file.link
WHERE type = "source" AND contains(module, this.module_name)
```

<!-- USER-NOTES-START -->
## Notes
Use this section for type and variable meanings, units, and allowed values. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
