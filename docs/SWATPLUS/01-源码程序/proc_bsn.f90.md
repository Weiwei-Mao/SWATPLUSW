---
type: source
subtype: subroutine
tags:
  - swat/源码
  - swat/待读
file: proc_bsn.f90
subroutine: proc_bsn
module:
  - time_module
  - output_path_module
calls:
  - readcio_read
  - open_output_file
  - basin_read_cc
  - basin_read_objs
  - time_read
  - basin_read_prm
  - basin_prm_default
  - basin_print_codes_read
  - co2_read
  - carbon_bsn_read
  - carbon_layers_read
reads: []
writes: []
purpose: ""
---

# proc_bsn

> [!info] 概要
> 待补充

## 基本信息
- **类型**：`subroutine`
- **源文件**：`proc_bsn.f90`
- **使用模块**：[[time_module.f90]]、[[output_path_module.f90]]
- **调用子程序**：11 个 ｜ **读取文件**：0 ｜ **写入文件**：0

## 调用关系
**本程序调用：**

- [[readcio_read.f90]]
- `open_output_file`
- [[basin_read_cc.f90]]
- [[basin_read_objs.f90]]
- [[time_read.f90]]
- [[basin_read_prm.f90]]
- [[basin_prm_default.f90]]
- [[basin_print_codes_read.f90]]
- [[co2_read.f90]]
- [[carbon_bsn_read.f90]]
- [[carbon_layers_read.f90]]

**被以下程序调用**（dataview 实时反查）：

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

<!-- USER-NOTES-START -->
## 我的笔记
（在此自由记录：逐行注解、关键变量、个人理解。重跑生成脚本时本段会被保留。）

- use: `time_module`, `output_path_module`
- Line 12: call [[readcio_read.f90]]
- Line 15: call `open_output_file(9000, "files_out.out")`
- Line 18: call `open_output_file(9001, "diagnostics.out", 8000)` —— unit 9001, recl 8000
- Line 21: call `open_output_file(9004, "area_calc.out", 80000)` —— unit 9004, recl 80000
- Line 23: call [[basin_read_cc.f90]]
<!-- USER-NOTES-END -->
