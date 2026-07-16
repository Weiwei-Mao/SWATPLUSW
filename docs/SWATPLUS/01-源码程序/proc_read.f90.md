---
type: source
subtype: subroutine
tags:
  - swat/源码
  - swat/待读
file: proc_read.f90
subroutine: proc_read
module: []
calls:
  - ch_read_temp
  - cli_read_atmodep
  - cli_staread
  - constit_db_read
  - pest_metabolite_read
  - soil_plant_init
  - solt_db_read
  - pest_hru_aqu_read
  - path_hru_aqu_read
  - hmet_hru_aqu_read
  - salt_hru_read
  - salt_aqu_read
  - salt_irr_read
  - salt_plant_read
  - cli_read_atmodep_salt
  - salt_roadsalt_read
  - salt_uptake_read
  - salt_urban_read
  - salt_fert_read
  - cs_hru_read
  - cs_aqu_read
  - cli_read_atmodep_cs
  - cs_irr_read
  - cs_plant_read
  - cs_uptake_read
  - cs_reactions_read
  - cs_urban_read
  - cs_fert_read
  - topo_read
  - field_read
  - hydrol_read
  - shade_factor_read
  - snowdb_read
  - soil_db_read
  - soil_lte_db_read
reads: []
writes: []
purpose: ""
---

# proc_read

> [!info] 概要
> 待补充

## 基本信息
- **类型**：`subroutine`
- **源文件**：`proc_read.f90`
- **使用模块**：—
- **调用子程序**：35 个 ｜ **读取文件**：0 ｜ **写入文件**：0

## 调用关系
**本程序调用：**

- [[ch_read_temp.f90]]
- [[cli_read_atmodep.f90]]
- [[cli_staread.f90]]
- [[constit_db_read.f90]]
- [[pest_metabolite_read.f90]]
- [[soil_plant_init.f90]]
- [[solt_db_read.f90]]
- [[pest_hru_aqu_read.f90]]
- [[path_hru_aqu_read.f90]]
- [[hmet_hru_aqu_read.f90]]
- [[salt_hru_read.f90]]
- [[salt_aqu_read.f90]]
- [[salt_irr_read.f90]]
- [[salt_plant_read.f90]]
- [[cli_read_atmodep_salt.f90]]
- [[salt_roadsalt_read.f90]]
- [[salt_uptake_read.f90]]
- [[salt_urban_read.f90]]
- [[salt_fert_read.f90]]
- [[cs_hru_read.f90]]
- [[cs_aqu_read.f90]]
- [[cli_read_atmodep_cs.f90]]
- [[cs_irr_read.f90]]
- [[cs_plant_read.f90]]
- [[cs_uptake_read.f90]]
- [[cs_reactions_read.f90]]
- [[cs_urban_read.f90]]
- [[cs_fert_read.f90]]
- [[topo_read.f90]]
- [[field_read.f90]]
- [[hydrol_read.f90]]
- [[shade_factor_read.f90]]
- [[snowdb_read.f90]]
- [[soil_db_read.f90]]
- [[soil_lte_db_read.f90]]

**被以下程序调用**（dataview 实时反查）：

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

<!-- USER-NOTES-START -->
## 我的笔记
（在此自由记录：逐行注解、关键变量、个人理解。重跑生成脚本时本段会被保留。）
<!-- USER-NOTES-END -->
