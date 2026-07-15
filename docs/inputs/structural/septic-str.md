---
title: septic.str input file
kind: input-reference
status: partial
created: 2026-07-15
updated: 2026-07-15
source_revision: cb442f7c05fc3bfc34349c446010f452d2737ca0
scenario: Osu_1hru
tags: [inputs, reference, demo-context]
---

# `septic.str`

## Purpose

Structural septic-system setup file.


## Official SWAT+ Reference

- Official page: [septic.str](https://swatplus.gitbook.io/io-docs/introduction-1/structural-practices/septic.str).
- Official index note: This file contains the septic system parameters.
- Official field metadata available: 28 field row(s); matched to 28 of 28 observed demo header field(s).
- Demo cross-check: local header and first data row are still used below to show how this scenario instantiates the official format.

## Role In SWAT+

- Category: Structural.
- Usage class: `active scenario input`.
- Activation: `file.cio`.
- `Osu_1hru` status: `active`.
- Source inventory slot(s): `in_str%septic_str = "septic.str"`.

## File Format

SWAT+ input files use a plain-text, free-format layout with space-delimited values. GitBook documents the general convention as a title line first, then usually a header line, with exceptions such as `file.cio` and files that add count or block-header lines.
This file is controlled by the master `file.cio` manifest in normal runs. A non-`null` entry activates the selected filename; `null` means the file slot is intentionally unused for that scenario.

Local demo evidence from `VSProj/SWAT/Osu_1hru/septic.str`:

- Title/comment line: `septic.str: written by SWAT+ editor v2.2.0 on 2023-03-22 04:25 for SWAT+ rev.60.5.4`.
- Observed header line: `name                   typ        yr  operation     residents          area    t_fail       dp_bioz      thk_bioz      cha_dist      sep_dens       bm_dens     bod_decay      bod_conv        fc_lin        fc_exp   fecal_decay      tds_conv          mort          resp       slough1       slough2           nit         denit        p_sorp    p_sorp_max      solp_slp      solp_int`.
- Nonblank records after the header: 2.
- First demo data record: `standard                 1         0         0       2.50000     100.00000        70     500.00000      50.00000       0.50000       1.50000    1000.00000       0.50000       0.32000      30.00000       0.80000       1.30000       0.10000       0.50000       0.16000       0.30000       0.50000       1.50000       0.32000     128.00000     850.00000       0.04000       3.10000`.

## Fields And Parameters

The table merges the local demo header with official SWAT+ metadata when an official field definition is available. Rows marked `demo/source inferred` still need reader-level confirmation.

| Field | Meaning | Type | Unit | Default | Range | Demo value | Basis |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `name` | Name of septic system record. | - | - | - | - | `standard` | official GitBook |
| `typ` | Septic system type. | - | - | - | - | `1` | official GitBook |
| `yr` | Year the septic system became operational. | - | - | - | - | `0` | official GitBook |
| `operation` | Septic system operation flag. | - | - | - | - | `0` | official GitBook |
| `residents` | Number of permanent residents in the house. | - | - | - | - | `2.50000` | official GitBook |
| `area` | Average area of drainfield of individual septic systems. | - | - | - | - | `100.00000` | official GitBook |
| `t_fail` | Time until failing systems gets fixed. | - | - | - | - | `70` | official GitBook |
| `dp_bioz` | Depth to the top of the biozone layer from the ground surface. | - | - | - | - | `500.00000` | official GitBook |
| `thk_bioz` | Thickness of biozone layer. | - | - | - | - | `50.00000` | official GitBook |
| `cha_dist` | Distance from septic system to the stream. | - | - | - | - | `0.50000` | official GitBook |
| `sep_dens` | Number of septic systems per square kilometer. | - | - | - | - | `1.50000` | official GitBook |
| `bm_dens` | Density of biomass. | - | - | - | - | `1000.00000` | official GitBook |
| `bod_decay` | BOD decay rate coefficient. | - | - | - | - | `0.50000` | official GitBook |
| `bod_conv` | Conversion factor representing the proportion of mass bacterial growth and mass BOD degraded in the septic system. | - | - | - | - | `0.32000` | official GitBook |
| `fc_lin` | Linear coefficient for calculation of field capacity in the biozone. | - | - | - | - | `30.00000` | official GitBook |
| `fc_exp` | Exponential coefficient for calculation of field capacity in the biozone. | - | - | - | - | `0.80000` | official GitBook |
| `fecal_decay` | Fecal coliform bacteria decay rate coefficient. | - | - | - | - | `1.30000` | official GitBook |
| `tds_conv` | Conversion factor for plaque from Total Dissolved Solids. | - | - | - | - | `0.10000` | official GitBook |
| `mort` | Mortality rate coefficient. | - | - | - | - | `0.50000` | official GitBook |
| `resp` | Respiration rate coefficient. | - | - | - | - | `0.16000` | official GitBook |
| `slough1` | Linear coefficient for calculating the rate of biomass sloughing. | - | - | - | - | `0.30000` | official GitBook |
| `slough2` | Exponential coefficient for calculating the rate of biomass sloughing. | - | - | - | - | `0.50000` | official GitBook |
| `nit` | Nitrification rate coefficient. | - | - | - | - | `1.50000` | official GitBook |
| `denit` | Denitrification rate coefficient. | - | - | - | - | `0.32000` | official GitBook |
| `p_sorp` | Linear P sorption distribution coefficient. | - | - | - | - | `128.00000` | official GitBook |
| `p_sorp_max` | Maximum P sorption capacity. | - | - | - | - | `850.00000` | official GitBook |
| `solp_slp` | Slope of the linear effluent soluble P equation. | - | - | - | - | `0.04000` | official GitBook |
| `solp_int` | Intercept of the linear effluent soluble P equation. | - | - | - | - | `3.10000` | official GitBook |

## Defaults And Conversions

- Defaults: use the source inventory filename and the `file.cio` slot state as the first default/activation check.
- Missing-file behavior: if the master file or upstream manifest uses `null`, SWAT+ treats that slot as inactive for the scenario.
- Numeric conversions: not yet traced for this page; inspect the reader for unit conversions, bounds checks, and derived runtime fields.

## Reader Path

- Source inventory: `SWATPLUS/swatplus/src/input_file_module.f90`.
- Source slot: `in_str%septic_str` defaulting to `septic.str`.
- Candidate reader/source files: `SWATPLUS/swatplus/src/sep_read.f90`.

## Downstream Consumers

Structural practice routines such as tile drains, filter strips, grassed waterways, septic systems, and BMP adjustments.

## Scenario Evidence

- Scenario: `VSProj/SWAT/Osu_1hru`.
- Scenario state: `active`.
- Activation evidence: `file.cio`.
- Local file evidence: `VSProj/SWAT/Osu_1hru/septic.str`.

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
