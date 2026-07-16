---
type: source
subtype: subroutine
tags:
  - swat/源码
  - swat/待读
file: hru_urbanhr.f90
subroutine: hru_urbanhr
module:
  - hru_module
  - plant_module
  - urban_data_module
  - climate_module
  - time_module
calls:
  - hru_sweep
reads: []
writes: []
purpose: "this subroutine computes loadings from urban areas using the；a build-up/wash-off algorithm at subdaily time intervals"
---

# hru_urbanhr

> [!info] 概要
> this subroutine computes loadings from urban areas using the；a build-up/wash-off algorithm at subdaily time intervals

## 基本信息
- **类型**：`subroutine`
- **源文件**：`hru_urbanhr.f90`
- **使用模块**：[[hru_module.f90]]、[[plant_module.f90]]、[[urban_data_module.f90]]、[[climate_module.f90]]、[[time_module.f90]]
- **调用子程序**：1 个 ｜ **读取文件**：0 ｜ **写入文件**：0

## 调用关系
**本程序调用：**

- [[hru_sweep.f90]]

**被以下程序调用**（dataview 实时反查）：

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

<!-- USER-NOTES-START -->
## 我的笔记
（在此自由记录：逐行注解、关键变量、个人理解。重跑生成脚本时本段会被保留。）
<!-- USER-NOTES-END -->
