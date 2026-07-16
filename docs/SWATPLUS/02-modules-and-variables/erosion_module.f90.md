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
  - ero_output
  - ero_hdr
  - ero_hdr_units
  - ero_1
  - ero_2
  - ero_3
defines_subroutines: []
defines_functions:
  - ero_add
  - ero_divide
defines_procedures:
  - ero_add
  - ero_divide
purpose: ""
---

# erosion_module

> [!info] Module
> Defines derived types and module-level variables.

## Defined Types
### erosion_output_variables

- **Defined in source**: `erosion_module.f90:5`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `sedyld` | `real` | 6 | t/ha \|sediment yield |
| `precip` | `real` | 7 | mm \|precipitation |
| `surfq` | `real` | 8 | mm \|surface runoff |
| `peak` | `real` | 9 | m3/s \|peak rate |
| `k` | `real` | 10 | \|usle k factor |
| `s` | `real` | 11 | m/m \|slope |
| `l` | `real` | 12 | m \|slope length |
| `ls` | `real` | 13 | \|usle ls factor |
| `p` | `real` | 14 | \|usle p factor |
| `c` | `real` | 15 | \|usle c factor |
| `rsd_m` | `real` | 16 | kg/ha \|surface residue mass |
| `grcov_frac` | `real` | 17 | frac \|ground cover fraction |
| `rsd_covfact` | `real` | 18 | \|residue cover factor |
| `bio_covfact` | `real` | 19 | \|growing biomass factor |

### erosion_output

- **Defined in source**: `erosion_module.f90:22`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `n_events` | `integer` | 23 | number of erosion events |
| `ero_d` | `erosion_output_variables` | 24 | ersion variables at each erosion event |
| `ero_ave` | `erosion_output_variables` | 25 | erosion variables averaged by number of events |

### erosion_output_header

- **Defined in source**: `erosion_module.f90:29`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `hru` | `character (len=6)` | 30 |  |
| `neve` | `character (len=6)` | 31 |  |
| `sedyld` | `character (len=6)` | 32 |  |
| `precip` | `character (len=6)` | 33 |  |
| `peak` | `character (len=9)` | 34 |  |
| `k` | `character (len=8)` | 35 |  |
| `s` | `character (len=16)` | 36 |  |
| `l` | `character (len=12)` | 37 |  |
| `ls` | `character (len=12)` | 38 |  |
| `p` | `character (len=12)` | 39 |  |
| `c` | `character (len=12)` | 40 |  |
| `rsd_m` | `character (len=12)` | 41 |  |
| `grcov_frac` | `character (len=12)` | 42 |  |
| `rsd_covfact` | `character (len=12)` | 43 |  |
| `bio_covfact` | `character (len=12)` | 44 |  |

### erosion_header_units

- **Defined in source**: `erosion_module.f90:48`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `hru` | `character (len=6)` | 49 |  |
| `neve` | `character (len=6)` | 50 |  |
| `sedyld` | `character (len=6)` | 51 |  |
| `precip` | `character (len=6)` | 52 |  |
| `peak` | `character (len=8)` | 53 |  |
| `k` | `character (len=8)` | 54 |  |
| `s` | `character (len=16)` | 55 |  |
| `l` | `character (len=12)` | 56 |  |
| `ls` | `character (len=12)` | 57 |  |
| `p` | `character (len=12)` | 58 |  |
| `c` | `character (len=12)` | 59 |  |
| `rsd_m` | `character (len=12)` | 60 |  |
| `grcov_frac` | `character (len=12)` | 61 |  |
| `rsd_covfact` | `character (len=12)` | 62 |  |
| `bio_covfact` | `character (len=12)` | 63 |  |

## Variables Defined
### ero_output

- **Type**: `erosion_output`
- **Defined in source**: `erosion_module.f90:27`
- **Source note**: dimensioned by hru

### ero_hdr

- **Type**: `erosion_output_header`
- **Defined in source**: `erosion_module.f90:46`

### ero_hdr_units

- **Type**: `erosion_header_units`
- **Defined in source**: `erosion_module.f90:65`

### ero_1

- **Type**: `erosion_output_variables`
- **Defined in source**: `erosion_module.f90:68`

### ero_2

- **Type**: `erosion_output_variables`
- **Defined in source**: `erosion_module.f90:68`

### ero_3

- **Type**: `erosion_output_variables`
- **Defined in source**: `erosion_module.f90:68`

## Subroutines Defined
(No subroutines detected.)

## Functions Defined
### ero_add

### ero_divide

## Used By Source Routines

```dataview
LIST file.link
WHERE type = "source" AND contains(module, this.module_name)
```

<!-- USER-NOTES-START -->
## Notes
Use this section for type and variable meanings, units, and allowed values. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
