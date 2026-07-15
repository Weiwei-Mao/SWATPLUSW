---
title: Input and output documentation classification structure
status: approved-for-design
created: 2026-07-15
scope: docs
---

# Input And Output Documentation Classification Structure

## Goal

Refine the SWAT+ documentation structure so readers can quickly answer:

- which input files are basic/core files;
- which files are active in the current `Osu_1hru` scenario;
- which files are optional, conditional, indirect, or fixed-name companions;
- where detailed input references live;
- where output-file knowledge belongs;
- how to trace one value from input through runtime state to output.

The current `docs/input-files.md` maps 170 input entries and every entry has a `docs/inputs/*.md` page. That is the right coverage level, but the flat `docs/inputs/` folder is too large, and the usage classes are not explicit enough. The tracing guide is also not an output-file catalog.

## External Reference Basis

Use the SWAT+ IO documentation as an external reference, not as a blind replacement for local source evidence:

- Input files are free-format and space-delimited. The first line is a title; most input files have a second header line, while `file.cio` is the exception. Source: <https://swatplus.gitbook.io/io-docs/introduction-1/input-file-format>
- Output files are also free-format and space-delimited, with title, header, and units lines. Many output files are controlled by `print.prt`; selected object outputs can also be controlled by `object.prt`; some debugging outputs are printed every run. Source: <https://swatplus.gitbook.io/io-docs/swat+-output-files/output-file-format>
- GitBook categories should guide folder names and map groupings where they match local SWAT+ source structure. Local source files and the active scenario remain the authority for whether a file is actually used in this workspace.

## Target Top-Level Docs

```text
docs/
  README.md
  model-structure.md
  tracing-guide.md
  input-files.md
  output-files.md
  inputs/
    simulation/
    basin/
    climate/
    climate-timeseries/
    connectivity/
    channels/
    reservoirs-wetlands/
    routing-units/
    hru/
    hydrology/
    soils/
    landuse-management/
    operations/
    structural/
    databases/
    initialization/
    constituents-salt/
    calibration/
    regions/
    water-allocation/
    livestock/
    point-sources-inlets/
  outputs/
    debugging/
    soil/
    management/
    flow-duration/
    water-balance/
    nutrient-balance/
    losses/
    plant-weather/
    channel/
    aquifer/
    reservoir/
    recall/
    hydrographs/
    routing-unit/
    pesticides/
    objects/
```

## File Roles

`docs/input-files.md` is the authoritative input map. It defines usage classes, category meanings, source-of-truth rules, and the full file map. It should answer whether a file is basic/core, active, indirect, conditional, optional/default, or fixed-name/companion.

`docs/inputs/**/<file>.md` contains one page per input file or input-file family. These pages may be detailed references or stubs. Moving them into category subfolders is a navigation change, not a claim that every page is complete.

`docs/output-files.md` is the output-file map. It should focus on output file classes, print controls, output frequencies, units rows, writer routines, and debugging outputs. It should not duplicate input-file field tables.

`docs/outputs/**/<file>.md` can be added incrementally for output files once output writers and units are traced. Do not generate hundreds of output stubs until there is a stable output inventory.

`docs/tracing-guide.md` explains the chain from input to reader to storage to calculations to output. It should link to both `input-files.md` and `output-files.md`.

`docs/topics/*.md` remains for conceptual notes, scenario notes, external-source notes, and workflow-specific observations.

## Input Usage Classes

`input-files.md` should define these classes near the top:

| Usage class | Meaning |
| --- | --- |
| `core` | Basic files needed for nearly every normal SWAT+ run. Examples: `file.cio`, `time.sim`, `print.prt`, `object.cnt`, `codes.bsn`, `parameters.bsn`. |
| `active scenario input` | Selected directly by the current `Osu_1hru/file.cio` and not `null`. |
| `indirect input` | Reached through another input file rather than directly through `file.cio`, such as climate time-series files named by `.cli` manifests. |
| `conditional input` | Used only when a model switch, object count, module, or process is active, such as carbon, salt, constituents, GWFLOW, water allocation, soft calibration, or livestock. |
| `optional/default` | Defined by source defaults but not required for the current scenario. |
| `fixed-name companion` | Opened by convention or derived from another file name, such as `carbon_lyr.bsn` and `carbon_layers.prt`. |
| `local artifact/output-like` | Present in a scenario folder but not a stable input until a reader path proves it. Example: untracked `recall_db.rec`. |

These classes are not mutually exclusive in plain English, so the table should separate durable usage and current-scenario state:

| Column | Purpose |
| --- | --- |
| `Usage class` | Durable role, such as `core`, `conditional input`, or `optional/default`. |
| `Activation` | Why SWAT+ reads it: `file.cio`, another manifest, a switch, an object count, a fixed-name reader, or not yet traced. |
| `Osu_1hru status` | `active`, `inactive/null`, `indirect`, `not present`, or `local artifact`. |
| `Reference` | Link to the categorized `docs/inputs/...` page. |

## Input Categories

Use category folders that are stable and understandable:

| Folder | Contents |
| --- | --- |
| `simulation/` | `file.cio`, `time.sim`, `print.prt`, `object.cnt`, `object.prt`, `constituents.cs`. |
| `basin/` | `codes.bsn`, `parameters.bsn`, carbon and CO2 basin companions. |
| `climate/` | Climate manifest files such as `weather-sta.cli`, `pcp.cli`, `tmp.cli`, `slr.cli`, `wnd.cli`, `hmd.cli`, `pet.cli`, `atmodep.cli`. |
| `climate-timeseries/` | File-family pages for `*.pcp`, `*.tmp`, `*.slr`, `*.wnd`, `*.hmd`, `*.pet`. |
| `connectivity/` | `.con`, `.lin`, and related routing/connectivity files. |
| `channels/` | Channel and SWAT-DEG channel files. |
| `reservoirs-wetlands/` | Reservoir, pond, and wetland inputs. |
| `routing-units/` | Routing-unit definition, element, parameter, and delivery-ratio files. |
| `hru/` | Full HRU and HRU-LTE files. |
| `hydrology/` | HRU hydrology, field, and topography files. |
| `soils/` | Soil profile and nutrient/soil-test files. |
| `landuse-management/` | Land-use management, schedules, curve-number and conservation-practice files. |
| `operations/` | Operation scheduling files such as harvest, grazing, irrigation, chemical application, fire, sweep, puddle, and treatment. |
| `structural/` | Tile drains, septic, filter strip, grassed waterway, BMP user, and shade factor. |
| `databases/` | Plant, fertilizer, tillage, pesticide, urban, septic, snow, manure, pathogens, metals, and salt databases. |
| `initialization/` | Plant, soil/plant, organic-mineral water, pesticide/pathogen/heavy-metal/salt initialization files. |
| `constituents-salt/` | Fixed-name constituent and salt module files not already better classified. |
| `calibration/` | Calibration and soft-calibration files. |
| `regions/` | Landscape, channel, aquifer, reservoir, and recall region/category-unit files. |
| `water-allocation/` | Water-rights and allocation files. |
| `livestock/` | Animal, herd, and ranch files. |
| `point-sources-inlets/` | Recall and export-coefficient files. |

## Output Docs

Create `docs/output-files.md` with:

- output format summary from GitBook;
- distinction between always-written/debug outputs and optional print-controlled outputs;
- `print.prt` as the main output-control input;
- `object.prt` as selected object-output control when used;
- a starter map of known current scenario output-like files from `Osu_1hru`, marked `generated/debug/output-like` until writer routines are traced.

Do not fully populate `docs/outputs/` yet. Output documentation should be evidence-based because output file names, frequencies, units, and writer routines need source tracing.

## Migration Plan

1. Use `docs/tracing-guide.md` as the input-to-output tracing guide.
2. Update all live links to point to `tracing-guide.md`.
3. Add `docs/output-files.md`.
4. Create input category subfolders.
5. Move every `docs/inputs/*.md` page into its category folder.
6. Rewrite links in `docs/input-files.md` to the new paths.
7. Rewrite links inside moved input pages back to `../../input-files.md` and `../../tracing-guide.md`.
8. Update `docs/README.md` document boundaries and reading path.
9. Validate there are no stale links to the old tracing-guide name or old flat `docs/inputs/*.md` paths.

## Validation

After implementation:

- `docs/input-files.md` should reference every input page.
- Every `docs/inputs/**/*.md` page should be referenced by `docs/input-files.md`.
- Markdown relative-link existence check should pass.
- A repository scan for the old tracing-guide filename should find no live links.
- `rg "docs/inputs/[A-Za-z0-9_-]+\\.md|\\]\\(inputs/[A-Za-z0-9_-]+\\.md\\)" docs` should find no stale flat input-page links outside historical specs.
- `git status --short` should show only intended docs changes plus the existing unrelated `VSProj/SWAT/Osu_1hru/recall_db.rec` untracked artifact.

## Non-Goals

- Do not fully document every input parameter in this restructuring pass.
- Do not generate all output-file stubs yet.
- Do not treat scenario outputs or local artifacts as stable inputs.
- Do not copy large sections of GitBook text; summarize format rules and link to the source.
