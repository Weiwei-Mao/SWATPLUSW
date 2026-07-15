---
title: recall.rec input file
kind: input-reference
status: partial
created: 2026-07-15
updated: 2026-07-15
source_revision: cb442f7c05fc3bfc34349c446010f452d2737ca0
scenario: Osu_1hru
tags: [inputs, reference, demo-context]
---

# `recall.rec`

## Purpose

External time-series hydrograph/input source data for recall objects.

## Role In SWAT+

- Category: Point Sources Inlets.
- Usage class: `active scenario input`.
- Activation: `file.cio`.
- `Osu_1hru` status: `active`.
- Source inventory slot(s): `in_rec%recall_rec = "recall.rec"`.

## File Format

SWAT+ input files use a plain-text, free-format layout with space-delimited values. GitBook documents the general convention as a title line first, then usually a header line, with exceptions such as `file.cio` and files that add count or block-header lines.
This file is controlled by the master `file.cio` manifest in normal runs. A non-`null` entry activates the selected filename; `null` means the file slot is intentionally unused for that scenario.

Local demo evidence from `VSProj/SWAT/Osu_1hru/recall.rec`:

- Title/comment line: `recall.rec`.
- Observed header line: `NUM     NAME    TYPE     FNAME    OBJ_TYP     OBJ_NAME       flo     sed    orgn    sedp     no3    solp    chla     nh3      no2    cbod     dox     san     sil     cla     sag     lag     grv    temp`.
- Nonblank records after the header: 2.
- First demo data record: `1    PSTYR    3    	RECYR.        hru         hru1   12120.5       0       0       0       0       0       0        0       0       0       0       0       0       0       0       0       0       0`.

## Fields And Parameters

The table below is generated from the demo header. Meanings are practical working descriptions from the header name, local scenario context, and SWAT+ conventions; verify units and storage against the reader before citing them as final.

| Field | Working meaning | Demo value |
| --- | --- | --- |
| `NUM` | Count of following records or related objects. | `1` |
| `NAME` | Record name or target name used by the calibration/update reader. | `PSTYR` |
| `TYPE` | Field named in the demo/source header; trace the reader for exact units and storage. | `3` |
| `FNAME` | Field named in the demo/source header; trace the reader for exact units and storage. | `RECYR.` |
| `OBJ_TYP` | Field named in the demo/source header; trace the reader for exact units and storage. | `hru` |
| `OBJ_NAME` | Field named in the demo/source header; trace the reader for exact units and storage. | `hru1` |
| `flo` | Flow-related value or routing parameter. | `12120.5` |
| `sed` | Sediment-related value, efficiency, or parameter; verify units in the reader. | `0` |
| `orgn` | Organic nitrogen component; verify units in the reader. | `0` |
| `sedp` | Sediment-related value, efficiency, or parameter; verify units in the reader. | `0` |
| `no3` | Nitrate-nitrogen concentration, mass, or parameter component; verify units in the reader. | `0` |
| `solp` | Phosphorus-related component; verify units in the reader. | `0` |
| `chla` | Field named in the demo/source header; trace the reader for exact units and storage. | `0` |
| `nh3` | Ammonia-nitrogen concentration, mass, or parameter component; verify units in the reader. | `0` |
| `no2` | Field named in the demo/source header; trace the reader for exact units and storage. | `0` |
| `cbod` | Field named in the demo/source header; trace the reader for exact units and storage. | `0` |
| `dox` | Field named in the demo/source header; trace the reader for exact units and storage. | `0` |
| `san` | Field named in the demo/source header; trace the reader for exact units and storage. | `0` |
| `sil` | Field named in the demo/source header; trace the reader for exact units and storage. | `0` |
| `cla` | Field named in the demo/source header; trace the reader for exact units and storage. | `0` |
| `sag` | Field named in the demo/source header; trace the reader for exact units and storage. | `0` |
| `lag` | Field named in the demo/source header; trace the reader for exact units and storage. | `0` |
| `grv` | Field named in the demo/source header; trace the reader for exact units and storage. | `0` |
| `temp` | Field named in the demo/source header; trace the reader for exact units and storage. | `0` |

## Defaults And Conversions

- Defaults: use the source inventory filename and the `file.cio` slot state as the first default/activation check.
- Missing-file behavior: if the master file or upstream manifest uses `null`, SWAT+ treats that slot as inactive for the scenario.
- Numeric conversions: not yet traced for this page; inspect the reader for unit conversions, bounds checks, and derived runtime fields.

## Reader Path

- Source inventory: `SWATPLUS/swatplus/src/input_file_module.f90`.
- Source slot: `in_rec%recall_rec` defaulting to `recall.rec`.
- Candidate reader/source files: `SWATPLUS/swatplus/src/recall_read_cs.f90`.

## Downstream Consumers

External source, recall, inlet, and constant-load routines.

## Scenario Evidence

- Scenario: `VSProj/SWAT/Osu_1hru`.
- Scenario state: `active`.
- Activation evidence: `file.cio`.
- Local file evidence: `VSProj/SWAT/Osu_1hru/recall.rec`.

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
