---
type: source
subtype: subroutine
tags:
  - swat/源码
  - swat/待读
file: proc_aqu.f90
subroutine: proc_aqu
module:
  - hydrograph_module
calls:
  - aqu_read
  - aqu_initial
  - aqu_read_init
  - aqu_read_init_cs
reads: []
writes: []
purpose: ""
---

# proc_aqu

> [!info] 概要
> 待补充

## 基本信息
- **类型**：`subroutine`
- **源文件**：`proc_aqu.f90`
- **使用模块**：[[hydrograph_module.f90]]
- **调用子程序**：4 个 ｜ **读取文件**：0 ｜ **写入文件**：0

## 调用关系
**本程序调用：**

- [[aqu_read.f90]]
- [[aqu_initial.f90]]
- [[aqu_read_init.f90]]
- [[aqu_read_init_cs.f90]]

**被以下程序调用**（dataview 实时反查）：

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

<!-- USER-NOTES-START -->
## 我的笔记
（在此自由记录：逐行注解、关键变量、个人理解。重跑生成脚本时本段会被保留。）
<!-- USER-NOTES-END -->
