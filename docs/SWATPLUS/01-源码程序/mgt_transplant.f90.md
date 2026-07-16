---
type: source
subtype: subroutine
tags:
  - swat/源码
  - swat/待读
file: mgt_transplant.f90
subroutine: mgt_transplant
module:
  - hru_module
  - plant_module
  - plant_data_module
  - organic_mineral_mass_module
calls:
  - pl_root_gro
  - pl_seed_gro
  - pl_partition
reads: []
writes: []
purpose: ""
---

# mgt_transplant

> [!info] 概要
> 待补充

## 基本信息
- **类型**：`subroutine`
- **源文件**：`mgt_transplant.f90`
- **使用模块**：[[hru_module.f90]]、[[plant_module.f90]]、[[plant_data_module.f90]]、[[organic_mineral_mass_module.f90]]
- **调用子程序**：3 个 ｜ **读取文件**：0 ｜ **写入文件**：0

## 调用关系
**本程序调用：**

- [[pl_root_gro.f90]]
- [[pl_seed_gro.f90]]
- [[pl_partition.f90]]

**被以下程序调用**（dataview 实时反查）：

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

<!-- USER-NOTES-START -->
## 我的笔记
（在此自由记录：逐行注解、关键变量、个人理解。重跑生成脚本时本段会被保留。）
<!-- USER-NOTES-END -->
