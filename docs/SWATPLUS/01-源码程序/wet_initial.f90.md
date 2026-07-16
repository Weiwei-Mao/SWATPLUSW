---
type: source
subtype: subroutine
tags:
  - swat/源码
  - swat/待读
file: wet_initial.f90
subroutine: wet_initial
module:
  - reservoir_module
  - reservoir_data_module
  - hydrograph_module
  - hru_module
  - maximum_data_module
  - water_body_module
  - soil_module
  - conditional_module
  - constituent_mass_module
  - res_salt_module
  - res_cs_module
calls:
  - res_convert_mass
reads: []
writes: []
purpose: ""
---

# wet_initial

> [!info] 概要
> 待补充

## 基本信息
- **类型**：`subroutine`
- **源文件**：`wet_initial.f90`
- **使用模块**：[[reservoir_module.f90]]、[[reservoir_data_module.f90]]、[[hydrograph_module.f90]]、[[hru_module.f90]]、[[maximum_data_module.f90]]、[[water_body_module.f90]]、[[soil_module.f90]]、[[conditional_module.f90]]、[[constituent_mass_module.f90]]、[[res_salt_module.f90]]、[[res_cs_module.f90]]
- **调用子程序**：1 个 ｜ **读取文件**：0 ｜ **写入文件**：0

## 调用关系
**本程序调用：**

- `res_convert_mass`

**被以下程序调用**（dataview 实时反查）：

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

<!-- USER-NOTES-START -->
## 我的笔记
（在此自由记录：逐行注解、关键变量、个人理解。重跑生成脚本时本段会被保留。）
<!-- USER-NOTES-END -->
