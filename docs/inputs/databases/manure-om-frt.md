---
title: manure_om.frt input file
kind: input-reference
status: partial
created: 2026-07-15
updated: 2026-07-15
source_revision: cb442f7c05fc3bfc34349c446010f452d2737ca0
scenario: Osu_1hru
tags: [inputs, reference, demo-context]
---

# `manure_om.frt`

## Purpose

Optional organic/mineral manure database.


## Official SWAT+ Reference

No standalone official SWAT+ GitBook page was found for this exact filename in the current documentation index. Keep this page tied to the source inventory and local demo evidence until a reader-specific official page is identified.

## Role In SWAT+

- Category: Databases.
- Usage class: `fixed-name companion`.
- Activation: fixed-name or derived reader.
- `Osu_1hru` status: `fixed-name/conditional`.
- Source inventory: no direct default slot was found in `input_file_module.f90`; trace fixed-name or derived readers before treating the filename as mandatory.

## File Format

SWAT+ input files use a plain-text, free-format layout with space-delimited values. GitBook documents the general convention as a title line first, then usually a header line, with exceptions such as `file.cio` and files that add count or block-header lines.
This file is a fixed-name or derived companion rather than a primary `file.cio` selection. The reader may open it by convention when its parent workflow is active.

Local demo evidence from `VSProj/SWAT/Osu_1hru/manure_om.frt`:

- Title/comment line: `manure_om.frt: manure organic matter database`.
- Observed header line: `name            frac_water   fcbn          fminn         fminp         forgn         forgp         fnh3n  description`.
- Nonblank records after the header: 2.
- First demo data record: `mw_beef_liq     0.988        0.000780576   0.000311751   0.00081295    0.002110312   0.000365707   0.99   midwest_beef_liquid`.

## Fields And Parameters

The table is generated from the local demo header. Meanings are practical working descriptions and should be confirmed against the reader before final use.

| Field | Working meaning | Demo value | Basis |
| --- | --- | --- | --- |
| `name` | Record name used by other SWAT+ inputs to reference this row. | `mw_beef_liq` | demo/source inferred |
| `frac_water` | Header field observed in the demo file; trace the reader for exact storage and constraints. | `0.988` | demo/source inferred |
| `fcbn` | Header field observed in the demo file; trace the reader for exact storage and constraints. | `0.000780576` | demo/source inferred |
| `fminn` | Minimum value or lower bound, depending on the reader. | `0.000311751` | demo/source inferred |
| `fminp` | Minimum value or lower bound, depending on the reader. | `0.00081295` | demo/source inferred |
| `forgn` | Organic nitrogen value; verify storage and units in the reader. | `0.002110312` | demo/source inferred |
| `forgp` | Phosphorus-related parameter or state value. | `0.000365707` | demo/source inferred |
| `fnh3n` | Ammonia-nitrogen value; verify storage and units in the reader. | `0.99` | demo/source inferred |
| `description` | Header field observed in the demo file; trace the reader for exact storage and constraints. | `midwest_beef_liquid` | demo/source inferred |

## Defaults And Conversions

- Defaults: use the source inventory filename and the `file.cio` slot state as the first default/activation check.
- Missing-file behavior: if the master file or upstream manifest uses `null`, SWAT+ treats that slot as inactive for the scenario.
- Numeric conversions: not yet traced for this page; inspect the reader for unit conversions, bounds checks, and derived runtime fields.

## Reader Path

- Source inventory: `SWATPLUS/swatplus/src/input_file_module.f90`.
- Source slot: not found as a direct default filename in the source inventory.
- Candidate reader/source files: `SWATPLUS/swatplus/src/manure_orgmin_read.f90`.

## Downstream Consumers

Reusable parameter databases referenced by management, land-use, constituent, and operation records.

## Scenario Evidence

- Scenario: `VSProj/SWAT/Osu_1hru`.
- Scenario state: `fixed-name/conditional`.
- Activation evidence: fixed-name or derived reader.
- Local file evidence: `VSProj/SWAT/Osu_1hru/manure_om.frt`.

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
