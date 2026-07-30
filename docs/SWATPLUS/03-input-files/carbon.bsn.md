---
type: input
tags:
  - swat/input
file: carbon.bsn
ext: bsn
cio_field: carbon_bsn
read_by:
  - carbon_bsn_read.f90
purpose: "Basin-wide scalar controls for the dynamic CENTURY/SWAT-C carbon option."
---

# carbon.bsn

> [!info] Input File
> Declared in `file.cio` field `carbon_bsn`. Required only when the basin carbon code enables the dynamic CENTURY/SWAT-C carbon option (`codes.bsn` carbon = `2`).

## Overview
- **Declared in `file.cio` field**: `carbon_bsn`
- **Default file name**: `carbon.bsn`
- **Required when**: dynamic carbon is enabled (`codes.bsn` carbon / `bsn_cc%cswat` = `2`).
- **Companion file**: [[carbon_lyr.bsn]], whose name is derived from this file name by [[carbon_bsn_read.f90]].
- **Format source**: [[carbon_bsn_read.f90]] and the Ames_sub1 demo input.
- **Format style**: SWAT+ text input using list-directed Fortran reads for the data row.

## Reader Routines
- [[carbon_bsn_read.f90]]

## File Structure
- [[carbon_bsn_read.f90]] source line 66: reads `titldum` from the first record as ignored title/comment text.
- [[carbon_bsn_read.f90]] source line 67: reads `header` from the second record as ignored column-header text.
- [[carbon_bsn_read.f90]] source line 69: reads one data row containing 28 scalar values in this order: `init_seq`, `init_microb`, `init_slow`, `init_passive`, `koc_c`, `solc_ratio`, `till_eff_days`, `manure_c_frac`, `bio_consol`, `till_consol`, `tmpf_eqn`, `watf_eqn`, `t_cbn_min`, `t_cbn_opt`, `t_cbn_max`, `bmix_a`, `bmix_b`, `bmix_c`, `tillmix_a`, `tillmix_b`, `tillmix_c`, `sfc_rsd_photodeg`, `n_act_frac`, `cnr_cap`, `cnr_ref`, `cpr_cap`, `cpr_ref`, `mathers_method`.

The first two records are consumed even if they are blank. Their contents are ignored, but the records must be present so the scalar data row starts on the third line.

## Parameters
| Parameter                   | Type      | Units   | Meaning                                                                                                                                           | Source                                         |                Reader line |
| --------------------------- | --------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------- | -------------------------: |
| `org_frac%frac_seq`         | `real`    | frac    | fraction of total carbon initialized into sequestered pools                                                                                       | [[carbon_module.f90#org_frac]]                 | [[carbon_bsn_read.f90]]:69 |
| `org_frac%frac_hum_microb`  | `real`    | frac    | fraction of sequestered carbon initialized into microbial biomass                                                                                 | [[carbon_module.f90#org_frac]]                 | [[carbon_bsn_read.f90]]:69 |
| `org_frac%frac_hum_slow`    | `real`    | frac    | fraction of sequestered carbon initialized into slow humus when `mathers_method` is off                                                           | [[carbon_module.f90#org_frac]]                 | [[carbon_bsn_read.f90]]:69 |
| `org_frac%frac_hum_passive` | `real`    | frac    | fraction of sequestered carbon initialized into passive humus                                                                                     | [[carbon_module.f90#org_frac]]                 | [[carbon_bsn_read.f90]]:69 |
| `cb_wtr_coef%prmt_21`       | `real`    |         | KOC FOR CARBON LOSS IN WATER AND SEDIMENT(500._1500.) KD = KOC * C                                                                                | [[carbon_module.f90#cb_wtr_coef]]              | [[carbon_bsn_read.f90]]:69 |
| `cb_wtr_coef%prmt_44`       | `real`    |         | RATIO OF SOLUBLE C CONCENTRATION IN RUNOFF TO PERCOLATE(0.1_1.)                                                                                   | [[carbon_module.f90#cb_wtr_coef]]              | [[carbon_bsn_read.f90]]:69 |
| `till_eff_days`             | `integer` |         | none \|length of days a tillage operation will have an effect                                                                                     | [[tillage_data_module.f90#till_eff_days]]      | [[carbon_bsn_read.f90]]:69 |
| `man_coef%rtof`             | `real`    | none    | input/calibration label `manure_c_frac`; partition factor used by manure and organic fertilizer routines, not the manure database carbon fraction | [[carbon_module.f90#man_coef]]                 | [[carbon_bsn_read.f90]]:69 |
| `bio_consf`                 | `real`    | none    | biological-mixing consolidation factor used while tillage effects are active                                                                      | [[tillage_data_module.f90#bio_consf]]          | [[carbon_bsn_read.f90]]:69 |
| `till_consf`                | `real`    | none    | tillage-mixing consolidation factor used while tillage effects are active                                                                         | [[tillage_data_module.f90#till_consf]]         | [[carbon_bsn_read.f90]]:69 |
| `org_con%tmpf`              | `integer` |         | temperature factor approach used in cbn_zhang2                                                                                                    | [[carbon_module.f90#org_con]]                  | [[carbon_bsn_read.f90]]:69 |
| `org_con%watf`              | `integer` |         | water factor approach used in cbn_zhang2                                                                                                          | [[carbon_module.f90#org_con]]                  | [[carbon_bsn_read.f90]]:69 |
| `org_con%tn`                | `real`    | celsius | minimum temperature bound                                                                                                                         | [[carbon_module.f90#org_con]]                  | [[carbon_bsn_read.f90]]:69 |
| `org_con%top`               | `real`    | celsius | peak (optimum) temperature                                                                                                                        | [[carbon_module.f90#org_con]]                  | [[carbon_bsn_read.f90]]:69 |
| `org_con%tx`                | `real`    | celsius | maximum temperature bound                                                                                                                         | [[carbon_module.f90#org_con]]                  | [[carbon_bsn_read.f90]]:69 |
| `bmix_a`                    | `real`    |         | none !Base intercept in zz equation in mgt_tillfactor.f90 for biomixing                                                                           | [[tillage_data_module.f90#bmix_a]]             | [[carbon_bsn_read.f90]]:69 |
| `bmix_b`                    | `real`    |         | none !slope of in zz equation in mgt_tillfactor.f90 for biomixing                                                                                 | [[tillage_data_module.f90#bmix_b]]             | [[carbon_bsn_read.f90]]:69 |
| `bmix_c`                    | `real`    |         | none !exponent multiplier in zz equation in mgt_tillfactor.f90 for biomixing                                                                      | [[tillage_data_module.f90#bmix_c]]             | [[carbon_bsn_read.f90]]:69 |
| `tillmix_a`                 | `real`    |         | none !Base intercept in zz equation in mgt_tillfactor.f90 for tillage mixing                                                                      | [[tillage_data_module.f90#tillmix_a]]          | [[carbon_bsn_read.f90]]:69 |
| `tillmix_b`                 | `real`    |         | none !slope of in zz equation in mgt_tillfactor.f90 for tillage mixing                                                                            | [[tillage_data_module.f90#tillmix_b]]          | [[carbon_bsn_read.f90]]:69 |
| `tillmix_c`                 | `real`    |         | none !exponent multiplier in zz equation in mgt_tillfactor.f90 for tillage mixing                                                                 | [[tillage_data_module.f90#tillmix_c]]          | [[carbon_bsn_read.f90]]:69 |
| `photo_degrade_factor`      | `real`    | none    | fraction to reduce surface residue due to photo degradation                                                                                       | [[plant_data_module.f90#photo_degrade_factor]] | [[carbon_bsn_read.f90]]:69 |
| `n_act_frac`                | `real`    | frac    | fraction of organic N in the active humus pool (used in nut_nminrl active to stable flow)                                                         | [[carbon_module.f90#n_act_frac]]               | [[carbon_bsn_read.f90]]:69 |
| `cnr_cap`                   | `real`    | none    | upper cap on residue C:N ratio before computing decomp factor                                                                                     | [[carbon_module.f90#cnr_cap]]                  | [[carbon_bsn_read.f90]]:69 |
| `cnr_ref`                   | `real`    | none    | reference C:N ratio where decomp factor equals 1                                                                                                  | [[carbon_module.f90#cnr_ref]]                  | [[carbon_bsn_read.f90]]:69 |
| `cpr_cap`                   | `real`    | none    | upper cap on residue C:P ratio before computing decomp factor                                                                                     | [[carbon_module.f90#cpr_cap]]                  | [[carbon_bsn_read.f90]]:69 |
| `cpr_ref`                   | `real`    | none    | reference C:P ratio where decomp factor equals 1                                                                                                  | [[carbon_module.f90#cpr_ref]]                  | [[carbon_bsn_read.f90]]:69 |
| `mathers_int`               | `integer` |         | 0/1 flag for org_frac%mathers_method                                                                                                              | `carbon_bsn_read.f90:44`                       | [[carbon_bsn_read.f90]]:69 |

## Ames_sub1 Example

The Ames_sub1 demo enables dynamic carbon with `codes.bsn` carbon = `2`, so this file and [[carbon_lyr.bsn]] are both required. The demo file at `VSProj/SWAT/Ames_sub1/carbon.bsn` matches `SWATPLUS/swatplus/refdata/Ames_sub1/carbon.bsn`.

```text
carbon.bsn: derived from carb_coefs.cbn (basin carbon scalars)
          init_seq       init_microb         init_slow      init_passive             koc_c        solc_ratio     till_eff_days     manure_c_frac        bio_consol       till_consol          tmpf_eqn          watf_eqn         t_cbn_min         t_cbn_opt         t_cbn_max            bmix_a            bmix_b            bmix_c         tillmix_a         tillmix_b         tillmix_c  sfc_rsd_photodeg        n_act_frac           cnr_cap           cnr_ref           cpr_cap           cpr_ref    mathers_method
              0.95              0.02              0.44              0.54            1000.0               0.5               100               0.5              0.15              0.10                 2                 1              -0.5              30.0              50.0               3.0               5.0              -5.5               3.0              15.0              -3.5             0.001              0.02             500.0              25.0            5000.0             200.0                 1
```

The demo row sets `mathers_method = 1`, so [[carbon_bsn_read.f90]] stores `org_frac%mathers_method = .true.` for the humus-slow pool initialization path in [[soil_nutcarb_init.f90]].

### Ames_sub1 Value Map

| File column | Reader target | Ames_sub1 value |
|---|---|---:|
| `init_seq` | `org_frac%frac_seq` | 0.95 |
| `init_microb` | `org_frac%frac_hum_microb` | 0.02 |
| `init_slow` | `org_frac%frac_hum_slow` | 0.44 |
| `init_passive` | `org_frac%frac_hum_passive` | 0.54 |
| `koc_c` | `cb_wtr_coef%prmt_21` | 1000.0 |
| `solc_ratio` | `cb_wtr_coef%prmt_44` | 0.5 |
| `till_eff_days` | `till_eff_days` | 100 |
| `manure_c_frac` | `man_coef%rtof` | 0.5 |
| `bio_consol` | `bio_consf` | 0.15 |
| `till_consol` | `till_consf` | 0.10 |
| `tmpf_eqn` | `org_con%tmpf` | 2 |
| `watf_eqn` | `org_con%watf` | 1 |
| `t_cbn_min` | `org_con%tn` | -0.5 |
| `t_cbn_opt` | `org_con%top` | 30.0 |
| `t_cbn_max` | `org_con%tx` | 50.0 |
| `bmix_a` | `bmix_a` | 3.0 |
| `bmix_b` | `bmix_b` | 5.0 |
| `bmix_c` | `bmix_c` | -5.5 |
| `tillmix_a` | `tillmix_a` | 3.0 |
| `tillmix_b` | `tillmix_b` | 15.0 |
| `tillmix_c` | `tillmix_c` | -3.5 |
| `sfc_rsd_photodeg` | `photo_degrade_factor` | 0.001 |
| `n_act_frac` | `n_act_frac` | 0.02 |
| `cnr_cap` | `cnr_cap` | 500.0 |
| `cnr_ref` | `cnr_ref` | 25.0 |
| `cpr_cap` | `cpr_cap` | 5000.0 |
| `cpr_ref` | `cpr_ref` | 200.0 |
| `mathers_method` | `org_frac%mathers_method` through `mathers_int` | 1 |

## Notes
- `carbon.bsn` is ignored when `bsn_cc%cswat` is not `2`.
- The legacy `cbn_diag` column is no longer part of this file. Carbon diagnostic output is controlled elsewhere.
- The scalar row has 28 values: 22 original basin scalars, 5 residue-decomposition tunables (`n_act_frac`, `cnr_cap`, `cnr_ref`, `cpr_cap`, `cpr_ref`), and the integer `mathers_method` flag.
- With `mathers_method = 1`, [[soil_nutcarb_init.f90]] initializes slow humus with the Mathers fraction, so `init_slow` is still read but is not the slow-humus initialization fraction for that run.
