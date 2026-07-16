---
type: source
subtype: subroutine
tags:
  - swat/源码
  - swat/待读
file: swift_output.f90
subroutine: swift_output
module:
  - hydrograph_module
  - hru_module
  - soil_module
  - output_landscape_module
  - reservoir_data_module
  - maximum_data_module
  - climate_module
  - aquifer_module
  - input_file_module
  - sd_channel_module
  - time_module
  - recall_module
calls:
  - system
  - copy_file
  - hyd_convert_mass_to_conc
reads: []
writes:
  - SWIFT/file_cio.swf
  - SWIFT/precip.swf
  - SWIFT/hru_dat.swf
  - SWIFT/hru_exco.swf
  - SWIFT/hru_wet.swf
  - SWIFT/chan_dat.swf
  - SWIFT/chan_dr.swf
  - SWIFT/aqu_dr.swf
  - SWIFT/res_dat.swf
  - SWIFT/res_dr.swf
  - SWIFT/recall.swf
  - SWIFT/" // trim(adjustl(recall_db(irec
  - SWIFT/object_prt.swf
purpose: ""
---

# swift_output

> [!info] 概要
> 待补充

## 基本信息
- **类型**：`subroutine`
- **源文件**：`swift_output.f90`
- **使用模块**：[[hydrograph_module.f90]]、[[hru_module.f90]]、[[soil_module.f90]]、[[output_landscape_module.f90]]、[[reservoir_data_module.f90]]、[[maximum_data_module.f90]]、[[climate_module.f90]]、[[aquifer_module.f90]]、[[input_file_module.f90]]、[[sd_channel_module.f90]]、[[time_module.f90]]、[[recall_module.f90]]
- **调用子程序**：3 个 ｜ **读取文件**：0 ｜ **写入文件**：13

## 调用关系
**本程序调用：**

- `system`
- [[copy_file.f90]]
- `hyd_convert_mass_to_conc`

**被以下程序调用**（dataview 实时反查）：

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## 文件读写
- **写入**：`SWIFT/file_cio.swf`、`SWIFT/precip.swf`、`SWIFT/hru_dat.swf`、`SWIFT/hru_exco.swf`、`SWIFT/hru_wet.swf`、`SWIFT/chan_dat.swf`、`SWIFT/chan_dr.swf`、`SWIFT/aqu_dr.swf`、`SWIFT/res_dat.swf`、`SWIFT/res_dr.swf`、`SWIFT/recall.swf`、`SWIFT/" // trim(adjustl(recall_db(irec`、`SWIFT/object_prt.swf`

<!-- USER-NOTES-START -->
## 我的笔记
（在此自由记录：逐行注解、关键变量、个人理解。重跑生成脚本时本段会被保留。）
<!-- USER-NOTES-END -->
