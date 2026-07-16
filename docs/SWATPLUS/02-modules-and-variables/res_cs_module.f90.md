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
  - rescs_d
  - rescs_m
  - rescs_y
  - rescs_a
  - wetcs_d
  - wetcs_m
  - wetcs_y
  - wetcs_a
  - res_cs_data
  - rescs_hdr
defines_subroutines: []
defines_functions: []
defines_procedures: []
purpose: ""
---

# res_cs_module

> [!info] Module
> Defines derived types and module-level variables.

## Defined Types
### res_cs_balance

- **Defined in source**: `res_cs_module.f90:6`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `inflow` | `real` | 7 | kg !constituent entering the reservoir |
| `outflow` | `real` | 8 | kg !constituent leaving the reservoir via streamflow |
| `seep` | `real` | 9 | kg !constituent leaving the reservoir via seepage to aquifer |
| `settle` | `real` | 10 | kg !constituent settling to bottom of reservoir |
| `rctn` | `real` | 11 | kg !constituent removal due to chemical reaction |
| `prod` | `real` | 12 | kg !constituent produced due to chemical reaction |
| `fert` | `real` | 13 | kg !constituent added in fertilizer (to wetland) |
| `irrig` | `real` | 14 | kg !constituent removed from the reservoir via irrigation diversion |
| `div` | `real` | 15 | kg !constituent removed or added via diversion |
| `mass` | `real` | 16 | kg !constituent in reservoir water at end of day |
| `conc` | `real` | 17 | g/m3 !constituent concentration in reservoir at end of day |
| `volm` | `real` | 18 | m3 !volume of water in the reservoir |

### res_cs_output

- **Defined in source**: `res_cs_module.f90:21`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `cs` | `res_cs_balance` | 22 | constituents hydrographs |

### reservoir_cs_data

- **Defined in source**: `res_cs_module.f90:39`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `name` | `character(len=25)` | 40 |  |
| `v_seo4` | `real` | 41 | m/day \|settling rate for selenate |
| `v_seo3` | `real` | 42 | m/day \|settling rate for selinite |
| `v_born` | `real` | 43 | m/day \|settling rate for boron |
| `k_seo4` | `real` | 44 | 1/day \|first-order degradation constant for selenate |
| `k_seo3` | `real` | 45 | 1/day \|first-order degradation constant for selenite |
| `k_born` | `real` | 46 | 1/day \|first-order degradation constant for boron |
| `theta_seo4` | `real` | 47 | none \|temperature adjustment for selenate degradation |
| `theta_seo3` | `real` | 48 | none \|temperature adjustment for selenite degradation |
| `theta_born` | `real` | 49 | none \|temperature adjustment for boron degradation |
| `c_seo4` | `real` | 50 | g/m3 \|initial concentration of selenate |
| `c_seo3` | `real` | 51 | g/m3 \|initial concentration of selenite |
| `c_born` | `real` | 52 | g/m3 \|initial concentration of boron |

### res_cs_header

- **Defined in source**: `res_cs_module.f90:57`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `day` | `character (len=6)` | 58 |  |
| `mo` | `character (len=6)` | 59 |  |
| `day_mo` | `character (len=6)` | 60 |  |
| `yrc` | `character (len=6)` | 61 |  |
| `isd` | `character (len=8)` | 62 |  |
| `id` | `character (len=12)` | 63 |  |
| `seo4in` | `character(len=15)` | 64 |  |
| `seo3in` | `character(len=15)` | 65 |  |
| `bornin` | `character(len=15)` | 66 |  |
| `seo4out` | `character(len=15)` | 67 |  |
| `seo3out` | `character(len=15)` | 68 |  |
| `bornout` | `character(len=15)` | 69 |  |
| `seo4seep` | `character(len=15)` | 70 |  |
| `seo3seep` | `character(len=15)` | 71 |  |
| `bornseep` | `character(len=15)` | 72 |  |
| `seo4setl` | `character(len=15)` | 73 |  |
| `seo3setl` | `character(len=15)` | 74 |  |
| `bornsetl` | `character(len=15)` | 75 |  |
| `seo4rctn` | `character(len=15)` | 76 |  |
| `seo3rctn` | `character(len=15)` | 77 |  |
| `bornrctn` | `character(len=15)` | 78 |  |
| `seo4prod` | `character(len=15)` | 79 |  |
| `seo3prod` | `character(len=15)` | 80 |  |
| `bornprod` | `character(len=15)` | 81 |  |
| `seo4fert` | `character(len=15)` | 82 |  |
| `seo3fert` | `character(len=15)` | 83 |  |
| `bornfert` | `character(len=15)` | 84 |  |
| `seo4irr` | `character(len=15)` | 85 |  |
| `seo3irr` | `character(len=15)` | 86 |  |
| `bornirr` | `character(len=15)` | 87 |  |
| `seo4div` | `character(len=15)` | 88 |  |
| `seo3div` | `character(len=15)` | 89 |  |
| `borndiv` | `character(len=15)` | 90 |  |
| `seo4` | `character(len=15)` | 91 |  |
| `seo3` | `character(len=15)` | 92 |  |
| `born` | `character(len=15)` | 93 |  |
| `seo4c` | `character(len=15)` | 94 |  |
| `seo3c` | `character(len=15)` | 95 |  |
| `bornc` | `character(len=15)` | 96 |  |
| `volm` | `character(len=15)` | 97 |  |

## Variables Defined
### res_csbz

- **Type**: `res_cs_balance`
- **Defined in source**: `res_cs_module.f90:24`

### rescs_d

- **Type**: `res_cs_output`
- **Defined in source**: `res_cs_module.f90:27`

### rescs_m

- **Type**: `res_cs_output`
- **Defined in source**: `res_cs_module.f90:28`

### rescs_y

- **Type**: `res_cs_output`
- **Defined in source**: `res_cs_module.f90:29`

### rescs_a

- **Type**: `res_cs_output`
- **Defined in source**: `res_cs_module.f90:30`

### wetcs_d

- **Type**: `res_cs_output`
- **Defined in source**: `res_cs_module.f90:33`

### wetcs_m

- **Type**: `res_cs_output`
- **Defined in source**: `res_cs_module.f90:34`

### wetcs_y

- **Type**: `res_cs_output`
- **Defined in source**: `res_cs_module.f90:35`

### wetcs_a

- **Type**: `res_cs_output`
- **Defined in source**: `res_cs_module.f90:36`

### res_cs_data

- **Type**: `reservoir_cs_data`
- **Defined in source**: `res_cs_module.f90:54`

### rescs_hdr

- **Type**: `res_cs_header`
- **Defined in source**: `res_cs_module.f90:99`

## Subroutines Defined
(No subroutines detected.)

## Functions Defined
(No functions detected.)

## Used By Source Routines

```dataview
LIST file.link
WHERE type = "source" AND contains(module, this.module_name)
```

<!-- USER-NOTES-START -->
## Notes
Use this section for type and variable meanings, units, and allowed values. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
