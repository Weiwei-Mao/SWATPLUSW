---
title: file.cio master input file
kind: knowledge
status: partial
created: 2026-07-11
updated: 2026-07-11
source_revision: cb442f7c05fc3bfc34349c446010f452d2737ca0
scenario: Osu_1hru
tags: [inputs, file-cio, reader, input-dispatch]
---

# `file.cio` — master input file

## Summary

`file.cio` is the SWAT+ **master input manifest**: a flat text file that lists, section by section, every input file the scenario uses. The model reads it first to learn which files to open and what role each plays. A `null` in a slot means that position is unused. Changing scenarios is largely a matter of pointing `file.cio` at a different set of files.

## Scope

Covers the on-disk format of `file.cio` and the identity of its reader, verified against the `Osu_1hru` scenario at revision `cb442f7`. Does **not** yet cover the internal parse loop, the derived type that stores the filenames, or how each filename is later consumed by per-section readers — see Unresolved boundaries.

## Inputs and configuration

Format: plain text, one logical record per line. Each line is:

```text
<section_keyword>  <file1>  <file2>  ...  null  null  ...
```

- The leading lowercase token is the section name.
- The remaining whitespace-separated tokens are filenames (or `null`) for that section's fixed slots.
- Line 1 is an editor comment (`written by SWAT+ editor ...`), not data.

Sections observed in `Osu_1hru/file.cio` and the files they activate (representative):

| section | files activated |
| --- | --- |
| `simulation` | `time.sim`, `print.prt`, `object.cnt` |
| `basin` | `codes.bsn`, `parameters.bsn` |
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

The `Osu_1hru` file was written by SWAT+ editor v2.2.0 for rev.60.5.4; the input format is compatible with our rev.62 source.

## Data structures

**Not yet verified.** The parsed section->filename map is expected to live in a derived type defined in [`input_file_module.f90`](../../../SWATPLUS/swatplus/src/input_file_module.f90) (its header comment at line 5 says `!! file.cio input file`). Confirm by reading `readcio_read.f90`'s parse loop and the module's type definitions.

## Control and calculation path

- `program main` calls `proc_read` (see [`main.f90.in`](../../../SWATPLUS/swatplus/src/main.f90.in), the `call proc_read` line).
- `proc_read` is expected to call the `file.cio` reader early, since every other input file depends on the filenames it supplies.
- Reader: subroutine in [`readcio_read.f90`](../../../SWATPLUS/swatplus/src/readcio_read.f90):
  - L19 `!! read file.cio`
  - L20 `inquire(file="file.cio", exist=i_exist)`
  - L22 `open(107, file="file.cio")`

The exact call edge from `proc_read` and the per-section dispatch that follows are **not yet traced**.

## Outputs and downstream effects

`file.cio` has no direct physical output; its effect is to **gate which other input files are opened**. Every section reader downstream consumes the filename it was handed here. [`swift_output.f90`](../../../SWATPLUS/swatplus/src/swift_output.f90) can also write a new `file.cio` (L75-77) for SWIFT coupling.

## Evidence

- [`Osu_1hru/file.cio`](../../../VSProj/SWAT/Osu_1hru/file.cio): the 32-line manifest inspected directly.
- [`readcio_read.f90`](../../../SWATPLUS/swatplus/src/readcio_read.f90) L19-22: reader identification (inquire + open).
- [`input_file_module.f90`](../../../SWATPLUS/swatplus/src/input_file_module.f90) L5: header comment marking the file.cio input module (structure not yet read).

## Unresolved boundaries

- The parse loop in `readcio_read.f90` (how section keywords are matched and how many slots each section reads) — not yet read.
- The exact derived type/field that stores the filenames in `input_file_module.f90` — not yet read.
- The call edge from `proc_read` to the `file.cio` reader — assumed, not yet confirmed in source.
- How a specific filename (e.g. `time.sim`) is then passed to its own reader — not yet traced.

Status stays `partial` until the reader -> structure -> consumer chain is confirmed.

## Change guidance

- To change which input files a scenario uses, edit `file.cio` (or regenerate via the editor), not the source.
- A source change to how `file.cio` is parsed belongs in `readcio_read.f90`; a change to the storage type belongs in `input_file_module.f90`.

## Related notes

- [Main-program generation](../architecture/main-program-generation.md)
- [Simulation control flow](../architecture/simulation-control-flow.md)
- Journal: [2026-07-11 file.cio trace start](../../journal/2026/2026-07-11-file-cio-trace.md)
