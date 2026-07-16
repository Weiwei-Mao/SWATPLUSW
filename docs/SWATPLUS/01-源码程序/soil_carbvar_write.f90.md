---
type: source
subtype: subroutine
tags:
  - swat/源码
  - swat/待读
file: soil_carbvar_write.f90
subroutine: soil_carbvar_write
module:
  - basin_module
  - carbon_module
  - hydrograph_module
  - organic_mineral_mass_module
  - calibration_data_module
  - soil_module
  - time_module
calls:
  - cv_emit_row_id_txt
  - cb_write_depth_row
  - cv_drv_blocks
  - cv_emit_row_id_csv
  - cv_dyn_blocks
  - cb_write_var_block
reads: []
writes: []
purpose: ""
---

# soil_carbvar_write

> [!info] 概要
> 待补充

## 基本信息
- **类型**：`subroutine`
- **源文件**：`soil_carbvar_write.f90`
- **使用模块**：[[basin_module.f90]]、[[carbon_module.f90]]、[[hydrograph_module.f90]]、[[organic_mineral_mass_module.f90]]、[[calibration_data_module.f90]]、[[soil_module.f90]]、[[time_module.f90]]
- **调用子程序**：6 个 ｜ **读取文件**：0 ｜ **写入文件**：0

## 调用关系
**本程序调用：**

- `cv_emit_row_id_txt`
- `cb_write_depth_row`
- `cv_drv_blocks`
- `cv_emit_row_id_csv`
- `cv_dyn_blocks`
- `cb_write_var_block`

**被以下程序调用**（dataview 实时反查）：

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

<!-- USER-NOTES-START -->
## 我的笔记
（在此自由记录：逐行注解、关键变量、个人理解。重跑生成脚本时本段会被保留。）
<!-- USER-NOTES-END -->
