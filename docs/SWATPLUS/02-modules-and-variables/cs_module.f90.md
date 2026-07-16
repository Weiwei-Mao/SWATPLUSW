---
type: module
tags:
  - swat/module
  - swat/to-read
file: cs_module.f90
note_file: cs_module.f90
module_name: cs_module
defines_types:
  - cs_balance
  - object_cs_balance
  - fert_db_cs
  - output_csbal_header
  - output_cs_hdr_hru
defines_vars:
  - csb_hdr
  - cs_hdr_hru
  - fertnm
  - yrc
  - mon
  - day
  - latseo4
  - surseo4
  - sedseo4
  - urbseo4
  - wetseo4
  - tileseo4
  - percseo4
  - gwupseo4
  - wtspseo4
  - irswseo4
  - irgwseo4
  - irwoseo4
  - rainseo4
  - drydseo4
  - fertseo4
  - uptkseo4
  - rctnseo4
  - sorbseo4
  - ptsoseo4
  - poutseo4
  - sldsseo4
  - srbdseo4
  - gwseo4
  - rchgseo4
  - seepseo4
  - rctaseo4
  - srbaseo4
  - aqdsseo4
  - srdaseo4
  - latseo3
  - surseo3
  - sedseo3
  - urbseo3
  - wetseo3
  - tileseo3
  - percseo3
  - gwupseo3
  - wtspseo3
  - irswseo3
  - irgwseo3
  - irwoseo3
  - rainseo3
  - drydseo3
  - fertseo3
  - uptkseo3
  - rctnseo3
  - sorbseo3
  - ptsoseo3
  - poutseo3
  - sldsseo3
  - srbdseo3
  - gwseo3
  - rchgseo3
  - seepseo3
  - rctaseo3
  - srbaseo3
  - aqdsseo3
  - srdaseo3
  - latborn
  - surborn
  - sedborn
  - urbborn
  - wetborn
  - tileborn
  - percborn
  - gwupborn
  - wtspborn
  - irswborn
  - irgwborn
  - irwoborn
  - rainborn
  - drydborn
  - fertborn
  - uptkborn
  - rctnborn
  - sorbborn
  - ptsoborn
  - poutborn
  - sldsborn
  - srbdborn
  - gwborn
  - rchgborn
  - seepborn
  - rctaborn
  - srbaborn
  - aqdsborn
  - srdaborn
  - mo
  - day_mo
  - isd
  - id
  - seo4sl
  - seo3sl
  - bornsl
  - seo4sq
  - seo3sq
  - bornsq
  - seo4sd
  - seo3sd
  - bornsd
  - seo4lq
  - seo3lq
  - bornlq
  - seo4ub
  - seo3ub
  - bornub
  - seo4wt
  - seo3wt
  - bornwt
  - seo4tq
  - seo3tq
  - borntq
  - seo4pc
  - seo3pc
  - bornpc
  - seo4gt
  - seo3gt
  - borngt
  - seo4ws
  - seo3ws
  - bornws
  - seo4is
  - seo3is
  - bornis
  - seo4ig
  - seo3ig
  - bornig
  - seo4io
  - seo3io
  - bornio
  - seo4rn
  - seo3rn
  - bornrn
  - seo4dd
  - seo3dd
  - borndd
  - seo4fz
  - seo3fz
  - bornfz
  - seo4up
  - seo3up
  - bornup
  - seo4rc
  - seo3rc
  - bornrc
  - seo4sp
  - seo3sp
  - bornsp
  - seo4c
  - seo3c
  - bornc
  - seo4srbd
  - seo3srbd
  - bornsrbd
purpose: ""
---

# cs_module

> [!info] Module
> Defines derived types and module-level variables.

## Defined Types
| Type | Notes |
|---|---|
| `cs_balance` |  |
| `object_cs_balance` |  |
| `fert_db_cs` |  |
| `output_csbal_header` |  |
| `output_cs_hdr_hru` |  |

## Module-Level Variables
| Variable | Type | Meaning |
|---|---|---|
| `csb_hdr` |  |  |
| `cs_hdr_hru` |  |  |
| `fertnm` |  |  |
| `yrc` |  |  |
| `mon` |  |  |
| `day` |  |  |
| `latseo4` |  |  |
| `surseo4` |  |  |
| `sedseo4` |  |  |
| `urbseo4` |  |  |
| `wetseo4` |  |  |
| `tileseo4` |  |  |
| `percseo4` |  |  |
| `gwupseo4` |  |  |
| `wtspseo4` |  |  |
| `irswseo4` |  |  |
| `irgwseo4` |  |  |
| `irwoseo4` |  |  |
| `rainseo4` |  |  |
| `drydseo4` |  |  |
| `fertseo4` |  |  |
| `uptkseo4` |  |  |
| `rctnseo4` |  |  |
| `sorbseo4` |  |  |
| `ptsoseo4` |  |  |
| `poutseo4` |  |  |
| `sldsseo4` |  |  |
| `srbdseo4` |  |  |
| `gwseo4` |  |  |
| `rchgseo4` |  |  |
| `seepseo4` |  |  |
| `rctaseo4` |  |  |
| `srbaseo4` |  |  |
| `aqdsseo4` |  |  |
| `srdaseo4` |  |  |
| `latseo3` |  |  |
| `surseo3` |  |  |
| `sedseo3` |  |  |
| `urbseo3` |  |  |
| `wetseo3` |  |  |

*(Showing first 40 of 160 variables.)*

## Used By Source Routines

```dataview
LIST file.link
WHERE type = "source" AND contains(module, this.module_name)
```

<!-- USER-NOTES-START -->
## Notes
Use this section for type and variable meanings, units, and allowed values. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
