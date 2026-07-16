---
type: input
tags:
  - swat/input
file: weather-wgn.cli
ext: cli
cio_field: weat_wgn
read_by:
  - cli_wgnread.f90
purpose: ""
---

# weather-wgn.cli

> [!info] Input File
> Declared in `file.cio` field `weat_wgn`. See [[file.cio]] for the controlling file map.

## Overview
- **Declared in `file.cio` field**: `weat_wgn`
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[cli_wgnread.f90]]

## File Structure
- [[cli_wgnread.f90]] source line 45: reads `titldum`
- [[cli_wgnread.f90]] source line 49: reads `titldum`
- [[cli_wgnread.f90]] source line 51: reads `header`
- [[cli_wgnread.f90]] source line 54: reads `titldum`
- [[cli_wgnread.f90]] source line 85: reads `titldum`
- [[cli_wgnread.f90]] source line 91: reads `wgn_n(iwgn)`, `wgn(iwgn)%lat`, `wgn(iwgn)%long`, `wgn(iwgn)%elev`, `wgn(iwgn)%rain_yrs`
- [[cli_wgnread.f90]] source line 93: reads `header`
- [[cli_wgnread.f90]] source line 96: reads `wgn(iwgn)%tmpmx(mo)`, `wgn(iwgn)%tmpmn(mo)`, `wgn(iwgn)%tmpstdmx(mo)`, `wgn(iwgn)%tmpstdmn(mo)`, `wgn(iwgn)%pcpmm(mo)`, `wgn(iwgn)%pcpstd(mo)`, `wgn(iwgn)%pcpskw(mo)`, `wgn(iwgn)%pr_wd(mo)`, `wgn(iwgn)%pr_ww(mo)`, `wgn(iwgn)%pcpd(mo)`, `wgn(iwgn)%rainhmx(mo)`, `wgn(iwgn)%solarav(mo)`, `wgn(iwgn)%dewpt(mo)`, `wgn(iwgn)%windav(mo)`

## Parameters
| Parameter | Type | Units | Meaning | Source | Reader line |
|---|---|---|---|---|---:|
| `wgn_n` | `character(len=50), dimension(:), allocatable` |  |  | [[climate_module.f90#wgn_n]] | [[cli_wgnread.f90]]:91 |
| `wgn%lat` | `real` | degrees | latitude of weather station used to compile data | [[climate_module.f90#wgn]] | [[cli_wgnread.f90]]:91 |
| `wgn%long` | `real` | degrees | longitude of weather station | [[climate_module.f90#wgn]] | [[cli_wgnread.f90]]:91 |
| `wgn%elev` | `real` |  | elevation of weather station used to compile weather generator data | [[climate_module.f90#wgn]] | [[cli_wgnread.f90]]:91 |
| `wgn%rain_yrs` | `real` | none | number of years of recorded maximum 0.5h rainfall used to calculate values for rainhhmx(:) | [[climate_module.f90#wgn]] | [[cli_wgnread.f90]]:91 |
| `wgn%tmpmx` | `real, dimension (12)` | deg C | avg monthly maximum air temperature | [[climate_module.f90#wgn]] | [[cli_wgnread.f90]]:96 |
| `wgn%tmpmn` | `real, dimension (12)` | deg C | avg monthly minimum air temperature | [[climate_module.f90#wgn]] | [[cli_wgnread.f90]]:96 |
| `wgn%tmpstdmx` | `real, dimension (12)` | deg C | standard deviation for avg monthly maximum air temperature | [[climate_module.f90#wgn]] | [[cli_wgnread.f90]]:96 |
| `wgn%tmpstdmn` | `real, dimension (12)` | deg C | standard deviation for avg monthly minimum air temperature | [[climate_module.f90#wgn]] | [[cli_wgnread.f90]]:96 |
| `wgn%pcpmm` | `real, dimension (12)` | mm | amount of precipitation in month | [[climate_module.f90#wgn]] | [[cli_wgnread.f90]]:96 |
| `wgn%pcpstd` | `real, dimension (12)` | mm/day | standard deviation for the average daily | [[climate_module.f90#wgn]] | [[cli_wgnread.f90]]:96 |
| `wgn%pcpskw` | `real, dimension (12)` | none | skew coefficient for the average daily precipitation | [[climate_module.f90#wgn]] | [[cli_wgnread.f90]]:96 |
| `wgn%pr_wd` | `real, dimension (12)` | none | probability of wet day after dry day in month | [[climate_module.f90#wgn]] | [[cli_wgnread.f90]]:96 |
| `wgn%pr_ww` | `real, dimension (12)` | none | probability of wet day after wet day in month | [[climate_module.f90#wgn]] | [[cli_wgnread.f90]]:96 |
| `wgn%pcpd` | `real, dimension (12)` | days | average number of days of precipitation in the month | [[climate_module.f90#wgn]] | [[cli_wgnread.f90]]:96 |
| `wgn%rainhmx` | `real, dimension (12)` | mm | maximum 0.5 hour rainfall in month | [[climate_module.f90#wgn]] | [[cli_wgnread.f90]]:96 |
| `wgn%solarav` | `real, dimension (12)` | MJ/m^2/day | average daily solar radiation for the month | [[climate_module.f90#wgn]] | [[cli_wgnread.f90]]:96 |
| `wgn%dewpt` | `real, dimension (12)` | deg C | average dew point temperature for the month | [[climate_module.f90#wgn]] | [[cli_wgnread.f90]]:96 |
| `wgn%windav` | `real, dimension (12)` | m/s | average wind speed for the month | [[climate_module.f90#wgn]] | [[cli_wgnread.f90]]:96 |
