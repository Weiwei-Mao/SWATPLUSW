---
type: module
tags:
  - swat/module
  - swat/to-read
file: res_salt_module.f90
note_file: res_salt_module.f90
module_name: res_salt_module
defines_types:
  - res_salt_balance
  - res_salt_output
  - reservoir_salt_data
  - res_salt_header
defines_vars:
  - res_saltbz
  - ressalt_hdr
  - name
  - day
  - mo
  - day_mo
  - yrc
  - isd
  - id
  - so4in
  - cain
  - mgin
  - nain
  - kin
  - clin
  - co3in
  - hco3in
  - so4out
  - caout
  - mgout
  - naout
  - kout
  - clout
  - co3out
  - hco3out
  - so4seep
  - caseep
  - mgseep
  - naseep
  - kseep
  - clseep
  - co3seep
  - hco3seep
  - so4fert
  - cafert
  - mgfert
  - nafert
  - kfert
  - clfert
  - co3fert
  - hco3fert
  - so4irr
  - cairr
  - mgirr
  - nairr
  - kirr
  - clirr
  - co3irr
  - hco3irr
  - so4div
  - cadiv
  - mgdiv
  - nadiv
  - kdiv
  - cldiv
  - co3div
  - hco3div
  - so4
  - ca
  - mg
  - na
  - k
  - cl
  - co3
  - hco3
  - so4c
  - cac
  - mgc
  - nac
  - kc
  - clc
  - co3c
  - hco3c
  - volm
purpose: ""
---

# res_salt_module

> [!info] Module
> Defines derived types and module-level variables.

## Defined Types
| Type | Notes |
|---|---|
| `res_salt_balance` |  |
| `res_salt_output` |  |
| `reservoir_salt_data` |  |
| `res_salt_header` |  |

## Module-Level Variables
| Variable | Type | Meaning |
|---|---|---|
| `res_saltbz` |  |  |
| `ressalt_hdr` |  |  |
| `name` |  |  |
| `day` |  |  |
| `mo` |  |  |
| `day_mo` |  |  |
| `yrc` |  |  |
| `isd` |  |  |
| `id` |  |  |
| `so4in` |  |  |
| `cain` |  |  |
| `mgin` |  |  |
| `nain` |  |  |
| `kin` |  |  |
| `clin` |  |  |
| `co3in` |  |  |
| `hco3in` |  |  |
| `so4out` |  |  |
| `caout` |  |  |
| `mgout` |  |  |
| `naout` |  |  |
| `kout` |  |  |
| `clout` |  |  |
| `co3out` |  |  |
| `hco3out` |  |  |
| `so4seep` |  |  |
| `caseep` |  |  |
| `mgseep` |  |  |
| `naseep` |  |  |
| `kseep` |  |  |
| `clseep` |  |  |
| `co3seep` |  |  |
| `hco3seep` |  |  |
| `so4fert` |  |  |
| `cafert` |  |  |
| `mgfert` |  |  |
| `nafert` |  |  |
| `kfert` |  |  |
| `clfert` |  |  |
| `co3fert` |  |  |

*(Showing first 40 of 74 variables.)*

## Used By Source Routines

```dataview
LIST file.link
WHERE type = "source" AND contains(module, this.module_name)
```

<!-- USER-NOTES-START -->
## Notes
Use this section for type and variable meanings, units, and allowed values. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
