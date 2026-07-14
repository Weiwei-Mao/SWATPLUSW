---
title: SWAT+ input files catalog
kind: reference
status: partial
created: 2026-07-14
updated: 2026-07-14
source_revision: 30283a4
scenario: Osu_1hru
tags: [inputs, file-cio, catalog]
---

# SWAT+ Input Files Catalog

## Scope

This catalog gives a short introduction for the input files used by the `Osu_1hru` debug scenario. The main source of truth is `file.cio`, whose section order is defined in `input_file_module.f90`.

This is an orientation catalog, not a field-by-field specification. Detailed notes should stay in separate topic files.

## How To Read This Catalog

| Term | Meaning |
| --- | --- |
| Listed in `file.cio` | The scenario explicitly points to this file. |
| `null` in `file.cio` | The scenario does not use that optional input in this slot. |
| Extra input-like file | Present in the scenario folder but not selected directly by the active `file.cio` line. It may be read by a fixed-name reader, optional module, or may be leftover/generated support. |

## Simulation And Basin Files

| File | Intro |
| --- | --- |
| `file.cio` | Master input manifest; tells SWAT+ which scenario input files to read. |
| `time.sim` | Simulation dates, time step, and run period settings. |
| `print.prt` | Output print-control settings: which output groups and intervals are written. |
| `object.cnt` | Counts of spatial/object types; used for allocation and object-command setup. |
| `codes.bsn` | Basin-wide model switches and process-selection codes. |
| `parameters.bsn` | Basin-wide numeric parameters and default coefficients. |

## Climate Files

| File | Intro |
| --- | --- |
| `weather-sta.cli` | Weather station list and links to precipitation, temperature, solar radiation, wind, and generator records. |
| `weather-wgn.cli` | Weather generator station list. |
| `pcp.cli` | Precipitation gauge list; points to precipitation time-series files. |
| `tmp.cli` | Temperature gauge list; points to temperature time-series files. |
| `slr.cli` | Solar radiation gauge list; points to solar-radiation time-series files. |
| `wnd.cli` | Wind-speed gauge list; points to wind time-series files. |
| `Imsilpcp.pcp` | Precipitation time series used by the local climate station. |
| `Imsiltmp.tmp` | Temperature time series used by the local climate station. |
| `Imsilsol.slr` | Solar radiation time series used by the local climate station. |
| `Imsilwind.wnd` | Wind-speed time series used by the local climate station. |

## Connection Files

| File | Intro |
| --- | --- |
| `hru.con` | Connection definition for full HRU objects. In QSWAT-style routing, HRUs may have no direct output and are wrapped by routing units. |
| `rout_unit.con` | Routing-unit connection file; defines where routing-unit hydrographs go. |
| `aquifer.con` | Aquifer connection file; defines receiving objects for aquifer outputs. |
| `recall.con` | Recall-object connection file; defines routing for external time-series hydrographs. |
| `chandeg.con` | SWAT-DEG channel connection file; defines routing for `sdc` / `chandeg` objects. |

## Channel And SWAT-DEG Channel Files

| File | Intro |
| --- | --- |
| `initial.cha` | Named initial channel water-quality/constituent setup; points to records such as `om_water.ini`. |
| `nutrients.cha` | Channel nutrient and water-quality parameter database. |
| `channel-lte.cha` | SWAT-DEG channel definition file; describes detailed channel objects used by `sdc` / `chandeg`. |
| `hyd-sed-lte.cha` | SWAT-DEG hydrology/sediment control parameters. |

## Reservoir And Wetland Files

| File | Intro |
| --- | --- |
| `initial.res` | Named initial reservoir/wetland water-quality setup. |
| `sediment.res` | Reservoir sediment parameter database. |
| `nutrients.res` | Reservoir nutrient and water-quality parameter database. |
| `weir.res` | Reservoir release/weir parameter file. |
| `wetland.wet` | Wetland object parameter file. |
| `hydrology.wet` | Wetland hydrology parameter database. |

## Routing Unit Files

| File | Intro |
| --- | --- |
| `rout_unit.def` | Defines each routing unit by listing which element records belong to it. |
| `rout_unit.ele` | Defines routing-unit member elements, such as HRUs, HRU-LTEs, or other spatial elements. |
| `rout_unit.rtu` | Routing-unit parameter file. |

## HRU Files

| File | Intro |
| --- | --- |
| `hru-data.hru` | Full HRU database file; links each HRU definition to land use, soil, hydrology, topography, snow, and field records. |

## Recall, Aquifer, And Region Files

| File | Intro |
| --- | --- |
| `recall.rec` | External time-series hydrograph/input source data for recall objects. |
| `initial.aqu` | Initial aquifer condition records. |
| `aquifer.aqu` | Lumped aquifer parameter database. |
| `ls_unit.ele` | Landscape-unit element membership file. |
| `ls_unit.def` | Landscape-unit definition file. |
| `aqu_catunit.ele` | Aquifer calibration/category-unit element file. |

## HRU Hydrology, Topography, And Structural Files

| File | Intro |
| --- | --- |
| `hydrology.hyd` | HRU hydrology parameter database, including ET, lateral flow, percolation, and related coefficients. |
| `topography.hyd` | HRU topography parameter database, including slope, slope length, and related geometry. |
| `field.fld` | Field geometry and field-related parameter database. |
| `tiledrain.str` | Structural tile-drain parameter database. |
| `septic.str` | Structural septic-system setup file. |
| `filterstrip.str` | Filter-strip structural parameter database. |
| `grassedww.str` | Grassed-waterway structural parameter database. |
| `bmpuser.str` | User-defined BMP structural parameter database. |

## Parameter Database Files

| File | Intro |
| --- | --- |
| `plants.plt` | Plant parameter database. |
| `fertilizer.frt` | Fertilizer/mineral nutrient database. |
| `tillage.til` | Tillage operation database. |
| `pesticide.pes` | Pesticide parameter database. |
| `urban.urb` | Urban land-use parameter database. |
| `septic.sep` | Septic-system parameter database. |
| `snow.sno` | Snow parameter database. |

## Management Operation Files

| File | Intro |
| --- | --- |
| `harv.ops` | Harvest operation definitions. |
| `graze.ops` | Grazing operation definitions. |
| `irr.ops` | Irrigation operation definitions. |
| `chem_app.ops` | Chemical application operation definitions. |
| `fire.ops` | Fire operation definitions. |
| `sweep.ops` | Street-sweeping operation definitions. |

## Land Use And Management Files

| File | Intro |
| --- | --- |
| `landuse.lum` | Land-use-management database; links land-use names to plant cover, management schedule, curve-number table, and structural features. |
| `management.sch` | Management schedules that sequence operations over time. |
| `cntable.lum` | Curve-number lookup table by land use and soil/hydrologic condition. |
| `cons_practice.lum` | Conservation-practice parameter database. |
| `ovn_table.lum` | Overland Manning's `n` lookup table. |

## Calibration Files

| File | Intro |
| --- | --- |
| `cal_parms.cal` | Calibration parameter definition file. |
| `calibration.cal` | Calibration change/update file. |

## Initial Condition Files

| File | Intro |
| --- | --- |
| `plant.ini` | Initial plant-community condition records. |
| `soil_plant.ini` | Initial soil/plant nutrient, pesticide, pathogen, metal, salt, and constituent pointer records. |
| `om_water.ini` | Named initial organic-mineral water states for channels, reservoirs, wetlands, or related water-storage objects. |

## Soil Files

| File | Intro |
| --- | --- |
| `soils.sol` | Soil profile database for full HRUs. |
| `nutrients.sol` | Soil nutrient/soil-test initialization database. |

## Decision Table Files

| File | Intro |
| --- | --- |
| `lum.dtl` | Land-use/management decision tables, including growth-start and growth-end rules used by some routines. |
| `res_rel.dtl` | Reservoir release decision tables. |

## Extra Input-Like Files Present In `Osu_1hru`

These files are present in the scenario folder but are not all selected directly by the active `file.cio` rows. Treat each as optional, fixed-name, module-specific, or support data until its reader is traced.

| File | Intro |
| --- | --- |
| `cs_aqu.ini` | Initial generic constituent setup for aquifer-related constituent simulation. |
| `cs_channel.ini` | Initial generic constituent setup for channel water/bed constituent simulation. |
| `cs_hru.ini` | Initial generic constituent setup for HRU soil/plant constituent simulation. |
| `salt_aqu.ini` | Initial salt setup for aquifer-related salt simulation. |
| `salt_channel.ini` | Initial salt setup for channel salt simulation. |
| `salt_hru.ini` | Initial salt setup for HRU soil/plant salt simulation. |
| `manure_db.frt` | Manure database with extended manure composition information. |
| `manure_om.frt` | Organic/mineral manure database. |
| `puddle.ops` | Puddling operation definitions. |
| `transplant.plt` | Plant transplant data. |
| `treatment.trt` | Water-treatment or treatment-operation support file. |
| `recall_db.rec` | Untracked local recall database file currently present in the debug scenario; not yet classified in this documentation. |

## Files That Are Probably Outputs Or Generated Support

Files such as `simulation.out`, `diagnostics.out`, `files_out.out`, `co2.out`, `area_calc.out`, `checker.out`, `erosion.out`, `mgt_out.txt`, and many `.swf` files are not treated as primary input files in this catalog. Some `.swf` files may be soft-calibration support data, but they should be traced before being documented as active inputs.

## Current Limits

Verified:

- File groups and active filenames are from `VSProj/SWAT/Osu_1hru/file.cio`.
- The group order is supported by `input_file_module.f90`.
- Several files already have detailed topic notes: `file.cio`, `codes.bsn`, `parameters.bsn`, `print.prt`, `object.cnt`, and `om_water.ini`.

Still partial:

- This catalog does not define every column in every input file.
- Some optional module-specific files are listed as extra input-like files because their exact reader path has not been fully traced in this scenario.
- Output/generated files in the scenario folder need separate classification if they become relevant to debugging.
