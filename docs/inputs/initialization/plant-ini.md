---
title: plant.ini input file
kind: input-reference
status: partial
created: 2026-07-15
updated: 2026-07-15
source_revision: cb442f7c05fc3bfc34349c446010f452d2737ca0
scenario: Osu_1hru
tags: [inputs, reference, demo-context]
---

# `plant.ini`

## Purpose

Initial plant-community condition records.


## Official SWAT+ Reference

- Official page: [plant.ini](https://swatplus.gitbook.io/io-docs/introduction-1/landuse-and-management/plant.ini).
- Official index note: This file stores information about the plants growing in a plant community.
- Official field metadata available: 11 field row(s); matched to 8 of 11 observed demo header field(s).
- Demo cross-check: local header and first data row are still used below to show how this scenario instantiates the official format.

## Role In SWAT+

- Category: Initialization.
- Usage class: `active scenario input`.
- Activation: `file.cio`.
- `Osu_1hru` status: `active`.
- Source inventory slot(s): `in_init%plant = "plant.ini"`.

## File Format

SWAT+ input files use a plain-text, free-format layout with space-delimited values. GitBook documents the general convention as a title line first, then usually a header line, with exceptions such as `file.cio` and files that add count or block-header lines.
This file is controlled by the master `file.cio` manifest in normal runs. A non-`null` entry activates the selected filename; `null` means the file slot is intentionally unused for that scenario.

Local demo evidence from `VSProj/SWAT/Osu_1hru/plant.ini`:

- Title/comment line: `plant.ini: default bare-start communities for rev62`.
- Observed header line: `pcom_name          plt_cnt  rot_yr_ini          plt_name     lc_status      lai_init       bm_init      phu_init      plnt_pop      yrs_init      rsd_init`.
- Nonblank records after the header: 21.
- First demo data record: `gras_comm              1          1`.

## Fields And Parameters

The table merges the local demo header with official SWAT+ metadata when an official field definition is available. Rows marked `demo/source inferred` still need reader-level confirmation.

| Field | Meaning | Type | Unit | Default | Range | Demo value | Basis |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `pcom_name` | Header field observed in the demo file; trace the reader for exact storage and constraints. | - | - | - | - | `gras_comm` | demo/source inferred |
| `plt_cnt` | Plant-related parameter or record reference. | - | - | - | - | `1` | demo/source inferred |
| `rot_yr_ini` | Initial rotation year. | - | - | - | - | `1` | official GitBook |
| `plt_name` | Plant-related parameter or record reference. | - | - | - | - | - | demo/source inferred |
| `lc_status` | Land cover status at start of simulation. | - | - | - | - | - | official GitBook |
| `lai_init` | Initial Leaf Area Index. | - | - | - | - | - | official GitBook |
| `bm_init` | Initial plant biomass. | - | - | - | - | - | official GitBook |
| `phu_init` | Initial fraction of plant heat units accumulated. | - | - | - | - | - | official GitBook |
| `plnt_pop` | Plant population. | - | - | - | - | - | official GitBook |
| `yrs_init` | Age of plant at start of simulation. | - | - | - | - | - | official GitBook |
| `rsd_init` | Initial residue cover. | - | - | - | - | - | official GitBook |

Additional official field rows that are not part of the observed demo header:

| Field | Meaning | Type | Unit |
| --- | --- | --- | --- |
| `name` | Plant community name. | - | - |
| `plnt_cnt` | Number of plants in the community. | - | - |
| `plnt_name` | Plant name as in plant database. | - | - |

## Defaults And Conversions

- Defaults: use the source inventory filename and the `file.cio` slot state as the first default/activation check.
- Missing-file behavior: if the master file or upstream manifest uses `null`, SWAT+ treats that slot as inactive for the scenario.
- Numeric conversions: not yet traced for this page; inspect the reader for unit conversions, bounds checks, and derived runtime fields.

## Reader Path

- Source inventory: `SWATPLUS/swatplus/src/input_file_module.f90`.
- Source slot: `in_init%plant` defaulting to `plant.ini`.
- Candidate reader/source files: `SWATPLUS/swatplus/src/readpcom.f90`.

## Downstream Consumers

Initial condition assignment for plants, soil/plant pools, water bodies, and constituents.

## Scenario Evidence

- Scenario: `VSProj/SWAT/Osu_1hru`.
- Scenario state: `active`.
- Activation evidence: `file.cio`.
- Local file evidence: `VSProj/SWAT/Osu_1hru/plant.ini`.

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
