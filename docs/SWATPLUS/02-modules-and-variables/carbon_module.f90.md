---
type: module
tags:
  - swat/module
  - swat/to-read
file: carbon_module.f90
note_file: carbon_module.f90
module_name: carbon_module
defines_types:
  - carbon_inputs
  - manure_coef
  - organic_allocations
  - organic_controls
  - organic_fractions
  - organic_ratio
  - carbon_water_coef
  - organic_transformations
  - organic_flux
  - carbon_soil_transformations
  - carbon_soil_gain_losses
  - carbon_residue_gain_losses
  - carbon_plant_gain_losses
defines_vars:
  - cbn_diagnostics
  - n_act_frac
  - cnr_cap
  - cnr_ref
  - cpr_cap
  - cpr_ref
  - cb_n_layers
  - cb_n_layers_explicit
  - cb_lyr_missing
  - cpool_vars
  - n_p_pool_vars
  - cflux_vars
  - carb_drv_vars
  - carb_dyn_vars
  - soil_snap_vars
  - carbdb
  - carbz
  - man_coef
  - org_allo
  - org_alloz
  - org_con
  - org_frac
  - org_ratio
  - org_ratio_zero
  - cb_wtr_coef
  - org_tran
  - org_tran_zero
  - org_flux
  - org_flux_zero
  - hscfz
  - hscf_d
  - hscf_m
  - hscf_y
  - hscf_a
  - lscf_d
  - lscf_m
  - lscf_y
  - lscf_a
  - lcsf_a
  - bscf_d
  - bscf_m
  - bscf_y
  - bscf_a
  - hscz
  - hsc_d
  - hsc_m
  - hsc_y
  - hsc_a
  - lsc_d
  - lsc_m
  - lsc_y
  - lsc_a
  - bsc_d
  - bsc_m
  - bsc_y
  - bsc_a
  - hrcz
  - hrc_d
  - hrc_m
  - hrc_y
  - hrc_a
  - lrc_d
  - lrc_m
  - lrc_y
  - lrc_a
  - brc_d
  - brc_m
  - brc_y
  - brc_a
  - hpcz
  - hpc_d
  - hpc_m
  - hpc_y
  - hpc_a
  - lpc_d
  - lpc_m
  - lpc_y
  - lpc_a
  - bpc_d
  - bpc_m
  - bpc_y
  - bpc_a
defines_subroutines:
  - cb_write_flat_header
  - cb_write_wide_header
  - cb_write_cbn_lyr_header
  - cb_write_depth_row
  - cb_write_var_block
defines_functions:
  - carbon_soil_flux__add
  - carbon_soil_flux_mult
  - carbon_soil_flux_div
  - carbon_soil_gl__add
  - carbon_soil_gl_mult
  - carbon_soil_gl_div
  - carbon_residue_gl__add
  - carbon_residue_gl_mult
  - carbon_residue_gl_div
  - carbon_plant_gl__add
  - carbon_plant_gl_mult
  - carbon_plant_gl_div
defines_procedures:
  - cb_write_flat_header
  - cb_write_wide_header
  - cb_write_cbn_lyr_header
  - cb_write_depth_row
  - cb_write_var_block
  - carbon_soil_flux__add
  - carbon_soil_flux_mult
  - carbon_soil_flux_div
  - carbon_soil_gl__add
  - carbon_soil_gl_mult
  - carbon_soil_gl_div
  - carbon_residue_gl__add
  - carbon_residue_gl_mult
  - carbon_residue_gl_div
  - carbon_plant_gl__add
  - carbon_plant_gl_mult
  - carbon_plant_gl_div
purpose: ""
---

# carbon_module

> [!info] Module
> Defines derived types and module-level variables.

## Defined Types
### carbon_inputs

- **Defined in source**: `carbon_module.f90:63`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `hp_rate` | `real` | 64 | \|rate of transformation of passive humus under optimal conditions |
| `hs_rate` | `real` | 65 | \|rate of transformation of slow humus under optimal conditions |
| `microb_rate` | `real` | 66 | \|rate of transformation of microbial biomass and associated products under optimal conditions |
| `meta_rate` | `real` | 67 | \|rate of transformation of metabolic litter under optimal conditions |
| `str_rate` | `real` | 68 | \|rate of potential transformation of structural litter under optimal conditions |
| `microb_top_rate` | `real` | 69 | \|coef adjusts mocribial activity function in top soil layer |
| `hs_hp` | `real` | 70 | \|coef in century eq allocating slow to passive humus |
| `microb_koc` | `real` | 71 | 10^3 m^3 Mg-1 \|liquid-solid partition coefficient for microbial biomass |
| `min_n_frac` | `real` | 72 | \|fraction of mineral n sorbed to litter |
| `c_org_frac` | `real` | 73 | \|carbon fraction of organic materials |

### manure_coef

- **Defined in source**: `carbon_module.f90:78`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `rtof` | `real` | 79 | none \|weighting factor used to partition the organic N & P concentration of septic effluent between the fresh organic and the stable organic pools |
| `man_to_c` | `real` | 82 | \|conversion of manure solids to carbon |

### organic_allocations

- **Defined in source**: `carbon_module.f90:86`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `abp` | `real` | 88 | \|Fraction of decomposed microbial biomass allocated to passive humus |
| `asp` | `real` | 89 | \|Fraction of decomposed slow humus allocated to passive |
| `a1co2` | `real` | 93 | \|Fraction of decomposed metabolic and passive pools to CO2 |
| `asco2` | `real` | 94 | \|Fraction of decomposed slow humus allocated to CO2 |
| `apco2` | `real` | 95 | \|Fraction of decomposed passive humus allocated to CO2 |
| `abco2` | `real` | 96 | \|Fraction of decomposed microbial biomass allocated to CO2 |

### organic_controls

- **Defined in source**: `carbon_module.f90:101`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `sut` | `real` | 102 | \|soil water control on biological processes |
| `cdg` | `real` | 103 | \|soil temperature control on biological processes |
| `cs` | `real` | 104 | \|combined factor controlling biological processes |
| `ox` | `real` | 105 | \|oxygen control on biological processes |
| `till_eff` | `real` | 106 | \|tillage effect |
| `x1` | `real` | 107 | \|tillage control on residue decomposition |
| `no3` | `real` | 108 | \|no3 as adjusted in cbn_zhang2 |
| `nh4` | `real` | 109 | \|nh4 as adjusted in cbn_zhang2 |
| `resp` | `real` | 110 | \|co2 respiration The following three parameters resolve the shape of the temperature effect equation: |
| `tn` | `real` | 114 | celsius \|minimum temperature bound |
| `top` | `real` | 115 | celsius \|peak (optimum) temperature |
| `tx` | `real` | 116 | celsius \|maximum temperature bound |
| `tmpf` | `integer` | 117 | \|temperature factor approach used in cbn_zhang2 |
| `watf` | `integer` | 118 | \|water factor approach used in cbn_zhang2 |

### organic_fractions

- **Defined in source**: `carbon_module.f90:122`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `lmf` | `real` | 123 | frac \|fraction of the litter that is metabolic |
| `lmnf` | `real` | 124 | kg kg-1 \|fraction of metabolic litter that is N |
| `lsf` | `real` | 125 | frac \|fraction of the litter that is structural |
| `lslf` | `real` | 126 | kg kg-1 \|fraction of structural litter that is lignin |
| `lsnf` | `real` | 127 | kg kg-1 \|fraction of structural litter that is N |
| `frac_seq` | `real` | 128 | \|fraction of total carbon the is sequestered carbon when initializing sequestered pools |
| `frac_not_seq` | `real` | 129 | \|fraction of total carbon the is NOT sequestered carbon when initializing non-sequestered pools |
| `frac_hum_microb` | `real` | 130 | !fraction of carbon that is microbrial pool when initializing microbrial pools |
| `frac_hum_slow` | `real` | 131 | !fraction of carbon that is humas slow pool when initializing humus slow pools |
| `frac_hum_passive` | `real` | 132 | \|fraction of carbon that is humas passive pool when initializing humas passive pools |
| `mathers_method` | `logical` | 133 | !logical indicating whether to use the mathers_method to initialize humus slow pools |

### organic_ratio

- **Defined in source**: `carbon_module.f90:137`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `ncbm` | `real` | 139 | \|n/c ratio of biomass |
| `nchp` | `real` | 140 | \|n/c ratio of passive humus |
| `nchs` | `real` | 141 | \|n/c ration of slow humus |

### carbon_water_coef

- **Defined in source**: `carbon_module.f90:146`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `prmt_21` | `real` | 147 | \|KOC FOR CARBON LOSS IN WATER AND SEDIMENT(500._1500.) KD = KOC * C |
| `prmt_44` | `real` | 148 | \|RATIO OF SOLUBLE C CONCENTRATION IN RUNOFF TO PERCOLATE(0.1_1.) |

### organic_transformations

- **Defined in source**: `carbon_module.f90:152`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `bmctp` | `real` | 153 | kg ha-1 day-1 \|potential transformation of C in microbial biomass |
| `bmntp` | `real` | 154 | kg ha-1 day-1 \|potential transformation of N in microbial biomass |
| `hsctp` | `real` | 155 | kg ha-1 day-1 \|potential transformation of C in slow humus |
| `hsntp` | `real` | 156 | kg ha-1 day-1 \|potential transformation of N in slow humus |
| `hpctp` | `real` | 157 | kg ha-1 day-1 \|potential transformation of C in passive humus |
| `hpntp` | `real` | 158 | kg ha-1 day-1 \|potential transformation of N in passive humus |
| `lmctp` | `real` | 159 | kg ha-1 day-1 \|potential transformation of C in metabolic litter |
| `lmntp` | `real` | 160 | kg ha-1 day-1 \|potential transformation of N in metabolic litter |
| `lsctp` | `real` | 161 | kg ha-1 day-1 \|potential transformation of C in structural litter |
| `lslctp` | `real` | 162 | kg ha-1 day-1 \|potential transformation of C in lignin of structural litter |
| `lslnctp` | `real` | 163 | kg ha-1 day-1 \|potential transformation of C in nonlignin structural litter |
| `lsntp` | `real` | 164 | kg ha-1 day-1 \|potential transformation of N in structural litter |

### organic_flux

- **Defined in source**: `carbon_module.f90:169`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `cfmets1` | `real` | 170 | (kg C ha-1 day-1) \|C transformed from Metabolic Litter to S1 (Microbial Biomass) |
| `cfstrs1` | `real` | 171 | (kg C ha-1 day-1) \|C transformed from Structural Litter to S1 (Microbial Biomass) |
| `cfstrs2` | `real` | 172 | (kg C ha-1 day-1) \|C transformed from Structural Litter to S2 (Slow Humus) |
| `efmets1` | `real` | 173 | (kg N ha-1 day-1) \|N transformed from Metabolic Litter to S1 (Microbial Biomass) |
| `efstrs1` | `real` | 174 | (kg N ha-1 day-1) \|N transformed from Structural Litter to S1 (Microbial Biomass) |
| `efstrs2` | `real` | 175 | (kg N ha-1 day-1) \|N transformed from Structural Litter to S2 (Slow Humus) |
| `immmets1` | `real` | 176 | (kg N ha-1 day-1) \|N immibolization resulting from transforming Metabolic Litter to S1 (Microbial Biomass) |
| `immstrs1` | `real` | 177 | (kg N ha-1 day-1) \|N immibolization resulting from transforming Structural Litter to S1 (Microbial Biomass) |
| `immstrs2` | `real` | 178 | (kg N ha-1 day-1) \|N immibolization resulting from transforming Structural Litter to S2 (Slow Humus) |
| `mnrmets1` | `real` | 179 | (kg N ha-1 day-1) \|N mineralization resulting from transforming Metabolic Litter to S1 (Microbial Biomass) |
| `mnrstrs1` | `real` | 180 | (kg N ha-1 day-1) \|N mineralization resulting from transforming Structural Litter to S1 (Microbial Biomass) |
| `mnrstrs2` | `real` | 181 | (kg N ha-1 day-1) \|N mineralization resulting from transforming Structural Litter to S2 (Slow Humus) |
| `co2fmet` | `real` | 182 | (kg C ha-1 day-1) \|CO2 production resulting from metabolic litter transformaitons |
| `co2fstr` | `real` | 183 | (kg C ha-1 day-1) \|CO2 production resulting from lignin structural litter transformaitons |
| `cfs1s2` | `real` | 184 | (kg C ha-1 day-1) \|C transformed from S1 (Microbial Biomass) to S2 (Slow Humus) |
| `cfs1s3` | `real` | 185 | (kg C ha-1 day-1) \|C transformed from S1 (Microbial Biomass) to S3 (Passive Humus) |
| `cfs2s1` | `real` | 186 | (kg C ha-1 day-1) \|C transformed from S2 (Slow Humus) to S1 (Microbial Biomass) |
| `cfs2s3` | `real` | 187 | (kg C ha-1 day-1) \|C transformed from S2 (Slow Humus) to S3 (Passive Humus) |
| `cfs3s1` | `real` | 188 | (kg C ha-1 day-1) \|C transformed from S3 (Passive Humus) to S1 (Microbial Biomass) |
| `efs1s2` | `real` | 189 | (kg N ha-1 day-1) \|N transformed from from S1 (Microbial Biomass) to S2 (Slow Humus) |
| `efs1s3` | `real` | 190 | (kg N ha-1 day-1) \|N transformed from from S1 (Microbial Biomass) to S3 (Passive Humus) |
| `efs2s1` | `real` | 191 | (kg N ha-1 day-1) \|N transformed from from S2 (Slow Humus) to S1 (Microbial Biomass) |
| `efs2s3` | `real` | 192 | (kg N ha-1 day-1) \|N transformed from from S2 (Slow Humus) to S3 (Passive Humus) |
| `efs3s1` | `real` | 193 | (kg N ha-1 day-1) \|N transformed from from S3 (Passive Humus) to S1 (Microbial Biomass) |
| `imms1s2` | `real` | 194 | (kg N ha-1 day-1) \|N immibolization resulting from transforming S1 (Microbial Biomass) to S2 (Slow Humus) |
| `imms1s3` | `real` | 195 | (kg N ha-1 day-1) \|N immibolization resulting from transforming S1 (Microbial Biomass) to S3 (Passive Humus) |
| `imms2s1` | `real` | 196 | (kg N ha-1 day-1) \|N immibolization resulting from transforming S2 (Slow Humus) to S1 (Microbial Biomass) |
| `imms2s3` | `real` | 197 | (kg N ha-1 day-1) \|N immibolization resulting from transforming S2 (Slow Humus) to S3 (Passive Humus) |
| `imms3s1` | `real` | 198 | (kg N ha-1 day-1) \|N immibolization resulting from transforming S3 (Passive Humus) to S1 (Microbial Biomass) |
| `mnrs1s2` | `real` | 199 | (kg N ha-1 day-1) \|N mineralization resulting from transforming S1 (Microbial Biomass) to S2 (Slow Humus) |
| `mnrs1s3` | `real` | 200 | (kg N ha-1 day-1) \|N mineralization resulting from transforming S1 (Microbial Biomass) to S3 (Passive Humus) |
| `mnrs2s1` | `real` | 201 | (kg N ha-1 day-1) \|N mineralization resulting from transforming S2 (Slow Humus) to S1 (Microbial Biomass) |
| `mnrs2s3` | `real` | 202 | (kg N ha-1 day-1) \|N mineralization resulting from transforming S2 (Slow Humus) to S3 (Passive Humus) |
| `mnrs3s1` | `real` | 203 | (kg N ha-1 day-1) \|N mineralization resulting from transforming S3 (Passive Humus) to S1 (Microbial Biomass) |
| `co2fs1` | `real` | 204 | (kg C ha-1 day-1) \|CO2 production resulting from S1 (Microbial Biomass) transformations |
| `co2fs2` | `real` | 205 | (kg C ha-1 day-1) \|CO2 production resulting from S2 (Slow Humus) transformations |
| `co2fs3` | `real` | 206 | (kg C ha-1 day-1) \|CO2 production resulting from S3 (Passive Humus) transformations |

### carbon_soil_transformations

- **Defined in source**: `carbon_module.f90:211`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `meta_micr` | `real` | 212 | (kg C ha-1 day-1) \|C transformed from Metabolic Litter to S1 (Microbial Biomass) |
| `str_micr` | `real` | 213 | (kg C ha-1 day-1) \|C transformed from Structural Litter to S1 (Microbial Biomass) |
| `str_hs` | `real` | 214 | (kg C ha-1 day-1) \|C transformed from Structural Litter to S2 (Slow Humus) |
| `co2_meta` | `real` | 215 | (kg C ha-1 day-1) \|CO2 production resulting from metabolic litter transformations |
| `co2_str` | `real` | 216 | (kg C ha-1 day-1) \|CO2 production resulting from lignin structural litter transformations |
| `micr_hs` | `real` | 217 | (kg C ha-1 day-1) \|C transformed from S1 (Microbial Biomass) to S2 (Slow Humus) |
| `micr_hp` | `real` | 218 | (kg C ha-1 day-1) \|C transformed from S1 (Microbial Biomass) to S3 (Passive Humus) |
| `hs_micr` | `real` | 219 | (kg C ha-1 day-1) \|C transformed from S2 (Slow Humus) to S1 (Microbial Biomass) |
| `hs_hp` | `real` | 220 | (kg C ha-1 day-1) \|C transformed from S2 (Slow Humus) to S3 (Passive Humus) |
| `hp_micr` | `real` | 221 | (kg C ha-1 day-1) \|C transformed from S3 (Passive Humus) to S1 (Microbial Biomass) |
| `co2_micr` | `real` | 222 | (kg C ha-1 day-1) \|CO2 production resulting from S1 (Microbial Biomass) transformations |
| `co2_hs` | `real` | 223 | (kg C ha-1 day-1) \|CO2 production resulting from S2 (Slow Humus) transformations |
| `co2_hp` | `real` | 224 | (kg C ha-1 day-1) \|CO2 production resulting from S3 (Passive Humus) transformations |

### carbon_soil_gain_losses

- **Defined in source**: `carbon_module.f90:245`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `sed_c` | `real` | 246 | kg C/ha \|C transported with sediment yield |
| `surq_c` | `real` | 247 | kg C/ha \|total dissolved C transported with surface runoff |
| `latq_c` | `real` | 248 | kg C/ha \|dissolved organic C transported with lateral flow (all layers) |
| `perc_c` | `real` | 249 | kg C/ha \|total dissolved C transported with percolate |
| `rsd_decay_c` | `real` | 250 | kg C/ha \|carbon added to soil from residue decay |
| `man_app_c` | `real` | 251 | kg C/ha \|amount of carbon applied to soil from manure |
| `man_graz_c` | `real` | 252 | kg C/ha \|amount of carbon manure from grazing animals |
| `rsp_c` | `real` | 253 | kg C/ha \|CO2 production from soil respiration summarized for the profile |
| `emit_c` | `real` | 254 | kg C/ha \|CO2 production from burning soil carbon |

### carbon_residue_gain_losses

- **Defined in source**: `carbon_module.f90:274`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `plant_surf_c` | `real` | 275 | kg C/ha \|carbon added to surface residue from leaf drop and kill |
| `plant_root_c` | `real` | 276 | kg C/ha \|carbon added to soil residue from root kill |
| `rsd_surfdecay_c` | `real` | 277 | kg C/ha \|carbon lost to soil from surface residue decay |
| `rsd_rootdecay_c` | `real` | 278 | kg C/ha \|carbon lost to soil from soil/root and incorporated residue decay |
| `harv_stov_c` | `real` | 279 | kg C/ha \|carbon removed during surface residue harvest |
| `emit_c` | `real` | 280 | kg C/ha \|CO2 production from burning surface residue carbon |

### carbon_plant_gain_losses

- **Defined in source**: `carbon_module.f90:300`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `npp_c` | `real` | 301 | kg C/ha \|plant carbon growth from photosynthesis |
| `harv_abgr_c` | `real` | 302 | kg C/ha \|carbon removed during grain/biomass harvest |
| `harv_root_c` | `real` | 303 | kg C/ha \|carbon removed during tuber (root) harvest |
| `drop_c` | `real` | 304 | kg C/ha \|carbon added to residue from leaf drop and kill |
| `grazeat_c` | `real` | 305 | kg C/ha \|amount of carbon ate by animals in grazing |
| `emit_c` | `real` | 306 | kg C/ha \|CO2 production from burning residue carbon |

## Variables Defined
### cbn_diagnostics

- **Type**: `logical`
- **Defined in source**: `carbon_module.f90:10`
- **Source note**: turns on the legacy plc/cflux/cpool and soil-prop files

### n_act_frac

- **Type**: `real`
- **Defined in source**: `carbon_module.f90:13`
- **Source note**: frac    |fraction of organic N in the active humus pool (used in nut_nminrl active to stable flow)

### cnr_cap

- **Type**: `real`
- **Defined in source**: `carbon_module.f90:14`
- **Source note**: none    |upper cap on residue C:N ratio before computing decomp factor

### cnr_ref

- **Type**: `real`
- **Defined in source**: `carbon_module.f90:15`
- **Source note**: none    |reference C:N ratio where decomp factor equals 1

### cpr_cap

- **Type**: `real`
- **Defined in source**: `carbon_module.f90:16`
- **Source note**: none    |upper cap on residue C:P ratio before computing decomp factor

### cpr_ref

- **Type**: `real`
- **Defined in source**: `carbon_module.f90:17`
- **Source note**: none    |reference C:P ratio where decomp factor equals 1

### cb_n_layers

- **Type**: `integer`
- **Defined in source**: `carbon_module.f90:23`

### cb_n_layers_explicit

- **Type**: `logical`
- **Defined in source**: `carbon_module.f90:24`
- **Source note**: .true. when carbon_layers.prt set the count

### cb_lyr_missing

- **Type**: `real, parameter`
- **Defined in source**: `carbon_module.f90:25`
- **Source note**: sentinel written when a soil has fewer layers than cb_n_layers

### cpool_vars

- **Type**: `character(len=16), parameter`
- **Defined in source**: `carbon_module.f90:29`

### n_p_pool_vars

- **Type**: `character(len=16), parameter`
- **Defined in source**: `carbon_module.f90:33`

### cflux_vars

- **Type**: `character(len=16), parameter`
- **Defined in source**: `carbon_module.f90:39`

### carb_drv_vars

- **Type**: `character(len=16), parameter`
- **Defined in source**: `carbon_module.f90:49`

### carb_dyn_vars

- **Type**: `character(len=16), parameter`
- **Defined in source**: `carbon_module.f90:53`

### soil_snap_vars

- **Type**: `character(len=16), parameter`
- **Defined in source**: `carbon_module.f90:59`

### carbdb

- **Type**: `carbon_inputs`
- **Defined in source**: `carbon_module.f90:75`

### carbz

- **Type**: `carbon_inputs`
- **Defined in source**: `carbon_module.f90:76`

### man_coef

- **Type**: `manure_coef`
- **Defined in source**: `carbon_module.f90:84`

### org_allo

- **Type**: `organic_allocations`
- **Defined in source**: `carbon_module.f90:98`

### org_alloz

- **Type**: `organic_allocations`
- **Defined in source**: `carbon_module.f90:99`

### org_con

- **Type**: `organic_controls`
- **Defined in source**: `carbon_module.f90:120`

### org_frac

- **Type**: `organic_fractions`
- **Defined in source**: `carbon_module.f90:135`

### org_ratio

- **Type**: `organic_ratio`
- **Defined in source**: `carbon_module.f90:143`

### org_ratio_zero

- **Type**: `organic_ratio`
- **Defined in source**: `carbon_module.f90:144`

### cb_wtr_coef

- **Type**: `carbon_water_coef`
- **Defined in source**: `carbon_module.f90:150`

### org_tran

- **Type**: `organic_transformations`
- **Defined in source**: `carbon_module.f90:166`

### org_tran_zero

- **Type**: `organic_transformations`
- **Defined in source**: `carbon_module.f90:167`

### org_flux

- **Type**: `organic_flux`
- **Defined in source**: `carbon_module.f90:208`

### org_flux_zero

- **Type**: `organic_flux`
- **Defined in source**: `carbon_module.f90:209`

### hscfz

- **Type**: `carbon_soil_transformations`
- **Defined in source**: `carbon_module.f90:226`

### hscf_d

- **Type**: `carbon_soil_transformations`
- **Defined in source**: `carbon_module.f90:229`

### hscf_m

- **Type**: `carbon_soil_transformations`
- **Defined in source**: `carbon_module.f90:230`

### hscf_y

- **Type**: `carbon_soil_transformations`
- **Defined in source**: `carbon_module.f90:231`

### hscf_a

- **Type**: `carbon_soil_transformations`
- **Defined in source**: `carbon_module.f90:232`

### lscf_d

- **Type**: `carbon_soil_transformations`
- **Defined in source**: `carbon_module.f90:234`

### lscf_m

- **Type**: `carbon_soil_transformations`
- **Defined in source**: `carbon_module.f90:235`

### lscf_y

- **Type**: `carbon_soil_transformations`
- **Defined in source**: `carbon_module.f90:236`

### lscf_a

- **Type**: `carbon_soil_transformations`
- **Defined in source**: `carbon_module.f90:237`

### lcsf_a

- **Type**: `carbon_soil_transformations`
- **Defined in source**: `carbon_module.f90:238`

### bscf_d

- **Type**: `carbon_soil_transformations`
- **Defined in source**: `carbon_module.f90:240`

### bscf_m

- **Type**: `carbon_soil_transformations`
- **Defined in source**: `carbon_module.f90:241`

### bscf_y

- **Type**: `carbon_soil_transformations`
- **Defined in source**: `carbon_module.f90:242`

### bscf_a

- **Type**: `carbon_soil_transformations`
- **Defined in source**: `carbon_module.f90:243`

### hscz

- **Type**: `carbon_soil_gain_losses`
- **Defined in source**: `carbon_module.f90:256`

### hsc_d

- **Type**: `carbon_soil_gain_losses`
- **Defined in source**: `carbon_module.f90:259`

### hsc_m

- **Type**: `carbon_soil_gain_losses`
- **Defined in source**: `carbon_module.f90:260`

### hsc_y

- **Type**: `carbon_soil_gain_losses`
- **Defined in source**: `carbon_module.f90:261`

### hsc_a

- **Type**: `carbon_soil_gain_losses`
- **Defined in source**: `carbon_module.f90:262`

### lsc_d

- **Type**: `carbon_soil_gain_losses`
- **Defined in source**: `carbon_module.f90:264`

### lsc_m

- **Type**: `carbon_soil_gain_losses`
- **Defined in source**: `carbon_module.f90:265`

### lsc_y

- **Type**: `carbon_soil_gain_losses`
- **Defined in source**: `carbon_module.f90:266`

### lsc_a

- **Type**: `carbon_soil_gain_losses`
- **Defined in source**: `carbon_module.f90:267`

### bsc_d

- **Type**: `carbon_soil_gain_losses`
- **Defined in source**: `carbon_module.f90:269`

### bsc_m

- **Type**: `carbon_soil_gain_losses`
- **Defined in source**: `carbon_module.f90:270`

### bsc_y

- **Type**: `carbon_soil_gain_losses`
- **Defined in source**: `carbon_module.f90:271`

### bsc_a

- **Type**: `carbon_soil_gain_losses`
- **Defined in source**: `carbon_module.f90:272`

### hrcz

- **Type**: `carbon_residue_gain_losses`
- **Defined in source**: `carbon_module.f90:282`

### hrc_d

- **Type**: `carbon_residue_gain_losses`
- **Defined in source**: `carbon_module.f90:285`

### hrc_m

- **Type**: `carbon_residue_gain_losses`
- **Defined in source**: `carbon_module.f90:286`

### hrc_y

- **Type**: `carbon_residue_gain_losses`
- **Defined in source**: `carbon_module.f90:287`

### hrc_a

- **Type**: `carbon_residue_gain_losses`
- **Defined in source**: `carbon_module.f90:288`

### lrc_d

- **Type**: `carbon_residue_gain_losses`
- **Defined in source**: `carbon_module.f90:290`

### lrc_m

- **Type**: `carbon_residue_gain_losses`
- **Defined in source**: `carbon_module.f90:291`

### lrc_y

- **Type**: `carbon_residue_gain_losses`
- **Defined in source**: `carbon_module.f90:292`

### lrc_a

- **Type**: `carbon_residue_gain_losses`
- **Defined in source**: `carbon_module.f90:293`

### brc_d

- **Type**: `carbon_residue_gain_losses`
- **Defined in source**: `carbon_module.f90:295`

### brc_m

- **Type**: `carbon_residue_gain_losses`
- **Defined in source**: `carbon_module.f90:296`

### brc_y

- **Type**: `carbon_residue_gain_losses`
- **Defined in source**: `carbon_module.f90:297`

### brc_a

- **Type**: `carbon_residue_gain_losses`
- **Defined in source**: `carbon_module.f90:298`

### hpcz

- **Type**: `carbon_plant_gain_losses`
- **Defined in source**: `carbon_module.f90:308`

### hpc_d

- **Type**: `carbon_plant_gain_losses`
- **Defined in source**: `carbon_module.f90:311`

### hpc_m

- **Type**: `carbon_plant_gain_losses`
- **Defined in source**: `carbon_module.f90:312`

### hpc_y

- **Type**: `carbon_plant_gain_losses`
- **Defined in source**: `carbon_module.f90:313`

### hpc_a

- **Type**: `carbon_plant_gain_losses`
- **Defined in source**: `carbon_module.f90:314`

### lpc_d

- **Type**: `carbon_plant_gain_losses`
- **Defined in source**: `carbon_module.f90:316`

### lpc_m

- **Type**: `carbon_plant_gain_losses`
- **Defined in source**: `carbon_module.f90:317`

### lpc_y

- **Type**: `carbon_plant_gain_losses`
- **Defined in source**: `carbon_module.f90:318`

### lpc_a

- **Type**: `carbon_plant_gain_losses`
- **Defined in source**: `carbon_module.f90:319`

### bpc_d

- **Type**: `carbon_plant_gain_losses`
- **Defined in source**: `carbon_module.f90:321`

### bpc_m

- **Type**: `carbon_plant_gain_losses`
- **Defined in source**: `carbon_module.f90:322`

### bpc_y

- **Type**: `carbon_plant_gain_losses`
- **Defined in source**: `carbon_module.f90:323`

### bpc_a

- **Type**: `carbon_plant_gain_losses`
- **Defined in source**: `carbon_module.f90:324`

## Subroutines Defined
### cb_write_flat_header

### cb_write_wide_header

### cb_write_cbn_lyr_header

### cb_write_depth_row

### cb_write_var_block

## Functions Defined
### carbon_soil_flux__add

### carbon_soil_flux_mult

### carbon_soil_flux_div

### carbon_soil_gl__add

### carbon_soil_gl_mult

### carbon_soil_gl_div

### carbon_residue_gl__add

### carbon_residue_gl_mult

### carbon_residue_gl_div

### carbon_plant_gl__add

### carbon_plant_gl_mult

### carbon_plant_gl_div

## Used By Source Routines

```dataview
LIST file.link
WHERE type = "source" AND contains(module, this.module_name)
```

<!-- USER-NOTES-START -->
## Notes
Use this section for type and variable meanings, units, and allowed values. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
