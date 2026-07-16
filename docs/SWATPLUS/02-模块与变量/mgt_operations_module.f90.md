---
type: module
tags:
  - swat/模块
  - swat/待读
file: mgt_operations_module.f90
module_name: mgt_operations_module
defines_types:
  - irrigation_operation
  - puddle_operation
  - filtstrip_operation
  - fire_operation
  - grwaterway_operation
  - bmpuser_operation
  - bmpuser_operation1
  - chemical_application_operation
  - harvest_operation
  - grazing_operation
  - streetsweep_operation
  - management_ops
  - management_schedule
defines_vars:
  - harvop
  - hkop
  - graze
  - sweepop
  - mgt
  - mgt1
  - name
  - form
  - op_typ
  - typ
  - fertnm
  - op
  - op_char
  - op_plant
purpose: ""
---

# mgt_operations_module

> [!info] 模块
> 定义派生类型与模块级变量（关键变量的归宿）。

## 定义的类型
| 类型 | 说明 |
|---|---|
| `irrigation_operation` |  |
| `puddle_operation` |  |
| `filtstrip_operation` |  |
| `fire_operation` |  |
| `grwaterway_operation` |  |
| `bmpuser_operation` |  |
| `bmpuser_operation1` |  |
| `chemical_application_operation` |  |
| `harvest_operation` |  |
| `grazing_operation` |  |
| `streetsweep_operation` |  |
| `management_ops` |  |
| `management_schedule` |  |

## 模块级变量（关键变量）
| 变量 | 类型 | 含义 |
|---|---|---|
| `harvop` |  |  |
| `hkop` |  |  |
| `graze` |  |  |
| `sweepop` |  |  |
| `mgt` |  |  |
| `mgt1` |  |  |
| `name` |  |  |
| `form` |  |  |
| `op_typ` |  |  |
| `typ` |  |  |
| `fertnm` |  |  |
| `op` |  |  |
| `op_char` |  |  |
| `op_plant` |  |  |

## 被以下源码使用（dataview 实时反查）

```dataview
LIST file.link
WHERE type = "source" AND contains(module, this.module_name)
```

<!-- USER-NOTES-START -->
## 我的笔记
（在此记录类型/变量的含义、单位、取值。重跑生成脚本时本段会被保留。）
<!-- USER-NOTES-END -->
