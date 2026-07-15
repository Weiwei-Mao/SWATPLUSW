---
title: aquifer.aqu input file
kind: input-reference
status: partial
created: 2026-07-15
updated: 2026-07-15
source_revision: cb442f7c05fc3bfc34349c446010f452d2737ca0
scenario: Osu_1hru
tags: [inputs, reference, demo-context]
---

# `aquifer.aqu`

## Purpose

Lumped aquifer parameter database.


## Official SWAT+ Reference

- Official page: [aquifer.aqu](https://swatplus.gitbook.io/io-docs/introduction-1/aquifers/aquifer.aqu).
- Official index note: This file contains the general physical and chemical aquifer properties.
- Official field metadata available: 18 field row(s); matched to 18 of 18 observed demo header field(s).
- Demo cross-check: local header and first data row are still used below to show how this scenario instantiates the official format.

## Role In SWAT+

- Category: Aquifers.
- Usage class: `active scenario input`.
- Activation: `file.cio`.
- `Osu_1hru` status: `active`.
- Source inventory slot(s): `in_aqu%aqu = "aquifer.aqu"`.

## File Format

SWAT+ input files use a plain-text, free-format layout with space-delimited values. GitBook documents the general convention as a title line first, then usually a header line, with exceptions such as `file.cio` and files that add count or block-header lines.
This file is controlled by the master `file.cio` manifest in normal runs. A non-`null` entry activates the selected filename; `null` means the file slot is intentionally unused for that scenario.

Local demo evidence from `VSProj/SWAT/Osu_1hru/aquifer.aqu`:

- Title/comment line: `aquifer.aqu: written by SWAT+ editor v2.2.0 on 2023-03-22 04:25 for SWAT+ rev.60.5.4`.
- Observed header line: `id  name                          init        gw_flo       dep_bot        dep_wt         no3_n         sol_p        carbon      flo_dist        bf_max      alpha_bf         revap       rchg_dp      spec_yld       hl_no3n       flo_min     revap_min`.
- Nonblank records after the header: 21.
- First demo data record: `1  aqu011                    initaqu1       0.05000      10.00000       6.00000       0.00000       0.00000       0.50000      50.00000       1.00000       0.95000       0.02000       0.01000       0.05000       0.00000       5.00000       5.00000`.

## Fields And Parameters

The table merges the local demo header with official SWAT+ metadata when an official field definition is available. Rows marked `demo/source inferred` still need reader-level confirmation.

| Field | Meaning | Type | Unit | Default | Range | Demo value | Basis |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | ID of the aquifer. | `integer` | `n/a` | - | - | `1` | official GitBook |
| `name` | Name of the aquifer. | `string` | `n/a` | `n/a` | `n/a` | `aqu011` | official GitBook |
| `init` | Pointer to the aquifer initialization file. | `string` | `n/a` | `n/a` | `n/a` | `initaqu1` | official GitBook |
| `gw_flo` | Initial groundwater flow. | `real` | `mm` | `0.05` | `0-2` | `0.05000` | official GitBook |
| `dep_bot` | Depth from mid-slope surface to bottom of aquifer. | `real` | `m` | `10.0` | `0-10` | `10.00000` | official GitBook |
| `dep_wt` | Depth from mid-slope surface to initial water table. | `real` | `m` | `10.0` | `0-10` | `6.00000` | official GitBook |
| `no3_n` | NO3-N concentration in aquifer. | `real` | `ppm NO3-N` | `0` | `0-1000` | `0.00000` | official GitBook |
| `sol_p` | Mineral P concentration in aquifer. | `real` | `mg P/L` | `0` | `0-1000` | `0.00000` | official GitBook |
| `carbon` | Organic carbon in aquifer. | `real` | `percent` | `0.50` | `0-15` | `0.50000` | official GitBook |
| `flo_dist` | Average flow distance to stream or object. | `real` | `m` | `50.0` | `0-1000` | `50.00000` | official GitBook |
| `bf_max` | Baseflow rate at which all streams linked to an aquifer receive groundwater flow. | `real` | `mm` | `1.0` | `0-2` | `1.00000` | official GitBook |
| `alpha_bf` | Alpha factor for groundwater recession curve. | `real` | `1/days` | `0.05` | `0-1` | `0.95000` | official GitBook |
| `revap` | Groundwater revap coefficient. | `real` | `fraction` | `0` | `0-1` | `0.02000` | official GitBook |
| `rchg_dp` | Recharge to deep aquifer. | `real` | `fraction` | `0` | `0-1` | `0.01000` | official GitBook |
| `spec_yld` | Specific yield of the aquifer. | `real` | `m^3/m^3` | `0` | `0-0.40` | `0.05000` | official GitBook |
| `hl_no3n` | Half-life of NO3-N in the aquifer. | `real` | `days` | `0` | `0-200` | `0.00000` | official GitBook |
| `flo_min` | Threshold depth from surface to water table for groundwater flow to occur. | `real` | `m` | `3` | `0-10` | `5.00000` | official GitBook |
| `revap_min` | Threshold depth from surface to water table for revap to occur. | `real` | `m` | `5` | `0-10` | `5.00000` | official GitBook |

## Defaults And Conversions

- Defaults: use the source inventory filename and the `file.cio` slot state as the first default/activation check.
- Missing-file behavior: if the master file or upstream manifest uses `null`, SWAT+ treats that slot as inactive for the scenario.
- Numeric conversions: not yet traced for this page; inspect the reader for unit conversions, bounds checks, and derived runtime fields.

## Reader Path

- Source inventory: `SWATPLUS/swatplus/src/input_file_module.f90`.
- Source slot: `in_aqu%aqu` defaulting to `aquifer.aqu`.
- Candidate reader/source files: `SWATPLUS/swatplus/src/aqu_read.f90`.

## Downstream Consumers

Aquifer initialization, groundwater storage, and groundwater routing routines.

## Scenario Evidence

- Scenario: `VSProj/SWAT/Osu_1hru`.
- Scenario state: `active`.
- Activation evidence: `file.cio`.
- Local file evidence: `VSProj/SWAT/Osu_1hru/aquifer.aqu`.

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
