---
title: bmpuser.str input file
kind: input-reference
status: partial
created: 2026-07-15
updated: 2026-07-15
source_revision: cb442f7c05fc3bfc34349c446010f452d2737ca0
scenario: Osu_1hru
tags: [inputs, reference, demo-context]
---

# `bmpuser.str`

## Purpose

User-defined BMP structural parameter database.

## Role In SWAT+

- Category: Structural.
- Usage class: `active scenario input`.
- Activation: `file.cio`.
- `Osu_1hru` status: `active`.
- Source inventory slot(s): `in_str%bmpuser_str = "bmpuser.str"`.

## File Format

SWAT+ input files use a plain-text, free-format layout with space-delimited values. GitBook documents the general convention as a title line first, then usually a header line, with exceptions such as `file.cio` and files that add count or block-header lines.
This file is controlled by the master `file.cio` manifest in normal runs. A non-`null` entry activates the selected filename; `null` means the file slot is intentionally unused for that scenario.

Local demo evidence from `VSProj/SWAT/Osu_1hru/bmpuser.str`:

- Title/comment line: `bmpuser.str: written by SWAT+ editor v2.2.0 on 2023-03-22 04:25 for SWAT+ rev.60.5.4`.
- Observed header line: `name                  flag       sed_eff      ptlp_eff      solp_eff      ptln_eff      soln_eff      bact_eff  description`.
- Nonblank records after the header: 1.
- First demo data record: `bmpusr1                  1       0.20000       0.20000       0.20000       0.20000       0.20000       0.20000`.

## Fields And Parameters

The table below is generated from the demo header. Meanings are practical working descriptions from the header name, local scenario context, and SWAT+ conventions; verify units and storage against the reader before citing them as final.

| Field | Working meaning | Demo value |
| --- | --- | --- |
| `name` | Record name used by other input files to reference this parameter set. | `bmpusr1` |
| `flag` | Switch or flag controlling how the record is interpreted. | `1` |
| `sed_eff` | Sediment-related value, efficiency, or parameter; verify units in the reader. | `0.20000` |
| `ptlp_eff` | Phosphorus-related component; verify units in the reader. | `0.20000` |
| `solp_eff` | Phosphorus-related component; verify units in the reader. | `0.20000` |
| `ptln_eff` | Removal efficiency or effect fraction/percent used by a practice or treatment. | `0.20000` |
| `soln_eff` | Removal efficiency or effect fraction/percent used by a practice or treatment. | `0.20000` |
| `bact_eff` | Pathogen/bacteria-related value or parameter; verify units in the reader. | `0.20000` |
| `description` | Free-text description retained for reader/user context. | - |

## Defaults And Conversions

- Defaults: use the source inventory filename and the `file.cio` slot state as the first default/activation check.
- Missing-file behavior: if the master file or upstream manifest uses `null`, SWAT+ treats that slot as inactive for the scenario.
- Numeric conversions: not yet traced for this page; inspect the reader for unit conversions, bounds checks, and derived runtime fields.

## Reader Path

- Source inventory: `SWATPLUS/swatplus/src/input_file_module.f90`.
- Source slot: `in_str%bmpuser_str` defaulting to `bmpuser.str`.
- Candidate reader/source files: `SWATPLUS/swatplus/src/scen_read_bmpuser.f90`.

## Downstream Consumers

Structural practice routines such as tile drains, filter strips, grassed waterways, septic systems, and BMP adjustments.

## Scenario Evidence

- Scenario: `VSProj/SWAT/Osu_1hru`.
- Scenario state: `active`.
- Activation evidence: `file.cio`.
- Local file evidence: `VSProj/SWAT/Osu_1hru/bmpuser.str`.

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
