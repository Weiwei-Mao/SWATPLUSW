---
type: module
tags:
  - swat/module
  - swat/to-read
file: climate_module.f90
note_file: climate_module.f90
module_name: climate_module
defines_types:
  - weather_generator_db
  - wgn_parms
  - wind_direction_db
  - weather_daily
  - weather_codes_station
  - weather_codes_station_char
  - weather_station
  - climate_change_variables
  - climate_measured_data
  - atmospheric_deposition
  - atmospheric_deposition_control
  - atmospheric_deposition_cs
  - object_deposition_cs
  - road_salt
  - object_road_salt
defines_vars:
  - w
  - wco_c
  - wco
  - weat
  - name
  - precip_prior_day
  - wgn
  - pgage
  - tgage
  - sgage
  - hgage
  - wgage
  - petgage
  - atmodep
  - filename
  - timestep
  - salt_atmo
  - cs_atmo
purpose: ""
---

# climate_module

> [!info] Module
> Defines derived types and module-level variables.

## Defined Types
| Type | Notes |
|---|---|
| `weather_generator_db` |  |
| `wgn_parms` |  |
| `wind_direction_db` |  |
| `weather_daily` |  |
| `weather_codes_station` |  |
| `weather_codes_station_char` |  |
| `weather_station` |  |
| `climate_change_variables` |  |
| `climate_measured_data` |  |
| `atmospheric_deposition` |  |
| `atmospheric_deposition_control` |  |
| `atmospheric_deposition_cs` |  |
| `object_deposition_cs` |  |
| `road_salt` |  |
| `object_road_salt` |  |

## Module-Level Variables
| Variable | Type | Meaning |
|---|---|---|
| `w` |  |  |
| `wco_c` |  |  |
| `wco` |  |  |
| `weat` |  |  |
| `name` |  |  |
| `precip_prior_day` |  |  |
| `wgn` |  |  |
| `pgage` |  |  |
| `tgage` |  |  |
| `sgage` |  |  |
| `hgage` |  |  |
| `wgage` |  |  |
| `petgage` |  |  |
| `atmodep` |  |  |
| `filename` |  |  |
| `timestep` |  |  |
| `salt_atmo` |  |  |
| `cs_atmo` |  |  |

## Used By Source Routines

```dataview
LIST file.link
WHERE type = "source" AND contains(module, this.module_name)
```

<!-- USER-NOTES-START -->
## Notes
Use this section for type and variable meanings, units, and allowed values. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
