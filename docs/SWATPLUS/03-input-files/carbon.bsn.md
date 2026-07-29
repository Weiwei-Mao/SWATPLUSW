---
type: input
tags:
  - swat/input
file: carbon.bsn
ext: bsn
cio_field: carbon_bsn
read_by:
  - carbon_bsn_read.f90
purpose: ""
---

# carbon.bsn

> [!info] Input File
> Declared in `file.cio` field `carbon_bsn`. See [[file.cio]] for the controlling file map.

## Overview
- **Declared in `file.cio` field**: `carbon_bsn`
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[carbon_bsn_read.f90]]

## File Structure
- [[carbon_bsn_read.f90]] source line 66: reads `'`, `iostat=eof) titldum`
- [[carbon_bsn_read.f90]] source line 67: reads `'`, `iostat=eof) header`
- [[carbon_bsn_read.f90]] source line 69: reads `org_frac%frac_seq`, `org_frac%frac_hum_microb`, `org_frac%frac_hum_slow`, `org_frac%frac_hum_passive`, `cb_wtr_coef%prmt_21`, `cb_wtr_coef%prmt_44`, `till_eff_days`, `man_coef%rtof`, `bio_consf`, `till_consf`, `org_con%tmpf`, `org_con%watf`, `org_con%tn`, `org_con%top`, `org_con%tx`, `bmix_a`, `bmix_b`, `bmix_c`, `tillmix_a`, `tillmix_b`, `tillmix_c`, `photo_degrade_factor`, `n_act_frac`, `cnr_cap`, `cnr_ref`, `cpr_cap`, `cpr_ref`, `mathers_int`

## Parameters
| Parameter | Type | Units | Meaning | Source | Reader line |
|---|---|---|---|---|---:|
| `org_frac%frac_seq` | `real` |  | fraction of total carbon the is sequestered carbon when initializing sequestered pools | [[carbon_module.f90#org_frac]] | [[carbon_bsn_read.f90]]:69 |
| `org_frac%frac_hum_microb` | `real` |  | !fraction of carbon that is microbrial pool when initializing microbrial pools | [[carbon_module.f90#org_frac]] | [[carbon_bsn_read.f90]]:69 |
| `org_frac%frac_hum_slow` | `real` |  | !fraction of carbon that is humas slow pool when initializing humus slow pools | [[carbon_module.f90#org_frac]] | [[carbon_bsn_read.f90]]:69 |
| `org_frac%frac_hum_passive` | `real` |  | fraction of carbon that is humas passive pool when initializing humas passive pools | [[carbon_module.f90#org_frac]] | [[carbon_bsn_read.f90]]:69 |
| `cb_wtr_coef%prmt_21` | `real` |  | KOC FOR CARBON LOSS IN WATER AND SEDIMENT(500._1500.) KD = KOC * C | [[carbon_module.f90#cb_wtr_coef]] | [[carbon_bsn_read.f90]]:69 |
| `cb_wtr_coef%prmt_44` | `real` |  | RATIO OF SOLUBLE C CONCENTRATION IN RUNOFF TO PERCOLATE(0.1_1.) | [[carbon_module.f90#cb_wtr_coef]] | [[carbon_bsn_read.f90]]:69 |
| `till_eff_days` | `integer` |  | none \|length of days a tillage operation will have an effect | [[tillage_data_module.f90#till_eff_days]] | [[carbon_bsn_read.f90]]:69 |
| `man_coef%rtof` | `real` | none | weighting factor used to partition the organic N & P concentration of septic effluent between the fresh organic and the stable organic pools | [[carbon_module.f90#man_coef]] | [[carbon_bsn_read.f90]]:69 |
| `bio_consf` | `real` |  |  | [[tillage_data_module.f90#bio_consf]] | [[carbon_bsn_read.f90]]:69 |
| `till_consf` | `real` |  |  | [[tillage_data_module.f90#till_consf]] | [[carbon_bsn_read.f90]]:69 |
| `org_con%tmpf` | `integer` |  | temperature factor approach used in cbn_zhang2 | [[carbon_module.f90#org_con]] | [[carbon_bsn_read.f90]]:69 |
| `org_con%watf` | `integer` |  | water factor approach used in cbn_zhang2 | [[carbon_module.f90#org_con]] | [[carbon_bsn_read.f90]]:69 |
| `org_con%tn` | `real` | celsius | minimum temperature bound | [[carbon_module.f90#org_con]] | [[carbon_bsn_read.f90]]:69 |
| `org_con%top` | `real` | celsius | peak (optimum) temperature | [[carbon_module.f90#org_con]] | [[carbon_bsn_read.f90]]:69 |
| `org_con%tx` | `real` | celsius | maximum temperature bound | [[carbon_module.f90#org_con]] | [[carbon_bsn_read.f90]]:69 |
| `bmix_a` | `real` |  | none !Base intercept in zz equation in mgt_tillfactor.f90 for biomixing | [[tillage_data_module.f90#bmix_a]] | [[carbon_bsn_read.f90]]:69 |
| `bmix_b` | `real` |  | none !slope of in zz equation in mgt_tillfactor.f90 for biomixing | [[tillage_data_module.f90#bmix_b]] | [[carbon_bsn_read.f90]]:69 |
| `bmix_c` | `real` |  | none !exponent multiplier in zz equation in mgt_tillfactor.f90 for biomixing | [[tillage_data_module.f90#bmix_c]] | [[carbon_bsn_read.f90]]:69 |
| `tillmix_a` | `real` |  | none !Base intercept in zz equation in mgt_tillfactor.f90 for tillage mixing | [[tillage_data_module.f90#tillmix_a]] | [[carbon_bsn_read.f90]]:69 |
| `tillmix_b` | `real` |  | none !slope of in zz equation in mgt_tillfactor.f90 for tillage mixing | [[tillage_data_module.f90#tillmix_b]] | [[carbon_bsn_read.f90]]:69 |
| `tillmix_c` | `real` |  | none !exponent multiplier in zz equation in mgt_tillfactor.f90 for tillage mixing | [[tillage_data_module.f90#tillmix_c]] | [[carbon_bsn_read.f90]]:69 |
| `photo_degrade_factor` | `real` | none | fraction to reduce surface residue due to photo degradation | [[plant_data_module.f90#photo_degrade_factor]] | [[carbon_bsn_read.f90]]:69 |
| `n_act_frac` | `real` | frac | fraction of organic N in the active humus pool (used in nut_nminrl active to stable flow) | [[carbon_module.f90#n_act_frac]] | [[carbon_bsn_read.f90]]:69 |
| `cnr_cap` | `real` | none | upper cap on residue C:N ratio before computing decomp factor | [[carbon_module.f90#cnr_cap]] | [[carbon_bsn_read.f90]]:69 |
| `cnr_ref` | `real` | none | reference C:N ratio where decomp factor equals 1 | [[carbon_module.f90#cnr_ref]] | [[carbon_bsn_read.f90]]:69 |
| `cpr_cap` | `real` | none | upper cap on residue C:P ratio before computing decomp factor | [[carbon_module.f90#cpr_cap]] | [[carbon_bsn_read.f90]]:69 |
| `cpr_ref` | `real` | none | reference C:P ratio where decomp factor equals 1 | [[carbon_module.f90#cpr_ref]] | [[carbon_bsn_read.f90]]:69 |
| `mathers_int` | `integer` |  | 0/1 flag for org_frac%mathers_method | `carbon_bsn_read.f90:44` | [[carbon_bsn_read.f90]]:69 |
