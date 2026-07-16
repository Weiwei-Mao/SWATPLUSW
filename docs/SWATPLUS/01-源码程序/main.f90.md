---
type: source
subtype: program
tags:
  - swat/源码
  - swat/待读
file: main.f90
subroutine: main
module:
  - time_module
  - hydrograph_module
  - maximum_data_module
  - calibration_data_module
  - hru_module
calls:
  - proc_bsn
  - proc_date_time
  - proc_db
  - proc_read
  - hyd_connect
  - recalldb_read
  - exco_db_read
  - dr_db_read
  - cli_lapse
  - object_read_output
  - om_water_init
  - pest_cha_res_read
  - path_cha_res_read
  - salt_cha_read
  - cs_cha_read
  - lsu_read_elements
  - proc_hru
  - proc_cha
  - proc_aqu
  - dtbl_lum_read
  - hru_lte_read
  - proc_cond
  - res_read_weir
  - dtbl_res_read
  - dtbl_scen_read
  - cal_cond_read
  - manure_allocation_read
  - dtbl_flocon_read
  - om_treat_read
  - om_use_read
  - om_osrc_read
  - water_treatment_read
  - water_use_read
  - water_tower_read
  - water_pipe_read
  - water_canal_read
  - water_allocation_read
  - hru_dtbl_actions_init
  - proc_res
  - wet_read_hyd
  - wet_read
  - wet_read_salt_cs
  - wet_all_initial
  - wet_fp_init
  - proc_cal
  - soil_nutcarb_init
  - proc_open
  - unit_hyd_ru_hru
  - dr_ru
  - hyd_connect_out
  - command
  - time_control
  - calsoft_control
  - cal_parmchg_read
  - calhard_control
  - swift_output
  - date_and_time
reads: []
writes:
  - simulation.out
  - erosion.txt
  - success.fin
purpose: ""
---

# main

> [!info] 概要
> 待补充

## 基本信息
- **类型**：`program`
- **源文件**：`main.f90`
- **使用模块**：[[time_module.f90]]、[[hydrograph_module.f90]]、[[maximum_data_module.f90]]、[[calibration_data_module.f90]]、[[hru_module.f90]]
- **调用子程序**：57 个 ｜ **读取文件**：0 ｜ **写入文件**：3

## 调用关系
**本程序调用：**

- [[proc_bsn.f90]]
- [[proc_date_time.f90]]
- [[proc_db.f90]]
- [[proc_read.f90]]
- [[hyd_connect.f90]]
- `recalldb_read`
- [[exco_db_read.f90]]
- [[dr_db_read.f90]]
- [[cli_lapse.f90]]
- [[object_read_output.f90]]
- [[om_water_init.f90]]
- [[pest_cha_res_read.f90]]
- [[path_cha_res_read.f90]]
- [[salt_cha_read.f90]]
- [[cs_cha_read.f90]]
- [[lsu_read_elements.f90]]
- [[proc_hru.f90]]
- [[proc_cha.f90]]
- [[proc_aqu.f90]]
- [[dtbl_lum_read.f90]]
- [[hru_lte_read.f90]]
- [[proc_cond.f90]]
- [[res_read_weir.f90]]
- [[dtbl_res_read.f90]]
- [[dtbl_scen_read.f90]]
- [[cal_cond_read.f90]]
- [[manure_allocation_read.f90]]
- [[dtbl_flocon_read.f90]]
- [[om_treat_read.f90]]
- [[om_use_read.f90]]
- [[om_osrc_read.f90]]
- [[water_treatment_read.f90]]
- [[water_use_read.f90]]
- [[water_tower_read.f90]]
- [[water_pipe_read.f90]]
- [[water_canal_read.f90]]
- [[water_allocation_read.f90]]
- [[hru_dtbl_actions_init.f90]]
- [[proc_res.f90]]
- [[wet_read_hyd.f90]]
- [[wet_read.f90]]
- [[wet_read_salt_cs.f90]]
- [[wet_all_initial.f90]]
- [[wet_fp_init.f90]]
- [[proc_cal.f90]]
- [[soil_nutcarb_init.f90]]
- [[proc_open.f90]]
- [[unit_hyd_ru_hru.f90]]
- [[dr_ru.f90]]
- [[hyd_connect_out.f90]]
- [[command.f90]]
- [[time_control.f90]]
- [[calsoft_control.f90]]
- [[cal_parmchg_read.f90]]
- [[calhard_control.f90]]
- [[swift_output.f90]]
- `date_and_time`

**被以下程序调用**（dataview 实时反查）：

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## 文件读写
- **写入**：`simulation.out`、`erosion.txt`、`success.fin`

<!-- USER-NOTES-START -->
## 我的笔记
（在此自由记录：逐行注解、关键变量、个人理解。重跑生成脚本时本段会被保留。）

- Line 30: 打开文件 `simulation.out`（unit 9003）
- Line 38: 打开文件 `erosion.txt`（unit 888, recl 1500）
- 调用入口 [[proc_bsn.f90]]
<!-- USER-NOTES-END -->
