---
type: source
subtype: subroutine
tags:
  - swat/源码
  - swat/待读
file: salt_chem_soil_single.f90
subroutine: salt_chem_soil_single
module:
  - basin_module
  - constituent_mass_module
  - salt_data_module
  - soil_module
  - salt_module
  - time_module
calls:
  - ionic_strength
  - activity_coefficient
  - caco3
  - mgco3
  - caso4
  - mgso4
  - nacl
reads: []
writes: []
purpose: "this subroutine calculates salt ion concentrations based on equilibrium chemical reactions；(precipitation-dissolution, complexation, cation exchange), for a specified HRU, for a specified layer"
---

# salt_chem_soil_single

> [!info] 概要
> this subroutine calculates salt ion concentrations based on equilibrium chemical reactions；(precipitation-dissolution, complexation, cation exchange), for a specified HRU, for a specified layer

## 基本信息
- **类型**：`subroutine`
- **源文件**：`salt_chem_soil_single.f90`
- **使用模块**：[[basin_module.f90]]、[[constituent_mass_module.f90]]、[[salt_data_module.f90]]、[[soil_module.f90]]、[[salt_module.f90]]、[[time_module.f90]]
- **调用子程序**：7 个 ｜ **读取文件**：0 ｜ **写入文件**：0

## 调用关系
**本程序调用：**

- `ionic_strength`
- `activity_coefficient`
- `caco3`
- `mgco3`
- `caso4`
- `mgso4`
- `nacl`

**被以下程序调用**（dataview 实时反查）：

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

<!-- USER-NOTES-START -->
## 我的笔记
（在此自由记录：逐行注解、关键变量、个人理解。重跑生成脚本时本段会被保留。）
<!-- USER-NOTES-END -->
