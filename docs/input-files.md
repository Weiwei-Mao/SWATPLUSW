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

This file is the high-level map for SWAT+ input files. It is source-aligned with `input_file_module.f90` and includes known fixed-name or companion input files from the current notes. It is designed to grow into a full field-level reference.

Every named input file or input-file family in this map has a corresponding page in [`inputs/`](inputs/). Some pages are detailed references; most are deliberate stubs until their reader paths and fields are traced.

For the broader distinction between active inputs, optional files, generated outputs, and local artifacts in the `Osu_1hru` folder, see [`topics/osu-1hru-file-classification.md`](topics/osu-1hru-file-classification.md).

## Coverage Summary

- Mapped input entries: 170.
- Active in `Osu_1hru` through `file.cio`: 72.
- Detailed per-file references: 6.
- Stub/reference placeholder pages: 164.

## Reference Status

| Status | Meaning |
| --- | --- |
| Detailed | The linked page has reader evidence and at least partial field/parameter interpretation. |
| Stub | The linked page exists to reserve the file reference, but reader path and fields still need tracing. |
| Active | `Osu_1hru/file.cio` selects this file directly. |
| Optional/default | The file is defined in source defaults but is not selected by the current scenario. |
| Fixed-name/companion | The file is opened by convention, derived from another filename, or observed as an optional module input. |
| File family | The exact file name is scenario-specific, but the format family is a SWAT+ input. |

## Master control file

| File | Role | Scenario/source status | Reference |
| --- | --- | --- | --- |
| `file.cio` | Master input manifest; tells SWAT+ which scenario input files to read. | Active | Detailed: [inputs/file-cio.md](inputs/file-cio.md) |

## Simulation

| File | Role | Scenario/source status | Reference |
| --- | --- | --- | --- |
| `constituents.cs` | Input file for simulation; source slot cs_db. | Optional/default | Stub: [inputs/constituents-cs.md](inputs/constituents-cs.md) |
| `object.cnt` | Counts of spatial/object types; used for allocation and object-command setup. | Active | Detailed: [inputs/object-cnt.md](inputs/object-cnt.md) |
| `object.prt` | Input file for simulation; source slot object_prt. | Optional/default | Stub: [inputs/object-prt.md](inputs/object-prt.md) |
| `print.prt` | Output print-control settings: which output groups and intervals are written. | Active | Detailed: [inputs/print-prt.md](inputs/print-prt.md) |
| `time.sim` | Simulation dates, time step, and run period settings. | Active | Stub: [inputs/time-sim.md](inputs/time-sim.md) |

## Basin

| File | Role | Scenario/source status | Reference |
| --- | --- | --- | --- |
| `carbon.bsn` | Optional dynamic carbon basin parameter file when carbon behavior is enabled. | Optional/default | Stub: [inputs/carbon-bsn.md](inputs/carbon-bsn.md) |
| `codes.bsn` | Basin-wide model switches and process-selection codes. | Active | Detailed: [inputs/codes-bsn.md](inputs/codes-bsn.md) |
| `parameters.bsn` | Basin-wide numeric parameters and default coefficients. | Active | Detailed: [inputs/parameters-bsn.md](inputs/parameters-bsn.md) |

## Basin carbon companions

| File | Role | Scenario/source status | Reference |
| --- | --- | --- | --- |
| `carbon_layers.prt` | Optional carbon-layer output control file. | Fixed-name/companion | Stub: [inputs/carbon-layers-prt.md](inputs/carbon-layers-prt.md) |
| `carbon_lyr.bsn` | Companion per-layer file for dynamic carbon basin parameters; derived from the selected carbon basin filename. | Fixed-name/companion | Stub: [inputs/carbon-lyr-bsn.md](inputs/carbon-lyr-bsn.md) |
| `co2.dat` | Optional annual CO2 input series; otherwise the model can use basin defaults. | Fixed-name/companion | Stub: [inputs/co2-dat.md](inputs/co2-dat.md) |

## Climate

| File | Role | Scenario/source status | Reference |
| --- | --- | --- | --- |
| `atmodep.cli` | Input file for climate; source slot atmo_cli. | Optional/default | Stub: [inputs/atmodep-cli.md](inputs/atmodep-cli.md) |
| `hmd.cli` | Input file for climate; source slot hmd_cli. | Optional/default | Stub: [inputs/hmd-cli.md](inputs/hmd-cli.md) |
| `pcp.cli` | Precipitation gauge list; points to precipitation time-series files. | Active | Stub: [inputs/pcp-cli.md](inputs/pcp-cli.md) |
| `pet.cli` | Input file for climate; source slot pet_cli. | Optional/default | Stub: [inputs/pet-cli.md](inputs/pet-cli.md) |
| `slr.cli` | Solar radiation gauge list; points to solar-radiation time-series files. | Active | Stub: [inputs/slr-cli.md](inputs/slr-cli.md) |
| `tmp.cli` | Temperature gauge list; points to temperature time-series files. | Active | Stub: [inputs/tmp-cli.md](inputs/tmp-cli.md) |
| `weather-sta.cli` | Weather station list and links to precipitation, temperature, solar radiation, wind, and generator records. | Active | Stub: [inputs/weather-sta-cli.md](inputs/weather-sta-cli.md) |
| `weather-wgn.cli` | Weather generator station list. | Active | Stub: [inputs/weather-wgn-cli.md](inputs/weather-wgn-cli.md) |
| `wnd.cli` | Wind-speed gauge list; points to wind time-series files. | Active | Stub: [inputs/wnd-cli.md](inputs/wnd-cli.md) |

## Climate time-series files

| File | Role | Scenario/source status | Reference |
| --- | --- | --- | --- |
| `*.hmd` | Relative-humidity time-series file named by a humidity gauge manifest. | File family | Stub: [inputs/hmd-time-series.md](inputs/hmd-time-series.md) |
| `*.pcp` | Precipitation time-series file named by a precipitation gauge manifest. | File family | Stub: [inputs/pcp-time-series.md](inputs/pcp-time-series.md) |
| `*.pet` | Potential-ET time-series file named by a PET gauge manifest. | File family | Stub: [inputs/pet-time-series.md](inputs/pet-time-series.md) |
| `*.slr` | Solar-radiation time-series file named by a solar-radiation gauge manifest. | File family | Stub: [inputs/slr-time-series.md](inputs/slr-time-series.md) |
| `*.tmp` | Temperature time-series file named by a temperature gauge manifest. | File family | Stub: [inputs/tmp-time-series.md](inputs/tmp-time-series.md) |
| `*.wnd` | Wind-speed time-series file named by a wind gauge manifest. | File family | Stub: [inputs/wnd-time-series.md](inputs/wnd-time-series.md) |

## Connect

| File | Role | Scenario/source status | Reference |
| --- | --- | --- | --- |
| `aquifer.con` | Aquifer connection file; defines receiving objects for aquifer outputs. | Active | Stub: [inputs/aquifer-con.md](inputs/aquifer-con.md) |
| `aquifer2d.con` | Input file for connect; source slot aqu2d_con. | Optional/default | Stub: [inputs/aquifer2d-con.md](inputs/aquifer2d-con.md) |
| `chandeg.con` | SWAT-DEG channel connection file; defines routing for `sdc` / `chandeg` objects. | Active | Stub: [inputs/chandeg-con.md](inputs/chandeg-con.md) |
| `channel.con` | Input file for connect; source slot chan_con. | Optional/default | Stub: [inputs/channel-con.md](inputs/channel-con.md) |
| `delratio.con` | Input file for connect; source slot delr_con. | Optional/default | Stub: [inputs/delratio-con.md](inputs/delratio-con.md) |
| `exco.con` | Input file for connect; source slot exco_con. | Optional/default | Stub: [inputs/exco-con.md](inputs/exco-con.md) |
| `gwflow.con` | Input file for connect; source slot gwflow_con. | Optional/default | Stub: [inputs/gwflow-con.md](inputs/gwflow-con.md) |
| `hru.con` | Connection definition for full HRU objects. In QSWAT-style routing, HRUs may have no direct output and are wrapped by routing units. | Active | Stub: [inputs/hru-con.md](inputs/hru-con.md) |
| `hru-lte.con` | Input file for connect; source slot hruez_con. | Optional/default | Stub: [inputs/hru-lte-con.md](inputs/hru-lte-con.md) |
| `outlet.con` | Input file for connect; source slot out_con. | Optional/default | Stub: [inputs/outlet-con.md](inputs/outlet-con.md) |
| `recall.con` | Recall-object connection file; defines routing for external time-series hydrographs. | Active | Stub: [inputs/recall-con.md](inputs/recall-con.md) |
| `reservoir.con` | Input file for connect; source slot res_con. | Optional/default | Stub: [inputs/reservoir-con.md](inputs/reservoir-con.md) |
| `rout_unit.con` | Routing-unit connection file; defines where routing-unit hydrographs go. | Active | Stub: [inputs/rout-unit-con.md](inputs/rout-unit-con.md) |

## Channel

| File | Role | Scenario/source status | Reference |
| --- | --- | --- | --- |
| `channel.cha` | Input file for channel; source slot dat. | Optional/default | Stub: [inputs/channel-cha.md](inputs/channel-cha.md) |
| `channel-lte.cha` | SWAT-DEG channel definition file; describes detailed channel objects used by `sdc` / `chandeg`. | Active | Stub: [inputs/channel-lte-cha.md](inputs/channel-lte-cha.md) |
| `hydrology.cha` | Input file for channel; source slot hyd. | Optional/default | Stub: [inputs/hydrology-cha.md](inputs/hydrology-cha.md) |
| `hyd-sed-lte.cha` | SWAT-DEG hydrology/sediment control parameters. | Active | Stub: [inputs/hyd-sed-lte-cha.md](inputs/hyd-sed-lte-cha.md) |
| `initial.cha` | Named initial channel water-quality/constituent setup; can point to records such as `om_water.ini`. | Active | Stub: [inputs/initial-cha.md](inputs/initial-cha.md) |
| `nutrients.cha` | Channel nutrient and water-quality parameter database. | Active | Stub: [inputs/nutrients-cha.md](inputs/nutrients-cha.md) |
| `sediment.cha` | Input file for channel; source slot sed. | Optional/default | Stub: [inputs/sediment-cha.md](inputs/sediment-cha.md) |
| `temperature.cha` | Input file for channel; source slot temp. | Optional/default | Stub: [inputs/temperature-cha.md](inputs/temperature-cha.md) |

## Reservoir

| File | Role | Scenario/source status | Reference |
| --- | --- | --- | --- |
| `hydrology.res` | Input file for reservoir; source slot hyd_res. | Optional/default | Stub: [inputs/hydrology-res.md](inputs/hydrology-res.md) |
| `hydrology.wet` | Wetland hydrology parameter database. | Active | Stub: [inputs/hydrology-wet.md](inputs/hydrology-wet.md) |
| `initial.res` | Named initial reservoir/wetland water-quality setup. | Active | Stub: [inputs/initial-res.md](inputs/initial-res.md) |
| `nutrients.res` | Reservoir nutrient and water-quality parameter database. | Active | Stub: [inputs/nutrients-res.md](inputs/nutrients-res.md) |
| `reservoir.res` | Input file for reservoir; source slot res. | Optional/default | Stub: [inputs/reservoir-res.md](inputs/reservoir-res.md) |
| `sediment.res` | Reservoir sediment parameter database. | Active | Stub: [inputs/sediment-res.md](inputs/sediment-res.md) |
| `weir.res` | Reservoir release/weir parameter file. | Active | Stub: [inputs/weir-res.md](inputs/weir-res.md) |
| `wetland.wet` | Wetland object parameter file. | Active | Stub: [inputs/wetland-wet.md](inputs/wetland-wet.md) |

## Routing unit

| File | Role | Scenario/source status | Reference |
| --- | --- | --- | --- |
| `rout_unit.def` | Defines each routing unit by listing which element records belong to it. | Active | Stub: [inputs/rout-unit-def.md](inputs/rout-unit-def.md) |
| `rout_unit.dr` | Input file for routing unit; source slot ru_dr. | Optional/default | Stub: [inputs/rout-unit-dr.md](inputs/rout-unit-dr.md) |
| `rout_unit.ele` | Defines routing-unit member elements, such as HRUs, HRU-LTEs, or other spatial elements. | Active | Stub: [inputs/rout-unit-ele.md](inputs/rout-unit-ele.md) |
| `rout_unit.rtu` | Routing-unit parameter file. | Active | Stub: [inputs/rout-unit-rtu.md](inputs/rout-unit-rtu.md) |

## HRU

| File | Role | Scenario/source status | Reference |
| --- | --- | --- | --- |
| `hru-data.hru` | Full HRU database file; links each HRU definition to land use, soil, hydrology, topography, snow, and field records. | Active | Stub: [inputs/hru-data-hru.md](inputs/hru-data-hru.md) |
| `hru-lte.hru` | Input file for HRU; source slot hru_ez. | Optional/default | Stub: [inputs/hru-lte-hru.md](inputs/hru-lte-hru.md) |

## Exco (recall constant)

| File | Role | Scenario/source status | Reference |
| --- | --- | --- | --- |
| `exco.exc` | Input file for exco (recall constant); source slot exco. | Optional/default | Stub: [inputs/exco-exc.md](inputs/exco-exc.md) |
| `exco_hmet.exc` | Input file for exco (recall constant); source slot hmet. | Optional/default | Stub: [inputs/exco-hmet-exc.md](inputs/exco-hmet-exc.md) |
| `exco_om.exc` | Input file for exco (recall constant); source slot om. | Optional/default | Stub: [inputs/exco-om-exc.md](inputs/exco-om-exc.md) |
| `exco_path.exc` | Input file for exco (recall constant); source slot path. | Optional/default | Stub: [inputs/exco-path-exc.md](inputs/exco-path-exc.md) |
| `exco_pest.exc` | Input file for exco (recall constant); source slot pest. | Optional/default | Stub: [inputs/exco-pest-exc.md](inputs/exco-pest-exc.md) |
| `exco_salt.exc` | Input file for exco (recall constant); source slot salt. | Optional/default | Stub: [inputs/exco-salt-exc.md](inputs/exco-salt-exc.md) |

## Recall (daily, monthly and annual)

| File | Role | Scenario/source status | Reference |
| --- | --- | --- | --- |
| `recall.rec` | External time-series hydrograph/input source data for recall objects. | Active | Stub: [inputs/recall-rec.md](inputs/recall-rec.md) |

## Delivery ratio

| File | Role | Scenario/source status | Reference |
| --- | --- | --- | --- |
| `delratio.del` | Input file for delivery ratio; source slot del_ratio. | Optional/default | Stub: [inputs/delratio-del.md](inputs/delratio-del.md) |
| `dr_hmet.del` | Input file for delivery ratio; source slot hmet. | Optional/default | Stub: [inputs/dr-hmet-del.md](inputs/dr-hmet-del.md) |
| `dr_om.del` | Input file for delivery ratio; source slot om. | Optional/default | Stub: [inputs/dr-om-del.md](inputs/dr-om-del.md) |
| `dr_path.del` | Input file for delivery ratio; source slot path. | Optional/default | Stub: [inputs/dr-path-del.md](inputs/dr-path-del.md) |
| `dr_pest.del` | Input file for delivery ratio; source slot pest. | Optional/default | Stub: [inputs/dr-pest-del.md](inputs/dr-pest-del.md) |
| `dr_salt.del` | Input file for delivery ratio; source slot salt. | Optional/default | Stub: [inputs/dr-salt-del.md](inputs/dr-salt-del.md) |

## Aquifer

| File | Role | Scenario/source status | Reference |
| --- | --- | --- | --- |
| `aquifer.aqu` | Lumped aquifer parameter database. | Active | Stub: [inputs/aquifer-aqu.md](inputs/aquifer-aqu.md) |
| `initial.aqu` | Initial aquifer condition records. | Active | Stub: [inputs/initial-aqu.md](inputs/initial-aqu.md) |

## Herd

| File | Role | Scenario/source status | Reference |
| --- | --- | --- | --- |
| `animal.hrd` | Input file for herd; source slot animal. | Optional/default | Stub: [inputs/animal-hrd.md](inputs/animal-hrd.md) |
| `herd.hrd` | Input file for herd; source slot herd. | Optional/default | Stub: [inputs/herd-hrd.md](inputs/herd-hrd.md) |
| `ranch.hrd` | Input file for herd; source slot ranch. | Optional/default | Stub: [inputs/ranch-hrd.md](inputs/ranch-hrd.md) |

## Water-rights

| File | Role | Scenario/source status | Reference |
| --- | --- | --- | --- |
| `element.wro` | Input file for water-rights; source slot element. | Optional/default | Stub: [inputs/element-wro.md](inputs/element-wro.md) |
| `water_allocation.wro` | Input file for water-rights; source slot transfer_wro. | Optional/default | Stub: [inputs/water-allocation-wro.md](inputs/water-allocation-wro.md) |
| `water_rights.wro` | Input file for water-rights; source slot water_rights. | Optional/default | Stub: [inputs/water-rights-wro.md](inputs/water-rights-wro.md) |

## Link

| File | Role | Scenario/source status | Reference |
| --- | --- | --- | --- |
| `aqu_cha.lin` | Input file for link; source slot aqu_cha. | Optional/default | Stub: [inputs/aqu-cha-lin.md](inputs/aqu-cha-lin.md) |
| `chan-surf.lin` | Input file for link; source slot chan_surf. | Optional/default | Stub: [inputs/chan-surf-lin.md](inputs/chan-surf-lin.md) |

## Hydrology

| File | Role | Scenario/source status | Reference |
| --- | --- | --- | --- |
| `field.fld` | Field geometry and field-related parameter database. | Active | Stub: [inputs/field-fld.md](inputs/field-fld.md) |
| `hydrology.hyd` | HRU hydrology parameter database, including ET, lateral flow, percolation, and related coefficients. | Active | Stub: [inputs/hydrology-hyd.md](inputs/hydrology-hyd.md) |
| `topography.hyd` | HRU topography parameter database, including slope, slope length, and related geometry. | Active | Stub: [inputs/topography-hyd.md](inputs/topography-hyd.md) |

## Structural

| File | Role | Scenario/source status | Reference |
| --- | --- | --- | --- |
| `bmpuser.str` | User-defined BMP structural parameter database. | Active | Stub: [inputs/bmpuser-str.md](inputs/bmpuser-str.md) |
| `filterstrip.str` | Filter-strip structural parameter database. | Active | Stub: [inputs/filterstrip-str.md](inputs/filterstrip-str.md) |
| `grassedww.str` | Grassed-waterway structural parameter database. | Active | Stub: [inputs/grassedww-str.md](inputs/grassedww-str.md) |
| `septic.str` | Structural septic-system setup file. | Active | Stub: [inputs/septic-str.md](inputs/septic-str.md) |
| `tiledrain.str` | Structural tile-drain parameter database. | Active | Stub: [inputs/tiledrain-str.md](inputs/tiledrain-str.md) |

## HRU databases

| File | Role | Scenario/source status | Reference |
| --- | --- | --- | --- |
| `fertilizer.frt` | Fertilizer/mineral nutrient database. | Active | Stub: [inputs/fertilizer-frt.md](inputs/fertilizer-frt.md) |
| `metals.mtl` | Input file for HRU databases; source slot hmetcom_db. | Optional/default | Stub: [inputs/metals-mtl.md](inputs/metals-mtl.md) |
| `pathogens.pth` | Input file for HRU databases; source slot pathcom_db. | Optional/default | Stub: [inputs/pathogens-pth.md](inputs/pathogens-pth.md) |
| `pesticide.pes` | Pesticide parameter database. | Active | Stub: [inputs/pesticide-pes.md](inputs/pesticide-pes.md) |
| `plants.plt` | Plant parameter database. | Active | Stub: [inputs/plants-plt.md](inputs/plants-plt.md) |
| `salt.slt` | Input file for HRU databases; source slot saltcom_db. | Optional/default | Stub: [inputs/salt-slt.md](inputs/salt-slt.md) |
| `septic.sep` | Septic-system parameter database. | Active | Stub: [inputs/septic-sep.md](inputs/septic-sep.md) |
| `snow.sno` | Snow parameter database. | Active | Stub: [inputs/snow-sno.md](inputs/snow-sno.md) |
| `tillage.til` | Tillage operation database. | Active | Stub: [inputs/tillage-til.md](inputs/tillage-til.md) |
| `urban.urb` | Urban land-use parameter database. | Active | Stub: [inputs/urban-urb.md](inputs/urban-urb.md) |

## Parameter database files

| File | Role | Scenario/source status | Reference |
| --- | --- | --- | --- |
| `manure_db.frt` | Optional manure database with extended manure composition information. | Fixed-name/companion | Stub: [inputs/manure-db-frt.md](inputs/manure-db-frt.md) |
| `manure_om.frt` | Optional organic/mineral manure database. | Fixed-name/companion | Stub: [inputs/manure-om-frt.md](inputs/manure-om-frt.md) |
| `transplant.plt` | Optional plant transplant data. | Fixed-name/companion | Stub: [inputs/transplant-plt.md](inputs/transplant-plt.md) |

## Operation scheduling

| File | Role | Scenario/source status | Reference |
| --- | --- | --- | --- |
| `chem_app.ops` | Chemical application operation definitions. | Active | Stub: [inputs/chem-app-ops.md](inputs/chem-app-ops.md) |
| `fire.ops` | Fire operation definitions. | Active | Stub: [inputs/fire-ops.md](inputs/fire-ops.md) |
| `graze.ops` | Grazing operation definitions. | Active | Stub: [inputs/graze-ops.md](inputs/graze-ops.md) |
| `harv.ops` | Harvest operation definitions. | Active | Stub: [inputs/harv-ops.md](inputs/harv-ops.md) |
| `irr.ops` | Irrigation operation definitions. | Active | Stub: [inputs/irr-ops.md](inputs/irr-ops.md) |
| `sweep.ops` | Street-sweeping operation definitions. | Active | Stub: [inputs/sweep-ops.md](inputs/sweep-ops.md) |

## Management operation files

| File | Role | Scenario/source status | Reference |
| --- | --- | --- | --- |
| `puddle.ops` | Optional puddling operation definitions. | Fixed-name/companion | Stub: [inputs/puddle-ops.md](inputs/puddle-ops.md) |
| `treatment.trt` | Optional water-treatment or treatment-operation support file. | Fixed-name/companion | Stub: [inputs/treatment-trt.md](inputs/treatment-trt.md) |

## Land use management

| File | Role | Scenario/source status | Reference |
| --- | --- | --- | --- |
| `cntable.lum` | Curve-number lookup table by land use and soil/hydrologic condition. | Active | Stub: [inputs/cntable-lum.md](inputs/cntable-lum.md) |
| `cons_practice.lum` | Conservation-practice parameter database. | Active | Stub: [inputs/cons-practice-lum.md](inputs/cons-practice-lum.md) |
| `landuse.lum` | Land-use-management database; links land-use names to plant cover, management schedule, curve-number table, and structural features. | Active | Stub: [inputs/landuse-lum.md](inputs/landuse-lum.md) |
| `management.sch` | Management schedules that sequence operations over time. | Active | Stub: [inputs/management-sch.md](inputs/management-sch.md) |
| `ovn_table.lum` | Overland Manning's `n` lookup table. | Active | Stub: [inputs/ovn-table-lum.md](inputs/ovn-table-lum.md) |

## Calibration change

| File | Role | Scenario/source status | Reference |
| --- | --- | --- | --- |
| `cal_parms.cal` | Calibration parameter definition file. | Active | Stub: [inputs/cal-parms-cal.md](inputs/cal-parms-cal.md) |
| `calibration.cal` | Calibration change/update file. | Active | Stub: [inputs/calibration-cal.md](inputs/calibration-cal.md) |
| `ch_sed_budget.sft` | Input file for calibration change; source slot ch_sed_budget_sft. | Optional/default | Stub: [inputs/ch-sed-budget-sft.md](inputs/ch-sed-budget-sft.md) |
| `ch_sed_parms.sft` | Input file for calibration change; source slot ch_sed_parms_sft. | Optional/default | Stub: [inputs/ch-sed-parms-sft.md](inputs/ch-sed-parms-sft.md) |
| `codes.sft` | Input file for calibration change; source slot codes_sft. | Optional/default | Stub: [inputs/codes-sft.md](inputs/codes-sft.md) |
| `plant_gro.sft` | Input file for calibration change; source slot plant_gro_sft. | Optional/default | Stub: [inputs/plant-gro-sft.md](inputs/plant-gro-sft.md) |
| `plant_parms.sft` | Input file for calibration change; source slot plant_parms_sft. | Optional/default | Stub: [inputs/plant-parms-sft.md](inputs/plant-parms-sft.md) |
| `water_balance.sft` | Input file for calibration change; source slot water_balance_sft. | Optional/default | Stub: [inputs/water-balance-sft.md](inputs/water-balance-sft.md) |
| `wb_parms.sft` | Input file for calibration change; source slot wb_parms_sft. | Optional/default | Stub: [inputs/wb-parms-sft.md](inputs/wb-parms-sft.md) |

## Initial conditions

| File | Role | Scenario/source status | Reference |
| --- | --- | --- | --- |
| `hmet_hru.ini` | Input file for initial conditions; source slot hmet_soil. | Optional/default | Stub: [inputs/hmet-hru-ini.md](inputs/hmet-hru-ini.md) |
| `hmet_water.ini` | Input file for initial conditions; source slot hmet_water. | Optional/default | Stub: [inputs/hmet-water-ini.md](inputs/hmet-water-ini.md) |
| `om_water.ini` | Named initial organic-mineral water states for channels, reservoirs, wetlands, or related water-storage objects. | Active | Detailed: [inputs/om-water-ini.md](inputs/om-water-ini.md) |
| `path_hru.ini` | Input file for initial conditions; source slot path_soil. | Optional/default | Stub: [inputs/path-hru-ini.md](inputs/path-hru-ini.md) |
| `path_water.ini` | Input file for initial conditions; source slot path_water. | Optional/default | Stub: [inputs/path-water-ini.md](inputs/path-water-ini.md) |
| `pest_hru.ini` | Input file for initial conditions; source slot pest_soil. | Optional/default | Stub: [inputs/pest-hru-ini.md](inputs/pest-hru-ini.md) |
| `pest_water.ini` | Input file for initial conditions; source slot pest_water. | Optional/default | Stub: [inputs/pest-water-ini.md](inputs/pest-water-ini.md) |
| `plant.ini` | Initial plant-community condition records. | Active | Stub: [inputs/plant-ini.md](inputs/plant-ini.md) |
| `salt_hru.ini` | Initial salt setup for HRU soil/plant salt simulation. | Optional/default | Stub: [inputs/salt-hru-ini.md](inputs/salt-hru-ini.md) |
| `salt_water.ini` | Input file for initial conditions; source slot salt_water. | Optional/default | Stub: [inputs/salt-water-ini.md](inputs/salt-water-ini.md) |
| `soil_plant.ini` | Initial soil/plant nutrient, pesticide, pathogen, metal, salt, and constituent pointer records. | Active | Stub: [inputs/soil-plant-ini.md](inputs/soil-plant-ini.md) |

## Constituents, salt, and optional module files

| File | Role | Scenario/source status | Reference |
| --- | --- | --- | --- |
| `cs_aqu.ini` | Initial generic constituent setup for aquifer-related constituent simulation. | Fixed-name/companion | Stub: [inputs/cs-aqu-ini.md](inputs/cs-aqu-ini.md) |
| `cs_channel.ini` | Initial generic constituent setup for channel water/bed constituent simulation. | Fixed-name/companion | Stub: [inputs/cs-channel-ini.md](inputs/cs-channel-ini.md) |
| `cs_hru.ini` | Initial generic constituent setup for HRU soil/plant constituent simulation. | Fixed-name/companion | Stub: [inputs/cs-hru-ini.md](inputs/cs-hru-ini.md) |
| `salt_aqu.ini` | Initial salt setup for aquifer-related salt simulation. | Fixed-name/companion | Stub: [inputs/salt-aqu-ini.md](inputs/salt-aqu-ini.md) |
| `salt_channel.ini` | Initial salt setup for channel salt simulation. | Fixed-name/companion | Stub: [inputs/salt-channel-ini.md](inputs/salt-channel-ini.md) |
| `salt_fertilizer.frt` | Optional salt composition data for fertilizer-related salt simulation. | Fixed-name/companion | Stub: [inputs/salt-fertilizer-frt.md](inputs/salt-fertilizer-frt.md) |

## Soils

| File | Role | Scenario/source status | Reference |
| --- | --- | --- | --- |
| `nutrients.sol` | Soil nutrient/soil-test initialization database. | Active | Stub: [inputs/nutrients-sol.md](inputs/nutrients-sol.md) |
| `soils.sol` | Soil profile database for full HRUs. | Active | Stub: [inputs/soils-sol.md](inputs/soils-sol.md) |
| `soils_lte.sol` | Input file for soils; source slot lte_sol. | Optional/default | Stub: [inputs/soils-lte-sol.md](inputs/soils-lte-sol.md) |

## Conditional

| File | Role | Scenario/source status | Reference |
| --- | --- | --- | --- |
| `flo_con.dtl` | Input file for conditional; source slot dtbl_flo. | Optional/default | Stub: [inputs/flo-con-dtl.md](inputs/flo-con-dtl.md) |
| `lum.dtl` | Land-use/management decision tables, including growth-start and growth-end rules used by some routines. | Active | Stub: [inputs/lum-dtl.md](inputs/lum-dtl.md) |
| `res_rel.dtl` | Reservoir release decision tables. | Active | Stub: [inputs/res-rel-dtl.md](inputs/res-rel-dtl.md) |
| `scen_lu.dtl` | Input file for conditional; source slot dtbl_scen. | Optional/default | Stub: [inputs/scen-lu-dtl.md](inputs/scen-lu-dtl.md) |

## Regions

| File | Role | Scenario/source status | Reference |
| --- | --- | --- | --- |
| `aqu_catunit.def` | Input file for regions; source slot def_aqu. | Optional/default | Stub: [inputs/aqu-catunit-def.md](inputs/aqu-catunit-def.md) |
| `aqu_catunit.ele` | Aquifer calibration/category-unit element file. | Active | Stub: [inputs/aqu-catunit-ele.md](inputs/aqu-catunit-ele.md) |
| `aqu_reg.def` | Input file for regions; source slot def_aqu_reg. | Optional/default | Stub: [inputs/aqu-reg-def.md](inputs/aqu-reg-def.md) |
| `ch_catunit.def` | Input file for regions; source slot def_cha. | Optional/default | Stub: [inputs/ch-catunit-def.md](inputs/ch-catunit-def.md) |
| `ch_catunit.ele` | Input file for regions; source slot ele_cha. | Optional/default | Stub: [inputs/ch-catunit-ele.md](inputs/ch-catunit-ele.md) |
| `ch_reg.def` | Input file for regions; source slot def_cha_reg. | Optional/default | Stub: [inputs/ch-reg-def.md](inputs/ch-reg-def.md) |
| `ls_cal.reg` | Input file for regions; source slot cal_lcu. | Optional/default | Stub: [inputs/ls-cal-reg.md](inputs/ls-cal-reg.md) |
| `ls_reg.def` | Input file for regions; source slot def_reg. | Optional/default | Stub: [inputs/ls-reg-def.md](inputs/ls-reg-def.md) |
| `ls_reg.ele` | Input file for regions; source slot ele_reg. | Optional/default | Stub: [inputs/ls-reg-ele.md](inputs/ls-reg-ele.md) |
| `ls_unit.def` | Landscape-unit definition file. | Active | Stub: [inputs/ls-unit-def.md](inputs/ls-unit-def.md) |
| `ls_unit.ele` | Landscape-unit element membership file. | Active | Stub: [inputs/ls-unit-ele.md](inputs/ls-unit-ele.md) |
| `rec_catunit.def` | Input file for regions; source slot def_psc. | Optional/default | Stub: [inputs/rec-catunit-def.md](inputs/rec-catunit-def.md) |
| `rec_catunit.ele` | Input file for regions; source slot ele_psc. | Optional/default | Stub: [inputs/rec-catunit-ele.md](inputs/rec-catunit-ele.md) |
| `rec_reg.def` | Input file for regions; source slot def_psc_reg. | Optional/default | Stub: [inputs/rec-reg-def.md](inputs/rec-reg-def.md) |
| `res_catunit.def` | Input file for regions; source slot def_res. | Optional/default | Stub: [inputs/res-catunit-def.md](inputs/res-catunit-def.md) |
| `res_catunit.ele` | Input file for regions; source slot ele_res. | Optional/default | Stub: [inputs/res-catunit-ele.md](inputs/res-catunit-ele.md) |
| `res_reg.def` | Input file for regions; source slot def_res_reg. | Optional/default | Stub: [inputs/res-reg-def.md](inputs/res-reg-def.md) |

## Shade factor

| File | Role | Scenario/source status | Reference |
| --- | --- | --- | --- |
| `shade_factor.shf` | Input file for shade factor; source slot ssff_shf. | Optional/default | Stub: [inputs/shade-factor-shf.md](inputs/shade-factor-shf.md) |

## Generated Support And Local Artifacts

Files such as `simulation.out`, `diagnostics.out`, `files_out.out`, `co2.out`, `area_calc.out`, `checker.out`, `erosion.out`, `mgt_out.txt`, many `.swf` files, and the untracked local `recall_db.rec` file are not treated as primary input references here. Document them in scenario classification or output notes until a reader path proves they are stable inputs.

## Current Limits

- This map is broad, but most pages are stubs. Field-level meanings still require reader tracing.
- `input_file_module.f90` provides source-default filenames; an individual scenario only uses the files selected by `file.cio` plus fixed-name or manifest-referenced files.
- Climate time-series filenames are scenario-specific, so this map uses file-family pages such as `*.pcp` rather than hard-coding one station name.

## Related Notes

- [`file.cio` master input file](inputs/file-cio.md)
- [`Osu_1hru` file classification](topics/osu-1hru-file-classification.md)
- [`codes.bsn` basin control codes](inputs/codes-bsn.md)
- [`parameters.bsn` basin parameters](inputs/parameters-bsn.md)
- [`print.prt` output control file](inputs/print-prt.md)
- [`object.cnt` and SWAT+ object concepts](inputs/object-cnt.md)
- [`om_water.ini` initial organic-mineral water state](inputs/om-water-ini.md)
- [Input to output path](input-output.md)
