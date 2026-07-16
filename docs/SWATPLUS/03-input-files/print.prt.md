---
type: input
tags:
  - swat/input
file: print.prt
ext: prt
cio_field: prt
read_by:
  - basin_print_codes_read.f90
purpose: ""
---

# print.prt

> [!info] Input File
> Declared in `file.cio` field `prt`. See [[file.cio]] for the controlling file map.

## Overview
- **Declared in `file.cio` field**: `prt`
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[basin_print_codes_read.f90]]

## File Structure
- [[basin_print_codes_read.f90]] source line 24: reads `titldum`
- [[basin_print_codes_read.f90]] source line 26: reads `header`
- [[basin_print_codes_read.f90]] source line 28: reads `pco%nyskip`, `pco%day_start`, `pco%yrc_start`, `pco%day_end`, `pco%yrc_end`, `pco%int_day`
- [[basin_print_codes_read.f90]] source line 30: reads `header`
- [[basin_print_codes_read.f90]] source line 32: reads `pco%aa_numint`
- [[basin_print_codes_read.f90]] source line 36: reads `pco%aa_numint`, `(pco%aa_yrs(ii), ii = 1, pco%aa_numint)`
- [[basin_print_codes_read.f90]] source line 42: reads `header`
- [[basin_print_codes_read.f90]] source line 44: reads `pco%csvout`, `pco%use_obj_labels`, `pco%cdfout`
- [[basin_print_codes_read.f90]] source line 48: reads `header`
- [[basin_print_codes_read.f90]] source line 50: reads `pco%crop_yld`, `pco%mgtout`, `pco%hydcon`, `pco%fdcout`
- [[basin_print_codes_read.f90]] source line 55: reads `header`
- [[basin_print_codes_read.f90]] source line 58: reads `name`, `pco%wb_bsn%d`, `pco%wb_bsn%m`, `pco%wb_bsn%y`, `pco%wb_bsn%a`
- [[basin_print_codes_read.f90]] source line 60: reads `name`, `pco%nb_bsn%d`, `pco%nb_bsn%m`, `pco%nb_bsn%y`, `pco%nb_bsn%a`
- [[basin_print_codes_read.f90]] source line 62: reads `name`, `pco%ls_bsn%d`, `pco%ls_bsn%m`, `pco%ls_bsn%y`, `pco%ls_bsn%a`
- [[basin_print_codes_read.f90]] source line 64: reads `name`, `pco%pw_bsn%d`, `pco%pw_bsn%m`, `pco%pw_bsn%y`, `pco%pw_bsn%a`
- [[basin_print_codes_read.f90]] source line 66: reads `name`, `pco%aqu_bsn%d`, `pco%aqu_bsn%m`, `pco%aqu_bsn%y`, `pco%aqu_bsn%a`
- [[basin_print_codes_read.f90]] source line 68: reads `name`, `pco%res_bsn%d`, `pco%res_bsn%m`, `pco%res_bsn%y`, `pco%res_bsn%a`
- [[basin_print_codes_read.f90]] source line 70: reads `name`, `pco%chan_bsn%d`, `pco%chan_bsn%m`, `pco%chan_bsn%y`, `pco%chan_bsn%a`
- [[basin_print_codes_read.f90]] source line 72: reads `name`, `pco%sd_chan_bsn%d`, `pco%sd_chan_bsn%m`, `pco%sd_chan_bsn%y`, `pco%sd_chan_bsn%a`
- [[basin_print_codes_read.f90]] source line 74: reads `name`, `pco%recall_bsn%d`, `pco%recall_bsn%m`, `pco%recall_bsn%y`, `pco%recall_bsn%a`
- [[basin_print_codes_read.f90]] source line 77: reads `name`, `pco%wb_reg%d`, `pco%wb_reg%m`, `pco%wb_reg%y`, `pco%wb_reg%a`
- [[basin_print_codes_read.f90]] source line 79: reads `name`, `pco%nb_reg%d`, `pco%nb_reg%m`, `pco%nb_reg%y`, `pco%nb_reg%a`
- [[basin_print_codes_read.f90]] source line 81: reads `name`, `pco%ls_reg%d`, `pco%ls_reg%m`, `pco%ls_reg%y`, `pco%ls_reg%a`
- [[basin_print_codes_read.f90]] source line 83: reads `name`, `pco%pw_reg%d`, `pco%pw_reg%m`, `pco%pw_reg%y`, `pco%pw_reg%a`
- [[basin_print_codes_read.f90]] source line 85: reads `name`, `pco%aqu_reg%d`, `pco%aqu_reg%m`, `pco%aqu_reg%y`, `pco%aqu_reg%a`
- [[basin_print_codes_read.f90]] source line 87: reads `name`, `pco%res_reg%d`, `pco%res_reg%m`, `pco%res_reg%y`, `pco%res_reg%a`
- [[basin_print_codes_read.f90]] source line 89: reads `name`, `pco%sd_chan_reg%d`, `pco%sd_chan_reg%m`, `pco%sd_chan_reg%y`, `pco%sd_chan_reg%a`
- [[basin_print_codes_read.f90]] source line 91: reads `name`, `pco%recall_reg%d`, `pco%recall_reg%m`, `pco%recall_reg%y`, `pco%recall_reg%a`
- [[basin_print_codes_read.f90]] source line 93: reads `name`, `pco%water_allo%d`, `pco%water_allo%m`, `pco%water_allo%y`, `pco%water_allo%a`
- [[basin_print_codes_read.f90]] source line 96: reads `name`, `pco%wb_lsu%d`, `pco%wb_lsu%m`, `pco%wb_lsu%y`, `pco%wb_lsu%a`
- [[basin_print_codes_read.f90]] source line 98: reads `name`, `pco%nb_lsu%d`, `pco%nb_lsu%m`, `pco%nb_lsu%y`, `pco%nb_lsu%a`
- [[basin_print_codes_read.f90]] source line 100: reads `name`, `pco%ls_lsu%d`, `pco%ls_lsu%m`, `pco%ls_lsu%y`, `pco%ls_lsu%a`
- [[basin_print_codes_read.f90]] source line 102: reads `name`, `pco%pw_lsu%d`, `pco%pw_lsu%m`, `pco%pw_lsu%y`, `pco%pw_lsu%a`
- [[basin_print_codes_read.f90]] source line 105: reads `name`, `pco%wb_hru%d`, `pco%wb_hru%m`, `pco%wb_hru%y`, `pco%wb_hru%a`
- [[basin_print_codes_read.f90]] source line 107: reads `name`, `pco%nb_hru%d`, `pco%nb_hru%m`, `pco%nb_hru%y`, `pco%nb_hru%a`
- [[basin_print_codes_read.f90]] source line 109: reads `name`, `pco%ls_hru%d`, `pco%ls_hru%m`, `pco%ls_hru%y`, `pco%ls_hru%a`
- [[basin_print_codes_read.f90]] source line 111: reads `name`, `pco%pw_hru%d`, `pco%pw_hru%m`, `pco%pw_hru%y`, `pco%pw_hru%a`
- [[basin_print_codes_read.f90]] source line 115: reads `name`, `pco%wb_sd%d`, `pco%wb_sd%m`, `pco%wb_sd%y`, `pco%wb_sd%a`
- [[basin_print_codes_read.f90]] source line 117: reads `name`, `pco%nb_sd%d`, `pco%nb_sd%m`, `pco%nb_sd%y`, `pco%nb_sd%a`
- [[basin_print_codes_read.f90]] source line 119: reads `name`, `pco%ls_sd%d`, `pco%ls_sd%m`, `pco%ls_sd%y`, `pco%ls_sd%a`
- [[basin_print_codes_read.f90]] source line 121: reads `name`, `pco%pw_sd%d`, `pco%pw_sd%m`, `pco%pw_sd%y`, `pco%pw_sd%a`
- [[basin_print_codes_read.f90]] source line 124: reads `name`, `pco%chan%d`, `pco%chan%m`, `pco%chan%y`, `pco%chan%a`
- [[basin_print_codes_read.f90]] source line 127: reads `name`, `pco%sd_chan%d`, `pco%sd_chan%m`, `pco%sd_chan%y`, `pco%sd_chan%a`
- [[basin_print_codes_read.f90]] source line 130: reads `name`, `pco%aqu%d`, `pco%aqu%m`, `pco%aqu%y`, `pco%aqu%a`
- [[basin_print_codes_read.f90]] source line 133: reads `name`, `pco%res%d`, `pco%res%m`, `pco%res%y`, `pco%res%a`
- [[basin_print_codes_read.f90]] source line 136: reads `name`, `pco%recall%d`, `pco%recall%m`, `pco%recall%y`, `pco%recall%a`
- [[basin_print_codes_read.f90]] source line 139: reads `name`, `pco%hyd%d`, `pco%hyd%m`, `pco%hyd%y`, `pco%hyd%a`
- [[basin_print_codes_read.f90]] source line 142: reads `name`, `pco%ru%d`, `pco%ru%m`, `pco%ru%y`, `pco%ru%a`
- [[basin_print_codes_read.f90]] source line 145: reads `name`, `pco%pest%d`, `pco%pest%m`, `pco%pest%y`, `pco%pest%a`
- [[basin_print_codes_read.f90]] source line 148: reads `name`, `pco%salt_basin%d`, `pco%salt_basin%m`, `pco%salt_basin%y`, `pco%salt_basin%a`
- [[basin_print_codes_read.f90]] source line 150: reads `name`, `pco%salt_hru%d`, `pco%salt_hru%m`, `pco%salt_hru%y`, `pco%salt_hru%a`
- [[basin_print_codes_read.f90]] source line 152: reads `name`, `pco%salt_ru%d`, `pco%salt_ru%m`, `pco%salt_ru%y`, `pco%salt_ru%a`
- [[basin_print_codes_read.f90]] source line 154: reads `name`, `pco%salt_aqu%d`, `pco%salt_aqu%m`, `pco%salt_aqu%y`, `pco%salt_aqu%a`
- [[basin_print_codes_read.f90]] source line 156: reads `name`, `pco%salt_chn%d`, `pco%salt_chn%m`, `pco%salt_chn%y`, `pco%salt_chn%a`
- [[basin_print_codes_read.f90]] source line 158: reads `name`, `pco%salt_res%d`, `pco%salt_res%m`, `pco%salt_res%y`, `pco%salt_res%a`
- [[basin_print_codes_read.f90]] source line 160: reads `name`, `pco%salt_wet%d`, `pco%salt_wet%m`, `pco%salt_wet%y`, `pco%salt_wet%a`
- [[basin_print_codes_read.f90]] source line 163: reads `name`, `pco%cs_basin%d`, `pco%cs_basin%m`, `pco%cs_basin%y`, `pco%cs_basin%a`
- [[basin_print_codes_read.f90]] source line 165: reads `name`, `pco%cs_hru%d`, `pco%cs_hru%m`, `pco%cs_hru%y`, `pco%cs_hru%a`
- [[basin_print_codes_read.f90]] source line 167: reads `name`, `pco%cs_ru%d`, `pco%cs_ru%m`, `pco%cs_ru%y`, `pco%cs_ru%a`
- [[basin_print_codes_read.f90]] source line 169: reads `name`, `pco%cs_aqu%d`, `pco%cs_aqu%m`, `pco%cs_aqu%y`, `pco%cs_aqu%a`
- [[basin_print_codes_read.f90]] source line 171: reads `name`, `pco%cs_chn%d`, `pco%cs_chn%m`, `pco%cs_chn%y`, `pco%cs_chn%a`
- [[basin_print_codes_read.f90]] source line 173: reads `name`, `pco%cs_res%d`, `pco%cs_res%m`, `pco%cs_res%y`, `pco%cs_res%a`
- [[basin_print_codes_read.f90]] source line 175: reads `name`, `pco%cs_wet%d`, `pco%cs_wet%m`, `pco%cs_wet%y`, `pco%cs_wet%a`
- [[basin_print_codes_read.f90]] source line 179: reads `name`
- [[basin_print_codes_read.f90]] source line 188: reads `name`, `pco%wb_bsn%d`, `pco%wb_bsn%m`, `pco%wb_bsn%y`, `pco%wb_bsn%a`
- [[basin_print_codes_read.f90]] source line 196: reads `name`, `pco%nb_bsn%d`, `pco%nb_bsn%m`, `pco%nb_bsn%y`, `pco%nb_bsn%a`
- [[basin_print_codes_read.f90]] source line 204: reads `name`, `pco%ls_bsn%d`, `pco%ls_bsn%m`, `pco%ls_bsn%y`, `pco%ls_bsn%a`
- [[basin_print_codes_read.f90]] source line 212: reads `name`, `pco%pw_bsn%d`, `pco%pw_bsn%m`, `pco%pw_bsn%y`, `pco%pw_bsn%a`
- [[basin_print_codes_read.f90]] source line 220: reads `name`, `pco%aqu_bsn%d`, `pco%aqu_bsn%m`, `pco%aqu_bsn%y`, `pco%aqu_bsn%a`
- [[basin_print_codes_read.f90]] source line 228: reads `name`, `pco%res_bsn%d`, `pco%res_bsn%m`, `pco%res_bsn%y`, `pco%res_bsn%a`
- [[basin_print_codes_read.f90]] source line 236: reads `name`, `pco%chan_bsn%d`, `pco%chan_bsn%m`, `pco%chan_bsn%y`, `pco%chan_bsn%a`
- [[basin_print_codes_read.f90]] source line 244: reads `name`, `pco%sd_chan_bsn%d`, `pco%sd_chan_bsn%m`, `pco%sd_chan_bsn%y`, `pco%sd_chan_bsn%a`
- [[basin_print_codes_read.f90]] source line 252: reads `name`, `pco%recall_bsn%d`, `pco%recall_bsn%m`, `pco%recall_bsn%y`, `pco%recall_bsn%a`
- [[basin_print_codes_read.f90]] source line 260: reads `name`, `pco%wb_reg%d`, `pco%wb_reg%m`, `pco%wb_reg%y`, `pco%wb_reg%a`
- [[basin_print_codes_read.f90]] source line 268: reads `name`, `pco%nb_reg%d`, `pco%nb_reg%m`, `pco%nb_reg%y`, `pco%nb_reg%a`
- [[basin_print_codes_read.f90]] source line 276: reads `name`, `pco%ls_reg%d`, `pco%ls_reg%m`, `pco%ls_reg%y`, `pco%ls_reg%a`
- [[basin_print_codes_read.f90]] source line 284: reads `name`, `pco%pw_reg%d`, `pco%pw_reg%m`, `pco%pw_reg%y`, `pco%pw_reg%a`
- [[basin_print_codes_read.f90]] source line 292: reads `name`, `pco%aqu_reg%d`, `pco%aqu_reg%m`, `pco%aqu_reg%y`, `pco%aqu_reg%a`
- [[basin_print_codes_read.f90]] source line 300: reads `name`, `pco%res_reg%d`, `pco%res_reg%m`, `pco%res_reg%y`, `pco%res_reg%a`
- [[basin_print_codes_read.f90]] source line 308: reads `name`, `pco%sd_chan_reg%d`, `pco%sd_chan_reg%m`, `pco%sd_chan_reg%y`, `pco%sd_chan_reg%a`
- ... 57 additional read statements omitted from this generated summary.

## Parameters
| Parameter | Type | Units | Meaning | Source | Reader line |
|---|---|---|---|---|---:|
| `pco%nyskip` | `integer` |  | number of years to skip output summarization | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:28 |
| `pco%day_start` | `integer` |  | julian day to start printing output | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:28 |
| `pco%yrc_start` | `integer` |  | calendar year to start printing output | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:28 |
| `pco%day_end` | `integer` |  | julian day to end printing output | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:28 |
| `pco%yrc_end` | `integer` |  | calendar year to end printing output | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:28 |
| `pco%int_day` | `integer` |  | interval between daily printing | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:28 |
| `pco%aa_numint` | `integer` |  | number of print intervals for ave annual output | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:32 |
| `pco%aa_yrs%aa_numint` | `integer, dimension(:), allocatable` |  | end years for ave annual output SPECIAL OUTPUTS | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:36 |
| `pco%csvout` | `character(len=1)` |  | code to print .csv files n=no print; y=print; code to print carbon output; d = end of day; m = end of month; y = end of year; a = end of simulation; | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:44 |
| `pco%use_obj_labels` | `character(len=1)` |  | code to read in the print.prt print objects respecting the label of in the row (1st column) to identify name of the print object | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:44 |
| `pco%cdfout` | `character(len=1)` |  | code to print netcdf (cdf) files n=no print; y=print; OTHER OUTPUTS | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:44 |
| `pco%crop_yld` | `character(len=1)` |  | crop yields - a=average annual; y=yearly; b=both annual and yearly; n=no print | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:50 |
| `pco%mgtout` | `character(len=1)` |  | management output file (mgt.out) (default ave annual-d,m,y,a input) | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:50 |
| `pco%hydcon` | `character(len=1)` |  | hydrograph connect output file (hydcon.out) | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:50 |
| `pco%fdcout` | `character(len=1)` |  | flow duration curve output n=no print; avann=print; NOT ACTIVE BASIN | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:50 |
| `name` | `character (len=16)` |  | name | `basin_print_codes_read.f90:11` | [[basin_print_codes_read.f90]]:58 |
| `pco%wb_bsn%d` | `character(len=1)` |  | water balance BASIN output | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:58 |
| `pco%wb_bsn%m` | `character(len=1)` |  | water balance BASIN output | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:58 |
| `pco%wb_bsn%y` | `character(len=1)` |  | water balance BASIN output | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:58 |
| `pco%wb_bsn%a` | `character(len=1)` |  | water balance BASIN output | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:58 |
| `pco%nb_bsn%d` | `character(len=1)` |  | nutrient balance BASIN output | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:60 |
| `pco%nb_bsn%m` | `character(len=1)` |  | nutrient balance BASIN output | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:60 |
| `pco%nb_bsn%y` | `character(len=1)` |  | nutrient balance BASIN output | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:60 |
| `pco%nb_bsn%a` | `character(len=1)` |  | nutrient balance BASIN output | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:60 |
| `pco%ls_bsn%d` | `character(len=1)` |  | losses BASIN output | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:62 |
| `pco%ls_bsn%m` | `character(len=1)` |  | losses BASIN output | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:62 |
| `pco%ls_bsn%y` | `character(len=1)` |  | losses BASIN output | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:62 |
| `pco%ls_bsn%a` | `character(len=1)` |  | losses BASIN output | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:62 |
| `pco%pw_bsn%d` | `character(len=1)` |  | plant weather BASIN output | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:64 |
| `pco%pw_bsn%m` | `character(len=1)` |  | plant weather BASIN output | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:64 |
| `pco%pw_bsn%y` | `character(len=1)` |  | plant weather BASIN output | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:64 |
| `pco%pw_bsn%a` | `character(len=1)` |  | plant weather BASIN output | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:64 |
| `pco%aqu_bsn%d` | `character(len=1)` |  |  | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:66 |
| `pco%aqu_bsn%m` | `character(len=1)` |  |  | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:66 |
| `pco%aqu_bsn%y` | `character(len=1)` |  |  | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:66 |
| `pco%aqu_bsn%a` | `character(len=1)` |  |  | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:66 |
| `pco%res_bsn%d` | `character(len=1)` |  |  | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:68 |
| `pco%res_bsn%m` | `character(len=1)` |  |  | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:68 |
| `pco%res_bsn%y` | `character(len=1)` |  |  | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:68 |
| `pco%res_bsn%a` | `character(len=1)` |  |  | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:68 |
| `pco%chan_bsn%d` | `character(len=1)` |  |  | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:70 |
| `pco%chan_bsn%m` | `character(len=1)` |  |  | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:70 |
| `pco%chan_bsn%y` | `character(len=1)` |  |  | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:70 |
| `pco%chan_bsn%a` | `character(len=1)` |  |  | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:70 |
| `pco%sd_chan_bsn%d` | `character(len=1)` |  |  | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:72 |
| `pco%sd_chan_bsn%m` | `character(len=1)` |  |  | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:72 |
| `pco%sd_chan_bsn%y` | `character(len=1)` |  |  | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:72 |
| `pco%sd_chan_bsn%a` | `character(len=1)` |  |  | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:72 |
| `pco%recall_bsn%d` | `character(len=1)` |  | REGION | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:74 |
| `pco%recall_bsn%m` | `character(len=1)` |  | REGION | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:74 |
| `pco%recall_bsn%y` | `character(len=1)` |  | REGION | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:74 |
| `pco%recall_bsn%a` | `character(len=1)` |  | REGION | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:74 |
| `pco%wb_reg%d` | `character(len=1)` |  | water balance REGION output | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:77 |
| `pco%wb_reg%m` | `character(len=1)` |  | water balance REGION output | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:77 |
| `pco%wb_reg%y` | `character(len=1)` |  | water balance REGION output | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:77 |
| `pco%wb_reg%a` | `character(len=1)` |  | water balance REGION output | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:77 |
| `pco%nb_reg%d` | `character(len=1)` |  | nutrient balance REGION output | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:79 |
| `pco%nb_reg%m` | `character(len=1)` |  | nutrient balance REGION output | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:79 |
| `pco%nb_reg%y` | `character(len=1)` |  | nutrient balance REGION output | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:79 |
| `pco%nb_reg%a` | `character(len=1)` |  | nutrient balance REGION output | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:79 |
| `pco%ls_reg%d` | `character(len=1)` |  | losses REGION output | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:81 |
| `pco%ls_reg%m` | `character(len=1)` |  | losses REGION output | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:81 |
| `pco%ls_reg%y` | `character(len=1)` |  | losses REGION output | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:81 |
| `pco%ls_reg%a` | `character(len=1)` |  | losses REGION output | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:81 |
| `pco%pw_reg%d` | `character(len=1)` |  | plant weather REGION output | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:83 |
| `pco%pw_reg%m` | `character(len=1)` |  | plant weather REGION output | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:83 |
| `pco%pw_reg%y` | `character(len=1)` |  | plant weather REGION output | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:83 |
| `pco%pw_reg%a` | `character(len=1)` |  | plant weather REGION output | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:83 |
| `pco%aqu_reg%d` | `character(len=1)` |  |  | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:85 |
| `pco%aqu_reg%m` | `character(len=1)` |  |  | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:85 |
| `pco%aqu_reg%y` | `character(len=1)` |  |  | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:85 |
| `pco%aqu_reg%a` | `character(len=1)` |  |  | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:85 |
| `pco%res_reg%d` | `character(len=1)` |  |  | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:87 |
| `pco%res_reg%m` | `character(len=1)` |  |  | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:87 |
| `pco%res_reg%y` | `character(len=1)` |  |  | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:87 |
| `pco%res_reg%a` | `character(len=1)` |  |  | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:87 |
| `pco%sd_chan_reg%d` | `character(len=1)` |  |  | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:89 |
| `pco%sd_chan_reg%m` | `character(len=1)` |  |  | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:89 |
| `pco%sd_chan_reg%y` | `character(len=1)` |  |  | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:89 |
| `pco%sd_chan_reg%a` | `character(len=1)` |  |  | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:89 |
| `pco%recall_reg%d` | `character(len=1)` |  |  | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:91 |
| `pco%recall_reg%m` | `character(len=1)` |  |  | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:91 |
| `pco%recall_reg%y` | `character(len=1)` |  |  | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:91 |
| `pco%recall_reg%a` | `character(len=1)` |  |  | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:91 |
| `pco%water_allo%d` | `character(len=1)` |  | LSU | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:93 |
| `pco%water_allo%m` | `character(len=1)` |  | LSU | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:93 |
| `pco%water_allo%y` | `character(len=1)` |  | LSU | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:93 |
| `pco%water_allo%a` | `character(len=1)` |  | LSU | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:93 |
| `pco%wb_lsu%d` | `character(len=1)` |  | water balance LSU output | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:96 |
| `pco%wb_lsu%m` | `character(len=1)` |  | water balance LSU output | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:96 |
| `pco%wb_lsu%y` | `character(len=1)` |  | water balance LSU output | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:96 |
| `pco%wb_lsu%a` | `character(len=1)` |  | water balance LSU output | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:96 |
| `pco%nb_lsu%d` | `character(len=1)` |  | nutrient balance LSU output | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:98 |
| `pco%nb_lsu%m` | `character(len=1)` |  | nutrient balance LSU output | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:98 |
| `pco%nb_lsu%y` | `character(len=1)` |  | nutrient balance LSU output | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:98 |
| `pco%nb_lsu%a` | `character(len=1)` |  | nutrient balance LSU output | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:98 |
| `pco%ls_lsu%d` | `character(len=1)` |  | losses LSU output | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:100 |
| `pco%ls_lsu%m` | `character(len=1)` |  | losses LSU output | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:100 |
| `pco%ls_lsu%y` | `character(len=1)` |  | losses LSU output | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:100 |
| `pco%ls_lsu%a` | `character(len=1)` |  | losses LSU output | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:100 |
| `pco%pw_lsu%d` | `character(len=1)` |  | plant weather LSU output HRU | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:102 |
| `pco%pw_lsu%m` | `character(len=1)` |  | plant weather LSU output HRU | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:102 |
| `pco%pw_lsu%y` | `character(len=1)` |  | plant weather LSU output HRU | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:102 |
| `pco%pw_lsu%a` | `character(len=1)` |  | plant weather LSU output HRU | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:102 |
| `pco%wb_hru%d` | `character(len=1)` |  | water balance HRU output | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:105 |
| `pco%wb_hru%m` | `character(len=1)` |  | water balance HRU output | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:105 |
| `pco%wb_hru%y` | `character(len=1)` |  | water balance HRU output | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:105 |
| `pco%wb_hru%a` | `character(len=1)` |  | water balance HRU output | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:105 |
| `pco%nb_hru%d` | `character(len=1)` |  | nutrient balance HRU output | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:107 |
| `pco%nb_hru%m` | `character(len=1)` |  | nutrient balance HRU output | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:107 |
| `pco%nb_hru%y` | `character(len=1)` |  | nutrient balance HRU output | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:107 |
| `pco%nb_hru%a` | `character(len=1)` |  | nutrient balance HRU output | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:107 |
| `pco%ls_hru%d` | `character(len=1)` |  | losses HRU output | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:109 |
| `pco%ls_hru%m` | `character(len=1)` |  | losses HRU output | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:109 |
| `pco%ls_hru%y` | `character(len=1)` |  | losses HRU output | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:109 |
| `pco%ls_hru%a` | `character(len=1)` |  | losses HRU output | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:109 |
| `pco%pw_hru%d` | `character(len=1)` |  | plant weather HRU output | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:111 |
| `pco%pw_hru%m` | `character(len=1)` |  | plant weather HRU output | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:111 |
| `pco%pw_hru%y` | `character(len=1)` |  | plant weather HRU output | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:111 |
| `pco%pw_hru%a` | `character(len=1)` |  | plant weather HRU output | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:111 |
| `pco%wb_sd%d` | `character(len=1)` |  | water balance SWAT-DEG output | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:115 |
| `pco%wb_sd%m` | `character(len=1)` |  | water balance SWAT-DEG output | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:115 |
| `pco%wb_sd%y` | `character(len=1)` |  | water balance SWAT-DEG output | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:115 |
| `pco%wb_sd%a` | `character(len=1)` |  | water balance SWAT-DEG output | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:115 |
| `pco%nb_sd%d` | `character(len=1)` |  | nutrient balance SWAT-DEG output | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:117 |
| `pco%nb_sd%m` | `character(len=1)` |  | nutrient balance SWAT-DEG output | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:117 |
| `pco%nb_sd%y` | `character(len=1)` |  | nutrient balance SWAT-DEG output | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:117 |
| `pco%nb_sd%a` | `character(len=1)` |  | nutrient balance SWAT-DEG output | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:117 |
| `pco%ls_sd%d` | `character(len=1)` |  | losses SWAT-DEG output | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:119 |
| `pco%ls_sd%m` | `character(len=1)` |  | losses SWAT-DEG output | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:119 |
| `pco%ls_sd%y` | `character(len=1)` |  | losses SWAT-DEG output | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:119 |
| `pco%ls_sd%a` | `character(len=1)` |  | losses SWAT-DEG output | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:119 |
| `pco%pw_sd%d` | `character(len=1)` |  | plant weather SWAT-DEG output CHANNEL | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:121 |
| `pco%pw_sd%m` | `character(len=1)` |  | plant weather SWAT-DEG output CHANNEL | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:121 |
| `pco%pw_sd%y` | `character(len=1)` |  | plant weather SWAT-DEG output CHANNEL | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:121 |
| `pco%pw_sd%a` | `character(len=1)` |  | plant weather SWAT-DEG output CHANNEL | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:121 |
| `pco%chan%d` | `character(len=1)` |  | channel output CHANNEL_LTE | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:124 |
| `pco%chan%m` | `character(len=1)` |  | channel output CHANNEL_LTE | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:124 |
| `pco%chan%y` | `character(len=1)` |  | channel output CHANNEL_LTE | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:124 |
| `pco%chan%a` | `character(len=1)` |  | channel output CHANNEL_LTE | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:124 |
| `pco%sd_chan%d` | `character(len=1)` |  | swat deg (lte) channel output AQUIFER | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:127 |
| `pco%sd_chan%m` | `character(len=1)` |  | swat deg (lte) channel output AQUIFER | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:127 |
| `pco%sd_chan%y` | `character(len=1)` |  | swat deg (lte) channel output AQUIFER | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:127 |
| `pco%sd_chan%a` | `character(len=1)` |  | swat deg (lte) channel output AQUIFER | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:127 |
| `pco%aqu%d` | `character(len=1)` |  | aqufier output RESERVOIR | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:130 |
| `pco%aqu%m` | `character(len=1)` |  | aqufier output RESERVOIR | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:130 |
| `pco%aqu%y` | `character(len=1)` |  | aqufier output RESERVOIR | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:130 |
| `pco%aqu%a` | `character(len=1)` |  | aqufier output RESERVOIR | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:130 |
| `pco%res%d` | `character(len=1)` |  | reservoir output RECALL | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:133 |
| `pco%res%m` | `character(len=1)` |  | reservoir output RECALL | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:133 |
| `pco%res%y` | `character(len=1)` |  | reservoir output RECALL | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:133 |
| `pco%res%a` | `character(len=1)` |  | reservoir output RECALL | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:133 |
| `pco%recall%d` | `character(len=1)` |  | recall output HYDIN AND HYDOUT | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:136 |
| `pco%recall%m` | `character(len=1)` |  | recall output HYDIN AND HYDOUT | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:136 |
| `pco%recall%y` | `character(len=1)` |  | recall output HYDIN AND HYDOUT | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:136 |
| `pco%recall%a` | `character(len=1)` |  | recall output HYDIN AND HYDOUT | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:136 |
| `pco%hyd%d` | `character(len=1)` |  | hydin_output and hydout_output | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:139 |
| `pco%hyd%m` | `character(len=1)` |  | hydin_output and hydout_output | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:139 |
| `pco%hyd%y` | `character(len=1)` |  | hydin_output and hydout_output | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:139 |
| `pco%hyd%a` | `character(len=1)` |  | hydin_output and hydout_output | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:139 |
| `pco%ru%d` | `character(len=1)` |  |  | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:142 |
| `pco%ru%m` | `character(len=1)` |  |  | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:142 |
| `pco%ru%y` | `character(len=1)` |  |  | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:142 |
| `pco%ru%a` | `character(len=1)` |  |  | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:142 |
| `pco%pest%d` | `character(len=1)` |  | all constituents pesticide output files (hru, chan, res, basin_chan, basin_res, basin_ls SALT (rtb salt) | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:145 |
| `pco%pest%m` | `character(len=1)` |  | all constituents pesticide output files (hru, chan, res, basin_chan, basin_res, basin_ls SALT (rtb salt) | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:145 |
| `pco%pest%y` | `character(len=1)` |  | all constituents pesticide output files (hru, chan, res, basin_chan, basin_res, basin_ls SALT (rtb salt) | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:145 |
| `pco%pest%a` | `character(len=1)` |  | all constituents pesticide output files (hru, chan, res, basin_chan, basin_res, basin_ls SALT (rtb salt) | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:145 |
| `pco%salt_basin%d` | `character(len=1)` |  | salt output for the basin | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:148 |
| `pco%salt_basin%m` | `character(len=1)` |  | salt output for the basin | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:148 |
| `pco%salt_basin%y` | `character(len=1)` |  | salt output for the basin | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:148 |
| `pco%salt_basin%a` | `character(len=1)` |  | salt output for the basin | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:148 |
| `pco%salt_hru%d` | `character(len=1)` |  | salt output for HRUs | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:150 |
| `pco%salt_hru%m` | `character(len=1)` |  | salt output for HRUs | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:150 |
| `pco%salt_hru%y` | `character(len=1)` |  | salt output for HRUs | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:150 |
| `pco%salt_hru%a` | `character(len=1)` |  | salt output for HRUs | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:150 |
| `pco%salt_ru%d` | `character(len=1)` |  | salt output for routing units | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:152 |
| `pco%salt_ru%m` | `character(len=1)` |  | salt output for routing units | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:152 |
| `pco%salt_ru%y` | `character(len=1)` |  | salt output for routing units | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:152 |
| `pco%salt_ru%a` | `character(len=1)` |  | salt output for routing units | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:152 |
| `pco%salt_aqu%d` | `character(len=1)` |  | salt output for aquifers | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:154 |
| `pco%salt_aqu%m` | `character(len=1)` |  | salt output for aquifers | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:154 |
| `pco%salt_aqu%y` | `character(len=1)` |  | salt output for aquifers | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:154 |
| `pco%salt_aqu%a` | `character(len=1)` |  | salt output for aquifers | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:154 |
| `pco%salt_chn%d` | `character(len=1)` |  | salt output for channels | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:156 |
| `pco%salt_chn%m` | `character(len=1)` |  | salt output for channels | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:156 |
| `pco%salt_chn%y` | `character(len=1)` |  | salt output for channels | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:156 |
| `pco%salt_chn%a` | `character(len=1)` |  | salt output for channels | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:156 |
| `pco%salt_res%d` | `character(len=1)` |  | salt output for reservoirs | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:158 |
| `pco%salt_res%m` | `character(len=1)` |  | salt output for reservoirs | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:158 |
| `pco%salt_res%y` | `character(len=1)` |  | salt output for reservoirs | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:158 |
| `pco%salt_res%a` | `character(len=1)` |  | salt output for reservoirs | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:158 |
| `pco%salt_wet%d` | `character(len=1)` |  | salt output for reservoirs CONSTITUENTS (rtb cs) | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:160 |
| `pco%salt_wet%m` | `character(len=1)` |  | salt output for reservoirs CONSTITUENTS (rtb cs) | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:160 |
| `pco%salt_wet%y` | `character(len=1)` |  | salt output for reservoirs CONSTITUENTS (rtb cs) | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:160 |
| `pco%salt_wet%a` | `character(len=1)` |  | salt output for reservoirs CONSTITUENTS (rtb cs) | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:160 |
| `pco%cs_basin%d` | `character(len=1)` |  | constituent output for the basin | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:163 |
| `pco%cs_basin%m` | `character(len=1)` |  | constituent output for the basin | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:163 |
| `pco%cs_basin%y` | `character(len=1)` |  | constituent output for the basin | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:163 |
| `pco%cs_basin%a` | `character(len=1)` |  | constituent output for the basin | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:163 |
| `pco%cs_hru%d` | `character(len=1)` |  | constituent output for HRUs | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:165 |
| `pco%cs_hru%m` | `character(len=1)` |  | constituent output for HRUs | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:165 |
| `pco%cs_hru%y` | `character(len=1)` |  | constituent output for HRUs | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:165 |
| `pco%cs_hru%a` | `character(len=1)` |  | constituent output for HRUs | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:165 |
| `pco%cs_ru%d` | `character(len=1)` |  | constituent output for routing units | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:167 |
| `pco%cs_ru%m` | `character(len=1)` |  | constituent output for routing units | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:167 |
| `pco%cs_ru%y` | `character(len=1)` |  | constituent output for routing units | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:167 |
| `pco%cs_ru%a` | `character(len=1)` |  | constituent output for routing units | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:167 |
| `pco%cs_aqu%d` | `character(len=1)` |  | constituent output for aquifers | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:169 |
| `pco%cs_aqu%m` | `character(len=1)` |  | constituent output for aquifers | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:169 |
| `pco%cs_aqu%y` | `character(len=1)` |  | constituent output for aquifers | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:169 |
| `pco%cs_aqu%a` | `character(len=1)` |  | constituent output for aquifers | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:169 |
| `pco%cs_chn%d` | `character(len=1)` |  | constituent output for channels | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:171 |
| `pco%cs_chn%m` | `character(len=1)` |  | constituent output for channels | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:171 |
| `pco%cs_chn%y` | `character(len=1)` |  | constituent output for channels | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:171 |
| `pco%cs_chn%a` | `character(len=1)` |  | constituent output for channels | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:171 |
| `pco%cs_res%d` | `character(len=1)` |  | constituent output for reservoirs | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:173 |
| `pco%cs_res%m` | `character(len=1)` |  | constituent output for reservoirs | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:173 |
| `pco%cs_res%y` | `character(len=1)` |  | constituent output for reservoirs | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:173 |
| `pco%cs_res%a` | `character(len=1)` |  | constituent output for reservoirs | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:173 |
| `pco%cs_wet%d` | `character(len=1)` |  | constituent output for reservoirs | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:175 |
| `pco%cs_wet%m` | `character(len=1)` |  | constituent output for reservoirs | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:175 |
| `pco%cs_wet%y` | `character(len=1)` |  | constituent output for reservoirs | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:175 |
| `pco%cs_wet%a` | `character(len=1)` |  | constituent output for reservoirs | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:175 |
| `pco%cb_gl_lsu%d` | `character(len=1)` |  | lsu_carb_gl_* LSU-area-weighted C gain/loss | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:365 |
| `pco%cb_gl_lsu%m` | `character(len=1)` |  | lsu_carb_gl_* LSU-area-weighted C gain/loss | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:365 |
| `pco%cb_gl_lsu%y` | `character(len=1)` |  | lsu_carb_gl_* LSU-area-weighted C gain/loss | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:365 |
| `pco%cb_gl_lsu%a` | `character(len=1)` |  | lsu_carb_gl_* LSU-area-weighted C gain/loss | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:365 |
| `pco%cb_trf_lsu%d` | `character(len=1)` |  | lsu_scf_* LSU-area-weighted C transformations | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:373 |
| `pco%cb_trf_lsu%m` | `character(len=1)` |  | lsu_scf_* LSU-area-weighted C transformations | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:373 |
| `pco%cb_trf_lsu%y` | `character(len=1)` |  | lsu_scf_* LSU-area-weighted C transformations | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:373 |
| `pco%cb_trf_lsu%a` | `character(len=1)` |  | lsu_scf_* LSU-area-weighted C transformations | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:373 |
| `pco%cb_plt_lsu%d` | `character(len=1)` |  | lsu_plc_stat_* LSU-area-weighted plant C state HRU-LTE | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:381 |
| `pco%cb_plt_lsu%m` | `character(len=1)` |  | lsu_plc_stat_* LSU-area-weighted plant C state HRU-LTE | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:381 |
| `pco%cb_plt_lsu%y` | `character(len=1)` |  | lsu_plc_stat_* LSU-area-weighted plant C state HRU-LTE | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:381 |
| `pco%cb_plt_lsu%a` | `character(len=1)` |  | lsu_plc_stat_* LSU-area-weighted plant C state HRU-LTE | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:381 |
| `pco%cb_hru%d` | `character(len=1)` |  | legacy carbon flag (kept for backward compat with print.prt readers; no longer referenced by writers) | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:421 |
| `pco%cb_hru%m` | `character(len=1)` |  | legacy carbon flag (kept for backward compat with print.prt readers; no longer referenced by writers) | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:421 |
| `pco%cb_hru%y` | `character(len=1)` |  | legacy carbon flag (kept for backward compat with print.prt readers; no longer referenced by writers) | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:421 |
| `pco%cb_hru%a` | `character(len=1)` |  | legacy carbon flag (kept for backward compat with print.prt readers; no longer referenced by writers) | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:421 |
| `pco%cb_vars_hru%d` | `character(len=1)` |  | legacy carbon variable flag (same) per-family carbon output flags (10 rows) | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:429 |
| `pco%cb_vars_hru%m` | `character(len=1)` |  | legacy carbon variable flag (same) per-family carbon output flags (10 rows) | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:429 |
| `pco%cb_vars_hru%y` | `character(len=1)` |  | legacy carbon variable flag (same) per-family carbon output flags (10 rows) | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:429 |
| `pco%cb_vars_hru%a` | `character(len=1)` |  | legacy carbon variable flag (same) per-family carbon output flags (10 rows) | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:429 |
| `pco%cb_gl_hru%d` | `character(len=1)` |  | hru_carb_gl_* HRU C gain/loss | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:438 |
| `pco%cb_gl_hru%m` | `character(len=1)` |  | hru_carb_gl_* HRU C gain/loss | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:438 |
| `pco%cb_gl_hru%y` | `character(len=1)` |  | hru_carb_gl_* HRU C gain/loss | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:438 |
| `pco%cb_gl_hru%a` | `character(len=1)` |  | hru_carb_gl_* HRU C gain/loss | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:438 |
| `pco%cb_trf_hru%d` | `character(len=1)` |  | hru_scf_* HRU C transformations | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:446 |
| `pco%cb_trf_hru%m` | `character(len=1)` |  | hru_scf_* HRU C transformations | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:446 |
| `pco%cb_trf_hru%y` | `character(len=1)` |  | hru_scf_* HRU C transformations | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:446 |
| `pco%cb_trf_hru%a` | `character(len=1)` |  | hru_scf_* HRU C transformations | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:446 |
| `pco%cb_lyr_hru%d` | `character(len=1)` |  | hru_cbn_lyr_* per-layer SOC totals + sequestered | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:454 |
| `pco%cb_lyr_hru%m` | `character(len=1)` |  | hru_cbn_lyr_* per-layer SOC totals + sequestered | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:454 |
| `pco%cb_lyr_hru%y` | `character(len=1)` |  | hru_cbn_lyr_* per-layer SOC totals + sequestered | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:454 |
| `pco%cb_lyr_hru%a` | `character(len=1)` |  | hru_cbn_lyr_* per-layer SOC totals + sequestered | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:454 |
| `pco%cb_cpool_hru%d` | `character(len=1)` |  | hru_cpool_stat_* per-layer C pools | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:462 |
| `pco%cb_cpool_hru%m` | `character(len=1)` |  | hru_cpool_stat_* per-layer C pools | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:462 |
| `pco%cb_cpool_hru%y` | `character(len=1)` |  | hru_cpool_stat_* per-layer C pools | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:462 |
| `pco%cb_cpool_hru%a` | `character(len=1)` |  | hru_cpool_stat_* per-layer C pools | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:462 |
| `pco%cb_npool_hru%d` | `character(len=1)` |  | hru_n_p_pool_stat_* per-layer N+P pools | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:470 |
| `pco%cb_npool_hru%m` | `character(len=1)` |  | hru_n_p_pool_stat_* per-layer N+P pools | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:470 |
| `pco%cb_npool_hru%y` | `character(len=1)` |  | hru_n_p_pool_stat_* per-layer N+P pools | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:470 |
| `pco%cb_npool_hru%a` | `character(len=1)` |  | hru_n_p_pool_stat_* per-layer N+P pools | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:470 |
| `pco%cb_plt_hru%d` | `character(len=1)` |  | hru_plc_stat_* plant C state | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:478 |
| `pco%cb_plt_hru%m` | `character(len=1)` |  | hru_plc_stat_* plant C state | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:478 |
| `pco%cb_plt_hru%y` | `character(len=1)` |  | hru_plc_stat_* plant C state | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:478 |
| `pco%cb_plt_hru%a` | `character(len=1)` |  | hru_plc_stat_* plant C state | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:478 |
| `pco%cb_flux_hru%d` | `character(len=1)` |  | hru_cflux_stat_* per-layer flux diagnostic | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:486 |
| `pco%cb_flux_hru%m` | `character(len=1)` |  | hru_cflux_stat_* per-layer flux diagnostic | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:486 |
| `pco%cb_flux_hru%y` | `character(len=1)` |  | hru_cflux_stat_* per-layer flux diagnostic | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:486 |
| `pco%cb_flux_hru%a` | `character(len=1)` |  | hru_cflux_stat_* per-layer flux diagnostic | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:486 |
| `pco%cb_drv_hru%d` | `character(len=1)` |  | hru_carb_drv_* per-layer drivers diagnostic | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:494 |
| `pco%cb_drv_hru%m` | `character(len=1)` |  | hru_carb_drv_* per-layer drivers diagnostic | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:494 |
| `pco%cb_drv_hru%y` | `character(len=1)` |  | hru_carb_drv_* per-layer drivers diagnostic | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:494 |
| `pco%cb_drv_hru%a` | `character(len=1)` |  | hru_carb_drv_* per-layer drivers diagnostic | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:494 |
| `pco%cb_dyn_hru%d` | `character(len=1)` |  | hru_carb_dyn_* per-layer dynamics diagnostic | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:502 |
| `pco%cb_dyn_hru%m` | `character(len=1)` |  | hru_carb_dyn_* per-layer dynamics diagnostic | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:502 |
| `pco%cb_dyn_hru%y` | `character(len=1)` |  | hru_carb_dyn_* per-layer dynamics diagnostic | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:502 |
| `pco%cb_dyn_hru%a` | `character(len=1)` |  | hru_carb_dyn_* per-layer dynamics diagnostic | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:502 |
| `pco%cb_snap_hru%d` | `character(len=1)` |  | hru_soil_snap_* soil property snapshot LSU-level area-weighted aggregations (Option 1: HRU-aggregated families only) | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:510 |
| `pco%cb_snap_hru%m` | `character(len=1)` |  | hru_soil_snap_* soil property snapshot LSU-level area-weighted aggregations (Option 1: HRU-aggregated families only) | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:510 |
| `pco%cb_snap_hru%y` | `character(len=1)` |  | hru_soil_snap_* soil property snapshot LSU-level area-weighted aggregations (Option 1: HRU-aggregated families only) | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:510 |
| `pco%cb_snap_hru%a` | `character(len=1)` |  | hru_soil_snap_* soil property snapshot LSU-level area-weighted aggregations (Option 1: HRU-aggregated families only) | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:510 |
| `pco%gwflow_wb%d` | `character(len=1)` |  | gwflow cell + basin water balance (day/mon/yr/aa) | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:727 |
| `pco%gwflow_wb%m` | `character(len=1)` |  | gwflow cell + basin water balance (day/mon/yr/aa) | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:727 |
| `pco%gwflow_wb%y` | `character(len=1)` |  | gwflow cell + basin water balance (day/mon/yr/aa) | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:727 |
| `pco%gwflow_wb%a` | `character(len=1)` |  | gwflow cell + basin water balance (day/mon/yr/aa) | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:727 |
| `pco%gwflow_flux%d` | `character(len=1)` |  | gwflow canal, pond, tile, gwsw, chan obs diagnostic output | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:735 |
| `pco%gwflow_flux%m` | `character(len=1)` |  | gwflow canal, pond, tile, gwsw, chan obs diagnostic output | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:735 |
| `pco%gwflow_flux%y` | `character(len=1)` |  | gwflow canal, pond, tile, gwsw, chan obs diagnostic output | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:735 |
| `pco%gwflow_flux%a` | `character(len=1)` |  | gwflow canal, pond, tile, gwsw, chan obs diagnostic output | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:735 |
| `pco%gwflow_heat%d` | `character(len=1)` |  | gwflow basin heat balance output | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:743 |
| `pco%gwflow_heat%m` | `character(len=1)` |  | gwflow basin heat balance output | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:743 |
| `pco%gwflow_heat%y` | `character(len=1)` |  | gwflow basin heat balance output | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:743 |
| `pco%gwflow_heat%a` | `character(len=1)` |  | gwflow basin heat balance output | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:743 |
| `pco%gwflow_solute%d` | `character(len=1)` |  | gwflow basin solute balance output | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:751 |
| `pco%gwflow_solute%m` | `character(len=1)` |  | gwflow basin solute balance output | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:751 |
| `pco%gwflow_solute%y` | `character(len=1)` |  | gwflow basin solute balance output | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:751 |
| `pco%gwflow_solute%a` | `character(len=1)` |  | gwflow basin solute balance output | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:751 |
| `pco%gwflow_obs%d` | `character(len=1)` |  | gwflow observation well output | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:759 |
| `pco%gwflow_obs%m` | `character(len=1)` |  | gwflow observation well output | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:759 |
| `pco%gwflow_obs%y` | `character(len=1)` |  | gwflow observation well output | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:759 |
| `pco%gwflow_obs%a` | `character(len=1)` |  | gwflow observation well output | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:759 |
| `pco%gwflow_pump%d` | `character(len=1)` |  | gwflow HRU pumping output | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:767 |
| `pco%gwflow_pump%m` | `character(len=1)` |  | gwflow HRU pumping output | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:767 |
| `pco%gwflow_pump%y` | `character(len=1)` |  | gwflow HRU pumping output | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:767 |
| `pco%gwflow_pump%a` | `character(len=1)` |  | gwflow HRU pumping output | [[basin_module.f90#pco]] | [[basin_print_codes_read.f90]]:767 |
