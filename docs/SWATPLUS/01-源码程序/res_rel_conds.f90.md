---
type: source
subtype: subroutine
tags:
  - swat/源码
  - swat/待读
file: res_rel_conds.f90
subroutine: res_rel_conds
module:
  - reservoir_conditions_module
  - time_module
  - hydrograph_module
calls:
  - cond_real_c
  - cond_integer_c
reads: []
writes: []
purpose: ""
---

# res_rel_conds

> [!info] 概要
> 待补充

## 基本信息
- **类型**：`subroutine`
- **源文件**：`res_rel_conds.f90`
- **使用模块**：[[reservoir_conditions_module.f90]]、[[time_module.f90]]、[[hydrograph_module.f90]]
- **调用子程序**：2 个 ｜ **读取文件**：0 ｜ **写入文件**：0

## 调用关系
**本程序调用：**

- [[cond_real_c.f90]]
- [[cond_integer_c.f90]]

**被以下程序调用**（dataview 实时反查）：

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

<!-- USER-NOTES-START -->
## 我的笔记
（在此自由记录：逐行注解、关键变量、个人理解。重跑生成脚本时本段会被保留。）
<!-- USER-NOTES-END -->
