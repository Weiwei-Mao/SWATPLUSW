---
type: source
subtype: subroutine
tags:
  - swat/源码
  - swat/待读
file: exco_db_read.f90
subroutine: exco_db_read
module:
  - exco_module
  - constituent_mass_module
  - input_file_module
  - maximum_data_module
calls:
  - exco_read_om
  - exco_read_pest
  - exco_read_path
  - exco_read_hmet
  - exco_read_salt
reads:
  - in_exco%exco
writes: []
purpose: ""
---

# exco_db_read

> [!info] 概要
> 待补充

## 基本信息
- **类型**：`subroutine`
- **源文件**：`exco_db_read.f90`
- **使用模块**：[[exco_module.f90]]、[[constituent_mass_module.f90]]、[[input_file_module.f90]]、[[maximum_data_module.f90]]
- **调用子程序**：5 个 ｜ **读取文件**：1 ｜ **写入文件**：0

## 调用关系
**本程序调用：**

- [[exco_read_om.f90]]
- [[exco_read_pest.f90]]
- [[exco_read_path.f90]]
- [[exco_read_hmet.f90]]
- [[exco_read_salt.f90]]

**被以下程序调用**（dataview 实时反查）：

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## 文件读写
- **读取**：`in_exco%exco` _（变量，见 file.cio）_

<!-- USER-NOTES-START -->
## 我的笔记
（在此自由记录：逐行注解、关键变量、个人理解。重跑生成脚本时本段会被保留。）
<!-- USER-NOTES-END -->
