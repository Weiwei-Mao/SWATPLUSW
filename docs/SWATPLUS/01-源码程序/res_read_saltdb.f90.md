---
type: source
subtype: subroutine
tags:
  - swat/源码
  - swat/待读
file: res_read_saltdb.f90
subroutine: res_read_saltdb
module:
  - input_file_module
  - maximum_data_module
  - reservoir_data_module
  - res_salt_module
  - constituent_mass_module
calls: []
reads:
  - salt_res
writes: []
purpose: "this subroutine reads reservoir water quality parameters for salt ions"
---

# res_read_saltdb

> [!info] 概要
> this subroutine reads reservoir water quality parameters for salt ions

## 基本信息
- **类型**：`subroutine`
- **源文件**：`res_read_saltdb.f90`
- **使用模块**：[[input_file_module.f90]]、[[maximum_data_module.f90]]、[[reservoir_data_module.f90]]、[[res_salt_module.f90]]、[[constituent_mass_module.f90]]
- **调用子程序**：0 个 ｜ **读取文件**：1 ｜ **写入文件**：0

## 调用关系
（无 call 语句，叶子节点）

**被以下程序调用**（dataview 实时反查）：

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## 文件读写
- **读取**：`salt_res` _（变量，见 file.cio）_

<!-- USER-NOTES-START -->
## 我的笔记
（在此自由记录：逐行注解、关键变量、个人理解。重跑生成脚本时本段会被保留。）
<!-- USER-NOTES-END -->
