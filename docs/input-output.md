---
title: SWAT+ input to output path
kind: guide
status: partial
created: 2026-07-13
updated: 2026-07-13
source_revision: cb442f7c05fc3bfc34349c446010f452d2737ca0
scenario: Osu_1hru
tags: [guide, inputs, outputs, tracing]
---

# SWAT+ Input To Output Path

This guide explains the learning path we use for SWAT+: start with a concrete scenario input, trace it through source and state, then connect it to watched values or output files.

## The Practical Chain

```text
file.cio
    -> named input files
    -> readers
    -> modules/types/arrays
    -> object sequence and process routines
    -> routing/aggregation
    -> output files or watched debugger state
```

The first scenario is [`VSProj/SWAT/Osu_1hru`](../VSProj/SWAT/Osu_1hru/). It is small enough for breakpoints and watches, but it only proves code paths that are active in that scenario.

## What Is Known

| Stage | Current understanding | Status |
| --- | --- | --- |
| Master input manifest | `file.cio` lists the scenario input files by section. | Partial: format and reader identified. |
| Reader identity | `readcio_read.f90` opens `file.cio`; `input_file_module.f90` is expected to hold related structures. | Partial: parse loop and fields not fully traced. |
| Program control | `main` initializes input/object state, then normal runs enter `time_control` and daily `command` dispatch. | Verified orientation map. |
| Object dispatch | `command` dispatches configured object types, including full HRUs through `hru_control`. | Verified orientation map; scenario-specific object sequence still needs tracing. |
| Outputs | Output production and column-level mappings are not yet traced. | Not yet mapped. |

## First Detailed Trace

The active trace is `file.cio`:

- Detailed note: [`topics/file-cio.md`](topics/file-cio.md)
- Scenario note: [`topics/osu-1hru-scenario.md`](topics/osu-1hru-scenario.md)
- Related control map: [`topics/simulation-control-flow.md`](topics/simulation-control-flow.md)

The next step is to read `readcio_read.f90` in full, identify the exact derived type and fields that receive filenames, then follow one filename such as `time.sim` into its own reader.

## Output Caution

Do not assume an output column proves a calculation until the producer is traced. For each output, record:

- the print-control input that enables it;
- the writer routine and output file;
- the aggregation period;
- the object index or spatial unit;
- the units and reset timing;
- the watched internal value used to compare against the file.

Until that chain is proven, output-related notes should stay `partial` or `hypothesis`.
