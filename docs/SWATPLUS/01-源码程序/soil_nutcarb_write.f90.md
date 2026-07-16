---
type: source
subtype: subroutine
tags:
  - swat/源码
  - swat/待读
file: soil_nutcarb_write.f90
subroutine: soil_nutcarb_write
module:
  - soil_module
  - organic_mineral_mass_module
  - hydrograph_module
  - calibration_data_module
  - carbon_module
  - basin_module
  - plant_module
calls:
  - cb_soil_snap_emit
  - cb_cbn_lyr_emit
  - cb_n_p_pool_emit
  - cb_plc_stat_emit
  - cb_soil_snap_period
  - cb_cflux_stat_emit
  - cb_cpool_stat_emit
  - cb_write_depth_row
  - cb_write_var_block
  - cb_emit_row_id_csv
  - cb_emit_row_id_txt
  - cb_cflux_emit_blocks
reads: []
writes: []
purpose: "this subroutine writes soil carbon output."
---

# soil_nutcarb_write

> [!info] 概要
> this subroutine writes soil carbon output.

## 基本信息
- **类型**：`subroutine`
- **源文件**：`soil_nutcarb_write.f90`
- **使用模块**：[[soil_module.f90]]、[[organic_mineral_mass_module.f90]]、[[hydrograph_module.f90]]、[[calibration_data_module.f90]]、[[carbon_module.f90]]、[[basin_module.f90]]、[[plant_module.f90]]
- **调用子程序**：12 个 ｜ **读取文件**：0 ｜ **写入文件**：0

## 调用关系
**本程序调用：**

- `cb_soil_snap_emit`
- `cb_cbn_lyr_emit`
- `cb_n_p_pool_emit`
- `cb_plc_stat_emit`
- `cb_soil_snap_period`
- `cb_cflux_stat_emit`
- `cb_cpool_stat_emit`
- `cb_write_depth_row`
- `cb_write_var_block`
- `cb_emit_row_id_csv`
- `cb_emit_row_id_txt`
- `cb_cflux_emit_blocks`

**被以下程序调用**（dataview 实时反查）：

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

<!-- USER-NOTES-START -->
## 我的笔记
（在此自由记录：逐行注解、关键变量、个人理解。重跑生成脚本时本段会被保留。）
<!-- USER-NOTES-END -->
