---
type: guide
tags:
  - swat/spatial-objects
  - swat/input
  - swat/source
title: Spatial object property reading diagrams
---

# Spatial Object Property Reading Diagrams

This note maps each SWAT+ spatial object from `object.cnt` and its connect file
to the object-specific property files and runtime arrays.

The important split is:

- `object.cnt` gives counts by object type.
- `hyd_connect.f90` assigns each type a global range in `ob(:)`.
- Most `*.con` files are read by `hyd_read_connect.f90` into `ob(:)`.
- Object-specific readers later use `ob()%props`, `ob()%num`, or the local
  object number to choose the actual property data.

## Common Connect Shell

```mermaid
flowchart LR
  CNT["object.cnt<br/>sp_ob counts"] -->|"basin_read_objs.f90"| HC["hyd_connect.f90<br/>assigns sp_ob1 start indexes"]
  CON["object-specific *.con file<br/>id, name, gis_id, area, lat/lon, elev,<br/>props, wst, constit, props2, ruleset,<br/>routing targets"] -->|"hyd_read_connect.f90"| OB["ob(global index)<br/>typ, num, name, area_ha,<br/>elev, props, props2, wst,<br/>source and receiver arrays"]
  HC --> OB
  OB -->|"hyd_connect.f90"| ROUTE["routing graph<br/>output object indexes<br/>hyd types: tot, rhg, sur, lat, til<br/>command order"]
```

## Object Summary

| `object.cnt` field | Runtime object type | Output-link keyword | Connect file | Main property path |
|---|---|---|---|---|
| `sp_ob%hru` | `hru` | `hru` | [[hru.con]] | `ob()%props` selects [[hru-data.hru]], which expands to soil, landuse-management, plant community, management schedule, field, snow, and structural databases. See [[hru-property-reading-map]]. |
| `sp_ob%hru_lte` | `hru_lte` | `hlt` | [[hru-lte.con]] | `ob()%props` selects [[hru-lte.hru]]; that row crosswalks to [[plants.plt]], [[lum.dtl]], and [[soils_lte.sol]]. |
| `sp_ob%ru` | `ru` | `ru` | [[rout_unit.con]] | [[rout_unit.rtu]] reads `ru(:)` by local RU number; [[rout_unit.ele]] and [[rout_unit.def]] define member objects and fractions. |
| `sp_ob%gwflow` | `gwflow` | `gwflow` | [[gwflow.con]] | `gwflow_chan_read.f90` reads `chancell.gw`; `gwflow_read.f90` reads grid, cell, zone, HRU/LSU-cell, channel-cell, canal, pump, pond, and output files. |
| `sp_ob%aqu` | `aqu` | `aqu` | [[aquifer.con]] | `ob()%props` selects [[aquifer.aqu]] and initializes `aqu_dat(:)`, `aqu_prm(:)`, and aquifer state. |
| `sp_ob%chan` | `chan` | `cha` | [[channel.con]] | `ob()%props` selects [[channel.cha]], which crosswalks to [[initial.cha]], [[hydrology.cha]], [[sediment.cha]], and [[nutrients.cha]]. |
| `sp_ob%res` | `res` | `res` | [[reservoir.con]] | `ob()%props` selects [[reservoir.res]], which crosswalks to initial, hydrology, release, sediment, nutrient, salt, and constituent reservoir databases. |
| `sp_ob%recall` | `recall` | `recall` | [[recall.con]] | Runtime command uses `ob()%num` to index `recall(:)` and `recall_db(:)`; [[recall_db.rec]] names the time-series files. |
| `sp_ob%exco` | `exco` | `exc` | [[exco.con]] | `ob()%props` selects [[exco.exc]] for optional pest/path/metal/salt hydrographs. In this source branch, the organic-mineral assignment in `exco_read_om.f90` is commented out. |
| `sp_ob%dr` | `dr` | `dr` | [[delratio.con]] | `ob()%props` selects [[delratio.del]], then organic-mineral and optional constituent ratio files; command applies `dr(ob()%props)` to the incoming hydrograph. |
| `sp_ob%outlet` | `outlet` | `out` | [[outlet.con]] | No separate property database in this path; it passes incoming hydrograph to an outlet object. |
| `sp_ob%chandeg` | `chandeg` | `sdc` | [[chandeg.con]] | `ob()%props` selects [[channel-lte.cha]], which crosswalks to [[initial.cha]], [[hyd-sed-lte.cha]], [[sed_nut.cha]], and [[nutrients.cha]]. |
| `sp_ob%canal` | not a normal `hyd_read_connect` object here | water-allocation object | none in `hyd_connect.f90` | Count range is assigned, but canal data are read through [[water_canal.wal]] and GWFLOW canal files. |
| `sp_ob%pump` | not a normal `hyd_read_connect` object here | water-allocation conveyance | none in `hyd_connect.f90` | Count range is assigned, but pump behavior is handled through water-allocation transfer logic and GWFLOW pump files such as [[hru_pump.gw]] and [[pumpex.gw]]. |
| `sp_ob%aqu2d` | not currently used as a separate object | none | [[aquifer2d.con]] | `object.cnt` marks it not currently used; `aqu2d_read` and `aqu2d_init` are called from aquifer/channel setup, not through a separate `sp_ob%aqu2d` command range. |
| `sp_ob%herd` | not currently used | none | none | Count field exists in `object.cnt`, but no normal spatial-object connect path is used in `hyd_connect.f90`. |
| `sp_ob%wro` | not currently used | none | none | Count field exists in `object.cnt`, but no normal spatial-object connect path is used in `hyd_connect.f90`. |

## HRU

```mermaid
flowchart LR
  HCON["hru.con<br/>active HRU shell"] -->|"hyd_read_connect.f90"| HOB["ob(i)<br/>ob(i)%props"]
  HOB -->|"props selects row"| HDATA["hru-data.hru<br/>topo, hyd, soil, lu_mgt,<br/>soil_plant_init, surf_stor,<br/>snow, field"]
  HDATA --> SOIL["soils.sol<br/>soil physical layers"]
  HDATA --> SPI["soil_plant.ini<br/>initial soil and plant setup"]
  SPI --> NUT["nutrients.sol<br/>initial soil nutrient/carbon pools"]
  HDATA --> LUM["landuse.lum<br/>landuse and management pointer"]
  LUM --> PCOM["plant.ini<br/>plant community"]
  PCOM --> PLT["plants.plt<br/>plant parameters"]
  LUM --> MGT["management.sch<br/>operation schedule"]
  HDATA --> STRUCT["field, snow, wetland,<br/>tile/septic/filterstrip/BMP files"]
  SOIL --> HRU["hru(ihru), soil(ihru), soil1(ihru), pcom(ihru)"]
  NUT --> HRU
  PLT --> HRU
  MGT --> HRU
  STRUCT --> HRU
```

See [[hru-property-reading-map]] for the detailed HRU-only diagram.

## HRU-LTE

```mermaid
flowchart LR
  HLTCON["hru-lte.con<br/>active HRU-LTE shell"] -->|"hyd_read_connect.f90"| HLTOB["ob(i)<br/>ob(i)%props"]
  HLTOB -->|"props selects row"| HLTFILE["hru-lte.hru"]
  HLTFILE -->|"hru_lte_read.f90"| HLTDB["hlt_db(props)<br/>area, CN2, ET/percolation,<br/>slope, soil depth, plant,<br/>growth decision table names,<br/>soil texture name"]
  HLTDB --> PLANTS["plants.plt<br/>plant name crosswalk"]
  HLTDB --> LUMDTL["lum.dtl<br/>start/end growing season decisions"]
  HLTDB --> SOLLTE["soils_lte.sol<br/>texture to AWC, porosity,<br/>conductivity"]
  PLANTS --> HLT["hlt(i)<br/>runtime HRU-LTE object"]
  LUMDTL --> HLT
  SOLLTE --> HLT
```

## Routing Unit

```mermaid
flowchart LR
  RUCON["rout_unit.con<br/>active RU shell"] -->|"hyd_read_connect.f90"| RUOB["ob(i)<br/>RU object and routing"]
  RTU["rout_unit.rtu"] -->|"ru_read.f90"| RU["ru(local RU number)<br/>topography and field pointers"]
  TOPO["topography.hyd"] -->|"name crosswalk"| RU
  FIELD["field.fld"] -->|"name crosswalk"| RU

  RUELE["rout_unit.ele<br/>element name, object type,<br/>object number, fraction, dr name"] -->|"ru_read_elements.f90"| ELEM["ru_elem(:)<br/>member object references"]
  RUDEF["rout_unit.def<br/>which elements belong to each RU"] --> ELEM
  DRDB["delratio.del<br/>delivery-ratio database"] -->|"dr name crosswalk"| ELEM
  RUOB --> ROUTE["RU routing and aggregation"]
  RU --> ROUTE
  ELEM --> ROUTE
```

For RU, the connect file defines the active RU object and routing shell. The
`rout_unit.rtu` file fills `ru(:)` by local RU number rather than through a
separate `ru_db(props)` array.

## Aquifer

```mermaid
flowchart LR
  AQCON["aquifer.con<br/>active aquifer shell"] -->|"hyd_read_connect.f90"| AQOB["ob(i)<br/>ob(i)%props and area"]
  AQFILE["aquifer.aqu"] -->|"aqu_read.f90"| AQDB["aqudb(:)<br/>aquifer property database"]
  AQOB -->|"props selects row"| INIT["aqu_initial.f90"]
  AQDB --> INIT
  INIT --> AQDAT["aqu_dat(iaq)<br/>selected aquifer parameters"]
  INIT --> AQPRM["aqu_prm(iaq)<br/>area, alpha, N loss factors"]
  INIT --> AQSTATE["aqu_d(iaq)<br/>flow, storage, water table,<br/>NO3, carbon, constituents"]
  AQ2D["aquifer2d.con<br/>support file path"] -->|"aqu2d_read / aqu2d_init"| LINK["stream-aquifer interaction setup"]
```

## Regular Channel

```mermaid
flowchart LR
  CHCON["channel.con<br/>active regular channel shell"] -->|"hyd_read_connect.f90"| CHOB["ob(i)<br/>ob(i)%props"]
  CHFILE["channel.cha"] -->|"ch_read.f90"| CHDAT["ch_dat(props)<br/>links to init, hyd, sed, nut"]
  INIT["initial.cha<br/>initial water-quality state"] --> CHDAT
  HYD["hydrology.cha<br/>geometry and hydraulic parameters"] --> CHDAT
  SED["sediment.cha<br/>bank/bed sediment parameters"] --> CHDAT
  NUT["nutrients.cha<br/>nutrient and water-quality parameters"] --> CHDAT
  CHOB -->|"props selects row"| CHINIT["proc_cha.f90<br/>ch_ttcoef + ch_initial"]
  CHDAT --> CHINIT
  CHINIT --> CHSTATE["regular channel runtime state<br/>ch(:), ch_hyd(:), ch_sed(:), ch_nut(:)"]
```

Regular channels use `sp_ob%chan`, runtime type `chan`, and output-link keyword
`cha`.

## SWAT-DEG Channel

```mermaid
flowchart LR
  SDCON["chandeg.con<br/>active SWAT-DEG channel shell"] -->|"hyd_read_connect.f90"| SDOB["ob(i)<br/>ob(i)%props<br/>ob(i)%props2"]
  LTE["channel-lte.cha"] -->|"sd_channel_read.f90"| SDDAT["sd_dat(props)<br/>initc, hydc, sedc, nutc"]
  INIT["initial.cha<br/>plus optional initial pest/path/salt/cs files"] -->|"initc crosswalk"| SDDAT
  HYDSED["hyd-sed-lte.cha"] -->|"hydc crosswalk"| SDDAT
  SEDNUT["sed_nut.cha"] -->|"hydc crosswalk for sediment/nutrient controls"| SDDAT
  NUT["nutrients.cha"] -->|"nutc crosswalk"| SDDAT
  SDOB -->|"props selects sd_dat row"| SDINIT["sd_hydsed_init.f90"]
  SDDAT --> SDINIT
  SDINIT --> SDCH["sd_ch(i)<br/>morphology, rating curves,<br/>channel/floodplain water,<br/>sediment, nutrients, constituents"]
  SDOB -->|"props2 used by command.f90"| SURF["surface-link object for SWAT-DEG channel"]
```

SWAT-DEG channels use `sp_ob%chandeg`, runtime type `chandeg`, and output-link
keyword `sdc`. In `command.f90`, `ob(icmd)%num` is the SWAT-DEG channel number
and `ob(icmd)%props2` is also used during SWAT-DEG channel control.

## Reservoir

```mermaid
flowchart LR
  RESCON["reservoir.con<br/>active reservoir shell"] -->|"hyd_read_connect.f90"| RESOB0["ob(i)<br/>ob(i)%props"]
  RESOB0 -->|"res_objects.f90"| RESOB["res_ob(ires)<br/>global object number and props"]
  RESFILE["reservoir.res"] -->|"res_read.f90"| RESDAT["res_dat(props)<br/>init, hyd, release, sed, nut,<br/>salt/cs links"]
  INIT["initial.res<br/>initial water-quality state"] --> RESDAT
  HYD["hydrology.res<br/>volume-area and routing parameters"] --> RESDAT
  REL["release table<br/>ctbl_* or dtbl_res"] --> RESDAT
  SED["sediment.res"] --> RESDAT
  NUT["nutrients.res"] --> RESDAT
  RESOB -->|"props selects row"| RINIT["res_initial.f90"]
  RESDAT --> RINIT
  RINIT --> RESSTATE["reservoir runtime state<br/>res(:), res_ob(:), res_hyd(:),<br/>water quality and constituent state"]
```

## Recall, Export Coefficient, Delivery Ratio, Outlet

```mermaid
flowchart LR
  RECCON["recall.con"] -->|"hyd_read_connect.f90"| RECOB["ob(i)<br/>runtime uses ob(i)%num"]
  RECDB["recall_db.rec"] -->|"recalldb_read.f90"| RECFILES["time-series files<br/>org-min, pest, path,<br/>hmet, salt, constituents"]
  RECFILES --> RECSTATE["recall(:)<br/>point-source hydrographs"]
  RECOB -->|"command.f90 selects recall(ob%num)"| RECSTATE

  EXCON["exco.con"] -->|"hyd_read_connect.f90"| EXOB["ob(i)<br/>ob(i)%props"]
  EXDB["exco.exc"] -->|"exco_db_read.f90"| EXFILES["exco_om.exc<br/>exco_pest.exc<br/>exco_path.exc<br/>exco_hmet.exc<br/>exco_salt.exc"]
  EXFILES --> EXSTATE["export coefficient hydrographs<br/>optional constituents use ob%props"]
  EXOB --> EXSTATE

  DRCON["delratio.con"] -->|"hyd_read_connect.f90"| DROB["ob(i)<br/>ob(i)%props"]
  DRDB["delratio.del"] -->|"dr_db_read.f90"| DRFILES["delivery-ratio hydrograph files"]
  DRFILES --> DRSTATE["dr(:)<br/>delivery-ratio multipliers"]
  DROB -->|"command.f90 applies dr(ob%props) to incoming hydrograph"| DRSTATE

  OUTCON["outlet.con"] -->|"hyd_read_connect.f90"| OUTOB["ob(i)<br/>outlet shell"]
  OUTOB -->|"command.f90"| OUTSTATE["outlet hydrograph = incoming hydrograph"]
```

## GWFLOW

```mermaid
flowchart LR
  GWCON["gwflow.con<br/>active GWFLOW object shell"] -->|"hyd_read_connect.f90"| GWOB["ob(i)<br/>gwflow object"]
  CHCELL["chancell.gw<br/>channel-cell connections"] -->|"gwflow_chan_read.f90"| CHLINK["gw_chan_* arrays"]
  GWIN["gwflow input set<br/>gwflow.codes, cells, zones,<br/>cell properties, solutes,<br/>boundary and output files"] -->|"gwflow_read.f90"| GWSTATE["gw_state(:)<br/>groundwater grid state"]
  HRUCELL["hrucell.gw or lsucell.gw<br/>HRU/LSU-cell overlaps"] -->|"gwflow_read.f90"| OBLINK["SWAT+ object to grid-cell fractions"]
  OPTIONAL["optional GWFLOW files<br/>gwflow_canal.con, hru_pump.gw,<br/>pumpex.gw, ponds/pond_cell files,<br/>transit/output groups"] -->|"gwflow_read.f90"| GWSTATE
  GWOB --> GWSTATE
  CHLINK --> GWSTATE
  OBLINK --> GWSTATE
```

In this branch, `gwflow_chan_read.f90` uses `sp_ob%gwflow` as the number of
channel-cell connection rows. GWFLOW is therefore more like a grid subsystem
attached to SWAT+ objects than a simple single-row property database.

## Canal, Pump, Aquifer2D, Herd, Water Rights

```mermaid
flowchart LR
  CNT["object.cnt fields<br/>canal, pump, aqu2d, herd, wro"] --> HC["hyd_connect.f90"]
  HC --> RANGE["canal and pump get sp_ob1 ranges<br/>aqu2d range is commented out<br/>herd and wro are not normal connect objects"]

  WCAN["water_canal.wal"] -->|"water_canal_read.f90"| CANAL["canal(:)<br/>water-allocation canal data"]
  GWCA["gwflow_canal.con<br/>plus GWFLOW canal files"] -->|"gwflow_read.f90"| GW_CANAL["GWFLOW canal-cell exchange"]
  HPUMP["hru_pump.gw"] -->|"gwflow_read / gwflow_simulate"| HRUPUMP["HRU groundwater pumping"]
  PUMPX["pumpex.gw"] -->|"gwflow_read / gwflow_pump_ext"| PUMPEX["external pumping"]
  AQ2D["aquifer2d.con"] -->|"aqu2d_read / aqu2d_init"| AQLINK["stream-aquifer interaction support"]
```

These fields are included in `object.cnt`, but they are not all equivalent to
the normal `*.con -> hyd_read_connect -> ob()%props -> property database` pattern.
For this source branch:

- `canal` is mainly read from `water_canal.wal` and GWFLOW canal files.
- `pump` appears through water-allocation conveyance and GWFLOW pump files.
- `aqu2d` is marked not currently used as its own spatial-object count, although
  `aqu2d_read` and `aqu2d_init` are still called in the aquifer/channel setup.
- `herd` and `wro` are count fields with no normal spatial-object reader path in
  `hyd_connect.f90`.

## Source Routine Anchors

- [[object.cnt]] is read by [[basin_read_objs.f90]].
- [[hyd_connect.f90]] assigns `sp_ob1` ranges and calls `hyd_read_connect.f90`.
- [[hyd_read_connect.f90]] reads most spatial-object connect files into `ob(:)`.
- [[main.f90]] calls `hyd_connect`, then recall, exco, delivery ratio, HRU,
  channel, aquifer, HRU-LTE, canal, reservoir, and output setup routines.
- [[command.f90]] executes the routed objects during simulation.
