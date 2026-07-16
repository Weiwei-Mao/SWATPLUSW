---
type: module
tags:
  - swat/模块
  - swat/待读
file: soil_data_module.f90
module_name: soil_data_module
defines_types:
  - soil_lte_database
  - soiltest_db
  - soiltest_db_old
  - soilayer_db
  - soil_profile_db
  - soil_database
defines_vars:
  - s
  - texture
  - name
  - snam
  - hydgrp
purpose: ""
---

# soil_data_module

> [!info] 模块
> 定义派生类型与模块级变量（关键变量的归宿）。

## 定义的类型
| 类型 | 说明 |
|---|---|
| `soil_lte_database` |  |
| `soiltest_db` |  |
| `soiltest_db_old` |  |
| `soilayer_db` |  |
| `soil_profile_db` |  |
| `soil_database` |  |

## 模块级变量（关键变量）
| 变量 | 类型 | 含义 |
|---|---|---|
| `s` |  |  |
| `texture` |  |  |
| `name` |  |  |
| `snam` |  |  |
| `hydgrp` |  |  |

## 被以下源码使用（dataview 实时反查）

```dataview
LIST file.link
WHERE type = "source" AND contains(module, this.module_name)
```

<!-- USER-NOTES-START -->
## 我的笔记
（在此记录类型/变量的含义、单位、取值。重跑生成脚本时本段会被保留。）
<!-- USER-NOTES-END -->
