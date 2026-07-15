# SWAT+ Workspace Agent Guide

## Mission

Use this workspace to learn the SWAT+ Fortran model, document verified structure and behavior, and make changes in the maintained source location when explicitly requested. Treat scientific-code work as evidence driven: identify the input, reader, stored state, controller, calculation, consumers, and outputs before editing.

This file applies to the workspace root that contains this `AGENTS.md`.

## Workspace Map

| Path | Role | Edit policy |
| --- | --- | --- |
| `SWATPLUS/swatplus/` | SWAT+ source, tracked as a git submodule | Usually read-only object of study. Make model-source edits only when the task explicitly asks for code changes. |
| `SWATPLUS/swatplus/src/` | Maintained Fortran source | Durable source changes belong here. |
| `VSProj/SWAT/SWAT.slnx` | Visual Studio solution | Use for Intel Fortran debugging. |
| `VSProj/SWAT/SWAT.vfproj` | Intel Fortran project | Its source entries link to `SWATPLUS/swatplus/src`; do not assume it contains copied source. |
| `VSProj/SWAT/Osu_1hru/` | Small one-HRU SWAT+ scenario | Default debug case. Preserve inputs unless a task explicitly changes the scenario. |
| `VSProj/SWAT/x64/` | Compiler and linker output | Generated artifacts; do not edit. |
| `docs/README.md` | Main learning entrance | Keep concise and reader-facing. |
| `docs/model-structure.md` | Code-structure guide | Keep as the current orientation map. |
| `docs/tracing-guide.md` | Input-to-output tracing guide | Keep as the current tracing map. |
| `docs/input-files.md` | SWAT+ input-file reference map | Keep as the big map for active, optional, indirect, and scenario-local input status. |
| `docs/output-files.md` | SWAT+ output-file reference map | Keep focused on output controls, output classes, and writer evidence requirements. |
| `docs/inputs/` | Per-input-file reference pages | One page per SWAT+ input file or file family, grouped by category. |
| `docs/outputs/` | Per-output-file reference pages | Add pages only after writer routines, units, and reset timing are traced. |
| `docs/topics/` | Detailed technical notes | Store durable topic evidence here. |
| `docs/internal/debug-inbox.md` | Raw debugger observations | Working inbox for step-by-step notes before promotion into guides or topics. |

The workspace root is the Git repository. Inspect `git status` before modifying files, and preserve unrelated user changes and untracked generated outputs.

## Source-Of-Truth Rules

1. Use the actual folder names `SWATPLUS/swatplus` and `VSProj`.
2. Visual Studio source entries point to `SWATPLUS/swatplus/src`. Editing a linked file in Visual Studio normally edits the authoritative source.
3. Git tracks `SWATPLUS/swatplus/src/main.f90.in`, not generated `main.f90`. Upstream CMake generates `SWATPLUS/swatplus/src/main.f90`; this workspace keeps Visual Studio's generated copy at `VSProj/SWAT/generated/main.f90`.
4. For durable main-program changes, edit `src/main.f90.in` and regenerate the local Visual Studio copy with `VSProj/SWAT/generated/generate-main.ps1`. Do not maintain generated `main.f90` independently.
5. Do not edit `.obj`, `.mod`, `__genmod.f90`, executables, or other build outputs.
6. Keep disposable experiments outside `SWATPLUS/swatplus/` and outside `docs/`. `docs/` is for durable notes only.

## Required Investigation Workflow

Before recommending or making a model change, trace behavior through these layers:

1. Input or configuration: controlling file, field, value, and scenario.
2. Reader: routine that opens and parses the file.
3. Data structure: module, derived type, array, field, and object index.
4. Orchestration: how `main`, `time_control`, `command`, or another controller reaches the calculation.
5. Process calculation: smallest routine containing the scientific equation or state transition.
6. Consumers and outputs: routing, mass balance, aggregation, writer, and output column.
7. Verification: breakpoint, watched value, output signal, or regression check.

Use code evidence for call paths. Label unverified interpretations as inference. If similarly named legacy, LTE, channel, reservoir, aquifer, or groundwater implementations exist, determine which path the active configuration selects.

## Model Orientation

Use this only as a starting map:

```text
main.f90.in -> generated Visual Studio main.f90
    -> input reading and object initialization
    -> time_control
        -> daily initialization and climate
        -> command
            -> object dispatch
            -> object/process outputs
```

Important entry files:

- `SWATPLUS/swatplus/src/main.f90.in`
- `SWATPLUS/swatplus/src/time_control.f90`
- `SWATPLUS/swatplus/src/command.f90`
- `SWATPLUS/swatplus/src/hru_control.f90`

The active object path depends on `object.cnt`, connection files, object types, and simulation options.

## Visual Studio And Intel Fortran

The default learning/debug configuration is `Debug|x64` with Intel `ifx`.

- Set the debugger working directory to `$(SolutionDir)Osu_1hru`.
- Keep source preprocessing enabled for `.f90` files containing compiler-condition directives.
- Multi-processor compilation speeds compilation; it does not make a SWAT+ simulation multithreaded.
- Keep Debug builds unoptimized with debug information, traceback, interface warnings, bounds checks, and stack-frame checks when diagnosing behavior.
- Visual Studio property changes are configuration- and platform-specific. Confirm selectors before applying or evaluating a setting.

The current `SWAT.vfproj` records multi-processor compilation and preprocessing for `Debug|x64`; do not assume those settings are present in every configuration. The debugger working directory is user-specific and is not stored in the shared project XML.

## Change And Verification Rules

- For explanation or diagnosis, inspect and report; do not change model behavior unless requested.
- For implementation, make the smallest change that addresses the traced behavior.
- Do not modify an equation based only on a filename or variable name. Check units, indexing, initialization, reset timing, mass balance, and downstream use.
- Prefer `Osu_1hru` for fast step-by-step verification when it exercises the relevant path.
- Build the configuration that will be debugged. A successful compile is necessary but not sufficient; run the relevant scenario and inspect output or watched state.
- For regression after source changes, build the upstream CMake project under `SWATPLUS/swatplus/` and run its scenario tests when practical.
- Report exact paths and routine names, what was verified, what remains uncertain, and output differences.

## Documentation Workflow

Use `docs/README.md` as the single reader entrance.

1. Put stable orientation in `docs/model-structure.md`, input-to-output traces in `docs/tracing-guide.md`, input inventory in `docs/input-files.md`, and output inventory in `docs/output-files.md`.
2. Put detailed technical evidence in one topic note under `docs/topics/`.
3. Put raw live-debug observations in `docs/internal/debug-inbox.md`.
4. Do not add per-category README files under `docs/inputs/` or `docs/outputs/` unless the documentation grows enough to justify a new approved structure.
5. Keep root `README.md` short: purpose, workspace map, setup, and essential rules.

Substantive notes must state `status`, `source_revision`, and `scenario`. Use `verified`, `partial`, `hypothesis`, or `superseded` consistently.

## Documentation Standards

- Link to maintained source and local evidence with relative paths.
- Distinguish verified facts, partial paths, hypotheses, and superseded history.
- Keep one durable topic per note.
- Do not copy large sections of upstream documentation. Summarize and link to the local upstream document.
- Update `docs/README.md` when a topic becomes part of the required reading path or changes the current learning status.
