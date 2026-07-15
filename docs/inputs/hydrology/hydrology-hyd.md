---
title: hydrology.hyd input file
kind: input-reference
status: partial
created: 2026-07-15
updated: 2026-07-15
source_revision: cb442f7c05fc3bfc34349c446010f452d2737ca0
scenario: Osu_1hru
tags: [inputs, reference, demo-context]
---

# `hydrology.hyd`

## Purpose

HRU hydrology parameter database, including ET, lateral flow, percolation, and related coefficients.

## Role In SWAT+

- Category: Hydrology.
- Usage class: `active scenario input`.
- Activation: `file.cio`.
- `Osu_1hru` status: `active`.
- Source inventory slot(s): `in_hyd%hydrol_hyd = "hydrology.hyd"`.

## File Format

SWAT+ input files use a plain-text, free-format layout with space-delimited values. GitBook documents the general convention as a title line first, then usually a header line, with exceptions such as `file.cio` and files that add count or block-header lines.
This file is controlled by the master `file.cio` manifest in normal runs. A non-`null` entry activates the selected filename; `null` means the file slot is intentionally unused for that scenario.

Local demo evidence from `VSProj/SWAT/Osu_1hru/hydrology.hyd`:

- Title/comment line: `hydrology.hyd: written by SWAT+ editor v2.2.0 on 2023-03-22 04:25 for SWAT+ rev.60.5.4`.
- Observed header line: `name                 lat_ttime       lat_sed       can_max          esco          epco   orgn_enrich   orgp_enrich       cn3_swf       bio_mix         perco      lat_orgn      lat_orgp      harg_pet       latq_co`.
- Nonblank records after the header: 1.
- First demo data record: `hyd0001                0.00000       0.00000       1.00000       0.95000       0.50000       0.00000       0.00000       0.95000       0.20000       0.90000       0.00000       0.00000       0.00000       0.01000`.

## Fields And Parameters

The table below is generated from the demo header. Meanings are practical working descriptions from the header name, local scenario context, and SWAT+ conventions; verify units and storage against the reader before citing them as final.

| Field | Working meaning | Demo value |
| --- | --- | --- |
| `name` | Record name used by other input files to reference this parameter set. | `hyd0001` |
| `lat_ttime` | Field named in the demo/source header; trace the reader for exact units and storage. | `0.00000` |
| `lat_sed` | Sediment-related value, efficiency, or parameter; verify units in the reader. | `0.00000` |
| `can_max` | Maximum value or upper bound, depending on the reader. | `1.00000` |
| `esco` | Field named in the demo/source header; trace the reader for exact units and storage. | `0.95000` |
| `epco` | Field named in the demo/source header; trace the reader for exact units and storage. | `0.50000` |
| `orgn_enrich` | Organic nitrogen component; verify units in the reader. | `0.00000` |
| `orgp_enrich` | Phosphorus-related component; verify units in the reader. | `0.00000` |
| `cn3_swf` | Curve-number or conservation-practice related value; verify in reader. | `0.95000` |
| `bio_mix` | Field named in the demo/source header; trace the reader for exact units and storage. | `0.20000` |
| `perco` | Field named in the demo/source header; trace the reader for exact units and storage. | `0.90000` |
| `lat_orgn` | Organic nitrogen component; verify units in the reader. | `0.00000` |
| `lat_orgp` | Phosphorus-related component; verify units in the reader. | `0.00000` |
| `harg_pet` | Field named in the demo/source header; trace the reader for exact units and storage. | `0.00000` |
| `latq_co` | Field named in the demo/source header; trace the reader for exact units and storage. | `0.01000` |

## Defaults And Conversions

- Defaults: use the source inventory filename and the `file.cio` slot state as the first default/activation check.
- Missing-file behavior: if the master file or upstream manifest uses `null`, SWAT+ treats that slot as inactive for the scenario.
- Numeric conversions: not yet traced for this page; inspect the reader for unit conversions, bounds checks, and derived runtime fields.

## Reader Path

- Source inventory: `SWATPLUS/swatplus/src/input_file_module.f90`.
- Source slot: `in_hyd%hydrol_hyd` defaulting to `hydrology.hyd`.
- Candidate reader/source files: `SWATPLUS/swatplus/src/hydrol_read.f90`.

## Downstream Consumers

Land-phase hydrology, topography, field geometry, and runoff/infiltration calculations.

## Scenario Evidence

- Scenario: `VSProj/SWAT/Osu_1hru`.
- Scenario state: `active`.
- Activation evidence: `file.cio`.
- Local file evidence: `VSProj/SWAT/Osu_1hru/hydrology.hyd`.

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
