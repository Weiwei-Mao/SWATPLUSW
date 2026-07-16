---
type: module
tags:
  - swat/module
  - swat/to-read
file: output_ls_pesticide_module.f90
note_file: output_ls_pesticide_module.f90
module_name: output_ls_pesticide_module
defines_types:
  - pesticide_balance
  - object_pesticide_balance
  - output_pestbal_header
defines_vars:
  - pestbz
  - bpestb_d
  - bpestb_m
  - bpestb_y
  - bpestb_a
  - pestb_hdr
  - day
  - mo
  - day_mo
  - yrc
  - isd
  - id
  - name
  - pest
  - on_plant
  - soil
  - sed
  - surq
  - latq
  - tileq
  - perc
  - apply_s
  - apply_f
  - decay_s
  - decay_f
  - wash
  - metab_s
  - metab_f
  - uptake
  - in_plant
purpose: ""
---

# output_ls_pesticide_module

> [!info] Module
> Defines derived types and module-level variables.

## Defined Types
| Type | Notes |
|---|---|
| `pesticide_balance` |  |
| `object_pesticide_balance` |  |
| `output_pestbal_header` |  |

## Module-Level Variables
| Variable | Type | Meaning |
|---|---|---|
| `pestbz` |  |  |
| `bpestb_d` |  |  |
| `bpestb_m` |  |  |
| `bpestb_y` |  |  |
| `bpestb_a` |  |  |
| `pestb_hdr` |  |  |
| `day` |  |  |
| `mo` |  |  |
| `day_mo` |  |  |
| `yrc` |  |  |
| `isd` |  |  |
| `id` |  |  |
| `name` |  |  |
| `pest` |  |  |
| `on_plant` |  |  |
| `soil` |  |  |
| `sed` |  |  |
| `surq` |  |  |
| `latq` |  |  |
| `tileq` |  |  |
| `perc` |  |  |
| `apply_s` |  |  |
| `apply_f` |  |  |
| `decay_s` |  |  |
| `decay_f` |  |  |
| `wash` |  |  |
| `metab_s` |  |  |
| `metab_f` |  |  |
| `uptake` |  |  |
| `in_plant` |  |  |

## Used By Source Routines

```dataview
LIST file.link
WHERE type = "source" AND contains(module, this.module_name)
```

<!-- USER-NOTES-START -->
## Notes
Use this section for type and variable meanings, units, and allowed values. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
