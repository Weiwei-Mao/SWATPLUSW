---
type: module
tags:
  - swat/module
  - swat/to-read
file: maximum_data_module.f90
note_file: maximum_data_module.f90
module_name: maximum_data_module
defines_types:
  - data_files_max_elements
defines_vars:
  - db_mx
defines_subroutines: []
defines_functions: []
defines_procedures: []
purpose: ""
---

# maximum_data_module

> [!info] Module
> Defines derived types and module-level variables.

## Defined Types
### data_files_max_elements

- **Defined in source**: `maximum_data_module.f90:7`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `topo` | `integer` | 8 | nubz |
| `hyd` | `integer` | 9 | nubz |
| `soil` | `integer` | 10 | none \|number of types of soils |
| `landuse` | `integer` | 11 | none \|number of landuse types |
| `mgt_ops` | `integer` | 12 | none \|number of records in management |
| `cn_lu` | `integer` | 13 | none \|number of records in cntable.lum |
| `cons_prac` | `integer` | 14 | none \|number of records in conservation practice table |
| `pothole` | `integer` | 15 | none \|number of potholes |
| `sdr` | `integer` | 16 | none \|number of types of susbsurface drain systems |
| `str_ops` | `integer` | 17 | none \|number of management ops |
| `urban` | `integer` | 18 | none \|number of urban land use types in urban.urb |
| `ovn` | `integer` | 19 | none \|number of overland flow n types in ovn_table.lum |
| `septic` | `integer` | 20 | none \|number of types of septic systems |
| `plantparm` | `integer` | 21 | none \|number of total plants in plants.plt |
| `fertparm` | `integer` | 22 | none \|number of total fertilizer in fertilizer.frt |
| `manureparm` | `integer` | 23 | none \|number of total manures in manure.frt |
| `tillparm` | `integer` | 24 | none \|number of total tillages in tillage.til |
| `pestparm` | `integer` | 25 | none !number of total pesticides in pesticide.pes |
| `pestcom` | `integer` | 26 | none !number of total pesticides communities in pesticide.com |
| `plantcom` | `integer` | 27 | none \|number of plant communities |
| `soiltest` | `integer` | 28 | none \|number of soiltest |
| `sno` | `integer` | 29 | none \|number of snow props |
| `field` | `integer` | 30 | none \|number of field props |
| `atmodep` | `integer` | 31 | none \|atmospheric deposition props |
| `chemapp_db` | `integer` | 32 | none \|chemical application (fert and pest) operations |
| `grazeop_db` | `integer` | 33 | none \|grazing operations |
| `harvop_db` | `integer` | 34 | none \|harvest only operations |
| `irrop_db` | `integer` | 35 | none \|irrigation operations |
| `sweepop_db` | `integer` | 36 | none \|sweep operations |
| `filtop_db` | `integer` | 37 | none \|filter strip data |
| `fireop_db` | `integer` | 38 | none \|fire data |
| `grassop_db` | `integer` | 39 | none \|grassed waterways data |
| `plparmop_db` | `integer` | 40 | none \|plant parms update data |
| `rsdmgtop_db` | `integer` | 41 | none \|residue management data |
| `bmpuserop_db` | `integer` | 42 | none \|user defined upland CP removal |
| `cond` | `integer` | 43 | none \|conditional data |
| `initop_db` | `integer` | 44 | none \|initial.str |
| `wgnsta` | `integer` | 45 | none \|max wgn stations included in weather-wgn.cli |
| `wst` | `integer` | 46 | none \|max weather stations include in weather-sta.cli |
| `pcpfiles` | `integer` | 47 | none \|max pcp files included in pcp.cli |
| `tmpfiles` | `integer` | 48 | none \|max tmp files included in tmp.cli |
| `rhfiles` | `integer` | 49 | none \|max relative humidity files included in hmd.cli |
| `slrfiles` | `integer` | 50 | none \|max solar radiation files included in slr.cli |
| `petfiles` | `integer` | 51 | none \|max pet files included in pet.cli |
| `wndfiles` | `integer` | 52 | none \|max wind files included in the wnd.cli |
| `cal_parms` | `integer` | 53 | none \|max number of calibration parameters in cal_parms_upd |
| `cal_upd` | `integer` | 54 | none \|max number of calibration parameter updates |
| `sched_up` | `integer` | 55 | none \|max number of scheduled updates (parameters, structures, land_use_mgt) |
| `cond_up` | `integer` | 56 | none \|max number of conditional updates (parameters, structures, land_use_mgt) |
| `d_tbl` | `integer` | 57 | none \|max number of decision tables |
| `dtbl_lum` | `integer` | 58 | none \|max number of decision tables |
| `dtbl_res` | `integer` | 59 | none \|max number of decision tables |
| `dtbl_flo` | `integer` | 60 | none \|max number of decision tables |
| `dtbl_scen` | `integer` | 61 | none \|max number of decision tables |
| `cs_db` | `integer` | 62 |  |
| `pathcom` | `integer` | 63 |  |
| `hmetcom` | `integer` | 64 |  |
| `saltcom` | `integer` | 65 |  |
| `ru_elem` | `integer` | 66 |  |
| `lsu_elem` | `integer` | 67 |  |
| `lsu_out` | `integer` | 68 | none \|max number of landscape regions for output |
| `reg_elem` | `integer` | 69 |  |
| `lsu_reg` | `integer` | 70 | none \|max number of landscape regions for soft cal and output by lum |
| `lscal_reg` | `integer` | 71 | none \|max number of soft data for landscape calibration (for each cal region) |
| `aqu_elem` | `integer` | 72 |  |
| `aqu_out` | `integer` | 73 | none \|max number of aquifer regions for output |
| `aqu_reg` | `integer` | 74 | none \|max number of aquifer regions for soft cal and output by aquifer type |
| `cha_out` | `integer` | 75 | none \|max number of channel regions for output |
| `cha_reg` | `integer` | 76 | none \|max number of channel regions for soft cal and output by channel order |
| `res_out` | `integer` | 77 | none \|max number of reservoir regions for output |
| `res_reg` | `integer` | 78 | none \|max number of reservoir regions for soft cal and output by reservoir type |
| `rec_out` | `integer` | 79 | none \|max number of recall regions for output |
| `rec_reg` | `integer` | 80 | none \|max number of recall regions for soft cal and output by recall type |
| `plcal_reg` | `integer` | 81 | none \|max number of regions for plant calibration |
| `ch_reg` | `integer` | 82 | none \|max number of regions for channel calibration |
| `lscal_prms` | `integer` | 83 | none \|max number of parameters for landscape hru calibration |
| `res_dat` | `integer` | 84 |  |
| `res_init` | `integer` | 85 |  |
| `res_hyd` | `integer` | 86 |  |
| `res_sed` | `integer` | 87 |  |
| `res_nut` | `integer` | 88 |  |
| `res_salt` | `integer` | 89 | rtb salt |
| `res_cs` | `integer` | 90 | rtb cs |
| `res_weir` | `integer` | 91 |  |
| `wet_dat` | `integer` | 92 |  |
| `wet_hyd` | `integer` | 93 |  |
| `ch_surf` | `integer` | 94 |  |
| `ch_dat` | `integer` | 95 |  |
| `ch_init` | `integer` | 96 |  |
| `ch_init_cs` | `integer` | 97 | rtb salt/cs |
| `ch_hyd` | `integer` | 98 |  |
| `ch_sed` | `integer` | 99 |  |
| `ch_nut` | `integer` | 100 |  |
| `ch_temp` | `integer` | 101 |  |
| `shf` | `integer` | 102 |  |
| `w_temp` | `integer` | 103 |  |
| `path` | `integer` | 104 |  |
| `exco` | `integer` | 105 |  |
| `exco_om` | `integer` | 106 |  |
| `exco_pest` | `integer` | 107 |  |
| `exco_path` | `integer` | 108 |  |
| `exco_hmet` | `integer` | 109 |  |
| `exco_salt` | `integer` | 110 |  |
| `dr` | `integer` | 111 |  |
| `dr_om` | `integer` | 112 |  |
| `trt_om` | `integer` | 113 |  |
| `dr_pest` | `integer` | 114 |  |
| `dr_path` | `integer` | 115 |  |
| `dr_hmet` | `integer` | 116 |  |
| `dr_salt` | `integer` | 117 |  |
| `sol_plt_ini` | `integer` | 118 |  |
| `pest_ini` | `integer` | 119 |  |
| `path_ini` | `integer` | 120 |  |
| `hmet_ini` | `integer` | 121 |  |
| `salt_ini` | `integer` | 122 | rtb salt |
| `salt_gw_ini` | `integer` | 123 | rtb salt |
| `cs_ini` | `integer` | 124 | rtb cs |
| `pestw_ini` | `integer` | 125 |  |
| `pathw_ini` | `integer` | 126 |  |
| `hmetw_ini` | `integer` | 127 |  |
| `salt_cha_ini` | `integer` | 128 | rtb salt |
| `cs_cha_ini` | `integer` | 129 | rtb cs |
| `sep` | `integer` | 130 |  |
| `ch_lte` | `integer` | 131 |  |
| `om_water_init` | `integer` | 132 |  |
| `sdc_dat` | `integer` | 133 |  |
| `aqudb` | `integer` | 134 |  |
| `aqu2d` | `integer` | 135 |  |
| `wallo_db` | `integer` | 136 |  |
| `mallo_db` | `integer` | 137 |  |
| `transplant` | `integer` | 138 |  |
| `pudl_db` | `integer` | 139 |  |
| `recalldb_max` | `integer` | 140 |  |
| `object_prt` | `integer` | 141 |  |
| `ctbl_res` | `integer` | 142 |  |
| `ch_sednut` | `integer` | 143 |  |
| `sat_buff` | `integer` | 144 |  |
| `canal` | `integer` | 145 |  |
| `pipe` | `integer` | 146 |  |
| `wtp` | `integer` | 147 |  |
| `treat` | `integer` | 148 |  |
| `uses` | `integer` | 149 |  |
| `stor` | `integer` | 150 |  |
| `om_treat` | `integer` | 151 |  |
| `om_use` | `integer` | 152 |  |
| `out_src` | `integer` | 153 |  |
| `out_rcv` | `integer` | 154 |  |
| `manure_om` | `integer` | 155 | none \|number of manure organic matter types in manure_om.frt |

## Variables Defined
### db_mx

- **Type**: `data_files_max_elements`
- **Defined in source**: `maximum_data_module.f90:157`

## Subroutines Defined
(No subroutines detected.)

## Functions Defined
(No functions detected.)

## Used By Source Routines

```dataview
LIST file.link
WHERE type = "source" AND contains(module, this.module_name)
```

<!-- USER-NOTES-START -->
## Notes
Use this section for type and variable meanings, units, and allowed values. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
