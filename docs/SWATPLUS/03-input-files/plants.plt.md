---
type: input
tags:
  - swat/input
file: plants.plt
ext: plt
cio_field: plants_plt
read_by:
  - plant_parm_read.f90
purpose: ""
---

# plants.plt

> [!info] Input File
> Declared in `file.cio` field `plants_plt`. See [[file.cio]] for the controlling file map.

## Overview
- **Declared in `file.cio` field**: `plants_plt`
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[plant_parm_read.f90]]

## File Structure
- [[plant_parm_read.f90]] source line 33: reads `titldum`
- [[plant_parm_read.f90]] source line 35: reads `header`
- [[plant_parm_read.f90]] source line 38: reads `titldum`
- [[plant_parm_read.f90]] source line 48: reads `titldum`
- [[plant_parm_read.f90]] source line 50: reads `header`
- [[plant_parm_read.f90]] source line 55: reads `pldb(ic)`
- [[plant_parm_read.f90]] source line 57: reads `pldb(ic)`, `pl_class(ic)`

## Parameters
| Parameter | Type | Units | Meaning | Source | Reader line |
|---|---|---|---|---|---:|
| `pldb%plantnm` | `character(len=40)` | none | crop name | [[plant_data_module.f90#pldb]] | [[plant_parm_read.f90]]:55 |
| `pldb%typ` | `character(len=18)` | none | plant category warm_annual cold_annual warm_annual_tuber cold_annual_tuber perennial | [[plant_data_module.f90#pldb]] | [[plant_parm_read.f90]]:55 |
| `pldb%trig` | `character(len=18)` | none | phenology trigger moisture_gro temp_gro | [[plant_data_module.f90#pldb]] | [[plant_parm_read.f90]]:55 |
| `pldb%nfix_co` | `real` | none | n fixation coefficient (0.5 legume; 0 non-legume) | [[plant_data_module.f90#pldb]] | [[plant_parm_read.f90]]:55 |
| `pldb%days_mat` | `integer` | days | days to maturity - if zero use hu for entire growing season | [[plant_data_module.f90#pldb]] | [[plant_parm_read.f90]]:55 |
| `pldb%bio_e` | `real` | (kg/ha/(MJ/m**2) | biomass-energy ratio | [[plant_data_module.f90#pldb]] | [[plant_parm_read.f90]]:55 |
| `pldb%hvsti` | `real` | (kg/ha)/(kg/ha) | harvest index: crop yield/aboveground biomass | [[plant_data_module.f90#pldb]] | [[plant_parm_read.f90]]:55 |
| `pldb%blai` | `real` | none | max (potential) leaf area index | [[plant_data_module.f90#pldb]] | [[plant_parm_read.f90]]:55 |
| `pldb%frgrw1` | `real` | none | fraction of the growing season corresponding to the 1st point on optimal leaf area development curve | [[plant_data_module.f90#pldb]] | [[plant_parm_read.f90]]:55 |
| `pldb%laimx1` | `real` | none | frac of max leaf area index corresponding to the 1st point on optimal leaf area development curve | [[plant_data_module.f90#pldb]] | [[plant_parm_read.f90]]:55 |
| `pldb%frgrw2` | `real` | none | fraction of the growing season corresponding to the 2nd point on optimal leaf area development curve | [[plant_data_module.f90#pldb]] | [[plant_parm_read.f90]]:55 |
| `pldb%laimx2` | `real` | none | fraction of max leaf area index corresponding to the 2nd point on optimal leaf area development curve | [[plant_data_module.f90#pldb]] | [[plant_parm_read.f90]]:55 |
| `pldb%dlai` | `real` | none | frac of growing season when leaf are declines | [[plant_data_module.f90#pldb]] | [[plant_parm_read.f90]]:55 |
| `pldb%dlai_rate` | `real` | none | exponent that governs lai decline rate | [[plant_data_module.f90#pldb]] | [[plant_parm_read.f90]]:55 |
| `pldb%chtmx` | `real` | m | maximum canopy height | [[plant_data_module.f90#pldb]] | [[plant_parm_read.f90]]:55 |
| `pldb%rdmx` | `real` | m | maximum root depth | [[plant_data_module.f90#pldb]] | [[plant_parm_read.f90]]:55 |
| `pldb%t_opt` | `real` | deg C | optimal temp for plant growth | [[plant_data_module.f90#pldb]] | [[plant_parm_read.f90]]:55 |
| `pldb%t_base` | `real` | deg C | minimum temp for plant growth | [[plant_data_module.f90#pldb]] | [[plant_parm_read.f90]]:55 |
| `pldb%cnyld` | `real` | kg N/kg yld | frac of nitrogen in yield | [[plant_data_module.f90#pldb]] | [[plant_parm_read.f90]]:55 |
| `pldb%cpyld` | `real` | kg P/kg yld | frac of phosphorus in yield | [[plant_data_module.f90#pldb]] | [[plant_parm_read.f90]]:55 |
| `pldb%pltnfr1` | `real` | kg N/kg biomass | nitrogen uptake parm #1 | [[plant_data_module.f90#pldb]] | [[plant_parm_read.f90]]:55 |
| `pldb%pltnfr2` | `real` | kg N/kg biomass | nitrogen uptake parm #2 | [[plant_data_module.f90#pldb]] | [[plant_parm_read.f90]]:55 |
| `pldb%pltnfr3` | `real` | kg N/kg/biomass | nitrogen uptake parm #3 | [[plant_data_module.f90#pldb]] | [[plant_parm_read.f90]]:55 |
| `pldb%pltpfr1` | `real` | kg P/kg/biomass | phoshorus uptake parm #1 | [[plant_data_module.f90#pldb]] | [[plant_parm_read.f90]]:55 |
| `pldb%pltpfr2` | `real` | kg P/kg/biomass | phoshorus uptake parm #2 | [[plant_data_module.f90#pldb]] | [[plant_parm_read.f90]]:55 |
| `pldb%pltpfr3` | `real` | kg P/kg/biomass | phoshorus uptake parm #3 | [[plant_data_module.f90#pldb]] | [[plant_parm_read.f90]]:55 |
| `pldb%wsyf` | `real` | (kg/ha)/(kg/ha) | value of harvest index bet 0 and HVSTI | [[plant_data_module.f90#pldb]] | [[plant_parm_read.f90]]:55 |
| `pldb%usle_c` | `real` | none | minimum value of the USLE C factor for water erosion | [[plant_data_module.f90#pldb]] | [[plant_parm_read.f90]]:55 |
| `pldb%gsi` | `real` | m/s | maximum stomatal conductance | [[plant_data_module.f90#pldb]] | [[plant_parm_read.f90]]:55 |
| `pldb%vpdfr` | `real` | kPa | vapor pressure deficit at which GMAXFR is valid | [[plant_data_module.f90#pldb]] | [[plant_parm_read.f90]]:55 |
| `pldb%gmaxfr` | `real` | none | fraction of max stomatal conductance that is achieved at the vapor pressure deficit defined by VPDFR | [[plant_data_module.f90#pldb]] | [[plant_parm_read.f90]]:55 |
| `pldb%wavp` | `real` | none | rate of decline in radiation use efficiency | [[plant_data_module.f90#pldb]] | [[plant_parm_read.f90]]:55 |
| `pldb%co2hi` | `real` | uL CO2/L air | CO2 concentration higher than the ambient corresponding to the 2nd point on radiation use efficiency curve | [[plant_data_module.f90#pldb]] | [[plant_parm_read.f90]]:55 |
| `pldb%bioehi` | `real` | (kg/ha)/(MJ/m**2) | biomass-energy ratio when plant is in an environment with CO2 level equal to the value of CO2HI. | [[plant_data_module.f90#pldb]] | [[plant_parm_read.f90]]:55 |
| `pldb%rsdco_pl` | `real` | none | plant residue decomposition coeff | [[plant_data_module.f90#pldb]] | [[plant_parm_read.f90]]:55 |
| `pldb%alai_min` | `real` | m**2/m**2 | min LAI during winter dormant period | [[plant_data_module.f90#pldb]] | [[plant_parm_read.f90]]:55 |
| `pldb%laixco_tree` | `real` | none | coefficient to estimate max lai during tree growth | [[plant_data_module.f90#pldb]] | [[plant_parm_read.f90]]:55 |
| `pldb%mat_yrs` | `integer` | years | years to maturity | [[plant_data_module.f90#pldb]] | [[plant_parm_read.f90]]:55 |
| `pldb%bmx_peren` | `real` | metric tons/ha | max biomass for forest | [[plant_data_module.f90#pldb]] | [[plant_parm_read.f90]]:55 |
| `pldb%ext_coef` | `real` |  | light extinction coefficient | [[plant_data_module.f90#pldb]] | [[plant_parm_read.f90]]:55 |
| `pldb%leaf_tov_min` | `real` | months | perennial leaf turnover rate with minimum stress (complete turnover in 12 mon) | [[plant_data_module.f90#pldb]] | [[plant_parm_read.f90]]:55 |
| `pldb%leaf_tov_max` | `real` | months | perennial leaf turnover rate with maximum stress (complete turnover in 3 mon) | [[plant_data_module.f90#pldb]] | [[plant_parm_read.f90]]:55 |
| `pldb%bm_dieoff` | `real` | frac | above ground biomass that dies off at dormancy | [[plant_data_module.f90#pldb]] | [[plant_parm_read.f90]]:55 |
| `pldb%rsr1` | `real` | frac | initial root to shoot ratio at the beg of growing season | [[plant_data_module.f90#pldb]] | [[plant_parm_read.f90]]:55 |
| `pldb%rsr2` | `real` | frac | root to shoot ratio at the end of the growing season | [[plant_data_module.f90#pldb]] | [[plant_parm_read.f90]]:55 |
| `pldb%pop1` | `real` | plants/m^2 | plant population corresponding to the 1st point on the population lai curve | [[plant_data_module.f90#pldb]] | [[plant_parm_read.f90]]:55 |
| `pldb%frlai1` | `real` | frac | frac of max leaf area index corresponding to the 1st point on the leaf area development curve | [[plant_data_module.f90#pldb]] | [[plant_parm_read.f90]]:55 |
| `pldb%pop2` | `real` | plants/m^2 | plant population corresponding to the 2nd point on the population lai curve | [[plant_data_module.f90#pldb]] | [[plant_parm_read.f90]]:55 |
| `pldb%frlai2` | `real` | frac | frac of max leaf area index corresponding to the 2nd point on the leaf area development curve | [[plant_data_module.f90#pldb]] | [[plant_parm_read.f90]]:55 |
| `pldb%frsw_gro` | `real` | frac | 30 day sum of P-PET to initiate growth of tropical plants during monsoon season - pcom()%plcur()%iseason | [[plant_data_module.f90#pldb]] | [[plant_parm_read.f90]]:55 |
| `pldb%aeration` | `real` |  | aeration stress factor | [[plant_data_module.f90#pldb]] | [[plant_parm_read.f90]]:55 |
| `pldb%rsd_pctcov` | `real` |  | residue factor for percent cover equation | [[plant_data_module.f90#pldb]] | [[plant_parm_read.f90]]:55 |
| `pldb%rsd_covfac` | `real` |  | residue factor for surface cover (C factor) equation | [[plant_data_module.f90#pldb]] | [[plant_parm_read.f90]]:55 |
| `pldb%res_part_fracs%meta_frac` | `real` | none | reads plants.plt avg_lig_frac | [[plant_data_module.f90#pldb]] | [[plant_parm_read.f90]]:55 |
| `pldb%res_part_fracs%str_frac` | `real` | none | reads plants.plt ab_lig_frac (used as above-ground lignin) | [[plant_data_module.f90#pldb]] | [[plant_parm_read.f90]]:55 |
| `pldb%res_part_fracs%lig_frac` | `real` | none | reads plants.plt bg_lig_frac (used as below-ground lignin) | [[plant_data_module.f90#pldb]] | [[plant_parm_read.f90]]:55 |
| `pl_class` | `character(len=25), dimension(:), allocatable` | none | plant class - row crop, tree, grass, etc | [[plant_data_module.f90#pl_class]] | [[plant_parm_read.f90]]:57 |
