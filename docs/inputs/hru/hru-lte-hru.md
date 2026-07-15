---
title: hru-lte.hru input file
kind: input-reference
status: partial
created: 2026-07-15
updated: 2026-07-15
source_revision: cb442f7c05fc3bfc34349c446010f452d2737ca0
scenario: Osu_1hru
tags: [inputs, reference, demo-context]
---

# `hru-lte.hru`

## Purpose

Input file for HRU; source slot hru_ez.


## Official SWAT+ Reference

- Official page: [hru-lte.hru](https://swatplus.gitbook.io/io-docs/introduction-1/hydrologic-response-units/hru-lte.hru).
- Official field metadata available: 35 field row(s); matched to 0 of 0 observed demo header field(s).

## Role In SWAT+

- Category: Hru.
- Usage class: `optional/default`.
- Activation: source default or inactive `file.cio` slot.
- `Osu_1hru` status: `inactive/null`.
- Source inventory slot(s): `in_hru%hru_ez = "hru-lte.hru"`.

## File Format

SWAT+ input files use a plain-text, free-format layout with space-delimited values. GitBook documents the general convention as a title line first, then usually a header line, with exceptions such as `file.cio` and files that add count or block-header lines.
This file is controlled by the master `file.cio` manifest in normal runs. A non-`null` entry activates the selected filename; `null` means the file slot is intentionally unused for that scenario.

Local demo evidence: the `Osu_1hru` scenario does not include a concrete `hru-lte.hru` file, or the file family is inactive there. Use another scenario or the reader routine for field-level confirmation.

## Fields And Parameters

No local demo header is available, but the official SWAT+ page provides field metadata. Demo value cells are therefore blank until an active scenario file is added.

| Field | Meaning | Type | Unit | Default | Range |
| --- | --- | --- | --- | --- | --- |
| `id` | ID of the HRU-lte. | - | - | - | - |
| `name` | Name of HRU-lte. | - | - | - | - |
| `area` | HRU-lte drainage area. | - | - | - | - |
| `cn2` | Condition II Curve Number. | - | - | - | - |
| `cn3_swf` | Soil water factor for CN3. | - | - | - | - |
| `t_conc` | Time of concentration. | - | - | - | - |
| `soil_dp` | Soil profile depth. | - | - | - | - |
| `perco_co` | Soil percolation coefficient. | - | - | - | - |
| `slp` | Land surface slope. | - | - | - | - |
| `slp_len` | Land surface slope length. | - | - | - | - |
| `et_co` | ET coefficient. | - | - | - | - |
| `aqu_sp_yld` | Specific yield of the shallow aquifer. | - | - | - | - |
| `alpha_bf` | Baseflow alpha factor. | - | - | - | - |
| `revap` | Revap coefficient. | - | - | - | - |
| `rchg_dp` | Percolation coefficient from shallow to deep aquifer. | - | - | - | - |
| `sw_init` | Initial soil water (fraction of available water capacity). | - | - | - | - |
| `aqu_init` | Initial shallow aquifer storage. | - | - | - | - |
| `aqu_sh_flo` | Initial shallow aquifer flow. | - | - | - | - |
| `aqu_dp_flo` | Initial deep aquifer flow. | - | - | - | - |
| `snow_h2o` | Initial snow water equivalent. | - | - | - | - |
| `lat` | Latitude. | - | - | - | - |
| `soil_text` | Soil texture. | - | - | - | - |
| `trop_flag` | Tropical flag. | - | - | - | - |
| `grow_start` | Start of growing season for non-tropical/start of monsoon initialization period for tropical. | - | - | - | - |
| `grow_end` | End of growing season for non-tropical/start of monsoon initialization period for tropical. | - | - | - | - |
| `plnt_typ` | Plant type. | - | - | - | - |
| `stress` | Plant stress. | - | - | - | - |
| `pet_flag` | Potential ET method. | - | - | - | - |
| `irr_flag` | Irrigation code. | - | - | - | - |
| `irr_src` | Irrigation source. | - | - | - | - |
| `t_drain` | Design subsurface tile drain time. | - | - | - | - |
| `usle_k` | USLE soil erodibility factor K. | - | - | - | - |
| `usle_c` | USLE cover factor C. | - | - | - | - |
| `usle_p` | USLE support practice factor P. | - | - | - | - |
| `usle_ls` | USLE slope length and slope factor LS. | - | - | - | - |

## Defaults And Conversions

- Defaults: use the source inventory filename and the `file.cio` slot state as the first default/activation check.
- Missing-file behavior: if the master file or upstream manifest uses `null`, SWAT+ treats that slot as inactive for the scenario.
- Numeric conversions: not yet traced for this page; inspect the reader for unit conversions, bounds checks, and derived runtime fields.

## Reader Path

- Source inventory: `SWATPLUS/swatplus/src/input_file_module.f90`.
- Source slot: `in_hru%hru_ez` defaulting to `hru-lte.hru`.
- Candidate reader/source files: `SWATPLUS/swatplus/src/hru_lte_read.f90`.

## Downstream Consumers

HRU or HRU-LTE object setup and land-phase calculations.

## Scenario Evidence

- Scenario: `VSProj/SWAT/Osu_1hru`.
- Scenario state: `inactive/null`.
- Activation evidence: source default or inactive `file.cio` slot.
- Local file evidence: no concrete file found in the demo scenario.

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
