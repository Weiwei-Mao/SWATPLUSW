---
type: source
subtype: subroutine
tags:
  - swat/源码
  - swat/待读
file: plant_all_init.f90
subroutine: plant_all_init
module:
  - plant_module
  - plant_data_module
  - hru_module
  - hydrograph_module
  - maximum_data_module
calls:
  - plant_init
reads: []
writes: []
purpose: ""
---

# plant_all_init

> [!info] 概要
> 待补充

## 基本信息
- **类型**：`subroutine`
- **源文件**：`plant_all_init.f90`
- **使用模块**：[[plant_module.f90]]、[[plant_data_module.f90]]、[[hru_module.f90]]、[[hydrograph_module.f90]]、[[maximum_data_module.f90]]
- **调用子程序**：1 个 ｜ **读取文件**：0 ｜ **写入文件**：0

## 调用关系
**本程序调用：**

- [[plant_init.f90]]

**被以下程序调用**（dataview 实时反查）：

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

<!-- USER-NOTES-START -->
## 我的笔记
（在此自由记录：逐行注解、关键变量、个人理解。重跑生成脚本时本段会被保留。）
<!-- USER-NOTES-END -->
