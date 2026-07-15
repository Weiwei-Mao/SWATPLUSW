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


## Official SWAT+ Reference

- Official page: [recall_db.rec](https://swatplus.gitbook.io/io-docs/introduction-1/point-sources-and-inlets/recall.rec).
- Official index note: This file lists all recall records used in a simulation.
- Official field metadata available: 20 field row(s); matched to 1 of 24 observed demo header field(s).
- Demo cross-check: local header and first data row are still used below to show how this scenario instantiates the official format.

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

The table merges the local demo header with official SWAT+ metadata when an official field definition is available. Rows marked `demo/source inferred` still need reader-level confirmation.

| Field | Meaning | Type | Unit | Default | Range | Demo value | Basis |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `NUM` | Header field observed in the demo file; trace the reader for exact storage and constraints. | - | - | - | - | `1` | demo/source inferred |
| `NAME` | Name of the recall record. | `string` | - | - | - | `PSTYR` | official GitBook |
| `TYPE` | Header field observed in the demo file; trace the reader for exact storage and constraints. | - | - | - | - | `3` | demo/source inferred |
| `FNAME` | Header field observed in the demo file; trace the reader for exact storage and constraints. | - | - | - | - | `RECYR.` | demo/source inferred |
| `OBJ_TYP` | Header field observed in the demo file; trace the reader for exact storage and constraints. | - | - | - | - | `hru` | demo/source inferred |
| `OBJ_NAME` | Header field observed in the demo file; trace the reader for exact storage and constraints. | - | - | - | - | `hru1` | demo/source inferred |
| `flo` | Header field observed in the demo file; trace the reader for exact storage and constraints. | - | - | - | - | `12120.5` | demo/source inferred |
| `sed` | Sediment-related parameter or state value. | - | - | - | - | `0` | demo/source inferred |
| `orgn` | Organic nitrogen value; verify storage and units in the reader. | - | - | - | - | `0` | demo/source inferred |
| `sedp` | Sediment-related parameter or state value. | - | - | - | - | `0` | demo/source inferred |
| `no3` | Nitrate-nitrogen value; verify storage and units in the reader. | - | - | - | - | `0` | demo/source inferred |
| `solp` | Phosphorus-related parameter or state value. | - | - | - | - | `0` | demo/source inferred |
| `chla` | Header field observed in the demo file; trace the reader for exact storage and constraints. | - | - | - | - | `0` | demo/source inferred |
| `nh3` | Ammonia-nitrogen value; verify storage and units in the reader. | - | - | - | - | `0` | demo/source inferred |
| `no2` | Header field observed in the demo file; trace the reader for exact storage and constraints. | - | - | - | - | `0` | demo/source inferred |
| `cbod` | Header field observed in the demo file; trace the reader for exact storage and constraints. | - | - | - | - | `0` | demo/source inferred |
| `dox` | Header field observed in the demo file; trace the reader for exact storage and constraints. | - | - | - | - | `0` | demo/source inferred |
| `san` | Header field observed in the demo file; trace the reader for exact storage and constraints. | - | - | - | - | `0` | demo/source inferred |
| `sil` | Header field observed in the demo file; trace the reader for exact storage and constraints. | - | - | - | - | `0` | demo/source inferred |
| `cla` | Header field observed in the demo file; trace the reader for exact storage and constraints. | - | - | - | - | `0` | demo/source inferred |
| `sag` | Header field observed in the demo file; trace the reader for exact storage and constraints. | - | - | - | - | `0` | demo/source inferred |
| `lag` | Header field observed in the demo file; trace the reader for exact storage and constraints. | - | - | - | - | `0` | demo/source inferred |
| `grv` | Header field observed in the demo file; trace the reader for exact storage and constraints. | - | - | - | - | `0` | demo/source inferred |
| `temp` | Header field observed in the demo file; trace the reader for exact storage and constraints. | - | - | - | - | `0` | demo/source inferred |

Additional official field rows that are not part of the observed demo header:

| Field | Meaning | Type | Unit |
| --- | --- | --- | --- |
| `id` | ID of the recall record. | `integer` | - |
| `om_name` | Name of the organic and mineral data file. | `string` | - |
| `om_unit` | Unit of the organic and mineral data. | `string` | - |
| `om_tstep` | Time step of the organic and mineral data. | `string` | - |
| `pest_name` | Official field row listed for this file. | - | - |
| `pest_unit` | Official field row listed for this file. | - | - |
| `pest_tstep` | Official field row listed for this file. | - | - |
| `path_name` | Official field row listed for this file. | - | - |
| `path_unit` | Official field row listed for this file. | - | - |
| `path_tstep` | Official field row listed for this file. | - | - |
| `hmet_name` | Official field row listed for this file. | - | - |
| `hmet_unit` | Official field row listed for this file. | - | - |
| `hmet_tstep` | Official field row listed for this file. | - | - |
| `salt_name` | Official field row listed for this file. | - | - |
| `salt_unit` | Official field row listed for this file. | - | - |
| `salt_tstep` | Official field row listed for this file. | - | - |
| `cst_name` | Official field row listed for this file. | - | - |
| `cst_unit` | Official field row listed for this file. | - | - |
| `cst_tstep` | Official field row listed for this file. | - | - |

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
