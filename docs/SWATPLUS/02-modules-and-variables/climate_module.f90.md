---
type: module
tags:
  - swat/module
  - swat/to-read
file: climate_module.f90
note_file: climate_module.f90
module_name: climate_module
defines_types:
  - weather_generator_db
  - wgn_parms
  - wind_direction_db
  - weather_daily
  - weather_codes_station
  - weather_codes_station_char
  - weather_station
  - climate_change_variables
  - climate_measured_data
  - atmospheric_deposition
  - atmospheric_deposition_control
  - atmospheric_deposition_cs
  - object_deposition_cs
  - road_salt
  - object_road_salt
defines_vars:
  - ppet_ndays
  - ppet_mce
  - frad
  - wgncur
  - wgnold
  - elevp
  - elevt
  - idg
  - rndseed
  - rnd2
  - rnd3
  - rnd8
  - rnd9
  - rndseed_cond
  - co2y
  - wgn
  - wgn_orig
  - wgn_pms
  - wnd_dir
  - w
  - wst
  - pcp
  - tmp
  - slr
  - hmd
  - wnd
  - petm
  - atmodep
  - atmodep_cont
  - salt_atmo
  - cs_atmo
  - atmodep_salt
  - atmodep_cs
  - rdapp_salt
  - wst_n
  - wgn_n
  - pcp_n
  - tmp_n
  - slr_n
  - hmd_n
  - wnd_n
  - atmo_n
  - petm_n
defines_subroutines: []
defines_functions: []
defines_procedures: []
purpose: ""
---

# climate_module

> [!info] Module
> Defines derived types and module-level variables.

## Defined Types
### weather_generator_db

- **Defined in source**: `climate_module.f90:24`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `lat` | `real` | 25 | degrees \|latitude of weather station used to compile data |
| `long` | `real` | 26 | degrees \|longitude of weather station |
| `elev` | `real` | 27 | \|elevation of weather station used to compile weather generator data |
| `rain_yrs` | `real` | 28 | none \|number of years of recorded maximum 0.5h rainfall used to calculate values for rainhhmx(:) |
| `tmpmx` | `real, dimension (12)` | 29 | deg C \|avg monthly maximum air temperature |
| `tmpmn` | `real, dimension (12)` | 30 | deg C \|avg monthly minimum air temperature |
| `tmpstdmx` | `real, dimension (12)` | 31 | deg C \|standard deviation for avg monthly maximum air temperature |
| `tmpstdmn` | `real, dimension (12)` | 32 | deg C \|standard deviation for avg monthly minimum air temperature |
| `pcpmm` | `real, dimension (12)` | 33 | mm \|amount of precipitation in month |
| `pcpstd` | `real, dimension (12)` | 34 | mm/day \|standard deviation for the average daily |
| `pcpskw` | `real, dimension (12)` | 35 | none \|skew coefficient for the average daily precipitation |
| `pr_wd` | `real, dimension (12)` | 36 | none \|probability of wet day after dry day in month |
| `pr_ww` | `real, dimension (12)` | 37 | none \|probability of wet day after wet day in month |
| `pcpd` | `real, dimension (12)` | 38 | days \|average number of days of precipitation in the month |
| `rainhmx` | `real, dimension (12)` | 39 | mm \|maximum 0.5 hour rainfall in month |
| `solarav` | `real, dimension (12)` | 40 | MJ/m^2/day \|average daily solar radiation for the month |
| `dewpt` | `real, dimension (12)` | 41 | deg C \|average dew point temperature for the month |
| `windav` | `real, dimension (12)` | 42 | m/s \|average wind speed for the month |

### wgn_parms

- **Defined in source**: `climate_module.f90:47`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `pr_wdays` | `real, dimension (12)` | 48 | none \|proportion of wet days in a month |
| `pcpmean` | `real, dimension (12)` | 49 | mm/day \|average amount of precipitation falling in one day for the month |
| `daylmn` | `real` | 50 | \|minimum day length |
| `daylth` | `real` | 51 | \|day length threshold to trigger dormancy |
| `latsin` | `real` | 52 | \|sine of latitude |
| `latcos` | `real` | 53 | \|cosine of latitude |
| `phutot` | `real` | 54 | \|total base zero heat units for year |
| `pcpdays` | `real` | 55 | \|days of precip in year |
| `tmp_an` | `real` | 56 | \|average annual air temperature |
| `pcp_an` | `real` | 57 | \|average annual precipitation |
| `ppet_an` | `real` | 58 | \|average annual precip/pet |
| `precip_sum` | `real` | 59 | \|30 day sum of PET (mm) |
| `pet_sum` | `real` | 60 | \|30 day sum of PRECIP (mm) |
| `p_pet_rto` | `real` | 61 | \|30 day sum of PRECIP/PET ratio |
| `pcf` | `real, dimension (12)` | 62 | \|normalization factor for precipitation |
| `amp_r` | `real, dimension (12)` | 63 | \|alpha factor for rain(mo max 0.5h rain) |
| `pet` | `real, dimension (12)` | 64 | \|average monthly PET (mm) |
| `mne_ppet` | `integer, dimension (:), allocatable` | 65 | none \|next element in precip-pet linked list |
| `precip_mce` | `real, dimension (:), allocatable` | 66 | mm \|precip on current day of 30 day list |
| `pet_mce` | `real, dimension (:), allocatable` | 67 | mm \|pet on current day of 30 day list |
| `ireg` | `integer` | 68 | \|annual precip category-1 <= 508 mm; 2 > 508 and <= 1016 mm; 3 > 1016 mm/yr |
| `idewpt` | `integer` | 69 | \|0=dewpoint; 1=rel humididty input |

### wind_direction_db

- **Defined in source**: `climate_module.f90:73`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `name` | `character(len=16)` | 74 |  |
| `dir` | `real, dimension (12,16)` | 75 | 1-16 \|avg monthly wind direstion |

### weather_daily

- **Defined in source**: `climate_module.f90:79`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `precip` | `real` | 80 |  |
| `precip_next` | `real` | 81 | mm \|precip generated for next day |
| `tmax` | `real` | 82 |  |
| `tmin` | `real` | 83 |  |
| `tave` | `real` | 84 |  |
| `solrad` | `real` | 85 |  |
| `solradmx` | `real` | 86 |  |
| `rhum` | `real` | 87 |  |
| `dewpt` | `real` | 88 |  |
| `windsp` | `real` | 89 |  |
| `pet` | `real` | 90 |  |
| `wndir` | `real` | 92 |  |
| `phubase0` | `real` | 93 | deg C \|cumulative base 0 heat units |
| `ppet` | `real` | 94 | mm/mm \|climatic moisture index - cumulative p/pet |
| `daylength` | `real` | 95 | hr \|day length |
| `precip_half_hr` | `real` | 96 | frac \|fraction of total rainfall on day that occurs during 0.5h highest intensity rainfall |
| `precip_prior_day` | `character(len=3)` | 98 | \|"dry" or "wet" |
| `ts` | `real, dimension(:), allocatable` | 99 | mm \|subdaily precip - current day |
| `ts_next` | `real, dimension(:), allocatable` | 100 | mm \|subdaily precip - next day |

### weather_codes_station

- **Defined in source**: `climate_module.f90:104`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `wgn` | `integer` | 105 | weather generator station number |
| `pgage` | `integer` | 106 | gage number for rainfall (sim if generating) |
| `tgage` | `integer` | 107 | gage number for temperature (sim if generating) |
| `sgage` | `integer` | 108 | gage number for solar radiation (sim if generating) |
| `hgage` | `integer` | 109 | gage number for relative humidity (sim if generating) |
| `wgage` | `integer` | 110 | gage number for windspeed (sim if generating) |
| `petgage` | `integer` | 111 | number of pet gage files used in sim |
| `atmodep` | `integer` | 112 | atmospheric depostion data file locator |

### weather_codes_station_char

- **Defined in source**: `climate_module.f90:115`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `wgn` | `character (len=50)` | 117 | weather generator name |
| `pgage` | `character (len=50)` | 118 | gage name for rainfall |
| `tgage` | `character (len=50)` | 119 | gage name for temperature |
| `sgage` | `character (len=50)` | 120 | gage name for solar radiation |
| `hgage` | `character (len=50)` | 121 | gage name for relative humidity |
| `wgage` | `character (len=50)` | 122 | gage name for windspeed |
| `petgage` | `character (len=50)` | 123 | name of pet gage |
| `atmodep` | `character (len=50)` | 124 | atmospheric depostion data file locator |

### weather_station

- **Defined in source**: `climate_module.f90:127`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `name` | `character(len=50)` | 128 |  |
| `lat` | `real` | 129 | degrees \|latitude |
| `wco_c` | `weather_codes_station_char` | 130 |  |
| `wco` | `weather_codes_station` | 131 |  |
| `weat` | `weather_daily` | 132 |  |
| `precip_aa` | `real` | 133 | mm \|average annual precipitation |
| `pet_aa` | `real` | 134 | mm \|average annual potential ET |
| `pcp_ts` | `integer` | 135 | 1/day \|precipitation time steps per day (0 or 1 = daily) |
| `rfinc` | `real, dimension(12)` | 136 | deg C \|monthly precipitation adjustment |
| `tmpinc` | `real, dimension(12)` | 137 | deg C \|monthly temperature adjustment |
| `radinc` | `real, dimension(12)` | 138 | MJ/m^2 \|monthly solar radiation adjustment |
| `huminc` | `real, dimension(12)` | 139 | none \|monthly humidity adjustment |
| `tlag` | `real, dimension(:), allocatable` | 140 | deg C \|daily average temperature for channel temp lag |
| `airlag_temp` | `real` | 141 | deg C \|average temperature w_temp%airlag_d days ago |
| `tlag_mne` | `integer` | 142 | \|next element (day) for the air temp linked list |

### climate_change_variables

- **Defined in source**: `climate_module.f90:146`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `name` | `character(len=50)` | 147 |  |
| `ref_yr` | `integer` | 148 | none \|reference year to begin incremental adjustments |
| `co2inc` | `real` | 149 | ppm \|annual CO2 increment |
| `rfinc` | `real, dimension(12)` | 150 | deg C \|monthly precipitation annual increment |
| `tmpinc` | `real, dimension(12)` | 151 | deg C \|monthly temperature annual increment |
| `radinc` | `real, dimension(12)` | 152 | MJ/m^2 \|monthly solar radiation annual increment |
| `huminc` | `real, dimension(12)` | 153 | none \|monthly humidity annual increment |
| `co2scen` | `real` | 154 | ppm \|annual CO2 scenario adjustment |
| `rfscen` | `real, dimension(12)` | 155 | deg C \|monthly precipitation scenario adjustment |
| `tmpscen` | `real, dimension(12)` | 156 | deg C \|monthly temperature scenario adjustment |
| `radscen` | `real, dimension(12)` | 157 | MJ/m^2 \|monthly solar radiation scenario adjustment |
| `humscen` | `real, dimension(12)` | 158 | none \|monthly humidity scenario adjustment |

### climate_measured_data

- **Defined in source**: `climate_module.f90:161`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `filename` | `character (len=50)` | 162 |  |
| `lat` | `real` | 163 | latitude of raingage |
| `long` | `real` | 164 | longitude of raingage |
| `elev` | `real` | 165 | elevation of raingage |
| `nbyr` | `integer` | 166 | number of years of daily rainfall |
| `tstep` | `integer` | 167 | timestep of precipitation |
| `days_gen` | `integer` | 169 | number of missing days - generated |
| `yrs_start` | `integer` | 170 | number of years of simulation before record starts |
| `start_day` | `integer` | 172 | daily precip start julian day |
| `start_yr` | `integer` | 173 | daily precip start year |
| `end_day` | `integer` | 174 | daily precip end julian day |
| `end_yr` | `integer` | 175 | daily precip end year |
| `mean_mon` | `real, dimension (12)` | 176 | same as variable unit \|mean monthly measured value |
| `max_mon` | `real, dimension (12)` | 177 | same as variable unit \|maximum monthly measured value |
| `min_mon` | `real, dimension (12)` | 178 | same as variable unit \|minimum monthly measured value |
| `ts` | `real, dimension (:,:), allocatable` | 180 |  |
| `ts2` | `real, dimension (:,:), allocatable` | 181 |  |
| `tss` | `real, dimension (:,:,:), allocatable` | 182 |  |

### atmospheric_deposition

- **Defined in source**: `climate_module.f90:191`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `nh4_rf` | `real` | 192 | ave annual ammonia in rainfall - mg/l |
| `no3_rf` | `real` | 193 | ave annual nitrate in rainfall - mg/l |
| `nh4_dry` | `real` | 194 | ave annual ammonia dry deposition - kg/ha/yr |
| `no3_dry` | `real` | 195 | ave annual nitrate dry deposition - kg/ha/yr |
| `name` | `character(len=50)` | 196 |  |
| `nh4_rfmo` | `real, dimension(:), allocatable` | 197 |  |
| `no3_rfmo` | `real, dimension(:), allocatable` | 198 |  |
| `nh4_drymo` | `real, dimension(:), allocatable` | 199 |  |
| `no3_drymo` | `real, dimension(:), allocatable` | 200 |  |
| `nh4_rfyr` | `real, dimension(:), allocatable` | 201 |  |
| `no3_rfyr` | `real, dimension(:), allocatable` | 202 |  |
| `nh4_dryyr` | `real, dimension(:), allocatable` | 203 |  |
| `no3_dryyr` | `real, dimension(:), allocatable` | 204 |  |

### atmospheric_deposition_control

- **Defined in source**: `climate_module.f90:208`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `num_sta` | `integer` | 209 |  |
| `timestep` | `character(len=2)` | 210 |  |
| `ts` | `integer` | 211 |  |
| `mo_init` | `integer` | 212 |  |
| `yr_init` | `integer` | 213 |  |
| `num` | `integer` | 214 |  |
| `first` | `integer` | 215 |  |

### atmospheric_deposition_cs

- **Defined in source**: `climate_module.f90:223`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `rf` | `real` | 224 | concentration in rainfall - mg/l |
| `dry` | `real` | 225 | dry deposition - kg/ha/yr |
| `rfmo` | `real, dimension(:), allocatable` | 226 |  |
| `drymo` | `real, dimension(:), allocatable` | 227 |  |
| `rfyr` | `real, dimension(:), allocatable` | 228 |  |
| `dryyr` | `real, dimension(:), allocatable` | 229 |  |

### object_deposition_cs

- **Defined in source**: `climate_module.f90:231`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `salt` | `atmospheric_deposition_cs` | 232 |  |
| `cs` | `atmospheric_deposition_cs` | 233 |  |

### road_salt

- **Defined in source**: `climate_module.f90:239`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `road` | `real` | 240 | ave annual salt ion loading via road salt application (kg/ha) |
| `roadday` | `real, dimension(:,:), allocatable` | 241 | daily salt ion loading via road salt application (kg/ha) |
| `roadmo` | `real, dimension(:), allocatable` | 242 | monthly salt ion loading via road salt application (kg/ha) |
| `roadyr` | `real, dimension(:), allocatable` | 243 | yearly salt ion loading via road salt application (kg/ha) |

### object_road_salt

- **Defined in source**: `climate_module.f90:245`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `salt` | `road_salt` | 246 |  |

## Variables Defined
### ppet_ndays

- **Type**: `integer`
- **Defined in source**: `climate_module.f90:5`
- **Source note**: none          |number of days for precip/pet sum

### ppet_mce

- **Type**: `integer`
- **Defined in source**: `climate_module.f90:6`
- **Source note**: none          |current element in precip/pet linked list

### frad

- **Type**: `real, dimension (:,:), allocatable`
- **Defined in source**: `climate_module.f90:7`
- **Source note**: none          |fraction of solar radiation occurring

### wgncur

- **Type**: `real, dimension (:,:), allocatable`
- **Defined in source**: `climate_module.f90:9`
- **Source note**: none          |parameter to predict the impact of precip on

### wgnold

- **Type**: `real, dimension (:,:), allocatable`
- **Defined in source**: `climate_module.f90:11`
- **Source note**: none          |previous value of wgncur(:,:)

### elevp

- **Type**: `integer, dimension (:), allocatable`
- **Defined in source**: `climate_module.f90:12`
- **Source note**: m             |elevation of precipitation gage station

### elevt

- **Type**: `integer, dimension (:), allocatable`
- **Defined in source**: `climate_module.f90:13`
- **Source note**: m             |elevation of temperature gage station

### idg

- **Type**: `integer, dimension (:), allocatable`
- **Defined in source**: `climate_module.f90:14`
- **Source note**: none          |array location of random number seed

### rndseed

- **Type**: `integer, dimension (:,:), allocatable`
- **Defined in source**: `climate_module.f90:16`
- **Source note**: none          |random number generator seeds

### rnd2

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `climate_module.f90:17`
- **Source note**: none          |random number between 0.0 and 1.0

### rnd3

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `climate_module.f90:18`
- **Source note**: none          |random number between 0.0 and 1.0

### rnd8

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `climate_module.f90:19`
- **Source note**: none          |random number between 0.0 and 1.0

### rnd9

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `climate_module.f90:20`
- **Source note**: none          |random number between 0.0 and 1.0

### rndseed_cond

- **Type**: `integer`
- **Defined in source**: `climate_module.f90:21`
- **Source note**: random number seed for dtbl conditional

### co2y

- **Type**: `real, dimension(:), allocatable`
- **Defined in source**: `climate_module.f90:22`

### wgn

- **Type**: `weather_generator_db`
- **Defined in source**: `climate_module.f90:44`

### wgn_orig

- **Type**: `weather_generator_db`
- **Defined in source**: `climate_module.f90:45`

### wgn_pms

- **Type**: `wgn_parms`
- **Defined in source**: `climate_module.f90:71`

### wnd_dir

- **Type**: `wind_direction_db`
- **Defined in source**: `climate_module.f90:77`

### w

- **Type**: `weather_daily`
- **Defined in source**: `climate_module.f90:102`

### wst

- **Type**: `weather_station`
- **Defined in source**: `climate_module.f90:144`

### pcp

- **Type**: `climate_measured_data`
- **Defined in source**: `climate_module.f90:184`

### tmp

- **Type**: `climate_measured_data`
- **Defined in source**: `climate_module.f90:185`

### slr

- **Type**: `climate_measured_data`
- **Defined in source**: `climate_module.f90:186`

### hmd

- **Type**: `climate_measured_data`
- **Defined in source**: `climate_module.f90:187`

### wnd

- **Type**: `climate_measured_data`
- **Defined in source**: `climate_module.f90:188`

### petm

- **Type**: `climate_measured_data`
- **Defined in source**: `climate_module.f90:189`

### atmodep

- **Type**: `atmospheric_deposition`
- **Defined in source**: `climate_module.f90:206`

### atmodep_cont

- **Type**: `atmospheric_deposition_control`
- **Defined in source**: `climate_module.f90:217`

### salt_atmo

- **Type**: `character(len=1)`
- **Defined in source**: `climate_module.f90:220`

### cs_atmo

- **Type**: `character(len=1)`
- **Defined in source**: `climate_module.f90:221`

### atmodep_salt

- **Type**: `object_deposition_cs`
- **Defined in source**: `climate_module.f90:235`

### atmodep_cs

- **Type**: `object_deposition_cs`
- **Defined in source**: `climate_module.f90:236`

### rdapp_salt

- **Type**: `object_road_salt`
- **Defined in source**: `climate_module.f90:248`
- **Source note**: applied road salt

### wst_n

- **Type**: `character(len=50), dimension(:), allocatable`
- **Defined in source**: `climate_module.f90:250`

### wgn_n

- **Type**: `character(len=50), dimension(:), allocatable`
- **Defined in source**: `climate_module.f90:251`

### pcp_n

- **Type**: `character(len=50), dimension(:), allocatable`
- **Defined in source**: `climate_module.f90:252`

### tmp_n

- **Type**: `character(len=50), dimension(:), allocatable`
- **Defined in source**: `climate_module.f90:253`

### slr_n

- **Type**: `character(len=50), dimension(:), allocatable`
- **Defined in source**: `climate_module.f90:254`

### hmd_n

- **Type**: `character(len=50), dimension(:), allocatable`
- **Defined in source**: `climate_module.f90:255`

### wnd_n

- **Type**: `character(len=50), dimension(:), allocatable`
- **Defined in source**: `climate_module.f90:256`

### atmo_n

- **Type**: `character(len=50), dimension(:), allocatable`
- **Defined in source**: `climate_module.f90:257`

### petm_n

- **Type**: `character(len=50), dimension(:), allocatable`
- **Defined in source**: `climate_module.f90:258`

## Subroutines Defined
(No subroutines detected.)

## Functions Defined
(No functions detected.)

## Used By Source Routines

```dataview
LIST file.link
WHERE type = "source" AND contains(module, this.module_name)
```

<!-- USER-NOTES-START -->
## Notes
Use this section for type and variable meanings, units, and allowed values. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
