---
type: source
subtype: subroutine
tags:
  - swat/源码
  - swat/待读
file: proc_cal.f90
subroutine: proc_cal
module:
  - hydrograph_module
  - calibration_data_module
calls:
  - cal_parm_read
  - cal_parmchg_read
  - pl_read_regions_cal
  - pl_read_parms_cal
  - cal_conditions
  - calsoft_read_codes
  - lcu_read_softcal
  - ls_read_lsparms_cal
  - aqu_read_elements
  - ch_read_elements
  - res_read_elements
  - rec_read_elements
  - ch_read_orders_cal
  - ch_read_parms_cal
  - cal_allo_init
reads: []
writes: []
purpose: ""
---

# proc_cal

> [!info] 概要
> 待补充

## 基本信息
- **类型**：`subroutine`
- **源文件**：`proc_cal.f90`
- **使用模块**：[[hydrograph_module.f90]]、[[calibration_data_module.f90]]
- **调用子程序**：15 个 ｜ **读取文件**：0 ｜ **写入文件**：0

## 调用关系
**本程序调用：**

- [[cal_parm_read.f90]]
- [[cal_parmchg_read.f90]]
- [[pl_read_regions_cal.f90]]
- [[pl_read_parms_cal.f90]]
- [[cal_conditions.f90]]
- [[calsoft_read_codes.f90]]
- [[lcu_read_softcal.f90]]
- `ls_read_lsparms_cal`
- [[aqu_read_elements.f90]]
- [[ch_read_elements.f90]]
- [[res_read_elements.f90]]
- [[rec_read_elements.f90]]
- [[ch_read_orders_cal.f90]]
- [[ch_read_parms_cal.f90]]
- [[cal_allo_init.f90]]

**被以下程序调用**（dataview 实时反查）：

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

<!-- USER-NOTES-START -->
## 我的笔记
（在此自由记录：逐行注解、关键变量、个人理解。重跑生成脚本时本段会被保留。）
<!-- USER-NOTES-END -->
