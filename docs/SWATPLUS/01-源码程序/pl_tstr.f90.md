---
type: source
subtype: subroutine
tags:
  - swat/源码
  - swat/待读
file: pl_tstr.f90
subroutine: pl_tstr
module:
  - climate_module
  - plant_data_module
  - hru_module
  - plant_module
calls: []
reads: []
writes: []
purpose: "computes temperature stress for crop growth - strstmp"
---

# pl_tstr

> [!info] 概要
> computes temperature stress for crop growth - strstmp

## 基本信息
- **类型**：`subroutine`
- **源文件**：`pl_tstr.f90`
- **使用模块**：[[climate_module.f90]]、[[plant_data_module.f90]]、[[hru_module.f90]]、[[plant_module.f90]]
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
