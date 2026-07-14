---
title: Osu_1hru file classification
kind: reference
status: partial
created: 2026-07-14
updated: 2026-07-14
source_revision: 5b3705b300d95ebe4914119f056548446bdc208f
scenario: Osu_1hru
tags: [scenario, inputs, outputs, generated-files, debugging]
---

# `Osu_1hru` File Classification

## Purpose

The `VSProj/SWAT/Osu_1hru` folder mixes real scenario inputs, weather time series, optional module inputs, generated outputs, soft-calibration support files, and local debug artifacts. This note separates those roles so debugging does not treat every file in the folder as a primary input.

Use this note to answer:

```text
Is this file an active input, optional input, generated output, support file, or local artifact?
```

Use [`input-files-catalog.md`](input-files-catalog.md) for one-line introductions to active input files.

## Classification Rules

| Class | Rule |
| --- | --- |
| Active manifest input | Listed directly in `file.cio` and not `null`. |
| Active weather time series | Reached through active `.cli` files, not listed directly in `file.cio`. |
| Optional or fixed-name input | Present in the folder and likely read by a module-specific or fixed-name reader, but not selected directly by the active `file.cio` rows. |
| Support / soft-calibration file | Looks like model support data, often `.swf`, but needs reader-path tracing before treating it as a primary input. |
| Generated output / runtime file | Written by a run, diagnostic, checker, or output routine. |
| Local artifact | Local debug/generated file not tracked or not part of the stable scenario definition. |

## Active Manifest Inputs

These are explicitly selected by `file.cio`.

| Group | Files |
| --- | --- |
| Simulation/basin | `time.sim`, `print.prt`, `object.cnt`, `codes.bsn`, `parameters.bsn` |
| Climate manifests | `weather-sta.cli`, `weather-wgn.cli`, `pcp.cli`, `tmp.cli`, `slr.cli`, `wnd.cli` |
| Connections | `hru.con`, `rout_unit.con`, `aquifer.con`, `recall.con`, `chandeg.con` |
| Channel / SWAT-DEG channel | `initial.cha`, `nutrients.cha`, `channel-lte.cha`, `hyd-sed-lte.cha` |
| Reservoir/wetland | `initial.res`, `sediment.res`, `nutrients.res`, `weir.res`, `wetland.wet`, `hydrology.wet` |
| Routing unit | `rout_unit.def`, `rout_unit.ele`, `rout_unit.rtu` |
| HRU | `hru-data.hru` |
| Recall | `recall.rec` |
| Aquifer | `initial.aqu`, `aquifer.aqu` |
| Hydrology/topography/field | `hydrology.hyd`, `topography.hyd`, `field.fld` |
| Structural | `tiledrain.str`, `septic.str`, `filterstrip.str`, `grassedww.str`, `bmpuser.str` |
| Parameter databases | `plants.plt`, `fertilizer.frt`, `tillage.til`, `pesticide.pes`, `urban.urb`, `septic.sep`, `snow.sno` |
| Operations | `harv.ops`, `graze.ops`, `irr.ops`, `chem_app.ops`, `fire.ops`, `sweep.ops` |
| Land use / management | `landuse.lum`, `management.sch`, `cntable.lum`, `cons_practice.lum`, `ovn_table.lum` |
| Calibration | `cal_parms.cal`, `calibration.cal` |
| Initial conditions | `plant.ini`, `soil_plant.ini`, `om_water.ini` |
| Soils | `soils.sol`, `nutrients.sol` |
| Decision tables | `lum.dtl`, `res_rel.dtl` |
| Regions | `ls_unit.ele`, `ls_unit.def`, `aqu_catunit.ele` |

## Active Weather Time-Series Files

These are not listed directly in `file.cio`; they are reached through active climate manifest files.

| File | Role |
| --- | --- |
| `Imsilpcp.pcp` | Precipitation time series. |
| `Imsiltmp.tmp` | Temperature time series. |
| `Imsilsol.slr` | Solar radiation time series. |
| `Imsilwind.wnd` | Wind-speed time series. |

## Optional Or Fixed-Name Inputs Present

These files exist in the folder but are not directly selected by the active `file.cio` rows. Treat them as optional/module-specific until the exact reader path is traced.

| File | Current classification |
| --- | --- |
| `cs_aqu.ini` | Optional generic constituent initialization for aquifer-related paths. Empty in this scenario. |
| `cs_channel.ini` | Optional generic constituent initialization for channel-related paths. Empty in this scenario. |
| `cs_hru.ini` | Optional generic constituent initialization for HRU-related paths. Empty in this scenario. |
| `salt_aqu.ini` | Optional salt initialization for aquifer-related paths. Empty in this scenario. |
| `salt_channel.ini` | Optional salt initialization for channel-related paths. Empty in this scenario. |
| `salt_hru.ini` | Optional salt initialization for HRU-related paths. Empty in this scenario. |
| `manure_db.frt` | Manure database support file; read by manure database routines when active. |
| `manure_om.frt` | Organic/mineral manure database support file. |
| `puddle.ops` | Puddling operation support file. |
| `transplant.plt` | Plant transplant support file. |
| `treatment.trt` | Treatment support file; empty in this scenario. |
| `calibration.cal.org` | Backup/original calibration file, not selected by `file.cio`. |

## Support / Soft-Calibration Files

These are present and may support calibration, checking, or SWIFT/soft-data workflows. Do not treat them as primary scenario inputs until the reader path is traced.

| File | Current classification |
| --- | --- |
| `aqu_dr.swf` | Soft-data/support file. |
| `chan_dat.swf` | Soft-data/support file. |
| `chan_dr.swf` | Soft-data/support file. |
| `file_cio.swf` | SWIFT/soft-data support file. |
| `hru_dat.swf` | Soft-data/support file. |
| `hru_exco.swf` | Soft-data/support file. |
| `hru_wet.swf` | Soft-data/support file. |
| `precip.swf` | Soft-data/support file. |
| `recall.swf` | Soft-data/support file; empty in this scenario. |
| `res_dat.swf` | Soft-data/support file. |
| `res_dr.swf` | Soft-data/support file. |

## Generated Outputs And Runtime Files

These are written or updated by runs/tools and should not be edited as stable inputs.

| File | Current classification |
| --- | --- |
| `area_calc.out` | Runtime/output file. |
| `checker.out` | Runtime checker output. |
| `co2.out` | Output written by CO2 setup. |
| `diagnostics.out` | Diagnostic log written on unit `9001`. |
| `erosion.out` | Runtime/output file. |
| `erosion.txt` | Runtime file opened by startup. |
| `files_out.out` | Output-file listing/status file. |
| `fort.2222` | Fortran runtime scratch/output artifact. |
| `mgt_out.txt` | Management output file. |
| `simulation.out` | Main simulation banner/status output. |

## Local Artifacts

| File | Current classification |
| --- | --- |
| `recall_db.rec` | Untracked local zero-byte file currently present in the debug scenario. Not part of the committed scenario definition. Leave untracked unless a traced reader proves it is required. |
| `2010` | Zero-byte file with unclear role. Treat as local/unknown until traced. |

## Practical Debugging Rule

When you see a file in `Osu_1hru`, classify it in this order:

1. Is it listed in `file.cio` and not `null`?
2. Is it referenced by an active `.cli` weather manifest?
3. Is it read by a fixed-name or optional module-specific reader?
4. Is it written by a run or diagnostic routine?
5. Is it a local artifact or leftover?

Only class 1 and class 2 should be assumed active without further reader-path tracing.

## Current Limits

Verified:

- Active manifest inputs are taken from `VSProj/SWAT/Osu_1hru/file.cio`.
- Weather time-series files are present and correspond to active climate manifests.
- `recall_db.rec` is untracked and zero bytes at the time of this note.

Still partial:

- Some optional/fixed-name files need exact reader-path tracing.
- `.swf` files need separate investigation if soft-data/SWIFT workflows become part of debugging.
- Generated-output classification is based on filenames and recent runtime updates; exact writer routines are not fully mapped here.

## Related Notes

- [`Osu_1hru` learning and debug scenario](osu-1hru-scenario.md)
- [SWAT+ input files catalog](input-files-catalog.md)
- [`file.cio` master input file](file-cio.md)
- [Input to output path](../input-output.md)
