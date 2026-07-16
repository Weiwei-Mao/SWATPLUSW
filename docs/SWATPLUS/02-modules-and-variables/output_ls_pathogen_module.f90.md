---
type: module
tags:
  - swat/module
  - swat/to-read
file: output_ls_pathogen_module.f90
note_file: output_ls_pathogen_module.f90
module_name: output_ls_pathogen_module
defines_types:
  - pathogen_balance
  - object_pathogen_balance
  - output_pathbal_header
defines_vars:
  - pathbz
  - bpathb_d
  - bpathb_m
  - bpathb_y
  - bpathb_a
  - pathb_hdr
  - day
  - mo
  - day_mo
  - yrc
  - isd
  - id
  - name
  - plant
  - soil
  - sed
  - surq
  - latq
  - perc
  - apply
  - decay
purpose: ""
---

# output_ls_pathogen_module

> [!info] Module
> Defines derived types and module-level variables.

## Defined Types
| Type | Notes |
|---|---|
| `pathogen_balance` |  |
| `object_pathogen_balance` |  |
| `output_pathbal_header` |  |

## Module-Level Variables
| Variable | Type | Meaning |
|---|---|---|
| `pathbz` |  |  |
| `bpathb_d` |  |  |
| `bpathb_m` |  |  |
| `bpathb_y` |  |  |
| `bpathb_a` |  |  |
| `pathb_hdr` |  |  |
| `day` |  |  |
| `mo` |  |  |
| `day_mo` |  |  |
| `yrc` |  |  |
| `isd` |  |  |
| `id` |  |  |
| `name` |  |  |
| `plant` |  |  |
| `soil` |  |  |
| `sed` |  |  |
| `surq` |  |  |
| `latq` |  |  |
| `perc` |  |  |
| `apply` |  |  |
| `decay` |  |  |

## Used By Source Routines

```dataview
LIST file.link
WHERE type = "source" AND contains(module, this.module_name)
```

<!-- USER-NOTES-START -->
## Notes
Use this section for type and variable meanings, units, and allowed values. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
