---
type: source
subtype: subroutine
tags:
  - swat/源码
  - swat/待读
file: output_landscape_init.f90
subroutine: output_landscape_init
module:
  - hydrograph_module
  - channel_module
  - sd_channel_module
  - basin_module
  - maximum_data_module
  - calibration_data_module
  - aquifer_module
  - output_landscape_module
  - time_module
  - carbon_module
  - output_path_module
  - soil_module
  - carbon_legacy_module
calls:
  - open_output_file
  - open_cb_banner_pair
  - open_cb_wide_pair
  - soil_nutcarb_write
  - open_cb_flat_pair
  - carbon_legacy_open
  - cb_write_wide_header
  - cb_write_flat_header
  - cb_write_cbn_lyr_header
reads: []
writes: []
purpose: ""
---

# output_landscape_init

> [!info] 概要
> 待补充

## 基本信息
- **类型**：`subroutine`
- **源文件**：`output_landscape_init.f90`
- **使用模块**：[[hydrograph_module.f90]]、[[channel_module.f90]]、[[sd_channel_module.f90]]、[[basin_module.f90]]、[[maximum_data_module.f90]]、[[calibration_data_module.f90]]、[[aquifer_module.f90]]、[[output_landscape_module.f90]]、[[time_module.f90]]、[[carbon_module.f90]]、[[output_path_module.f90]]、[[soil_module.f90]]、[[carbon_legacy_module.f90]]
- **调用子程序**：9 个 ｜ **读取文件**：0 ｜ **写入文件**：0

## 调用关系
**本程序调用：**

- `open_output_file`
- `open_cb_banner_pair`
- `open_cb_wide_pair`
- [[soil_nutcarb_write.f90]]
- `open_cb_flat_pair`
- `carbon_legacy_open`
- `cb_write_wide_header`
- `cb_write_flat_header`
- `cb_write_cbn_lyr_header`

**被以下程序调用**（dataview 实时反查）：

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

<!-- USER-NOTES-START -->
## 我的笔记
（在此自由记录：逐行注解、关键变量、个人理解。重跑生成脚本时本段会被保留。）
<!-- USER-NOTES-END -->
