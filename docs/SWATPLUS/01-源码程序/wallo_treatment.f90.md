---
type: source
subtype: subroutine
tags:
  - swat/源码
  - swat/待读
file: wallo_treatment.f90
subroutine: wallo_treatment
module:
  - water_allocation_module
  - hydrograph_module
  - constituent_mass_module
calls:
  - hyd_convert_conc_to_mass
  - hyd_min
  - hydcsout_conc_mass
reads: []
writes: []
purpose: ""
---

# wallo_treatment

> [!info] 概要
> 待补充

## 基本信息
- **类型**：`subroutine`
- **源文件**：`wallo_treatment.f90`
- **使用模块**：[[water_allocation_module.f90]]、[[hydrograph_module.f90]]、[[constituent_mass_module.f90]]
- **调用子程序**：3 个 ｜ **读取文件**：0 ｜ **写入文件**：0

## 调用关系
**本程序调用：**

- `hyd_convert_conc_to_mass`
- `hyd_min`
- `hydcsout_conc_mass`

**被以下程序调用**（dataview 实时反查）：

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

<!-- USER-NOTES-START -->
## 我的笔记
（在此自由记录：逐行注解、关键变量、个人理解。重跑生成脚本时本段会被保留。）
<!-- USER-NOTES-END -->
