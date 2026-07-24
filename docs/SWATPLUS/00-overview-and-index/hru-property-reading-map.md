---
type: guide
tags:
  - swat/hru
  - swat/input
  - swat/source
title: HRU property reading diagram
---

# HRU Property Reading Diagram

## Full HRU Property Flow

```mermaid
flowchart LR
  HCON["hru.con<br/>active HRU object<br/>area, lat/lon, elev, wst, routing<br/>hru column = props"] -->|"hyd_read_connect.f90"| OB["ob(i)<br/>active object record<br/>ob(i)%props"]
  OB -->|"props selects row"| HRUDATA["hru-data.hru<br/>hru_db(props)<br/>topo, hyd, soil, lu_mgt,<br/>soil_plant_init, surf_stor,<br/>snow, field"]
  HRUDATA -->|"hru_read.f90<br/>text names -> db indexes"| HRUDB["hru_db(:)<br/>dbsc = original names<br/>dbs = integer pointers"]
  HRUDB -->|"hrudb_init.f90<br/>copy selected row"| HRU["hru(ihru)<br/>active runtime HRU<br/>area comes from hru.con"]

  HRUDATA -->|"topo"| TOPO["topography.hyd"]
  HRUDATA -->|"hyd"| HYD["hydrology.hyd"]
  HRUDATA -->|"field"| FIELD["field.fld"]
  HRUDATA -->|"snow"| SNOW["snow.sno"]
  TOPO --> TOPOHYD["topohyd_init.f90"]
  HYD --> TOPOHYD
  FIELD --> TOPOHYD
  SNOW --> TOPOHYD
  TOPOHYD -->|"topo, hyd, field, snow state"| HRU

  HRUDATA -->|"soil"| SOILDB["soils.sol"]
  SOILDB -->|"soil_db_read.f90<br/>then soils_init.f90"| SOILSTATE["soil(ihru)<br/>soil layers and physical properties<br/>soil1 arrays allocated"]
  SOILSTATE --> HRU

  HRUDATA -->|"soil_plant_init"| SPI["soil_plant.ini"]
  SPI -->|"selects nutrient init name"| NUTSOL["nutrients.sol"]
  NUTSOL -->|"soil_nutcarb_init.f90"| SOIL1["soil1(ihru)<br/>NO3, mineral P,<br/>organic C/N/P pools"]
  SOIL1 --> HRU

  HRUDATA -->|"lu_mgt"| LUM["landuse.lum"]
  LUM -->|"plnt_com"| PCOM["plant.ini<br/>plant community"]
  PCOM -->|"readpcom.f90<br/>links crop names"| PLANTS["plants.plt<br/>crop/species parameters"]
  PCOM -->|"plant_all_init.f90<br/>plant_init.f90"| PLSTATE["pcom(ihru), pl_mass(ihru)<br/>plants, residue, LAI, biomass,<br/>root fractions, heat units"]
  PLANTS --> PLSTATE
  PLSTATE --> HRU

  LUM -->|"mgt"| MGT["management.sch<br/>operation schedule"]
  MGT -->|"mgt_read_mgtops.f90<br/>read_mgtops.f90"| SCHED["sched(:)<br/>operation rows and db indexes"]
  SCHED -->|"mgt_operatn.f90<br/>mgt_sched.f90 during run"| MGTRUN["management actions<br/>till, plant, fert, irrigate,<br/>harvest, graze, burn, skip"]
  MGTRUN --> HRU

  LUM -->|"cn2, cons_prac, ov_mann"| LUMDB["cntable.lum<br/>cons_practice.lum<br/>ovn_table.lum"]
  LUMDB -->|"cn2_init_all.f90<br/>plant_init.f90"| HRU

  LUM -->|"tile, septic, vfs,<br/>grww, bmp"| STRUCTDB["tiledrain.str<br/>septic.str / septic.sep<br/>filterstrip.str<br/>grassedww.str<br/>bmpuser.str"]
  STRUCTDB -->|"structure_init.f90<br/>structure_set_parms.f90"| HRU

  HRUDATA -->|"surf_stor when not null"| WETDB["wetland.wet"]
  WETDB -->|"wet_initial.f90"| WETSTATE["wet(ihr), wet_ob(ihr)<br/>surface storage / wetland / paddy state"]
  WETSTATE --> HRU
```

## Ames Sub1 Example

```mermaid
flowchart LR
  A["hru.con row 1<br/>hru0001<br/>area = 1.005 ha<br/>hru(props) = 1<br/>wst = wgn_01"] --> B["hru-data.hru row 1<br/>topo = topohru0001<br/>hyd = hyd0001<br/>soil = soil_01-h1<br/>lu_mgt = cosy_lum<br/>soil_plant_init = soilplant1<br/>surf_stor = null<br/>snow = snow001<br/>field = null"]

  B -->|"topo"| C["topography.hyd<br/>topohru0001"]
  B -->|"hyd"| D["hydrology.hyd<br/>hyd0001"]
  B -->|"soil"| E["soils.sol<br/>soil_01-h1"]
  B -->|"soil_plant_init"| F["soil_plant.ini<br/>soilplant1"]
  B -->|"snow"| G["snow.sno<br/>snow001"]
  B -->|"lu_mgt"| H["landuse.lum<br/>cosy_lum"]

  H --> I["plant community<br/>cosy_comm"]
  H --> J["management schedule<br/>mgt_01"]
  H --> K["curve number<br/>rc_strow_g"]
  H --> L["conservation practice<br/>up_down_slope"]
  H --> M["overland n<br/>convtill_nores"]

  J --> N["management.sch rows<br/>till, plnt, irrm,<br/>fert, hvkl, skip"]
```

## How To Read The Diagram

- `hru.con` chooses the active object and its area, elevation, weather station,
  routing, and `props` pointer.
- `props` selects one row in `hru-data.hru`.
- `hru-data.hru` is mostly a bundle of names pointing to other input files.
- `lu_mgt` expands into plant community, management schedule, curve number,
  conservation practice, urban settings, and structural practices.
- Soil physical layers come from `soils.sol`; initial nutrient/carbon pools are
  initialized later through `soil_plant.ini` and `nutrients.sol`.

