---
type: source
subtype: subroutine
tags:
  - swat/源码
  - swat/待读
file: wet_cs.f90
subroutine: wet_cs
module:
  - reservoir_data_module
  - reservoir_module
  - water_body_module
  - hydrograph_module
  - hru_module
  - constituent_mass_module
  - res_cs_module
  - climate_module
  - cs_data_module
calls: []
reads: []
writes: []
purpose: "this subroutine computes the wetland constituent mass balance"
---

# wet_cs

> [!info] 概要
> this subroutine computes the wetland constituent mass balance

## 基本信息
- **类型**：`subroutine`
- **源文件**：`wet_cs.f90`
- **使用模块**：[[reservoir_data_module.f90]]、[[reservoir_module.f90]]、[[water_body_module.f90]]、[[hydrograph_module.f90]]、[[hru_module.f90]]、[[constituent_mass_module.f90]]、[[res_cs_module.f90]]、[[climate_module.f90]]、[[cs_data_module.f90]]
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
