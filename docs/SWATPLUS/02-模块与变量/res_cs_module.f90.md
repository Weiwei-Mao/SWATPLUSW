---
type: module
tags:
  - swat/模块
  - swat/待读
file: res_cs_module.f90
module_name: res_cs_module
defines_types:
  - res_cs_balance
  - res_cs_output
  - reservoir_cs_data
  - res_cs_header
defines_vars:
  - res_csbz
  - rescs_hdr
  - name
  - day
  - mo
  - day_mo
  - yrc
  - isd
  - id
  - seo4in
  - seo3in
  - bornin
  - seo4out
  - seo3out
  - bornout
  - seo4seep
  - seo3seep
  - bornseep
  - seo4setl
  - seo3setl
  - bornsetl
  - seo4rctn
  - seo3rctn
  - bornrctn
  - seo4prod
  - seo3prod
  - bornprod
  - seo4fert
  - seo3fert
  - bornfert
  - seo4irr
  - seo3irr
  - bornirr
  - seo4div
  - seo3div
  - borndiv
  - seo4
  - seo3
  - born
  - seo4c
  - seo3c
  - bornc
  - volm
purpose: ""
---

# res_cs_module

> [!info] 模块
> 定义派生类型与模块级变量（关键变量的归宿）。

## 定义的类型
| 类型 | 说明 |
|---|---|
| `res_cs_balance` |  |
| `res_cs_output` |  |
| `reservoir_cs_data` |  |
| `res_cs_header` |  |

## 模块级变量（关键变量）
| 变量 | 类型 | 含义 |
|---|---|---|
| `res_csbz` |  |  |
| `rescs_hdr` |  |  |
| `name` |  |  |
| `day` |  |  |
| `mo` |  |  |
| `day_mo` |  |  |
| `yrc` |  |  |
| `isd` |  |  |
| `id` |  |  |
| `seo4in` |  |  |
| `seo3in` |  |  |
| `bornin` |  |  |
| `seo4out` |  |  |
| `seo3out` |  |  |
| `bornout` |  |  |
| `seo4seep` |  |  |
| `seo3seep` |  |  |
| `bornseep` |  |  |
| `seo4setl` |  |  |
| `seo3setl` |  |  |
| `bornsetl` |  |  |
| `seo4rctn` |  |  |
| `seo3rctn` |  |  |
| `bornrctn` |  |  |
| `seo4prod` |  |  |
| `seo3prod` |  |  |
| `bornprod` |  |  |
| `seo4fert` |  |  |
| `seo3fert` |  |  |
| `bornfert` |  |  |
| `seo4irr` |  |  |
| `seo3irr` |  |  |
| `bornirr` |  |  |
| `seo4div` |  |  |
| `seo3div` |  |  |
| `borndiv` |  |  |
| `seo4` |  |  |
| `seo3` |  |  |
| `born` |  |  |
| `seo4c` |  |  |

*（仅显示前 40 个，共 43 个）*

## 被以下源码使用（dataview 实时反查）

```dataview
LIST file.link
WHERE type = "source" AND contains(module, this.module_name)
```

<!-- USER-NOTES-START -->
## 我的笔记
（在此记录类型/变量的含义、单位、取值。重跑生成脚本时本段会被保留。）
<!-- USER-NOTES-END -->
