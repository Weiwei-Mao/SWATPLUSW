---
title: pesticide.pes input file
kind: input-reference
status: partial
created: 2026-07-15
updated: 2026-07-15
source_revision: cb442f7c05fc3bfc34349c446010f452d2737ca0
scenario: Osu_1hru
tags: [inputs, reference, demo-context]
---

# `pesticide.pes`

## Purpose

Pesticide parameter database.


## Official SWAT+ Reference

- Official page: [pesticide.pes](https://swatplus.gitbook.io/io-docs/introduction-1/databases/pesticide.pes).
- Official index note: The pesticide database summarizes parameters used by the model to simulate the fate and transport of different types of pesticides.
- Official field metadata available: 14 field row(s); matched to 12 of 15 observed demo header field(s).
- Demo cross-check: local header and first data row are still used below to show how this scenario instantiates the official format.

## Role In SWAT+

- Category: Databases.
- Usage class: `conditional input`.
- Activation: `file.cio`.
- `Osu_1hru` status: `active`.
- Source inventory slot(s): `in_parmdb%pest = "pesticide.pes"`.

## File Format

SWAT+ input files use a plain-text, free-format layout with space-delimited values. GitBook documents the general convention as a title line first, then usually a header line, with exceptions such as `file.cio` and files that add count or block-header lines.
This file is controlled by the master `file.cio` manifest in normal runs. A non-`null` entry activates the selected filename; `null` means the file slot is intentionally unused for that scenario.

Local demo evidence from `VSProj/SWAT/Osu_1hru/pesticide.pes`:

- Title/comment line: `pesticide.pes: written by SWAT+ editor v2.2.0 on 2023-03-22 04:25 for SWAT+ rev.60.5.4`.
- Observed header line: `name                  soil_ads     frac_wash    hl_foliage       hl_soil         solub      aq_hlife      aq_volat        mol_wt      aq_resus     aq_settle   ben_act_dep      ben_bury     ben_hlife  description`.
- Nonblank records after the header: 233.
- First demo data record: `245-tp              2600.00000       0.40000       5.00000      20.00000       2.50000       0.00700       0.00001       0.10000       0.00200       0.50000       0.30000       0.00200       0.05000  Silvex_Amine`.

## Fields And Parameters

The table merges the local demo header with official SWAT+ metadata when an official field definition is available. Rows marked `demo/source inferred` still need reader-level confirmation.

| Field | Meaning | Type | Unit | Default | Range | Demo value | Basis |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `name` | Name of the pesticide record. | - | - | - | - | `245-tp` | official GitBook |
| `soil_ads` | Soil adsorption coefficient normalized for soil organic carbon content. | - | - | - | - | `2600.00000` | official GitBook |
| `frac_wash` | Fraction of pesticide on foliage that is washed off by rainfall event. | - | - | - | - | `0.40000` | official GitBook |
| `hl_foliage` | Half-life of the pesticide on the foliage. | - | - | - | - | `5.00000` | official GitBook |
| `hl_soil` | Half-life of the pesticide in the soil. | - | - | - | - | `20.00000` | official GitBook |
| `solub` | Solubility of the pesticide in water. | - | - | - | - | `2.50000` | official GitBook |
| `aq_hlife` | Header field observed in the demo file; trace the reader for exact storage and constraints. | - | - | - | - | `0.00700` | demo/source inferred |
| `aq_volat` | Aquatic volatilization coefficient. | - | - | - | - | `0.00001` | official GitBook |
| `mol_wt` | Molecular weight to calculate mixing velocity. | - | - | - | - | `0.10000` | official GitBook |
| `aq_resus` | Aquatic resuspension velocity for pesticide sorbed to sediment. | - | - | - | - | `0.00200` | official GitBook |
| `aq_settle` | Aquatic settling velocity for pesticide sorbed to sediment. | - | - | - | - | `0.50000` | official GitBook |
| `ben_act_dep` | Depth of the active benthic layer. | - | - | - | - | `0.30000` | official GitBook |
| `ben_bury` | Burial velocity in the benthic sediment. | - | - | - | - | `0.00200` | official GitBook |
| `ben_hlife` | Header field observed in the demo file; trace the reader for exact storage and constraints. | - | - | - | - | `0.05000` | demo/source inferred |
| `description` | Header field observed in the demo file; trace the reader for exact storage and constraints. | - | - | - | - | `Silvex_Amine` | demo/source inferred |

Additional official field rows that are not part of the observed demo header:

| Field | Meaning | Type | Unit |
| --- | --- | --- | --- |
| `aq_reac` | Aquatic pesticide reaction coefficient. | - | - |
| `ben_reac` | Reaction coefficient in the benthic sediment. | - | - |

## Defaults And Conversions

- Defaults: use the source inventory filename and the `file.cio` slot state as the first default/activation check.
- Missing-file behavior: if the master file or upstream manifest uses `null`, SWAT+ treats that slot as inactive for the scenario.
- Numeric conversions: not yet traced for this page; inspect the reader for unit conversions, bounds checks, and derived runtime fields.

## Reader Path

- Source inventory: `SWATPLUS/swatplus/src/input_file_module.f90`.
- Source slot: `in_parmdb%pest` defaulting to `pesticide.pes`.
- Candidate reader/source files: `SWATPLUS/swatplus/src/pest_parm_read.f90`.

## Downstream Consumers

Reusable parameter databases referenced by management, land-use, constituent, and operation records.

## Scenario Evidence

- Scenario: `VSProj/SWAT/Osu_1hru`.
- Scenario state: `active`.
- Activation evidence: `file.cio`.
- Local file evidence: `VSProj/SWAT/Osu_1hru/pesticide.pes`.

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
