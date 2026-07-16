---
type: source
subtype: subroutine
tags:
  - swat/源码
  - swat/待读
file: wallo_demand.f90
subroutine: wallo_demand
module:
  - water_allocation_module
  - hru_module
  - hydrograph_module
  - conditional_module
  - recall_module
  - exco_module
calls:
  - conditions
  - actions
reads: []
writes: []
purpose: ""
---

# wallo_demand

> [!info] 概要
> 待补充

## 基本信息
- **类型**：`subroutine`
- **源文件**：`wallo_demand.f90`
- **使用模块**：[[water_allocation_module.f90]]、[[hru_module.f90]]、[[hydrograph_module.f90]]、[[conditional_module.f90]]、[[recall_module.f90]]、[[exco_module.f90]]
- **调用子程序**：2 个 ｜ **读取文件**：0 ｜ **写入文件**：0

## 调用关系
**本程序调用：**

- [[conditions.f90]]
- [[actions.f90]]

**被以下程序调用**（dataview 实时反查）：

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

<!-- USER-NOTES-START -->
## 我的笔记
（在此自由记录：逐行注解、关键变量、个人理解。重跑生成脚本时本段会被保留。）
<!-- USER-NOTES-END -->
