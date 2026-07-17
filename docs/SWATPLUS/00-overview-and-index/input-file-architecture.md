---
type: overview
tags:
  - swat/overview
  - swat/input
title: SWAT+ Input File Architecture
purpose: "How SWAT+ locates and classifies input files: file.cio registration vs hardcoded, and database vs scenario vs operations roles"
status: verified
source_revision: "readcio_read.f90, salt_hru_read.f90, soil_plant_init.f90, constit_db_read.f90 + grep over src"
scenario: "general (Osu_1hru)"
---

# SWAT+ Input File Architecture

> Answers two questions that come up constantly while reading the input-reading layer:
> 1. **How does a reader find its file?** — registered in `file.cio` vs hardcoded in source.
> 2. **What role does the file play?** — shared database vs per-object scenario data vs operations/structural library.
>
> `status: verified` against source. See evidence links in each section.

## 1. Two mechanisms for opening an input file

Every reader subroutine opens its file with an `inquire (file=...)`. The second argument is either a **module variable** (file.cio-registered) or a **string literal** (hardcoded).

### (A) Registered via `file.cio` — the legacy SWAT+ pattern

`file.cio` is the master control file, read once by [[readcio_read.f90]] (unit 107). It is ~25 lines; each line holds one category of filenames. `readcio_read` parses each line straight into a derived-type module variable in [[input_file_module.f90]]: `in_sim`, `in_basin`, `in_cli`, `in_con`, `in_cha`, `in_res`, `in_ru`, `in_hru`, `in_exco`, `in_rec`, `in_delr`, `in_aqu`, `in_herd`, `in_watrts`, `in_link`, `in_hyd`, `in_str`, `in_parmdb`, `in_ops`, `in_lum`, `in_chg`, `in_init`, `in_sol`, `in_cond`, `in_regs`, plus weather paths and the output path. See the full field map in [[file.cio]].

A legacy reader then does:

```fortran
inquire (file=in_<cat>%<field>, exist=i_exist)   ! e.g. in_parmdb%plants_plt
```

So the **filename is whatever the user typed in `file.cio`**; renaming a file means editing `file.cio`, not source. Examples (verified by grep):

| Reader | file.cio field | File |
|---|---|---|
| [[plant_parm_read.f90]] | `in_parmdb%plants_plt` | plants.plt |
| [[fert_parm_read.f90]] | `in_parmdb%fert_frt` | fertilizer.frt |
| [[soil_plant_init.f90]] | `in_init%soil_plant_ini` | soil_plant.ini |
| [[solt_db_read.f90]] | `in_sol%nut_sol` | nutrients.sol |
| [[soil_db_read.f90]] | `in_sol%soils_sol` | soils.sol |
| [[constit_db_read.f90]] | `in_sim%cs_db` | constituents.cs |
| [[cli_read_atmodep.f90]] | `in_cli%atmo_cli` | atmodep.cli |
| [[cli_staread.f90]] | `in_cli%weat_sta` | weather-sta.cli |
| [[ch_read_temp.f90]] | `in_cha%temp` | temperature.cha |
| [[hydrol_read.f90]] / [[topo_read.f90]] / [[field_read.f90]] | `in_hyd%*` | hydrology.hyd / topography.hyd / field_fld |
| [[exco_read_salt.f90]] / [[dr_read_salt.f90]] | `in_exco%salt` / `in_delr%salt` | exco_salt.exc / dr_salt.del |

### (B) Hardcoded filename — newer modules, not file.cio-controlled

Some readers ignore `file.cio` and open a fixed name:

```fortran
inquire (file='salt_hru.ini', exist=i_exist)     ! literal, not in_<cat>%<field>
```

To rename one of these you must edit source. Two groups do this:

- **The `rtb salt` / `rtb cs` modules** (Ryan Bailey). Every one of their data files is hardcoded — see §3.
- **A scattered set of other readers**: [[pest_metabolite_read.f90]] (pest_metabolite.pes), [[manure_orgmin_read.f90]]/[[manure_db_read.f90]] (manure_om.frt / manure_db.frt), [[mgt_read_puddle.f90]] (puddle.ops), [[plant_transplant_read.f90]] (transplant.plt), [[co2_read.f90]] (co2_yr.dat), [[carbon_layers_read.f90]] (carbon_layers.prt), [[sat_buff_read.f90]] (satbuffer.str), the `water_*.wal` rights files, `recall_db.rec`.

## 2. The salt/cs question: "are salt inputs in file.cio?"

**Short answer: the salt/cs *data* files are NOT file.cio-controlled; they are all hardcoded.** With two nuances:

1. **`constituents.cs` IS in file.cio** (`in_sim%cs_db`, read by [[constit_db_read.f90]]). It is the *master list* of which constituents are active — it declares the names of the pesticide/pathogen/metal/**salt-ion**/cs species to simulate and sets `cs_db%num_salts` etc. So file.cio decides *which* salt ions exist; the salt-module files decide *their values*.
2. **file.cio reserves placeholder slots** `in_init%salt_soil` / `salt_water` (see [[file.cio]] lines "in_init"), but the rtb salt readers **ignore them** and hardcode the filenames. Verified: [[salt_hru_read.f90]] opens literal `'salt_hru.ini'`; [[salt_aqu_read.f90]] opens literal `"salt_aqu.ini"`. So although the slot exists, salt input filenames are effectively fixed.
3. **The salt *routing transfer* files ARE file.ciro-controlled**: `exco_salt.exc` (`in_exco%salt`) and `dr_salt.del` (`in_delr%salt`). These belong to the legacy exco/delratio routing layer, not the rtb salt module.

So "salt inputs are out of file.cio" is correct for the rtb salt/cs *module data*, but not for the constituent master list or the routing transfer files.

## 3. Complete salt/cs reader → file table (all hardcoded)

Every file below is opened by a string literal (mechanism B), so none are renamed via `file.cio`.

### `rtb salt` (called from [[proc_read.f90]] and [[main.f90]])

| Reader | File | Role (see §4) |
|---|---|---|
| [[salt_hru_read.f90]] | `salt_hru.ini` | scenario init (soil+plant salt per named profile) |
| [[salt_aqu_read.f90]] | `salt_aqu.ini` | scenario init (aquifer salt) |
| [[salt_irr_read.f90]] | `salt_irrigation` | params (salt in irrigation sources) |
| [[salt_plant_read.f90]] | `salt_plants` | database (plant salt tolerance/uptake) |
| [[cli_read_atmodep_salt.f90]] | `salt_atmo.cli` | time-series (atm. deposition per station) |
| [[salt_roadsalt_read.f90]] | `salt_road` | scenario input (road-deicing application) |
| [[salt_uptake_read.f90]] | `salt_uptake` | params (uptake coefficients) |
| [[salt_urban_read.f90]] | `salt_urban` | scenario input (urban salt) |
| [[salt_fert_read.f90]] | `salt_fertilizer.frt` | database (salt content per fertilizer type) |
| [[salt_cha_read.f90]] | `salt_channel.ini` | scenario init (channel salt) |

### `rtb cs` (constituent transport; same call sites)

| Reader | File | Role |
|---|---|---|
| [[cs_hru_read.f90]] | `cs_hru.ini` | scenario init |
| [[cs_aqu_read.f90]] | `cs_aqu.ini` | scenario init |
| [[cli_read_atmodep_cs.f90]] | `cs_atmo.cli` | time-series |
| [[cs_irr_read.f90]] | `cs_irrigation` | params |
| [[cs_plant_read.f90]] | `cs_plants_boron` | database (note: underscore, not hyphen) |
| [[cs_uptake_read.f90]] | `cs_uptake` | params |
| [[cs_reactions_read.f90]] | `cs_reactions` | database (reaction parameters) |
| [[cs_urban_read.f90]] | `cs_urban` | scenario input |
| [[cs_fert_read.f90]] | `fertilizer.frt_cs` | database |
| [[cs_cha_read.f90]] | `cs_channel.ini` / `cs_streamobs` | scenario init / observations |

## 4. Three semantic roles (orthogonal to the file.cio question)

A file's **role** is about its content and how it is consumed, not about mechanism A/B:

- **Database (DB)** — shared parameter *definitions*, referenced by name or ID, not tied to one spatial object. Read once into a `*db(:)` array with a count in `db_mx%*`. Examples: `plants.plt`, `fertilizer.frt`, `tillage.til`, `pesticide.pes`, `urban.urb`, `nutrients.sol`, `constituents.cs`, `salt_plants`, `cs_plants_boron`, `cs_reactions`, `salt_fertilizer.frt`.
- **Scenario / object initialization** — actual values *assigned to specific spatial objects* (HRU, aquifer, channel), usually via named records that an object's definition points to. Examples: `soil_plant.ini`, `salt_hru.ini`, `pest_hru.ini`, `hydrology.hyd` / `topography.hyd`, `hru-data.hru`.
- **Operations / structural / management library** — schedules and structural BMP definitions referenced by name from a landuse/management record. Examples: `management.sch`, `*.ops`, `*.str`, `landuse.lum`, `*.dtl`. (See the [[proc_db.f90]] notes for the `landuse.lum → management.sch → lum.dtl` chain.)

A fourth minor kind: **time-series / climate forcing** — station-indexed time series (`pcp.cli`, `atmodep.cli`, `salt_atmo.cli`).

## 5. subroutine vs input file vs database vs assignment

The four terms the question conflates, separated:

| Term | What it is | Where its note lives | Example |
|---|---|---|---|
| **subroutine** | the Fortran code that *reads* a file | `01-source-routines/X_read.f90.md` | [[salt_hru_read.f90]] |
| **input file** | the data file on disk | `03-input-files/X.md` | [[salt_hru.ini]] |
| **database** | a *role*: shared, by-ID parameter definitions (a kind of input file) | `03-input-files/` | plants.plt, nutrients.sol |
| **scenario assignment** | a *role*: per-object values (another kind of input file) | `03-input-files/` | salt_hru.ini, soil_plant.ini |

Naming convention (mostly holds): a subroutine `X_read` reads a file whose name starts with `X` (`salt_hru_read` → `salt_hru.ini`; `plant_parm_read` → `plants.plt`). The exception family is the `_parm_read` database readers, which read `in_parmdb%*` shared databases.

## How to tell, for any reader, which mechanism and role

1. Open the reader in `01-source-routines/` and find its `inquire (file=...)`.
2. `in_<cat>%<field>` → mechanism **A** (file.cio-controlled); look the field up in [[file.cio]]. A literal `'name'` → mechanism **B** (hardcoded).
3. For role: if it allocates a `*db(:)` array and stores a count in `db_mx%*`, it is a **database**; if it fills per-object initial state referenced from an object definition, it is **scenario init**; if it is `.ops`/`.str`/`.sch`/`.lum`/`.dtl`, it is **operations/structural**.

## Related

- [[file.cio]] — the field-by-field control-file map.
- [[readcio_read.f90]] — the parser that populates the `in_*` types.
- [[input_file_module.f90]] — the derived types holding the registered filenames.
- [[proc_read.f90]] / [[proc_db.f90]] / [[proc_bsn.f90]] — the top-level read orchestration.
