---
title: SWAT+ model structure
kind: guide
status: partial
created: 2026-07-13
updated: 2026-07-15
source_revision: cb442f7c05fc3bfc34349c446010f452d2737ca0
scenario: general
tags: [guide, architecture, control-flow]
---

# SWAT+ Model Structure

This guide is the short map of which part of the code does what. It is an orientation layer; use the linked topic notes when you need exact evidence.

## Top-Level Shape

```text
main.f90.in -> generated Visual Studio main.f90
    -> input and object initialization
    -> time_control
        -> daily calendar and climate work
        -> command
            -> object dispatch
            -> object/process outputs
```

The maintained program entry is [`main.f90.in`](../SWATPLUS/swatplus/src/main.f90.in). The Visual Studio project compiles ignored local output `VSProj/SWAT/generated/main.f90`, generated from the template by [`generate-main.ps1`](../VSProj/SWAT/generated/generate-main.ps1). The generated file is not the durable edit target.

At startup, `main` writes the program banner to the console and `simulation.out`, opens `erosion.txt`, then calls `proc_bsn`, which begins the `file.cio` input-selection path.

## Demo Structural Levels Figure

This figure is a static level map for the [`Osu_1hru`](topics/osu-1hru-scenario.md) demo. It is not a procedure or call-order diagram; read it as "what level contains or configures what."

```mermaid
flowchart TB
    L0["Level 0: Code and run target<br/>main.f90.in -> generated main.f90"]
    L1["Level 1: Demo scenario folder<br/>VSProj/SWAT/Osu_1hru"]
    L2["Level 2: Core run controls<br/>file.cio, time.sim, print.prt,<br/>object.cnt, codes.bsn, parameters.bsn"]

    subgraph L3["Level 3: Scenario input families"]
        C1["Climate<br/>weather-sta.cli, pcp.cli, tmp.cli,<br/>slr.cli, wnd.cli, time-series files"]
        C2["Connectivity and routing<br/>hru.con, rout_unit.con, aquifer.con,<br/>recall.con, chandeg.con"]
        C3["Spatial objects<br/>hru-data.hru, rout_unit.*, channel-lte.cha,<br/>aquifer.aqu, wetland.wet, recall.rec"]
        C4["Physical parameters<br/>soils.sol, hydrology.hyd, topography.hyd,<br/>plants.plt, fertilizer.frt, tillage.til"]
        C5["Management and conditions<br/>landuse.lum, management.sch, operations,<br/>plant.ini, soil_plant.ini, initial.*"]
    end

    subgraph L4["Level 4: Runtime object graph"]
        R1["Landscape side<br/>routing unit -> HRU -> soil/plant state"]
        R2["Water side<br/>channel, reservoir, wetland,<br/>aquifer, recall objects"]
        R3["Network side<br/>receivers, fractions,<br/>object order, output requests"]
    end

    L5["Level 5: Reported results<br/>requested output tables and runtime logs"]

    L0 --> L1 --> L2
    L2 --> C1
    L2 --> C2
    L2 --> C3
    L2 --> C4
    L2 --> C5
    C2 --> R3
    C3 --> R1
    C3 --> R2
    C4 --> R1
    C5 --> R1
    R1 --> L5
    R2 --> L5
    R3 --> L5
```

Use this hierarchy when you need to decide whether a file defines the whole run, selects an input family, defines an object, supplies parameters for an object, initializes state, or controls reported results.

## Demo Procedure Diagram

Use this procedure for the small [`Osu_1hru`](topics/osu-1hru-scenario.md) demo when learning the runtime structure in the Visual Studio debugger.

```mermaid
flowchart TD
    A["Set debugger working directory<br/>VSProj/SWAT/Osu_1hru"] --> B["Start generated main.f90<br/>built from main.f90.in"]
    B --> C["main startup<br/>banner, simulation.out, erosion.txt"]
    C --> D["proc_bsn reads file.cio<br/>and selects active input filenames"]
    D --> E["Read simulation-control inputs<br/>time.sim, print.prt, object.cnt"]
    E --> F["Read object, connection, climate, soil,<br/>landuse, and management inputs"]
    F --> G["Initialize runtime objects<br/>and state arrays"]
    G --> H{"time%step mode"}
    H -->|"normal daily run"| I["time_control"]
    H -->|"average annual / export coefficient"| J["command directly"]
    I --> K["Advance date, load weather,<br/>apply scheduled operations"]
    K --> L["command walks configured<br/>object sequence"]
    J --> L
    L --> M{"active object type"}
    M -->|"full HRU in Osu_1hru"| N["hru_control<br/>land-phase processes"]
    M -->|"other configured object"| O["matching object controller<br/>channel, reservoir, aquifer, recall"]
    N --> P["Route water, sediment,<br/>nutrients, and constituents"]
    O --> P
    P --> Q["Aggregate and write requested outputs"]
    Q --> R{"more simulation days?"}
    R -->|"yes"| I
    R -->|"no"| S["finalize files and stop"]
```

The demo is useful because its object count is small enough to watch the transition from `file.cio` selection into `time_control`, `command`, and the active HRU controller. It does not prove optional object paths unless the selecting inputs enable those objects in the scenario.

## Major Responsibilities

| Area | Main files | Responsibility |
| --- | --- | --- |
| Program lifecycle | [`main.f90.in`](../SWATPLUS/swatplus/src/main.f90.in) | Startup, input/object initialization, run-mode branch, shutdown. |
| Calendar and daily orchestration | [`time_control.f90`](../SWATPLUS/swatplus/src/time_control.f90) | Simulation dates, daily initialization, climate handling, scheduled actions, call into command execution. |
| Object dispatch | [`command.f90`](../SWATPLUS/swatplus/src/command.f90) | Walk the configured command/object sequence and call the selected object controller. |
| Full HRU controller | [`hru_control.f90`](../SWATPLUS/swatplus/src/hru_control.f90) | Enter the detailed land-phase path for a configured full HRU. |
| Input selection | [`readcio_read.f90`](../SWATPLUS/swatplus/src/readcio_read.f90), [`input_file_module.f90`](../SWATPLUS/swatplus/src/input_file_module.f90) | Read `file.cio` and store filenames used by downstream readers. This path is only partially traced. |
| External source discovery | [`topics/deepwiki-swatplus.md`](topics/deepwiki-swatplus.md) | Use DeepWiki to find candidate files, then verify locally. |

## Important Branches

In a normal time-stepped run, `main` calls `time_control`. If `time%step < 0`, `main` takes the average-annual/export-coefficient path and calls `command` directly. This explains why a `time_control` breakpoint may not be reached in that special mode.

Inside `command`, the active route depends on scenario object definitions, connection files, object types, command order, and model options. Seeing a routine in `command.f90` does not prove a scenario executes it.

## Alternative Object Representations

Some object types represent the same broad physical system with different model detail:

| Physical system | Simpler / lumped representation | Detailed / stronger representation |
| --- | --- | --- |
| Land unit | `hru_lte` / `hlt` | `hru` |
| Stream channel | `cha` | `sdc` / SWAT-DEG channel |
| Groundwater / aquifer | `aqu` | `gwflow` |

The first two pairs are strong direct comparisons. The groundwater pair is useful but less exact because `gwflow` is not always a direct one-to-one replacement for every `aqu` setup. Details and caveats are in [`topics/alternative-object-representations.md`](topics/alternative-object-representations.md).

## How To Read A Code Path

For a new behavior, start broad and then narrow:

1. Identify the input or option that selects the behavior.
2. Find the reader and the storage field.
3. Confirm the controlling object type and index.
4. Step through `time_control` and `command` only until the active object controller is known.
5. Move into the smallest process routine that owns the equation or state transition.
6. Follow downstream routing, aggregation, and output.

The detailed control-flow evidence is in [`topics/simulation-control-flow.md`](topics/simulation-control-flow.md). Main-program generation details are in [`topics/main-program-generation.md`](topics/main-program-generation.md).
