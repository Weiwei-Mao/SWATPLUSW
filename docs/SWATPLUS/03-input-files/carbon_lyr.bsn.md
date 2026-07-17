---
type: input
tags:
  - swat/input
  - swat/auxiliary-input
file: carbon_lyr.bsn
ext: bsn
cio_field: []
read_by:
  - carbon_bsn_read.f90
purpose: "Per-layer carbon transformation and allocation coefficients used with carbon.bsn."
---

# carbon_lyr.bsn

> [!info] Input File
> Companion file for [[carbon.bsn]]. It is not listed directly in `file.cio`; [[carbon_bsn_read.f90]] derives its name from the `carbon_bsn` entry.

## Overview
- **Declared in `file.cio` field**: not listed directly. The reader derives this file from `carbon_bsn`.
- **Derived name rule**: `carbon.bsn` -> `carbon_lyr.bsn`; `foo.bsn` -> `foo_lyr.bsn`; a name without an extension gets `_lyr.bsn` appended.
- **Required when**: dynamic carbon is enabled (`codes.bsn` carbon / `bsn_cc%cswat` = `2`).
- **Format source**: [[carbon_bsn_read.f90]] and the Ames_sub1 demo input.
- **Format style**: SWAT+ text input using list-directed Fortran reads.

## Reader Routines
- [[carbon_bsn_read.f90]]

## File Structure
- [[carbon_bsn_read.f90]] source line 121: reads `titldum`
- [[carbon_bsn_read.f90]] source line 122: reads `header`
- [[carbon_bsn_read.f90]] source line 127: reads one or more data rows containing `layer`, `hp_rate`, `hs_rate`, `microb_rate`, `meta_rate`, `str_rate`, `microb_top_rate`, `hs_hp`, `a1co2`, `asco2`, `apco2`, `abco2`

The first two records are consumed as title and column-header text. Their contents are ignored, but the records should be present so the first coefficient row starts on the third line.

## Layer Rules
- `layer_id` is the array index used for both `carbdb(layer_id)` and `org_allo(layer_id)`.
- Current valid `layer_id` values are `1` and `2`, because [[carbon_module.f90#carbdb]] and [[carbon_module.f90#org_allo]] are both declared with `dimension(2)`.
- The source comments define layer `1` as the top layer coefficient group and layer `2` as the subsurface coefficient group.
- Rows with `layer_id` outside `1:size(carbdb)` are ignored and logged.
- The reader requires at least `size(carbdb)` valid rows. With the current source, that means two valid rows are expected.

This two-row constraint applies to the carbon coefficient groups in `carbon_lyr.bsn`. It is separate from [[carbon_layers.prt]], which controls the number of soil layers written in per-layer carbon output files.

## Parameters
| Parameter | Type | Units | Meaning | Source | Reader line |
|---|---|---|---|---|---:|
| `layer` | `integer` |  | coefficient layer index; currently `1` = top and `2` = subsurface | `layer_id` local variable | [[carbon_bsn_read.f90]]:128 |
| `hp_rate` | `real` |  | rate of transformation of passive humus under optimal conditions | [[carbon_module.f90#carbdb]]`(layer)%hp_rate` | [[carbon_bsn_read.f90]]:140 |
| `hs_rate` | `real` |  | rate of transformation of slow humus under optimal conditions | [[carbon_module.f90#carbdb]]`(layer)%hs_rate` | [[carbon_bsn_read.f90]]:141 |
| `microb_rate` | `real` |  | rate of transformation of microbial biomass and associated products under optimal conditions | [[carbon_module.f90#carbdb]]`(layer)%microb_rate` | [[carbon_bsn_read.f90]]:142 |
| `meta_rate` | `real` |  | rate of transformation of metabolic litter under optimal conditions | [[carbon_module.f90#carbdb]]`(layer)%meta_rate` | [[carbon_bsn_read.f90]]:143 |
| `str_rate` | `real` |  | rate of potential transformation of structural litter under optimal conditions | [[carbon_module.f90#carbdb]]`(layer)%str_rate` | [[carbon_bsn_read.f90]]:144 |
| `microb_top_rate` | `real` |  | coefficient adjusting microbial activity function in the top soil layer | [[carbon_module.f90#carbdb]]`(layer)%microb_top_rate` | [[carbon_bsn_read.f90]]:145 |
| `hs_hp` | `real` |  | coefficient in the CENTURY equation allocating slow humus to passive humus | [[carbon_module.f90#carbdb]]`(layer)%hs_hp` | [[carbon_bsn_read.f90]]:146 |
| `a1co2` | `real` | frac | fraction of decomposed metabolic and passive pools allocated to CO2 | [[carbon_module.f90#org_allo]]`(layer)%a1co2` | [[carbon_bsn_read.f90]]:148 |
| `asco2` | `real` | frac | fraction of decomposed slow humus allocated to CO2 | [[carbon_module.f90#org_allo]]`(layer)%asco2` | [[carbon_bsn_read.f90]]:149 |
| `apco2` | `real` | frac | fraction of decomposed passive humus allocated to CO2 | [[carbon_module.f90#org_allo]]`(layer)%apco2` | [[carbon_bsn_read.f90]]:150 |
| `abco2` | `real` | frac | fraction of decomposed microbial biomass allocated to CO2 | [[carbon_module.f90#org_allo]]`(layer)%abco2` | [[carbon_bsn_read.f90]]:151 |

## Ames_sub1 Example

The Ames_sub1 demo provides two coefficient rows:

```text
carbon_lyr.bsn: derived from carb_coefs.cbn (per-layer carbon coefficients)
           layer         hp_rate         hs_rate     microb_rate       meta_rate        str_rate microb_top_rate           hs_hp           a1co2           asco2           apco2           abco2
               1         1.2e-05        2.92e-04          0.0164          0.0405          0.0107          0.0164            0.05            0.60            0.55            0.55            0.55
               2         1.2e-05        1.81e-04            0.02          0.0507          0.0134            0.02            0.05            0.55            0.55            0.55             0.0
```

## Notes
- `carbon_lyr.bsn` is required together with [[carbon.bsn]] only for the dynamic CENTURY/SWAT-C carbon option (`codes.bsn` carbon = `2`).
- If `carbon.bsn` is renamed through `file.cio`, this file must be renamed using the same derived-name rule.
- Duplicate valid `layer_id` rows are not rejected explicitly; later rows overwrite earlier values for the same layer.
