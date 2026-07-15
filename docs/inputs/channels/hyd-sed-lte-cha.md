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


## Official SWAT+ Reference

- Official page: [hyd-sed-lte.cha](https://swatplus.gitbook.io/io-docs/introduction-1/channels/hyd-sed-lte.cha).
- Official index note: This file controls the channel hydrology and sediment properties.
- Official field metadata available: 22 field row(s); matched to 21 of 24 observed demo header field(s).
- Demo cross-check: local header and first data row are still used below to show how this scenario instantiates the official format.

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

The table merges the local demo header with official SWAT+ metadata when an official field definition is available. Rows marked `demo/source inferred` still need reader-level confirmation.

| Field | Meaning | Type | Unit | Default | Range | Demo value | Basis |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `name` | Name of the channel hydrology and sediment record. | - | - | - | - | `hydcha01` | official GitBook |
| `order` | Header field observed in the demo file; trace the reader for exact storage and constraints. | - | - | - | - | `4` | demo/source inferred |
| `wd` | Channel width. | - | - | - | - | `27.17726` | official GitBook |
| `dp` | Channel depth. | - | - | - | - | `0.99164` | official GitBook |
| `slp` | Channel slope. | - | - | - | - | `0.00146` | official GitBook |
| `len` | Channel length. | - | - | - | - | `3.42760` | official GitBook |
| `mann` | Channel Manning's n value. | - | - | - | - | `0.05000` | official GitBook |
| `k` | Effective hydraulic conductivity of the channel alluvium. | - | - | - | - | `5.00000` | official GitBook |
| `erod_fact` | Channel erodibility factor. | - | - | - | - | `0.01000` | official GitBook |
| `cov_fact` | Channel cover factor. | - | - | - | - | `0.00500` | official GitBook |
| `wd_rto` | Header field observed in the demo file; trace the reader for exact storage and constraints. | - | - | - | - | `27.40638` | demo/source inferred |
| `eq_slp` | Equilibrium channel slope. | - | - | - | - | `0.00100` | official GitBook |
| `d50` | Channel median sediment size. | - | - | - | - | `12.00000` | official GitBook |
| `clay` | Clay content of channel bank and bed. | - | - | - | - | `50.00000` | official GitBook |
| `carbon` | Carbon content of channel bank and bed. | - | - | - | - | `0.04000` | official GitBook |
| `dry_bd` | Dry bulk density of the channel. | - | - | - | - | `1.00000` | official GitBook |
| `side_slp` | Channel side slope. | - | - | - | - | `0.50000` | official GitBook |
| `bed_load` | Percent of sediment entering the channel that is bed material. | - | - | - | - | `0.50000` | official GitBook |
| `fps` | Floodplain slope. | - | - | - | - | `0.00001` | official GitBook |
| `fpn` | Floodplain Manning's n. | - | - | - | - | `0.10000` | official GitBook |
| `n_conc` | Nitrogen concentration in channel bank. | - | - | - | - | `0.00000` | official GitBook |
| `p_conc` | Phosphorus concentration in channel bank. | - | - | - | - | `0.00000` | official GitBook |
| `p_bio` | Fraction of phosphorus in bank that is bioavailable. | - | - | - | - | `0.00000` | official GitBook |
| `description` | Header field observed in the demo file; trace the reader for exact storage and constraints. | - | - | - | - | - | demo/source inferred |

Additional official field rows that are not part of the observed demo header:

| Field | Meaning | Type | Unit |
| --- | --- | --- | --- |
| `sinu` | Channel sinuosity. | - | - |

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
