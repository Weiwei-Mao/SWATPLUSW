---
type: module
tags:
  - swat/module
  - swat/to-read
file: hru_lte_module.f90
note_file: hru_lte_module.f90
module_name: hru_lte_module
defines_types:
  - swatdeg_hru_data
  - swatdeg_hru_dynamic
defines_vars:
  - name
  - text
  - tropical
  - igrow1
  - igrow2
  - plant
  - ipet
  - irr
  - irrsrc
  - lsu
  - region
  - gro
purpose: ""
---

# hru_lte_module

> [!info] Module
> Defines derived types and module-level variables.

## Defined Types
| Type | Notes |
|---|---|
| `swatdeg_hru_data` |  |
| `swatdeg_hru_dynamic` |  |

## Module-Level Variables
| Variable | Type | Meaning |
|---|---|---|
| `name` |  |  |
| `text` |  |  |
| `tropical` |  |  |
| `igrow1` |  |  |
| `igrow2` |  |  |
| `plant` |  |  |
| `ipet` |  |  |
| `irr` |  |  |
| `irrsrc` |  |  |
| `lsu` |  |  |
| `region` |  |  |
| `gro` |  |  |

## Used By Source Routines

```dataview
LIST file.link
WHERE type = "source" AND contains(module, this.module_name)
```

<!-- USER-NOTES-START -->
## Notes
Use this section for type and variable meanings, units, and allowed values. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
