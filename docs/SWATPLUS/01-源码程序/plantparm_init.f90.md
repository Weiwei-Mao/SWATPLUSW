---
type: source
subtype: subroutine
tags:
  - swat/源码
  - swat/待读
file: plantparm_init.f90
subroutine: plantparm_init
module:
  - basin_module
  - maximum_data_module
  - plant_data_module
calls:
  - ascrv
reads: []
writes: []
purpose: ""
---

# plantparm_init

> [!info] 概要
> 待补充

## 基本信息
- **类型**：`subroutine`
- **源文件**：`plantparm_init.f90`
- **使用模块**：[[basin_module.f90]]、[[maximum_data_module.f90]]、[[plant_data_module.f90]]
- **调用子程序**：1 个 ｜ **读取文件**：0 ｜ **写入文件**：0

## 调用关系
**本程序调用：**

- [[ascrv.f90]]

**被以下程序调用**（dataview 实时反查）：

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

<!-- USER-NOTES-START -->
## 我的笔记
（在此自由记录：逐行注解、关键变量、个人理解。重跑生成脚本时本段会被保留。）
<!-- USER-NOTES-END -->
