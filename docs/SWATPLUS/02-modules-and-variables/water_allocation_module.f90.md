---
type: module
tags:
  - swat/module
  - swat/to-read
file: water_allocation_module.f90
note_file: water_allocation_module.f90
module_name: water_allocation_module
defines_types:
  - transfer_source_objects
  - transfer_receiving_objects
  - outside_basin_objects
  - water_transfer_objects
  - source_output
  - water_allocation
  - water_treatment_use_data
  - outside_basin_source
  - outside_basin_receive
  - aquifer_loss
  - water_transfer_data
  - water_canal_data
  - transfer_object_output
  - water_allocation_output
  - wallo_header
  - wallo_header_units
defines_vars:
  - trans_m3
  - trn_m3
  - walloz
  - wallo
  - wal
  - wtp
  - wuse
  - osrc
  - orcv
  - wtow
  - pipe
  - canal
  - om_init_name
  - om_treat_name
  - om_use_name
  - om_osrc_name
  - wallod_out
  - wallom_out
  - walloy_out
  - walloa_out
  - wallo_hdr
  - wallo_hdr_units
defines_subroutines: []
defines_functions:
  - wallout_add
  - wallo_div_const
defines_procedures:
  - wallout_add
  - wallo_div_const
purpose: ""
---

# water_allocation_module

> [!info] Module
> Defines derived types and module-level variables.

## Defined Types
### transfer_source_objects

- **Defined in source**: `water_allocation_module.f90:9`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `typ` | `character (len=10)` | 10 | source object type |
| `num` | `integer` | 11 | number of the source object |
| `conv_typ` | `character (len=10)` | 12 | conveyance type - pipe or pump |
| `conv_num` | `integer` | 13 | number of the conveyance object |
| `dtbl_lim` | `character (len=25)` | 14 | decision table name to set withdrawal limit of the source object |
| `wdraw_lim` | `real` | 15 | actual withdrawal limit of source object (res-frac principal, aqu-max depth (m); cha-min flow (m3/s)) |
| `frac` | `real` | 16 | fraction of transfer supplied by the source |
| `comp` | `character (len=1)` | 17 | compensate if other source objects are past withdrawal threshold (y/n) |

### transfer_receiving_objects

- **Defined in source**: `water_allocation_module.f90:21`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `typ` | `character (len=10)` | 22 | receiving object type |
| `num` | `integer` | 23 | number of the receiving object |
| `frac` | `integer` | 25 | soil layer to receive incoming tile flow |

### outside_basin_objects

- **Defined in source**: `water_allocation_module.f90:29`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `daymoyr` | `integer` | 30 | recall file number - recall_db - daily, monthly or yearly |
| `aa` | `integer` | 31 | exco number in exco_db - ave annual constant |

### water_transfer_objects

- **Defined in source**: `water_allocation_module.f90:35`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `num` | `integer` | 36 | transfer object number |
| `ch_src` | `integer` | 37 | channel number in transfer object (0 if no channel) |
| `trn_typ` | `character (len=10)` | 38 | transfer type - decision table, recall, ave daily |
| `trn_typ_name` | `character (len=40)` | 39 | transfer type name of table or recall |
| `dtbl_num` | `integer` | 40 | number of decision table for demand amount (if used) |
| `dtbl_lum` | `integer` | 41 | number of decision table for demand amount for irrigation (if used) |
| `rec_num` | `integer` | 42 | number of recall file for demand amount (if used) |
| `amount` | `real` | 43 | m3 per day for urban objects and mm for hru |
| `right` | `character (len=2)` | 44 | water right (sr -senior or jr - junior right) |
| `src_num` | `integer` | 45 | number of source objects |
| `dtbl_src` | `character (len=25)` | 46 | decision table name to allocate sources |
| `dtbl_src_num` | `integer` | 47 | number of source allocation decision table |
| `src` | `transfer_source_objects` | 48 | sequential source objects as listed in wallo object |
| `osrc` | `outside_basin_objects` | 49 | number of outside basin source object - recall_db.rec file |
| `rcv_num` | `integer` | 50 | number of receiving objects |
| `rcv` | `transfer_receiving_objects` | 52 | receiving object |
| `unmet_m3` | `real` | 53 | m3 \|unmet demand for the object |
| `withdr_tot` | `real` | 54 | m3 \|total withdrawal of demand object from all sources |
| `irr_eff` | `real` | 55 | irrigation in-field efficiency |
| `surq` | `real` | 56 | surface runoff ratio |

### source_output

- **Defined in source**: `water_allocation_module.f90:61`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `demand` | `real` | 62 | ha-m !demand |
| `withdr` | `real` | 63 | ha-m \|amoount withdrawn from the source |
| `unmet` | `real` | 64 | ha-m \|unmet demand |

### water_allocation

- **Defined in source**: `water_allocation_module.f90:69`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `name` | `character (len=25)` | 70 | name of the water allocation object |
| `rule_typ` | `character (len=25)` | 71 | rule type to allocate water |
| `trn_cur` | `integer` | 72 | current transfer object |
| `trn_obs` | `integer` | 73 | number of transfer objects |
| `tot` | `source_output` | 74 | total demand, withdrawal and unmet for entire allocation object |
| `trn` | `water_transfer_objects` | 75 | dimension by transfer objects |

### water_treatment_use_data

- **Defined in source**: `water_allocation_module.f90:81`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `name` | `character (len=25)` | 82 | name of the water treatment plant |
| `stor_mx` | `real` | 84 | m3 !maximum storage in plant |
| `lag_days` | `real` | 85 | days !treatement time - lag outflow |
| `loss_fr` | `real` | 86 | water loss during treament |
| `org_min` | `character (len=25)` | 87 | sediment, carbon, and nutrients |
| `pests` | `character (len=25)` | 88 | pesticides - ppm |
| `paths` | `character (len=25)` | 89 | pathogens - cfu |
| `hmets` | `character (len=25)` | 90 | heavy metals - ppm |
| `salts` | `character (len=25)` | 91 | salt ions - ppm |
| `constit` | `character (len=25)` | 92 | other constituents - ppm |
| `descrip` | `character (len=80)` | 93 | description |
| `iorg_min` | `integer` | 94 | sediment, carbon, and nutrients - pointer to om_use.wal |
| `ipests` | `integer` | 95 | pesticides |
| `ipaths` | `integer` | 96 | pathogens |
| `isalts` | `integer` | 97 | salt ions |
| `iconstit` | `integer` | 98 | other constituents |

### outside_basin_source

- **Defined in source**: `water_allocation_module.f90:104`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `name` | `character (len=25)` | 105 | name of outside basin source |
| `stor_mx` | `real` | 106 | m3 !maximum storage in plant |
| `lag_days` | `real` | 107 | days !treatement time - lag outflow |
| `loss_fr` | `real` | 108 | water loss during treament |
| `iorg_min` | `integer` | 109 | sediment, carbon, and nutrients - pointer to om_use.wal |
| `ipests` | `integer` | 110 | pesticides |
| `ipaths` | `integer` | 111 | pathogens |
| `isalts` | `integer` | 112 | salt ions |
| `iconstit` | `integer` | 113 | other constituents |

### outside_basin_receive

- **Defined in source**: `water_allocation_module.f90:118`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `name` | `character (len=25)` | 119 | name of outside basin receiving object |
| `filename` | `character (len=25)` | 120 | name of outside basin receiving object |

### aquifer_loss

- **Defined in source**: `water_allocation_module.f90:124`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `aqu_num` | `integer` | 125 | aquifer number |
| `frac` | `real` | 126 | fraction of loss in specific aquifer |

### water_transfer_data

- **Defined in source**: `water_allocation_module.f90:130`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `name` | `character (len=25)` | 131 | name of the water tower or pipe |
| `init` | `character (len=25)` | 132 | name of the intitial concentrations |
| `stor_mx` | `real` | 133 | m3 !maximum storage in plant |
| `ddown_days` | `real` | 134 | days !days to drawdown the storage to zero |
| `loss_fr` | `real` | 135 | water loss during treament |
| `num_aqu` | `integer` | 136 | number of aquifers |
| `aqu_loss` | `aquifer_loss` | 137 |  |

### water_canal_data

- **Defined in source**: `water_allocation_module.f90:143`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `name` | `character (len=25)` | 144 | name of the canal |
| `w_sta` | `character (len=25)` | 145 | name of nearby weather station |
| `init` | `character (len=25)` | 146 | name of the intitial concentrations in canal |
| `dtbl` | `character (len=25)` | 147 | name of decision table to determine canal outflow |
| `ddown_days` | `real` | 148 | days !days to drawdown the storage to zero |
| `w` | `real` | 149 | m !top width of canal |
| `d` | `real` | 150 | m !depth of canal |
| `s` | `real` | 151 | m !slope of canal |
| `ss` | `real` | 152 | m/m !side slope of trapezoidal canal |
| `sat_con` | `real` | 153 | to compute percolation from canal to groundwater |
| `loss_fr` | `real` | 154 | water loss during treament |
| `bed_thick` | `real` | 155 | m !bed sediment thickness for Darcy seepage (gwflow; 0 if not used) |
| `div_id` | `integer` | 156 | recall diversion ID (gwflow; 0 if wallo-routed) |
| `day_beg` | `integer` | 157 | Julian day canal begins operation (gwflow external; 0 otherwise) |
| `day_end` | `integer` | 158 | Julian day canal ends operation (gwflow external; 0 otherwise) |
| `num_aqu` | `integer` | 159 | number of aquifers |
| `aqu_loss` | `aquifer_loss` | 160 |  |

### transfer_object_output

- **Defined in source**: `water_allocation_module.f90:170`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `trn_flo` | `real` | 171 | m3 \|total transfer of the transfer object |
| `src` | `source_output` | 172 |  |

### water_allocation_output

- **Defined in source**: `water_allocation_module.f90:176`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `trn` | `transfer_object_output` | 177 |  |

### wallo_header

- **Defined in source**: `water_allocation_module.f90:184`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `day` | `character(len=6)` | 185 |  |
| `mo` | `character(len=6)` | 186 |  |
| `day_mo` | `character(len=6)` | 187 |  |
| `yrc` | `character(len=6)` | 188 |  |
| `itrn` | `character(len=8)` | 189 |  |
| `trn_typ` | `character(len=16)` | 190 |  |
| `trn_num` | `character(len=16)` | 191 |  |
| `rcv_typ` | `character(len=17)` | 192 |  |
| `rcv_num` | `character(len=16)` | 193 |  |
| `src1_obj` | `character(len=12)` | 194 |  |
| `src1_typ` | `character(len=12)` | 195 |  |
| `src1_num` | `character(len=12)` | 196 |  |
| `trn1` | `character(len=15)` | 197 | ha-m \|demand - muni or irrigation |
| `s1out` | `character(len=15)` | 198 | ha-m \|withdrawal from source 1 |
| `s1un` | `character(len=12)` | 199 | ha-m \|unmet from source 1 |
| `src2_typ` | `character(len=12)` | 200 |  |
| `src2_num` | `character(len=12)` | 201 |  |
| `trn2` | `character(len=15)` | 202 | ha-m \|demand - muni or irrigation |
| `s2out` | `character(len=15)` | 203 | ha-m \|withdrawal from source 2 |
| `s2un` | `character(len=12)` | 204 | ha-m \|unmet from source 2 |
| `src3_typ` | `character(len=12)` | 205 |  |
| `src3_num` | `character(len=12)` | 206 |  |
| `trn3` | `character(len=15)` | 207 | ha-m \|demand - muni or irrigation |
| `s3out` | `character(len=15)` | 208 | ha-m \|withdrawal from source 3 |
| `s3un` | `character(len=12)` | 209 | ha-m \|unmet from source 3 |

### wallo_header_units

- **Defined in source**: `water_allocation_module.f90:214`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `day` | `character (len=8)` | 215 |  |
| `mo` | `character (len=8)` | 216 |  |
| `day_mo` | `character (len=8)` | 217 |  |
| `yrc` | `character (len=8)` | 218 |  |
| `itrn` | `character (len=8)` | 219 |  |
| `trn_typ` | `character (len=16)` | 220 |  |
| `trn_num` | `character (len=16)` | 221 |  |
| `rcv_typ` | `character (len=16)` | 222 |  |
| `rcv_num` | `character (len=16)` | 223 |  |
| `src1_obj` | `character (len=12)` | 224 |  |
| `src1_typ` | `character (len=12)` | 225 |  |
| `src1_num` | `character (len=8)` | 226 |  |
| `trn1` | `character (len=15)` | 227 | ha-m \|demand - muni or irrigation |
| `s1out` | `character (len=15)` | 228 | ha-m \|withdrawal from source 1 |
| `s1un` | `character (len=9)` | 229 | ha-m \|unmet from source 1 |
| `src2_typ` | `character (len=15)` | 230 |  |
| `src2_num` | `character (len=15)` | 231 |  |
| `trn2` | `character (len=15)` | 232 | ha-m \|demand - muni or irrigation |
| `s2out` | `character (len=15)` | 233 | ha-m \|withdrawal from source 2 |
| `s2un` | `character (len=15)` | 234 | ha-m \|unmet from source 2 |
| `src3_typ` | `character (len=15)` | 235 |  |
| `src3_num` | `character (len=15)` | 236 |  |
| `trn3` | `character (len=15)` | 237 | ha-m \|demand - muni or irrigation |
| `s3out` | `character (len=15)` | 238 | ha-m \|withdrawal from source 3 |
| `s3un` | `character (len=15)` | 239 | ha-m \|unmet from source 3 |

## Variables Defined
### trans_m3

- **Type**: `real`
- **Defined in source**: `water_allocation_module.f90:5`

### trn_m3

- **Type**: `real`
- **Defined in source**: `water_allocation_module.f90:6`
- **Source note**: m3     |demand

### walloz

- **Type**: `source_output`
- **Defined in source**: `water_allocation_module.f90:66`

### wallo

- **Type**: `water_allocation`
- **Defined in source**: `water_allocation_module.f90:77`
- **Source note**: dimension by water allocation objects

### wal

- **Type**: `water_allocation`
- **Defined in source**: `water_allocation_module.f90:78`

### wtp

- **Type**: `water_treatment_use_data`
- **Defined in source**: `water_allocation_module.f90:100`

### wuse

- **Type**: `water_treatment_use_data`
- **Defined in source**: `water_allocation_module.f90:101`

### osrc

- **Type**: `outside_basin_source`
- **Defined in source**: `water_allocation_module.f90:115`

### orcv

- **Type**: `outside_basin_receive`
- **Defined in source**: `water_allocation_module.f90:122`

### wtow

- **Type**: `water_transfer_data`
- **Defined in source**: `water_allocation_module.f90:139`

### pipe

- **Type**: `water_transfer_data`
- **Defined in source**: `water_allocation_module.f90:140`

### canal

- **Type**: `water_canal_data`
- **Defined in source**: `water_allocation_module.f90:162`

### om_init_name

- **Type**: `character(len=16), dimension(:), allocatable`
- **Defined in source**: `water_allocation_module.f90:164`

### om_treat_name

- **Type**: `character(len=16), dimension(:), allocatable`
- **Defined in source**: `water_allocation_module.f90:165`

### om_use_name

- **Type**: `character(len=16), dimension(:), allocatable`
- **Defined in source**: `water_allocation_module.f90:166`

### om_osrc_name

- **Type**: `character(len=16), dimension(:), allocatable`
- **Defined in source**: `water_allocation_module.f90:167`

### wallod_out

- **Type**: `water_allocation_output`
- **Defined in source**: `water_allocation_module.f90:179`
- **Source note**: dimension by transfer objects

### wallom_out

- **Type**: `water_allocation_output`
- **Defined in source**: `water_allocation_module.f90:180`
- **Source note**: dimension by transfer objects

### walloy_out

- **Type**: `water_allocation_output`
- **Defined in source**: `water_allocation_module.f90:181`
- **Source note**: dimension by transfer objects

### walloa_out

- **Type**: `water_allocation_output`
- **Defined in source**: `water_allocation_module.f90:182`
- **Source note**: dimension by transfer objects

### wallo_hdr

- **Type**: `wallo_header`
- **Defined in source**: `water_allocation_module.f90:212`

### wallo_hdr_units

- **Type**: `wallo_header_units`
- **Defined in source**: `water_allocation_module.f90:242`

## Subroutines Defined
(No subroutines detected.)

## Functions Defined
### wallout_add

### wallo_div_const

## Used By Source Routines

```dataview
LIST file.link
WHERE type = "source" AND contains(module, this.module_name)
```

<!-- USER-NOTES-START -->
## Notes
Use this section for type and variable meanings, units, and allowed values. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
