---
type: module
tags:
  - swat/module
  - swat/to-read
file: plant_module.f90
note_file: plant_module.f90
module_name: plant_module
defines_types:
  - plant_growth
  - plant_mass
  - plant_status
  - plant_stress
  - auto_operations
  - fertilize_future
  - plant_community
  - basin_crop_yields
  - plant_carbon
defines_vars:
  - yld_tbr
  - yld_grn
  - yld_veg
  - yld_rsd
  - plmz
  - o_m1
  - o_m2
  - o_m3
  - plstrz
  - bsn_crop_yld_z
  - c_frac
  - gro
  - idorm
  - mseas
  - name
  - fertname
  - fertop
  - last_kill
purpose: ""
---

# plant_module

> [!info] Module
> Defines derived types and module-level variables.

## Defined Types
| Type | Notes |
|---|---|
| `plant_growth` |  |
| `plant_mass` |  |
| `plant_status` |  |
| `plant_stress` |  |
| `auto_operations` |  |
| `fertilize_future` |  |
| `plant_community` |  |
| `basin_crop_yields` |  |
| `plant_carbon` |  |

## Module-Level Variables
| Variable | Type | Meaning |
|---|---|---|
| `yld_tbr` |  |  |
| `yld_grn` |  |  |
| `yld_veg` |  |  |
| `yld_rsd` |  |  |
| `plmz` |  |  |
| `o_m1` |  |  |
| `o_m2` |  |  |
| `o_m3` |  |  |
| `plstrz` |  |  |
| `bsn_crop_yld_z` |  |  |
| `c_frac` |  |  |
| `gro` |  |  |
| `idorm` |  |  |
| `mseas` |  |  |
| `name` |  |  |
| `fertname` |  |  |
| `fertop` |  |  |
| `last_kill` |  |  |

## Used By Source Routines

```dataview
LIST file.link
WHERE type = "source" AND contains(module, this.module_name)
```

<!-- USER-NOTES-START -->
## Notes
Use this section for type and variable meanings, units, and allowed values. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
