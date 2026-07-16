---
type: source
subtype: subroutine
tags:
  - swat/源码
  - swat/待读
file: basin_read_cc.f90
subroutine: basin_read_cc
module:
  - input_file_module
  - basin_module
calls: []
reads:
  - in_basin%codes_bas
  - pet.cli
writes: []
purpose: ""
---

# basin_read_cc

> [!info] 概要
> 待补充

## 基本信息
- **类型**：`subroutine`
- **源文件**：`basin_read_cc.f90`
- **使用模块**：[[input_file_module.f90]]、[[basin_module.f90]]
- **调用子程序**：0 个 ｜ **读取文件**：2 ｜ **写入文件**：0

## 调用关系
（无 call 语句，叶子节点）

**被以下程序调用**（dataview 实时反查）：

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## 文件读写
- **读取**：`in_basin%codes_bas` _（变量，见 file.cio）_、`pet.cli`

<!-- USER-NOTES-START -->
## 我的笔记
（在此自由记录：逐行注解、关键变量、个人理解。重跑生成脚本时本段会被保留。）

- use: `input_file_module`, [[basin_module.f90]]
- Line 13–28: 从 `codes.bsn` 读取 `bsn_cc`（basin control codes）
- Line 30–40: 若 `bsn_cc%pet == 3`（输入潜在蒸散发），则检查输入文件 `pet.cli` 是否存在
<!-- USER-NOTES-END -->
