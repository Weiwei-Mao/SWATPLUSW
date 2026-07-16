---
type: module
tags:
  - swat/module
  - swat/to-read
file: output_landscape_module.f90
note_file: output_landscape_module.f90
module_name: output_landscape_module
defines_types:
  - output_waterbal
  - regional_output_waterbal
  - output_nutbal
  - regional_output_nutbal
  - output_nutcarb_cycling
  - output_losses
  - regional_output_losses
  - output_plantweather
  - regional_output_plantweather
  - output_waterbal_header
  - output_waterbal_header_units
  - output_nutbal_header
  - output_nutbal_header_units
  - output_losses_header
  - output_losses_header_units
  - output_nutcarb_cycling_header
  - output_nutbal_header_units1
  - output_carbon_header
  - output_carbon_header_units1
  - output_carb_gl_header
  - output_carb_gl_header_units
  - output_hscf_header
  - output_hscf_header_units
  - output_losses_header1
  - output_losses_header_units1
  - output_plantweather_header
  - output_plantweather_header_units
defines_vars:
  - hwbz
  - bwb_d
  - bwb_m
  - bwb_y
  - bwb_a
  - hnbz
  - bnb_d
  - bnb_m
  - bnb_y
  - bnb_a
  - hycl_z
  - hlsz
  - bls_d
  - bls_m
  - bls_y
  - bls_a
  - hpwz
  - bpw_d
  - bpw_m
  - bpw_y
  - bpw_a
  - wb_hdr
  - wb_hdr_units
  - nb_hdr
  - nb_hdr_units
  - ls_hdr
  - ls_hdr_units
  - nb_hdr1
  - nb_hdr_units1
  - carbon_hdr1
  - carbon_hdr_units1
  - carb_gl_hdr
  - carb_gl_hdr_units
  - hscf_hdr
  - hscf_hdr_units
  - ls_hdr1
  - ls_hdr_units1
  - pw_hdr
  - pw_hdr_units
  - day
  - mo
  - day_mo
  - yrc
  - isd
  - id
  - name
  - precip
  - snofall
  - snomlt
  - surq_gen
  - latq
  - wateryld
  - perc
  - et
  - ecanopy
  - eplant
  - esoil
  - surq_cont
  - cn
  - sw_init
  - sw_final
  - sw_ave
  - sw_300
  - sno_init
  - sno_final
  - snopack
  - pet
  - qtile
  - irr
  - surq_runon
  - latq_runon
  - overbank
  - surq_cha
  - surq_res
  - surq_ls
  - latq_cha
  - latq_res
  - latq_ls
  - gwsoilq
  - satex
  - satex_chan
  - sw_change
  - lagsurf
  - laglatq
  - lagsatex
  - wet_evap
  - wet_oflo
  - wet_stor
  - plt_cov
  - mgt_ops
  - grazn
  - grazp
  - lab_min_p
  - act_sta_p
  - fertn
  - fertp
  - fixn
  - denit
  - act_nit_n
  - act_sta_n
  - org_lab_p
  - rsd_nitorg_n
  - rsd_laborg_p
  - no3atmo
  - nh4atmo
  - nuptake
  - puptake
  - gwsoiln
  - gwsoilp
  - sedyld
  - sedorgn
  - sedorgp
  - surqno3
  - latno3
  - surqsolp
  - usle
  - sedminp
  - tileno3
  - lchlabp
  - tilelabp
  - satexn
  - percn
  - sedmin
  - rsd_hs_c
  - sed_c
  - surq_c
  - surq_doc
  - surq_dic
  - latq_c
  - latq_doc
  - latq_dic
  - perc_c
  - perc_doc
  - perc_dic
  - npp_c
  - rsd_c
  - grain_c
  - stover_c
  - rsp_c
  - emit_c
  - res_decay
  - man_app_c
  - man_graze_c
  - soil_emit_c
  - plant_surf_c
  - plant_root_c
  - rsd_surfdecay_c
  - rsd_rootdecay_c
  - harv_stov_c
  - rsd_emit_c
  - harv_abgr_c
  - harv_root_c
  - drop_c
  - grazeat_c
  - plant_emit_c
  - meta_micr
  - str_micr
  - str_hs
  - co2_meta
  - co2_str
  - micr_hs
  - micr_hp
  - hs_micr
  - hs_hp
  - hp_micr
  - co2_micr
  - co2_hs
  - co2_hp
  - sedorgc
  - manurec
  - manuren
  - manurep
  - fertc
  - grazc_eat
  - gracn_eat
  - gracp_eat
  - grazc_man
  - gracn_man
  - gracp_man
  - yieldc
  - yieldn
  - yieldp
  - lai
  - bioms
  - yield
  - residue
  - sol_tmp
  - strsw
  - strsa
  - strstmp
  - strsn
  - strsp
  - strss
  - nplnt
  - pplnt
  - tmx
  - tmn
  - tmpav
  - solrad
  - wndspd
  - rhum
  - phubase0
  - lai_max
  - bm_max
  - bm_grow
  - c_gro
purpose: ""
---

# output_landscape_module

> [!info] Module
> Defines derived types and module-level variables.

## Defined Types
| Type | Notes |
|---|---|
| `output_waterbal` |  |
| `regional_output_waterbal` |  |
| `output_nutbal` |  |
| `regional_output_nutbal` |  |
| `output_nutcarb_cycling` |  |
| `output_losses` |  |
| `regional_output_losses` |  |
| `output_plantweather` |  |
| `regional_output_plantweather` |  |
| `output_waterbal_header` |  |
| `output_waterbal_header_units` |  |
| `output_nutbal_header` |  |
| `output_nutbal_header_units` |  |
| `output_losses_header` |  |
| `output_losses_header_units` |  |
| `output_nutcarb_cycling_header` |  |
| `output_nutbal_header_units1` |  |
| `output_carbon_header` |  |
| `output_carbon_header_units1` |  |
| `output_carb_gl_header` |  |
| `output_carb_gl_header_units` |  |
| `output_hscf_header` |  |
| `output_hscf_header_units` |  |
| `output_losses_header1` |  |
| `output_losses_header_units1` |  |
| `output_plantweather_header` |  |
| `output_plantweather_header_units` |  |

## Module-Level Variables
| Variable | Type | Meaning |
|---|---|---|
| `hwbz` |  |  |
| `bwb_d` |  |  |
| `bwb_m` |  |  |
| `bwb_y` |  |  |
| `bwb_a` |  |  |
| `hnbz` |  |  |
| `bnb_d` |  |  |
| `bnb_m` |  |  |
| `bnb_y` |  |  |
| `bnb_a` |  |  |
| `hycl_z` |  |  |
| `hlsz` |  |  |
| `bls_d` |  |  |
| `bls_m` |  |  |
| `bls_y` |  |  |
| `bls_a` |  |  |
| `hpwz` |  |  |
| `bpw_d` |  |  |
| `bpw_m` |  |  |
| `bpw_y` |  |  |
| `bpw_a` |  |  |
| `wb_hdr` |  |  |
| `wb_hdr_units` |  |  |
| `nb_hdr` |  |  |
| `nb_hdr_units` |  |  |
| `ls_hdr` |  |  |
| `ls_hdr_units` |  |  |
| `nb_hdr1` |  |  |
| `nb_hdr_units1` |  |  |
| `carbon_hdr1` |  |  |
| `carbon_hdr_units1` |  |  |
| `carb_gl_hdr` |  |  |
| `carb_gl_hdr_units` |  |  |
| `hscf_hdr` |  |  |
| `hscf_hdr_units` |  |  |
| `ls_hdr1` |  |  |
| `ls_hdr_units1` |  |  |
| `pw_hdr` |  |  |
| `pw_hdr_units` |  |  |
| `day` |  |  |

*(Showing first 40 of 206 variables.)*

## Used By Source Routines

```dataview
LIST file.link
WHERE type = "source" AND contains(module, this.module_name)
```

<!-- USER-NOTES-START -->
## Notes
Use this section for type and variable meanings, units, and allowed values. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
