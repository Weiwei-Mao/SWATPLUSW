---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/read
file: proc_read.f90
note_file: proc_read.f90
subroutine: proc_read
module: []
calls:
  - ch_read_temp
  - cli_read_atmodep
  - cli_staread
  - constit_db_read
  - pest_metabolite_read
  - soil_plant_init
  - solt_db_read
  - pest_hru_aqu_read
  - path_hru_aqu_read
  - hmet_hru_aqu_read
  - salt_hru_read
  - salt_aqu_read
  - salt_irr_read
  - salt_plant_read
  - cli_read_atmodep_salt
  - salt_roadsalt_read
  - salt_uptake_read
  - salt_urban_read
  - salt_fert_read
  - cs_hru_read
  - cs_aqu_read
  - cli_read_atmodep_cs
  - cs_irr_read
  - cs_plant_read
  - cs_uptake_read
  - cs_reactions_read
  - cs_urban_read
  - cs_fert_read
  - topo_read
  - field_read
  - hydrol_read
  - shade_factor_read
  - snowdb_read
  - soil_db_read
  - soil_lte_db_read
uses_variables: []
input_variables: []
reads: []
writes: []
purpose: ""
---

# proc_read

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `proc_read.f90`
- **Modules used**:
  - -
- **Subroutine calls**: 35 | **Files read**: 0 | **Files written**: 0

## Call Relationships
**This routine calls:**

- [[ch_read_temp.f90]]
- [[cli_read_atmodep.f90]]
- [[cli_staread.f90]]
- [[constit_db_read.f90]]
- [[pest_metabolite_read.f90]]
- [[soil_plant_init.f90]]
- [[solt_db_read.f90]]
- [[pest_hru_aqu_read.f90]]
- [[path_hru_aqu_read.f90]]
- [[hmet_hru_aqu_read.f90]]
- [[salt_hru_read.f90]]
- [[salt_aqu_read.f90]]
- [[salt_irr_read.f90]]
- [[salt_plant_read.f90]]
- [[cli_read_atmodep_salt.f90]]
- [[salt_roadsalt_read.f90]]
- [[salt_uptake_read.f90]]
- [[salt_urban_read.f90]]
- [[salt_fert_read.f90]]
- [[cs_hru_read.f90]]
- [[cs_aqu_read.f90]]
- [[cli_read_atmodep_cs.f90]]
- [[cs_irr_read.f90]]
- [[cs_plant_read.f90]]
- [[cs_uptake_read.f90]]
- [[cs_reactions_read.f90]]
- [[cs_urban_read.f90]]
- [[cs_fert_read.f90]]
- [[topo_read.f90]]
- [[field_read.f90]]
- [[hydrol_read.f90]]
- [[shade_factor_read.f90]]
- [[snowdb_read.f90]]
- [[soil_db_read.f90]]
- [[soil_lte_db_read.f90]]

**Called by:**

- [[main.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
(No module-level variable references detected.)

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.

- Line 18: call [[ch_read_temp.f90]], read channel temperature parameter/input file: [[temperature.cha]]
- Line 19: call [[cli_read_atmodep.f90]], read atmospheric deposition input for nutrients/standard constituents: [[atmodep.cli]]
- Line 20: call [[cli_staread.f90]], read weather station definitions: [[weather-sta.cli]]
- Line 22: call [[constit_db_read.f90]], read constituent database: [[constituents.cs]]
- Line 23: call [[pest_metabolite_read.f90]], read [[pest_metabolite.pes]], hardcoded filename (not in [[file.cio]])
- Line 24: call [[soil_plant_init.f90]], read [[input_file_module.f90#in_init]] %soil_plant_ini
- Line 25: call [[solt_db_read.f90]], read [[nutrients.sol]]
- Line 26: call [[pest_hru_aqu_read.f90]], read [[input_file_module.f90#in_init]] %pest_soil
- Line 27: call [[path_hru_aqu_read.f90]], read  [[input_file_module.f90#in_init]] %path_soil
- Line 28: call [[hmet_hru_aqu_read.f90]], read  [[input_file_module.f90#in_init]] %hmet_soil
- Line 31: call [[salt_hru_read.f90]], read [[salt_hru.ini]], out of [[file.cio]]
- Line 32: call [[salt_aqu_read.f90]], read [[salt_aqu.ini]], out of [[file.cio]]
- Line 33: call [[salt_irr_read.f90]], read [[salt_irrigation]], out of [[file.cio]]
- Line 34: call [[salt_plant_read.f90]], read [[salt_plants]], out of [[file.cio]]
- Line 35: [[cli_read_atmodep_salt.f90]] → [[salt_atmo.cli]]. Salt version of line 19: line 19 reads nutrient atmospheric deposition (atmodep.cli), this one reads salt-ion deposition.
- Line 36: call [[salt_roadsalt_read.f90]], read [[salt_road]], out of [[file.cio]]
- Line 37: call [[salt_uptake_read.f90]], read [[salt_uptake]], out of [[file.cio]]
- Line 38: call [[salt_urban_read.f90]], read [[salt_urban]], out of [[file.cio]]
- Line 39: call [[salt_fert_read.f90]], read [[salt_fertilizer.frt]], out of [[file.cio]]
- Line 42: call [[cs_hru_read.f90]], read [[cs_hru.ini]], out of [[file.cio]]
- Line 43: call [[cs_aqu_read.f90]], read [[cs_aqu.ini]], out of [[file.cio]]
- Line 44: call [[cli_read_atmodep_cs.f90]], read [[cs_atmo.cli]], out of [[file.cio]]
- Line 45: call [[cs_irr_read.f90]], read [[cs_irrigation]], out of [[file.cio]]
- Line 46: call [[cs_plant_read.f90]], read [[cs_plants_boron]] (underscore, not hyphen), hardcoded filename (not in [[file.cio]])
- Line 47: call [[cs_uptake_read.f90]], read [[cs_uptake]], out of [[file.cio]]
- Line 48: call [[cs_reactions_read.f90]], read [[cs_reactions]], out of [[file.cio]]
- Line 49: call [[cs_urban_read.f90]], read [[cs_urban]], out of [[file.cio]]
- Line 50: call [[cs_fert_read.f90]], read [[fertilizer.frt_cs]], out of [[file.cio]]
- Line 52: call [[topo_read.f90]], read [[input_file_module.f90#in_hyd]], %topogr_hyd
- Line 53: call [[field_read.f90]], read [[input_file_module.f90#in_hyd]] %field_fld
- Line 54: call [[hydrol_read.f90]], read [[input_file_module.f90#in_hyd]] %hydrol_hyd (hydrology.hyd)
- Line 56: [[shade_factor_read.f90]] reads `in_shf%ssff_shf` — but this is **dead code**. Nothing ever puts a filename in `in_shf` (not in file.cio, not set by any routine), so the reader always thinks the file is missing and skips. Shade factors never load; looks unfinished/optional.
- Line 58: call [[snowdb_read.f90]], read [[input_file_module.f90#in_parmdb]] %snow
- Line 59: call [[soil_db_read.f90]], read [[input_file_module.f90#in_sol]] %soils_sol
- Line 60: call [[soil_lte_db_read.f90]], read [[input_file_module.f90#in_sol]] %lte_sol
- End
- How files are opened here: names listed in file.cio are looked up via the in_* vars (e.g. soil_plant.ini, nutrients.sol, temperature.cha); the salt_/cs_ names are hardwired in the reader itself (e.g. salt_hru.ini). Full picture: [[input-file-architecture]].
- (Fixed 2026-07-16) Generator used to skip input files with no extension (like salt_plants) — patched, notes now exist.
<!-- USER-NOTES-END -->
