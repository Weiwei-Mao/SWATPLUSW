---
type: module
tags:
  - swat/模块
  - swat/待读
file: water_body_module.f90
module_name: water_body_module
defines_types:
  - water_body
defines_vars:
  - wbodz
  - bch_wat_d
  - bch_wat_m
  - bch_wat_y
  - bch_wat_a
  - bres_wat_d
  - bres_wat_m
  - bres_wat_y
  - bres_wat_a
purpose: ""
---

# water_body_module

> [!info] 模块
> 定义派生类型与模块级变量（关键变量的归宿）。

## 定义的类型
| 类型 | 说明 |
|---|---|
| `water_body` |  |

## 模块级变量（关键变量）
| 变量 | 类型 | 含义 |
|---|---|---|
| `wbodz` |  |  |
| `bch_wat_d` |  |  |
| `bch_wat_m` |  |  |
| `bch_wat_y` |  |  |
| `bch_wat_a` |  |  |
| `bres_wat_d` |  |  |
| `bres_wat_m` |  |  |
| `bres_wat_y` |  |  |
| `bres_wat_a` |  |  |

## 被以下源码使用（dataview 实时反查）

```dataview
LIST file.link
WHERE type = "source" AND contains(module, this.module_name)
```

<!-- USER-NOTES-START -->
## 我的笔记
（在此记录类型/变量的含义、单位、取值。重跑生成脚本时本段会被保留。）
<!-- USER-NOTES-END -->
