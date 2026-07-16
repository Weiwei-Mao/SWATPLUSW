---
type: module
tags:
  - swat/module
  - swat/to-read
file: output_ls_salt_module.f90
note_file: output_ls_salt_module.f90
module_name: output_ls_salt_module
defines_types:
  - salt_balance
  - object_salt_balance
  - output_saltbal_header
defines_vars:
  - saltbz
  - bsaltb_d
  - bsaltb_m
  - bsaltb_y
  - bsaltb_a
  - saltb_hdr
  - day
  - mo
  - day_mo
  - yrc
  - isd
  - id
  - name
  - salt
  - plant
  - soil
  - surq
  - latq
  - tileq
  - perc
  - irrig
purpose: ""
---

# output_ls_salt_module

> [!info] Module
> Defines derived types and module-level variables.

## Defined Types
| Type | Notes |
|---|---|
| `salt_balance` |  |
| `object_salt_balance` |  |
| `output_saltbal_header` |  |

## Module-Level Variables
| Variable | Type | Meaning |
|---|---|---|
| `saltbz` |  |  |
| `bsaltb_d` |  |  |
| `bsaltb_m` |  |  |
| `bsaltb_y` |  |  |
| `bsaltb_a` |  |  |
| `saltb_hdr` |  |  |
| `day` |  |  |
| `mo` |  |  |
| `day_mo` |  |  |
| `yrc` |  |  |
| `isd` |  |  |
| `id` |  |  |
| `name` |  |  |
| `salt` |  |  |
| `plant` |  |  |
| `soil` |  |  |
| `surq` |  |  |
| `latq` |  |  |
| `tileq` |  |  |
| `perc` |  |  |
| `irrig` |  |  |

## Used By Source Routines

```dataview
LIST file.link
WHERE type = "source" AND contains(module, this.module_name)
```

<!-- USER-NOTES-START -->
## Notes
Use this section for type and variable meanings, units, and allowed values. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
