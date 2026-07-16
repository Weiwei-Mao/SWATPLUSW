---
type: source
subtype: subroutine
tags:
  - swat/源码
  - swat/待读
file: time_read.f90
subroutine: time_read
module:
  - time_module
  - input_file_module
calls:
  - xmon
reads:
  - in_sim%time
writes: []
purpose: ""
---

# time_read

> [!info] 概要
> 待补充

## 基本信息
- **类型**：`subroutine`
- **源文件**：`time_read.f90`
- **使用模块**：[[time_module.f90]]、[[input_file_module.f90]]
- **调用子程序**：1 个 ｜ **读取文件**：1 ｜ **写入文件**：0

## 调用关系
**本程序调用：**

- [[xmon.f90]]

**被以下程序调用**（dataview 实时反查）：

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## 文件读写
- **读取**：`in_sim%time` _（变量，见 file.cio）_

<!-- USER-NOTES-START -->
## 我的笔记
（在此自由记录：逐行注解、关键变量、个人理解。重跑生成脚本时本段会被保留。）
<!-- USER-NOTES-END -->
