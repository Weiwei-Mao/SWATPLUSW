---
type: module
tags:
  - swat/module
  - swat/to-read
file: ch_cs_module.f90
note_file: ch_cs_module.f90
module_name: ch_cs_module
defines_types:
  - ch_cs_balance
  - ch_cs_output
  - ch_cs_header
defines_vars:
  - ch_csbz
  - chcs_hdr
  - day
  - mo
  - day_mo
  - yrc
  - isd
  - id
  - seo4in
  - seo3in
  - bornin
  - seo4gw
  - seo3gw
  - borngw
  - seo4out
  - seo3out
  - bornout
  - seo4seep
  - seo3seep
  - bornseep
  - seo4irr
  - seo3irr
  - bornirr
  - seo4div
  - seo3div
  - borndiv
  - seo4
  - seo3
  - born
  - seo4c
  - seo3c
  - bornc
purpose: ""
---

# ch_cs_module

> [!info] Module
> Defines derived types and module-level variables.

## Defined Types
| Type | Notes |
|---|---|
| `ch_cs_balance` |  |
| `ch_cs_output` |  |
| `ch_cs_header` |  |

## Module-Level Variables
| Variable | Type | Meaning |
|---|---|---|
| `ch_csbz` |  |  |
| `chcs_hdr` |  |  |
| `day` |  |  |
| `mo` |  |  |
| `day_mo` |  |  |
| `yrc` |  |  |
| `isd` |  |  |
| `id` |  |  |
| `seo4in` |  |  |
| `seo3in` |  |  |
| `bornin` |  |  |
| `seo4gw` |  |  |
| `seo3gw` |  |  |
| `borngw` |  |  |
| `seo4out` |  |  |
| `seo3out` |  |  |
| `bornout` |  |  |
| `seo4seep` |  |  |
| `seo3seep` |  |  |
| `bornseep` |  |  |
| `seo4irr` |  |  |
| `seo3irr` |  |  |
| `bornirr` |  |  |
| `seo4div` |  |  |
| `seo3div` |  |  |
| `borndiv` |  |  |
| `seo4` |  |  |
| `seo3` |  |  |
| `born` |  |  |
| `seo4c` |  |  |
| `seo3c` |  |  |
| `bornc` |  |  |

## Used By Source Routines

```dataview
LIST file.link
WHERE type = "source" AND contains(module, this.module_name)
```

<!-- USER-NOTES-START -->
## Notes
Use this section for type and variable meanings, units, and allowed values. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
