---
title: aquifer.aqu input file
kind: input-reference
status: partial
created: 2026-07-15
updated: 2026-07-15
source_revision: cb442f7c05fc3bfc34349c446010f452d2737ca0
scenario: Osu_1hru
tags: [inputs, reference, demo-context]
---

# `aquifer.aqu`

## Purpose

Lumped aquifer parameter database.

## Role In SWAT+

- Category: Aquifers.
- Usage class: `active scenario input`.
- Activation: `file.cio`.
- `Osu_1hru` status: `active`.
- Source inventory slot(s): `in_aqu%aqu = "aquifer.aqu"`.

## File Format

SWAT+ input files use a plain-text, free-format layout with space-delimited values. GitBook documents the general convention as a title line first, then usually a header line, with exceptions such as `file.cio` and files that add count or block-header lines.
This file is controlled by the master `file.cio` manifest in normal runs. A non-`null` entry activates the selected filename; `null` means the file slot is intentionally unused for that scenario.

Local demo evidence from `VSProj/SWAT/Osu_1hru/aquifer.aqu`:

- Title/comment line: `aquifer.aqu: written by SWAT+ editor v2.2.0 on 2023-03-22 04:25 for SWAT+ rev.60.5.4`.
- Observed header line: `id  name                          init        gw_flo       dep_bot        dep_wt         no3_n         sol_p        carbon      flo_dist        bf_max      alpha_bf         revap       rchg_dp      spec_yld       hl_no3n       flo_min     revap_min`.
- Nonblank records after the header: 21.
- First demo data record: `1  aqu011                    initaqu1       0.05000      10.00000       6.00000       0.00000       0.00000       0.50000      50.00000       1.00000       0.95000       0.02000       0.01000       0.05000       0.00000       5.00000       5.00000`.

## Fields And Parameters

The table below is generated from the demo header. Meanings are practical working descriptions from the header name, local scenario context, and SWAT+ conventions; verify units and storage against the reader before citing them as final.

| Field | Working meaning | Demo value |
| --- | --- | --- |
| `id` | Numeric record identifier. | `1` |
| `name` | Record name used by other input files to reference this parameter set. | `aqu011` |
| `init` | Initial value/state used at model startup. | `initaqu1` |
| `gw_flo` | Flow-related value or routing parameter. | `0.05000` |
| `dep_bot` | Depth, deposition, or dependency field; verify exact meaning in the reader. | `10.00000` |
| `dep_wt` | Depth, deposition, or dependency field; verify exact meaning in the reader. | `6.00000` |
| `no3_n` | Nitrate-nitrogen concentration, mass, or parameter component; verify units in the reader. | `0.00000` |
| `sol_p` | Field named in the demo/source header; trace the reader for exact units and storage. | `0.00000` |
| `carbon` | Field named in the demo/source header; trace the reader for exact units and storage. | `0.50000` |
| `flo_dist` | Flow-related value or routing parameter. | `50.00000` |
| `bf_max` | Maximum value or upper bound, depending on the reader. | `1.00000` |
| `alpha_bf` | Field named in the demo/source header; trace the reader for exact units and storage. | `0.95000` |
| `revap` | Field named in the demo/source header; trace the reader for exact units and storage. | `0.02000` |
| `rchg_dp` | Field named in the demo/source header; trace the reader for exact units and storage. | `0.01000` |
| `spec_yld` | Field named in the demo/source header; trace the reader for exact units and storage. | `0.05000` |
| `hl_no3n` | Nitrate-nitrogen concentration, mass, or parameter component; verify units in the reader. | `0.00000` |
| `flo_min` | Flow-related value or routing parameter. | `5.00000` |
| `revap_min` | Minimum value or lower bound, depending on the reader. | `5.00000` |

## Defaults And Conversions

- Defaults: use the source inventory filename and the `file.cio` slot state as the first default/activation check.
- Missing-file behavior: if the master file or upstream manifest uses `null`, SWAT+ treats that slot as inactive for the scenario.
- Numeric conversions: not yet traced for this page; inspect the reader for unit conversions, bounds checks, and derived runtime fields.

## Reader Path

- Source inventory: `SWATPLUS/swatplus/src/input_file_module.f90`.
- Source slot: `in_aqu%aqu` defaulting to `aquifer.aqu`.
- Candidate reader/source files: `SWATPLUS/swatplus/src/aqu_read.f90`.

## Downstream Consumers

Aquifer initialization, groundwater storage, and groundwater routing routines.

## Scenario Evidence

- Scenario: `VSProj/SWAT/Osu_1hru`.
- Scenario state: `active`.
- Activation evidence: `file.cio`.
- Local file evidence: `VSProj/SWAT/Osu_1hru/aquifer.aqu`.

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
