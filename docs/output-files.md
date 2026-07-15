---
title: SWAT+ output files map
kind: reference
status: partial
created: 2026-07-15
updated: 2026-07-15
source_revision: cb442f7c05fc3bfc34349c446010f452d2737ca0
scenario: Osu_1hru
tags: [outputs, print-prt, object-prt, catalog]
---

# SWAT+ Output Files Map

## Scope

This file is the output-side companion to [`input-files.md`](input-files.md). It explains output-file classes, print controls, and the evidence expected before adding detailed output references. It does not duplicate field-by-field input definitions from [`inputs/`](inputs/).

Use [`tracing-guide.md`](tracing-guide.md) when following one value from input to reader, state, calculation, and output. Use [`inputs/simulation/print-prt.md`](inputs/simulation/print-prt.md) for the current input-side understanding of output print controls.

## External Format Baseline

SWAT+ output files are plain text, free-format, and space-delimited. The first line is a title, the second line is the column header, and the third line gives units. Output writing is mainly controlled by `print.prt`; selected object outputs can also be controlled by `object.prt`; some debugging files are printed every run. External reference: [SWAT+ Output File Format](https://swatplus.gitbook.io/io-docs/swat+-output-files/output-file-format).

Local writer routines, `print.prt`, `object.prt`, and the active scenario remain the authority for whether a specific output is written here.

## Output Classes

| Class | Meaning |
| --- | --- |
| `print-controlled output` | Normal model output controlled by `print.prt` rows and reporting frequencies. |
| `selected-object output` | Output limited to selected objects, controlled by `object.prt` when that file is used. |
| `always-written/runtime output` | Banner, status, diagnostics, or file-list outputs written by startup or support routines. |
| `debug/checker output` | Checker, diagnostic, or debug files that help validate a run but are not primary model result tables. |
| `local artifact/output-like` | Files present in a scenario folder whose role is not yet proven by a writer trace. |

## Control Inputs

| Input | Role | Reference |
| --- | --- | --- |
| `file.cio` | Starts the run and can set the output path record read by `readcio_read`. | [`inputs/simulation/file-cio.md`](inputs/simulation/file-cio.md) |
| `print.prt` | Main output-control input for daily, monthly, yearly, and average annual output groups. | [`inputs/simulation/print-prt.md`](inputs/simulation/print-prt.md) |
| `object.prt` | Optional selected-object output control. | [`inputs/simulation/object-prt.md`](inputs/simulation/object-prt.md) |

## Starter Output Inventory For `Osu_1hru`

These files are observed or classified in the current scenario notes. Treat the map as a starting point until each writer routine, frequency, units row, and reset timing is traced.

| File | Current class | Trace status |
| --- | --- | --- |
| `simulation.out` | `always-written/runtime output` | Startup/status writer identified at a high level; detailed format not traced. |
| `files_out.out` | `always-written/runtime output` | Output-file listing/status file; writer path still needs detailed tracing. |
| `diagnostics.out` | `debug/checker output` | Diagnostic log written on unit `9001`; detailed producer map still partial. |
| `checker.out` | `debug/checker output` | Runtime checker output; detailed producer map not traced. |
| `co2.out` | `debug/checker output` | CO2 setup output; writer and conditions need field-level tracing. |
| `area_calc.out` | `debug/checker output` | Runtime/output-like file; writer not yet traced. |
| `erosion.out` | `debug/checker output` | Runtime/output-like file; writer not yet traced. |
| `erosion.txt` | `always-written/runtime output` | Opened during startup in the current source trace; detailed role still partial. |
| `mgt_out.txt` | `print-controlled output` | Management output file related to `print.prt` `mgtout`; writer and columns not yet traced. |
| `fort.2222` | `local artifact/output-like` | Fortran runtime scratch/output artifact; do not treat as a stable SWAT+ output table yet. |

## Output Reference Pages

Detailed output pages should live under [`outputs/`](outputs/) once writer routines and units are traced. Do not generate broad output stubs until the inventory is stable enough to avoid misleading readers.

Expected future folders include debugging, soil, management, flow-duration, water-balance, nutrient-balance, losses, plant-weather, channel, aquifer, reservoir, recall, hydrographs, routing-unit, pesticides, and selected objects.

## Evidence Required For A Detailed Output Page

Record these before marking any output page more than `partial`:

1. The input control that enables the output.
2. The writer routine and unit number.
3. The file name and path behavior.
4. Reporting frequency and aggregation period.
5. Header and units rows.
6. Object index or spatial unit represented by each row.
7. Reset timing for accumulated variables.
8. A watched internal value that can be compared to the file.

## Related Notes

- [`tracing-guide.md`](tracing-guide.md)
- [`input-files.md`](input-files.md)
- [`topics/osu-1hru-file-classification.md`](topics/osu-1hru-file-classification.md)
- [`topics/simulation-control-flow.md`](topics/simulation-control-flow.md)
