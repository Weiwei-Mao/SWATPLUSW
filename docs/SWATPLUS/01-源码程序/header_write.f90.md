---
type: source
subtype: subroutine
tags:
  - swat/源码
  - swat/待读
file: header_write.f90
subroutine: header_write
module:
  - basin_module
  - aquifer_module
  - channel_module
  - reservoir_module
  - hydrograph_module
  - sd_channel_module
  - maximum_data_module
  - calibration_data_module
  - output_path_module
calls:
  - open_output_file
reads:
  - hydrology-cal.hyd
writes:
  - hru-out.cal
  - hru-new.cal
purpose: ""
---

# header_write

> [!info] 概要
> 待补充

## 基本信息
- **类型**：`subroutine`
- **源文件**：`header_write.f90`
- **使用模块**：[[basin_module.f90]]、[[aquifer_module.f90]]、[[channel_module.f90]]、[[reservoir_module.f90]]、[[hydrograph_module.f90]]、[[sd_channel_module.f90]]、[[maximum_data_module.f90]]、[[calibration_data_module.f90]]、[[output_path_module.f90]]
- **调用子程序**：1 个 ｜ **读取文件**：1 ｜ **写入文件**：2

## 调用关系
**本程序调用：**

- `open_output_file`

**被以下程序调用**（dataview 实时反查）：

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## 文件读写
- **写入**：`hru-out.cal`、`hru-new.cal`
- **读取**：`hydrology-cal.hyd`

<!-- USER-NOTES-START -->
## 我的笔记
（在此自由记录：逐行注解、关键变量、个人理解。重跑生成脚本时本段会被保留。）
<!-- USER-NOTES-END -->
