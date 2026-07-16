---
type: source
subtype: subroutine
tags:
  - swat/源码
  - swat/待读
file: mgt_read_mgtops.f90
subroutine: mgt_read_mgtops
module:
  - input_file_module
  - maximum_data_module
  - mgt_operations_module
calls:
  - read_mgtops
reads:
  - in_lum%management_sch
writes: []
purpose: ""
---

# mgt_read_mgtops

> [!info] 概要
> 待补充

## 基本信息
- **类型**：`subroutine`
- **源文件**：`mgt_read_mgtops.f90`
- **使用模块**：[[input_file_module.f90]]、[[maximum_data_module.f90]]、[[mgt_operations_module.f90]]
- **调用子程序**：1 个 ｜ **读取文件**：1 ｜ **写入文件**：0

## 调用关系
**本程序调用：**

- [[read_mgtops.f90]]

**被以下程序调用**（dataview 实时反查）：

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## 文件读写
- **读取**：`in_lum%management_sch` _（变量，见 file.cio）_

<!-- USER-NOTES-START -->
## 我的笔记
（在此自由记录：逐行注解、关键变量、个人理解。重跑生成脚本时本段会被保留。）
<!-- USER-NOTES-END -->
