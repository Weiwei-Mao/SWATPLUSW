---
type: module
tags:
  - swat/module
  - swat/to-read
file: salt_module.f90
note_file: salt_module.f90
module_name: salt_module
defines_types:
  - salt_balance
  - object_salt_balance
  - fert_db_salt
  - output_saltbal_header
  - output_salt_hdr_hru
defines_vars:
  - hsaltb_d
  - hsaltb_m
  - hsaltb_y
  - hsaltb_a
  - ru_hru_saltb_d
  - ru_hru_saltb_m
  - ru_hru_saltb_y
  - ru_hru_saltb_a
  - salt_basin_mo
  - salt_basin_yr
  - salt_basin_aa
  - fert_salt
  - fert_salt_flag
  - salt_uptake_kg
  - salt_uptake_on
  - salt_urban_conc
  - saltb_hdr
  - salt_hdr_hru
defines_subroutines: []
defines_functions: []
defines_procedures: []
purpose: ""
---

# salt_module

> [!info] Module
> Defines derived types and module-level variables.

## Defined Types
### salt_balance

- **Defined in source**: `salt_module.f90:7`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `soil` | `real` | 9 | \|kg/ha \|total salt ion mass in the soil profile |
| `diss` | `real` | 10 | \|kg/ha \|salt ion mass transferred from sorbed phase to dissolved phase |
| `surq` | `real` | 11 | \|kg/ha \|salt ion mass lost in surface runoff in HRU |
| `latq` | `real` | 12 | \|kg/ha \|salt ion mass in lateral flow in HRU |
| `urbq` | `real` | 13 | \|kg/ha \|salt ion mass in urban runoff |
| `wetq` | `real` | 14 | \|kg/ha \|salt ion mass in wetland runoff |
| `tile` | `real` | 15 | \|kg/ha \|salt ion mass in tile flow in HRU |
| `perc` | `real` | 16 | \|kg/ha \|salt ion mass leached past bottom of soil |
| `gwup` | `real` | 17 | \|kg/ha \|salt ion mass from groundwater (to soil profile) |
| `wtsp` | `real` | 18 | \|kg/ha \|salt ion mass in wetland seepage (to soil profile) |
| `irsw` | `real` | 19 | \|kg/ha \|salt ion mass applied on soil via surface water irrigation |
| `irgw` | `real` | 20 | \|kg/ha \|salt ion mass applied on soil via groundwater irrigation |
| `irwo` | `real` | 21 | \|kg/ha \|salt ion mass applied on soil via girrigation from without (wo) the watershed |
| `rain` | `real` | 22 | \|kg/ha \|salt ion mass added to soil via rainfall |
| `dryd` | `real` | 23 | \|kg/ha \|salt ion mass added to soil via dry atmospheric deposition |
| `road` | `real` | 24 | \|kg/ha \|salt ion mass added to soil via applied road salt |
| `fert` | `real` | 25 | \|kg/ha \|salt ion mass added to soil via fertilizer |
| `amnd` | `real` | 26 | \|kg/ha \|salt ion mass added to soil via salt amendments |
| `uptk` | `real` | 27 | \|kg/ha \|salt ion mass taken up by crop roots |
| `conc` | `real` | 28 | \|mg/L \|salt ion concentration in soil water (averaged over all soil layers) |

### object_salt_balance

- **Defined in source**: `salt_module.f90:31`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `salt` | `salt_balance` | 32 |  |

### fert_db_salt

- **Defined in source**: `salt_module.f90:53`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `fertnm` | `character(len=16)` | 54 |  |
| `so4` | `real` | 55 | kg so4/ha \|fertilizer load of so4 (kg/ha) |
| `ca` | `real` | 56 | kg ca/ha \|fertilizer load of ca (kg/ha) |
| `mg` | `real` | 57 | kg mg/ha \|fertilizer load of mg (kg/ha) |
| `na` | `real` | 58 | kg na/ha \|fertilizer load of na (kg/ha) |
| `k` | `real` | 59 | kg k/ha \|fertilizer load of k (kg/ha) |
| `cl` | `real` | 60 | kg cl/ha \|fertilizer load of cl (kg/ha) |
| `co3` | `real` | 61 | kg co3/ha \|fertilizer load of co3 (kg/ha) |
| `hco3` | `real` | 62 | kg hco3/ha \|fertilizer load of hco3 (kg/ha) |

### output_saltbal_header

- **Defined in source**: `salt_module.f90:75`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `yrc` | `character (len=8)` | 76 |  |
| `mon` | `character (len=8)` | 77 |  |
| `day` | `character (len=8)` | 78 |  |
| `lat` | `character(len=16)` | 79 |  |
| `gw` | `character(len=16)` | 80 |  |
| `sur` | `character(len=16)` | 81 |  |
| `urb` | `character(len=16)` | 82 |  |
| `wet` | `character(len=16)` | 83 |  |
| `tile` | `character(len=16)` | 84 |  |
| `perc` | `character(len=16)` | 85 |  |
| `gwup` | `character(len=16)` | 86 |  |
| `wtsp` | `character(len=16)` | 87 |  |
| `irsw` | `character(len=16)` | 88 |  |
| `irgw` | `character(len=16)` | 89 |  |
| `irwo` | `character(len=16)` | 90 |  |
| `rain` | `character(len=16)` | 91 |  |
| `dryd` | `character(len=16)` | 92 |  |
| `road` | `character(len=16)` | 93 |  |
| `fert` | `character(len=16)` | 94 |  |
| `amnd` | `character(len=16)` | 95 |  |
| `uptk` | `character(len=16)` | 96 |  |
| `ptso` | `character(len=16)` | 97 |  |
| `pout` | `character(len=16)` | 98 |  |
| `rchg` | `character(len=16)` | 99 |  |
| `seep` | `character(len=16)` | 100 |  |
| `dssl` | `character(len=16)` | 101 |  |
| `dsaq` | `character(len=16)` | 102 |  |
| `slds` | `character(len=16)` | 103 |  |
| `slmn` | `character(len=16)` | 104 |  |
| `aqds` | `character(len=16)` | 105 |  |
| `aqmn` | `character(len=16)` | 106 |  |

### output_salt_hdr_hru

- **Defined in source**: `salt_module.f90:111`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `day` | `character (len=6)` | 112 |  |
| `mo` | `character (len=6)` | 113 |  |
| `day_mo` | `character (len=6)` | 114 |  |
| `yrc` | `character (len=6)` | 115 |  |
| `isd` | `character (len=8)` | 116 |  |
| `id` | `character (len=12)` | 117 | total salt in soil profile |
| `so4sl` | `character(len=15)` | 119 |  |
| `casl` | `character(len=15)` | 120 |  |
| `mgsl` | `character(len=15)` | 121 |  |
| `nasl` | `character(len=15)` | 122 |  |
| `ksl` | `character(len=15)` | 123 |  |
| `clsl` | `character(len=15)` | 124 |  |
| `co3sl` | `character(len=15)` | 125 |  |
| `hco3sl` | `character(len=15)` | 126 | surface runoff |
| `so4sq` | `character(len=15)` | 128 |  |
| `casq` | `character(len=15)` | 129 |  |
| `mgsq` | `character(len=15)` | 130 |  |
| `nasq` | `character(len=15)` | 131 |  |
| `ksq` | `character(len=15)` | 132 |  |
| `clsq` | `character(len=15)` | 133 |  |
| `co3sq` | `character(len=15)` | 134 |  |
| `hco3sq` | `character(len=15)` | 135 | lateral flow |
| `so4lq` | `character(len=15)` | 137 |  |
| `calq` | `character(len=15)` | 138 |  |
| `mglq` | `character(len=15)` | 139 |  |
| `nalq` | `character(len=15)` | 140 |  |
| `klq` | `character(len=15)` | 141 |  |
| `cllq` | `character(len=15)` | 142 |  |
| `co3lq` | `character(len=15)` | 143 |  |
| `hco3lq` | `character(len=15)` | 144 | urban runoff |
| `so4uq` | `character(len=15)` | 146 |  |
| `cauq` | `character(len=15)` | 147 |  |
| `mguq` | `character(len=15)` | 148 |  |
| `nauq` | `character(len=15)` | 149 |  |
| `kuq` | `character(len=15)` | 150 |  |
| `cluq` | `character(len=15)` | 151 |  |
| `co3uq` | `character(len=15)` | 152 |  |
| `hco3uq` | `character(len=15)` | 153 | wetland runoff |
| `so4wt` | `character(len=15)` | 155 |  |
| `cawt` | `character(len=15)` | 156 |  |
| `mgwt` | `character(len=15)` | 157 |  |
| `nawt` | `character(len=15)` | 158 |  |
| `kwt` | `character(len=15)` | 159 |  |
| `clwt` | `character(len=15)` | 160 |  |
| `co3wt` | `character(len=15)` | 161 |  |
| `hco3wt` | `character(len=15)` | 162 | tile flow |
| `so4tq` | `character(len=15)` | 164 |  |
| `catq` | `character(len=15)` | 165 |  |
| `mgtq` | `character(len=15)` | 166 |  |
| `natq` | `character(len=15)` | 167 |  |
| `ktq` | `character(len=15)` | 168 |  |
| `cltq` | `character(len=15)` | 169 |  |
| `co3tq` | `character(len=15)` | 170 |  |
| `hco3tq` | `character(len=15)` | 171 | percolation |
| `so4pc` | `character(len=15)` | 173 |  |
| `capc` | `character(len=15)` | 174 |  |
| `mgpc` | `character(len=15)` | 175 |  |
| `napc` | `character(len=15)` | 176 |  |
| `kpc` | `character(len=15)` | 177 |  |
| `clpc` | `character(len=15)` | 178 |  |
| `co3pc` | `character(len=15)` | 179 |  |
| `hco3pc` | `character(len=15)` | 180 | groundwater transfer |
| `so4gt` | `character(len=15)` | 182 |  |
| `cagt` | `character(len=15)` | 183 |  |
| `mggt` | `character(len=15)` | 184 |  |
| `nagt` | `character(len=15)` | 185 |  |
| `kgt` | `character(len=15)` | 186 |  |
| `clgt` | `character(len=15)` | 187 |  |
| `co3gt` | `character(len=15)` | 188 |  |
| `hco3gt` | `character(len=15)` | 189 | wetland seepage to soil |
| `so4ws` | `character(len=15)` | 191 |  |
| `caws` | `character(len=15)` | 192 |  |
| `mgws` | `character(len=15)` | 193 |  |
| `naws` | `character(len=15)` | 194 |  |
| `kws` | `character(len=15)` | 195 |  |
| `clws` | `character(len=15)` | 196 |  |
| `co3ws` | `character(len=15)` | 197 |  |
| `hco3ws` | `character(len=15)` | 198 | irrigation (surface water) |
| `so4is` | `character(len=15)` | 200 |  |
| `cais` | `character(len=15)` | 201 |  |
| `mgis` | `character(len=15)` | 202 |  |
| `nais` | `character(len=15)` | 203 |  |
| `kis` | `character(len=15)` | 204 |  |
| `clis` | `character(len=15)` | 205 |  |
| `co3is` | `character(len=15)` | 206 |  |
| `hco3is` | `character(len=15)` | 207 | irrigation (groundwater) |
| `so4ig` | `character(len=15)` | 209 |  |
| `caig` | `character(len=15)` | 210 |  |
| `mgig` | `character(len=15)` | 211 |  |
| `naig` | `character(len=15)` | 212 |  |
| `kig` | `character(len=15)` | 213 |  |
| `clig` | `character(len=15)` | 214 |  |
| `co3ig` | `character(len=15)` | 215 |  |
| `hco3ig` | `character(len=15)` | 216 | irrigation (outside watershed) |
| `so4io` | `character(len=15)` | 218 |  |
| `caio` | `character(len=15)` | 219 |  |
| `mgio` | `character(len=15)` | 220 |  |
| `naio` | `character(len=15)` | 221 |  |
| `kio` | `character(len=15)` | 222 |  |
| `clio` | `character(len=15)` | 223 |  |
| `co3io` | `character(len=15)` | 224 |  |
| `hco3io` | `character(len=15)` | 225 | rainfall (wet deposition) |
| `so4rn` | `character(len=15)` | 227 |  |
| `carn` | `character(len=15)` | 228 |  |
| `mgrn` | `character(len=15)` | 229 |  |
| `narn` | `character(len=15)` | 230 |  |
| `krn` | `character(len=15)` | 231 |  |
| `clrn` | `character(len=15)` | 232 |  |
| `co3rn` | `character(len=15)` | 233 |  |
| `hco3rn` | `character(len=15)` | 234 | dry deposition |
| `so4dd` | `character(len=15)` | 236 |  |
| `cadd` | `character(len=15)` | 237 |  |
| `mgdd` | `character(len=15)` | 238 |  |
| `nadd` | `character(len=15)` | 239 |  |
| `kdd` | `character(len=15)` | 240 |  |
| `cldd` | `character(len=15)` | 241 |  |
| `co3dd` | `character(len=15)` | 242 |  |
| `hco3dd` | `character(len=15)` | 243 | road salt application |
| `so4rd` | `character(len=15)` | 245 |  |
| `card` | `character(len=15)` | 246 |  |
| `mgrd` | `character(len=15)` | 247 |  |
| `nard` | `character(len=15)` | 248 |  |
| `krd` | `character(len=15)` | 249 |  |
| `clrd` | `character(len=15)` | 250 |  |
| `co3rd` | `character(len=15)` | 251 |  |
| `hco3rd` | `character(len=15)` | 252 | fertilizer application |
| `so4fz` | `character(len=15)` | 254 |  |
| `cafz` | `character(len=15)` | 255 |  |
| `mgfz` | `character(len=15)` | 256 |  |
| `nafz` | `character(len=15)` | 257 |  |
| `kfz` | `character(len=15)` | 258 |  |
| `clfz` | `character(len=15)` | 259 |  |
| `co3fz` | `character(len=15)` | 260 |  |
| `hco3fz` | `character(len=15)` | 261 | amnd salt application |
| `so4am` | `character(len=15)` | 263 |  |
| `caam` | `character(len=15)` | 264 |  |
| `mgam` | `character(len=15)` | 265 |  |
| `naam` | `character(len=15)` | 266 |  |
| `kam` | `character(len=15)` | 267 |  |
| `clam` | `character(len=15)` | 268 |  |
| `co3am` | `character(len=15)` | 269 |  |
| `hco3am` | `character(len=15)` | 270 | salt uptake |
| `so4up` | `character(len=15)` | 272 |  |
| `caup` | `character(len=15)` | 273 |  |
| `mgup` | `character(len=15)` | 274 |  |
| `naup` | `character(len=15)` | 275 |  |
| `kup` | `character(len=15)` | 276 |  |
| `clup` | `character(len=15)` | 277 |  |
| `co3up` | `character(len=15)` | 278 |  |
| `hco3up` | `character(len=15)` | 279 | soil water concentration (averaged over layers) |
| `so4c` | `character(len=15)` | 281 |  |
| `cac` | `character(len=15)` | 282 |  |
| `mgc` | `character(len=15)` | 283 |  |
| `nac` | `character(len=15)` | 284 |  |
| `kc` | `character(len=15)` | 285 |  |
| `clc` | `character(len=15)` | 286 |  |
| `co3c` | `character(len=15)` | 287 |  |
| `hco3c` | `character(len=15)` | 288 | salt mineral dissolution and precipitation |
| `dssl` | `character(len=15)` | 290 |  |

## Variables Defined
### hsaltb_d

- **Type**: `object_salt_balance`
- **Defined in source**: `salt_module.f90:36`

### hsaltb_m

- **Type**: `object_salt_balance`
- **Defined in source**: `salt_module.f90:37`

### hsaltb_y

- **Type**: `object_salt_balance`
- **Defined in source**: `salt_module.f90:38`

### hsaltb_a

- **Type**: `object_salt_balance`
- **Defined in source**: `salt_module.f90:39`

### ru_hru_saltb_d

- **Type**: `object_salt_balance`
- **Defined in source**: `salt_module.f90:42`

### ru_hru_saltb_m

- **Type**: `object_salt_balance`
- **Defined in source**: `salt_module.f90:43`

### ru_hru_saltb_y

- **Type**: `object_salt_balance`
- **Defined in source**: `salt_module.f90:44`

### ru_hru_saltb_a

- **Type**: `object_salt_balance`
- **Defined in source**: `salt_module.f90:45`

### salt_basin_mo

- **Type**: `real`
- **Defined in source**: `salt_module.f90:48`

### salt_basin_yr

- **Type**: `real`
- **Defined in source**: `salt_module.f90:49`

### salt_basin_aa

- **Type**: `real`
- **Defined in source**: `salt_module.f90:50`

### fert_salt

- **Type**: `fert_db_salt`
- **Defined in source**: `salt_module.f90:64`

### fert_salt_flag

- **Type**: `integer`
- **Defined in source**: `salt_module.f90:65`

### salt_uptake_kg

- **Type**: `real, dimension(:,:), allocatable`
- **Defined in source**: `salt_module.f90:68`
- **Source note**: specified daily salt mass taken up by crop roots (kg/ha)

### salt_uptake_on

- **Type**: `integer`
- **Defined in source**: `salt_module.f90:69`
- **Source note**: flag for simulating salt uptake

### salt_urban_conc

- **Type**: `real, dimension(:,:), allocatable`
- **Defined in source**: `salt_module.f90:72`
- **Source note**: salt ion conc in suspended solid load from imp areas (mg salt / kg sed)

### saltb_hdr

- **Type**: `output_saltbal_header`
- **Defined in source**: `salt_module.f90:108`

### salt_hdr_hru

- **Type**: `output_salt_hdr_hru`
- **Defined in source**: `salt_module.f90:292`

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
