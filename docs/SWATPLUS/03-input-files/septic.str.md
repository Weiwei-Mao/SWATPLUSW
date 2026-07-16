---
type: input
tags:
  - swat/input
file: septic.str
ext: str
cio_field: septic_str
read_by:
  - sep_read.f90
purpose: ""
---

# septic.str

> [!info] Input File
> Declared in `file.cio` field `septic_str`. See [[file.cio]] for the controlling file map.

## Overview
- **Declared in `file.cio` field**: `septic_str`
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[sep_read.f90]]

## File Structure
- [[sep_read.f90]] source line 25: reads `titldum`
- [[sep_read.f90]] source line 27: reads `header`
- [[sep_read.f90]] source line 30: reads `titldum`
- [[sep_read.f90]] source line 37: reads `titldum`
- [[sep_read.f90]] source line 39: reads `header`
- [[sep_read.f90]] source line 43: reads `sep(isep)`

## Parameters
| Parameter | Type | Units | Meaning | Source | Reader line |
|---|---|---|---|---|---:|
| `sep%name` | `character(len=13)` |  |  | [[septic_data_module.f90#sep]] | [[sep_read.f90]]:43 |
| `sep%typ` | `integer` | none | septic system type | [[septic_data_module.f90#sep]] | [[sep_read.f90]]:43 |
| `sep%yr` | `integer` |  | year the septic system became operational | [[septic_data_module.f90#sep]] | [[sep_read.f90]]:43 |
| `sep%opt` | `integer` | none | Septic system operation flag (1=active,2=failing,0=not operated) | [[septic_data_module.f90#sep]] | [[sep_read.f90]]:43 |
| `sep%cap` | `real` | none | Number of permanent residents in the house | [[septic_data_module.f90#sep]] | [[sep_read.f90]]:43 |
| `sep%area` | `real` | m^2 | average area of drainfield of individual septic systems | [[septic_data_module.f90#sep]] | [[sep_read.f90]]:43 |
| `sep%tfail` | `integer` | days | time until falling systems gets fixed | [[septic_data_module.f90#sep]] | [[sep_read.f90]]:43 |
| `sep%z` | `real` | mm | depth to the top of the biozone layer from the ground surface | [[septic_data_module.f90#sep]] | [[sep_read.f90]]:43 |
| `sep%thk` | `real` | mm | thickness of biozone layer | [[septic_data_module.f90#sep]] | [[sep_read.f90]]:43 |
| `sep%strm_dist` | `real` | km | distance to the stream from the septic | [[septic_data_module.f90#sep]] | [[sep_read.f90]]:43 |
| `sep%density` | `real` |  | number of septic systems per square kilometer | [[septic_data_module.f90#sep]] | [[sep_read.f90]]:43 |
| `sep%bd` | `real` | kg/m^3 | density of biomass | [[septic_data_module.f90#sep]] | [[sep_read.f90]]:43 |
| `sep%bod_dc` | `real` | m^3/day | BOD decay rate coefficient | [[septic_data_module.f90#sep]] | [[sep_read.f90]]:43 |
| `sep%bod_conv` | `real` |  | a conversion factor representing the proportion of mass bacterial growth and mass BOD degraded in the STE. | [[septic_data_module.f90#sep]] | [[sep_read.f90]]:43 |
| `sep%fc1` | `real` | none | Linear coefficient for calculation of field capacity in the biozone | [[septic_data_module.f90#sep]] | [[sep_read.f90]]:43 |
| `sep%fc2` | `real` | none | Exponential coefficient for calculation of field capacity in the biozone | [[septic_data_module.f90#sep]] | [[sep_read.f90]]:43 |
| `sep%fecal` | `real` | m^3/day | fecal coliform bacteria decay rate coefficient | [[septic_data_module.f90#sep]] | [[sep_read.f90]]:43 |
| `sep%plq` | `real` | none | conversion factor for plaque from TDS | [[septic_data_module.f90#sep]] | [[sep_read.f90]]:43 |
| `sep%mrt` | `real` | none | mortality rate coefficient | [[septic_data_module.f90#sep]] | [[sep_read.f90]]:43 |
| `sep%rsp` | `real` | none | respiration rate coefficient | [[septic_data_module.f90#sep]] | [[sep_read.f90]]:43 |
| `sep%slg1` | `real` | none | slough-off calibration parameter | [[septic_data_module.f90#sep]] | [[sep_read.f90]]:43 |
| `sep%slg2` | `real` | none | slough-off calibration parameter | [[septic_data_module.f90#sep]] | [[sep_read.f90]]:43 |
| `sep%nitr` | `real` | none | nitrification rate coefficient | [[septic_data_module.f90#sep]] | [[sep_read.f90]]:43 |
| `sep%denitr` | `real` | none | denitrification rate coefficient | [[septic_data_module.f90#sep]] | [[sep_read.f90]]:43 |
| `sep%pdistrb` | `real` | (L/kg) | Linear P sorption distribution coefficient | [[septic_data_module.f90#sep]] | [[sep_read.f90]]:43 |
| `sep%psorpmax` | `real` | (mg P/kg Soil) | Maximum P sorption capacity | [[septic_data_module.f90#sep]] | [[sep_read.f90]]:43 |
| `sep%solpslp` | `real` |  | Slope of the linear effluent soluble P equation | [[septic_data_module.f90#sep]] | [[sep_read.f90]]:43 |
| `sep%solpintc` | `real` |  | Intercept of the linear effluent soluble P equation | [[septic_data_module.f90#sep]] | [[sep_read.f90]]:43 |
