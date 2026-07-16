---
type: source
subtype: subroutine
tags:
  - swat/源码
  - swat/待读
file: proc_hru.f90
subroutine: proc_hru
module:
  - hydrograph_module
  - maximum_data_module
  - hru_module
  - soil_module
  - constituent_mass_module
  - landuse_data_module
  - erosion_module
  - output_path_module
calls:
  - hru_allo
  - hru_read
  - hrudb_init
  - hru_lum_init_all
  - topohyd_init
  - hru_output_allo
  - structure_set_parms
  - soils_init
  - structure_init
  - plant_all_init
  - cn2_init_all
  - hydro_init
  - pesticide_init
  - pathogen_init
  - salt_hru_init
  - cs_hru_init
  - open_output_file
  - rte_read_nut
reads: []
writes: []
purpose: ""
---

# proc_hru

> [!info] 概要
> 待补充

## 基本信息
- **类型**：`subroutine`
- **源文件**：`proc_hru.f90`
- **使用模块**：[[hydrograph_module.f90]]、[[maximum_data_module.f90]]、[[hru_module.f90]]、[[soil_module.f90]]、[[constituent_mass_module.f90]]、[[landuse_data_module.f90]]、[[erosion_module.f90]]、[[output_path_module.f90]]
- **调用子程序**：18 个 ｜ **读取文件**：0 ｜ **写入文件**：0

## 调用关系
**本程序调用：**

- [[hru_allo.f90]]
- [[hru_read.f90]]
- [[hrudb_init.f90]]
- [[hru_lum_init_all.f90]]
- [[topohyd_init.f90]]
- [[hru_output_allo.f90]]
- [[structure_set_parms.f90]]
- [[soils_init.f90]]
- [[structure_init.f90]]
- [[plant_all_init.f90]]
- [[cn2_init_all.f90]]
- [[hydro_init.f90]]
- [[pesticide_init.f90]]
- [[pathogen_init.f90]]
- [[salt_hru_init.f90]]
- [[cs_hru_init.f90]]
- `open_output_file`
- [[rte_read_nut.f90]]

**被以下程序调用**（dataview 实时反查）：

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

<!-- USER-NOTES-START -->
## 我的笔记
（在此自由记录：逐行注解、关键变量、个人理解。重跑生成脚本时本段会被保留。）
<!-- USER-NOTES-END -->
