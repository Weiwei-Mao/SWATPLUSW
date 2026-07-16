---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: proc_db.f90
note_file: proc_db.f90
subroutine: proc_db
module: []
calls:
  - plant_parm_read
  - plantparm_init
  - plant_transplant_read
  - till_parm_read
  - pest_parm_read
  - fert_parm_read
  - manure_orgmin_read
  - manure_db_read
  - urban_parm_read
  - path_parm_read
  - septic_parm_read
  - mgt_read_irrops
  - mgt_read_chemapp
  - mgt_read_harvops
  - mgt_read_grazeops
  - mgt_read_sweepops
  - mgt_read_fireops
  - mgt_read_mgtops
  - mgt_read_puddle
  - sdr_read
  - sep_read
  - scen_read_grwway
  - scen_read_filtstrip
  - scen_read_bmpuser
  - sat_buff_read
  - readpcom
  - cntbl_read
  - cons_prac_read
  - overland_n_read
  - landuse_read
uses_variables: []
input_variables: []
reads: []
writes: []
purpose: ""
---

# proc_db

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `proc_db.f90`
- **Modules used**:
  - -
- **Subroutine calls**: 30 | **Files read**: 0 | **Files written**: 0

## Call Relationships
**This routine calls:**

- [[plant_parm_read.f90]]
- [[plantparm_init.f90]]
- [[plant_transplant_read.f90]]
- [[till_parm_read.f90]]
- [[pest_parm_read.f90]]
- [[fert_parm_read.f90]]
- [[manure_orgmin_read.f90]]
- [[manure_db_read.f90]]
- [[urban_parm_read.f90]]
- [[path_parm_read.f90]]
- [[septic_parm_read.f90]]
- [[mgt_read_irrops.f90]]
- [[mgt_read_chemapp.f90]]
- [[mgt_read_harvops.f90]]
- [[mgt_read_grazeops.f90]]
- [[mgt_read_sweepops.f90]]
- [[mgt_read_fireops.f90]]
- [[mgt_read_mgtops.f90]]
- [[mgt_read_puddle.f90]]
- [[sdr_read.f90]]
- [[sep_read.f90]]
- [[scen_read_grwway.f90]]
- [[scen_read_filtstrip.f90]]
- [[scen_read_bmpuser.f90]]
- [[sat_buff_read.f90]]
- [[readpcom.f90]]
- [[cntbl_read.f90]]
- [[cons_prac_read.f90]]
- [[overland_n_read.f90]]
- [[landuse_read.f90]]

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

- Database used by all spatial modules
- Line 13: call [[plant_parm_read.f90]], read plant species/crop parameter database: [[plants.plt]]
- Line 14: call [[plantparm_init.f90]], initialize/derive plant parameters after [[plants.plt]] is read
- Line 15: call [[plant_transplant_read.f90]], read transplant-related plant data, used by transplant operations: [[plant_transplant_read.f90]]
- Line 16: call [[till_parm_read.f90]], read tillage operation parameter database: [[tillage.til]]
- Line 17: call [[pest_parm_read.f90]], read pesticide chemical parameter database: [[pesticide.pes]]
- Line 18: call [[fert_parm_read.f90]], read fertilizer/mineral nutrient database: [[fertilizer.frt]]
- Line 19: call [[manure_orgmin_read.f90]], read manure organic/mineral nutrient definitions: [[manure_om.frt]], this file is out of [[file.cio]]
- Line 20: call [[manure_db_read.f90]], read extended manure database, including pathogens/antibiotics, [[manure_db.frt]], also out of [[file.cio]]
- Line 21: call [[urban_parm_read.f90]], read urban parameters, [[urban.urb]]
- Line 22: call [[path_parm_read.f90]], read the pathogen data parameters, [[pathogens.pth]]
- Line 23: call [[septic_parm_read.f90]], read septic system parameter database: [[septic.sep]]
- Management scheduling and data files
- Line 26: call [[mgt_read_irrops.f90]], read irrigation operation definitions: [[irr.ops]]
- Line 27: call [[mgt_read_chemapp.f90]], read chemical/pesticide application operation definitions: [[chem_app.ops]]
- Line 28: call [[mgt_read_harvops.f90]], read harvest operation definitions: [[harv.ops]]
- Line 29: call [[mgt_read_grazeops.f90]], read grazing operation definitions: [[graze.ops]]
- Line 30: call [[mgt_read_sweepops.f90]], read street/urban sweeping operation definitions: [[sweep.ops]], an urban HRU operation that removes accumulated street/curb dirt before it can be washed off by runoff
- Line 31: call [[mgt_read_fireops.f90]], read fire/burn operation definitions: [[fire.ops]], a prescribed fire / burning management operation applied to vegetation, residue, and surface organic material
- Line 32: call [[mgt_read_mgtops.f90]], read management schedules: [[management.sch]], then operation sequences
	- HRU, uses a land use record from [[landuse.lum]], this file also have other records,
		- [[landuse.lum]] points to a management schedule name
			- [[management.sch]] defines that schedule
				- schedule may point to automatic decision tables in [[lum.dtl]]
- Line 33: call [[mgt_read_puddle.f90]], read puddling/paddy-related management operation data, [[puddle.ops]], out of [[file.cio]]
- Read structural operations files
- Line 36: call [[sdr_read.f90]], read tile drainage structural data: [[tiledrain.str]]
- Line 37: call [[sep_read.f90]], read septic structural data: [[septic.str]]
	- HRU, uses a land use record from [[landuse.lum]], this file also have other records,
		- [[landuse.lum]] points to a septic name
			- [[septic.str]] defines that septic type
				- Type corresponds the line number of [[septic.sep]] to get the exact parameters
- Line 38: call [[scen_read_grwway.f90]], read grassed waterway structural data: [[grassedww.str]], reads grassed-waterway definitions, which affect HRU surface runoff sediment, nutrients, and pesticides by routing flow through a grassed channel.
- Line 39: call [[scen_read_filtstrip.f90]], read filter strip structural data: [[filterstrip.str]], reads vegetative filter-strip definitions, which reduce sediment, nutrients, pesticides, and some runoff leaving the HRU.
- Line 40: call [[scen_read_bmpuser.f90]], read user-defined BMP structural data: [[bmpuser.str]], reads user-defined BMP removal efficiencies, which directly reduce selected HRU sediment, nitrogen, phosphorus, and bacteria loads by fixed fractions.
- Line 41: call [[sat_buff_read.f90]], read saturated buffer structural/BMP data: [[satbuffer.str]], reads saturated-buffer connections, which divert tile flow and nitrate from a source HRU into a receiving buffer HRU soil layer.
- Read plant community database
- Line 44: call [[readpcom.f90]], read plant community definitions used by landuse/management setup
- Line 46: call [[cntbl_read.f90]], read curve number table: [[cntable.lum]]
- Line 47: call [[cons_prac_read.f90]], read conservation practice table: [[cons_practice.lum]]
- Line 48: call [[overland_n_read.f90]], read overland Manning's n table: [[ovn_table.lum]]
- Line 49: call [[landuse_read.f90]], read landuse management definitions: [[landuse.lum]]
- End

<!-- USER-NOTES-END -->
