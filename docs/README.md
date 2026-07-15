# SWAT+ Learning Notes

This is the main entrance for understanding the SWAT+ code in this workspace. Read this file first, then the three companion guides:

1. [`model-structure.md`](model-structure.md) - how the code is organized and which controller does what.
2. [`input-output.md`](input-output.md) - how scenario inputs move through readers, state, calculations, and outputs.
3. [`input-files.md`](input-files.md) - the map of SWAT+ input files and links to detailed input references.

Detailed per-input-file references live in [`inputs/`](inputs/). Broader conceptual notes live in [`topics/`](topics/). Raw live-debug notes live in [`internal/debug-inbox.md`](internal/debug-inbox.md).

During live debugging, write raw step-by-step observations in [`internal/debug-inbox.md`](internal/debug-inbox.md). Codex can later read that inbox and promote stable understanding into the suitable guide or topic files.

## Document Boundaries

| File | Role | Avoid putting here |
| --- | --- | --- |
| `README.md` | Main entrance, reading path, and current docs index. | Detailed code traces or field-by-field input definitions. |
| `model-structure.md` | Stable code/object/control-flow orientation. | Long input-file catalogs or raw debugger notes. |
| `input-output.md` | End-to-end tracing method and current input/output knowledge map. | Complete per-file reference tables. |
| `input-files.md` | Big map and classification of SWAT+ input files, including optional files. | Field-by-field details for one file. |
| `inputs/*.md` | Detailed reference page for one SWAT+ input file. | Broad model concepts or multi-file debugging narratives. |
| `topics/*.md` | Durable conceptual notes and scenario/workflow evidence for one focused topic. | Field-by-field input references or raw debugger notes. |
| `internal/debug-inbox.md` | Raw live-debug observations waiting for promotion. | Stable documentation that readers should depend on. |

## Mental Model

```text
scenario inputs
    -> file readers
    -> modules, derived types, arrays, and object indices
    -> main / time_control / command
    -> object controllers and process routines
    -> routing, aggregation, watched state, and output files
```

The important habit is to follow one value end to end. Do not infer behavior from a filename alone; trace the input, reader, storage field, controller, calculation, downstream consumers, and output.

## Current Understanding

| Area | Status | Start here |
| --- | --- | --- |
| Program entry and top-level control | Verified orientation map | [`model-structure.md`](model-structure.md) |
| Main-program generation | Verified | [`topics/main-program-generation.md`](topics/main-program-generation.md) |
| `time_control` and `command` dispatch | Verified orientation map | [`topics/simulation-control-flow.md`](topics/simulation-control-flow.md) |
| Input files map | Partial | [`input-files.md`](input-files.md) |
| `file.cio` input manifest | Partial | [`inputs/file-cio.md`](inputs/file-cio.md) |
| `codes.bsn` basin control codes | Partial | [`inputs/codes-bsn.md`](inputs/codes-bsn.md) |
| `parameters.bsn` basin parameters | Partial | [`inputs/parameters-bsn.md`](inputs/parameters-bsn.md) |
| `print.prt` output controls | Partial | [`inputs/print-prt.md`](inputs/print-prt.md) |
| CO2 and carbon input readers | Partial | [`topics/co2-carbon-inputs.md`](topics/co2-carbon-inputs.md) |
| `object.cnt` and object concepts | Partial | [`inputs/object-cnt.md`](inputs/object-cnt.md) |
| `om_water.ini` initial organic-mineral water state | Partial | [`inputs/om-water-ini.md`](inputs/om-water-ini.md) |
| Alternative object representations | Partial | [`topics/alternative-object-representations.md`](topics/alternative-object-representations.md) |
| QSWAT+ HRU to routing-unit generated structure | Partial | [`topics/qswat-hru-routing-unit.md`](topics/qswat-hru-routing-unit.md) |
| Visual Studio / Intel Fortran setup | Verified | [`topics/visual-studio-intel-fortran.md`](topics/visual-studio-intel-fortran.md) |
| `Osu_1hru` debug scenario | Partial | [`topics/osu-1hru-scenario.md`](topics/osu-1hru-scenario.md) |
| `Osu_1hru` file classification | Partial | [`topics/osu-1hru-file-classification.md`](topics/osu-1hru-file-classification.md) |
| DeepWiki as an external source explorer | Verified usage rule | [`topics/deepwiki-swatplus.md`](topics/deepwiki-swatplus.md) |

## Required Reading Path

Read these three files to get the major ideas without getting lost:

1. This file.
2. [`model-structure.md`](model-structure.md).
3. [`input-output.md`](input-output.md).
4. [`input-files.md`](input-files.md).

Use the topic notes only when you need detailed evidence, source paths, or unresolved technical boundaries.

## Next Learning Targets

1. Finish tracing `file.cio`: parse loop, storage type, and one filename consumer such as `time.sim`.
2. Continue tracing `object.cnt` connection inputs into the exact `command` object sequence for `Osu_1hru`.
3. Trace one daily precipitation value from weather input through HRU water balance to output.
4. Map the internal process order called by `hru_control` for the configured full HRU.

## Status Vocabulary

| Status | Meaning |
| --- | --- |
| `verified` | Supported by source evidence or a reproducible runtime observation. |
| `partial` | Some path or behavior is verified, but important boundaries remain. |
| `hypothesis` | Plausible observation that still needs evidence. |
| `superseded` | Historical record replaced by a newer note, trace, or decision. |

## Writing Rules

- Keep this file as the single learning entrance.
- Keep root [`README.md`](../README.md) short and focused on workspace setup.
- Put detailed input-file references under [`inputs/`](inputs/).
- Put durable conceptual notes directly under [`topics/`](topics/).
- Put live debugger observations in [`internal/debug-inbox.md`](internal/debug-inbox.md).
- Keep one clear topic per note and include `status`, `source_revision`, and `scenario` metadata in substantive notes.
