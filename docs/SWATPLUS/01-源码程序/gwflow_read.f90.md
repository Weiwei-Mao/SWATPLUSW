---
type: source
subtype: subroutine
tags:
  - swat/源码
  - swat/待读
file: gwflow_read.f90
subroutine: gwflow_read
module:
  - gwflow_module
  - hydrograph_module
  - sd_channel_module
  - maximum_data_module
  - hru_module
  - reservoir_data_module
  - cs_data_module
  - constituent_mass_module
  - water_allocation_module
  - utils
calls:
  - date_and_time
  - split_line
  - gwflow_output_init
reads:
  - codes.gw
  - zones.gw
  - cells.gw
  - cellcon.gw
  - outputs.gw
  - hru_pump.gw
  - pumpex.gw
  - tile.gw
  - rescell.gw
  - floodplain.gw
  - gwflow_canal.con
  - phreato.gw
  - phreato_cell.gw
  - tvheads.gw
  - solute.gw
  - cell_sol.gw
  - minerals.gw
  - ponds.gw
  - pond_cell.gw
  - pond_div.gw
  - lsucell.gw
  - hrucell.gw
  - transit.gw
  - gwflow_transit_cell
  - gwflow_transit_chan
  - gwflow_transit_tile
  - sw_group.gw
writes:
  - gwflow_obs_day.txt
  - gwflow_obs_mon.txt
  - gwflow_obs_yr.txt
  - gwflow_obs_aa.txt
  - gwflow_chan_obs_flow_day.txt
  - gwflow_chan_obs_no3_day.txt
  - gwflow_hru_pump_day.txt
  - gwflow_hru_pump_mon.txt
  - gwflow_hru_pump_yr.txt
  - gwflow_hru_pump_aa.txt
  - gwflow_cell_wb_ppag_obs_day.txt
  - gwflow_tile_group_day.txt
  - gwflow_canal_wb_day.txt
  - gwflow_canal_sol_day.txt
  - gwflow_pond_wb_day.txt
  - gwflow_pond_sol_day.txt
  - gwflow_pond_mass_day.txt
  - gwflow_pond_conc_day.txt
  - gwflow_gwsw_group_day.txt
  - gwflow_chan_hydsep_day.txt
purpose: ""
---

# gwflow_read

> [!info] 概要
> 待补充

## 基本信息
- **类型**：`subroutine`
- **源文件**：`gwflow_read.f90`
- **使用模块**：[[gwflow_module.f90]]、[[hydrograph_module.f90]]、[[sd_channel_module.f90]]、[[maximum_data_module.f90]]、[[hru_module.f90]]、[[reservoir_data_module.f90]]、[[cs_data_module.f90]]、[[constituent_mass_module.f90]]、[[water_allocation_module.f90]]、[[utils.f90]]
- **调用子程序**：3 个 ｜ **读取文件**：27 ｜ **写入文件**：20

## 调用关系
**本程序调用：**

- `date_and_time`
- `split_line`
- `gwflow_output_init`

**被以下程序调用**（dataview 实时反查）：

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## 文件读写
- **写入**：`gwflow_obs_day.txt`、`gwflow_obs_mon.txt`、`gwflow_obs_yr.txt`、`gwflow_obs_aa.txt`、`gwflow_chan_obs_flow_day.txt`、`gwflow_chan_obs_no3_day.txt`、`gwflow_hru_pump_day.txt`、`gwflow_hru_pump_mon.txt`、`gwflow_hru_pump_yr.txt`、`gwflow_hru_pump_aa.txt`、`gwflow_cell_wb_ppag_obs_day.txt`、`gwflow_tile_group_day.txt`、`gwflow_canal_wb_day.txt`、`gwflow_canal_sol_day.txt`、`gwflow_pond_wb_day.txt`、`gwflow_pond_sol_day.txt`、`gwflow_pond_mass_day.txt`、`gwflow_pond_conc_day.txt`、`gwflow_gwsw_group_day.txt`、`gwflow_chan_hydsep_day.txt`
- **读取**：`codes.gw`、`zones.gw`、`cells.gw`、`cellcon.gw`、`outputs.gw`、`hru_pump.gw`、`pumpex.gw`、`tile.gw`、`rescell.gw`、`floodplain.gw`、`gwflow_canal.con`、`phreato.gw`、`phreato_cell.gw`、`tvheads.gw`、`solute.gw`、`cell_sol.gw`、`minerals.gw`、`ponds.gw`、`pond_cell.gw`、`pond_div.gw`、`lsucell.gw`、`hrucell.gw`、`transit.gw`、`gwflow_transit_cell` _（变量，见 file.cio）_、`gwflow_transit_chan` _（变量，见 file.cio）_、`gwflow_transit_tile` _（变量，见 file.cio）_、`sw_group.gw`

<!-- USER-NOTES-START -->
## 我的笔记
（在此自由记录：逐行注解、关键变量、个人理解。重跑生成脚本时本段会被保留。）
<!-- USER-NOTES-END -->
