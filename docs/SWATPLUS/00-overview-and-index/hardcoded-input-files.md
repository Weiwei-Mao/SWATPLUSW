---
type: overview
tags:
  - swat/overview
  - swat/input
title: Hardcoded SWAT+ Input Files
purpose: "Curated index of input files opened by literal or default names instead of file.cio fields."
status: partial
source_revision: "grep over SWATPLUS/swatplus/src file= literals; cross-checked with input-file-architecture"
scenario: "general"
---

# Hardcoded SWAT+ Input Files

This page tracks files whose names are fixed in source code or default module state, rather than renamed through `file.cio`.

Use this as a debugging map when a file appears to be missing even though `file.cio` looks correct. For the mechanism and role taxonomy, see [[input-file-architecture]].

## Meaning

| Class | How to recognize it | Rename rule |
|---|---|---|
| `file.cio` registered | reader opens `in_<category>%<field>` | edit [[file.cio]] |
| hardcoded literal | reader opens `'name'` or `"name"` | edit source or keep the expected filename |
| module default | reader opens a module variable with a default literal not populated by `file.cio` | change the module default or provide the default file |
| derived companion | reader derives a second filename from a `file.cio` file | rename using the same derivation rule |

## Core Scattered Files

| File | Reader | Call area | Notes |
|---|---|---|---|
| [[file.cio]] | [[readcio_read.f90]] | [[proc_bsn.f90]] | master control file; intentionally hardcoded as the root input |
| [[co2_yr.dat]] | [[co2_read.f90]] | [[proc_bsn.f90]] | atmospheric CO2 input, optional if present |
| [[carbon_layers.prt]] | [[carbon_layers_read.f90]] | [[proc_bsn.f90]] | carbon output-layer print controls |
| [[carbon_lyr.bsn]] | [[carbon_bsn_read.f90]] | [[proc_bsn.f90]] | derived companion to [[carbon.bsn]], not a direct `file.cio` entry |
| [[pest_metabolite.pes]] | [[pest_metabolite_read.f90]] | [[proc_read.f90]] | pesticide metabolite definitions |
| [[manure_om.frt]] | [[manure_orgmin_read.f90]] | [[proc_db.f90]] | manure organic/mineral nutrient definitions |
| [[manure_db.frt]] | [[manure_db_read.f90]] | [[proc_db.f90]] | extended manure database records |
| [[transplant.plt]] | [[plant_transplant_read.f90]] | [[proc_db.f90]] | plant transplanting data |
| [[puddle.ops]] | [[mgt_read_puddle.f90]] | [[proc_db.f90]] | puddling/paddy management operation data |
| [[satbuffer.str]] | [[sat_buff_read.f90]] | [[proc_db.f90]] | saturated-buffer structural connections |
| [[shade_factor.shf]] | [[shade_factor_read.f90]] | [[proc_read.f90]] | default module filename in `in_shf`, not listed in `file.cio` |

## Salt And Constituent Transport Files

These are the main `rtb salt` and `rtb cs` files opened by literal names. `constituents.cs` remains `file.cio`-registered and controls which constituents exist.

| File | Reader | Role |
|---|---|---|
| [[salt_hru.ini]] | [[salt_hru_read.f90]] | HRU salt initialization |
| [[salt_aqu.ini]] | [[salt_aqu_read.f90]] | aquifer salt initialization |
| [[salt_irrigation]] | [[salt_irr_read.f90]] | irrigation salt parameters |
| [[salt_plants]] | [[salt_plant_read.f90]] | plant salt parameters |
| [[salt_atmo.cli]] | [[cli_read_atmodep_salt.f90]] | atmospheric salt deposition |
| [[salt_road]] | [[salt_roadsalt_read.f90]] | road salt application |
| [[salt_uptake]] | [[salt_uptake_read.f90]] | salt uptake coefficients |
| [[salt_urban]] | [[salt_urban_read.f90]] | urban salt parameters |
| [[salt_fertilizer.frt]] | [[salt_fert_read.f90]] | fertilizer salt content |
| [[salt_channel.ini]] | [[salt_cha_read.f90]] | channel salt initialization |
| [[salt_res]] | [[res_read_saltdb.f90]] | reservoir salt inputs |
| [[cs_hru.ini]] | [[cs_hru_read.f90]] | HRU constituent initialization |
| [[cs_aqu.ini]] | [[cs_aqu_read.f90]] | aquifer constituent initialization |
| [[cs_atmo.cli]] | [[cli_read_atmodep_cs.f90]] | atmospheric constituent deposition |
| [[cs_irrigation]] | [[cs_irr_read.f90]] | irrigation constituent parameters |
| [[cs_plants_boron]] | [[cs_plant_read.f90]] | plant boron/constituent parameters |
| [[cs_uptake]] | [[cs_uptake_read.f90]] | constituent uptake coefficients |
| [[cs_reactions]] | [[cs_reactions_read.f90]] | reaction parameters |
| [[cs_urban]] | [[cs_urban_read.f90]] | urban constituent parameters |
| [[fertilizer.frt_cs]] | [[cs_fert_read.f90]] | fertilizer constituent content |
| [[cs_channel.ini]] | [[cs_cha_read.f90]] | channel constituent initialization |
| [[cs_streamobs]] | [[cs_cha_read.f90]] | channel constituent observation setup |
| [[cs_res]] | [[res_read_csdb.f90]] | reservoir constituent inputs |

## Recall And Time Series Companion Files

| File | Reader | Notes |
|---|---|---|
| [[recall_db.rec]] | [[recall_read.f90]] | hardcoded root recall database opened by `recalldb_read` |
| [[pest.com]] | [[recall_read.f90]] | hardcoded pesticide recall companion |
| [[cs_recall.rec]] | [[recall_read_cs.f90]] | hardcoded constituent recall control |
| [[salt_recall.rec]] | [[recall_read_salt.f90]] | hardcoded salt recall control |

The individual time-series filenames inside recall records are data values read from these control files, not standalone files that should be generated as notes automatically.

## Water Allocation Files

| File | Reader | Notes |
|---|---|---|
| [[outside_rcv.wal]] | [[water_orcv_read.f90]] | outside receiving objects |
| [[outside_src.wal]] / [[out_src.wal]] | [[water_osrc_read.f90]] | source code inquires `outside_src.wal` but opens `out_src.wal`; verify before changing |
| [[water_treat.wal]] | [[water_treatment_read.f90]] | treatment definitions |
| [[water_use.wal]] | [[water_use_read.f90]] | water use definitions |
| [[water_tower.wal]] | [[water_tower_read.f90]] | tower definitions |
| [[water_pipe.wal]] | [[water_pipe_read.f90]] | pipe definitions |
| [[water_canal.wal]] | [[water_canal_read.f90]] | canal definitions |
| [[om_treat.wal]] | [[om_treat_read.f90]] | organic/mineral treatment definitions |
| [[om_use.wal]] | [[om_use_read.f90]] | organic/mineral use definitions |
| [[om_osrc.wal]] | [[om_osrc_read.f90]] | organic/mineral outside source definitions |

## Groundwater And Optional Subsystems

The `gwflow` subsystem has many literal filenames (`codes.gw`, `cells.gw`, `zones.gw`, `cellcon.gw`, `outputs.gw`, `hrucell.gw`, `lsucell.gw`, `chancell.gw`, `chan_depth.gw`, and related files). Treat these as a subsystem-specific input set; do not expect `file.cio` renames to affect them.

Other optional literal inputs include calibration/update helpers such as [[scen_dtl.upd]], channel/reservoir constituent helpers such as [[initial.cha_cs]] and [[reservoir.res_cs]], and legacy/specialized files such as [[sed_nut.cha]] and [[soil_lyr_depths.sol]].

## Maintenance

When a new reader is studied, classify its file-opening mechanism:

1. `in_<category>%<field>`: update [[file.cio]] and the relevant input-file note.
2. Literal string: add it here and mark the source routine note.
3. Derived filename: document the derivation rule and the controlling input.
4. Data-driven child filename: keep it in the parent file's structure; do not create a fake note from the runtime expression.
