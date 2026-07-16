---
type: module
tags:
  - swat/module
  - swat/to-read
file: res_pesticide_module.f90
note_file: res_pesticide_module.f90
module_name: res_pesticide_module
defines_types:
  - res_pesticide_processes
  - res_pesticide_output
  - res_pesticide_header
defines_vars:
  - res_pestbz
  - brespst_d
  - brespst_m
  - brespst_y
  - brespst_a
  - respst
  - respstz
  - respest_hdr
  - day
  - mo
  - day_mo
  - yrc
  - isd
  - id
  - name
  - pest
  - tot_in
  - sol_out
  - sor_out
  - react
  - metab
  - volat
  - settle
  - resus
  - difus
  - react_bot
  - metab_bot
  - bury
  - water
  - benthic
purpose: ""
---

# res_pesticide_module

> [!info] Module
> Defines derived types and module-level variables.

## Defined Types
| Type | Notes |
|---|---|
| `res_pesticide_processes` |  |
| `res_pesticide_output` |  |
| `res_pesticide_header` |  |

## Module-Level Variables
| Variable | Type | Meaning |
|---|---|---|
| `res_pestbz` |  |  |
| `brespst_d` |  |  |
| `brespst_m` |  |  |
| `brespst_y` |  |  |
| `brespst_a` |  |  |
| `respst` |  |  |
| `respstz` |  |  |
| `respest_hdr` |  |  |
| `day` |  |  |
| `mo` |  |  |
| `day_mo` |  |  |
| `yrc` |  |  |
| `isd` |  |  |
| `id` |  |  |
| `name` |  |  |
| `pest` |  |  |
| `tot_in` |  |  |
| `sol_out` |  |  |
| `sor_out` |  |  |
| `react` |  |  |
| `metab` |  |  |
| `volat` |  |  |
| `settle` |  |  |
| `resus` |  |  |
| `difus` |  |  |
| `react_bot` |  |  |
| `metab_bot` |  |  |
| `bury` |  |  |
| `water` |  |  |
| `benthic` |  |  |

## Used By Source Routines

```dataview
LIST file.link
WHERE type = "source" AND contains(module, this.module_name)
```

<!-- USER-NOTES-START -->
## Notes
Use this section for type and variable meanings, units, and allowed values. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
