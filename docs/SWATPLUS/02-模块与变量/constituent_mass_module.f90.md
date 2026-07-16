---
type: module
tags:
  - swat/模块
  - swat/待读
file: constituent_mass_module.f90
module_name: constituent_mass_module
defines_types:
  - constituents
  - exco_pesticide
  - dr_pesticide
  - exco_pathogens
  - dr_pathogens
  - exco_heavy_metals
  - dr_heavy_metals
  - exco_salts
  - dr_salts
  - salt_solids_soil
  - constituent_mass
  - soil_constituent_mass
  - plant_constituent_mass
  - all_constituent_hydrograph
  - gw_load_hydrograph
  - recall_salt_inputs
  - recall_cs_inputs
  - recall_pesticide_inputs
  - cs_soil_init_concentrations
  - salt_aqu_init_concentrations
  - cs_aqu_init_concentrations
  - salt_cha_init_concentrations
  - cs_cha_init_concentrations
  - cs_water_init_concentrations
  - cs_irrigation_concentrations
  - output_rusaltb_header
  - output_rucsb_header
  - constituents_header_in
  - constituents_header_out
  - sol_sor
defines_vars:
  - cs_db
  - wdraw_cs
  - wdraw_cs_tot
  - outflo_cs
  - hcs1
  - hcs2
  - hcs3
  - hin_csz
  - hcsz
  - rusaltb_hdr
  - rucsb_hdr
  - csin_hyd_hdr
  - csout_hyd_hdr
  - name
  - filename
  - day
  - mo
  - day_mo
  - yrc
  - isd
  - id
  - so4tot
  - castot
  - mgstot
  - nastot
  - kstot
  - clstot
  - co3stot
  - hco3stot
  - so4pc
  - capc
  - mgpc
  - napc
  - kpc
  - clpc
  - co3pc
  - hco3pc
  - so4sq
  - casq
  - mgsq
  - nasq
  - ksq
  - clsq
  - co3sq
  - hco3sq
  - so4lq
  - calq
  - mglq
  - nalq
  - klq
  - cllq
  - co3lq
  - hco3lq
  - so4tq
  - catq
  - mgtq
  - natq
  - ktq
  - cltq
  - co3tq
  - hco3tq
  - so4ws
  - caws
  - mgws
  - naws
  - kws
  - clws
  - co3ws
  - hco3ws
  - so4is
  - cais
  - mgis
  - nais
  - kis
  - clis
  - co3is
  - hco3is
  - so4ig
  - caig
  - mgig
  - naig
  - kig
  - clig
  - co3ig
  - hco3ig
  - so4io
  - caio
  - mgio
  - naio
  - kio
  - clio
  - co3io
  - hco3io
  - so4rn
  - carn
  - mgrn
  - narn
  - krn
  - clrn
  - co3rn
  - hco3rn
  - so4dd
  - cadd
  - mgdd
  - nadd
  - kdd
  - cldd
  - co3dd
  - hco3dd
  - so4rd
  - card
  - mgrd
  - nard
  - krd
  - clrd
  - co3rd
  - hco3rd
  - so4fz
  - cafz
  - mgfz
  - nafz
  - kfz
  - clfz
  - co3fz
  - hco3fz
  - so4am
  - caam
  - mgam
  - naam
  - kam
  - clam
  - co3am
  - hco3am
  - so4up
  - caup
  - mgup
  - naup
  - kup
  - clup
  - co3up
  - hco3up
  - dssl
  - seo4tot
  - seo3tot
  - borntot
  - seo4pc
  - seo3pc
  - bornpc
  - seo4sq
  - seo3sq
  - bornsq
  - seo4lq
  - seo3lq
  - bornlq
  - seo4tq
  - seo3tq
  - borntq
  - seo4sd
  - seo3sd
  - bornsd
  - seo4ws
  - seo3ws
  - bornws
  - seo4is
  - seo3is
  - bornis
  - seo4ig
  - seo3ig
  - bornig
  - seo4io
  - seo3io
  - bornio
  - seo4rn
  - seo3rn
  - bornrn
  - seo4dd
  - seo3dd
  - borndd
  - seo4fz
  - seo3fz
  - bornfz
  - seo4up
  - seo3up
  - bornup
  - seo4rc
  - seo3rc
  - bornrc
  - seo4sb
  - seo3sb
  - bornsb
  - otype
  - type
  - num
  - obout
  - obno_out
  - htyp_out
  - frac
  - sol
  - sor
purpose: ""
---

# constituent_mass_module

> [!info] 模块
> 定义派生类型与模块级变量（关键变量的归宿）。

## 定义的类型
| 类型 | 说明 |
|---|---|
| `constituents` |  |
| `exco_pesticide` |  |
| `dr_pesticide` |  |
| `exco_pathogens` |  |
| `dr_pathogens` |  |
| `exco_heavy_metals` |  |
| `dr_heavy_metals` |  |
| `exco_salts` |  |
| `dr_salts` |  |
| `salt_solids_soil` |  |
| `constituent_mass` |  |
| `soil_constituent_mass` |  |
| `plant_constituent_mass` |  |
| `all_constituent_hydrograph` |  |
| `gw_load_hydrograph` |  |
| `recall_salt_inputs` |  |
| `recall_cs_inputs` |  |
| `recall_pesticide_inputs` |  |
| `cs_soil_init_concentrations` |  |
| `salt_aqu_init_concentrations` |  |
| `cs_aqu_init_concentrations` |  |
| `salt_cha_init_concentrations` |  |
| `cs_cha_init_concentrations` |  |
| `cs_water_init_concentrations` |  |
| `cs_irrigation_concentrations` |  |
| `output_rusaltb_header` |  |
| `output_rucsb_header` |  |
| `constituents_header_in` |  |
| `constituents_header_out` |  |
| `sol_sor` |  |

## 模块级变量（关键变量）
| 变量 | 类型 | 含义 |
|---|---|---|
| `cs_db` |  |  |
| `wdraw_cs` |  |  |
| `wdraw_cs_tot` |  |  |
| `outflo_cs` |  |  |
| `hcs1` |  |  |
| `hcs2` |  |  |
| `hcs3` |  |  |
| `hin_csz` |  |  |
| `hcsz` |  |  |
| `rusaltb_hdr` |  |  |
| `rucsb_hdr` |  |  |
| `csin_hyd_hdr` |  |  |
| `csout_hyd_hdr` |  |  |
| `name` |  |  |
| `filename` |  |  |
| `day` |  |  |
| `mo` |  |  |
| `day_mo` |  |  |
| `yrc` |  |  |
| `isd` |  |  |
| `id` |  |  |
| `so4tot` |  |  |
| `castot` |  |  |
| `mgstot` |  |  |
| `nastot` |  |  |
| `kstot` |  |  |
| `clstot` |  |  |
| `co3stot` |  |  |
| `hco3stot` |  |  |
| `so4pc` |  |  |
| `capc` |  |  |
| `mgpc` |  |  |
| `napc` |  |  |
| `kpc` |  |  |
| `clpc` |  |  |
| `co3pc` |  |  |
| `hco3pc` |  |  |
| `so4sq` |  |  |
| `casq` |  |  |
| `mgsq` |  |  |

*（仅显示前 40 个，共 199 个）*

## 被以下源码使用（dataview 实时反查）

```dataview
LIST file.link
WHERE type = "source" AND contains(module, this.module_name)
```

<!-- USER-NOTES-START -->
## 我的笔记
（在此记录类型/变量的含义、单位、取值。重跑生成脚本时本段会被保留。）
<!-- USER-NOTES-END -->
