---
title: SWAT+ input files map
kind: reference
status: partial
created: 2026-07-14
updated: 2026-07-15
source_revision: 5b3705b300d95ebe4914119f056548446bdc208f
scenario: Osu_1hru
tags: [inputs, file-cio, catalog, reference-map]
---

# SWAT+ Input Files Map

## Scope

This file is the high-level map for SWAT+ input files. It is designed to grow into a full input-file reference, including optional files that are not active in the current `Osu_1hru` debug scenario.

Use this map to answer:

```text
Which input files exist, what role do they play, and where is the detailed reference?
```

Use the per-file pages in [`inputs/`](inputs/) when you need field meanings, reader paths, internal storage, defaults, conversions, or downstream consumers.

For the broader distinction between active inputs, optional files, generated outputs, and local artifacts in the `Osu_1hru` folder, see [`topics/osu-1hru-file-classification.md`](topics/osu-1hru-file-classification.md).

## Reference Status

| Status | Meaning |
| --- | --- |
| Detailed | A per-file reference exists under `docs/inputs/`. |
| Partial | The file is identified and partly understood, but detailed field-level tracing is incomplete. |
| Not traced | The file is known or expected, but reader path and field meanings are not yet documented here. |
| Optional | The file is valid SWAT+ input or module support but is not active in the current `Osu_1hru` evidence. |
| Output/support | The file looks generated or auxiliary and should not be treated as a primary input until traced. |

## How To Read The Map

| Term | Meaning |
| --- | --- |
| Listed in `file.cio` | The scenario explicitly points to this file and the slot is not `null`. |
| `null` in `file.cio` | The scenario does not use that optional input slot. |
| Fixed-name or optional input | A reader may open the file by convention or only when a model switch is active. |
| Detailed reference | The linked page is the durable place for parameter meanings and reader evidence. |

## Simulation And Basin Files

| File | Role | Reference |
| --- | --- | --- |
| `file.cio` | Master input manifest; tells SWAT+ which scenario input files to read. | Detailed: [`inputs/file-cio.md`](inputs/file-cio.md) |
| `time.sim` | Simulation dates, time step, and run period settings. | Partial / not traced |
| `print.prt` | Output print-control settings: which output groups and intervals are written. | Detailed: [`inputs/print-prt.md`](inputs/print-prt.md) |
| `object.cnt` | Counts of spatial/object types; used for allocation and object-command setup. | Detailed: [`inputs/object-cnt.md`](inputs/object-cnt.md) |
| `codes.bsn` | Basin-wide model switches and process-selection codes. | Detailed: [`inputs/codes-bsn.md`](inputs/codes-bsn.md) |
| `parameters.bsn` | Basin-wide numeric parameters and default coefficients. | Detailed: [`inputs/parameters-bsn.md`](inputs/parameters-bsn.md) |
| `carbon.bsn` | Optional dynamic carbon basin parameter file when carbon behavior is enabled. | Partial: [`topics/co2-carbon-inputs.md`](topics/co2-carbon-inputs.md) |
| `carbon_lyr.bsn` | Optional companion layer/allocation file for dynamic carbon parameters. | Partial: [`topics/co2-carbon-inputs.md`](topics/co2-carbon-inputs.md) |
| `carbon_layers.prt` | Optional carbon-layer output control file. | Partial: [`topics/co2-carbon-inputs.md`](topics/co2-carbon-inputs.md) |
| `co2.dat` | Optional annual CO2 input series; otherwise the model can use basin defaults. | Partial: [`topics/co2-carbon-inputs.md`](topics/co2-carbon-inputs.md) |

## Climate Files

| File | Role | Reference |
| --- | --- | --- |
| `weather-sta.cli` | Weather station list and links to precipitation, temperature, solar radiation, wind, and generator records. | Partial / not traced |
| `weather-wgn.cli` | Weather generator station list. | Partial / not traced |
| `pcp.cli` | Precipitation gauge list; points to precipitation time-series files. | Partial / not traced |
| `tmp.cli` | Temperature gauge list; points to temperature time-series files. | Partial / not traced |
| `slr.cli` | Solar radiation gauge list; points to solar-radiation time-series files. | Partial / not traced |
| `wnd.cli` | Wind-speed gauge list; points to wind time-series files. | Partial / not traced |
| `*.pcp` | Precipitation time series reached through active climate manifests. | Partial / not traced |
| `*.tmp` | Temperature time series reached through active climate manifests. | Partial / not traced |
| `*.slr` | Solar radiation time series reached through active climate manifests. | Partial / not traced |
| `*.wnd` | Wind-speed time series reached through active climate manifests. | Partial / not traced |

## Connection Files

| File | Role | Reference |
| --- | --- | --- |
| `hru.con` | Connection definition for full HRU objects. In QSWAT-style routing, HRUs may have no direct output and are wrapped by routing units. | Partial: [`topics/qswat-hru-routing-unit.md`](topics/qswat-hru-routing-unit.md) |
| `rout_unit.con` | Routing-unit connection file; defines where routing-unit hydrographs go. | Partial: [`topics/qswat-hru-routing-unit.md`](topics/qswat-hru-routing-unit.md) |
| `aquifer.con` | Aquifer connection file; defines receiving objects for aquifer outputs. | Partial / not traced |
| `recall.con` | Recall-object connection file; defines routing for external time-series hydrographs. | Partial / not traced |
| `chandeg.con` | SWAT-DEG channel connection file; defines routing for `sdc` / `chandeg` objects. | Partial / not traced |

## Channel And SWAT-DEG Channel Files

| File | Role | Reference |
| --- | --- | --- |
| `initial.cha` | Named initial channel water-quality/constituent setup; can point to records such as `om_water.ini`. | Partial: [`inputs/om-water-ini.md`](inputs/om-water-ini.md) |
| `nutrients.cha` | Channel nutrient and water-quality parameter database. | Partial / not traced |
| `channel-lte.cha` | SWAT-DEG channel definition file; describes detailed channel objects used by `sdc` / `chandeg`. | Partial / not traced |
| `hyd-sed-lte.cha` | SWAT-DEG hydrology/sediment control parameters. | Partial / not traced |

## Reservoir And Wetland Files

| File | Role | Reference |
| --- | --- | --- |
| `initial.res` | Named initial reservoir/wetland water-quality setup. | Partial / not traced |
| `sediment.res` | Reservoir sediment parameter database. | Partial / not traced |
| `nutrients.res` | Reservoir nutrient and water-quality parameter database. | Partial / not traced |
| `weir.res` | Reservoir release/weir parameter file. | Partial / not traced |
| `wetland.wet` | Wetland object parameter file. | Partial / not traced |
| `hydrology.wet` | Wetland hydrology parameter database. | Partial / not traced |

## Routing Unit Files

| File | Role | Reference |
| --- | --- | --- |
| `rout_unit.def` | Defines each routing unit by listing which element records belong to it. | Partial: [`topics/qswat-hru-routing-unit.md`](topics/qswat-hru-routing-unit.md) |
| `rout_unit.ele` | Defines routing-unit member elements, such as HRUs, HRU-LTEs, or other spatial elements. | Partial: [`topics/qswat-hru-routing-unit.md`](topics/qswat-hru-routing-unit.md) |
| `rout_unit.rtu` | Routing-unit parameter file. | Partial / not traced |

## HRU Files

| File | Role | Reference |
| --- | --- | --- |
| `hru-data.hru` | Full HRU database file; links each HRU definition to land use, soil, hydrology, topography, snow, and field records. | Partial / not traced |

## Recall, Aquifer, And Region Files

| File | Role | Reference |
| --- | --- | --- |
| `recall.rec` | External time-series hydrograph/input source data for recall objects. | Partial / not traced |
| `initial.aqu` | Initial aquifer condition records. | Partial / not traced |
| `aquifer.aqu` | Lumped aquifer parameter database. | Partial / not traced |
| `ls_unit.ele` | Landscape-unit element membership file. | Partial / not traced |
| `ls_unit.def` | Landscape-unit definition file. | Partial / not traced |
| `aqu_catunit.ele` | Aquifer calibration/category-unit element file. | Partial / not traced |

## HRU Hydrology, Topography, And Structural Files

| File | Role | Reference |
| --- | --- | --- |
| `hydrology.hyd` | HRU hydrology parameter database, including ET, lateral flow, percolation, and related coefficients. | Partial / not traced |
| `topography.hyd` | HRU topography parameter database, including slope, slope length, and related geometry. | Partial / not traced |
| `field.fld` | Field geometry and field-related parameter database. | Partial / not traced |
| `tiledrain.str` | Structural tile-drain parameter database. | Partial / not traced |
| `septic.str` | Structural septic-system setup file. | Partial / not traced |
| `filterstrip.str` | Filter-strip structural parameter database. | Partial / not traced |
| `grassedww.str` | Grassed-waterway structural parameter database. | Partial / not traced |
| `bmpuser.str` | User-defined BMP structural parameter database. | Partial / not traced |

## Parameter Database Files

| File | Role | Reference |
| --- | --- | --- |
| `plants.plt` | Plant parameter database. | Partial / not traced |
| `fertilizer.frt` | Fertilizer/mineral nutrient database. | Partial / not traced |
| `tillage.til` | Tillage operation database. | Partial / not traced |
| `pesticide.pes` | Pesticide parameter database. | Partial / not traced |
| `urban.urb` | Urban land-use parameter database. | Partial / not traced |
| `septic.sep` | Septic-system parameter database. | Partial / not traced |
| `snow.sno` | Snow parameter database. | Partial / not traced |
| `manure_db.frt` | Optional manure database with extended manure composition information. | Optional / not traced |
| `manure_om.frt` | Optional organic/mineral manure database. | Optional / not traced |

## Management Operation Files

| File | Role | Reference |
| --- | --- | --- |
| `harv.ops` | Harvest operation definitions. | Partial / not traced |
| `graze.ops` | Grazing operation definitions. | Partial / not traced |
| `irr.ops` | Irrigation operation definitions. | Partial / not traced |
| `chem_app.ops` | Chemical application operation definitions. | Partial / not traced |
| `fire.ops` | Fire operation definitions. | Partial / not traced |
| `sweep.ops` | Street-sweeping operation definitions. | Partial / not traced |
| `puddle.ops` | Optional puddling operation definitions. | Optional / not traced |
| `treatment.trt` | Optional water-treatment or treatment-operation support file. | Optional / not traced |

## Land Use And Management Files

| File | Role | Reference |
| --- | --- | --- |
| `landuse.lum` | Land-use-management database; links land-use names to plant cover, management schedule, curve-number table, and structural features. | Partial / not traced |
| `management.sch` | Management schedules that sequence operations over time. | Partial / not traced |
| `cntable.lum` | Curve-number lookup table by land use and soil/hydrologic condition. | Partial / not traced |
| `cons_practice.lum` | Conservation-practice parameter database. | Partial / not traced |
| `ovn_table.lum` | Overland Manning's `n` lookup table. | Partial / not traced |

## Calibration Files

| File | Role | Reference |
| --- | --- | --- |
| `cal_parms.cal` | Calibration parameter definition file. | Partial / not traced |
| `calibration.cal` | Calibration change/update file. | Partial / not traced |

## Initial Condition Files

| File | Role | Reference |
| --- | --- | --- |
| `plant.ini` | Initial plant-community condition records. | Partial / not traced |
| `soil_plant.ini` | Initial soil/plant nutrient, pesticide, pathogen, metal, salt, and constituent pointer records. | Partial / not traced |
| `om_water.ini` | Named initial organic-mineral water states for channels, reservoirs, wetlands, or related water-storage objects. | Detailed: [`inputs/om-water-ini.md`](inputs/om-water-ini.md) |

## Soil Files

| File | Role | Reference |
| --- | --- | --- |
| `soils.sol` | Soil profile database for full HRUs. | Partial / not traced |
| `nutrients.sol` | Soil nutrient/soil-test initialization database. | Partial / not traced |

## Decision Table Files

| File | Role | Reference |
| --- | --- | --- |
| `lum.dtl` | Land-use/management decision tables, including growth-start and growth-end rules used by some routines. | Partial / not traced |
| `res_rel.dtl` | Reservoir release decision tables. | Partial / not traced |

## Constituents, Salt, And Optional Module Files

These files are present in the `Osu_1hru` scenario folder or are known optional module inputs, but they are not all selected directly by the active `file.cio` rows. Treat them as optional, fixed-name, module-specific, or support data until each reader is traced.

| File | Role | Reference |
| --- | --- | --- |
| `cs_aqu.ini` | Initial generic constituent setup for aquifer-related constituent simulation. | Optional / not traced |
| `cs_channel.ini` | Initial generic constituent setup for channel water/bed constituent simulation. | Optional / not traced |
| `cs_hru.ini` | Initial generic constituent setup for HRU soil/plant constituent simulation. | Optional / not traced |
| `salt_aqu.ini` | Initial salt setup for aquifer-related salt simulation. | Optional / not traced |
| `salt_channel.ini` | Initial salt setup for channel salt simulation. | Optional / not traced |
| `salt_hru.ini` | Initial salt setup for HRU soil/plant salt simulation. | Optional / not traced |
| `transplant.plt` | Optional plant transplant data. | Optional / not traced |
| `recall_db.rec` | Untracked local recall database file currently present in the debug scenario; not part of the committed scenario definition. | Local artifact unless traced |

## Generated Support And Output-Like Files

Files such as `simulation.out`, `diagnostics.out`, `files_out.out`, `co2.out`, `area_calc.out`, `checker.out`, `erosion.out`, `mgt_out.txt`, and many `.swf` files are not treated as primary input files in this map. Some `.swf` files may be soft-calibration support data, but they should be traced before being documented as active inputs.

## Current Limits

Verified:

- File groups and active filenames are from `VSProj/SWAT/Osu_1hru/file.cio`.
- The `file.cio` group order is supported by `input_file_module.f90`.
- Detailed references exist for `file.cio`, `codes.bsn`, `parameters.bsn`, `print.prt`, `object.cnt`, and `om_water.ini`.

Still partial:

- This map does not define every column in every input file.
- Many optional or module-specific files are listed because they are valid or observed input-like files, but their exact reader paths have not been fully traced.
- Generated-output classification is intentionally separate from input-reference documentation.

## Related Notes

- [`file.cio` master input file](inputs/file-cio.md)
- [`Osu_1hru` file classification](topics/osu-1hru-file-classification.md)
- [`codes.bsn` basin control codes](inputs/codes-bsn.md)
- [`parameters.bsn` basin parameters](inputs/parameters-bsn.md)
- [`print.prt` output control file](inputs/print-prt.md)
- [`object.cnt` and SWAT+ object concepts](inputs/object-cnt.md)
- [`om_water.ini` initial organic-mineral water state](inputs/om-water-ini.md)
- [Input to output path](input-output.md)
