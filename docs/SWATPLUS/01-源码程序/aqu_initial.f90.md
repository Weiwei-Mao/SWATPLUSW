---
type: source
subtype: subroutine
tags:
  - swat/源码
  - swat/待读
file: aqu_initial.f90
subroutine: aqu_initial
module:
  - aquifer_module
  - hydrograph_module
  - constituent_mass_module
  - aqu_pesticide_module
  - salt_module
  - salt_aquifer
  - cs_module
  - cs_aquifer
calls: []
reads: []
writes: []
purpose: ""
---

# aqu_initial

> [!info] 概要
> 待补充

## 基本信息
- **类型**：`subroutine`
- **源文件**：`aqu_initial.f90`
- **使用模块**：[[aquifer_module.f90]]、[[hydrograph_module.f90]]、[[constituent_mass_module.f90]]、[[aqu_pesticide_module.f90]]、[[salt_module.f90]]、[[salt_aquifer.f90]]、[[cs_module.f90]]、[[cs_aquifer.f90]]
- **调用子程序**：0 个 ｜ **读取文件**：0 ｜ **写入文件**：0

## 调用关系
（无 call 语句，叶子节点）

**被以下程序调用**（dataview 实时反查）：

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

<!-- USER-NOTES-START -->
## 我的笔记
（在此自由记录：逐行注解、关键变量、个人理解。重跑生成脚本时本段会被保留。）
<!-- USER-NOTES-END -->
