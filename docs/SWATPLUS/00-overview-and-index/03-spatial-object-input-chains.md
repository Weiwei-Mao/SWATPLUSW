---
type: guide
tags:
  - swat/spatial-objects
  - swat/input
  - swat/source
title: Spatial object input chains
purpose: "Property-reading diagrams for non-HRU SWAT+ spatial object families"
status: verified
source_revision: "object.cnt, hyd_connect.f90, hyd_read_connect.f90, command.f90, proc_cha.f90, proc_aqu.f90, proc_res.f90, ru_read.f90, ru_read_elements.f90, gwflow_read.f90"
---

# Spatial Object Input Chains

This note covers the non-HRU object families. Use [[02-hru-input-chain]] for
the HRU, because the HRU has its own soil, plant, landuse, and management
subtree.

## Common Connect Shell

Most spatial objects start with the same connect-file shell:

```mermaid
flowchart LR
  CNT["object.cnt<br/>object count"] --> CON["object-specific .con file"]
  CON --> OB["ob(:)<br/>runtime object shell"]
  CON --> PROP["object property pointer<br/>usually the 8th field"]
  CON --> ROUTE["out_tot route groups<br/>obj_typ, obj_id, hyd_typ, frac"]
  PROP --> DB["object property database"]
```

This pattern is useful, but not universal. RU, recall, outlet, GWFLOW, canal,
pump, aquifer2D, herd, and water rights have special behavior.

## Object Summary

| `object.cnt` field | Runtime object type | Output-link keyword | Connect file | Main property path |
|---|---|---|---|---|
| `sp_ob%hru_lte` | `hru_lte` | `hlt` | [[hru-lte.con]] | `ob()%props` selects [[hru-lte.hru]], which crosswalks to [[plants.plt]], [[lum.dtl]], and [[soils_lte.sol]]. |
| `sp_ob%ru` | `ru` | `ru` | [[rout_unit.con]] | [[rout_unit.rtu]] fills `ru(:)` by local RU number; [[rout_unit.def]] and [[rout_unit.ele]] define members. |
| `sp_ob%gwflow` | `gwflow` | `gwflow` | [[gwflow.con]] | `gwflow_read.f90` reads grid, cell, HRU/LSU-cell, channel-cell, canal, pump, pond, transit, and output files. |
| `sp_ob%aqu` | `aqu` | `aqu` | [[aquifer.con]] | `ob()%props` selects [[aquifer.aqu]] and initializes aquifer state. |
| `sp_ob%chan` | `chan` | `cha` | [[channel.con]] | `ob()%props` selects [[channel.cha]], which crosswalks to channel initialization, hydrology, sediment, and nutrient databases. |
| `sp_ob%res` | `res` | `res` | [[reservoir.con]] | `ob()%props` selects [[reservoir.res]], which crosswalks to initial, hydrology, release, sediment, nutrient, salt, and constituent databases. |
| `sp_ob%recall` | `recall` | `recall` | [[recall.con]] | Runtime command uses `ob()%num`; [[recall_db.rec]] names time-series files. |
| `sp_ob%exco` | `exco` | `exc` | [[exco.con]] | `ob()%props` selects [[exco.exc]] and optional transfer hydrographs. |
| `sp_ob%dr` | `dr` | `dr` | [[delratio.con]] | `ob()%props` selects [[delratio.del]] and optional ratio hydrographs. |
| `sp_ob%outlet` | `outlet` | `out` | [[outlet.con]] | No separate property database in this path. |
| `sp_ob%chandeg` | `chandeg` | `sdc` | [[chandeg.con]] | `ob()%props` selects [[channel-lte.cha]], which crosswalks to [[initial.cha]], [[hyd-sed-lte.cha]], [[sed_nut.cha]], and [[nutrients.cha]]. |
| `sp_ob%canal` | special | water-allocation object | none through `hyd_read_connect` here | Count range exists, but canal data are read through [[water_canal.wal]] and GWFLOW canal files. |
| `sp_ob%pump` | special | water-allocation conveyance | none through `hyd_read_connect` here | Pump behavior is handled through water-allocation transfer logic and GWFLOW pump files such as [[hru_pump.gw]] and [[pumpex.gw]]. |
| `sp_ob%aqu2d` | support path | none | [[aquifer2d.con]] | `aqu2d_read` and `aqu2d_init` are called from aquifer/channel setup; it is not a normal active command object here. |
| `sp_ob%herd`, `sp_ob%wro` | not normal connect objects | none | none in `hyd_connect.f90` | Count fields exist, but no normal spatial-object connect path is used here. |

## HRU-LTE

```mermaid
flowchart LR
  CON["hru-lte.con<br/>active HRU-LTE shell"] -->|"hyd_read_connect.f90"| OB["ob(i)<br/>ob(i)%props"]
  OB -->|"props selects row"| HLTFILE["hru-lte.hru"]
  HLTFILE -->|"hru_lte_read.f90"| HLTDB["hlt_db(props)<br/>area, CN2, ET, percolation,<br/>slope, soil depth, plant,<br/>decision table names, texture"]
  HLTDB --> PLANT["plants.plt"]
  HLTDB --> LUMDTL["lum.dtl"]
  HLTDB --> SOLLTE["soils_lte.sol"]
  PLANT --> HLT["hlt(:)<br/>runtime HRU-LTE object"]
  LUMDTL --> HLT
  SOLLTE --> HLT
```

## Routing Unit

Routing units group member objects, often HRUs, and route the combined
hydrographs downstream.

```mermaid
flowchart LR
  CON["rout_unit.con<br/>active RU shell"] -->|"hyd_read_connect.f90"| RUOB["ob(i)<br/>RU shell and routing"]
  RTU["rout_unit.rtu"] -->|"ru_read.f90"| RU["ru(local RU number)<br/>topography and field pointers"]
  TOPO["topography.hyd"] --> RU
  FIELD["field.fld"] --> RU
  DEF["rout_unit.def<br/>which elements belong to each RU"] --> ELEM["ru_elem(:)<br/>member object references"]
  ELE["rout_unit.ele<br/>object type, id, fraction, dr name"] --> ELEM
  DR["delratio.del<br/>optional delivery ratio"] --> ELEM
  RUOB --> ROUTE["RU aggregation and routing"]
  RU --> ROUTE
  ELEM --> ROUTE
```

Important caveat: in this source branch `rout_unit.rtu` fills `ru(:)` by local
RU number rather than through a separate `ru_db(props)` array. Keep the RU
connect row and `rout_unit.rtu` row order aligned.

## Aquifer

```mermaid
flowchart LR
  CON["aquifer.con<br/>active aquifer shell"] -->|"hyd_read_connect.f90"| OB["ob(i)<br/>ob(i)%props and area"]
  AFILE["aquifer.aqu"] -->|"aqu_read.f90"| ADB["aqudb(:)<br/>aquifer parameter database"]
  OB -->|"props selects row"| INIT["aqu_initial.f90"]
  ADB --> INIT
  INIT --> ADAT["aqu_dat(:)<br/>selected parameters"]
  INIT --> APRM["aqu_prm(:)<br/>area, alpha, N loss factors"]
  INIT --> ASTATE["aqu_d(:)<br/>flow, storage, water table,<br/>NO3, carbon, constituents"]
  AQ2D["aquifer2d.con"] -->|"aqu2d_read / aqu2d_init"| LINK["stream-aquifer interaction setup"]
```

## Regular Channel

```mermaid
flowchart LR
  CON["channel.con<br/>active regular channel shell"] -->|"hyd_read_connect.f90"| OB["ob(i)<br/>ob(i)%props"]
  CFILE["channel.cha"] -->|"ch_read.f90"| CDAT["ch_dat(props)<br/>init, hyd, sed, nut"]
  INIT["initial.cha"] --> CDAT
  HYD["hydrology.cha"] --> CDAT
  SED["sediment.cha"] --> CDAT
  NUT["nutrients.cha"] --> CDAT
  TEMP["temperature.cha"] --> WTEMP["w_temp(:)<br/>read by ch_read_temp.f90"]
  OB -->|"props selects row"| CINIT["proc_cha.f90<br/>ch_ttcoef + ch_initial"]
  CDAT --> CINIT
  CINIT --> CSTATE["regular channel runtime state"]
  WTEMP --> CHTEMP["ch_temp.f90<br/>water-temperature simulation"]
```

`temperature.cha` is read through the channel file group, but it is not a text
pointer inside `channel.cha`.

## SWAT-DEG Channel

```mermaid
flowchart LR
  CON["chandeg.con<br/>active SWAT-DEG channel shell"] -->|"hyd_read_connect.f90"| OB["ob(i)<br/>ob(i)%props<br/>ob(i)%props2"]
  LTE["channel-lte.cha"] -->|"sd_channel_read.f90"| SDAT["sd_dat(props)<br/>initc, hydc, sedc, nutc"]
  INIT["initial.cha<br/>plus optional constituent initial files"] -->|"initc"| SDAT
  HYDSED["hyd-sed-lte.cha"] -->|"hydc"| SDAT
  SEDNUT["sed_nut.cha"] -->|"hydc sediment/nutrient controls"| SDAT
  NUT["nutrients.cha"] -->|"nutc"| SDAT
  OB -->|"props selects sd_dat row"| SINIT["sd_hydsed_init.f90"]
  SDAT --> SINIT
  SINIT --> SSTATE["sd_ch(:)<br/>morphology, rating curves,<br/>water, sediment, nutrients, constituents"]
  OB -->|"props2 used by command.f90"| SURF["surface-link object"]
```

SWAT-DEG channels use output-link keyword `sdc`.

Read the SWAT-DEG chain as a two-step lookup:

| Step | File / field | Runtime result | Meaning |
|---|---|---|---|
| 1 | [[chandeg.con]] field `lcha` | `ob(i)%props` | Selects one row in [[channel-lte.cha]]. |
| 2 | [[channel-lte.cha]] field `cha_ini` | `sd_dat(props)%init` | Selects an initial-condition row in [[initial.cha]]. |
| 3 | [[channel-lte.cha]] field `cha_hyd` | `sd_dat(props)%hyd` | Selects geometry and hydrology/sediment parameters in [[hyd-sed-lte.cha]]. |
| 4 | [[channel-lte.cha]] field `cha_nut` | `sd_dat(props)%nut` | Selects water-quality coefficients in [[nutrients.cha]]. |

In the current source path, [[channel-lte.cha]] field `cha_sed` is read into
`sd_dat()%sedc`, but the optional [[sed_nut.cha]] lookup is matched by
`cha_hyd` / `sd_dat()%hydc` in `sd_channel_read.f90`.

## Reservoir

```mermaid
flowchart LR
  CON["reservoir.con<br/>active reservoir shell"] -->|"hyd_read_connect.f90"| OB["ob(i)<br/>ob(i)%props"]
  OB -->|"res_objects.f90"| ROB["res_ob(:)<br/>global object number and props"]
  RFILE["reservoir.res"] -->|"res_read.f90"| RDAT["res_dat(props)<br/>init, hyd, release, sed, nut,<br/>salt/cs links"]
  INIT["initial.res"] --> RDAT
  HYD["hydrology.res"] --> RDAT
  REL["release table<br/>ctbl_* or dtbl_res"] --> RDAT
  SED["sediment.res"] --> RDAT
  NUT["nutrients.res"] --> RDAT
  ROB -->|"props selects row"| RINIT["res_initial.f90"]
  RDAT --> RINIT
  RINIT --> RSTATE["reservoir runtime state"]
```

## Recall, Exco, Delivery Ratio, Outlet

```mermaid
flowchart LR
  RECCON["recall.con"] -->|"hyd_read_connect.f90"| RECOB["ob(i)<br/>runtime uses ob(i)%num"]
  RECDB["recall_db.rec"] -->|"recalldb_read.f90"| RECFILES["time-series files"]
  RECFILES --> RECSTATE["recall(:)<br/>point-source hydrographs"]
  RECOB -->|"command.f90 selects recall(ob%num)"| RECSTATE

  EXCON["exco.con"] -->|"hyd_read_connect.f90"| EXOB["ob(i)<br/>ob(i)%props"]
  EXDB["exco.exc"] -->|"exco_db_read.f90"| EXFILES["exco_om.exc<br/>exco_pest.exc<br/>exco_path.exc<br/>exco_hmet.exc<br/>exco_salt.exc"]
  EXFILES --> EXSTATE["export coefficient hydrographs"]
  EXOB --> EXSTATE

  DRCON["delratio.con"] -->|"hyd_read_connect.f90"| DROB["ob(i)<br/>ob(i)%props"]
  DRDB["delratio.del"] -->|"dr_db_read.f90"| DRFILES["delivery-ratio hydrograph files"]
  DRFILES --> DRSTATE["dr(:)<br/>delivery-ratio multipliers"]
  DROB -->|"command.f90 applies dr(ob%props)"| DRSTATE

  OUTCON["outlet.con"] -->|"hyd_read_connect.f90"| OUTOB["ob(i)<br/>outlet shell"]
  OUTOB -->|"command.f90"| OUTSTATE["outlet hydrograph = incoming hydrograph"]
```

## GWFLOW

```mermaid
flowchart LR
  GWCON["gwflow.con<br/>active GWFLOW shell"] -->|"hyd_read_connect.f90"| GWOB["ob(i)<br/>gwflow object"]
  CHCELL["chancell.gw<br/>channel-cell connections"] -->|"gwflow_chan_read.f90"| CHLINK["gw_chan_* arrays"]
  GWIN["gwflow input set<br/>gwflow.codes, cells, zones,<br/>cell properties, solutes,<br/>boundary and output files"] -->|"gwflow_read.f90"| GWSTATE["gw_state(:)<br/>groundwater grid state"]
  HRUCELL["hrucell.gw or lsucell.gw<br/>object-cell overlaps"] -->|"gwflow_read.f90"| OBLINK["SWAT+ object to grid-cell fractions"]
  OPTIONAL["optional GWFLOW files<br/>gwflow_canal.con, hru_pump.gw,<br/>pumpex.gw, ponds, transit/output files"] -->|"gwflow_read.f90"| GWSTATE
  GWOB --> GWSTATE
  CHLINK --> GWSTATE
  OBLINK --> GWSTATE
```

GWFLOW is more like a grid subsystem attached to SWAT+ objects than a simple
single-row property database.

## Canal, Pump, Aquifer2D, Herd, Water Rights

These fields appear in `object.cnt`, but they are not equivalent to the normal
`*.con -> hyd_read_connect -> ob()%props -> property database` pattern.

```mermaid
flowchart LR
  CNT["object.cnt fields<br/>canal, pump, aqu2d, herd, wro"] --> HC["hyd_connect.f90"]
  HC --> RANGE["canal and pump get sp_ob1 ranges<br/>aqu2d range is commented out<br/>herd and wro are not normal connect objects"]
  WCAN["water_canal.wal"] -->|"water_canal_read.f90"| CANAL["canal(:)<br/>water-allocation canal data"]
  GWCA["gwflow_canal.con<br/>plus GWFLOW canal files"] -->|"gwflow_read.f90"| GWCAN["GWFLOW canal-cell exchange"]
  HPUMP["hru_pump.gw"] -->|"gwflow_read / gwflow_simulate"| HRUPUMP["HRU groundwater pumping"]
  PUMPX["pumpex.gw"] -->|"gwflow_read / gwflow_pump_ext"| PUMPEX["external pumping"]
  AQ2D["aquifer2d.con"] -->|"aqu2d_read / aqu2d_init"| AQLINK["stream-aquifer interaction support"]
```

## Source Routine Anchors

- [[object.cnt]] is read by [[basin_read_objs.f90]].
- [[hyd_connect.f90]] assigns object ranges and calls [[hyd_read_connect.f90]].
- [[command.f90]] executes routed objects during simulation.
- [[proc_cha.f90]], [[proc_aqu.f90]], and [[proc_res.f90]] initialize channel,
  aquifer, and reservoir data.
- [[ru_read.f90]] and [[ru_read_elements.f90]] initialize routing units.
- [[gwflow_read.f90]] initializes GWFLOW grid inputs.

## Related

- [[01-input-file-system]] - general input-file rules.
- [[02-hru-input-chain]] - HRU-specific input chain.
- [[04-management-schedule-and-operations]] - management schedules and operations.
