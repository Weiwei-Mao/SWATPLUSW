---
title: file.cio master input file
kind: input-reference
status: partial
created: 2026-07-11
updated: 2026-07-15
source_revision: cb442f7c05fc3bfc34349c446010f452d2737ca0
scenario: Osu_1hru
tags: [inputs, file-cio, reader, input-dispatch]
---

# `file.cio` Master Input File

## Summary

`file.cio` is the SWAT+ master input manifest: a flat text file that lists, section by section, the input files a scenario uses. The model reads it first so later readers know which files to open. A `null` value means that slot is unused.

## Scope

This note covers the on-disk format of `file.cio`, the startup call path into its reader, the high-level read loop, and the module-level filename records that receive parsed values. It does not yet trace how every stored filename is later consumed by its own section reader.

## Inputs And Configuration

Format: plain text, one logical section record per line.

```text
<section_keyword>  <file1>  <file2>  ...  null  null  ...
```

- The leading token is the section name.
- The remaining whitespace-separated tokens are filenames or `null`.
- Line 1 is an editor comment, not data.

Sections observed in `Osu_1hru/file.cio` and representative files they activate:

| Section | Files activated |
| --- | --- |
| `simulation` | `time.sim`, `print.prt`, `object.cnt` |
| `basin` | `codes.bsn`, `parameters.bsn`, optional carbon file slot currently `null` |
| `climate` | `weather-sta.cli`, `weather-wgn.cli`, `pcp.cli`, `tmp.cli`, `slr.cli`, `wnd.cli` |
| `connect` | `hru.con`, `rout_unit.con`, `aquifer.con`, `recall.con`, `chandeg.con` |
| `channel` | `initial.cha`, `nutrients.cha`, `channel-lte.cha`, `hyd-sed-lte.cha` |
| `reservoir` | `initial.res`, `sediment.res`, `nutrients.res`, `weir.res`, `wetland.wet`, `hydrology.wet` |
| `routing_unit` | `rout_unit.def`, `rout_unit.ele`, `rout_unit.rtu` |
| `hru` | `hru-data.hru` |
| `aquifer` | `initial.aqu`, `aquifer.aqu` |
| `hydrology` | `hydrology.hyd`, `topography.hyd`, `field.fld` |
| `structural` | `tiledrain.str`, `septic.str`, `filterstrip.str`, `grassedww.str`, `bmpuser.str` |
| `hru_parm_db` | `plants.plt`, `fertilizer.frt`, `tillage.til`, `pesticide.pes`, `urban.urb`, `septic.sep`, `snow.sno` |
| `ops` | `harv.ops`, `graze.ops`, `irr.ops`, `chem_app.ops`, `fire.ops`, `sweep.ops` |
| `lum` | `landuse.lum`, `management.sch`, `cntable.lum`, `cons_practice.lum`, `ovn_table.lum` |
| `chg` | `cal_parms.cal`, `calibration.cal` |
| `init` | `plant.ini`, `soil_plant.ini`, `om_water.ini` |
| `soils` | `soils.sol`, `nutrients.sol` |
| `decision_table` | `lum.dtl`, `res_rel.dtl` |
| `regions` | `ls_unit.ele`, `ls_unit.def`, `aqu_catunit.ele` |

For the full input-file map, including optional files not active in this scenario, see [`input-files.md`](../../input-files.md).

## Data Structures

`file.cio` filenames are stored in module-level derived-type instances defined in [`input_file_module.f90`](../../../SWATPLUS/swatplus/src/input_file_module.f90). Examples:

| `file.cio` section | Stored object |
| --- | --- |
| `simulation` | `in_sim` |
| `basin` | `in_basin` |
| `climate` | `in_cli` |
| `connect` | `in_con` |
| `channel` | `in_cha` |
| `reservoir` | `in_res` |
| `routing_unit` | `in_ru` |
| `hru` | `in_hru` |

Each object has default filenames in its type definition. `readcio_read` then overwrites those fields from the active scenario's `file.cio`.

## Control And Reader Path

- [`main.f90.in`](../../../SWATPLUS/swatplus/src/main.f90.in) writes the startup banner, opens `simulation.out` on unit `9003`, opens `erosion.txt` on unit `888`, then calls `proc_bsn`.
- [`proc_bsn.f90`](../../../SWATPLUS/swatplus/src/proc_bsn.f90) calls `readcio_read` before opening diagnostic/output-list files and before calling basin/time readers.
- [`readcio_read.f90`](../../../SWATPLUS/swatplus/src/readcio_read.f90) is the `file.cio` reader:
  - L19-22: check for `file.cio` and open it on unit `107`.
  - L23: read the title/comment line.
  - L24-105: read section records into `in_sim`, `in_basin`, `in_cli`, `in_con`, and related module objects.
  - L109: close unit `107`.
  - L111-112: initialize the output path from the optional output-path record.

## Outputs And Downstream Effects

`file.cio` has no direct physical model output. Its effect is to gate which other input files are opened. Every downstream section reader consumes filenames stored by this first read. [`swift_output.f90`](../../../SWATPLUS/swatplus/src/swift_output.f90) can also write a new `file.cio` for SWIFT coupling.

## Evidence

- [`Osu_1hru/file.cio`](../../../VSProj/SWAT/Osu_1hru/file.cio): scenario manifest inspected directly.
- [`main.f90.in`](../../../SWATPLUS/swatplus/src/main.f90.in) L27-40: startup banner/output files and first call to `proc_bsn`.
- [`proc_bsn.f90`](../../../SWATPLUS/swatplus/src/proc_bsn.f90) L8-12: declares and calls `readcio_read`.
- [`readcio_read.f90`](../../../SWATPLUS/swatplus/src/readcio_read.f90) L19-112: reader identification, unit `107`, section reads, close, and output-path initialization.
- [`input_file_module.f90`](../../../SWATPLUS/swatplus/src/input_file_module.f90) L7-310: module-level filename records such as `in_sim`, `in_basin`, `in_cli`, and weather path records.

## Unresolved Boundaries

- The exact field-level mapping for every `file.cio` slot has not been fully tabulated.
- How a specific filename, such as `time.sim`, is passed from `in_sim` into its own reader is not yet traced.
- Output-path behavior is identified in `readcio_read`, but not yet followed into output writers.

Status stays `partial` until at least one stored filename is followed into its downstream reader and a concrete output or watched state.

## Change Guidance

- To change which input files a scenario uses, edit `file.cio` or regenerate it through the SWAT+ editor.
- A source change to how `file.cio` is parsed belongs in `readcio_read.f90`.
- A change to filename storage belongs in `input_file_module.f90`.

## Related Notes

- [Main-program generation](../../topics/main-program-generation.md)
- [Simulation control flow](../../topics/simulation-control-flow.md)
- [Input files catalog](../../input-files.md)
- [`codes.bsn` basin control codes](../basin/codes-bsn.md)
- [CO2 and carbon input readers](../../topics/co2-carbon-inputs.md)
- [`print.prt` output control file](print-prt.md)
