---
type: source
subtype: subroutine
tags:
  - swat/源码
  - swat/待读
file: sd_hydsed_init.f90
subroutine: sd_hydsed_init
module:
  - input_file_module
  - sd_channel_module
  - channel_velocity_module
  - maximum_data_module
  - hydrograph_module
  - constituent_mass_module
  - pesticide_data_module
  - basin_module
calls:
  - sd_rating_curve
  - rcurv_interp_dep
  - hyd_convert_conc_to_mass
reads: []
writes: []
purpose: ""
---

# sd_hydsed_init

> [!info] 概要
> 待补充

## 基本信息
- **类型**：`subroutine`
- **源文件**：`sd_hydsed_init.f90`
- **使用模块**：[[input_file_module.f90]]、[[sd_channel_module.f90]]、[[channel_velocity_module.f90]]、[[maximum_data_module.f90]]、[[hydrograph_module.f90]]、[[constituent_mass_module.f90]]、[[pesticide_data_module.f90]]、[[basin_module.f90]]
- **调用子程序**：3 个 ｜ **读取文件**：0 ｜ **写入文件**：0

## 调用关系
**本程序调用：**

- [[sd_rating_curve.f90]]
- [[rcurv_interp_dep.f90]]
- `hyd_convert_conc_to_mass`

**被以下程序调用**（dataview 实时反查）：

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

<!-- USER-NOTES-START -->
## 我的笔记
（在此自由记录：逐行注解、关键变量、个人理解。重跑生成脚本时本段会被保留。）
<!-- USER-NOTES-END -->
