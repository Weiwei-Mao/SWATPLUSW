---
type: module
tags:
  - swat/module
  - swat/to-read
file: erosion_module.f90
note_file: erosion_module.f90
module_name: erosion_module
defines_types:
  - erosion_output_variables
  - erosion_output
  - erosion_output_header
  - erosion_header_units
defines_vars:
  - ero_d
  - ero_ave
  - ero_hdr
  - ero_hdr_units
  - ero_1
  - ero_2
  - ero_3
  - hru
  - neve
  - sedyld
  - precip
  - peak
  - k
  - s
  - l
  - ls
  - p
  - c
  - rsd_m
  - grcov_frac
  - rsd_covfact
  - bio_covfact
purpose: ""
---

# erosion_module

> [!info] Module
> Defines derived types and module-level variables.

## Defined Types
| Type | Notes |
|---|---|
| `erosion_output_variables` |  |
| `erosion_output` |  |
| `erosion_output_header` |  |
| `erosion_header_units` |  |

## Module-Level Variables
| Variable | Type | Meaning |
|---|---|---|
| `ero_d` |  |  |
| `ero_ave` |  |  |
| `ero_hdr` |  |  |
| `ero_hdr_units` |  |  |
| `ero_1` |  |  |
| `ero_2` |  |  |
| `ero_3` |  |  |
| `hru` |  |  |
| `neve` |  |  |
| `sedyld` |  |  |
| `precip` |  |  |
| `peak` |  |  |
| `k` |  |  |
| `s` |  |  |
| `l` |  |  |
| `ls` |  |  |
| `p` |  |  |
| `c` |  |  |
| `rsd_m` |  |  |
| `grcov_frac` |  |  |
| `rsd_covfact` |  |  |
| `bio_covfact` |  |  |

## Used By Source Routines

```dataview
LIST file.link
WHERE type = "source" AND contains(module, this.module_name)
```

<!-- USER-NOTES-START -->
## Notes
Use this section for type and variable meanings, units, and allowed values. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
