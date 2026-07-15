---
title: SWAT+ input files map
kind: reference
status: partial
created: 2026-07-14
updated: 2026-07-15
source_revision: cb442f7c05fc3bfc34349c446010f452d2737ca0
scenario: Osu_1hru
tags: [inputs, file-cio, catalog, reference-map]
---

# SWAT+ Input Files Map

## Scope

This is the authoritative input-file map for this workspace. It covers the eventual SWAT+ input-file reference, not only the files used by the small `Osu_1hru` scenario. Each mapped input file or file family has a categorized page under [`inputs/`](inputs/).

Use this file for the big map: which files are basic, which are active in `Osu_1hru`, which are indirect, and which are optional, conditional, fixed-name, or not yet active. Use the linked per-file pages for field-level meanings and reader evidence. Use [`tracing-guide.md`](tracing-guide.md) when following one value from input through runtime state to output, and [`output-files.md`](output-files.md) for output-file controls and classes.

## External Format Baseline

SWAT+ input files are plain text, free-format, and space-delimited. The first line is a title, most input files have a second header line, and `file.cio` is the main exception. Some files add extra header lines before data blocks. External reference: [SWAT+ Input File Format](https://swatplus.gitbook.io/io-docs/introduction-1/input-file-format).

Local source and the active scenario remain the authority for whether a file is actually read here. GitBook categories guide navigation; they do not replace source-reader tracing.

## Coverage Summary

- Mapped input entries: 170.
- Core/basic input files: 6.
- Fixed startup file: 1 (`file.cio`).
- Direct files selected by `Osu_1hru/file.cio`: 71, including core, active-scenario, and currently active conditional inputs.
- Active rows for `Osu_1hru`: 72, including `file.cio` plus the direct `file.cio` selections.
- Climate time-series file-family entries: 6; active indirect families in `Osu_1hru`: 4; inactive/null families in `Osu_1hru`: 2.
- Conditional usage-class entries: 48.
- Optional/default usage-class entries: 35.
- Fixed-name or companion usage-class entries: 14.
- Detailed per-file references: 6.
- Stub/reference placeholder pages: 164.

## Usage Classes

| Usage class | Meaning |
| --- | --- |
| `core` | Basic files needed for nearly every normal SWAT+ run. In this workspace: `file.cio`, `time.sim`, `print.prt`, `object.cnt`, `codes.bsn`, and `parameters.bsn`. |
| `active scenario input` | Selected directly by the current `Osu_1hru/file.cio` and not `null`, but not necessarily required for every SWAT+ project. |
| `indirect input` | Reached through another input file rather than directly through `file.cio`, such as climate time-series files named by `.cli` manifests. |
| `conditional input` | Used only when a model switch, object count, module, calibration workflow, decision table, or optional process is active. |
| `optional/default` | Defined by source defaults or `file.cio` slots but inactive or `null` in the current scenario. |
| `fixed-name companion` | Opened by convention or derived from another file name, such as `carbon_lyr.bsn` and `carbon_layers.prt`. |
| `local artifact/output-like` | Present in a scenario folder but not a stable input until a reader path proves it. Example: untracked `recall_db.rec`. |

The table below separates durable role from scenario state:

| Column | Purpose |
| --- | --- |
| `Usage class` | The broad role of the file in SWAT+ documentation. |
| `Activation` | Why SWAT+ reads it: startup name, `file.cio`, another manifest, a switch, an object count, or a fixed-name reader. |
| `Osu_1hru status` | Whether it is active, indirect, inactive/null, fixed-name/conditional, local artifact, or not yet traced for the current scenario. |

## Category Guide

| Folder | Contents |
| --- | --- |
| [inputs/simulation/](inputs/simulation/) | Startup control files, run-period settings, object counts, and print-control inputs. |
| [inputs/basin/](inputs/basin/) | Basin-wide switches, parameters, carbon setup, and CO2 companions. |
| [inputs/climate/](inputs/climate/) | Weather station and climate manifest files listed by `file.cio`. |
| [inputs/climate-timeseries/](inputs/climate-timeseries/) | Scenario-specific weather data files reached through climate manifests. |
| [inputs/connectivity/](inputs/connectivity/) | Connection, outlet, link, and object-routing files. |
| [inputs/channels/](inputs/channels/) | Channel, SWAT-DEG channel, channel initialization, and channel water-quality inputs. |
| [inputs/reservoirs-wetlands/](inputs/reservoirs-wetlands/) | Reservoir, pond, wetland, release, sediment, nutrient, and hydrology inputs. |
| [inputs/routing-units/](inputs/routing-units/) | Routing-unit definitions, elements, parameters, and delivery-ratio inputs. |
| [inputs/hru/](inputs/hru/) | Full HRU and HRU-LTE object definition files. |
| [inputs/aquifers/](inputs/aquifers/) | Aquifer parameter and initial-condition files. |
| [inputs/hydrology/](inputs/hydrology/) | HRU hydrology, topography, field geometry, and related physical settings. |
| [inputs/soils/](inputs/soils/) | Soil profile and soil nutrient input files. |
| [inputs/landuse-management/](inputs/landuse-management/) | Land-use records, management schedules, curve-number tables, and conservation practices. |
| [inputs/operations/](inputs/operations/) | Scheduled operation files such as harvest, grazing, irrigation, fire, sweep, and treatment. |
| [inputs/structural/](inputs/structural/) | Structural practice files such as tile drains, septic systems, filter strips, waterways, BMPs, and shade factors. |
| [inputs/databases/](inputs/databases/) | Reusable plant, fertilizer, tillage, pesticide, urban, septic, snow, manure, pathogen, metal, and salt databases. |
| [inputs/initialization/](inputs/initialization/) | Initial plant, soil/plant, water-quality, pesticide, pathogen, metal, salt, and constituent states. |
| [inputs/constituents-salt/](inputs/constituents-salt/) | Salt, constituent, GWFLOW, calibration-support, and module-specific files not better classified elsewhere. |
| [inputs/calibration/](inputs/calibration/) | Calibration parameter and change files. |
| [inputs/regions/](inputs/regions/) | Landscape, channel, aquifer, reservoir, and recall region/category-unit files. |
| [inputs/decision-tables/](inputs/decision-tables/) | Conditional decision-table detail files used by management or reservoir release logic. |
| [inputs/water-allocation/](inputs/water-allocation/) | Water rights, allocation, and transfer files. |
| [inputs/livestock/](inputs/livestock/) | Animal, herd, and ranch files. |
| [inputs/point-sources-inlets/](inputs/point-sources-inlets/) | Recall inputs, export-coefficient files, and inlet/source load files. |

## Source-Of-Truth Rules

1. `file.cio` proves direct scenario activation only when the slot is not `null`.
2. Manifest files such as `.cli` files prove indirect activation for the files they name.
3. Source defaults prove a known SWAT+ input slot, not that the file is active in this scenario.
4. Fixed-name and companion files need their reader path before they are treated as active.
5. Files generated by a run, checker, debug routine, or local experiment belong in [`output-files.md`](output-files.md), a topic note, or the local-artifact section, not in the stable input inventory.

## Core Input Set

| File | Why it is core | Reference |
| --- | --- | --- |
| `file.cio` | Master input manifest; tells SWAT+ which scenario input files to read. | Detailed: [inputs/simulation/file-cio.md](inputs/simulation/file-cio.md) |
| `time.sim` | Simulation dates, time step, and run period settings. | Stub: [inputs/simulation/time-sim.md](inputs/simulation/time-sim.md) |
| `print.prt` | Output print-control settings: which output groups and intervals are written. | Detailed: [inputs/simulation/print-prt.md](inputs/simulation/print-prt.md) |
| `object.cnt` | Counts of spatial/object types; used for allocation and object-command setup. | Detailed: [inputs/simulation/object-cnt.md](inputs/simulation/object-cnt.md) |
| `codes.bsn` | Basin-wide model switches and process-selection codes. | Detailed: [inputs/basin/codes-bsn.md](inputs/basin/codes-bsn.md) |
| `parameters.bsn` | Basin-wide numeric parameters and default coefficients. | Detailed: [inputs/basin/parameters-bsn.md](inputs/basin/parameters-bsn.md) |

## Categorized Input Reference

### Simulation and Master Control

| File | Role | Usage class | Activation | Osu_1hru status | Reference |
| --- | --- | --- | --- | --- | --- |
| `file.cio` | Master input manifest; tells SWAT+ which scenario input files to read. | `core` | fixed startup filename | `active` | Detailed: [inputs/simulation/file-cio.md](inputs/simulation/file-cio.md) |
| `constituents.cs` | Input file for simulation; source slot cs_db. | `optional/default` | source default or inactive `file.cio` slot | `inactive/null` | Stub: [inputs/simulation/constituents-cs.md](inputs/simulation/constituents-cs.md) |
| `object.cnt` | Counts of spatial/object types; used for allocation and object-command setup. | `core` | `file.cio` | `active` | Detailed: [inputs/simulation/object-cnt.md](inputs/simulation/object-cnt.md) |
| `object.prt` | Input file for simulation; source slot object_prt. | `conditional input` | module switch, object count, or inactive `file.cio` slot | `inactive/null` | Stub: [inputs/simulation/object-prt.md](inputs/simulation/object-prt.md) |
| `print.prt` | Output print-control settings: which output groups and intervals are written. | `core` | `file.cio` | `active` | Detailed: [inputs/simulation/print-prt.md](inputs/simulation/print-prt.md) |
| `time.sim` | Simulation dates, time step, and run period settings. | `core` | `file.cio` | `active` | Stub: [inputs/simulation/time-sim.md](inputs/simulation/time-sim.md) |

### Basin

| File | Role | Usage class | Activation | Osu_1hru status | Reference |
| --- | --- | --- | --- | --- | --- |
| `carbon.bsn` | Optional dynamic carbon basin parameter file when carbon behavior is enabled. | `conditional input` | module switch, object count, or inactive `file.cio` slot | `inactive/null` | Stub: [inputs/basin/carbon-bsn.md](inputs/basin/carbon-bsn.md) |
| `codes.bsn` | Basin-wide model switches and process-selection codes. | `core` | `file.cio` | `active` | Detailed: [inputs/basin/codes-bsn.md](inputs/basin/codes-bsn.md) |
| `parameters.bsn` | Basin-wide numeric parameters and default coefficients. | `core` | `file.cio` | `active` | Detailed: [inputs/basin/parameters-bsn.md](inputs/basin/parameters-bsn.md) |
| `carbon_layers.prt` | Optional carbon-layer output control file. | `fixed-name companion` | fixed-name or derived reader | `fixed-name/conditional` | Stub: [inputs/basin/carbon-layers-prt.md](inputs/basin/carbon-layers-prt.md) |
| `carbon_lyr.bsn` | Companion per-layer file for dynamic carbon basin parameters; derived from the selected carbon basin filename. | `fixed-name companion` | fixed-name or derived reader | `fixed-name/conditional` | Stub: [inputs/basin/carbon-lyr-bsn.md](inputs/basin/carbon-lyr-bsn.md) |
| `co2.dat` | Optional annual CO2 input series; otherwise the model can use basin defaults. | `fixed-name companion` | fixed-name or derived reader | `fixed-name/conditional` | Stub: [inputs/basin/co2-dat.md](inputs/basin/co2-dat.md) |

### Climate Manifests

| File | Role | Usage class | Activation | Osu_1hru status | Reference |
| --- | --- | --- | --- | --- | --- |
| `atmodep.cli` | Input file for climate; source slot atmo_cli. | `optional/default` | source default or inactive `file.cio` slot | `inactive/null` | Stub: [inputs/climate/atmodep-cli.md](inputs/climate/atmodep-cli.md) |
| `hmd.cli` | Input file for climate; source slot hmd_cli. | `optional/default` | source default or inactive `file.cio` slot | `inactive/null` | Stub: [inputs/climate/hmd-cli.md](inputs/climate/hmd-cli.md) |
| `pcp.cli` | Precipitation gauge list; points to precipitation time-series files. | `active scenario input` | `file.cio` | `active` | Stub: [inputs/climate/pcp-cli.md](inputs/climate/pcp-cli.md) |
| `pet.cli` | Input file for climate; source slot pet_cli. | `optional/default` | source default or inactive `file.cio` slot | `inactive/null` | Stub: [inputs/climate/pet-cli.md](inputs/climate/pet-cli.md) |
| `slr.cli` | Solar radiation gauge list; points to solar-radiation time-series files. | `active scenario input` | `file.cio` | `active` | Stub: [inputs/climate/slr-cli.md](inputs/climate/slr-cli.md) |
| `tmp.cli` | Temperature gauge list; points to temperature time-series files. | `active scenario input` | `file.cio` | `active` | Stub: [inputs/climate/tmp-cli.md](inputs/climate/tmp-cli.md) |
| `weather-sta.cli` | Weather station list and links to precipitation, temperature, solar radiation, wind, and generator records. | `active scenario input` | `file.cio` | `active` | Stub: [inputs/climate/weather-sta-cli.md](inputs/climate/weather-sta-cli.md) |
| `weather-wgn.cli` | Weather generator station list. | `active scenario input` | `file.cio` | `active` | Stub: [inputs/climate/weather-wgn-cli.md](inputs/climate/weather-wgn-cli.md) |
| `wnd.cli` | Wind-speed gauge list; points to wind time-series files. | `active scenario input` | `file.cio` | `active` | Stub: [inputs/climate/wnd-cli.md](inputs/climate/wnd-cli.md) |

### Climate Time Series

| File | Role | Usage class | Activation | Osu_1hru status | Reference |
| --- | --- | --- | --- | --- | --- |
| `*.hmd` | Relative-humidity time-series file named by a humidity gauge manifest. | `indirect input` | manifest file when `hmd.cli` is active | `inactive/null` | Stub: [inputs/climate-timeseries/hmd-time-series.md](inputs/climate-timeseries/hmd-time-series.md) |
| `*.pcp` | Precipitation time-series file named by a precipitation gauge manifest. | `indirect input` | manifest file when `pcp.cli` is active | `indirect` | Stub: [inputs/climate-timeseries/pcp-time-series.md](inputs/climate-timeseries/pcp-time-series.md) |
| `*.pet` | Potential-ET time-series file named by a PET gauge manifest. | `indirect input` | manifest file when `pet.cli` is active | `inactive/null` | Stub: [inputs/climate-timeseries/pet-time-series.md](inputs/climate-timeseries/pet-time-series.md) |
| `*.slr` | Solar-radiation time-series file named by a solar-radiation gauge manifest. | `indirect input` | manifest file when `slr.cli` is active | `indirect` | Stub: [inputs/climate-timeseries/slr-time-series.md](inputs/climate-timeseries/slr-time-series.md) |
| `*.tmp` | Temperature time-series file named by a temperature gauge manifest. | `indirect input` | manifest file when `tmp.cli` is active | `indirect` | Stub: [inputs/climate-timeseries/tmp-time-series.md](inputs/climate-timeseries/tmp-time-series.md) |
| `*.wnd` | Wind-speed time-series file named by a wind gauge manifest. | `indirect input` | manifest file when `wnd.cli` is active | `indirect` | Stub: [inputs/climate-timeseries/wnd-time-series.md](inputs/climate-timeseries/wnd-time-series.md) |

### Connectivity and Links

| File | Role | Usage class | Activation | Osu_1hru status | Reference |
| --- | --- | --- | --- | --- | --- |
| `aquifer.con` | Aquifer connection file; defines receiving objects for aquifer outputs. | `active scenario input` | `file.cio` | `active` | Stub: [inputs/connectivity/aquifer-con.md](inputs/connectivity/aquifer-con.md) |
| `aquifer2d.con` | Input file for connect; source slot aqu2d_con. | `conditional input` | module switch, object count, or inactive `file.cio` slot | `inactive/null` | Stub: [inputs/connectivity/aquifer2d-con.md](inputs/connectivity/aquifer2d-con.md) |
| `chandeg.con` | SWAT-DEG channel connection file; defines routing for `sdc` / `chandeg` objects. | `active scenario input` | `file.cio` | `active` | Stub: [inputs/connectivity/chandeg-con.md](inputs/connectivity/chandeg-con.md) |
| `channel.con` | Input file for connect; source slot chan_con. | `optional/default` | source default or inactive `file.cio` slot | `inactive/null` | Stub: [inputs/connectivity/channel-con.md](inputs/connectivity/channel-con.md) |
| `delratio.con` | Input file for connect; source slot delr_con. | `conditional input` | module switch, object count, or inactive `file.cio` slot | `inactive/null` | Stub: [inputs/connectivity/delratio-con.md](inputs/connectivity/delratio-con.md) |
| `exco.con` | Input file for connect; source slot exco_con. | `conditional input` | module switch, object count, or inactive `file.cio` slot | `inactive/null` | Stub: [inputs/connectivity/exco-con.md](inputs/connectivity/exco-con.md) |
| `gwflow.con` | Input file for connect; source slot gwflow_con. | `conditional input` | module switch, object count, or inactive `file.cio` slot | `inactive/null` | Stub: [inputs/connectivity/gwflow-con.md](inputs/connectivity/gwflow-con.md) |
| `hru.con` | Connection definition for full HRU objects. In QSWAT-style routing, HRUs may have no direct output and are wrapped by routing units. | `active scenario input` | `file.cio` | `active` | Stub: [inputs/connectivity/hru-con.md](inputs/connectivity/hru-con.md) |
| `hru-lte.con` | Input file for connect; source slot hruez_con. | `optional/default` | source default or inactive `file.cio` slot | `inactive/null` | Stub: [inputs/connectivity/hru-lte-con.md](inputs/connectivity/hru-lte-con.md) |
| `outlet.con` | Input file for connect; source slot out_con. | `optional/default` | source default or inactive `file.cio` slot | `inactive/null` | Stub: [inputs/connectivity/outlet-con.md](inputs/connectivity/outlet-con.md) |
| `recall.con` | Recall-object connection file; defines routing for external time-series hydrographs. | `active scenario input` | `file.cio` | `active` | Stub: [inputs/connectivity/recall-con.md](inputs/connectivity/recall-con.md) |
| `reservoir.con` | Input file for connect; source slot res_con. | `optional/default` | source default or inactive `file.cio` slot | `inactive/null` | Stub: [inputs/connectivity/reservoir-con.md](inputs/connectivity/reservoir-con.md) |
| `rout_unit.con` | Routing-unit connection file; defines where routing-unit hydrographs go. | `active scenario input` | `file.cio` | `active` | Stub: [inputs/connectivity/rout-unit-con.md](inputs/connectivity/rout-unit-con.md) |
| `aqu_cha.lin` | Input file for link; source slot aqu_cha. | `optional/default` | source default or inactive `file.cio` slot | `inactive/null` | Stub: [inputs/connectivity/aqu-cha-lin.md](inputs/connectivity/aqu-cha-lin.md) |
| `chan-surf.lin` | Input file for link; source slot chan_surf. | `optional/default` | source default or inactive `file.cio` slot | `inactive/null` | Stub: [inputs/connectivity/chan-surf-lin.md](inputs/connectivity/chan-surf-lin.md) |

### Channels

| File | Role | Usage class | Activation | Osu_1hru status | Reference |
| --- | --- | --- | --- | --- | --- |
| `channel.cha` | Input file for channel; source slot dat. | `optional/default` | source default or inactive `file.cio` slot | `inactive/null` | Stub: [inputs/channels/channel-cha.md](inputs/channels/channel-cha.md) |
| `channel-lte.cha` | SWAT-DEG channel definition file; describes detailed channel objects used by `sdc` / `chandeg`. | `active scenario input` | `file.cio` | `active` | Stub: [inputs/channels/channel-lte-cha.md](inputs/channels/channel-lte-cha.md) |
| `hydrology.cha` | Input file for channel; source slot hyd. | `optional/default` | source default or inactive `file.cio` slot | `inactive/null` | Stub: [inputs/channels/hydrology-cha.md](inputs/channels/hydrology-cha.md) |
| `hyd-sed-lte.cha` | SWAT-DEG hydrology/sediment control parameters. | `active scenario input` | `file.cio` | `active` | Stub: [inputs/channels/hyd-sed-lte-cha.md](inputs/channels/hyd-sed-lte-cha.md) |
| `initial.cha` | Named initial channel water-quality/constituent setup; can point to records such as `om_water.ini`. | `active scenario input` | `file.cio` | `active` | Stub: [inputs/channels/initial-cha.md](inputs/channels/initial-cha.md) |
| `nutrients.cha` | Channel nutrient and water-quality parameter database. | `active scenario input` | `file.cio` | `active` | Stub: [inputs/channels/nutrients-cha.md](inputs/channels/nutrients-cha.md) |
| `sediment.cha` | Input file for channel; source slot sed. | `optional/default` | source default or inactive `file.cio` slot | `inactive/null` | Stub: [inputs/channels/sediment-cha.md](inputs/channels/sediment-cha.md) |
| `temperature.cha` | Input file for channel; source slot temp. | `optional/default` | source default or inactive `file.cio` slot | `inactive/null` | Stub: [inputs/channels/temperature-cha.md](inputs/channels/temperature-cha.md) |

### Reservoirs and Wetlands

| File | Role | Usage class | Activation | Osu_1hru status | Reference |
| --- | --- | --- | --- | --- | --- |
| `hydrology.res` | Input file for reservoir; source slot hyd_res. | `optional/default` | source default or inactive `file.cio` slot | `inactive/null` | Stub: [inputs/reservoirs-wetlands/hydrology-res.md](inputs/reservoirs-wetlands/hydrology-res.md) |
| `hydrology.wet` | Wetland hydrology parameter database. | `active scenario input` | `file.cio` | `active` | Stub: [inputs/reservoirs-wetlands/hydrology-wet.md](inputs/reservoirs-wetlands/hydrology-wet.md) |
| `initial.res` | Named initial reservoir/wetland water-quality setup. | `active scenario input` | `file.cio` | `active` | Stub: [inputs/reservoirs-wetlands/initial-res.md](inputs/reservoirs-wetlands/initial-res.md) |
| `nutrients.res` | Reservoir nutrient and water-quality parameter database. | `active scenario input` | `file.cio` | `active` | Stub: [inputs/reservoirs-wetlands/nutrients-res.md](inputs/reservoirs-wetlands/nutrients-res.md) |
| `reservoir.res` | Input file for reservoir; source slot res. | `optional/default` | source default or inactive `file.cio` slot | `inactive/null` | Stub: [inputs/reservoirs-wetlands/reservoir-res.md](inputs/reservoirs-wetlands/reservoir-res.md) |
| `sediment.res` | Reservoir sediment parameter database. | `active scenario input` | `file.cio` | `active` | Stub: [inputs/reservoirs-wetlands/sediment-res.md](inputs/reservoirs-wetlands/sediment-res.md) |
| `weir.res` | Reservoir release/weir parameter file. | `active scenario input` | `file.cio` | `active` | Stub: [inputs/reservoirs-wetlands/weir-res.md](inputs/reservoirs-wetlands/weir-res.md) |
| `wetland.wet` | Wetland object parameter file. | `active scenario input` | `file.cio` | `active` | Stub: [inputs/reservoirs-wetlands/wetland-wet.md](inputs/reservoirs-wetlands/wetland-wet.md) |

### Routing Units and Delivery Ratios

| File | Role | Usage class | Activation | Osu_1hru status | Reference |
| --- | --- | --- | --- | --- | --- |
| `rout_unit.def` | Defines each routing unit by listing which element records belong to it. | `active scenario input` | `file.cio` | `active` | Stub: [inputs/routing-units/rout-unit-def.md](inputs/routing-units/rout-unit-def.md) |
| `rout_unit.dr` | Input file for routing unit; source slot ru_dr. | `optional/default` | source default or inactive `file.cio` slot | `inactive/null` | Stub: [inputs/routing-units/rout-unit-dr.md](inputs/routing-units/rout-unit-dr.md) |
| `rout_unit.ele` | Defines routing-unit member elements, such as HRUs, HRU-LTEs, or other spatial elements. | `active scenario input` | `file.cio` | `active` | Stub: [inputs/routing-units/rout-unit-ele.md](inputs/routing-units/rout-unit-ele.md) |
| `rout_unit.rtu` | Routing-unit parameter file. | `active scenario input` | `file.cio` | `active` | Stub: [inputs/routing-units/rout-unit-rtu.md](inputs/routing-units/rout-unit-rtu.md) |
| `delratio.del` | Input file for delivery ratio; source slot del_ratio. | `conditional input` | module switch, object count, or inactive `file.cio` slot | `inactive/null` | Stub: [inputs/routing-units/delratio-del.md](inputs/routing-units/delratio-del.md) |
| `dr_hmet.del` | Input file for delivery ratio; source slot hmet. | `conditional input` | module switch, object count, or inactive `file.cio` slot | `inactive/null` | Stub: [inputs/routing-units/dr-hmet-del.md](inputs/routing-units/dr-hmet-del.md) |
| `dr_om.del` | Input file for delivery ratio; source slot om. | `conditional input` | module switch, object count, or inactive `file.cio` slot | `inactive/null` | Stub: [inputs/routing-units/dr-om-del.md](inputs/routing-units/dr-om-del.md) |
| `dr_path.del` | Input file for delivery ratio; source slot path. | `conditional input` | module switch, object count, or inactive `file.cio` slot | `inactive/null` | Stub: [inputs/routing-units/dr-path-del.md](inputs/routing-units/dr-path-del.md) |
| `dr_pest.del` | Input file for delivery ratio; source slot pest. | `conditional input` | module switch, object count, or inactive `file.cio` slot | `inactive/null` | Stub: [inputs/routing-units/dr-pest-del.md](inputs/routing-units/dr-pest-del.md) |
| `dr_salt.del` | Input file for delivery ratio; source slot salt. | `conditional input` | module switch, object count, or inactive `file.cio` slot | `inactive/null` | Stub: [inputs/routing-units/dr-salt-del.md](inputs/routing-units/dr-salt-del.md) |

### HRU Definitions

| File | Role | Usage class | Activation | Osu_1hru status | Reference |
| --- | --- | --- | --- | --- | --- |
| `hru-data.hru` | Full HRU database file; links each HRU definition to land use, soil, hydrology, topography, snow, and field records. | `active scenario input` | `file.cio` | `active` | Stub: [inputs/hru/hru-data-hru.md](inputs/hru/hru-data-hru.md) |
| `hru-lte.hru` | Input file for HRU; source slot hru_ez. | `optional/default` | source default or inactive `file.cio` slot | `inactive/null` | Stub: [inputs/hru/hru-lte-hru.md](inputs/hru/hru-lte-hru.md) |

### Aquifers

| File | Role | Usage class | Activation | Osu_1hru status | Reference |
| --- | --- | --- | --- | --- | --- |
| `aquifer.aqu` | Lumped aquifer parameter database. | `active scenario input` | `file.cio` | `active` | Stub: [inputs/aquifers/aquifer-aqu.md](inputs/aquifers/aquifer-aqu.md) |
| `initial.aqu` | Initial aquifer condition records. | `active scenario input` | `file.cio` | `active` | Stub: [inputs/aquifers/initial-aqu.md](inputs/aquifers/initial-aqu.md) |

### Hydrology, Topography, and Fields

| File | Role | Usage class | Activation | Osu_1hru status | Reference |
| --- | --- | --- | --- | --- | --- |
| `field.fld` | Field geometry and field-related parameter database. | `active scenario input` | `file.cio` | `active` | Stub: [inputs/hydrology/field-fld.md](inputs/hydrology/field-fld.md) |
| `hydrology.hyd` | HRU hydrology parameter database, including ET, lateral flow, percolation, and related coefficients. | `active scenario input` | `file.cio` | `active` | Stub: [inputs/hydrology/hydrology-hyd.md](inputs/hydrology/hydrology-hyd.md) |
| `topography.hyd` | HRU topography parameter database, including slope, slope length, and related geometry. | `active scenario input` | `file.cio` | `active` | Stub: [inputs/hydrology/topography-hyd.md](inputs/hydrology/topography-hyd.md) |

### Soils

| File | Role | Usage class | Activation | Osu_1hru status | Reference |
| --- | --- | --- | --- | --- | --- |
| `nutrients.sol` | Soil nutrient/soil-test initialization database. | `active scenario input` | `file.cio` | `active` | Stub: [inputs/soils/nutrients-sol.md](inputs/soils/nutrients-sol.md) |
| `soils.sol` | Soil profile database for full HRUs. | `active scenario input` | `file.cio` | `active` | Stub: [inputs/soils/soils-sol.md](inputs/soils/soils-sol.md) |
| `soils_lte.sol` | Input file for soils; source slot lte_sol. | `optional/default` | source default or inactive `file.cio` slot | `inactive/null` | Stub: [inputs/soils/soils-lte-sol.md](inputs/soils/soils-lte-sol.md) |

### Land Use and Management

| File | Role | Usage class | Activation | Osu_1hru status | Reference |
| --- | --- | --- | --- | --- | --- |
| `cntable.lum` | Curve-number lookup table by land use and soil/hydrologic condition. | `active scenario input` | `file.cio` | `active` | Stub: [inputs/landuse-management/cntable-lum.md](inputs/landuse-management/cntable-lum.md) |
| `cons_practice.lum` | Conservation-practice parameter database. | `active scenario input` | `file.cio` | `active` | Stub: [inputs/landuse-management/cons-practice-lum.md](inputs/landuse-management/cons-practice-lum.md) |
| `landuse.lum` | Land-use-management database; links land-use names to plant cover, management schedule, curve-number table, and structural features. | `active scenario input` | `file.cio` | `active` | Stub: [inputs/landuse-management/landuse-lum.md](inputs/landuse-management/landuse-lum.md) |
| `management.sch` | Management schedules that sequence operations over time. | `active scenario input` | `file.cio` | `active` | Stub: [inputs/landuse-management/management-sch.md](inputs/landuse-management/management-sch.md) |
| `ovn_table.lum` | Overland Manning's `n` lookup table. | `active scenario input` | `file.cio` | `active` | Stub: [inputs/landuse-management/ovn-table-lum.md](inputs/landuse-management/ovn-table-lum.md) |

### Operations

| File | Role | Usage class | Activation | Osu_1hru status | Reference |
| --- | --- | --- | --- | --- | --- |
| `chem_app.ops` | Chemical application operation definitions. | `active scenario input` | `file.cio` | `active` | Stub: [inputs/operations/chem-app-ops.md](inputs/operations/chem-app-ops.md) |
| `fire.ops` | Fire operation definitions. | `active scenario input` | `file.cio` | `active` | Stub: [inputs/operations/fire-ops.md](inputs/operations/fire-ops.md) |
| `graze.ops` | Grazing operation definitions. | `active scenario input` | `file.cio` | `active` | Stub: [inputs/operations/graze-ops.md](inputs/operations/graze-ops.md) |
| `harv.ops` | Harvest operation definitions. | `active scenario input` | `file.cio` | `active` | Stub: [inputs/operations/harv-ops.md](inputs/operations/harv-ops.md) |
| `irr.ops` | Irrigation operation definitions. | `active scenario input` | `file.cio` | `active` | Stub: [inputs/operations/irr-ops.md](inputs/operations/irr-ops.md) |
| `sweep.ops` | Street-sweeping operation definitions. | `active scenario input` | `file.cio` | `active` | Stub: [inputs/operations/sweep-ops.md](inputs/operations/sweep-ops.md) |
| `puddle.ops` | Optional puddling operation definitions. | `fixed-name companion` | fixed-name or derived reader | `fixed-name/conditional` | Stub: [inputs/operations/puddle-ops.md](inputs/operations/puddle-ops.md) |
| `treatment.trt` | Optional water-treatment or treatment-operation support file. | `fixed-name companion` | fixed-name or derived reader | `fixed-name/conditional` | Stub: [inputs/operations/treatment-trt.md](inputs/operations/treatment-trt.md) |

### Structural Practices

| File | Role | Usage class | Activation | Osu_1hru status | Reference |
| --- | --- | --- | --- | --- | --- |
| `bmpuser.str` | User-defined BMP structural parameter database. | `active scenario input` | `file.cio` | `active` | Stub: [inputs/structural/bmpuser-str.md](inputs/structural/bmpuser-str.md) |
| `filterstrip.str` | Filter-strip structural parameter database. | `active scenario input` | `file.cio` | `active` | Stub: [inputs/structural/filterstrip-str.md](inputs/structural/filterstrip-str.md) |
| `grassedww.str` | Grassed-waterway structural parameter database. | `active scenario input` | `file.cio` | `active` | Stub: [inputs/structural/grassedww-str.md](inputs/structural/grassedww-str.md) |
| `septic.str` | Structural septic-system setup file. | `active scenario input` | `file.cio` | `active` | Stub: [inputs/structural/septic-str.md](inputs/structural/septic-str.md) |
| `tiledrain.str` | Structural tile-drain parameter database. | `active scenario input` | `file.cio` | `active` | Stub: [inputs/structural/tiledrain-str.md](inputs/structural/tiledrain-str.md) |
| `shade_factor.shf` | Input file for shade factor; source slot ssff_shf. | `optional/default` | source default or inactive `file.cio` slot | `inactive/null` | Stub: [inputs/structural/shade-factor-shf.md](inputs/structural/shade-factor-shf.md) |

### Parameter Databases

| File | Role | Usage class | Activation | Osu_1hru status | Reference |
| --- | --- | --- | --- | --- | --- |
| `fertilizer.frt` | Fertilizer/mineral nutrient database. | `active scenario input` | `file.cio` | `active` | Stub: [inputs/databases/fertilizer-frt.md](inputs/databases/fertilizer-frt.md) |
| `metals.mtl` | Input file for HRU databases; source slot hmetcom_db. | `optional/default` | source default or inactive `file.cio` slot | `inactive/null` | Stub: [inputs/databases/metals-mtl.md](inputs/databases/metals-mtl.md) |
| `pathogens.pth` | Input file for HRU databases; source slot pathcom_db. | `conditional input` | module switch, object count, or inactive `file.cio` slot | `inactive/null` | Stub: [inputs/databases/pathogens-pth.md](inputs/databases/pathogens-pth.md) |
| `pesticide.pes` | Pesticide parameter database. | `conditional input` | `file.cio` | `active` | Stub: [inputs/databases/pesticide-pes.md](inputs/databases/pesticide-pes.md) |
| `plants.plt` | Plant parameter database. | `active scenario input` | `file.cio` | `active` | Stub: [inputs/databases/plants-plt.md](inputs/databases/plants-plt.md) |
| `salt.slt` | Input file for HRU databases; source slot saltcom_db. | `conditional input` | module switch, object count, or inactive `file.cio` slot | `inactive/null` | Stub: [inputs/databases/salt-slt.md](inputs/databases/salt-slt.md) |
| `septic.sep` | Septic-system parameter database. | `active scenario input` | `file.cio` | `active` | Stub: [inputs/databases/septic-sep.md](inputs/databases/septic-sep.md) |
| `snow.sno` | Snow parameter database. | `active scenario input` | `file.cio` | `active` | Stub: [inputs/databases/snow-sno.md](inputs/databases/snow-sno.md) |
| `tillage.til` | Tillage operation database. | `active scenario input` | `file.cio` | `active` | Stub: [inputs/databases/tillage-til.md](inputs/databases/tillage-til.md) |
| `urban.urb` | Urban land-use parameter database. | `active scenario input` | `file.cio` | `active` | Stub: [inputs/databases/urban-urb.md](inputs/databases/urban-urb.md) |
| `manure_db.frt` | Optional manure database with extended manure composition information. | `fixed-name companion` | fixed-name or derived reader | `fixed-name/conditional` | Stub: [inputs/databases/manure-db-frt.md](inputs/databases/manure-db-frt.md) |
| `manure_om.frt` | Optional organic/mineral manure database. | `fixed-name companion` | fixed-name or derived reader | `fixed-name/conditional` | Stub: [inputs/databases/manure-om-frt.md](inputs/databases/manure-om-frt.md) |
| `transplant.plt` | Optional plant transplant data. | `fixed-name companion` | fixed-name or derived reader | `fixed-name/conditional` | Stub: [inputs/databases/transplant-plt.md](inputs/databases/transplant-plt.md) |

### Initialization

| File | Role | Usage class | Activation | Osu_1hru status | Reference |
| --- | --- | --- | --- | --- | --- |
| `hmet_hru.ini` | Input file for initial conditions; source slot hmet_soil. | `conditional input` | module switch, object count, or inactive `file.cio` slot | `inactive/null` | Stub: [inputs/initialization/hmet-hru-ini.md](inputs/initialization/hmet-hru-ini.md) |
| `hmet_water.ini` | Input file for initial conditions; source slot hmet_water. | `conditional input` | module switch, object count, or inactive `file.cio` slot | `inactive/null` | Stub: [inputs/initialization/hmet-water-ini.md](inputs/initialization/hmet-water-ini.md) |
| `om_water.ini` | Named initial organic-mineral water states for channels, reservoirs, wetlands, or related water-storage objects. | `active scenario input` | `file.cio` | `active` | Detailed: [inputs/initialization/om-water-ini.md](inputs/initialization/om-water-ini.md) |
| `path_hru.ini` | Input file for initial conditions; source slot path_soil. | `conditional input` | module switch, object count, or inactive `file.cio` slot | `inactive/null` | Stub: [inputs/initialization/path-hru-ini.md](inputs/initialization/path-hru-ini.md) |
| `path_water.ini` | Input file for initial conditions; source slot path_water. | `conditional input` | module switch, object count, or inactive `file.cio` slot | `inactive/null` | Stub: [inputs/initialization/path-water-ini.md](inputs/initialization/path-water-ini.md) |
| `pest_hru.ini` | Input file for initial conditions; source slot pest_soil. | `conditional input` | module switch, object count, or inactive `file.cio` slot | `inactive/null` | Stub: [inputs/initialization/pest-hru-ini.md](inputs/initialization/pest-hru-ini.md) |
| `pest_water.ini` | Input file for initial conditions; source slot pest_water. | `conditional input` | module switch, object count, or inactive `file.cio` slot | `inactive/null` | Stub: [inputs/initialization/pest-water-ini.md](inputs/initialization/pest-water-ini.md) |
| `plant.ini` | Initial plant-community condition records. | `active scenario input` | `file.cio` | `active` | Stub: [inputs/initialization/plant-ini.md](inputs/initialization/plant-ini.md) |
| `salt_hru.ini` | Initial salt setup for HRU soil/plant salt simulation. | `conditional input` | module switch, object count, or inactive `file.cio` slot | `inactive/null` | Stub: [inputs/initialization/salt-hru-ini.md](inputs/initialization/salt-hru-ini.md) |
| `salt_water.ini` | Input file for initial conditions; source slot salt_water. | `conditional input` | module switch, object count, or inactive `file.cio` slot | `inactive/null` | Stub: [inputs/initialization/salt-water-ini.md](inputs/initialization/salt-water-ini.md) |
| `soil_plant.ini` | Initial soil/plant nutrient, pesticide, pathogen, metal, salt, and constituent pointer records. | `active scenario input` | `file.cio` | `active` | Stub: [inputs/initialization/soil-plant-ini.md](inputs/initialization/soil-plant-ini.md) |

### Constituents, Salt, and Optional Modules

| File | Role | Usage class | Activation | Osu_1hru status | Reference |
| --- | --- | --- | --- | --- | --- |
| `cs_aqu.ini` | Initial generic constituent setup for aquifer-related constituent simulation. | `fixed-name companion` | fixed-name or derived reader | `fixed-name/conditional` | Stub: [inputs/constituents-salt/cs-aqu-ini.md](inputs/constituents-salt/cs-aqu-ini.md) |
| `cs_channel.ini` | Initial generic constituent setup for channel water/bed constituent simulation. | `fixed-name companion` | fixed-name or derived reader | `fixed-name/conditional` | Stub: [inputs/constituents-salt/cs-channel-ini.md](inputs/constituents-salt/cs-channel-ini.md) |
| `cs_hru.ini` | Initial generic constituent setup for HRU soil/plant constituent simulation. | `fixed-name companion` | fixed-name or derived reader | `fixed-name/conditional` | Stub: [inputs/constituents-salt/cs-hru-ini.md](inputs/constituents-salt/cs-hru-ini.md) |
| `salt_aqu.ini` | Initial salt setup for aquifer-related salt simulation. | `fixed-name companion` | fixed-name or derived reader | `fixed-name/conditional` | Stub: [inputs/constituents-salt/salt-aqu-ini.md](inputs/constituents-salt/salt-aqu-ini.md) |
| `salt_channel.ini` | Initial salt setup for channel salt simulation. | `fixed-name companion` | fixed-name or derived reader | `fixed-name/conditional` | Stub: [inputs/constituents-salt/salt-channel-ini.md](inputs/constituents-salt/salt-channel-ini.md) |
| `salt_fertilizer.frt` | Optional salt composition data for fertilizer-related salt simulation. | `fixed-name companion` | fixed-name or derived reader | `fixed-name/conditional` | Stub: [inputs/constituents-salt/salt-fertilizer-frt.md](inputs/constituents-salt/salt-fertilizer-frt.md) |

### Calibration

| File | Role | Usage class | Activation | Osu_1hru status | Reference |
| --- | --- | --- | --- | --- | --- |
| `cal_parms.cal` | Calibration parameter definition file. | `conditional input` | `file.cio` | `active` | Stub: [inputs/calibration/cal-parms-cal.md](inputs/calibration/cal-parms-cal.md) |
| `calibration.cal` | Calibration change/update file. | `conditional input` | `file.cio` | `active` | Stub: [inputs/calibration/calibration-cal.md](inputs/calibration/calibration-cal.md) |
| `ch_sed_budget.sft` | Input file for calibration change; source slot ch_sed_budget_sft. | `conditional input` | module switch, object count, or inactive `file.cio` slot | `inactive/null` | Stub: [inputs/calibration/ch-sed-budget-sft.md](inputs/calibration/ch-sed-budget-sft.md) |
| `ch_sed_parms.sft` | Input file for calibration change; source slot ch_sed_parms_sft. | `conditional input` | module switch, object count, or inactive `file.cio` slot | `inactive/null` | Stub: [inputs/calibration/ch-sed-parms-sft.md](inputs/calibration/ch-sed-parms-sft.md) |
| `codes.sft` | Input file for calibration change; source slot codes_sft. | `conditional input` | module switch, object count, or inactive `file.cio` slot | `inactive/null` | Stub: [inputs/calibration/codes-sft.md](inputs/calibration/codes-sft.md) |
| `plant_gro.sft` | Input file for calibration change; source slot plant_gro_sft. | `conditional input` | module switch, object count, or inactive `file.cio` slot | `inactive/null` | Stub: [inputs/calibration/plant-gro-sft.md](inputs/calibration/plant-gro-sft.md) |
| `plant_parms.sft` | Input file for calibration change; source slot plant_parms_sft. | `conditional input` | module switch, object count, or inactive `file.cio` slot | `inactive/null` | Stub: [inputs/calibration/plant-parms-sft.md](inputs/calibration/plant-parms-sft.md) |
| `water_balance.sft` | Input file for calibration change; source slot water_balance_sft. | `conditional input` | module switch, object count, or inactive `file.cio` slot | `inactive/null` | Stub: [inputs/calibration/water-balance-sft.md](inputs/calibration/water-balance-sft.md) |
| `wb_parms.sft` | Input file for calibration change; source slot wb_parms_sft. | `conditional input` | module switch, object count, or inactive `file.cio` slot | `inactive/null` | Stub: [inputs/calibration/wb-parms-sft.md](inputs/calibration/wb-parms-sft.md) |

### Regions and Category Units

| File | Role | Usage class | Activation | Osu_1hru status | Reference |
| --- | --- | --- | --- | --- | --- |
| `aqu_catunit.def` | Input file for regions; source slot def_aqu. | `optional/default` | source default or inactive `file.cio` slot | `inactive/null` | Stub: [inputs/regions/aqu-catunit-def.md](inputs/regions/aqu-catunit-def.md) |
| `aqu_catunit.ele` | Aquifer calibration/category-unit element file. | `active scenario input` | `file.cio` | `active` | Stub: [inputs/regions/aqu-catunit-ele.md](inputs/regions/aqu-catunit-ele.md) |
| `aqu_reg.def` | Input file for regions; source slot def_aqu_reg. | `optional/default` | source default or inactive `file.cio` slot | `inactive/null` | Stub: [inputs/regions/aqu-reg-def.md](inputs/regions/aqu-reg-def.md) |
| `ch_catunit.def` | Input file for regions; source slot def_cha. | `optional/default` | source default or inactive `file.cio` slot | `inactive/null` | Stub: [inputs/regions/ch-catunit-def.md](inputs/regions/ch-catunit-def.md) |
| `ch_catunit.ele` | Input file for regions; source slot ele_cha. | `optional/default` | source default or inactive `file.cio` slot | `inactive/null` | Stub: [inputs/regions/ch-catunit-ele.md](inputs/regions/ch-catunit-ele.md) |
| `ch_reg.def` | Input file for regions; source slot def_cha_reg. | `optional/default` | source default or inactive `file.cio` slot | `inactive/null` | Stub: [inputs/regions/ch-reg-def.md](inputs/regions/ch-reg-def.md) |
| `ls_cal.reg` | Input file for regions; source slot cal_lcu. | `optional/default` | source default or inactive `file.cio` slot | `inactive/null` | Stub: [inputs/regions/ls-cal-reg.md](inputs/regions/ls-cal-reg.md) |
| `ls_reg.def` | Input file for regions; source slot def_reg. | `optional/default` | source default or inactive `file.cio` slot | `inactive/null` | Stub: [inputs/regions/ls-reg-def.md](inputs/regions/ls-reg-def.md) |
| `ls_reg.ele` | Input file for regions; source slot ele_reg. | `optional/default` | source default or inactive `file.cio` slot | `inactive/null` | Stub: [inputs/regions/ls-reg-ele.md](inputs/regions/ls-reg-ele.md) |
| `ls_unit.def` | Landscape-unit definition file. | `active scenario input` | `file.cio` | `active` | Stub: [inputs/regions/ls-unit-def.md](inputs/regions/ls-unit-def.md) |
| `ls_unit.ele` | Landscape-unit element membership file. | `active scenario input` | `file.cio` | `active` | Stub: [inputs/regions/ls-unit-ele.md](inputs/regions/ls-unit-ele.md) |
| `rec_catunit.def` | Input file for regions; source slot def_psc. | `optional/default` | source default or inactive `file.cio` slot | `inactive/null` | Stub: [inputs/regions/rec-catunit-def.md](inputs/regions/rec-catunit-def.md) |
| `rec_catunit.ele` | Input file for regions; source slot ele_psc. | `optional/default` | source default or inactive `file.cio` slot | `inactive/null` | Stub: [inputs/regions/rec-catunit-ele.md](inputs/regions/rec-catunit-ele.md) |
| `rec_reg.def` | Input file for regions; source slot def_psc_reg. | `optional/default` | source default or inactive `file.cio` slot | `inactive/null` | Stub: [inputs/regions/rec-reg-def.md](inputs/regions/rec-reg-def.md) |
| `res_catunit.def` | Input file for regions; source slot def_res. | `optional/default` | source default or inactive `file.cio` slot | `inactive/null` | Stub: [inputs/regions/res-catunit-def.md](inputs/regions/res-catunit-def.md) |
| `res_catunit.ele` | Input file for regions; source slot ele_res. | `optional/default` | source default or inactive `file.cio` slot | `inactive/null` | Stub: [inputs/regions/res-catunit-ele.md](inputs/regions/res-catunit-ele.md) |
| `res_reg.def` | Input file for regions; source slot def_res_reg. | `optional/default` | source default or inactive `file.cio` slot | `inactive/null` | Stub: [inputs/regions/res-reg-def.md](inputs/regions/res-reg-def.md) |

### Decision Tables

| File | Role | Usage class | Activation | Osu_1hru status | Reference |
| --- | --- | --- | --- | --- | --- |
| `flo_con.dtl` | Input file for conditional; source slot dtbl_flo. | `conditional input` | module switch, object count, or inactive `file.cio` slot | `inactive/null` | Stub: [inputs/decision-tables/flo-con-dtl.md](inputs/decision-tables/flo-con-dtl.md) |
| `lum.dtl` | Land-use/management decision tables, including growth-start and growth-end rules used by some routines. | `conditional input` | `file.cio` | `active` | Stub: [inputs/decision-tables/lum-dtl.md](inputs/decision-tables/lum-dtl.md) |
| `res_rel.dtl` | Reservoir release decision tables. | `conditional input` | `file.cio` | `active` | Stub: [inputs/decision-tables/res-rel-dtl.md](inputs/decision-tables/res-rel-dtl.md) |
| `scen_lu.dtl` | Input file for conditional; source slot dtbl_scen. | `conditional input` | module switch, object count, or inactive `file.cio` slot | `inactive/null` | Stub: [inputs/decision-tables/scen-lu-dtl.md](inputs/decision-tables/scen-lu-dtl.md) |

### Water Allocation and Rights

| File | Role | Usage class | Activation | Osu_1hru status | Reference |
| --- | --- | --- | --- | --- | --- |
| `element.wro` | Input file for water-rights; source slot element. | `conditional input` | module switch, object count, or inactive `file.cio` slot | `inactive/null` | Stub: [inputs/water-allocation/element-wro.md](inputs/water-allocation/element-wro.md) |
| `water_allocation.wro` | Input file for water-rights; source slot transfer_wro. | `conditional input` | module switch, object count, or inactive `file.cio` slot | `inactive/null` | Stub: [inputs/water-allocation/water-allocation-wro.md](inputs/water-allocation/water-allocation-wro.md) |
| `water_rights.wro` | Input file for water-rights; source slot water_rights. | `conditional input` | module switch, object count, or inactive `file.cio` slot | `inactive/null` | Stub: [inputs/water-allocation/water-rights-wro.md](inputs/water-allocation/water-rights-wro.md) |

### Livestock

| File | Role | Usage class | Activation | Osu_1hru status | Reference |
| --- | --- | --- | --- | --- | --- |
| `animal.hrd` | Input file for herd; source slot animal. | `conditional input` | module switch, object count, or inactive `file.cio` slot | `inactive/null` | Stub: [inputs/livestock/animal-hrd.md](inputs/livestock/animal-hrd.md) |
| `herd.hrd` | Input file for herd; source slot herd. | `conditional input` | module switch, object count, or inactive `file.cio` slot | `inactive/null` | Stub: [inputs/livestock/herd-hrd.md](inputs/livestock/herd-hrd.md) |
| `ranch.hrd` | Input file for herd; source slot ranch. | `conditional input` | module switch, object count, or inactive `file.cio` slot | `inactive/null` | Stub: [inputs/livestock/ranch-hrd.md](inputs/livestock/ranch-hrd.md) |

### Point Sources, Recalls, and Export Coefficients

| File | Role | Usage class | Activation | Osu_1hru status | Reference |
| --- | --- | --- | --- | --- | --- |
| `exco.exc` | Input file for exco (recall constant); source slot exco. | `conditional input` | module switch, object count, or inactive `file.cio` slot | `inactive/null` | Stub: [inputs/point-sources-inlets/exco-exc.md](inputs/point-sources-inlets/exco-exc.md) |
| `exco_hmet.exc` | Input file for exco (recall constant); source slot hmet. | `conditional input` | module switch, object count, or inactive `file.cio` slot | `inactive/null` | Stub: [inputs/point-sources-inlets/exco-hmet-exc.md](inputs/point-sources-inlets/exco-hmet-exc.md) |
| `exco_om.exc` | Input file for exco (recall constant); source slot om. | `conditional input` | module switch, object count, or inactive `file.cio` slot | `inactive/null` | Stub: [inputs/point-sources-inlets/exco-om-exc.md](inputs/point-sources-inlets/exco-om-exc.md) |
| `exco_path.exc` | Input file for exco (recall constant); source slot path. | `conditional input` | module switch, object count, or inactive `file.cio` slot | `inactive/null` | Stub: [inputs/point-sources-inlets/exco-path-exc.md](inputs/point-sources-inlets/exco-path-exc.md) |
| `exco_pest.exc` | Input file for exco (recall constant); source slot pest. | `conditional input` | module switch, object count, or inactive `file.cio` slot | `inactive/null` | Stub: [inputs/point-sources-inlets/exco-pest-exc.md](inputs/point-sources-inlets/exco-pest-exc.md) |
| `exco_salt.exc` | Input file for exco (recall constant); source slot salt. | `conditional input` | module switch, object count, or inactive `file.cio` slot | `inactive/null` | Stub: [inputs/point-sources-inlets/exco-salt-exc.md](inputs/point-sources-inlets/exco-salt-exc.md) |
| `recall.rec` | External time-series hydrograph/input source data for recall objects. | `active scenario input` | `file.cio` | `active` | Stub: [inputs/point-sources-inlets/recall-rec.md](inputs/point-sources-inlets/recall-rec.md) |

## Local Artifacts And Output-Like Files

The current debug scenario can contain files that look like inputs but are not stable input references. Keep them out of the 170-file map unless a reader path proves they belong there.

| File | Current treatment |
| --- | --- |
| `recall_db.rec` | Untracked zero-byte local artifact observed in `VSProj/SWAT/Osu_1hru`; leave untracked until a reader proves it is required. |
| `*.out`, `simulation.out`, `files_out.out`, checker/debug files | Generated output or runtime files; track in [`output-files.md`](output-files.md) after writer routines are traced. |

## Related Notes

- [`tracing-guide.md`](tracing-guide.md)
- [`output-files.md`](output-files.md)
- [`topics/osu-1hru-file-classification.md`](topics/osu-1hru-file-classification.md)
