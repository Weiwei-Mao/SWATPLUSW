---
type: source
subtype: subroutine
tags:
  - swat/源码
  - swat/待读
file: proc_res.f90
subroutine: proc_res
module:
  - hydrograph_module
calls:
  - res_read_hyd
  - res_read_sed
  - res_read_nut
  - res_read_init
  - res_read_saltdb
  - res_read_csdb
  - res_read_conds
  - res_allo
  - res_objects
  - res_read
  - res_read_salt_cs
  - res_initial
reads: []
writes: []
purpose: ""
---

# proc_res

> [!info] 概要
> 待补充

## 基本信息
- **类型**：`subroutine`
- **源文件**：`proc_res.f90`
- **使用模块**：[[hydrograph_module.f90]]
- **调用子程序**：12 个 ｜ **读取文件**：0 ｜ **写入文件**：0

## 调用关系
**本程序调用：**

- [[res_read_hyd.f90]]
- [[res_read_sed.f90]]
- [[res_read_nut.f90]]
- [[res_read_init.f90]]
- [[res_read_saltdb.f90]]
- [[res_read_csdb.f90]]
- [[res_read_conds.f90]]
- [[res_allo.f90]]
- [[res_objects.f90]]
- [[res_read.f90]]
- [[res_read_salt_cs.f90]]
- [[res_initial.f90]]

**被以下程序调用**（dataview 实时反查）：

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

<!-- USER-NOTES-START -->
## 我的笔记
（在此自由记录：逐行注解、关键变量、个人理解。重跑生成脚本时本段会被保留。）
<!-- USER-NOTES-END -->
