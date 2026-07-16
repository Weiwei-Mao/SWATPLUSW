---
type: module
tags:
  - swat/module
  - swat/to-read
file: soil_nutcarb_module.f90
note_file: soil_nutcarb_module.f90
module_name: soil_nutcarb_module
defines_types:
  - organic_carbon_header
  - total_carbon_header
  - organic_carbon_units
  - total_carbon_units
defines_vars:
  - orgc_hdr
  - totc_hdr
  - orgc_units
  - totc_units
  - day_mo
  - yrc
  - hru
  - str_c
  - lig_c
  - meta_c
  - man_c
  - hum_c
  - phum_c
  - mb_c
  - day
  - isd
  - soil_org_c
  - plm_com_c
  - rsd_com_c
purpose: ""
---

# soil_nutcarb_module

> [!info] Module
> Defines derived types and module-level variables.

## Defined Types
| Type | Notes |
|---|---|
| `organic_carbon_header` |  |
| `total_carbon_header` |  |
| `organic_carbon_units` |  |
| `total_carbon_units` |  |

## Module-Level Variables
| Variable | Type | Meaning |
|---|---|---|
| `orgc_hdr` |  |  |
| `totc_hdr` |  |  |
| `orgc_units` |  |  |
| `totc_units` |  |  |
| `day_mo` |  |  |
| `yrc` |  |  |
| `hru` |  |  |
| `str_c` |  |  |
| `lig_c` |  |  |
| `meta_c` |  |  |
| `man_c` |  |  |
| `hum_c` |  |  |
| `phum_c` |  |  |
| `mb_c` |  |  |
| `day` |  |  |
| `isd` |  |  |
| `soil_org_c` |  |  |
| `plm_com_c` |  |  |
| `rsd_com_c` |  |  |

## Used By Source Routines

```dataview
LIST file.link
WHERE type = "source" AND contains(module, this.module_name)
```

<!-- USER-NOTES-START -->
## Notes
Use this section for type and variable meanings, units, and allowed values. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
