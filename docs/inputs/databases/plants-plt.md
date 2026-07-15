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

The table below is generated from the demo header. Meanings are practical working descriptions from the header name, local scenario context, and SWAT+ conventions; verify units and storage against the reader before citing them as final.

| Field | Working meaning | Demo value |
| --- | --- | --- |
| `name` | Record name used by other input files to reference this parameter set. | `agrc` |
| `plnt_typ` | Field named in the demo/source header; trace the reader for exact units and storage. | `cold_annual` |
| `gro_trig` | Field named in the demo/source header; trace the reader for exact units and storage. | `temp_gro` |
| `nfix_co` | Field named in the demo/source header; trace the reader for exact units and storage. | `0.00000` |
| `days_mat` | Field named in the demo/source header; trace the reader for exact units and storage. | `110.00000` |
| `bm_e` | Field named in the demo/source header; trace the reader for exact units and storage. | `30.00000` |
| `harv_idx` | Field named in the demo/source header; trace the reader for exact units and storage. | `0.40000` |
| `lai_pot` | Leaf-area-index related value. | `4.00000` |
| `frac_hu1` | Field named in the demo/source header; trace the reader for exact units and storage. | `0.05000` |
| `lai_max1` | Maximum value or upper bound, depending on the reader. | `0.05000` |
| `frac_hu2` | Field named in the demo/source header; trace the reader for exact units and storage. | `0.45000` |
| `lai_max2` | Maximum value or upper bound, depending on the reader. | `0.95000` |
| `hu_lai_decl` | Leaf-area-index related value. | `0.50000` |
| `dlai_rate` | Leaf-area-index related value. | `1.00000` |
| `can_ht_max` | Maximum value or upper bound, depending on the reader. | `0.90000` |
| `rt_dp_max` | Maximum value or upper bound, depending on the reader. | `1.30000` |
| `tmp_opt` | Field named in the demo/source header; trace the reader for exact units and storage. | `18.00000` |
| `tmp_base` | Field named in the demo/source header; trace the reader for exact units and storage. | `0.00000` |
| `frac_n_yld` | Field named in the demo/source header; trace the reader for exact units and storage. | `0.02500` |
| `frac_p_yld` | Field named in the demo/source header; trace the reader for exact units and storage. | `0.00220` |
| `frac_n_em` | Field named in the demo/source header; trace the reader for exact units and storage. | `0.06630` |
| `frac_n_50` | Field named in the demo/source header; trace the reader for exact units and storage. | `0.02550` |
| `frac_n_mat` | Field named in the demo/source header; trace the reader for exact units and storage. | `0.01480` |
| `frac_p_em` | Field named in the demo/source header; trace the reader for exact units and storage. | `0.00530` |
| `frac_p_50` | Field named in the demo/source header; trace the reader for exact units and storage. | `0.00200` |
| `frac_p_mat` | Field named in the demo/source header; trace the reader for exact units and storage. | `0.00120` |
| `harv_idx_ws` | Field named in the demo/source header; trace the reader for exact units and storage. | `0.20000` |
| `usle_c_min` | Minimum value or lower bound, depending on the reader. | `0.03000` |
| `stcon_max` | Maximum value or upper bound, depending on the reader. | `0.00600` |
| `vpd` | Field named in the demo/source header; trace the reader for exact units and storage. | `4.00000` |
| `frac_stcon` | Field named in the demo/source header; trace the reader for exact units and storage. | `0.75000` |
| `ru_vpd` | Field named in the demo/source header; trace the reader for exact units and storage. | `6.00000` |
| `co2_hi` | Field named in the demo/source header; trace the reader for exact units and storage. | `660.00000` |
| `bm_e_hi` | Field named in the demo/source header; trace the reader for exact units and storage. | `39.00000` |
| `plnt_decomp` | Field named in the demo/source header; trace the reader for exact units and storage. | `0.05000` |
| `lai_min` | Minimum value or lower bound, depending on the reader. | `0.00000` |
| `bm_tree_acc` | Field named in the demo/source header; trace the reader for exact units and storage. | `0.00000` |
| `yrs_mat` | Calendar year or year range value. | `0.00000` |
| `bm_tree_max` | Maximum value or upper bound, depending on the reader. | `0.00000` |
| `ext_co` | Field named in the demo/source header; trace the reader for exact units and storage. | `0.65000` |

Only the first 40 header fields are shown here because the demo header is long; inspect `VSProj/SWAT/Osu_1hru/plants.plt` for the remaining fields.

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
