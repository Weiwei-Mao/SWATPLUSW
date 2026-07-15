---
title: plants.plt input file
kind: input-reference
status: partial
created: 2026-07-15
updated: 2026-07-15
source_revision: cb442f7c05fc3bfc34349c446010f452d2737ca0
scenario: Osu_1hru
tags: [inputs, reference, demo-context]
---

# `plants.plt`

## Purpose

Plant parameter database.


## Official SWAT+ Reference

- Official page: [plants.plt](https://swatplus.gitbook.io/io-docs/introduction-1/databases/plants.plt).
- Official index note: The plant growth database file stores information required to simulate plant growth by plant species.
- Official field metadata available: 53 field row(s); matched to 53 of 54 observed demo header field(s).
- Demo cross-check: local header and first data row are still used below to show how this scenario instantiates the official format.

## Role In SWAT+

- Category: Databases.
- Usage class: `active scenario input`.
- Activation: `file.cio`.
- `Osu_1hru` status: `active`.
- Source inventory slot(s): `in_parmdb%plants_plt = "plants.plt"`.

## File Format

SWAT+ input files use a plain-text, free-format layout with space-delimited values. GitBook documents the general convention as a title line first, then usually a header line, with exceptions such as `file.cio` and files that add count or block-header lines.
This file is controlled by the master `file.cio` manifest in normal runs. A non-`null` entry activates the selected filename; `null` means the file slot is intentionally unused for that scenario.

Local demo evidence from `VSProj/SWAT/Osu_1hru/plants.plt`:

- Title/comment line: `plants.plt: written by SWAT+ editor v2.2.0 on 2023-03-22 04:25 for SWAT+ rev.60.5.4`.
- Observed header line: `name                      plnt_typ          gro_trig       nfix_co      days_mat          bm_e      harv_idx       lai_pot      frac_hu1      lai_max1      frac_hu2      lai_max2   hu_lai_decl     dlai_rate    can_ht_max     rt_dp_max       tmp_opt      tmp_base    frac_n_yld    frac_p_yld     frac_n_em     frac_n_50    frac_n_mat     frac_p_em     frac_p_50    frac_p_mat   harv_idx_ws    usle_c_min     stcon_max           vpd    frac_stcon        ru_vpd        co2_hi       bm_e_hi   plnt_decomp       lai_min   bm_tree_acc       yrs_mat   bm_tree_max        ext_co   leaf_tov_mn   leaf_tov_mx     bm_dieoff     rt_st_beg     rt_st_end     plnt_pop1     frac_lai1     plnt_pop2     frac_lai2   frac_sw_gro      aeration      wnd_dead      wnd_flat  description`.
- Nonblank records after the header: 261.
- First demo data record: `agrc                   cold_annual          temp_gro       0.00000     110.00000      30.00000       0.40000       4.00000       0.05000       0.05000       0.45000       0.95000       0.50000       1.00000       0.90000       1.30000      18.00000       0.00000       0.02500       0.00220       0.06630       0.02550       0.01480       0.00530       0.00200       0.00120       0.20000       0.03000       0.00600       4.00000       0.75000       6.00000     660.00000      39.00000       0.05000       0.00000       0.00000       0.00000       0.00000       0.65000      12.00000       3.00000       0.10000       0.00000       0.00000       0.00000       0.00000       0.00000       0.00000       0.50000       0.00000       0.00000       0.00000  agricultural_land_close_grown`.

## Fields And Parameters

The table merges the local demo header with official SWAT+ metadata when an official field definition is available. Rows marked `demo/source inferred` still need reader-level confirmation.

| Field | Meaning | Type | Unit | Default | Range | Demo value | Basis |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `name` | Name of the plant/landcover. | `string` | `n/a` | `n/a` | `n/a` | `agrc` | official GitBook |
| `plnt_typ` | Plant/landcover type. | `string` | `n/a` | `n/a` | `n/a` | `cold_annual` | official GitBook |
| `gro_trig` | Phenology trigger. | `string` | `n/a` | `n/a` | `n/a` | `temp_gro` | official GitBook |
| `nfix_co` | Nitrogen fixation coefficient. | `real` | `none` | `0.0` | `n/a` | `0.00000` | official GitBook |
| `days_mat` | Days to maturity. | `real` | `days` | `110.0` | `0.0-300.0` | `110.00000` | official GitBook |
| `bm_e` | Biomass-energy ratio. | `real` | `(kg/ha/(MJ/m^2)` | `15.0` | `10.0-90.0` | `30.00000` | official GitBook |
| `harv_idx` | Harvest index for optimal growth conditions. | `real` | `(kg/ha)/(kg/ha)` | `0.76` | `0.01-1.25` | `0.40000` | official GitBook |
| `lai_pot` | Maximum potential leaf area index. | `real` | `none` | `5.0` | `0.50-10.0` | `4.00000` | official GitBook |
| `frac_hu1` | Fraction of the growing season heat units corresponding to the 1st point on optimal leaf area development curve. | `real` | `fraction` | `0.05` | `0.0-1.0` | `0.05000` | official GitBook |
| `lai_max1` | Fraction of the maximum leaf area index corresponding to the 1st point on optimal leaf area development curve. | `real` | `fraction` | `0.05` | `0.0-1.0` | `0.05000` | official GitBook |
| `frac_hu2` | Fraction of the growing season heat units corresponding to the 2nd point on optimal leaf area development curve. | `real` | `fraction` | `0.40` | `0.0-1.0` | `0.45000` | official GitBook |
| `lai_max2` | Fraction of the maximum leaf area index corresponding to the 2nd point on optimal leaf area development curve. | `real` | `fraction` | `0.95` | `0.0-1.0` | `0.95000` | official GitBook |
| `hu_lai_decl` | Fraction of growing season when leaf area begins to decline. | `real` | `fraction` | `0.99` | `0.2-1.0` | `0.50000` | official GitBook |
| `dlai_rate` | Exponent that governs the LAI decline rate. | `real` | `n/a` | `1.0` | - | `1.00000` | official GitBook |
| `can_ht_max` | Maximum canopy height. | `real` | `m` | `6.0` | `0.1-20.0` | `0.90000` | official GitBook |
| `rt_dp_max` | Maximum rooting depth. | `real` | `m` | `3.50` | `0.0-3.0` | `1.30000` | official GitBook |
| `tmp_opt` | Optimal temperature for plant growth. | `real` | `deg c` | `30.0` | `11.0-38.0` | `18.00000` | official GitBook |
| `tmp_base` | Minimum temperature for plant growth. | `real` | `deg c` | `10.0` | `0.0-18.0` | `0.00000` | official GitBook |
| `frac_n_yld` | Normal fraction of N in yield. | `real` | `kg N/kg yield` | `0.0015` | `0.0015-0.075` | `0.02500` | official GitBook |
| `frac_p_yld` | Normal fraction of P in yield. | `real` | `kg P/kg yield` | `0.0003` | `0.0015-0.0075` | `0.00220` | official GitBook |
| `frac_n_em` | Normal fraction of N in plant biomass at emergence. | `real` | `kg N/kg biomass` | `0.006` | `0.004-0.07` | `0.06630` | official GitBook |
| `frac_n_50` | Normal fraction of N in plant biomass at 50% maturity. | `real` | `kg N/kg biomass` | `0.002` | `0.002-0.05` | `0.02550` | official GitBook |
| `frac_n_mat` | Normal fraction of N in plant biomass at maturity. | `real` | `kg N/kg biomass` | `0.0015` | `0.001-0.27` | `0.01480` | official GitBook |
| `frac_p_em` | Normal fraction pf P in plant biomass at emergence. | `real` | `kg P/kg biomass` | `0.0007` | `0.0005-0.01` | `0.00530` | official GitBook |
| `frac_p_50` | Normal fraction of P in plant at 50% maturity. | `real` | `kg P/kg biomass` | `0.0004` | `0.0002-0.007` | `0.00200` | official GitBook |
| `frac_p_mat` | Normal fraction of P in plant at maturity. | `real` | `kg P/kg biomass` | `0.0003` | `0.0003-0.0004` | `0.00120` | official GitBook |
| `harv_idx_ws` | Harvest index that represents the lowest harvest index expected due to water stress. | `real` | `(kg/ha)/(kg/ha)` | `0.01` | `-0.2-1.1` | `0.20000` | official GitBook |
| `usle_c_min` | Minimum value of the USLE C factor for water erosion. | `real` | `none` | `0.001` | `0.001-0.50` | `0.03000` | official GitBook |
| `stcon_max` | Maximum stomatal conductance. | `real` | `m/s` | `0.002` | `0.0-0.50` | `0.00600` | official GitBook |
| `vpd` | Vapor pressure deficit corresponding to the 2nd point on the stomatal conductance curve. | `real` | `kPa` | `4.0` | `1.5-6.0` | `4.00000` | official GitBook |
| `frac_stcon` | Fraction of maximum stomatal conductance corresponding to the 2nd point on the stomatal conductance curve. | `read` | `fraction` | `0.75` | `0.0-1.0` | `0.75000` | official GitBook |
| `ru_vpd` | Rate of decline in radiation use efficiency per unit increase in vapor pressure deficit. | `real` | `none` | `8.0` | `0.0-50.0` | `6.00000` | official GitBook |
| `co2_hi` | Elevated CO2 atmospheric concentration corresponding the 2nd point on the radiation use efficiency curve. | `real` | `uL CO2/L air` | `660.0` | `300.0-1000.0` | `660.00000` | official GitBook |
| `bm_e_hi` | Biomass-energy ratio corresponding to the 2nd point on the radiation use efficiency curve. | `real` | `(kg/ha)/(MJ/m^2)` | `16.0` | `5.0-100.0` | `39.00000` | official GitBook |
| `plnt_decomp` | Plant residue decomposition coefficient. | `real` | `none` | `0.05` | `0.01-0.099` | `0.05000` | official GitBook |
| `lai_min` | Minimum LAI during dormant period. | `real` | `m^2/m^2` | `0.75` | `0.00-0.99` | `0.00000` | official GitBook |
| `bm_tree_acc` | Fraction of biomass accumulated each year. | `real` | `fraction` | `0.30` | `0.0-1.0` | `0.00000` | official GitBook |
| `yrs_mat` | Years to maturity. | `integer` | `years` | `10` | `0-100` | `0.00000` | official GitBook |
| `bm_tree_max` | Maximum forest biomass. | `real` | `metric tons/ha` | `1000.0` | `0.0-5000.0` | `0.00000` | official GitBook |
| `ext_co` | Light extinction coefficient. | `real` | `none` | `0.65` | `0.0-2.0` | `0.65000` | official GitBook |
| `leaf_tov_mn` | Perennial leaf turnover rate with minimum stress. | `real` | - | `12.0` | - | `12.00000` | official GitBook |
| `leaf_tov_mx` | Perennial leaf turnover rate with maximum stress. | `real` | - | `3.0` | - | `3.00000` | official GitBook |
| `bm_dieoff` | Above-ground biomass that dies off at dormancy. | `real` | `fraction` | `1.0` | `0.0-1.0` | `0.10000` | official GitBook |
| `rt_st_beg` | Root to shoot ratio at the beginning of the growing season. | `real` | `fraction` | `0.` | - | `0.00000` | official GitBook |
| `rt_st_end` | Root to shoot ratio at the end of the growing season. | `real` | `fraction` | `0.` | - | `0.00000` | official GitBook |
| `plnt_pop1` | Plant population corresponding to the 1st point on the population LAI curve. | `real` | `plants/m^2` | `0.` | - | `0.00000` | official GitBook |
| `frac_lai1` | Fraction of the maximum leaf area index corresponding to the 1st point on the leaf area development curve. | `real` | `fraction` | `0.` | `0.0-1.0` | `0.00000` | official GitBook |
| `plnt_pop2` | Plant population corresponding to the 2nd point on the population LAI curve. | `real` | `plants/m^2` | `0.0` | - | `0.00000` | official GitBook |
| `frac_lai2` | Fraction of the maximum leaf area index corresponding to the 2nd point on the leaf area development curve. | `real` | `fraction` | `0.0` | `0.0-1.0` | `0.00000` | official GitBook |
| `frac_sw_gro` | Fraction of field capacity to initiate growth of tropical plants during monsoon season. | `real` | `fraction` | `0.5` | `0.0-1.0` | `0.50000` | official GitBook |
| `aeration` | Aeration stress factor. | `real` | - | `0.0` | - | `0.00000` | official GitBook |
| `wnd_dead` | Residue factor for percent cover equation. | `real` | - | `0.0` | - | `0.00000` | official GitBook |
| `wnd_flat` | Residue factor for surface cover (C factor) equation. | `real` | - | `0.0` | - | `0.00000` | official GitBook |
| `description` | Header field observed in the demo file; trace the reader for exact storage and constraints. | - | - | - | - | `agricultural_land_close_grown` | demo/source inferred |

## Defaults And Conversions

- Defaults: use the source inventory filename and the `file.cio` slot state as the first default/activation check.
- Missing-file behavior: if the master file or upstream manifest uses `null`, SWAT+ treats that slot as inactive for the scenario.
- Numeric conversions: not yet traced for this page; inspect the reader for unit conversions, bounds checks, and derived runtime fields.

## Reader Path

- Source inventory: `SWATPLUS/swatplus/src/input_file_module.f90`.
- Source slot: `in_parmdb%plants_plt` defaulting to `plants.plt`.
- Candidate reader/source files: `SWATPLUS/swatplus/src/plant_parm_read.f90`.

## Downstream Consumers

Reusable parameter databases referenced by management, land-use, constituent, and operation records.

## Scenario Evidence

- Scenario: `VSProj/SWAT/Osu_1hru`.
- Scenario state: `active`.
- Activation evidence: `file.cio`.
- Local file evidence: `VSProj/SWAT/Osu_1hru/plants.plt`.

## Open Questions

- Which exact reader routine stores each field, and in which derived type or module variable?
- Which units, valid ranges, and default substitutions are enforced in that reader?
- Which routines consume each parsed value after initialization?

## External References

- [SWAT+ Input File Format](https://swatplus.gitbook.io/io-docs/introduction-1/input-file-format)
- [SWAT+ master file `file.cio`](https://swatplus.gitbook.io/io-docs/introduction-1/master-file-file.cio)
- [SWAT+ simulation settings](https://swatplus.gitbook.io/io-docs/introduction-1/simulation-settings)

## Related Files

- [SWAT+ input files map](../../input-files.md)
- [SWAT+ tracing guide](../../tracing-guide.md)
- [Master input manifest](../simulation/file-cio.md)
