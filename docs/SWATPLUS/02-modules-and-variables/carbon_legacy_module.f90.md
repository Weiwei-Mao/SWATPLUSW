---
type: module
tags:
  - swat/module
  - swat/to-read
file: carbon_legacy_module.f90
note_file: carbon_legacy_module.f90
module_name: carbon_legacy_module
defines_types:
  - output_plc_header
  - output_plc_header_units
  - output_soil_org_flux_header
  - output_soil_org_flux_header_units
  - output_cpool_header
  - output_cpool_header_units
  - output_n_p_pool_header
  - output_n_p_pool_header_units
  - output_carb_vars_header
  - output_org_allo_header
  - output_org_ratio_header
  - output_org_trans_header
  - output_org_trans_header_units
  - output_endsim_soil_prop_header
  - output_bsn_carb_header
  - output_bsn_carb_header_units
defines_vars:
  - plc_hdr
  - plc_hdr_units
  - soil_org_flux_hdr
  - soil_org_flux_hdr_units
  - cpool_hdr
  - cpool_units
  - n_p_pool_hdr
  - n_p_pool_units
  - carbvars_hdr
  - org_allow_hdr
  - org_ratio_hdr
  - org_trans_hdr
  - org_trans_units
  - endsim_soil_prop_hdr
  - bsn_carb_hdr
  - bsn_carb_hdr_units
defines_subroutines:
  - carbon_legacy_open
defines_functions: []
defines_procedures:
  - carbon_legacy_open
purpose: ""
---

# carbon_legacy_module

> [!info] Module
> Defines derived types and module-level variables.

## Defined Types
### output_plc_header

- **Defined in source**: `carbon_legacy_module.f90:19`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `freq` | `character (len=7)` | 20 |  |
| `day` | `character (len=11)` | 21 |  |
| `day_mo` | `character (len=11)` | 22 |  |
| `mo` | `character (len=11)` | 23 |  |
| `yrc` | `character (len=11)` | 24 |  |
| `isd` | `character (len=16)` | 25 |  |
| `id` | `character (len=21)` | 26 |  |
| `name` | `character (len=16)` | 27 |  |
| `tot_c` | `character(len=15)` | 28 |  |
| `ab_gr_c` | `character(len=15)` | 29 |  |
| `leaf_c` | `character(len=15)` | 30 |  |
| `stem_c` | `character(len=15)` | 31 |  |
| `seed_c` | `character(len=15)` | 32 |  |
| `root_c` | `character(len=15)` | 33 |  |
| `rsd_c` | `character(len=15)` | 34 |  |

### output_plc_header_units

- **Defined in source**: `carbon_legacy_module.f90:38`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `freq` | `character (len=7)` | 39 |  |
| `day` | `character (len=11)` | 40 |  |
| `day_mo` | `character (len=11)` | 41 |  |
| `mo` | `character (len=11)` | 42 |  |
| `yrc` | `character (len=11)` | 43 |  |
| `isd` | `character (len=16)` | 44 |  |
| `id` | `character (len=21)` | 45 |  |
| `name` | `character (len=16)` | 46 |  |
| `tot_c` | `character(len=15)` | 47 |  |
| `ab_gr_c` | `character(len=15)` | 48 |  |
| `leaf_c` | `character(len=15)` | 49 |  |
| `stem_c` | `character(len=15)` | 50 |  |
| `seed_c` | `character(len=15)` | 51 |  |
| `root_c` | `character(len=15)` | 52 |  |
| `rsd_c` | `character(len=15)` | 53 |  |

### output_soil_org_flux_header

- **Defined in source**: `carbon_legacy_module.f90:61`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `freq` | `character (len=7)` | 62 |  |
| `soil_lyr` | `character (len=12)` | 63 |  |
| `soil_depth` | `character (len=12)` | 64 |  |
| `day` | `character (len=12)` | 65 |  |
| `mo` | `character (len=12)` | 66 |  |
| `day_mo` | `character (len=12)` | 67 |  |
| `yrc` | `character (len=12)` | 68 |  |
| `isd` | `character (len=12)` | 69 |  |
| `id` | `character (len=23)` | 70 |  |
| `name` | `character (len=15)` | 71 |  |
| `cfmets1` | `character(len=15)` | 72 |  |
| `cfstrs1` | `character(len=15)` | 73 |  |
| `cfstrs2` | `character(len=15)` | 74 |  |
| `efmets1` | `character(len=15)` | 75 |  |
| `efstrs1` | `character(len=15)` | 76 |  |
| `efstrs2` | `character(len=15)` | 77 |  |
| `immmets1` | `character(len=15)` | 78 |  |
| `immstrs1` | `character(len=15)` | 79 |  |
| `immstrs2` | `character(len=15)` | 80 |  |
| `mnrmets1` | `character(len=15)` | 81 |  |
| `mnrstrs1` | `character(len=15)` | 82 |  |
| `mnrstrs2` | `character(len=15)` | 83 |  |
| `co2fmet` | `character(len=15)` | 84 |  |
| `co2fstr` | `character(len=15)` | 85 |  |
| `cfs1s2` | `character(len=15)` | 86 |  |
| `cfs1s3` | `character(len=15)` | 87 |  |
| `cfs2s1` | `character(len=15)` | 88 |  |
| `cfs2s3` | `character(len=15)` | 89 |  |
| `cfs3s1` | `character(len=15)` | 90 |  |
| `efs1s2` | `character(len=15)` | 91 |  |
| `efs1s3` | `character(len=15)` | 92 |  |
| `efs2s1` | `character(len=15)` | 93 |  |
| `efs2s3` | `character(len=15)` | 94 |  |
| `efs3s1` | `character(len=15)` | 95 |  |
| `imms1s2` | `character(len=15)` | 96 |  |
| `imms1s3` | `character(len=15)` | 97 |  |
| `imms2s1` | `character(len=15)` | 98 |  |
| `imms2s3` | `character(len=15)` | 99 |  |
| `imms3s1` | `character(len=15)` | 100 |  |
| `mnrs1s2` | `character(len=15)` | 101 |  |
| `mnrs1s3` | `character(len=15)` | 102 |  |
| `mnrs2s1` | `character(len=15)` | 103 |  |
| `mnrs2s3` | `character(len=15)` | 104 |  |
| `mnrs3s1` | `character(len=15)` | 105 |  |
| `co2fs1` | `character(len=15)` | 106 |  |
| `co2fs2` | `character(len=15)` | 107 |  |
| `co2fs3` | `character(len=15)` | 108 |  |

### output_soil_org_flux_header_units

- **Defined in source**: `carbon_legacy_module.f90:112`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `freq` | `character (len=7)` | 113 |  |
| `soil_lyr` | `character (len=12)` | 114 |  |
| `soil_depth` | `character (len=12)` | 115 |  |
| `day` | `character (len=12)` | 116 |  |
| `mo` | `character (len=12)` | 117 |  |
| `day_mo` | `character (len=12)` | 118 |  |
| `yrc` | `character (len=12)` | 119 |  |
| `isd` | `character (len=12)` | 120 |  |
| `id` | `character (len=23)` | 121 |  |
| `name` | `character (len=15)` | 122 |  |
| `cfmets1` | `character(len=15)` | 123 |  |
| `cfstrs1` | `character(len=15)` | 124 |  |
| `cfstrs2` | `character(len=15)` | 125 |  |
| `efmets1` | `character(len=15)` | 126 |  |
| `efstrs1` | `character(len=15)` | 127 |  |
| `efstrs2` | `character(len=15)` | 128 |  |
| `immmets1` | `character(len=15)` | 129 |  |
| `immstrs1` | `character(len=15)` | 130 |  |
| `immstrs2` | `character(len=15)` | 131 |  |
| `mnrmets1` | `character(len=15)` | 132 |  |
| `mnrstrs1` | `character(len=15)` | 133 |  |
| `mnrstrs2` | `character(len=15)` | 134 |  |
| `co2fmet` | `character(len=15)` | 135 |  |
| `co2fstr` | `character(len=15)` | 136 |  |
| `cfs1s2` | `character(len=15)` | 137 |  |
| `cfs1s3` | `character(len=15)` | 138 |  |
| `cfs2s1` | `character(len=15)` | 139 |  |
| `cfs2s3` | `character(len=15)` | 140 |  |
| `cfs3s1` | `character(len=15)` | 141 |  |
| `efs1s2` | `character(len=15)` | 142 |  |
| `efs1s3` | `character(len=15)` | 143 |  |
| `efs2s1` | `character(len=15)` | 144 |  |
| `efs2s3` | `character(len=15)` | 145 |  |
| `efs3s1` | `character(len=15)` | 146 |  |
| `imms1s2` | `character(len=15)` | 147 |  |
| `imms1s3` | `character(len=15)` | 148 |  |
| `imms2s1` | `character(len=15)` | 149 |  |
| `imms2s3` | `character(len=15)` | 150 |  |
| `imms3s1` | `character(len=15)` | 151 |  |
| `mnrs1s2` | `character(len=15)` | 152 |  |
| `mnrs1s3` | `character(len=15)` | 153 |  |
| `mnrs2s1` | `character(len=15)` | 154 |  |
| `mnrs2s3` | `character(len=15)` | 155 |  |
| `co2fs2` | `character(len=15)` | 156 |  |
| `co2fs3` | `character(len=15)` | 157 |  |

### output_cpool_header

- **Defined in source**: `carbon_legacy_module.f90:161`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `freq` | `character (len=7)` | 162 |  |
| `soil_lyr` | `character (len=12)` | 163 |  |
| `soil_depth` | `character (len=12)` | 164 |  |
| `day` | `character (len=12)` | 165 |  |
| `mo` | `character (len=12)` | 166 |  |
| `day_mo` | `character (len=12)` | 167 |  |
| `yrc` | `character (len=12)` | 168 |  |
| `isd` | `character (len=12)` | 169 |  |
| `id` | `character (len=22)` | 170 |  |
| `name` | `character (len=13)` | 171 |  |
| `residue_c` | `character(len=15)` | 172 |  |
| `str_c` | `character(len=15)` | 173 |  |
| `meta_c` | `character(len=15)` | 174 |  |
| `hs_c` | `character(len=15)` | 175 |  |
| `hp_c` | `character(len=15)` | 176 |  |
| `microb_c` | `character(len=15)` | 177 |  |
| `lig_c` | `character(len=15)` | 178 |  |
| `nonlig_c` | `character(len=15)` | 179 |  |
| `water_c` | `character(len=15)` | 180 |  |
| `manure_c` | `character(len=15)` | 181 |  |
| `root_mass` | `character(len=15)` | 182 |  |
| `soil_water` | `character(len=15)` | 183 |  |

### output_cpool_header_units

- **Defined in source**: `carbon_legacy_module.f90:187`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `freq` | `character (len=7)` | 188 |  |
| `soil_lyr` | `character (len=12)` | 189 |  |
| `soil_depth` | `character (len=12)` | 190 |  |
| `day` | `character (len=12)` | 191 |  |
| `mo` | `character (len=12)` | 192 |  |
| `day_mo` | `character (len=12)` | 193 |  |
| `yrc` | `character (len=12)` | 194 |  |
| `isd` | `character (len=12)` | 195 |  |
| `id` | `character (len=22)` | 196 |  |
| `name` | `character (len=13)` | 197 |  |
| `residue_c` | `character(len=15)` | 198 |  |
| `str_c` | `character(len=15)` | 199 |  |
| `meta_c` | `character(len=15)` | 200 |  |
| `hs_c` | `character(len=15)` | 201 |  |
| `hp_c` | `character(len=15)` | 202 |  |
| `microb_c` | `character(len=15)` | 203 |  |
| `lig_c` | `character(len=15)` | 204 |  |
| `nonlig_c` | `character(len=15)` | 205 |  |
| `water_c` | `character(len=15)` | 206 |  |
| `manure_c` | `character(len=15)` | 207 |  |
| `root_mass` | `character(len=15)` | 208 |  |
| `soil_water` | `character(len=15)` | 209 |  |

### output_n_p_pool_header

- **Defined in source**: `carbon_legacy_module.f90:213`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `freq` | `character (len=7)` | 214 |  |
| `soil_lyr` | `character (len=12)` | 215 |  |
| `soil_depth` | `character (len=12)` | 216 |  |
| `day` | `character (len=12)` | 217 |  |
| `mo` | `character (len=12)` | 218 |  |
| `day_mo` | `character (len=12)` | 219 |  |
| `yrc` | `character (len=12)` | 220 |  |
| `isd` | `character (len=12)` | 221 |  |
| `id` | `character (len=22)` | 222 |  |
| `name` | `character (len=13)` | 223 |  |
| `total_pool_n` | `character(len=15)` | 224 |  |
| `residue_n` | `character(len=15)` | 225 |  |
| `str_n` | `character(len=15)` | 226 |  |
| `meta_n` | `character(len=15)` | 227 |  |
| `hs_n` | `character(len=15)` | 228 |  |
| `hp_n` | `character(len=15)` | 229 |  |
| `microb_n` | `character(len=15)` | 230 |  |
| `lig_n` | `character(len=15)` | 231 |  |
| `nonlig_n` | `character(len=15)` | 232 |  |
| `water_n` | `character(len=15)` | 233 |  |
| `manure_n` | `character(len=15)` | 234 |  |
| `total_pool_p` | `character(len=15)` | 235 |  |
| `residue_p` | `character(len=15)` | 236 |  |
| `str_p` | `character(len=15)` | 237 |  |
| `meta_p` | `character(len=15)` | 238 |  |
| `hs_p` | `character(len=15)` | 239 |  |
| `hp_p` | `character(len=15)` | 240 |  |
| `microb_p` | `character(len=15)` | 241 |  |
| `lig_p` | `character(len=15)` | 242 |  |
| `nonlig_p` | `character(len=15)` | 243 |  |
| `water_p` | `character(len=15)` | 244 |  |
| `manure_p` | `character(len=15)` | 245 |  |

### output_n_p_pool_header_units

- **Defined in source**: `carbon_legacy_module.f90:249`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `freq` | `character (len=7)` | 250 |  |
| `soil_lyr` | `character (len=12)` | 251 |  |
| `soil_depth` | `character (len=12)` | 252 |  |
| `day` | `character (len=12)` | 253 |  |
| `mo` | `character (len=12)` | 254 |  |
| `day_mo` | `character (len=12)` | 255 |  |
| `yrc` | `character (len=12)` | 256 |  |
| `isd` | `character (len=12)` | 257 |  |
| `id` | `character (len=22)` | 258 |  |
| `name` | `character (len=13)` | 259 |  |
| `total_pool_n` | `character(len=15)` | 260 |  |
| `residue_n` | `character(len=15)` | 261 |  |
| `str_n` | `character(len=15)` | 262 |  |
| `meta_n` | `character(len=15)` | 263 |  |
| `hs_n` | `character(len=15)` | 264 |  |
| `hp_n` | `character(len=15)` | 265 |  |
| `microb_n` | `character(len=15)` | 266 |  |
| `lig_n` | `character(len=15)` | 267 |  |
| `nonlig_n` | `character(len=15)` | 268 |  |
| `water_n` | `character(len=15)` | 269 |  |
| `manure_n` | `character(len=15)` | 270 |  |
| `total_pool_p` | `character(len=15)` | 271 |  |
| `residue_p` | `character(len=15)` | 272 |  |
| `str_p` | `character(len=15)` | 273 |  |
| `meta_p` | `character(len=15)` | 274 |  |
| `hs_p` | `character(len=15)` | 275 |  |
| `hp_p` | `character(len=15)` | 276 |  |
| `microb_p` | `character(len=15)` | 277 |  |
| `lig_p` | `character(len=15)` | 278 |  |
| `nonlig_p` | `character(len=15)` | 279 |  |
| `water_p` | `character(len=15)` | 280 |  |
| `manure_p` | `character(len=15)` | 281 |  |

### output_carb_vars_header

- **Defined in source**: `carbon_legacy_module.f90:285`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `freq` | `character (len=7)` | 286 |  |
| `soil_lyr` | `character (len=12)` | 287 |  |
| `soil_depth` | `character (len=12)` | 288 |  |
| `day` | `character (len=12)` | 289 |  |
| `mo` | `character (len=12)` | 290 |  |
| `day_mo` | `character (len=12)` | 291 |  |
| `yrc` | `character (len=12)` | 292 |  |
| `isd` | `character (len=12)` | 293 |  |
| `id` | `character (len=22)` | 294 |  |
| `name` | `character (len=13)` | 295 |  |
| `sut` | `character(len=15)` | 296 |  |
| `tillagef` | `character(len=16)` | 297 |  |
| `bmix` | `character(len=16)` | 298 |  |
| `tillagef_biomix` | `character(len=16)` | 299 |  |
| `tillagef_tillmix` | `character(len=17)` | 300 |  |
| `till_eff` | `character(len=15)` | 301 |  |
| `cdg` | `character(len=15)` | 302 |  |
| `ox` | `character(len=15)` | 303 |  |
| `cs` | `character(len=15)` | 304 |  |
| `no3` | `character(len=15)` | 305 |  |
| `nh4` | `character(len=15)` | 306 |  |
| `resp` | `character(len=15)` | 307 |  |
| `soil_tmp` | `character(len=15)` | 308 |  |
| `emix` | `character(len=15)` | 309 |  |

### output_org_allo_header

- **Defined in source**: `carbon_legacy_module.f90:313`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `freq` | `character (len=7)` | 314 |  |
| `soil_lyr` | `character (len=12)` | 315 |  |
| `soil_depth` | `character (len=12)` | 316 |  |
| `day` | `character (len=12)` | 317 |  |
| `mo` | `character (len=12)` | 318 |  |
| `day_mo` | `character (len=12)` | 319 |  |
| `yrc` | `character (len=12)` | 320 |  |
| `isd` | `character (len=12)` | 321 |  |
| `id` | `character (len=22)` | 322 |  |
| `name` | `character (len=13)` | 323 |  |
| `asp` | `character(len=15)` | 324 |  |
| `abpt` | `character(len=15)` | 325 |  |
| `abco2` | `character(len=15)` | 326 |  |
| `a1co2` | `character(len=15)` | 327 |  |
| `asco2` | `character(len=15)` | 328 |  |
| `apco2` | `character(len=15)` | 329 |  |

### output_org_ratio_header

- **Defined in source**: `carbon_legacy_module.f90:333`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `freq` | `character (len=7)` | 334 |  |
| `soil_lyr` | `character (len=12)` | 335 |  |
| `soil_depth` | `character (len=12)` | 336 |  |
| `day` | `character (len=12)` | 337 |  |
| `mo` | `character (len=12)` | 338 |  |
| `day_mo` | `character (len=12)` | 339 |  |
| `yrc` | `character (len=12)` | 340 |  |
| `isd` | `character (len=12)` | 341 |  |
| `id` | `character (len=22)` | 342 |  |
| `name` | `character (len=13)` | 343 |  |
| `ncbm` | `character(len=15)` | 344 |  |
| `nchp` | `character(len=15)` | 345 |  |
| `nchs` | `character(len=15)` | 346 |  |

### output_org_trans_header

- **Defined in source**: `carbon_legacy_module.f90:350`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `freq` | `character (len=7)` | 351 |  |
| `soil_lyr` | `character (len=12)` | 352 |  |
| `soil_depth` | `character (len=12)` | 353 |  |
| `day` | `character (len=12)` | 354 |  |
| `mo` | `character (len=12)` | 355 |  |
| `day_mo` | `character (len=12)` | 356 |  |
| `yrc` | `character (len=12)` | 357 |  |
| `isd` | `character (len=12)` | 358 |  |
| `id` | `character (len=22)` | 359 |  |
| `name` | `character (len=13)` | 360 |  |
| `bmctp` | `character(len=15)` | 361 |  |
| `bmntp` | `character(len=15)` | 362 |  |
| `hsctp` | `character(len=15)` | 363 |  |
| `hsntp` | `character(len=15)` | 364 |  |
| `hpctp` | `character(len=15)` | 365 |  |
| `hpntp` | `character(len=15)` | 366 |  |
| `lmctp` | `character(len=15)` | 367 |  |
| `lmntp` | `character(len=15)` | 368 |  |
| `lsctp` | `character(len=15)` | 369 |  |
| `lslctp` | `character(len=15)` | 370 |  |
| `lslnctp` | `character(len=15)` | 371 |  |
| `lsntp` | `character(len=15)` | 372 |  |

### output_org_trans_header_units

- **Defined in source**: `carbon_legacy_module.f90:376`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `freq` | `character (len=7)` | 377 |  |
| `soil_lyr` | `character (len=12)` | 378 |  |
| `soil_depth` | `character (len=12)` | 379 |  |
| `day` | `character (len=12)` | 380 |  |
| `mo` | `character (len=12)` | 381 |  |
| `day_mo` | `character (len=12)` | 382 |  |
| `yrc` | `character (len=12)` | 383 |  |
| `isd` | `character (len=12)` | 384 |  |
| `id` | `character (len=22)` | 385 |  |
| `name` | `character (len=13)` | 386 |  |
| `bmctp` | `character(len=15)` | 387 |  |
| `bmntp` | `character(len=15)` | 388 |  |
| `hsctp` | `character(len=15)` | 389 |  |
| `hsntp` | `character(len=15)` | 390 |  |
| `hpctp` | `character(len=15)` | 391 |  |
| `hpntp` | `character(len=15)` | 392 |  |
| `lmctp` | `character(len=15)` | 393 |  |
| `lmntp` | `character(len=15)` | 394 |  |
| `lsctp` | `character(len=15)` | 395 |  |
| `lslctp` | `character(len=15)` | 396 |  |
| `lslnctp` | `character(len=15)` | 397 |  |
| `lsntp` | `character(len=15)` | 398 |  |

### output_endsim_soil_prop_header

- **Defined in source**: `carbon_legacy_module.f90:402`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `freq` | `character (len=7)` | 403 |  |
| `soil_name` | `character (len=20)` | 404 |  |
| `soil_lyr` | `character (len=8)` | 405 |  |
| `soil_depth` | `character (len=12)` | 406 |  |
| `day` | `character (len=12)` | 407 |  |
| `mo` | `character (len=12)` | 408 |  |
| `day_mo` | `character (len=12)` | 409 |  |
| `yrc` | `character (len=12)` | 410 |  |
| `isd` | `character (len=12)` | 411 |  |
| `id` | `character (len=22)` | 412 |  |
| `name` | `character (len=13)` | 413 |  |
| `bd` | `character(len=15)` | 414 |  |
| `awc` | `character(len=15)` | 415 |  |
| `soil_k` | `character(len=15)` | 416 |  |
| `carbon` | `character(len=15)` | 417 |  |
| `clay` | `character(len=15)` | 418 |  |
| `silt` | `character(len=15)` | 419 |  |
| `sand` | `character(len=15)` | 420 |  |
| `rock` | `character(len=15)` | 421 |  |
| `alb` | `character(len=15)` | 422 |  |
| `usle_k` | `character(len=15)` | 423 |  |
| `ec` | `character(len=15)` | 424 |  |
| `caco3` | `character(len=15)` | 425 |  |
| `ph` | `character(len=15)` | 426 |  |

### output_bsn_carb_header

- **Defined in source**: `carbon_legacy_module.f90:436`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `day` | `character (len=11)` | 437 |  |
| `yrc` | `character (len=11)` | 438 |  |
| `blnk` | `character (len=6)` | 439 |  |
| `org_soilc` | `character (len=15)` | 440 |  |
| `org_plc` | `character (len=15)` | 441 |  |
| `org_resc` | `character (len=15)` | 442 |  |

### output_bsn_carb_header_units

- **Defined in source**: `carbon_legacy_module.f90:446`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `day` | `character (len=11)` | 447 |  |
| `yrc` | `character (len=11)` | 448 |  |
| `blnk` | `character (len=6)` | 449 |  |
| `org_soilc` | `character(len=15)` | 450 |  |
| `org_plc` | `character(len=15)` | 451 |  |
| `org_resc` | `character(len=15)` | 452 |  |

## Variables Defined
### plc_hdr

- **Type**: `output_plc_header`
- **Defined in source**: `carbon_legacy_module.f90:36`

### plc_hdr_units

- **Type**: `output_plc_header_units`
- **Defined in source**: `carbon_legacy_module.f90:55`

### soil_org_flux_hdr

- **Type**: `output_soil_org_flux_header`
- **Defined in source**: `carbon_legacy_module.f90:110`

### soil_org_flux_hdr_units

- **Type**: `output_soil_org_flux_header_units`
- **Defined in source**: `carbon_legacy_module.f90:159`

### cpool_hdr

- **Type**: `output_cpool_header`
- **Defined in source**: `carbon_legacy_module.f90:185`

### cpool_units

- **Type**: `output_cpool_header_units`
- **Defined in source**: `carbon_legacy_module.f90:211`

### n_p_pool_hdr

- **Type**: `output_n_p_pool_header`
- **Defined in source**: `carbon_legacy_module.f90:247`

### n_p_pool_units

- **Type**: `output_n_p_pool_header_units`
- **Defined in source**: `carbon_legacy_module.f90:283`

### carbvars_hdr

- **Type**: `output_carb_vars_header`
- **Defined in source**: `carbon_legacy_module.f90:311`

### org_allow_hdr

- **Type**: `output_org_allo_header`
- **Defined in source**: `carbon_legacy_module.f90:331`

### org_ratio_hdr

- **Type**: `output_org_ratio_header`
- **Defined in source**: `carbon_legacy_module.f90:348`

### org_trans_hdr

- **Type**: `output_org_trans_header`
- **Defined in source**: `carbon_legacy_module.f90:374`

### org_trans_units

- **Type**: `output_org_trans_header_units`
- **Defined in source**: `carbon_legacy_module.f90:400`

### endsim_soil_prop_hdr

- **Type**: `output_endsim_soil_prop_header`
- **Defined in source**: `carbon_legacy_module.f90:428`

### bsn_carb_hdr

- **Type**: `output_bsn_carb_header`
- **Defined in source**: `carbon_legacy_module.f90:444`

### bsn_carb_hdr_units

- **Type**: `output_bsn_carb_header_units`
- **Defined in source**: `carbon_legacy_module.f90:454`

## Subroutines Defined
### carbon_legacy_open

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
