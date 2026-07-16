---
type: source
subtype: subroutine
tags:
  - swat/源码
  - swat/待读
file: header_path.f90
subroutine: header_path
module:
  - basin_module
  - reservoir_module
  - output_ls_pathogen_module
  - constituent_mass_module
  - output_path_module
calls:
  - open_output_file
reads: []
writes: []
purpose: ""
---

# header_path

> [!info] 概要
> 待补充

## 基本信息
- **类型**：`subroutine`
- **源文件**：`header_path.f90`
- **使用模块**：[[basin_module.f90]]、[[reservoir_module.f90]]、[[output_ls_pathogen_module.f90]]、[[constituent_mass_module.f90]]、[[output_path_module.f90]]
- **调用子程序**：1 个 ｜ **读取文件**：0 ｜ **写入文件**：0

## 调用关系
**本程序调用：**

- `open_output_file`

**被以下程序调用**（dataview 实时反查）：

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

<!-- USER-NOTES-START -->
## 我的笔记
（在此自由记录：逐行注解、关键变量、个人理解。重跑生成脚本时本段会被保留。）
<!-- USER-NOTES-END -->
