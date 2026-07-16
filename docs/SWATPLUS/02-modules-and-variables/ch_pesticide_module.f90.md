---
type: module
tags:
  - swat/module
  - swat/to-read
file: ch_pesticide_module.f90
note_file: ch_pesticide_module.f90
module_name: ch_pesticide_module
defines_types:
  - ch_pesticide_processes
  - ch_pesticide_output
  - ch_pesticide_header
defines_vars:
  - ch_pestbz
  - bchpst_d
  - bchpst_m
  - bchpst_y
  - bchpst_a
  - chpst
  - chpstz
  - chpest_hdr
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

# ch_pesticide_module

> [!info] Module
> Defines derived types and module-level variables.

## Defined Types
| Type | Notes |
|---|---|
| `ch_pesticide_processes` |  |
| `ch_pesticide_output` |  |
| `ch_pesticide_header` |  |

## Module-Level Variables
| Variable | Type | Meaning |
|---|---|---|
| `ch_pestbz` |  |  |
| `bchpst_d` |  |  |
| `bchpst_m` |  |  |
| `bchpst_y` |  |  |
| `bchpst_a` |  |  |
| `chpst` |  |  |
| `chpstz` |  |  |
| `chpest_hdr` |  |  |
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
