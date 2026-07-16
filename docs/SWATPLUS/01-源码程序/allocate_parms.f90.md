---
type: source
subtype: subroutine
tags:
  - swat/源码
  - swat/待读
file: allocate_parms.f90
subroutine: allocate_parms
module:
  - hru_module
  - time_module
  - hydrograph_module
  - constituent_mass_module
calls:
  - zero0
  - zero1
  - zero2
  - zeroini
reads: []
writes: []
purpose: "this subroutine allocates array sizes"
---

# allocate_parms

> [!info] 概要
> this subroutine allocates array sizes

## 基本信息
- **类型**：`subroutine`
- **源文件**：`allocate_parms.f90`
- **使用模块**：[[hru_module.f90]]、[[time_module.f90]]、[[hydrograph_module.f90]]、[[constituent_mass_module.f90]]
- **调用子程序**：4 个 ｜ **读取文件**：0 ｜ **写入文件**：0

## 调用关系
**本程序调用：**

- [[zero0.f90]]
- [[zero1.f90]]
- [[zero2.f90]]
- [[zeroini.f90]]

**被以下程序调用**（dataview 实时反查）：

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

<!-- USER-NOTES-START -->
## 我的笔记
（在此自由记录：逐行注解、关键变量、个人理解。重跑生成脚本时本段会被保留。）
<!-- USER-NOTES-END -->
