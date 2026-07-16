---
type: source
subtype: subroutine
tags:
  - swat/源码
  - swat/待读
file: rcurv_interp_dep.f90
subroutine: rcurv_interp_dep
module:
  - sd_channel_module
calls:
  - chrc_interp
reads: []
writes: []
purpose: "this subroutine interpolates between points on a rating curve given flow rate"
---

# rcurv_interp_dep

> [!info] 概要
> this subroutine interpolates between points on a rating curve given flow rate

## 基本信息
- **类型**：`subroutine`
- **源文件**：`rcurv_interp_dep.f90`
- **使用模块**：[[sd_channel_module.f90]]
- **调用子程序**：1 个 ｜ **读取文件**：0 ｜ **写入文件**：0

## 调用关系
**本程序调用：**

- `chrc_interp`

**被以下程序调用**（dataview 实时反查）：

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

<!-- USER-NOTES-START -->
## 我的笔记
（在此自由记录：逐行注解、关键变量、个人理解。重跑生成脚本时本段会被保留。）
<!-- USER-NOTES-END -->
