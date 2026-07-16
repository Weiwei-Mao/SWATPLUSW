---
type: source
subtype: subroutine
tags:
  - swat/源码
  - swat/待读
file: readcio_read.f90
subroutine: readcio_read
module:
  - input_file_module
  - output_path_module
calls:
  - init_output_path
reads:
  - file.cio
writes: []
purpose: ""
---

# readcio_read

> [!info] 概要
> 待补充

## 基本信息
- **类型**：`subroutine`
- **源文件**：`readcio_read.f90`
- **使用模块**：[[input_file_module.f90]]、[[output_path_module.f90]]
- **调用子程序**：1 个 ｜ **读取文件**：1 ｜ **写入文件**：0

## 调用关系
**本程序调用：**

- `init_output_path`

**被以下程序调用**（dataview 实时反查）：

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## 文件读写
- **读取**：`file.cio`

<!-- USER-NOTES-START -->
## 我的笔记
（在此自由记录：逐行注解、关键变量、个人理解。重跑生成脚本时本段会被保留。）

- use: `input_file_module`, `output_path_module`
- Line 17–109: 读取 [[file.cio]]
- Line 112: file.cio 第 32 行为输出路径；若有效则初始化输出路径（校验并按需创建目录）
<!-- USER-NOTES-END -->
