---
type: overview
tags:
  - swat/overview
  - swat/input
  - swat/scenario
title: Osu_1hru Input Inventory
purpose: "Inventory of configured files, active objects, record references, and optional hardcoded inputs in the default debug scenario."
status: verified
source_revision: "cb442f7c05fc3bfc34349c446010f452d2737ca0"
scenario: "VSProj/SWAT/Osu_1hru"
---

# Osu_1hru Input Inventory

This page answers two different questions:

1. Which files are configured and present?
2. Which object and process paths are active in this scenario?

A file can be present, and even named in `file.cio`, without an active object using it.

## Inventory Result

- [`file.cio`](../../../VSProj/SWAT/Osu_1hru/file.cio) contains **71 distinct non-`null` filenames**.
- All **71 of 71** named files exist in `VSProj/SWAT/Osu_1hru`.
- Climate control files lead to four measured child series: `Imsilpcp.pcp`, `Imsiltmp.tmp`, `Imsilsol.slr`, and `Imsilwind.wnd`; all are present.
- Relative humidity is configured as `sim`, so there is no measured humidity child file.
- Presence is complete at the configured-file level. Activity still depends on object counts, connection files, record names, and basin switches.

## `file.cio` Groups

`null` slots are intentionally omitted from this table.

| Group | Configured filenames |
|---|---|
| simulation | `time.sim`, `print.prt`, `object.cnt` |
| basin | `codes.bsn`, `parameters.bsn` |
| climate | `weather-sta.cli`, `weather-wgn.cli`, `pcp.cli`, `tmp.cli`, `slr.cli`, `wnd.cli` |
| connect | `hru.con`, `rout_unit.con`, `aquifer.con`, `recall.con`, `chandeg.con` |
| channel | `initial.cha`, `nutrients.cha`, `channel-lte.cha`, `hyd-sed-lte.cha` |
| reservoir/wetland | `initial.res`, `sediment.res`, `nutrients.res`, `weir.res`, `wetland.wet`, `hydrology.wet` |
| routing unit | `rout_unit.def`, `rout_unit.ele`, `rout_unit.rtu` |
| HRU | `hru-data.hru` |
| recall | `recall.rec` |
| aquifer | `initial.aqu`, `aquifer.aqu` |
| hydrology | `hydrology.hyd`, `topography.hyd`, `field.fld` |
| structural | `tiledrain.str`, `septic.str`, `filterstrip.str`, `grassedww.str`, `bmpuser.str` |
| HRU parameter database | `plants.plt`, `fertilizer.frt`, `tillage.til`, `pesticide.pes`, `urban.urb`, `septic.sep`, `snow.sno` |
| operations | `harv.ops`, `graze.ops`, `irr.ops`, `chem_app.ops`, `fire.ops`, `sweep.ops` |
| land use/management | `landuse.lum`, `management.sch`, `cntable.lum`, `cons_practice.lum`, `ovn_table.lum` |
| calibration/change | `cal_parms.cal`, `calibration.cal` |
| initialization | `plant.ini`, `soil_plant.ini`, `om_water.ini` |
| soils | `soils.sol`, `nutrients.sol` |
| decision tables | `lum.dtl`, `res_rel.dtl` |
| regions | `ls_unit.ele`, `ls_unit.def`, `aqu_catunit.ele` |

See [[file.cio]] for the field-by-field schema and [[input-file-architecture]] for registered versus hardcoded filenames.

## Active Object Topology

[`object.cnt`](../../../VSProj/SWAT/Osu_1hru/object.cnt) defines a 10 ha scenario with four command objects:

| Object type | Count | Active record |
|---|---:|---|
| HRU | 1 | `hru0001` |
| routing unit | 1 | `rtu001` |
| aquifer | 1 | `aqu001` connection, aquifer database index 1 |
| SWAT-deg channel | 1 | `cha01` (`lcha` column in `object.cnt`, `sp_ob%chandeg` in source) |
| HRU-LTE, conventional channel, reservoir, recall, exco, delivery ratio, outlet, groundwater-flow grid | 0 | not active by object count |

Important connection evidence:

- [`hru.con`](../../../VSProj/SWAT/Osu_1hru/hru.con) assigns 10 ha HRU `hru0001` to weather station `s35610n127290e`.
- [`rout_unit.ele`](../../../VSProj/SWAT/Osu_1hru/rout_unit.ele) puts HRU 1 into routing unit 1 at fraction 1.
- [`rout_unit.con`](../../../VSProj/SWAT/Osu_1hru/rout_unit.con) sends total flow to SWAT-deg channel 1 and recharge to aquifer 1.
- [`aquifer.con`](../../../VSProj/SWAT/Osu_1hru/aquifer.con) sends aquifer flow to SWAT-deg channel 1.
- [`chandeg.con`](../../../VSProj/SWAT/Osu_1hru/chandeg.con) activates `cha01`, which uses channel database index 1 and has no downstream object.
- The runtime dispatch to inspect is `hru -> ru`, branching through `aqu` and `chandeg`, in [`command.f90`](../../../SWATPLUS/swatplus/src/command.f90). Use the actual `cmd_next` and `ob(icmd)%typ` values when debugging rather than relying on this shorthand.

The SWAT-deg channel path is active and uses `channel-lte.cha` plus `hyd-sed-lte.cha`. The conventional channel count is zero. Reservoir and recall libraries remain configured and present, but their object counts are zero; their presence is not evidence that those object paths execute.

## Active HRU Record Chain

[`hru-data.hru`](../../../VSProj/SWAT/Osu_1hru/hru-data.hru) selects these named records:

| Role | Selected record | Controlling file |
|---|---|---|
| topography | `topohru0001` | `topography.hyd` |
| hydrology | `hyd0001` | `hydrology.hyd` |
| soil | `PadHOEGOG` | `soils.sol` |
| land use/management | `rice140_lum` | `landuse.lum` |
| soil/plant initialization | `soilplant1` | `soil_plant.ini` |
| surface storage | `paddy0001` | `wetland.wet` |
| snow | `snow001` | `snow.sno` |
| field | `null` | no `field.fld` record assigned to this HRU |

`rice140_lum` then links to plant community `rice140_comm`, management schedule `rice140_rot`, curve-number record `rc_strow_g`, conservation practice `cross_slope`, and overland record `convtill_res`. The management schedule and `lum.dtl` drive the rice/paddy event sequence seen in `mgt_out.txt`.

## Climate Chain

| Layer | Selection |
|---|---|
| HRU connection | station `s35610n127290e` |
| station record | WGN `Imsil`; precipitation `Imsilpcp.pcp`; temperature `Imsiltmp.tmp`; solar `Imsilsol.slr`; humidity `sim`; wind `Imsilwind.wnd` |
| list files | `pcp.cli`, `tmp.cli`, `slr.cli`, `wnd.cli` repeat the four measured child filenames |
| weather generator | `weather-wgn.cli` contains the `Imsil` record |

When debugging climate, stop first in `climate_control`, then in the relevant measured reader. Do not look for a humidity file in this scenario because that field is simulated.

## Basin Switches That Limit Activity

[`codes.bsn`](../../../VSProj/SWAT/Osu_1hru/codes.bsn) currently has:

| Switch | Value | Scenario implication |
|---|---:|---|
| `pet` | 1 | selected PET method; `pet_file` is `null` |
| `event` | 0 | daily simulation path |
| `carbon` | 0 | carbon option is off |
| `gw_flow` | 0 | gridded groundwater-flow subsystem is off |
| `tiledrain` | 0 | tile-drain switch is off |
| `atmo_dep` | `a` | atmospheric deposition mode comes from basin controls, without an `atmodep.cli` filename in `file.cio` |

The simulation-level constituent database field is `null`. `constit_db_read` therefore leaves salt/constituent counts at zero. Salt and CS files in the folder do not by themselves prove that constituent transport is active.

## Hardcoded And Optional Files

These files are outside the 71 `file.cio` names. Their readers and mechanisms are indexed in [[hardcoded-input-files]].

| File group | Present in scenario | Interpretation |
|---|---|---|
| `manure_om.frt`, `manure_db.frt`, `transplant.plt`, `puddle.ops` | yes | optional databases/operations available to the management path; the baseline management output includes manure and paddy operations |
| `salt_hru.ini`, `salt_aqu.ini`, `salt_channel.ini` | yes | hardcoded salt initialization files are present, but salt counts are zero because the constituent master file is `null` |
| `cs_hru.ini`, `cs_aqu.ini` | yes | constituent initialization files are present, but CS counts are zero |
| `co2_yr.dat`, `carbon_layers.prt`, `carbon_lyr.bsn` | no | consistent with `carbon = 0`; readers treat these as optional |
| `pest_metabolite.pes`, `satbuffer.str`, `shade_factor.shf` | no | optional-reader paths; `shade_factor_read` allocates an empty database when its default file is absent |
| `recall_db.rec`, `pest.com`, `cs_recall.rec`, `salt_recall.rec` | no | hardcoded recall companions absent; recall object count is zero |

`recall.rec` is separately present because it is named in `file.cio`, but the current `recalldb_read` implementation opens hardcoded `recall_db.rec`. With zero recall objects, neither filename indicates an active recall path here.

## Recheck After Scenario Edits

Re-run these checks whenever `file.cio`, `object.cnt`, a connection file, or `hru-data.hru` changes:

1. Count distinct non-`null` `file.cio` filenames and test that each exists.
2. Read `object.cnt` before deciding which connection/object files matter at runtime.
3. Follow selected record names from `hru-data.hru` into their database files.
4. Follow station records into measured child climate files.
5. Check basin switches and constituent counts before treating optional hardcoded files as active.
6. Run the [[osu-1hru-baseline-and-debug]] checks and compare output payloads.
