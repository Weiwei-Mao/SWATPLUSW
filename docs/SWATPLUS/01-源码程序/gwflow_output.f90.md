---
type: source
subtype: subroutine
tags:
  - swat/源码
  - swat/待读
file: gwflow_output.f90
subroutine: gwflow_output_init
module:
  - gwflow_module
  - hydrograph_module
  - sd_channel_module
  - time_module
  - constituent_mass_module
  - basin_module
calls:
  - gwflow_write_celldef
  - gwflow_write_cell_array
reads:
  - gwflow.wbgroups
  - file_name_scalar
  - file_name(n
  - file_name(n
  - file_name(n
  - file_name(n
writes:
  - gwflow_basin_wb_day.txt
  - gwflow_basin_wb_mon.txt
  - gwflow_basin_wb_yr.txt
  - gwflow_basin_wb_aa.txt
  - gwflow_basin_heat_day.txt
  - gwflow_basin_heat_yr.txt
  - gwflow_basin_heat_aa.txt
  - gwflow_cell_wb_day.txt
  - gwflow_cell_wb_mon.txt
  - gwflow_cell_wb_yr.txt
  - gwflow_cell_wb_aa.txt
  - gwflow_cell_definition.txt
purpose: "this subroutine opens all gwflow output files and writes headers；(extracted from gwflow_read)"
---

# gwflow_output_init

> [!info] 概要
> this subroutine opens all gwflow output files and writes headers；(extracted from gwflow_read)

## 基本信息
- **类型**：`subroutine`
- **源文件**：`gwflow_output.f90`
- **使用模块**：[[gwflow_module.f90]]、[[hydrograph_module.f90]]、[[sd_channel_module.f90]]、[[time_module.f90]]、[[constituent_mass_module.f90]]、[[basin_module.f90]]
- **调用子程序**：2 个 ｜ **读取文件**：6 ｜ **写入文件**：12

## 调用关系
**本程序调用：**

- `gwflow_write_celldef`
- `gwflow_write_cell_array`

**被以下程序调用**（dataview 实时反查）：

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## 文件读写
- **写入**：`gwflow_basin_wb_day.txt`、`gwflow_basin_wb_mon.txt`、`gwflow_basin_wb_yr.txt`、`gwflow_basin_wb_aa.txt`、`gwflow_basin_heat_day.txt`、`gwflow_basin_heat_yr.txt`、`gwflow_basin_heat_aa.txt`、`gwflow_cell_wb_day.txt`、`gwflow_cell_wb_mon.txt`、`gwflow_cell_wb_yr.txt`、`gwflow_cell_wb_aa.txt`、`gwflow_cell_definition.txt`
- **读取**：`gwflow.wbgroups`、`file_name_scalar` _（变量，见 file.cio）_、`file_name(n` _（变量，见 file.cio）_、`file_name(n` _（变量，见 file.cio）_、`file_name(n` _（变量，见 file.cio）_、`file_name(n` _（变量，见 file.cio）_

<!-- USER-NOTES-START -->
## 我的笔记
（在此自由记录：逐行注解、关键变量、个人理解。重跑生成脚本时本段会被保留。）
<!-- USER-NOTES-END -->
