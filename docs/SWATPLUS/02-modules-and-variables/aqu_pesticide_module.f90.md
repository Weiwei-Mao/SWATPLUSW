---
type: module
tags:
  - swat/module
  - swat/to-read
file: aqu_pesticide_module.f90
note_file: aqu_pesticide_module.f90
module_name: aqu_pesticide_module
defines_types:
  - aqu_pesticide_processes
  - aqu_pesticide_output
  - aqu_pesticide_header
defines_vars:
  - aqu_pestbz
  - baqupst_d
  - baqupst_m
  - baqupst_y
  - baqupst_a
  - aqupst
  - aqupstz
  - aqupest_hdr
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
  - sol_perc
  - react
  - metab
  - stor_ave
  - stor_init
  - stor_final
purpose: ""
---

# aqu_pesticide_module

> [!info] Module
> Defines derived types and module-level variables.

## Defined Types
| Type | Notes |
|---|---|
| `aqu_pesticide_processes` |  |
| `aqu_pesticide_output` |  |
| `aqu_pesticide_header` |  |

## Module-Level Variables
| Variable | Type | Meaning |
|---|---|---|
| `aqu_pestbz` |  |  |
| `baqupst_d` |  |  |
| `baqupst_m` |  |  |
| `baqupst_y` |  |  |
| `baqupst_a` |  |  |
| `aqupst` |  |  |
| `aqupstz` |  |  |
| `aqupest_hdr` |  |  |
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
| `sol_perc` |  |  |
| `react` |  |  |
| `metab` |  |  |
| `stor_ave` |  |  |
| `stor_init` |  |  |
| `stor_final` |  |  |

## Used By Source Routines

```dataview
LIST file.link
WHERE type = "source" AND contains(module, this.module_name)
```

<!-- USER-NOTES-START -->
## Notes
Use this section for type and variable meanings, units, and allowed values. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
