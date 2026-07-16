---
type: source
subtype: subroutine
tags:
  - swat/源码
  - swat/待读
file: command.f90
subroutine: command
module:
  - time_module
  - hydrograph_module
  - ru_module
  - channel_module
  - hru_lte_module
  - aquifer_module
  - sd_channel_module
  - reservoir_module
  - organic_mineral_mass_module
  - constituent_mass_module
  - hru_module
  - basin_module
  - maximum_data_module
  - gwflow_module
  - soil_module
  - recall_module
  - water_allocation_module
calls:
  - wallo_control
  - hru_control
  - hyddep_output
  - hru_lte_control
  - ru_control
  - gwflow_simulate
  - aqu_1d_control
  - res_control
  - recall_nut
  - recall_salt
  - recall_cs
  - constit_hyd_mult
  - sd_channel_control3
  - flow_dur_curve
  - hydout_output
  - obj_output
  - wallo_allo_output
  - wallo_trn_output
  - wallo_treat_output
  - wallo_use_output
  - manure_source_output
  - manure_demand_output
  - hru_lte_output
  - hru_output
  - hru_carbon_output
  - wetland_output
  - wet_salt_output
  - wet_cs_output
  - hru_pesticide_output
  - hru_pathogen_output
  - hru_salt_output
  - hru_cs_output
  - soil_nutcarb_write
  - soil_carbvar_write
  - soil_nutcarb_write_legacy
  - soil_carbvar_write_legacy
  - aquifer_output
  - aqu_salt_output
  - aqu_cs_output
  - aqu_pesticide_output
  - channel_output
  - sd_chanmorph_output
  - sd_chanbud_output
  - sd_channel_output
  - cha_pesticide_output
  - ch_salt_output
  - ch_cs_output
  - cs_str_output
  - reservoir_output
  - res_pesticide_output
  - res_salt_output
  - res_cs_output
  - ru_output
  - ru_salt_output
  - ru_cs_output
  - recall_output
  - hydin_output
  - basin_ch_pest_output
  - basin_res_pest_output
  - basin_ls_pest_output
  - basin_aqu_pest_output
  - basin_output
  - lsu_output
  - lsu_carbon_output
  - basin_aquifer_output
  - basin_reservoir_output
  - basin_channel_output
  - basin_chanmorph_output
  - basin_chanbud_output
  - basin_sdchannel_output
  - basin_recall_output
  - salt_balance
  - cs_balance
reads: []
writes: []
purpose: "for every day of simulation, this subroutine steps through the command；lines in the watershed configuration (.fig) file. Depending on the；command code on the .fig file line, a command loop is accessed"
---

# command

> [!info] 概要
> for every day of simulation, this subroutine steps through the command；lines in the watershed configuration (.fig) file. Depending on the；command code on the .fig file line, a command loop is accessed

## 基本信息
- **类型**：`subroutine`
- **源文件**：`command.f90`
- **使用模块**：[[time_module.f90]]、[[hydrograph_module.f90]]、[[ru_module.f90]]、[[channel_module.f90]]、[[hru_lte_module.f90]]、[[aquifer_module.f90]]、[[sd_channel_module.f90]]、[[reservoir_module.f90]]、[[organic_mineral_mass_module.f90]]、[[constituent_mass_module.f90]]、[[hru_module.f90]]、[[basin_module.f90]]、[[maximum_data_module.f90]]、[[gwflow_module.f90]]、[[soil_module.f90]]、[[recall_module.f90]]、[[water_allocation_module.f90]]
- **调用子程序**：73 个 ｜ **读取文件**：0 ｜ **写入文件**：0

## 调用关系
**本程序调用：**

- [[wallo_control.f90]]
- [[hru_control.f90]]
- [[hyddep_output.f90]]
- [[hru_lte_control.f90]]
- [[ru_control.f90]]
- [[gwflow_simulate.f90]]
- [[aqu_1d_control.f90]]
- [[res_control.f90]]
- [[recall_nut.f90]]
- [[recall_salt.f90]]
- [[recall_cs.f90]]
- [[constit_hyd_mult.f90]]
- [[sd_channel_control3.f90]]
- [[flow_dur_curve.f90]]
- [[hydout_output.f90]]
- [[obj_output.f90]]
- [[wallo_allo_output.f90]]
- [[wallo_trn_output.f90]]
- [[wallo_treat_output.f90]]
- [[wallo_use_output.f90]]
- [[manure_source_output.f90]]
- [[manure_demand_output.f90]]
- [[hru_lte_output.f90]]
- [[hru_output.f90]]
- [[hru_carbon_output.f90]]
- [[wetland_output.f90]]
- [[wet_salt_output.f90]]
- [[wet_cs_output.f90]]
- [[hru_pesticide_output.f90]]
- [[hru_pathogen_output.f90]]
- [[hru_salt_output.f90]]
- [[hru_cs_output.f90]]
- [[soil_nutcarb_write.f90]]
- [[soil_carbvar_write.f90]]
- [[soil_nutcarb_write_legacy.f90]]
- [[soil_carbvar_write_legacy.f90]]
- [[aquifer_output.f90]]
- [[aqu_salt_output.f90]]
- [[aqu_cs_output.f90]]
- [[aqu_pesticide_output.f90]]
- [[channel_output.f90]]
- [[sd_chanmorph_output.f90]]
- [[sd_chanbud_output.f90]]
- [[sd_channel_output.f90]]
- [[cha_pesticide_output.f90]]
- [[ch_salt_output.f90]]
- [[ch_cs_output.f90]]
- [[cs_str_output.f90]]
- [[reservoir_output.f90]]
- [[res_pesticide_output.f90]]
- [[res_salt_output.f90]]
- [[res_cs_output.f90]]
- [[ru_output.f90]]
- [[ru_salt_output.f90]]
- [[ru_cs_output.f90]]
- [[recall_output.f90]]
- [[hydin_output.f90]]
- [[basin_ch_pest_output.f90]]
- [[basin_res_pest_output.f90]]
- [[basin_ls_pest_output.f90]]
- [[basin_aqu_pest_output.f90]]
- [[basin_output.f90]]
- [[lsu_output.f90]]
- [[lsu_carbon_output.f90]]
- [[basin_aquifer_output.f90]]
- [[basin_reservoir_output.f90]]
- [[basin_channel_output.f90]]
- [[basin_chanmorph_output.f90]]
- [[basin_chanbud_output.f90]]
- [[basin_sdchannel_output.f90]]
- [[basin_recall_output.f90]]
- [[salt_balance.f90]]
- [[cs_balance.f90]]

**被以下程序调用**（dataview 实时反查）：

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

<!-- USER-NOTES-START -->
## 我的笔记
（在此自由记录：逐行注解、关键变量、个人理解。重跑生成脚本时本段会被保留。）
<!-- USER-NOTES-END -->
