---
type: source
subtype: subroutine
tags:
  - swat/源码
  - swat/待读
file: salt_fert_read.f90
subroutine: salt_fert_read
module:
  - constituent_mass_module
  - input_file_module
  - maximum_data_module
  - salt_module
calls: []
reads:
  - salt_fertilizer.frt
writes: []
purpose: "this subroutine reads salt ion fertilizer loading (kg/ha) for various fertilizer types"
---

# salt_fert_read

> [!info] 概要
> this subroutine reads salt ion fertilizer loading (kg/ha) for various fertilizer types

## 基本信息
- **类型**：`subroutine`
- **源文件**：`salt_fert_read.f90`
- **使用模块**：[[constituent_mass_module.f90]]、[[input_file_module.f90]]、[[maximum_data_module.f90]]、[[salt_module.f90]]
- **调用子程序**：0 个 ｜ **读取文件**：1 ｜ **写入文件**：0

## 调用关系
（无 call 语句，叶子节点）

**被以下程序调用**（dataview 实时反查）：

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## 文件读写
- **读取**：`salt_fertilizer.frt`

<!-- USER-NOTES-START -->
## 我的笔记
（在此自由记录：逐行注解、关键变量、个人理解。重跑生成脚本时本段会被保留。）
<!-- USER-NOTES-END -->
