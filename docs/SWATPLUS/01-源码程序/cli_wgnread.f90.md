---
type: source
subtype: subroutine
tags:
  - swat/源码
  - swat/待读
file: cli_wgnread.f90
subroutine: cli_wgnread
module:
  - input_file_module
  - time_module
  - maximum_data_module
  - climate_module
calls:
  - gcycl
  - cli_initwgn
reads:
  - in_cli%weat_wgn
writes: []
purpose: ""
---

# cli_wgnread

> [!info] 概要
> 待补充

## 基本信息
- **类型**：`subroutine`
- **源文件**：`cli_wgnread.f90`
- **使用模块**：[[input_file_module.f90]]、[[time_module.f90]]、[[maximum_data_module.f90]]、[[climate_module.f90]]
- **调用子程序**：2 个 ｜ **读取文件**：1 ｜ **写入文件**：0

## 调用关系
**本程序调用：**

- [[gcycl.f90]]
- [[cli_initwgn.f90]]

**被以下程序调用**（dataview 实时反查）：

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## 文件读写
- **读取**：`in_cli%weat_wgn` _（变量，见 file.cio）_

<!-- USER-NOTES-START -->
## 我的笔记
（在此自由记录：逐行注解、关键变量、个人理解。重跑生成脚本时本段会被保留。）
<!-- USER-NOTES-END -->
