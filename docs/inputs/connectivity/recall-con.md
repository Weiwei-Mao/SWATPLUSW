---
title: recall.con input file
kind: input-reference
status: partial
created: 2026-07-15
updated: 2026-07-15
source_revision: cb442f7c05fc3bfc34349c446010f452d2737ca0
scenario: Osu_1hru
tags: [inputs, reference, demo-context]
---

# `recall.con`

## Purpose

Recall-object connection file; defines routing for external time-series hydrographs.

## Role In SWAT+

- Category: Connectivity.
- Usage class: `active scenario input`.
- Activation: `file.cio`.
- `Osu_1hru` status: `active`.
- Source inventory slot(s): `in_con%rec_con = "recall.con"`.

## File Format

SWAT+ input files use a plain-text, free-format layout with space-delimited values. GitBook documents the general convention as a title line first, then usually a header line, with exceptions such as `file.cio` and files that add count or block-header lines.
This file is controlled by the master `file.cio` manifest in normal runs. A non-`null` entry activates the selected filename; `null` means the file slot is intentionally unused for that scenario.

Local demo evidence from `VSProj/SWAT/Osu_1hru/recall.con`:

- Title/comment line: `recall.con (2-stage)`.
- Observed header line: `NUMB    NAME    GIS_ID    AREA_HA      LAT     LONG       ELEV    RECALL     WST   CONSTIT  OVERFLOW  RULESET OUT_TOT OBTYP_OUT1 HTYPNO_OUT1  HTYP_OUT1  FRAC_OUT1`.
- Nonblank records after the header: 1.
- First demo data record: `1  inflow      1        0.000    31.734   -83.720     0.000      1    wea1         0         0        0       1         sdc          1        tot     1.0000`.

## Fields And Parameters

The table below is generated from the demo header. Meanings are practical working descriptions from the header name, local scenario context, and SWAT+ conventions; verify units and storage against the reader before citing them as final.

| Field | Working meaning | Demo value |
| --- | --- | --- |
| `NUMB` | Count of following records or related objects. | `1` |
| `NAME` | Record name or target name used by the calibration/update reader. | `inflow` |
| `GIS_ID` | Field named in the demo/source header; trace the reader for exact units and storage. | `1` |
| `AREA_HA` | Field named in the demo/source header; trace the reader for exact units and storage. | `0.000` |
| `LAT` | Field named in the demo/source header; trace the reader for exact units and storage. | `31.734` |
| `LONG` | Field named in the demo/source header; trace the reader for exact units and storage. | `-83.720` |
| `ELEV` | Field named in the demo/source header; trace the reader for exact units and storage. | `0.000` |
| `RECALL` | Field named in the demo/source header; trace the reader for exact units and storage. | `1` |
| `WST` | Field named in the demo/source header; trace the reader for exact units and storage. | `wea1` |
| `CONSTIT` | Field named in the demo/source header; trace the reader for exact units and storage. | `0` |
| `OVERFLOW` | Flow-related value or routing parameter. | `0` |
| `RULESET` | Field named in the demo/source header; trace the reader for exact units and storage. | `0` |
| `OUT_TOT` | Count of following records or related objects. | `1` |
| `OBTYP_OUT1` | Field named in the demo/source header; trace the reader for exact units and storage. | `sdc` |
| `HTYPNO_OUT1` | Field named in the demo/source header; trace the reader for exact units and storage. | `1` |
| `HTYP_OUT1` | Field named in the demo/source header; trace the reader for exact units and storage. | `tot` |
| `FRAC_OUT1` | Field named in the demo/source header; trace the reader for exact units and storage. | `1.0000` |

## Defaults And Conversions

- Defaults: use the source inventory filename and the `file.cio` slot state as the first default/activation check.
- Missing-file behavior: if the master file or upstream manifest uses `null`, SWAT+ treats that slot as inactive for the scenario.
- Numeric conversions: not yet traced for this page; inspect the reader for unit conversions, bounds checks, and derived runtime fields.

## Reader Path

- Source inventory: `SWATPLUS/swatplus/src/input_file_module.f90`.
- Source slot: `in_con%rec_con` defaulting to `recall.con`.
- Candidate reader/source files: `SWATPLUS/swatplus/src/hyd_connect.f90`, `SWATPLUS/swatplus/src/swift_output.f90`.

## Downstream Consumers

Object routing and connection setup for moving water and constituent loads between SWAT+ objects.

## Scenario Evidence

- Scenario: `VSProj/SWAT/Osu_1hru`.
- Scenario state: `active`.
- Activation evidence: `file.cio`.
- Local file evidence: `VSProj/SWAT/Osu_1hru/recall.con`.

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
