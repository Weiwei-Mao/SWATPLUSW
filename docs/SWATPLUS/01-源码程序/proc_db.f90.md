---
type: source
subtype: subroutine
tags:
  - swat/源码
  - swat/待读
file: proc_db.f90
subroutine: proc_db
module: []
calls:
  - plant_parm_read
  - plantparm_init
  - plant_transplant_read
  - till_parm_read
  - pest_parm_read
  - fert_parm_read
  - manure_orgmin_read
  - manure_db_read
  - urban_parm_read
  - path_parm_read
  - septic_parm_read
  - mgt_read_irrops
  - mgt_read_chemapp
  - mgt_read_harvops
  - mgt_read_grazeops
  - mgt_read_sweepops
  - mgt_read_fireops
  - mgt_read_mgtops
  - mgt_read_puddle
  - sdr_read
  - sep_read
  - scen_read_grwway
  - scen_read_filtstrip
  - scen_read_bmpuser
  - sat_buff_read
  - readpcom
  - cntbl_read
  - cons_prac_read
  - overland_n_read
  - landuse_read
reads: []
writes: []
purpose: ""
---

# proc_db

> [!info] 概要
> 待补充

## 基本信息
- **类型**：`subroutine`
- **源文件**：`proc_db.f90`
- **使用模块**：—
- **调用子程序**：30 个 ｜ **读取文件**：0 ｜ **写入文件**：0

## 调用关系
**本程序调用：**

- [[plant_parm_read.f90]]
- [[plantparm_init.f90]]
- [[plant_transplant_read.f90]]
- [[till_parm_read.f90]]
- [[pest_parm_read.f90]]
- [[fert_parm_read.f90]]
- [[manure_orgmin_read.f90]]
- [[manure_db_read.f90]]
- [[urban_parm_read.f90]]
- [[path_parm_read.f90]]
- [[septic_parm_read.f90]]
- [[mgt_read_irrops.f90]]
- [[mgt_read_chemapp.f90]]
- [[mgt_read_harvops.f90]]
- [[mgt_read_grazeops.f90]]
- [[mgt_read_sweepops.f90]]
- [[mgt_read_fireops.f90]]
- [[mgt_read_mgtops.f90]]
- [[mgt_read_puddle.f90]]
- [[sdr_read.f90]]
- [[sep_read.f90]]
- [[scen_read_grwway.f90]]
- [[scen_read_filtstrip.f90]]
- [[scen_read_bmpuser.f90]]
- [[sat_buff_read.f90]]
- [[readpcom.f90]]
- [[cntbl_read.f90]]
- [[cons_prac_read.f90]]
- [[overland_n_read.f90]]
- [[landuse_read.f90]]

**被以下程序调用**（dataview 实时反查）：

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

<!-- USER-NOTES-START -->
## 我的笔记
（在此自由记录：逐行注解、关键变量、个人理解。重跑生成脚本时本段会被保留。）
<!-- USER-NOTES-END -->
