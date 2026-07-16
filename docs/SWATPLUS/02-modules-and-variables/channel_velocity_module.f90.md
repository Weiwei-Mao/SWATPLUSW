---
type: module
tags:
  - swat/module
  - swat/to-read
file: channel_velocity_module.f90
note_file: channel_velocity_module.f90
module_name: channel_velocity_module
defines_types:
  - channel_velocity_parameters
defines_vars:
  - ch_vel
  - sd_ch_vel
  - grwway_vel
defines_subroutines: []
defines_functions: []
defines_procedures: []
purpose: ""
---

# channel_velocity_module

> [!info] Module
> Defines derived types and module-level variables.

## Defined Types
### channel_velocity_parameters

- **Defined in source**: `channel_velocity_module.f90:5`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `area` | `real` | 6 | m^2 \|cross sectional area of flow at bankfull depth |
| `vel_bf` | `real` | 7 | m^3/s \|flow rate when reach is at bankful depth |
| `vel` | `real` | 8 | m/s \|velocity (from sd_channel_sediment3) |
| `rttime` | `real` | 9 | hr \|routing time (from sd_channel_sediment3) |
| `wid_btm` | `real` | 10 | m \|bottom width of main channel |
| `dep_bf` | `real` | 11 | m \|depth of water when reach is at bankfull depth |
| `velav_bf` | `real` | 12 | m/s \|average velocity when reach is at bankfull depth |
| `celerity_bf` | `real` | 13 | m/s \|wave celerity when reach is at bankfull depth |
| `st_dis` | `real` | 14 | hr \|storage time constant for reach at bankfull depth |
| `vel_1bf` | `real` | 15 | m/s \|average velocity when reach is at 0.1 bankfull depth (low flow) |
| `celerity_1bf` | `real` | 16 | m/s \|wave celerity when reach is at 0.1 bankfull depth (low flow) |
| `stor_dis_1bf` | `real` | 17 | hr \|storage time constant for reach at 0.1 bankfull depth (low flow) |

## Variables Defined
### ch_vel

- **Type**: `channel_velocity_parameters`
- **Defined in source**: `channel_velocity_module.f90:19`

### sd_ch_vel

- **Type**: `channel_velocity_parameters`
- **Defined in source**: `channel_velocity_module.f90:20`

### grwway_vel

- **Type**: `channel_velocity_parameters`
- **Defined in source**: `channel_velocity_module.f90:21`

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
