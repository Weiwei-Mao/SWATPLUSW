---
type: module
tags:
  - swat/模块
  - swat/待读
file: ch_salt_module.f90
module_name: ch_salt_module
defines_types:
  - ch_salt_balance
  - ch_salt_output
  - ch_salt_header
defines_vars:
  - ch_saltbz
  - chsalt_hdr
  - day
  - mo
  - day_mo
  - yrc
  - isd
  - id
  - so4in
  - cain
  - mgin
  - nain
  - kin
  - clin
  - co3in
  - hco3in
  - so4gw
  - cagw
  - mggw
  - nagw
  - kgw
  - clgw
  - co3gw
  - hco3gw
  - so4out
  - caout
  - mgout
  - naout
  - kout
  - clout
  - co3out
  - hco3out
  - so4seep
  - caseep
  - mgseep
  - naseep
  - kseep
  - clseep
  - co3seep
  - hco3seep
  - so4irr
  - cairr
  - mgirr
  - nairr
  - kirr
  - clirr
  - co3irr
  - hco3irr
  - so4div
  - cadiv
  - mgdiv
  - nadiv
  - kdiv
  - cldiv
  - co3div
  - hco3div
  - so4
  - ca
  - mg
  - na
  - k
  - cl
  - co3
  - hco3
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

# ch_salt_module

> [!info] 模块
> 定义派生类型与模块级变量（关键变量的归宿）。

## 定义的类型
| 类型 | 说明 |
|---|---|
| `ch_salt_balance` |  |
| `ch_salt_output` |  |
| `ch_salt_header` |  |

## 模块级变量（关键变量）
| 变量 | 类型 | 含义 |
|---|---|---|
| `ch_saltbz` |  |  |
| `chsalt_hdr` |  |  |
| `day` |  |  |
| `mo` |  |  |
| `day_mo` |  |  |
| `yrc` |  |  |
| `isd` |  |  |
| `id` |  |  |
| `so4in` |  |  |
| `cain` |  |  |
| `mgin` |  |  |
| `nain` |  |  |
| `kin` |  |  |
| `clin` |  |  |
| `co3in` |  |  |
| `hco3in` |  |  |
| `so4gw` |  |  |
| `cagw` |  |  |
| `mggw` |  |  |
| `nagw` |  |  |
| `kgw` |  |  |
| `clgw` |  |  |
| `co3gw` |  |  |
| `hco3gw` |  |  |
| `so4out` |  |  |
| `caout` |  |  |
| `mgout` |  |  |
| `naout` |  |  |
| `kout` |  |  |
| `clout` |  |  |
| `co3out` |  |  |
| `hco3out` |  |  |
| `so4seep` |  |  |
| `caseep` |  |  |
| `mgseep` |  |  |
| `naseep` |  |  |
| `kseep` |  |  |
| `clseep` |  |  |
| `co3seep` |  |  |
| `hco3seep` |  |  |

*（仅显示前 40 个，共 72 个）*

## 被以下源码使用（dataview 实时反查）

```dataview
LIST file.link
WHERE type = "source" AND contains(module, this.module_name)
```

<!-- USER-NOTES-START -->
## 我的笔记
（在此记录类型/变量的含义、单位、取值。重跑生成脚本时本段会被保留。）
<!-- USER-NOTES-END -->
