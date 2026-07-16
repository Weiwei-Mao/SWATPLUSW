---
type: source
subtype: subroutine
tags:
  - swat/源码
  - swat/待读
file: mgt_operatn.f90
subroutine: mgt_operatn
module:
  - mgt_operations_module
  - hru_module
  - plant_module
  - time_module
calls:
  - mgt_sched
reads: []
writes: []
purpose: "this subroutine performs all management operations"
---

# mgt_operatn

> [!info] 概要
> this subroutine performs all management operations

## 基本信息
- **类型**：`subroutine`
- **源文件**：`mgt_operatn.f90`
- **使用模块**：[[mgt_operations_module.f90]]、[[hru_module.f90]]、[[plant_module.f90]]、[[time_module.f90]]
- **调用子程序**：1 个 ｜ **读取文件**：0 ｜ **写入文件**：0

## 调用关系
**本程序调用：**

- [[mgt_sched.f90]]

**被以下程序调用**（dataview 实时反查）：

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

<!-- USER-NOTES-START -->
## 我的笔记
（在此自由记录：逐行注解、关键变量、个人理解。重跑生成脚本时本段会被保留。）
<!-- USER-NOTES-END -->
