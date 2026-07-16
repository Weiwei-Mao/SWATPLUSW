---
type: module
tags:
  - swat/module
  - swat/to-read
file: reservoir_module.f90
note_file: reservoir_module.f90
module_name: reservoir_module
defines_types:
  - reservoir
  - wetland
  - reservoir_pest_processes
  - res_header
  - res_header1
  - reservoir_hdr
  - res_headerbsn
  - res_header_unit
  - res_header_unit1
  - res_header_unit2
  - res_header_unitbsn
defines_vars:
  - reactw
  - volatpst
  - setlpst
  - resuspst
  - difus
  - reactb
  - bury
  - res_ob
  - wet_ob
  - res_pest_d
  - res_pest_m
  - res_pest_y
  - res_pest_a
  - wet_pest_d
  - wet_pest_m
  - wet_pest_y
  - wet_pest_a
  - res_hdr
  - res_hdr1
  - res_hdr2
  - res_hdrbsn
  - res_hdr_unt
  - res_hdr_unt1
  - res_hdr_untbsn
defines_subroutines: []
defines_functions: []
defines_procedures: []
purpose: ""
---

# reservoir_module

> [!info] Module
> Defines derived types and module-level variables.

## Defined Types
### reservoir

- **Defined in source**: `reservoir_module.f90:13`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `name` | `character(len=13)` | 14 |  |
| `ob` | `integer` | 15 | object number if reservoir object; hru number if hru object |
| `props` | `integer` | 16 | points to res_dat |
| `wallo_call` | `integer` | 17 | !0 if not called from wallo on the current day; 1 if already called |
| `iweir` | `integer` | 18 | !weir ID Jaehak 2023 |
| `rel_tbl` | `character (len=1)` | 19 | d == decision table, c == conditions table |
| `psa` | `real` | 20 | ha \|res surface area when res is filled to princ spillway |
| `pvol` | `real` | 21 | ha-m \|vol of water needed to fill the res to the princ spillway (read in as ha-m and converted to m^3) |
| `esa` | `real` | 22 | ha \|res surface area when res is filled to emerg spillway |
| `evol` | `real` | 23 | ha-m \|vol of water needed to fill the res to the emerg spillway (read in as ha-m and converted to m^3) |
| `br1` | `real` | 24 | none \|vol-surface area coefficient for reservoirs (model estimates if zero) vol-depth coefficient for hru impoundment |
| `br2` | `real` | 26 | none \|vol-surface area coefficient for reservoirs (model estimates if zero) vol-depth coefficient for hru impoundment |
| `depth` | `real` | 28 | m !average depth of water |
| `weir_hgt` | `real` | 29 | m !height of weir above the bottom |
| `weir_wid` | `real` | 30 | m !width of weir above the bottom Jaehak 2022 |
| `seci` | `real` | 31 | m !seci depth |
| `prev_flo` | `real` | 32 | m3 !previous days flow to smooth outflows |
| `lag_up` | `real` | 33 | !lag parameter for increasing outflow - prevents sudden jumps |
| `lag_down` | `real` | 34 | !lag parameter for decreasing outflow - prevents sudden drops |
| `kd` | `real, dimension (:), allocatable` | 35 | \|aquatic mixing velocity (diffusion/dispersion)-using mol_wt |
| `aq_mix` | `real, dimension (:), allocatable` | 36 | m/day \|aquatic mixing velocity (diffusion/dispersion)-using mol_wt Additions to include hanazaki_06 release method \|Jose T 2025 |
| `I_mon_past` | `real, dimension(:), allocatable` | 39 | m3 \|Monthly mean inflow for the last N*12 months |
| `I_mean` | `real` | 40 | m3 \|Annual mean inflow for the last N years |
| `S_ini` | `real` | 41 | m3 \|Storage at the beginning of the operational year |
| `N_memory` | `integer` | 42 | m3 \|Number of years in the memory (by default 1 year) |
| `daily_inflow_array` | `real, dimension(:), allocatable` | 43 | m3 \|Array to store daily inflow for the month |
| `c_ratio` | `real` | 44 | \|Capacity ratio |
| `d_mean` | `real` | 45 | m3 \|Annual mean irrigation demand |
| `d_mon_past` | `real, dimension(:), allocatable` | 46 | m3 \|Monthly mean irrigation demand for the last N*12 months |
| `daily_demand_array` | `real, dimension(:), allocatable` | 47 | m3 \|Array to store daily irrigation demand for the month |
| `d_irrig_day` | `real` | 48 | m3 \|Daily irrigation demand |
| `irrig_track` | `integer` | 49 |  |

### wetland

- **Defined in source**: `reservoir_module.f90:53`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `iweir` | `integer` | 54 | !weir ID Jaehak 2022 |
| `psa` | `real` | 55 | ha \|res surface area when res is filled to princ spillway |
| `pvol` | `real` | 56 | m^3 \|vol of water needed to fill the res to the princ spillway (read in as ha-m and converted to m^3) |
| `esa` | `real` | 57 | ha \|res surface area when res is filled to emerg spillway |
| `evol` | `real` | 58 | m^3 \|vol of water needed to fill the res to the emerg spillway (read in as ha-m and converted to m^3) |
| `area_ha` | `real` | 59 | ha !reservoir surface area |
| `depth` | `real` | 60 | m !average depth of water |
| `weir_hgt` | `real` | 61 | m !height of weir above the bottom |
| `weir_wid` | `real` | 62 | m !width of weir Jaehak 2022 |
| `seci` | `real` | 63 | m !seci depth |

### reservoir_pest_processes

- **Defined in source**: `reservoir_module.f90:67`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `react` | `real` | 68 | kg !pesticide lost through reactions in water layer |
| `volat` | `real` | 69 | kg !pesticide lost through volatilization |
| `settle` | `real` | 70 | kg !pesticide settling to benthic layer |
| `resus` | `real` | 71 | kg !pesticide resuspended into lake water |
| `difus` | `real` | 72 | kg !pesticide diffusing from benthic sediment to water |
| `react_ben` | `real` | 73 | kg !pesticide lost from benthic by reactions |
| `bury` | `real` | 74 | Kg \|pesticide lost from benthic by burial |

### res_header

- **Defined in source**: `reservoir_module.f90:85`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `day` | `character (len=5)` | 87 |  |
| `mo` | `character (len=6)` | 88 |  |
| `day_mo` | `character (len=6)` | 89 |  |
| `yrc` | `character (len=6)` | 90 |  |
| `j` | `character (len=9)` | 91 |  |
| `id` | `character (len=9)` | 92 |  |
| `name` | `character (len=16)` | 93 |  |
| `flo` | `character (len=13)` | 94 | ha-m \|volume of water |
| `sed` | `character (len=12)` | 95 | metric tons \|sediment |
| `orgn` | `character (len=10)` | 96 | kg N \|organic N |
| `sedp` | `character (len=10)` | 97 | kg P \|organic P |
| `no3` | `character (len=10)` | 98 | kg N \|NO3-N |
| `solp` | `character (len=10)` | 99 | kg P \|mineral (soluble P) |
| `chla` | `character (len=10)` | 100 | kg \|chlorophyll-a |
| `nh3` | `character (len=10)` | 101 | kg N \|NH3 |
| `no2` | `character (len=10)` | 102 | kg N \|NO2 |
| `cbod` | `character (len=10)` | 103 | kg \|carbonaceous biological oxygen demand |
| `dox` | `character (len=10)` | 104 | kg \|dissolved oxygen |
| `san` | `character (len=10)` | 105 | tons \|detached sand |
| `sil` | `character (len=10)` | 106 | tons \|detached silt |
| `cla` | `character (len=10)` | 107 | tons \|detached clay |
| `sag` | `character (len=10)` | 108 | tons \|detached small ag |
| `lag` | `character (len=10)` | 109 | tons \|detached large ag |
| `grv` | `character (len=10)` | 110 | tons \|gravel |
| `temp` | `character (len=10)` | 111 | deg c \|temperature |

### res_header1

- **Defined in source**: `reservoir_module.f90:115`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `flo` | `character (len=8)` | 117 | ha-m \|volume of water |
| `sed` | `character (len=10)` | 118 | metric tons \|sediment |
| `orgn` | `character (len=10)` | 119 | kg N \|organic N |
| `sedp` | `character (len=10)` | 120 | kg P \|organic P |
| `no3` | `character (len=10)` | 121 | kg N \|NO3-N |
| `solp` | `character (len=10)` | 122 | kg P \|mineral (soluble P) |
| `chla` | `character (len=10)` | 123 | kg \|chlorophyll-a |
| `nh3` | `character (len=10)` | 124 | kg N \|NH3 |
| `no2` | `character (len=10)` | 125 | kg N \|NO2 |
| `cbod` | `character (len=10)` | 126 | kg \|carbonaceous biological oxygen demand |
| `dox` | `character (len=10)` | 127 | kg \|dissolved oxygen |
| `san` | `character (len=10)` | 128 | tons \|detached sand |
| `sil` | `character (len=10)` | 129 | tons \|detached silt |
| `cla` | `character (len=10)` | 130 | tons \|detached clay |
| `sag` | `character (len=10)` | 131 | tons \|detached small ag |
| `lag` | `character (len=10)` | 132 | tons \|detached large ag |
| `grv` | `character (len=10)` | 133 | tons \|gravel |
| `temp` | `character (len=10)` | 134 | deg c \|temperature |

### reservoir_hdr

- **Defined in source**: `reservoir_module.f90:138`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `area_ha` | `character (len=10)` | 140 |  |
| `evap` | `character (len=10)` | 141 | mm \|evaporation from res surface area |
| `seep` | `character (len=10)` | 142 | mm \|seepage from res bottom |
| `sed_setl` | `character (len=10)` | 143 | t \|sediment settling |
| `seci` | `character (len=10)` | 144 | m !seci depth |
| `solp_loss` | `character (len=10)` | 145 | kg \|soluble phosphorus loss |
| `sedp_loss` | `character (len=10)` | 146 | kg \|sediment attached phosphorus loss |
| `orgn_loss` | `character (len=10)` | 147 | kg \|organic nitrogen loss |
| `no3_loss` | `character (len=10)` | 148 | kg \|nitrate loss |
| `nh3_loss` | `character (len=10)` | 149 | kg \|ammonium nitrogen loss |
| `no2_loss` | `character (len=10)` | 150 | kg \|nitrite loss |

### res_headerbsn

- **Defined in source**: `reservoir_module.f90:154`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `flo` | `character (len=8)` | 156 | ha-m \|volume of water |
| `sed` | `character (len=12)` | 157 | metric tons \|sediment |
| `orgn` | `character (len=12)` | 158 | kg N \|organic N |
| `sedp` | `character (len=12)` | 159 | kg P \|organic P |
| `no3` | `character (len=12)` | 160 | kg N \|NO3-N |
| `solp` | `character (len=12)` | 161 | kg P \|mineral (soluble P) |
| `chla` | `character (len=12)` | 162 | kg \|chlorophyll-a |
| `nh3` | `character (len=12)` | 163 | kg N \|NH3 |
| `no2` | `character (len=12)` | 164 | kg N \|NO2 |
| `cbod` | `character (len=12)` | 165 | kg \|carbonaceous biological oxygen demand |
| `dox` | `character (len=12)` | 166 | kg \|dissolved oxygen |
| `san` | `character (len=12)` | 167 | tons \|detached sand |
| `sil` | `character (len=12)` | 168 | tons \|detached silt |
| `cla` | `character (len=12)` | 169 | tons \|detached clay |
| `sag` | `character (len=12)` | 170 | tons \|detached small ag |
| `lag` | `character (len=12)` | 171 | tons \|detached large ag |
| `grv` | `character (len=12)` | 172 | tons \|gravel |
| `temp` | `character (len=12)` | 173 | deg c \|temperature |

### res_header_unit

- **Defined in source**: `reservoir_module.f90:177`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `day` | `character (len=5)` | 179 |  |
| `mo` | `character (len=6)` | 180 |  |
| `day_mo` | `character (len=6)` | 181 |  |
| `yrc` | `character (len=6)` | 182 |  |
| `j` | `character (len=9)` | 183 |  |
| `id` | `character (len=9)` | 184 |  |
| `name` | `character (len=16)` | 185 |  |
| `flo` | `character (len=13)` | 186 | ha-m \|volume of water |
| `sed` | `character (len=12)` | 187 | metric tons \|sediment |
| `orgn` | `character (len=10)` | 188 | kg N \|organic N |
| `sedp` | `character (len=10)` | 189 | kg P \|organic P |
| `no3` | `character (len=10)` | 190 | kg N \|NO3-N |
| `solp` | `character (len=10)` | 191 | kg P \|mineral (soluble P) |
| `chla` | `character (len=10)` | 192 | kg \|chlorophyll-a |
| `nh3` | `character (len=10)` | 193 | kg N \|NH3 |
| `no2` | `character (len=10)` | 194 | kg N \|NO2 |
| `cbod` | `character (len=10)` | 195 | kg \|carbonaceous biological oxygen demand |
| `dox` | `character (len=10)` | 196 | kg \|dissolved oxygen |
| `san` | `character (len=10)` | 197 | tons \|detached sand |
| `sil` | `character (len=10)` | 198 | tons \|detached silt |
| `cla` | `character (len=10)` | 199 | tons \|detached clay |
| `sag` | `character (len=10)` | 200 | tons \|detached small ag |
| `lag` | `character (len=10)` | 201 | tons \|detached large ag |
| `grv` | `character (len=10)` | 202 | tons \|gravel |
| `temp` | `character (len=10)` | 203 | deg c \|temperature |

### res_header_unit1

- **Defined in source**: `reservoir_module.f90:207`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `flo` | `character (len=10)` | 209 | ha-m \|volume of water |
| `sed` | `character (len=8)` | 210 | metric tons \|sediment |
| `orgn` | `character (len=10)` | 211 | kg N \|organic N |
| `sedp` | `character (len=10)` | 212 | kg P \|organic P |
| `no3` | `character (len=10)` | 213 | kg N \|NO3-N |
| `solp` | `character (len=10)` | 214 | kg P \|mineral (soluble P) |
| `chla` | `character (len=10)` | 215 | kg \|chlorophyll-a |
| `nh3` | `character (len=10)` | 216 | kg N \|NH3 |
| `no2` | `character (len=10)` | 217 | kg N \|NO2 |
| `cbod` | `character (len=10)` | 218 | kg \|carbonaceous biological oxygen demand |
| `dox` | `character (len=10)` | 219 | kg \|dissolved oxygen |
| `san` | `character (len=10)` | 220 | tons \|detached sand |
| `sil` | `character (len=10)` | 221 | tons \|detached silt |
| `cla` | `character (len=10)` | 222 | tons \|detached clay |
| `sag` | `character (len=10)` | 223 | tons \|detached small ag |
| `lag` | `character (len=10)` | 224 | tons \|detached large ag |
| `grv` | `character (len=10)` | 225 | tons \|gravel |
| `temp` | `character (len=10)` | 226 | deg c \|temperature |

### res_header_unit2

- **Defined in source**: `reservoir_module.f90:230`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `area_ha` | `character (len=10)` | 232 |  |
| `evap` | `character (len=10)` | 233 |  |
| `seep` | `character (len=10)` | 234 | mm \|seepage from res bottom |
| `sed_setl` | `character (len=10)` | 235 | t \|sediment settling |
| `seci` | `character (len=10)` | 236 | m !seci depth |
| `solp_loss` | `character (len=10)` | 237 | kg \|soluble phosphorus loss |
| `sedp_loss` | `character (len=10)` | 238 | kg \|sediment attached phosphorus loss |
| `orgn_loss` | `character (len=10)` | 239 | kg \|organic nitrogen loss |
| `no3_loss` | `character (len=10)` | 240 | kg \|nitrate loss |
| `nh3_loss` | `character (len=10)` | 241 | kg \|ammonium nitrogen loss |
| `no2_loss` | `character (len=10)` | 242 | kg \|nitrite loss |

### res_header_unitbsn

- **Defined in source**: `reservoir_module.f90:246`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `flo` | `character (len=10)` | 248 | m^3 \|volume of water |
| `sed` | `character (len=12)` | 249 | metric tons \|sediment |
| `orgn` | `character (len=10)` | 250 | kg N \|organic N |
| `sedp` | `character (len=12)` | 251 | kg P \|organic P |
| `no3` | `character (len=12)` | 252 | kg N \|NO3-N |
| `solp` | `character (len=12)` | 253 | kg P \|mineral (soluble P) |
| `chla` | `character (len=12)` | 254 | kg \|chlorophyll-a |
| `nh3` | `character (len=12)` | 255 | kg N \|NH3 |
| `no2` | `character (len=12)` | 256 | kg N \|NO2 |
| `cbod` | `character (len=12)` | 257 | kg \|carbonaceous biological oxygen demand |
| `dox` | `character (len=12)` | 258 | kg \|dissolved oxygen |
| `san` | `character (len=12)` | 259 | tons \|detached sand |
| `sil` | `character (len=12)` | 260 | tons \|detached silt |
| `cla` | `character (len=12)` | 261 | tons \|detached clay |
| `sag` | `character (len=12)` | 262 | tons \|detached small ag |
| `lag` | `character (len=12)` | 263 | tons \|detached large ag |
| `grv` | `character (len=12)` | 264 | tons \|gravel |
| `temp` | `character (len=12)` | 265 | deg c \|temperature |

## Variables Defined
### reactw

- **Type**: `real`
- **Defined in source**: `reservoir_module.f90:5`
- **Source note**: mg pst        |amount of pesticide in reach that is lost through reactions

### volatpst

- **Type**: `real`
- **Defined in source**: `reservoir_module.f90:6`
- **Source note**: mg pst        |amount of pesticide lost from reach by volatilization

### setlpst

- **Type**: `real`
- **Defined in source**: `reservoir_module.f90:7`
- **Source note**: mg pst        |amount of pesticide moving from water to sediment due to settling

### resuspst

- **Type**: `real`
- **Defined in source**: `reservoir_module.f90:8`
- **Source note**: mg pst        |amount of pesticide moving from sediment to reach due to resuspension

### difus

- **Type**: `real`
- **Defined in source**: `reservoir_module.f90:9`
- **Source note**: mg pst        |diffusion of pesticide from sediment to reach

### reactb

- **Type**: `real`
- **Defined in source**: `reservoir_module.f90:10`
- **Source note**: mg pst        |amount of pesticide in sediment that is lost through reactions

### bury

- **Type**: `real`
- **Defined in source**: `reservoir_module.f90:11`
- **Source note**: mg pst        |loss of pesticide from active sediment layer by burial

### res_ob

- **Type**: `reservoir`
- **Defined in source**: `reservoir_module.f90:51`

### wet_ob

- **Type**: `wetland`
- **Defined in source**: `reservoir_module.f90:65`

### res_pest_d

- **Type**: `reservoir_pest_processes`
- **Defined in source**: `reservoir_module.f90:76`

### res_pest_m

- **Type**: `reservoir_pest_processes`
- **Defined in source**: `reservoir_module.f90:77`

### res_pest_y

- **Type**: `reservoir_pest_processes`
- **Defined in source**: `reservoir_module.f90:78`

### res_pest_a

- **Type**: `reservoir_pest_processes`
- **Defined in source**: `reservoir_module.f90:79`

### wet_pest_d

- **Type**: `reservoir_pest_processes`
- **Defined in source**: `reservoir_module.f90:80`

### wet_pest_m

- **Type**: `reservoir_pest_processes`
- **Defined in source**: `reservoir_module.f90:81`

### wet_pest_y

- **Type**: `reservoir_pest_processes`
- **Defined in source**: `reservoir_module.f90:82`

### wet_pest_a

- **Type**: `reservoir_pest_processes`
- **Defined in source**: `reservoir_module.f90:83`

### res_hdr

- **Type**: `res_header`
- **Defined in source**: `reservoir_module.f90:113`

### res_hdr1

- **Type**: `res_header1`
- **Defined in source**: `reservoir_module.f90:136`

### res_hdr2

- **Type**: `reservoir_hdr`
- **Defined in source**: `reservoir_module.f90:152`

### res_hdrbsn

- **Type**: `res_headerbsn`
- **Defined in source**: `reservoir_module.f90:175`

### res_hdr_unt

- **Type**: `res_header_unit`
- **Defined in source**: `reservoir_module.f90:205`

### res_hdr_unt1

- **Type**: `res_header_unit1`
- **Defined in source**: `reservoir_module.f90:228`

### res_hdr_untbsn

- **Type**: `res_header_unitbsn`
- **Defined in source**: `reservoir_module.f90:267`

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
