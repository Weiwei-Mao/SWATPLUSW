---
type: input
tags:
  - swat/input
  - swat/control-file
file: file.cio
ext: cio
read_by: [readcio_read.f90]
purpose: "Control file that declares SWAT+ input files and the output path"
---

> **How files get opened:** a filename declared here is stored by [[readcio_read.f90]] into an `in_*` field of [[input_file_module.f90]]; readers then do `inquire (file=in_<cat>%<field>)`. Files NOT in this list (every `rtb salt` / `rtb cs` data file, plus manure/transplant/puddle/co2/satbuffer/recall/water-rights files) are opened by **hardcoded literals** in source, so file.cio does not control them. Full mechanism + database/scenario/operations roles: [[input-file-architecture]].

### Line 1
 - title
### Line 2: in_sim
 - simulation
 - **time**: time.sim
 - **prt**: print.prt
 - **object_prt**: object.prt
 - **object_cnt**: object.cnt
 - **cs_db**: constituents.cs
 
### Line 3: in_basin
 - bsn
 - **codes_bas**: codes.bsn
 - **parms_bas**: parameters.bsn
 - **carboin_bsn**: carbon.bsn

### Line 4: in_cli
 - climate
 - **weat_sta**: weather-sta.cli
 - **weat_wgn**: weather-wgn.cli
 - **pet_cli**: pet.cli
 - **pcp_cli**: pcp.cli
 - **tmp_cli**: tmp.cli
 - **slr_cli**: slr.cli
 - **hmd_cli**: hmd.cli
 - **wnd_cli**: wnd.cli
 - **atmo_cli**: atmodep.cli

### Line 5: in_con
- connect
- **hru_con**: hru.con
- **hruez_con**: hru-lte.con
- **ru_con**: rout_unit.con
- **gwflow_con**: gwflow.con
- **aqu_con**: aquifer.con
- **aqu2d_con**: aquifer2d.con
- **chan_con**: channel.con
- **res_con**: reservoir.con
- **rec_con**: recall.con
- **exco_con**: exco.con
- **delr_con**: delratio.con
- **out_con**: outlet.con
- **chandeg_con**: chandeg.con

### Line 6: in_cha
- channel
- **init**: initial.cha
- **dat**: channel.cha
- **hyd**: hydrology.cha
- **sed**: sediment.cha
- **nut**: nutrient.cha
- **chan_ez**: channel_lte.cha
- **hyd_sed**: hyd_sed_lte.cha
- **temp**: temperature.cha

### Line 7: in_res
- reservoir
- **init_res**: initial.res
- **res**: reservoir.res
- **hyd_res**: hydrology.res
- **sed_res**: sediment.res
- **nut_res**: nutrient.res
- **weir_res**: weir.res
- **wet**: wetland.wet
- **hyd_wet**: hydrology.wet

### Line 8: in_ru
- routing_unit
- **ru_def**: rout_unit.def
- **ru_ele**: rout_unit.ele
- **ru**: rout_unit.rtu
- **ru_dr**: rout_unit.dr

### Line 9: in_hru
- hru
- **hru_data**: hru-data.hru
- **hru_ez**: hru-lte.hru

### Line 10: in_exco
- exco
- **exco**: exco.exc
- **om**: exco_om.exc
- **pest**: exco_pest.exc
- **path**: exco_path.exc
- **hmet**: exco_hmet.exc
- **salt**: exco_salt.exc

### Line 11: in_rec
- recall
- **recall_rec**: recall.exc

### Line 12: in_delr
- dr
- **del_ratio**: delratio.del
- **om**: dr_om.del
- **pest**: dr_pes.del
- **path**: dr_path.del
- **hmet**:: dr_hmet.del
- **salt**: dr_salt.del

### Line 13: in_aqu
- aquifer
- **init**: initial.aqu
- **aqu**: aquifer.aqu

### Line 14: in_herd
- herd
- **animal**: animal.hrd
- **herd**: herd.hrd
- **ranch**: ranch.hrd

### Line 15: in_watrts
- water_rights
- **transfer_wro**: water_allocation.wro
- **element**: element.wro
- **water_rights**: water_rights.wro

### Line 16: in_link
- link
- **chan_surf**: chan-surf.lin
- **aqu_cha**: aqu_cha.lin

### Line 17: in_hyd
- hydrology
- **hydrol_hyd**: hydrology.hyd
- **topogr_hyd**: topography.hyd
- **field_fld**: field_fld

### Line 18: in_str
- structural
- **tiledrain_str**: tiledrain.str
- **septic_str**: septic.str
- **fstrip_str**: filterstrip.str
- **grassww_str**: grassedww.str
- **bmpuser_str**: bmpuser.str

### Line 19: in_parmdb
- hru_parm_db
- **plants_plt**: plants.plt
- **fert_frt**: fertilizer.frt
- **till_til**: tillage.til
- **pest**: pesticide.pes
- **pathcom_db**: pathogens.pth
- **hmetcom_db**: metals.mtl
- **saltcom.db**: salt.slt
- **urban_urb**: urban.urb
- **septic_sep**: septic.sep
- **snow**: snow.sno

### Line 20: in_ops
- ops
- **harv_ops**: harv.ops
- **graze_ops**: graze.ops
- **irr_ops**: irr.ops
- **chem_ops**: chem_app.ops
- **fire_ops**: fire.ops
- **sweep_ops**: sweep.ops

### Line 21: in_lum
- lum
- **landuse_lim**: landuse_lum
- **management_sch**: management.sch
- **cntable_lum**: cntable.lum
- **cons_prac_lum**: cons_practice.lum
- **ovn_lum**: ovn_table.lum

### Line 22: in_chg
- chg
- **cal_parms**: cal_parms.cal
- **cal_upd**: calibration.cal
- **codes_sft**: codes.sft
- **wb_parms_sft**: wb_parms.sft
- **water_balance_sft**: water_balance.sft
- **ch_sed_budget_sft** = ch_sed_budget.sft
- **ch_sed_parms_sft**: ch_sed_parms.sft
- **plant_parms_sft**: plant_parms.sft
- **plant_gro_sft**: plant_gro.sft

### Line 23: in_init
- init
- **plant**: plant.ini
- **soil_plant_ini**: soil_plant.ini
- **om_water**: on_water.ini
- **pest_soil**: pest_hru.ini
- **pest_water**: pest_water.ini
- **path_soil**: path_hru.ini
- **path_water**: path_water.ini
- **hmet_soil**: hmet_hru.ini
- **hmet_water**: hmet_water.ini
- **salt_soil**: salt_hru.ini
- **salt_water**: salt_water.ini
- NOTE: these two salt slots are declared but **ignored** — [[salt_hru_read.f90]] / [[salt_aqu_read.f90]] hardcode `salt_hru.ini` / `salt_aqu.ini` and never dereference `in_init%salt_soil`. The `rtb salt`/`rtb cs` module bypasses file.cio entirely; see [[input-file-architecture]] §2.

### Line 24: in_sol
- soils
- **soils_sol**: soils.sol
- **nut_sol**: nutrients.sol
- **lte_sol**: soils_lte.sol

### Line 25: in_cond
- decision_table
- **dtbl_lum**: lum.dtl
- **dtbl_res**: res_rel.dtl
- **dtbl_scen**: scen_lu.dtl
- **dtbl_flo**: flo_con.dtl

### Line 26: in_regs
- regions
- **ele_lsu**: ls_unit.ele
- **def_lsu**: ls_unit.def
- **ele_reg**: ls_reg.ele
- **def_reg**: ls_reg.def
- **cal_lcu**: ls_cal.reg
- **ele_cha**: ch_catunit.ele
- **def_cha**: ch_catunit.def
- **def_cha_reg**: ch_reg.def
- **ele_aqu**: aqu_catunit.ele
- **def_aqu**: aqu_catunit.def
- **def_aqu_reg**: aqu_reg.def
- **ele_res**: res_catunit.ele
- **def_res**: res_catunit.def
- **def_res_reg**: res_reg.def
- **ele_psc**: rec_catunit.ele
- **def_psc**: rec_catunit.def
- **def_psc_reg**: rec_reg.def


### Line 27: in_path_pcp
### Line 28: in_path_tmp
### Line 29: in_path_slr
### Line 30: in_path_hmd
### Line 31: in_path_wnd


### Line 32: out_path_value






