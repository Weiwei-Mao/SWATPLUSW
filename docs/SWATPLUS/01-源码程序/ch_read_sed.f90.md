---
type: source
subtype: subroutine
tags:
  - swat/源码
  - swat/待读
file: ch_read_sed.f90
subroutine: ch_read_sed
module:
  - input_file_module
  - maximum_data_module
  - channel_data_module
calls: []
reads:
  - in_cha%sed
writes: []
purpose: "this subroutine reads data from the lake water quality input file (.lwq).；This file contains data related to initial pesticide and nutrient levels；in the lake/reservoir and transformation processes occurring within the"
---

# ch_read_sed

> [!info] 概要
> this subroutine reads data from the lake water quality input file (.lwq).；This file contains data related to initial pesticide and nutrient levels；in the lake/reservoir and transformation processes occurring within the

## 基本信息
- **类型**：`subroutine`
- **源文件**：`ch_read_sed.f90`
- **使用模块**：[[input_file_module.f90]]、[[maximum_data_module.f90]]、[[channel_data_module.f90]]
- **调用子程序**：0 个 ｜ **读取文件**：1 ｜ **写入文件**：0

## 调用关系
（无 call 语句，叶子节点）

**被以下程序调用**（dataview 实时反查）：

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## 文件读写
- **读取**：`in_cha%sed` _（变量，见 file.cio）_

<!-- USER-NOTES-START -->
## 我的笔记
（在此自由记录：逐行注解、关键变量、个人理解。重跑生成脚本时本段会被保留。）
<!-- USER-NOTES-END -->
