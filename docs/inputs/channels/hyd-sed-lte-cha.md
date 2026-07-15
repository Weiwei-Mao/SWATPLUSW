---
title: hyd-sed-lte.cha input file
kind: input-reference
status: partial
created: 2026-07-15
updated: 2026-07-15
source_revision: cb442f7c05fc3bfc34349c446010f452d2737ca0
scenario: Osu_1hru
tags: [inputs, reference, demo-context]
---

# `hyd-sed-lte.cha`

## Purpose

SWAT-DEG hydrology/sediment control parameters.

## Role In SWAT+

- Category: Channels.
- Usage class: `active scenario input`.
- Activation: `file.cio`.
- `Osu_1hru` status: `active`.
- Source inventory slot(s): `in_cha%hyd_sed = "hyd-sed-lte.cha"`.

## File Format

SWAT+ input files use a plain-text, free-format layout with space-delimited values. GitBook documents the general convention as a title line first, then usually a header line, with exceptions such as `file.cio` and files that add count or block-header lines.
This file is controlled by the master `file.cio` manifest in normal runs. A non-`null` entry activates the selected filename; `null` means the file slot is intentionally unused for that scenario.

Local demo evidence from `VSProj/SWAT/Osu_1hru/hyd-sed-lte.cha`:

- Title/comment line: `hyd-sed-lte.cha: written by SWAT+ editor v2.2.0 on 2023-03-22 04:25 for SWAT+ rev.60.5.4`.
- Observed header line: `name                         order            wd            dp           slp           len          mann             k     erod_fact      cov_fact        wd_rto        eq_slp           d50          clay        carbon        dry_bd      side_slp      bed_load           fps           fpn        n_conc        p_conc         p_bio  description`.
- Nonblank records after the header: 57.
- First demo data record: `hydcha01                         4      27.17726       0.99164       0.00146       3.42760       0.05000       5.00000       0.01000       0.00500      27.40638       0.00100      12.00000      50.00000       0.04000       1.00000       0.50000       0.50000       0.00001       0.10000       0.00000       0.00000       0.00000`.

## Fields And Parameters

The table below is generated from the demo header. Meanings are practical working descriptions from the header name, local scenario context, and SWAT+ conventions; verify units and storage against the reader before citing them as final.

| Field | Working meaning | Demo value |
| --- | --- | --- |
| `name` | Record name used by other input files to reference this parameter set. | `hydcha01` |
| `order` | Field named in the demo/source header; trace the reader for exact units and storage. | `4` |
| `wd` | Field named in the demo/source header; trace the reader for exact units and storage. | `27.17726` |
| `dp` | Field named in the demo/source header; trace the reader for exact units and storage. | `0.99164` |
| `slp` | Field named in the demo/source header; trace the reader for exact units and storage. | `0.00146` |
| `len` | Field named in the demo/source header; trace the reader for exact units and storage. | `3.42760` |
| `mann` | Field named in the demo/source header; trace the reader for exact units and storage. | `0.05000` |
| `k` | Field named in the demo/source header; trace the reader for exact units and storage. | `5.00000` |
| `erod_fact` | Field named in the demo/source header; trace the reader for exact units and storage. | `0.01000` |
| `cov_fact` | Field named in the demo/source header; trace the reader for exact units and storage. | `0.00500` |
| `wd_rto` | Field named in the demo/source header; trace the reader for exact units and storage. | `27.40638` |
| `eq_slp` | Field named in the demo/source header; trace the reader for exact units and storage. | `0.00100` |
| `d50` | Field named in the demo/source header; trace the reader for exact units and storage. | `12.00000` |
| `clay` | Field named in the demo/source header; trace the reader for exact units and storage. | `50.00000` |
| `carbon` | Field named in the demo/source header; trace the reader for exact units and storage. | `0.04000` |
| `dry_bd` | Field named in the demo/source header; trace the reader for exact units and storage. | `1.00000` |
| `side_slp` | Field named in the demo/source header; trace the reader for exact units and storage. | `0.50000` |
| `bed_load` | Field named in the demo/source header; trace the reader for exact units and storage. | `0.50000` |
| `fps` | Field named in the demo/source header; trace the reader for exact units and storage. | `0.00001` |
| `fpn` | Field named in the demo/source header; trace the reader for exact units and storage. | `0.10000` |
| `n_conc` | Concentration value; verify constituent and units in the reader. | `0.00000` |
| `p_conc` | Concentration value; verify constituent and units in the reader. | `0.00000` |
| `p_bio` | Field named in the demo/source header; trace the reader for exact units and storage. | `0.00000` |
| `description` | Free-text description retained for reader/user context. | - |

## Defaults And Conversions

- Defaults: use the source inventory filename and the `file.cio` slot state as the first default/activation check.
- Missing-file behavior: if the master file or upstream manifest uses `null`, SWAT+ treats that slot as inactive for the scenario.
- Numeric conversions: not yet traced for this page; inspect the reader for unit conversions, bounds checks, and derived runtime fields.

## Reader Path

- Source inventory: `SWATPLUS/swatplus/src/input_file_module.f90`.
- Source slot: `in_cha%hyd_sed` defaulting to `hyd-sed-lte.cha`.
- Candidate reader/source files: `SWATPLUS/swatplus/src/sd_hydsed_read.f90`.

## Downstream Consumers

Channel or SWAT-DEG channel hydrology, sediment, nutrient, and initialization routines.

## Scenario Evidence

- Scenario: `VSProj/SWAT/Osu_1hru`.
- Scenario state: `active`.
- Activation evidence: `file.cio`.
- Local file evidence: `VSProj/SWAT/Osu_1hru/hyd-sed-lte.cha`.

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
