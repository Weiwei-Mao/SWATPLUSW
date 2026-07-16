---
type: module
tags:
  - swat/模块
  - swat/待读
file: reservoir_conditions_module.f90
module_name: reservoir_conditions_module
defines_types:
  - cond
  - conditions
  - modules
  - reservoir_condition_tables
defines_vars:
  - hit
  - var
  - op
  - name
purpose: ""
---

# reservoir_conditions_module

> [!info] 模块
> 定义派生类型与模块级变量（关键变量的归宿）。

## 定义的类型
| 类型 | 说明 |
|---|---|
| `cond` |  |
| `conditions` |  |
| `modules` |  |
| `reservoir_condition_tables` |  |

## 模块级变量（关键变量）
| 变量 | 类型 | 含义 |
|---|---|---|
| `hit` |  |  |
| `var` |  |  |
| `op` |  |  |
| `name` |  |  |

## 被以下源码使用（dataview 实时反查）

```dataview
LIST file.link
WHERE type = "source" AND contains(module, this.module_name)
```

<!-- USER-NOTES-START -->
## 我的笔记
（在此记录类型/变量的含义、单位、取值。重跑生成脚本时本段会被保留。）
<!-- USER-NOTES-END -->
