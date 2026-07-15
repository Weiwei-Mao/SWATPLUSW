---
title: puddle.ops input file
kind: input-reference
status: partial
created: 2026-07-15
updated: 2026-07-15
source_revision: cb442f7c05fc3bfc34349c446010f452d2737ca0
scenario: Osu_1hru
tags: [inputs, reference, demo-context]
---

# `puddle.ops`

## Purpose

Optional puddling operation definitions.


## Official SWAT+ Reference

No standalone official SWAT+ GitBook page was found for this exact filename in the current documentation index. Keep this page tied to the source inventory and local demo evidence until a reader-specific official page is identified.

## Role In SWAT+

- Category: Operations.
- Usage class: `fixed-name companion`.
- Activation: fixed-name or derived reader.
- `Osu_1hru` status: `fixed-name/conditional`.
- Source inventory: no direct default slot was found in `input_file_module.f90`; trace fixed-name or derived readers before treating the filename as mandatory.

## File Format

SWAT+ input files use a plain-text, free-format layout with space-delimited values. GitBook documents the general convention as a title line first, then usually a header line, with exceptions such as `file.cio` and files that add count or block-header lines.
This file is a fixed-name or derived companion rather than a primary `file.cio` selection. The reader may open it by convention when its parent workflow is active.

Local demo evidence from `VSProj/SWAT/Osu_1hru/puddle.ops`:

- Title/comment line: `name                  hydcon_mm/h   sed_ppm      orgn_ppm      sedp_ppm     no3_ppm       solp_ppm       nh3_ppm  no2_ppm`.
- Observed header line: `high_eff              0.00000         10000       0.00000     800.00000     10.00000      20.00000       1.00000  1.00000`.
- Nonblank records after the header: 2.
- First demo data record: `med_eff               0.00000         10000       0.00000     500.00000     10.00000      20.00000       1.00000  1.00000`.

## Fields And Parameters

The table is generated from the local demo header. Meanings are practical working descriptions and should be confirmed against the reader before final use.

| Field | Working meaning | Demo value | Basis |
| --- | --- | --- | --- |
| `high_eff` | Removal efficiency or effect fraction/percent. | `med_eff` | demo/source inferred |
| `0.00000` | Header field observed in the demo file; trace the reader for exact storage and constraints. | `0.00000` | demo/source inferred |
| `10000` | Header field observed in the demo file; trace the reader for exact storage and constraints. | `10000` | demo/source inferred |
| `0.00000` | Header field observed in the demo file; trace the reader for exact storage and constraints. | `0.00000` | demo/source inferred |
| `800.00000` | Header field observed in the demo file; trace the reader for exact storage and constraints. | `500.00000` | demo/source inferred |
| `10.00000` | Header field observed in the demo file; trace the reader for exact storage and constraints. | `10.00000` | demo/source inferred |
| `20.00000` | Header field observed in the demo file; trace the reader for exact storage and constraints. | `20.00000` | demo/source inferred |
| `1.00000` | Header field observed in the demo file; trace the reader for exact storage and constraints. | `1.00000` | demo/source inferred |
| `1.00000` | Header field observed in the demo file; trace the reader for exact storage and constraints. | `1.00000` | demo/source inferred |

## Defaults And Conversions

- Defaults: use the source inventory filename and the `file.cio` slot state as the first default/activation check.
- Missing-file behavior: if the master file or upstream manifest uses `null`, SWAT+ treats that slot as inactive for the scenario.
- Numeric conversions: not yet traced for this page; inspect the reader for unit conversions, bounds checks, and derived runtime fields.

## Reader Path

- Source inventory: `SWATPLUS/swatplus/src/input_file_module.f90`.
- Source slot: not found as a direct default filename in the source inventory.
- Candidate reader/source files: `SWATPLUS/swatplus/src/mgt_read_puddle.f90`.

## Downstream Consumers

Scheduled management-operation routines such as planting, harvest, grazing, irrigation, fire, and treatment.

## Scenario Evidence

- Scenario: `VSProj/SWAT/Osu_1hru`.
- Scenario state: `fixed-name/conditional`.
- Activation evidence: fixed-name or derived reader.
- Local file evidence: `VSProj/SWAT/Osu_1hru/puddle.ops`.

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
