---
type: source
subtype: subroutine
tags:
  - swat/源码
  - swat/待读
file: copy_file.f90
subroutine: copy_file
module: []
calls: []
reads:
  - source
writes:
  - destination
purpose: ""
---

# copy_file

> [!info] 概要
> 待补充

## 基本信息
- **类型**：`subroutine`
- **源文件**：`copy_file.f90`
- **使用模块**：—
- **调用子程序**：0 个 ｜ **读取文件**：1 ｜ **写入文件**：1

## 调用关系
（无 call 语句，叶子节点）

**被以下程序调用**（dataview 实时反查）：

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## 文件读写
- **写入**：`destination`
- **读取**：`source` _（变量，见 file.cio）_

<!-- USER-NOTES-START -->
## 我的笔记
（在此自由记录：逐行注解、关键变量、个人理解。重跑生成脚本时本段会被保留。）
<!-- USER-NOTES-END -->
