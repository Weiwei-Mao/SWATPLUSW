---
type: source
subtype: subroutine
tags:
  - swat/源码
  - swat/待读
file: dr_db_read.f90
subroutine: dr_db_read
module:
  - dr_module
  - input_file_module
  - constituent_mass_module
  - maximum_data_module
calls:
  - dr_read_om
  - dr_read_pest
  - dr_path_read
  - dr_read_hmet
  - dr_read_salt
reads:
  - in_delr%del_ratio
writes: []
purpose: ""
---

# dr_db_read

> [!info] 概要
> 待补充

## 基本信息
- **类型**：`subroutine`
- **源文件**：`dr_db_read.f90`
- **使用模块**：[[dr_module.f90]]、[[input_file_module.f90]]、[[constituent_mass_module.f90]]、[[maximum_data_module.f90]]
- **调用子程序**：5 个 ｜ **读取文件**：1 ｜ **写入文件**：0

## 调用关系
**本程序调用：**

- [[dr_read_om.f90]]
- [[dr_read_pest.f90]]
- [[dr_path_read.f90]]
- [[dr_read_hmet.f90]]
- [[dr_read_salt.f90]]

**被以下程序调用**（dataview 实时反查）：

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## 文件读写
- **读取**：`in_delr%del_ratio` _（变量，见 file.cio）_

<!-- USER-NOTES-START -->
## 我的笔记
（在此自由记录：逐行注解、关键变量、个人理解。重跑生成脚本时本段会被保留。）
<!-- USER-NOTES-END -->
