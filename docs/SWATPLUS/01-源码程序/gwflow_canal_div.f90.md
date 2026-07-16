---
type: source
subtype: subroutine
tags:
  - swat/源码
  - swat/待读
file: gwflow_canal_div.f90
subroutine: gwflow_canal_div
module:
  - gwflow_module
  - hydrograph_module
  - time_module
  - constituent_mass_module
  - hru_module
  - res_salt_module
  - res_cs_module
  - salt_module
  - cs_module
calls: []
reads: []
writes: []
purpose: "this subroutine calculates the water exchange volume between irrigation canals and connected grid cells；for canals that are connected to a point source diversion (recall object); seepage water should be；removed from the diverted water volume."
---

# gwflow_canal_div

> [!info] 概要
> this subroutine calculates the water exchange volume between irrigation canals and connected grid cells；for canals that are connected to a point source diversion (recall object); seepage water should be；removed from the diverted water volume.

## 基本信息
- **类型**：`subroutine`
- **源文件**：`gwflow_canal_div.f90`
- **使用模块**：[[gwflow_module.f90]]、[[hydrograph_module.f90]]、[[time_module.f90]]、[[constituent_mass_module.f90]]、[[hru_module.f90]]、[[res_salt_module.f90]]、[[res_cs_module.f90]]、[[salt_module.f90]]、[[cs_module.f90]]
- **调用子程序**：0 个 ｜ **读取文件**：0 ｜ **写入文件**：0

## 调用关系
（无 call 语句，叶子节点）

**被以下程序调用**（dataview 实时反查）：

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

<!-- USER-NOTES-START -->
## 我的笔记
（在此自由记录：逐行注解、关键变量、个人理解。重跑生成脚本时本段会被保留。）
<!-- USER-NOTES-END -->
