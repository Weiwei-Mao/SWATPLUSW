---
type: module
tags:
  - swat/module
  - swat/to-read
file: res_cs_module.f90
note_file: res_cs_module.f90
module_name: res_cs_module
defines_types:
  - res_cs_balance
  - res_cs_output
  - reservoir_cs_data
  - res_cs_header
defines_vars:
  - res_csbz
  - rescs_hdr
  - name
  - day
  - mo
  - day_mo
  - yrc
  - isd
  - id
  - seo4in
  - seo3in
  - bornin
  - seo4out
  - seo3out
  - bornout
  - seo4seep
  - seo3seep
  - bornseep
  - seo4setl
  - seo3setl
  - bornsetl
  - seo4rctn
  - seo3rctn
  - bornrctn
  - seo4prod
  - seo3prod
  - bornprod
  - seo4fert
  - seo3fert
  - bornfert
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
  - volm
purpose: ""
---

# res_cs_module

> [!info] Module
> Defines derived types and module-level variables.

## Defined Types
| Type | Notes |
|---|---|
| `res_cs_balance` |  |
| `res_cs_output` |  |
| `reservoir_cs_data` |  |
| `res_cs_header` |  |

## Module-Level Variables
| Variable | Type | Meaning |
|---|---|---|
| `res_csbz` |  |  |
| `rescs_hdr` |  |  |
| `name` |  |  |
| `day` |  |  |
| `mo` |  |  |
| `day_mo` |  |  |
| `yrc` |  |  |
| `isd` |  |  |
| `id` |  |  |
| `seo4in` |  |  |
| `seo3in` |  |  |
| `bornin` |  |  |
| `seo4out` |  |  |
| `seo3out` |  |  |
| `bornout` |  |  |
| `seo4seep` |  |  |
| `seo3seep` |  |  |
| `bornseep` |  |  |
| `seo4setl` |  |  |
| `seo3setl` |  |  |
| `bornsetl` |  |  |
| `seo4rctn` |  |  |
| `seo3rctn` |  |  |
| `bornrctn` |  |  |
| `seo4prod` |  |  |
| `seo3prod` |  |  |
| `bornprod` |  |  |
| `seo4fert` |  |  |
| `seo3fert` |  |  |
| `bornfert` |  |  |
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

*(Showing first 40 of 43 variables.)*

## Used By Source Routines

```dataview
LIST file.link
WHERE type = "source" AND contains(module, this.module_name)
```

<!-- USER-NOTES-START -->
## Notes
Use this section for type and variable meanings, units, and allowed values. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
