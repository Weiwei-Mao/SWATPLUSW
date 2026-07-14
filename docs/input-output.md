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
| Reader identity | `readcio_read.f90` opens `file.cio`; `input_file_module.f90` stores filenames such as `in_basin%codes_bas`. | Partial: some downstream consumers still need tracing. |
| Basin control codes | `codes.bsn` is read by `basin_read_cc.f90` into `bsn_cc`, setting basin-wide model switches. | Partial: field meanings mapped; not every consumer traced. |
| Basin numeric parameters | `parameters.bsn` is read by `basin_read_prm.f90` into `bsn_prm`, then adjusted by `basin_prm_default.f90`. | Partial: field meanings mapped; not every consumer traced. |
| Output controls | `print.prt` is read by `basin_print_codes_read.f90` into `pco`, setting output frequencies and file-format flags. | Partial: main fields mapped; exact file writers still need deeper tracing. |
| CO2 and carbon setup | `co2_read.f90` resolves annual CO2 values; `carbon_bsn_read.f90` reads dynamic carbon parameters only when `codes.bsn` has `carbon = 2`; `carbon_layers_read.f90` optionally controls per-layer carbon output depth. | Partial: reader functions and input-file formats mapped; downstream carbon calculations still need tracing. |
| Initial organic-mineral water state | `om_water.ini` is read by `om_water_init.f90` into named `hyd_output` records, then selected by init files such as `initial.cha` through names like `no_init`. | Partial: channel path verified for `Osu_1hru`; reservoir, wetland, and aquifer paths need scenario-specific tracing. |
| Object inventory | `object.cnt` is read by `basin_read_objs.f90` into `bsn` and `sp_ob`, setting object counts for allocation, connection reading, and command dispatch. | Partial: object concepts mapped; exact `Osu_1hru` command order still needs final trace. |
| QSWAT-generated HRU routing | In the Robin/QSWAT workflow, each HRU is effectively wrapped by one routing unit. `hru.con` has no direct outputs; `rout_unit.ele` and `rout_unit.def` map HRUs to routing units; `rout_unit.con` stores downstream routing. | Partial: verified for Robin; do not generalize to all hand-written SWAT+ inputs. |
| Program control | `main` initializes input/object state, then normal runs enter `time_control` and daily `command` dispatch. | Verified orientation map. |
| Object dispatch | `command` dispatches configured object types, including full HRUs through `hru_control`. | Verified orientation map; scenario-specific object sequence still needs tracing. |
| Outputs | Output production and column-level mappings are not yet traced. | Not yet mapped. |

## First Detailed Trace

The active trace is `file.cio`:

- Detailed note: [`topics/file-cio.md`](topics/file-cio.md)
- Input files catalog: [`topics/input-files-catalog.md`](topics/input-files-catalog.md)
- Basin control note: [`topics/codes-bsn.md`](topics/codes-bsn.md)
- Basin parameter note: [`topics/parameters-bsn.md`](topics/parameters-bsn.md)
- Output control note: [`topics/print-prt.md`](topics/print-prt.md)
- CO2/carbon input note: [`topics/co2-carbon-inputs.md`](topics/co2-carbon-inputs.md)
- Initial organic-mineral water note: [`topics/om-water-ini.md`](topics/om-water-ini.md)
- Object inventory note: [`topics/object-cnt.md`](topics/object-cnt.md)
- QSWAT-generated HRU/routing-unit note: [`topics/qswat-hru-routing-unit.md`](topics/qswat-hru-routing-unit.md)
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
