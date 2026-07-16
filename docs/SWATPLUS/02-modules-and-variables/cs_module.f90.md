---
type: module
tags:
  - swat/module
  - swat/to-read
file: cs_module.f90
note_file: cs_module.f90
module_name: cs_module
defines_types:
  - cs_balance
  - object_cs_balance
  - fert_db_cs
  - output_csbal_header
  - output_cs_hdr_hru
defines_vars:
  - hcsb_d
  - hcsb_m
  - hcsb_y
  - hcsb_a
  - ru_hru_csb_d
  - ru_hru_csb_m
  - ru_hru_csb_y
  - ru_hru_csb_a
  - cs_basin_mo
  - cs_basin_yr
  - cs_basin_aa
  - fert_cs
  - fert_cs_flag
  - cs_uptake_kg
  - cs_uptake_on
  - cs_urban_conc
  - csb_hdr
  - cs_hdr_hru
defines_subroutines: []
defines_functions: []
defines_procedures: []
purpose: ""
---

# cs_module

> [!info] Module
> Defines derived types and module-level variables.

## Defined Types
### cs_balance

- **Defined in source**: `cs_module.f90:6`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `soil` | `real` | 8 | \|kg/ha \|total mass in the soil profile |
| `surq` | `real` | 9 | \|kg/ha \|mass lost in surface runoff in HRU |
| `sedm` | `real` | 10 | \|kg/ha \|mass lost in sediment runoff in HRU |
| `latq` | `real` | 11 | \|kg/ha \|mass in lateral flow in HRU |
| `urbq` | `real` | 12 | \|kg/ha \|mass in urban runoff |
| `wetq` | `real` | 13 | \|kg/ha \|mass in wetland outflow |
| `tile` | `real` | 14 | \|kg/ha \|mass in tile flow in HRU |
| `perc` | `real` | 15 | \|kg/ha \|mass leached past bottom of soil |
| `gwup` | `real` | 16 | \|kg/ha \|mass from groundwater (to soil profile) |
| `wtsp` | `real` | 17 | \|kg/ha \|mass in wetland seepage (to soil profile) |
| `irsw` | `real` | 18 | \|kg/ha \|mass applied on soil via surface water irrigation |
| `irgw` | `real` | 19 | \|kg/ha \|mass applied on soil via groundwater irrigation |
| `irwo` | `real` | 20 | \|kg/ha \|mass applied on soil via irrigation from without (wo) the watershed |
| `rain` | `real` | 21 | \|kg/ha \|mass added to soil via rainfall |
| `dryd` | `real` | 22 | \|kg/ha \|mass added to soil via dry atmospheric deposition |
| `fert` | `real` | 23 | \|kg/ha \|mass added to soil via fertilizer |
| `uptk` | `real` | 24 | \|kg/ha \|mass taken up by crop roots |
| `rctn` | `real` | 25 | \|kg/ha \|mass transferred by chemical reaction |
| `sorb` | `real` | 26 | \|kg/ha \|mass transferred by sorption |
| `conc` | `real` | 27 | \|mg/L \|concentration in soil water (averaged over all soil layers) |
| `srbd` | `real` | 28 | \|kg/ha \|mass sorbed to soil boron terms to add... uptake (already in list; do same as nitrate uptake) act_sta act_bor rsd_act rsd_bor sedm (already in list) |

### object_cs_balance

- **Defined in source**: `cs_module.f90:40`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `cs` | `cs_balance` | 41 |  |

### fert_db_cs

- **Defined in source**: `cs_module.f90:62`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `fertnm` | `character(len=16)` | 63 |  |
| `seo4` | `real` | 64 | kg seo4/ha \|fertilizer load of seo4 (kg/ha) |
| `seo3` | `real` | 65 | kg seo3/ha \|fertilizer load of seo3 (kg/ha) |
| `boron` | `real` | 66 | kg boron/ha \|fertilizer load of boron (kg/ha) |

### output_csbal_header

- **Defined in source**: `cs_module.f90:79`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `yrc` | `character (len=8)` | 80 |  |
| `mon` | `character (len=8)` | 81 |  |
| `day` | `character (len=8)` | 82 | soil profile balance - seo4 |
| `latseo4` | `character(len=16)` | 84 | 1 |
| `surseo4` | `character(len=16)` | 85 | 2 |
| `sedseo4` | `character(len=16)` | 86 | 3 |
| `urbseo4` | `character(len=16)` | 87 | 4 |
| `wetseo4` | `character(len=16)` | 88 | 5 |
| `tileseo4` | `character(len=16)` | 89 | 6 |
| `percseo4` | `character(len=16)` | 90 | 7 |
| `gwupseo4` | `character(len=16)` | 91 | 8 |
| `wtspseo4` | `character(len=16)` | 92 | 9 |
| `irswseo4` | `character(len=16)` | 93 | 10 |
| `irgwseo4` | `character(len=16)` | 94 | 11 |
| `irwoseo4` | `character(len=16)` | 95 | 12 |
| `rainseo4` | `character(len=16)` | 96 | 13 |
| `drydseo4` | `character(len=16)` | 97 | 14 |
| `fertseo4` | `character(len=16)` | 98 | 15 |
| `uptkseo4` | `character(len=16)` | 99 | 16 |
| `rctnseo4` | `character(len=16)` | 100 | 17 |
| `sorbseo4` | `character(len=16)` | 101 | 18 |
| `ptsoseo4` | `character(len=16)` | 102 | 19 |
| `poutseo4` | `character(len=16)` | 103 | 20 |
| `sldsseo4` | `character(len=16)` | 104 | 21 |
| `srbdseo4` | `character(len=16)` | 105 | 22 aquifer balance - seo4 |
| `gwseo4` | `character(len=16)` | 107 | 23 |
| `rchgseo4` | `character(len=16)` | 108 | 24 |
| `seepseo4` | `character(len=16)` | 109 | 25 |
| `rctaseo4` | `character(len=16)` | 110 | 26 |
| `srbaseo4` | `character(len=16)` | 111 | 27 |
| `aqdsseo4` | `character(len=16)` | 112 | 28 |
| `srdaseo4` | `character(len=16)` | 113 | 29 soil profile balance - seo3 |
| `latseo3` | `character(len=16)` | 115 | 30 |
| `surseo3` | `character(len=16)` | 116 | 31 |
| `sedseo3` | `character(len=16)` | 117 | 32 |
| `urbseo3` | `character(len=16)` | 118 | 33 |
| `wetseo3` | `character(len=16)` | 119 | 34 |
| `tileseo3` | `character(len=16)` | 120 | 35 |
| `percseo3` | `character(len=16)` | 121 | 36 |
| `gwupseo3` | `character(len=16)` | 122 | 37 |
| `wtspseo3` | `character(len=16)` | 123 | 38 |
| `irswseo3` | `character(len=16)` | 124 | 39 |
| `irgwseo3` | `character(len=16)` | 125 | 40 |
| `irwoseo3` | `character(len=16)` | 126 | 41 |
| `rainseo3` | `character(len=16)` | 127 | 42 |
| `drydseo3` | `character(len=16)` | 128 | 43 |
| `fertseo3` | `character(len=16)` | 129 | 44 |
| `uptkseo3` | `character(len=16)` | 130 | 45 |
| `rctnseo3` | `character(len=16)` | 131 | 46 |
| `sorbseo3` | `character(len=16)` | 132 | 47 |
| `ptsoseo3` | `character(len=16)` | 133 | 48 |
| `poutseo3` | `character(len=16)` | 134 | 49 |
| `sldsseo3` | `character(len=16)` | 135 | 50 |
| `srbdseo3` | `character(len=16)` | 136 | 51 aquifer balance - seo3 |
| `gwseo3` | `character(len=16)` | 138 | 52 |
| `rchgseo3` | `character(len=16)` | 139 | 53 |
| `seepseo3` | `character(len=16)` | 140 | 54 |
| `rctaseo3` | `character(len=16)` | 141 | 55 |
| `srbaseo3` | `character(len=16)` | 142 | 56 |
| `aqdsseo3` | `character(len=16)` | 143 | 57 |
| `srdaseo3` | `character(len=16)` | 144 | 58 soil profile balance - boron |
| `latborn` | `character(len=16)` | 146 | 59 |
| `surborn` | `character(len=16)` | 147 | 60 |
| `sedborn` | `character(len=16)` | 148 | 61 |
| `urbborn` | `character(len=16)` | 149 | 62 |
| `wetborn` | `character(len=16)` | 150 | 63 |
| `tileborn` | `character(len=16)` | 151 | 64 |
| `percborn` | `character(len=16)` | 152 | 65 |
| `gwupborn` | `character(len=16)` | 153 | 66 |
| `wtspborn` | `character(len=16)` | 154 | 67 |
| `irswborn` | `character(len=16)` | 155 | 68 |
| `irgwborn` | `character(len=16)` | 156 | 69 |
| `irwoborn` | `character(len=16)` | 157 | 70 |
| `rainborn` | `character(len=16)` | 158 | 71 |
| `drydborn` | `character(len=16)` | 159 | 72 |
| `fertborn` | `character(len=16)` | 160 | 73 |
| `uptkborn` | `character(len=16)` | 161 | 74 |
| `rctnborn` | `character(len=16)` | 162 | 75 |
| `sorbborn` | `character(len=16)` | 163 | 76 |
| `ptsoborn` | `character(len=16)` | 164 | 77 |
| `poutborn` | `character(len=16)` | 165 | 78 |
| `sldsborn` | `character(len=16)` | 166 | 79 |
| `srbdborn` | `character(len=16)` | 167 | 80 aquifer balance - boron |
| `gwborn` | `character(len=16)` | 169 | 81 |
| `rchgborn` | `character(len=16)` | 170 | 82 |
| `seepborn` | `character(len=16)` | 171 | 83 |
| `rctaborn` | `character(len=16)` | 172 | 84 |
| `srbaborn` | `character(len=16)` | 173 | 85 |
| `aqdsborn` | `character(len=16)` | 174 | 86 |
| `srdaborn` | `character(len=16)` | 175 | 87 |

### output_cs_hdr_hru

- **Defined in source**: `cs_module.f90:180`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `day` | `character (len=6)` | 181 |  |
| `mo` | `character (len=6)` | 182 |  |
| `day_mo` | `character (len=6)` | 183 |  |
| `yrc` | `character (len=6)` | 184 |  |
| `isd` | `character (len=8)` | 185 |  |
| `id` | `character (len=12)` | 186 | total cs in soil profile (solution; sorbed) |
| `seo4sl` | `character(len=15)` | 188 |  |
| `seo3sl` | `character(len=15)` | 189 |  |
| `bornsl` | `character(len=15)` | 190 | surface runoff |
| `seo4sq` | `character(len=15)` | 192 |  |
| `seo3sq` | `character(len=15)` | 193 |  |
| `bornsq` | `character(len=15)` | 194 | sediment runoff |
| `seo4sd` | `character(len=15)` | 196 |  |
| `seo3sd` | `character(len=15)` | 197 |  |
| `bornsd` | `character(len=15)` | 198 | lateral flow |
| `seo4lq` | `character(len=15)` | 200 |  |
| `seo3lq` | `character(len=15)` | 201 |  |
| `bornlq` | `character(len=15)` | 202 | urban sediment runoff |
| `seo4ub` | `character(len=15)` | 204 |  |
| `seo3ub` | `character(len=15)` | 205 |  |
| `bornub` | `character(len=15)` | 206 | wetland outflow |
| `seo4wt` | `character(len=15)` | 208 |  |
| `seo3wt` | `character(len=15)` | 209 |  |
| `bornwt` | `character(len=15)` | 210 | tile flow |
| `seo4tq` | `character(len=15)` | 212 |  |
| `seo3tq` | `character(len=15)` | 213 |  |
| `borntq` | `character(len=15)` | 214 | percolation |
| `seo4pc` | `character(len=15)` | 216 |  |
| `seo3pc` | `character(len=15)` | 217 |  |
| `bornpc` | `character(len=15)` | 218 | groundwater transfer |
| `seo4gt` | `character(len=15)` | 220 |  |
| `seo3gt` | `character(len=15)` | 221 |  |
| `borngt` | `character(len=15)` | 222 | wetland seepage |
| `seo4ws` | `character(len=15)` | 224 |  |
| `seo3ws` | `character(len=15)` | 225 |  |
| `bornws` | `character(len=15)` | 226 | irrigation (surface water) |
| `seo4is` | `character(len=15)` | 228 |  |
| `seo3is` | `character(len=15)` | 229 |  |
| `bornis` | `character(len=15)` | 230 | irrigation (groundwater) |
| `seo4ig` | `character(len=15)` | 232 |  |
| `seo3ig` | `character(len=15)` | 233 |  |
| `bornig` | `character(len=15)` | 234 | irrigation (outside watershed) |
| `seo4io` | `character(len=15)` | 236 |  |
| `seo3io` | `character(len=15)` | 237 |  |
| `bornio` | `character(len=15)` | 238 | rainfall (wet deposition) |
| `seo4rn` | `character(len=15)` | 240 |  |
| `seo3rn` | `character(len=15)` | 241 |  |
| `bornrn` | `character(len=15)` | 242 | dry deposition |
| `seo4dd` | `character(len=15)` | 244 |  |
| `seo3dd` | `character(len=15)` | 245 |  |
| `borndd` | `character(len=15)` | 246 | fertilizer |
| `seo4fz` | `character(len=15)` | 248 |  |
| `seo3fz` | `character(len=15)` | 249 |  |
| `bornfz` | `character(len=15)` | 250 | cs uptake |
| `seo4up` | `character(len=15)` | 252 |  |
| `seo3up` | `character(len=15)` | 253 |  |
| `bornup` | `character(len=15)` | 254 | cs chemial reactions |
| `seo4rc` | `character(len=15)` | 256 |  |
| `seo3rc` | `character(len=15)` | 257 |  |
| `bornrc` | `character(len=15)` | 258 | cs sorption |
| `seo4sp` | `character(len=15)` | 260 |  |
| `seo3sp` | `character(len=15)` | 261 |  |
| `bornsp` | `character(len=15)` | 262 | soil water concentration (averaged over layers) |
| `seo4c` | `character(len=15)` | 264 |  |
| `seo3c` | `character(len=15)` | 265 |  |
| `bornc` | `character(len=15)` | 266 | sorbed mass (total over layers) |
| `seo4srbd` | `character(len=15)` | 268 |  |
| `seo3srbd` | `character(len=15)` | 269 |  |
| `bornsrbd` | `character(len=15)` | 270 |  |

## Variables Defined
### hcsb_d

- **Type**: `object_cs_balance`
- **Defined in source**: `cs_module.f90:45`

### hcsb_m

- **Type**: `object_cs_balance`
- **Defined in source**: `cs_module.f90:46`

### hcsb_y

- **Type**: `object_cs_balance`
- **Defined in source**: `cs_module.f90:47`

### hcsb_a

- **Type**: `object_cs_balance`
- **Defined in source**: `cs_module.f90:48`

### ru_hru_csb_d

- **Type**: `object_cs_balance`
- **Defined in source**: `cs_module.f90:51`

### ru_hru_csb_m

- **Type**: `object_cs_balance`
- **Defined in source**: `cs_module.f90:52`

### ru_hru_csb_y

- **Type**: `object_cs_balance`
- **Defined in source**: `cs_module.f90:53`

### ru_hru_csb_a

- **Type**: `object_cs_balance`
- **Defined in source**: `cs_module.f90:54`

### cs_basin_mo

- **Type**: `real`
- **Defined in source**: `cs_module.f90:57`

### cs_basin_yr

- **Type**: `real`
- **Defined in source**: `cs_module.f90:58`

### cs_basin_aa

- **Type**: `real`
- **Defined in source**: `cs_module.f90:59`

### fert_cs

- **Type**: `fert_db_cs`
- **Defined in source**: `cs_module.f90:68`

### fert_cs_flag

- **Type**: `integer`
- **Defined in source**: `cs_module.f90:69`

### cs_uptake_kg

- **Type**: `real, dimension(:,:), allocatable`
- **Defined in source**: `cs_module.f90:72`
- **Source note**: specified daily constituent mass taken up by crop roots (kg/ha)

### cs_uptake_on

- **Type**: `integer`
- **Defined in source**: `cs_module.f90:73`
- **Source note**: flag for simulating constituent uptake

### cs_urban_conc

- **Type**: `real, dimension(:,:), allocatable`
- **Defined in source**: `cs_module.f90:76`
- **Source note**: constituent conc in suspended solid load from imp areas (mg cs / kg sed)

### csb_hdr

- **Type**: `output_csbal_header`
- **Defined in source**: `cs_module.f90:177`

### cs_hdr_hru

- **Type**: `output_cs_hdr_hru`
- **Defined in source**: `cs_module.f90:272`

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
