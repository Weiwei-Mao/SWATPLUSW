---
type: source
subtype: subroutine
tags:
  - swat/源码
  - swat/待读
file: unit_hyd_ru_hru.f90
subroutine: unit_hyd_ru_hru
module:
  - hru_module
  - ru_module
  - hydrograph_module
  - time_module
calls:
  - unit_hyd
reads: []
writes: []
purpose: ""
---

# unit_hyd_ru_hru

> [!info] 概要
> 待补充

## 基本信息
- **类型**：`subroutine`
- **源文件**：`unit_hyd_ru_hru.f90`
- **使用模块**：[[hru_module.f90]]、[[ru_module.f90]]、[[hydrograph_module.f90]]、[[time_module.f90]]
- **调用子程序**：1 个 ｜ **读取文件**：0 ｜ **写入文件**：0

## 调用关系
**本程序调用：**

- [[unit_hyd.f90]]

**被以下程序调用**（dataview 实时反查）：

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

<!-- USER-NOTES-START -->
## 我的笔记
（在此自由记录：逐行注解、关键变量、个人理解。重跑生成脚本时本段会被保留。）
<!-- USER-NOTES-END -->
