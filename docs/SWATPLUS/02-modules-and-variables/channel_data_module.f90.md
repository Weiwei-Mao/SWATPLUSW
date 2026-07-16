---
type: module
tags:
  - swat/module
  - swat/to-read
file: channel_data_module.f90
note_file: channel_data_module.f90
module_name: channel_data_module
defines_types:
  - routing_nut_data
  - channel_data_char_input
  - channel_init_datafiles
  - channel_init_datafiles_cs
  - channel_data
  - channel_hyd_data
  - channel_sed_data
  - channel_nut_data
  - channel_temperature_data
  - water_temperature_data
defines_vars:
  - rte_nut
  - ch_dat_c
  - ch_init
  - ch_init_cs
  - ch_dat
  - ch_hyd
  - ch_sed
  - ch_nut
  - w_temp
defines_subroutines: []
defines_functions: []
defines_procedures: []
purpose: ""
---

# channel_data_module

> [!info] Module
> Defines derived types and module-level variables.

## Defined Types
### routing_nut_data

- **Defined in source**: `channel_data_module.f90:5`
- **Source note**: used for 2-stage ditch in chandeg and overland flow

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `name` | `character(len=16)` | 6 |  |
| `len_inc` | `real` | 7 | m \|segment length for reduction |
| `no3_slp` | `real` | 8 | (mgN/m2/h)/ppm \|slope of denitrification (y-axis) and inflow no3 (x-axis) |
| `no3_int` | `real` | 9 | mgN/m2/h \|intercept of denitrification rate equation |
| `no3_slp_ob` | `real` | 10 | (mgN/m2/h)/ppm \|slope of denitrification (y-axis) and inflow no3 (x-axis) |
| `no3_int_ob` | `real` | 11 | mgN/m2/h \|intercept of denitrification rate equation |
| `no3_slp_ub` | `real` | 12 | (mgN/m2/h)/ppm \|slope of denitrification (y-axis) and inflow no3 (x-axis) |
| `no3_int_ub` | `real` | 13 | mgN/m2/h \|intercept of denitrification rate equation |
| `turb_slp` | `real` | 14 | (del ppm/ppm) \|slope of turbidity reduction (y) and inflow turbidity (x) |
| `turb_int` | `real` | 15 | ppm \|intecept of turbidity reduction equation |
| `tss_slp` | `real` | 16 | (del ppm/ppm) \|slope of total suspended solids (y) and inflow turbidity (x) |
| `tss_int` | `real` | 17 | ppm \|intecept of tss reduction equation |
| `tp_slp` | `real` | 18 | (del ppm/ppm) \|slope of total P reduction (y) and turbidity reduction (x) |
| `tp_int` | `real` | 19 | ppm \|intecept of total P reduction equation |
| `srp_slp` | `real` | 20 | (del ppm/ppm) \|slope of soluble reactive P reduction (y) and total P reduction (x) |
| `srp_int` | `real` | 21 | ppm \|intecept of soluble reactive P reduction equation |
| `turb_tss_slp` | `real` | 22 | ppm \|slope of turbidity and total suspended solids (0.2-0.4) |
| `no3_min_conc` | `real` | 23 | ppm \|minimum no3 concentration |
| `tp_min_conc` | `real` | 24 | ppm \|minimum tp concentration |
| `tss_min_conc` | `real` | 25 | ppm \|minimum tss concentration |
| `srp_min_conc` | `real` | 26 | ppm \|minimum srp concentration |

### channel_data_char_input

- **Defined in source**: `channel_data_module.f90:30`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `name` | `character(len=16)` | 31 |  |
| `init` | `character(len=16)` | 32 | points to initial_cha |
| `hyd` | `character(len=16)` | 33 | points to hydrology.res for hydrology inputs |
| `sed` | `character(len=16)` | 34 | sediment inputs-points to sediment.res |
| `nut` | `character(len=16)` | 35 | nutrient inputs-points to nutrient.res |

### channel_init_datafiles

- **Defined in source**: `channel_data_module.f90:39`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `name` | `character(len=16)` | 40 |  |
| `org_min` | `character(len=16)` | 41 | points to initial organic-mineral input file |
| `pest` | `character(len=16)` | 42 | points to initial pesticide input file |
| `path` | `character(len=16)` | 43 | points to initial pathogen input file |
| `hmet` | `character(len=16)` | 44 | points to initial heavy metals input file |
| `salt` | `character(len=16)` | 45 | points to initial salt input file |

### channel_init_datafiles_cs

- **Defined in source**: `channel_data_module.f90:50`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `name` | `character(len=16)` | 51 |  |
| `pest` | `character(len=16)` | 52 | points to initial pesticide input file |
| `path` | `character(len=16)` | 53 | points to initial pathogen input file |
| `hmet` | `character(len=16)` | 54 | points to initial heavy metals input file |
| `salt` | `character(len=16)` | 55 | points to initial salt input file |
| `cs` | `character(len=16)` | 56 | points to initial constituent input file |

### channel_data

- **Defined in source**: `channel_data_module.f90:60`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `name` | `character(len=16)` | 61 |  |
| `init` | `integer` | 62 | initial data-points to initial.res |
| `hyd` | `integer` | 63 | points to hydrology.res for hydrology inputs |
| `sed` | `integer` | 64 | sediment inputs-points to sediment.res |
| `nut` | `integer` | 65 | nutrient inputs-points to nutrient.res |

### channel_hyd_data

- **Defined in source**: `channel_data_module.f90:69`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `name` | `character(len=16)` | 73 |  |
| `w` | `real` | 74 | m \|average width of main channel |
| `d` | `real` | 75 | m \|average depth of main channel |
| `s` | `real` | 76 | m/m \|average slope of main channel |
| `l` | `real` | 77 | km \|main channel length in subbasin |
| `n` | `real` | 78 | none \|Manning"s "n" value for the main channel |
| `k` | `real` | 79 | mm/hr \|effective hydraulic conductivity of main channel alluvium |
| `wdr` | `real` | 80 | m/m \|channel width to depth ratio |
| `alpha_bnk` | `real` | 81 | days \|alpha factor for bank storage recession curve |
| `side` | `real` | 82 | \|change in horizontal distance per unit |

### channel_sed_data

- **Defined in source**: `channel_data_module.f90:86`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `name` | `character(len=16)` | 87 |  |
| `eqn` | `integer` | 88 | \|sediment routine methods: 0 = original SWAT method 1 = Bagnold"seqn 2 = Kodatie 3 = Molinas WU 4 = Yang |
| `cov1` | `real` | 94 | none \|channel erodibility factor (0.0-1.0) |
| `cov2` | `real` | 95 | none \|channel cover factor (0.0-1.0) |
| `bnk_bd` | `real` | 96 | (g/cc) \|bulk density of channel bank sediment (1.1-1.9) |
| `bed_bd` | `real` | 97 | (g/cc) \|bulk density of channel bed sediment (1.1-1.9) |
| `bnk_kd` | `real` | 98 | \|erodibility of channel bank sediment by jet test |
| `bed_kd` | `real` | 99 | \|erodibility of channel bed sediment by jet test |
| `bnk_d50` | `real` | 100 | \|D50(median) particle size diameter of channel |
| `bed_d50` | `real` | 101 | \|D50(median) particle size diameter of channel |
| `tc_bnk` | `real` | 102 | N/m2 \|critical shear stress of channel bank |
| `tc_bed` | `real` | 103 | N/m2 \|critical shear stress of channel bed |
| `erod` | `real, dimension(12)` | 104 | \|value of 0.0 indicates a non-erosive channel while a value of 1.0 indicates no resistance to erosion |

### channel_nut_data

- **Defined in source**: `channel_data_module.f90:109`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `name` | `character(len=16)` | 110 |  |
| `onco` | `real` | 111 | ppm \|channel organic n concentration |
| `opco` | `real` | 112 | ppm \|channel organic p concentration |
| `rs1` | `real` | 113 | m/day or m/hr \|local algal settling rate in reach at 20 deg C |
| `rs2` | `real` | 114 | (mg disP-P)/ \|benthos source rate for dissolved phos ((m**2)*day)\|in reach at 20 deg C or (mg disP-P)/((m**2)*hr)\| |
| `rs3` | `real` | 116 | (mg NH4-N)/ \|benthos source rate for ammonia nit in ((m**2)*day)\|reach at 20 deg C or (mg NH4-N)/((m**2)*hr)\| |
| `rs4` | `real` | 118 | 1/day or 1/hr \|rate coeff for organic nitrogen settling in reach at 20 deg C |
| `rs5` | `real` | 119 | 1/day or 1/hr \|org phos settling rate in reach at 20 deg C |
| `rs6` | `real` | 120 | 1/day \|rate coeff for settling of arbitrary non-conservative constituent in reach |
| `rs7` | `real` | 121 | (mg ANC)/ \|benthal source rate for arbitrary ((m**2)*day)\|non-conservative constituent in reach |
| `rk1` | `real` | 122 | 1/day or 1/hr \|CBOD deoxygenation rate coeff in reach at 20 deg C |
| `rk2` | `real` | 123 | 1/day or 1/hr \|reaeration rate in accordance with Fickian diffusion in reach at 20 deg C |
| `rk3` | `real` | 124 | 1/day or 1/hr \|rate of loss of CBOD due to settling in reach at 20 deg C |
| `rk4` | `real` | 125 | mg O2/ \|sed oxygen demand rate in reach ((m**2)*day)\|at 20 deg C or mg O2/((m**2)*hr) |
| `rk5` | `real` | 126 | 1/day \|coliform die-off rate in reach |
| `rk6` | `real` | 127 | 1/day \|decay rate for arbitrary non-conservative constituent in reach |
| `bc1` | `real` | 128 | 1/hr \|rate constant for biological oxidation of NH3 to NO2 in reach at 20 deg C |
| `bc2` | `real` | 129 | 1/hr \|rate constant for biological oxidation of NO2 to NO3 in reach at 20 deg C |
| `bc3` | `real` | 130 | 1/hr \|rate constant for hydrolysis of organic N to ammonia in reach at 20 deg C |
| `bc4` | `real` | 131 | 1/hr \|rate constant for the decay of organic P to dissolved P in reach at 20 deg C |
| `lao` | `real` | 132 | NA \|Qual2E light averaging option. Qual2E defines four light averaging options. The only option currently available in SWAT is #2. |
| `igropt` | `integer` | 134 | none \|Qual2E option for calculating the local specific growth rate of algae 1: multiplicative: u = mumax * fll * fnn * fpp 2: limiting nutrient: u = mumax * fll * Min(fnn, fpp) 3: harmonic mean: u = mumax * fll * 2. / ((1/fnn)+(1/fpp)) |
| `ai0` | `real` | 138 | ug chla/mg alg \|ratio of chlorophyll-a to algal biomass |
| `ai1` | `real` | 139 | mg N/mg alg \|fraction of algal biomass that is nitrogen |
| `ai2` | `real` | 140 | mg P/mg alg \|fraction of algal biomass that is phosphorus |
| `ai3` | `real` | 141 | mg O2/mg alg \|the rate of oxygen production per unit of algal photosynthesis |
| `ai4` | `real` | 142 | mg O2/mg alg \|the rate of oxygen uptake per unit of algae respiration |
| `ai5` | `real` | 143 | mg O2/mg N \|the rate of oxygen uptake per unit of NH3 nitrogen oxidation |
| `ai6` | `real` | 144 | mg O2/mg N \|the rate of oxygen uptake per unit of NO2 nitrogen oxidation |
| `mumax` | `real` | 145 | 1/hr \|maximum specific algal growth rate at 20 deg C |
| `rhoq` | `real` | 146 | 1/day or 1/hr \|algal respiration rate |
| `tfact` | `real` | 147 | none \|fraction of solar radiation computed in the temperature heat balance that is photosynthetically active |
| `k_l` | `real` | 149 | MJ/(m2*hr) \|half-saturation coefficient for light |
| `k_n` | `real` | 150 | mg N/L \|michaelis-menton half-saturation constant for nitrogen |
| `k_p` | `real` | 151 | mg P/L \|michaelis-menton half saturation constant for phosphorus |
| `lambda0` | `real` | 152 | 1/m \|non-algal portion of the light extinction coefficient |
| `lambda1` | `real` | 153 | 1/(m*ug chla/L) \|linear algal self-shading coefficient |
| `lambda2` | `real` | 154 | (1/m)(ug chla/L)**(-2/3) \|nonlinear algal self-shading coefficient |
| `p_n` | `real` | 155 | none \|algal preference factor for ammonia |

### channel_temperature_data

- **Defined in source**: `channel_data_module.f90:159`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `name` | `character(len=16)` | 160 |  |
| `sno_mlt` | `real` | 161 | none \|coefficient influencing snowmelt temperature contributions |
| `gw` | `real` | 162 | none \|coefficient influencing groundwater temperature contributions |
| `sur_lat` | `real` | 163 | none \|coefficient influencing surface and lateral flow temperature contributions |
| `bulk_co` | `real` | 164 | 1/hour \|bulk coefficient of heat transfer |
| `air_lag` | `real` | 165 | days \|average air temperature lag |

### water_temperature_data

- **Defined in source**: `channel_data_module.f90:169`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `name` | `character(len=13)` | 170 |  |
| `sno_mlt` | `real` | 171 | none \|coefficient influencing snowmelt temperature contributions |
| `gw` | `real` | 172 | none \|coefficient influencing groundwater temperature contributions |
| `sur_lat` | `real` | 173 | none \|coefficient influencing surface and lateral flow temperature contributions |
| `sno_lag` | `real` | 174 | days \|average air temperature lag to snowmelt (1-3) |
| `gw_lag` | `real` | 175 | days \|average air temperature lag to gw flow (200-365) |
| `surf_lag` | `real` | 176 | days \|average air temperature lag to surface runoff (2-5) |
| `lat_lag` | `real` | 177 | days \|average air temperature lag to lateral flow (5-10) |
| `lat_lag_coef` | `real` | 178 | none \|lat air lag coefficient |
| `surf_lag_coef` | `real` | 179 | none \|surf air lag coefficient (used also for snow) |
| `gw_lag_coef` | `real` | 180 | none \|gw air lag coefficient |
| `hex_coef1` | `real` | 181 | none \|calibrate dew point |
| `hex_coef2` | `real` | 182 | none \|calibrate channel geometry |
| `sf_on` | `integer` | 183 | none \|shade factor file activation, 1= file, 0= take value from cal file |
| `ssff` | `real` | 184 | none \|ssff value default 0.5, range 0-1 |

## Variables Defined
### rte_nut

- **Type**: `routing_nut_data`
- **Defined in source**: `channel_data_module.f90:28`

### ch_dat_c

- **Type**: `channel_data_char_input`
- **Defined in source**: `channel_data_module.f90:37`

### ch_init

- **Type**: `channel_init_datafiles`
- **Defined in source**: `channel_data_module.f90:47`

### ch_init_cs

- **Type**: `channel_init_datafiles_cs`
- **Defined in source**: `channel_data_module.f90:58`

### ch_dat

- **Type**: `channel_data`
- **Defined in source**: `channel_data_module.f90:67`

### ch_hyd

- **Type**: `channel_hyd_data`
- **Defined in source**: `channel_data_module.f90:84`

### ch_sed

- **Type**: `channel_sed_data`
- **Defined in source**: `channel_data_module.f90:107`

### ch_nut

- **Type**: `channel_nut_data`
- **Defined in source**: `channel_data_module.f90:157`

### w_temp

- **Type**: `water_temperature_data`
- **Defined in source**: `channel_data_module.f90:186`

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
