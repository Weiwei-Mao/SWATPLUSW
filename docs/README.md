# SWAT+ Learning Notes

This is the main entrance for understanding the SWAT+ code in this workspace. Read this file first, then the companion guides:

1. [`model-structure.md`](model-structure.md) - how the code is organized and which controller does what.
2. [`tracing-guide.md`](tracing-guide.md) - how scenario inputs move through readers, state, calculations, and outputs.
3. [`input-files.md`](input-files.md) - the categorized map of SWAT+ input files, including core, active, optional, conditional, indirect, and companion files.
4. [`output-files.md`](output-files.md) - the output-file map, print controls, output classes, and evidence needed before output pages are detailed.

Per-input-file references and stubs live in categorized subfolders under [`inputs/`](inputs/). Output-file references will be added under [`outputs/`](outputs/) once writer routines are traced. Broader conceptual notes live in [`topics/`](topics/). Raw live-debug notes live in [`internal/debug-inbox.md`](internal/debug-inbox.md).

During live debugging, write raw step-by-step observations in [`internal/debug-inbox.md`](internal/debug-inbox.md). Codex can later read that inbox and promote stable understanding into the suitable guide or topic files.

## Document Boundaries

| File | Role | Avoid putting here |
| --- | --- | --- |
| `README.md` | Main entrance, reading path, and current docs index. | Detailed code traces or field-by-field input/output definitions. |
| `model-structure.md` | Stable code/object/control-flow orientation. | Long input-file catalogs or raw debugger notes. |
| `tracing-guide.md` | End-to-end tracing method from input to reader, state, calculations, and output. | Complete per-file reference tables. |
| `input-files.md` | Big map and classification of SWAT+ input files, including optional and conditional files. | Field-by-field details for one file. |
| `output-files.md` | Output-file classes, print controls, starter output map, and required tracing evidence. | Input-file field tables or untraced output claims. |
| `inputs/**/*.md` | Detailed reference or stub page for one SWAT+ input file or file family. | Broad model concepts or multi-file debugging narratives. |
| `outputs/**/*.md` | Detailed reference page for one output file or output family, once traced. | Input controls except where needed as output evidence. |
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
| Output files map | Partial | [`output-files.md`](output-files.md) |
| `file.cio` input manifest | Partial | [`inputs/simulation/file-cio.md`](inputs/simulation/file-cio.md) |
| `codes.bsn` basin control codes | Partial | [`inputs/basin/codes-bsn.md`](inputs/basin/codes-bsn.md) |
| `parameters.bsn` basin parameters | Partial | [`inputs/basin/parameters-bsn.md`](inputs/basin/parameters-bsn.md) |
| `print.prt` output controls | Partial | [`inputs/simulation/print-prt.md`](inputs/simulation/print-prt.md) |
| CO2 and carbon input readers | Partial | [`topics/co2-carbon-inputs.md`](topics/co2-carbon-inputs.md) |
| `object.cnt` and object concepts | Partial | [`inputs/simulation/object-cnt.md`](inputs/simulation/object-cnt.md) |
| `om_water.ini` initial organic-mineral water state | Partial | [`inputs/initialization/om-water-ini.md`](inputs/initialization/om-water-ini.md) |
| Alternative object representations | Partial | [`topics/alternative-object-representations.md`](topics/alternative-object-representations.md) |
| QSWAT+ HRU to routing-unit generated structure | Partial | [`topics/qswat-hru-routing-unit.md`](topics/qswat-hru-routing-unit.md) |
| Visual Studio / Intel Fortran setup | Verified | [`topics/visual-studio-intel-fortran.md`](topics/visual-studio-intel-fortran.md) |
| `Osu_1hru` debug scenario | Partial | [`topics/osu-1hru-scenario.md`](topics/osu-1hru-scenario.md) |
| `Osu_1hru` file classification | Partial | [`topics/osu-1hru-file-classification.md`](topics/osu-1hru-file-classification.md) |
| DeepWiki as an external source explorer | Verified usage rule | [`topics/deepwiki-swatplus.md`](topics/deepwiki-swatplus.md) |

## Required Reading Path

Read these files to get the major ideas without getting lost:

1. This file.
2. [`model-structure.md`](model-structure.md).
3. [`tracing-guide.md`](tracing-guide.md).
4. [`input-files.md`](input-files.md).
5. [`output-files.md`](output-files.md).

Use the topic notes only when you need detailed evidence, source paths, or unresolved technical boundaries.

## Next Learning Targets

1. Finish tracing `file.cio`: parse loop, storage type, and one filename consumer such as `time.sim`.
2. Continue tracing `object.cnt` connection inputs into the exact `command` object sequence for `Osu_1hru`.
3. Trace one daily precipitation value from weather input through HRU water balance to output.
4. Map the internal process order called by `hru_control` for the configured full HRU.
5. Start the first detailed output-file page only after its writer routine and units row are traced.

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
- Put detailed input-file references and explicit stubs under categorized [`inputs/`](inputs/) folders.
- Put detailed output-file references under [`outputs/`](outputs/) only after writer evidence is traced.
- Put durable conceptual notes directly under [`topics/`](topics/).
- Put live debugger observations in [`internal/debug-inbox.md`](internal/debug-inbox.md).
- Keep one clear topic per note and include `status`, `source_revision`, and `scenario` metadata in substantive notes.
