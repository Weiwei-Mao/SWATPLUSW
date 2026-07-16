---
type: source
subtype: subroutine
tags:
  - swat/源码
  - swat/待读
file: proc_date_time.f90
subroutine: proc_date_time
module:
  - time_module
calls:
  - date_and_time
  - cli_petmeas
  - cli_pmeas
  - cli_tmeas
  - cli_smeas
  - cli_hmeas
  - cli_wmeas
  - cli_wgnread
reads: []
writes: []
purpose: ""
---

# proc_date_time

> [!info] 概要
> 待补充

## 基本信息
- **类型**：`subroutine`
- **源文件**：`proc_date_time.f90`
- **使用模块**：[[time_module.f90]]
- **调用子程序**：8 个 ｜ **读取文件**：0 ｜ **写入文件**：0

## 调用关系
**本程序调用：**

- `date_and_time`
- [[cli_petmeas.f90]]
- [[cli_pmeas.f90]]
- [[cli_tmeas.f90]]
- [[cli_smeas.f90]]
- [[cli_hmeas.f90]]
- [[cli_wmeas.f90]]
- [[cli_wgnread.f90]]

**被以下程序调用**（dataview 实时反查）：

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

<!-- USER-NOTES-START -->
## 我的笔记
（在此自由记录：逐行注解、关键变量、个人理解。重跑生成脚本时本段会被保留。）
<!-- USER-NOTES-END -->
