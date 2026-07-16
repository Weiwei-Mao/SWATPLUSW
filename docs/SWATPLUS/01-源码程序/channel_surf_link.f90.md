---
type: source
subtype: subroutine
tags:
  - swat/源码
  - swat/待读
file: channel_surf_link.f90
subroutine: channel_surf_link
module:
  - hydrograph_module
  - channel_module
  - ru_module
  - maximum_data_module
  - hru_module
calls: []
reads: []
writes: []
purpose: ""
---

# channel_surf_link

> [!info] 概要
> 待补充

## 基本信息
- **类型**：`subroutine`
- **源文件**：`channel_surf_link.f90`
- **使用模块**：[[hydrograph_module.f90]]、[[channel_module.f90]]、[[ru_module.f90]]、[[maximum_data_module.f90]]、[[hru_module.f90]]
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
