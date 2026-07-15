---
title: chem_app.ops input file
kind: input-reference
status: partial
created: 2026-07-15
updated: 2026-07-15
source_revision: cb442f7c05fc3bfc34349c446010f452d2737ca0
scenario: Osu_1hru
tags: [inputs, reference, demo-context]
---

# `chem_app.ops`

## Purpose

Chemical application operation definitions.


## Official SWAT+ Reference

- Official page: [chem_app.ops](https://swatplus.gitbook.io/io-docs/introduction-1/management-practices/chem_app.ops).
- Official index note: This file contains pre-defined fertilizer, manure, and pesticide application operations.
- Official field metadata available: 4 field row(s); matched to 4 of 10 observed demo header field(s).
- Demo cross-check: local header and first data row are still used below to show how this scenario instantiates the official format.

## Role In SWAT+

- Category: Operations.
- Usage class: `active scenario input`.
- Activation: `file.cio`.
- `Osu_1hru` status: `active`.
- Source inventory slot(s): `in_ops%chem_ops = "chem_app.ops"`.

## File Format

SWAT+ input files use a plain-text, free-format layout with space-delimited values. GitBook documents the general convention as a title line first, then usually a header line, with exceptions such as `file.cio` and files that add count or block-header lines.
This file is controlled by the master `file.cio` manifest in normal runs. A non-`null` entry activates the selected filename; `null` means the file slot is intentionally unused for that scenario.

Local demo evidence from `VSProj/SWAT/Osu_1hru/chem_app.ops`:

- Title/comment line: `chem_app.ops: written by SWAT+ editor v2.2.0 on 2023-03-22 04:25 for SWAT+ rev.60.5.4`.
- Observed header line: `name                     chem_form           app_typ       app_eff    foliar_eff     inject_dp     surf_frac     drift_pot   aerial_unif  description`.
- Nonblank records after the header: 12.
- First demo data record: `broadcast                    solid            spread       0.90000       0.00000       0.00000       1.00000       0.00000       1.00000`.

## Fields And Parameters

The table merges the local demo header with official SWAT+ metadata when an official field definition is available. Rows marked `demo/source inferred` still need reader-level confirmation.

| Field | Meaning | Type | Unit | Default | Range | Demo value | Basis |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `name` | Chemical application name. | - | - | - | - | `broadcast` | official GitBook |
| `chem_form` | Header field observed in the demo file; trace the reader for exact storage and constraints. | - | - | - | - | `solid` | demo/source inferred |
| `app_typ` | Header field observed in the demo file; trace the reader for exact storage and constraints. | - | - | - | - | `spread` | demo/source inferred |
| `app_eff` | Application efficiency. | - | - | - | - | `0.90000` | official GitBook |
| `foliar_eff` | Removal efficiency or effect fraction/percent. | - | - | - | - | `0.00000` | demo/source inferred |
| `inject_dp` | Injection depth. | - | - | - | - | `0.00000` | official GitBook |
| `surf_frac` | Surface fraction. | - | - | - | - | `1.00000` | official GitBook |
| `drift_pot` | Header field observed in the demo file; trace the reader for exact storage and constraints. | - | - | - | - | `0.00000` | demo/source inferred |
| `aerial_unif` | Header field observed in the demo file; trace the reader for exact storage and constraints. | - | - | - | - | `1.00000` | demo/source inferred |
| `description` | Header field observed in the demo file; trace the reader for exact storage and constraints. | - | - | - | - | - | demo/source inferred |

## Defaults And Conversions

- Defaults: use the source inventory filename and the `file.cio` slot state as the first default/activation check.
- Missing-file behavior: if the master file or upstream manifest uses `null`, SWAT+ treats that slot as inactive for the scenario.
- Numeric conversions: not yet traced for this page; inspect the reader for unit conversions, bounds checks, and derived runtime fields.

## Reader Path

- Source inventory: `SWATPLUS/swatplus/src/input_file_module.f90`.
- Source slot: `in_ops%chem_ops` defaulting to `chem_app.ops`.
- Candidate reader/source files: `SWATPLUS/swatplus/src/mgt_read_chemapp.f90`.

## Downstream Consumers

Scheduled management-operation routines such as planting, harvest, grazing, irrigation, fire, and treatment.

## Scenario Evidence

- Scenario: `VSProj/SWAT/Osu_1hru`.
- Scenario state: `active`.
- Activation evidence: `file.cio`.
- Local file evidence: `VSProj/SWAT/Osu_1hru/chem_app.ops`.

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
