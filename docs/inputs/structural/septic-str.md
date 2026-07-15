---
title: septic.str input file
kind: input-reference
status: partial
created: 2026-07-15
updated: 2026-07-15
source_revision: cb442f7c05fc3bfc34349c446010f452d2737ca0
scenario: Osu_1hru
tags: [inputs, reference, demo-context]
---

# `septic.str`

## Purpose

Structural septic-system setup file.

## Role In SWAT+

- Category: Structural.
- Usage class: `active scenario input`.
- Activation: `file.cio`.
- `Osu_1hru` status: `active`.
- Source inventory slot(s): `in_str%septic_str = "septic.str"`.

## File Format

SWAT+ input files use a plain-text, free-format layout with space-delimited values. GitBook documents the general convention as a title line first, then usually a header line, with exceptions such as `file.cio` and files that add count or block-header lines.
This file is controlled by the master `file.cio` manifest in normal runs. A non-`null` entry activates the selected filename; `null` means the file slot is intentionally unused for that scenario.

Local demo evidence from `VSProj/SWAT/Osu_1hru/septic.str`:

- Title/comment line: `septic.str: written by SWAT+ editor v2.2.0 on 2023-03-22 04:25 for SWAT+ rev.60.5.4`.
- Observed header line: `name                   typ        yr  operation     residents          area    t_fail       dp_bioz      thk_bioz      cha_dist      sep_dens       bm_dens     bod_decay      bod_conv        fc_lin        fc_exp   fecal_decay      tds_conv          mort          resp       slough1       slough2           nit         denit        p_sorp    p_sorp_max      solp_slp      solp_int`.
- Nonblank records after the header: 2.
- First demo data record: `standard                 1         0         0       2.50000     100.00000        70     500.00000      50.00000       0.50000       1.50000    1000.00000       0.50000       0.32000      30.00000       0.80000       1.30000       0.10000       0.50000       0.16000       0.30000       0.50000       1.50000       0.32000     128.00000     850.00000       0.04000       3.10000`.

## Fields And Parameters

The table below is generated from the demo header. Meanings are practical working descriptions from the header name, local scenario context, and SWAT+ conventions; verify units and storage against the reader before citing them as final.

| Field | Working meaning | Demo value |
| --- | --- | --- |
| `name` | Record name used by other input files to reference this parameter set. | `standard` |
| `typ` | Field named in the demo/source header; trace the reader for exact units and storage. | `1` |
| `yr` | Calendar year or year range value. | `0` |
| `operation` | Field named in the demo/source header; trace the reader for exact units and storage. | `0` |
| `residents` | Reservoir-related parameter or object reference. | `2.50000` |
| `area` | Area represented by the object or record. | `100.00000` |
| `t_fail` | Field named in the demo/source header; trace the reader for exact units and storage. | `70` |
| `dp_bioz` | Field named in the demo/source header; trace the reader for exact units and storage. | `500.00000` |
| `thk_bioz` | Field named in the demo/source header; trace the reader for exact units and storage. | `50.00000` |
| `cha_dist` | Channel-related parameter or object reference. | `0.50000` |
| `sep_dens` | Field named in the demo/source header; trace the reader for exact units and storage. | `1.50000` |
| `bm_dens` | Field named in the demo/source header; trace the reader for exact units and storage. | `1000.00000` |
| `bod_decay` | Field named in the demo/source header; trace the reader for exact units and storage. | `0.50000` |
| `bod_conv` | Field named in the demo/source header; trace the reader for exact units and storage. | `0.32000` |
| `fc_lin` | Field named in the demo/source header; trace the reader for exact units and storage. | `30.00000` |
| `fc_exp` | Field named in the demo/source header; trace the reader for exact units and storage. | `0.80000` |
| `fecal_decay` | Field named in the demo/source header; trace the reader for exact units and storage. | `1.30000` |
| `tds_conv` | Field named in the demo/source header; trace the reader for exact units and storage. | `0.10000` |
| `mort` | Field named in the demo/source header; trace the reader for exact units and storage. | `0.50000` |
| `resp` | Reservoir-related parameter or object reference. | `0.16000` |
| `slough1` | Field named in the demo/source header; trace the reader for exact units and storage. | `0.30000` |
| `slough2` | Field named in the demo/source header; trace the reader for exact units and storage. | `0.50000` |
| `nit` | Field named in the demo/source header; trace the reader for exact units and storage. | `1.50000` |
| `denit` | Field named in the demo/source header; trace the reader for exact units and storage. | `0.32000` |
| `p_sorp` | Field named in the demo/source header; trace the reader for exact units and storage. | `128.00000` |
| `p_sorp_max` | Maximum value or upper bound, depending on the reader. | `850.00000` |
| `solp_slp` | Phosphorus-related component; verify units in the reader. | `0.04000` |
| `solp_int` | Phosphorus-related component; verify units in the reader. | `3.10000` |

## Defaults And Conversions

- Defaults: use the source inventory filename and the `file.cio` slot state as the first default/activation check.
- Missing-file behavior: if the master file or upstream manifest uses `null`, SWAT+ treats that slot as inactive for the scenario.
- Numeric conversions: not yet traced for this page; inspect the reader for unit conversions, bounds checks, and derived runtime fields.

## Reader Path

- Source inventory: `SWATPLUS/swatplus/src/input_file_module.f90`.
- Source slot: `in_str%septic_str` defaulting to `septic.str`.
- Candidate reader/source files: `SWATPLUS/swatplus/src/sep_read.f90`.

## Downstream Consumers

Structural practice routines such as tile drains, filter strips, grassed waterways, septic systems, and BMP adjustments.

## Scenario Evidence

- Scenario: `VSProj/SWAT/Osu_1hru`.
- Scenario state: `active`.
- Activation evidence: `file.cio`.
- Local file evidence: `VSProj/SWAT/Osu_1hru/septic.str`.

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
