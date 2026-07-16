---
type: module
tags:
  - swat/模块
  - swat/待读
file: salt_module.f90
module_name: salt_module
defines_types:
  - salt_balance
  - object_salt_balance
  - fert_db_salt
  - output_saltbal_header
  - output_salt_hdr_hru
defines_vars:
  - saltb_hdr
  - salt_hdr_hru
  - fertnm
  - yrc
  - mon
  - day
  - lat
  - gw
  - sur
  - urb
  - wet
  - tile
  - perc
  - gwup
  - wtsp
  - irsw
  - irgw
  - irwo
  - rain
  - dryd
  - road
  - fert
  - amnd
  - uptk
  - ptso
  - pout
  - rchg
  - seep
  - dssl
  - dsaq
  - slds
  - slmn
  - aqds
  - aqmn
  - mo
  - day_mo
  - isd
  - id
  - so4sl
  - casl
  - mgsl
  - nasl
  - ksl
  - clsl
  - co3sl
  - hco3sl
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
  - so4uq
  - cauq
  - mguq
  - nauq
  - kuq
  - cluq
  - co3uq
  - hco3uq
  - so4wt
  - cawt
  - mgwt
  - nawt
  - kwt
  - clwt
  - co3wt
  - hco3wt
  - so4tq
  - catq
  - mgtq
  - natq
  - ktq
  - cltq
  - co3tq
  - hco3tq
  - so4pc
  - capc
  - mgpc
  - napc
  - kpc
  - clpc
  - co3pc
  - hco3pc
  - so4gt
  - cagt
  - mggt
  - nagt
  - kgt
  - clgt
  - co3gt
  - hco3gt
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
  - so4c
  - cac
  - mgc
  - nac
  - kc
  - clc
  - co3c
  - hco3c
purpose: ""
---

# salt_module

> [!info] 模块
> 定义派生类型与模块级变量（关键变量的归宿）。

## 定义的类型
| 类型 | 说明 |
|---|---|
| `salt_balance` |  |
| `object_salt_balance` |  |
| `fert_db_salt` |  |
| `output_saltbal_header` |  |
| `output_salt_hdr_hru` |  |

## 模块级变量（关键变量）
| 变量 | 类型 | 含义 |
|---|---|---|
| `saltb_hdr` |  |  |
| `salt_hdr_hru` |  |  |
| `fertnm` |  |  |
| `yrc` |  |  |
| `mon` |  |  |
| `day` |  |  |
| `lat` |  |  |
| `gw` |  |  |
| `sur` |  |  |
| `urb` |  |  |
| `wet` |  |  |
| `tile` |  |  |
| `perc` |  |  |
| `gwup` |  |  |
| `wtsp` |  |  |
| `irsw` |  |  |
| `irgw` |  |  |
| `irwo` |  |  |
| `rain` |  |  |
| `dryd` |  |  |
| `road` |  |  |
| `fert` |  |  |
| `amnd` |  |  |
| `uptk` |  |  |
| `ptso` |  |  |
| `pout` |  |  |
| `rchg` |  |  |
| `seep` |  |  |
| `dssl` |  |  |
| `dsaq` |  |  |
| `slds` |  |  |
| `slmn` |  |  |
| `aqds` |  |  |
| `aqmn` |  |  |
| `mo` |  |  |
| `day_mo` |  |  |
| `isd` |  |  |
| `id` |  |  |
| `so4sl` |  |  |
| `casl` |  |  |

*（仅显示前 40 个，共 190 个）*

## 被以下源码使用（dataview 实时反查）

```dataview
LIST file.link
WHERE type = "source" AND contains(module, this.module_name)
```

<!-- USER-NOTES-START -->
## 我的笔记
（在此记录类型/变量的含义、单位、取值。重跑生成脚本时本段会被保留。）
<!-- USER-NOTES-END -->
