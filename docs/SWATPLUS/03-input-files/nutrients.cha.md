---
type: input
tags:
  - swat/input
  - swat/auxiliary-input
file: nutrients.cha
ext: cha
cio_field: []
read_by:
  - ch_read_nut.f90
purpose: ""
---

# nutrients.cha

> [!info] Input File
> Referenced directly by source code or by a default file-name constant outside the main `file.cio` list.

## Overview
- **Declared in `file.cio` field**: not listed directly; referenced by source code or a default file-name constant.
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[ch_read_nut.f90]]

## File Structure
- [[ch_read_nut.f90]] source line 34: reads `titldum`
- [[ch_read_nut.f90]] source line 36: reads `header`
- [[ch_read_nut.f90]] source line 39: reads `titldum`
- [[ch_read_nut.f90]] source line 48: reads `titldum`
- [[ch_read_nut.f90]] source line 50: reads `header`
- [[ch_read_nut.f90]] source line 54: reads `titldum`
- [[ch_read_nut.f90]] source line 57: reads `ch_nut(ich)`

## Parameters
| Parameter | Type | Units | Meaning | Source | Reader line |
|---|---|---|---|---|---:|
| `ch_nut%name` | `character(len=16)` |  |  | [[channel_data_module.f90#ch_nut]] | [[ch_read_nut.f90]]:57 |
| `ch_nut%onco` | `real` | ppm | channel organic n concentration | [[channel_data_module.f90#ch_nut]] | [[ch_read_nut.f90]]:57 |
| `ch_nut%opco` | `real` | ppm | channel organic p concentration | [[channel_data_module.f90#ch_nut]] | [[ch_read_nut.f90]]:57 |
| `ch_nut%rs1` | `real` | m/day or m/hr | local algal settling rate in reach at 20 deg C | [[channel_data_module.f90#ch_nut]] | [[ch_read_nut.f90]]:57 |
| `ch_nut%rs2` | `real` | (mg disP-P)/ | benthos source rate for dissolved phos ((m**2)*day)\|in reach at 20 deg C or (mg disP-P)/((m**2)*hr)\| | [[channel_data_module.f90#ch_nut]] | [[ch_read_nut.f90]]:57 |
| `ch_nut%rs3` | `real` | (mg NH4-N)/ | benthos source rate for ammonia nit in ((m**2)*day)\|reach at 20 deg C or (mg NH4-N)/((m**2)*hr)\| | [[channel_data_module.f90#ch_nut]] | [[ch_read_nut.f90]]:57 |
| `ch_nut%rs4` | `real` | 1/day or 1/hr | rate coeff for organic nitrogen settling in reach at 20 deg C | [[channel_data_module.f90#ch_nut]] | [[ch_read_nut.f90]]:57 |
| `ch_nut%rs5` | `real` | 1/day or 1/hr | org phos settling rate in reach at 20 deg C | [[channel_data_module.f90#ch_nut]] | [[ch_read_nut.f90]]:57 |
| `ch_nut%rs6` | `real` | 1/day | rate coeff for settling of arbitrary non-conservative constituent in reach | [[channel_data_module.f90#ch_nut]] | [[ch_read_nut.f90]]:57 |
| `ch_nut%rs7` | `real` | (mg ANC)/ | benthal source rate for arbitrary ((m**2)*day)\|non-conservative constituent in reach | [[channel_data_module.f90#ch_nut]] | [[ch_read_nut.f90]]:57 |
| `ch_nut%rk1` | `real` | 1/day or 1/hr | CBOD deoxygenation rate coeff in reach at 20 deg C | [[channel_data_module.f90#ch_nut]] | [[ch_read_nut.f90]]:57 |
| `ch_nut%rk2` | `real` | 1/day or 1/hr | reaeration rate in accordance with Fickian diffusion in reach at 20 deg C | [[channel_data_module.f90#ch_nut]] | [[ch_read_nut.f90]]:57 |
| `ch_nut%rk3` | `real` | 1/day or 1/hr | rate of loss of CBOD due to settling in reach at 20 deg C | [[channel_data_module.f90#ch_nut]] | [[ch_read_nut.f90]]:57 |
| `ch_nut%rk4` | `real` | mg O2/ | sed oxygen demand rate in reach ((m**2)*day)\|at 20 deg C or mg O2/((m**2)*hr) | [[channel_data_module.f90#ch_nut]] | [[ch_read_nut.f90]]:57 |
| `ch_nut%rk5` | `real` | 1/day | coliform die-off rate in reach | [[channel_data_module.f90#ch_nut]] | [[ch_read_nut.f90]]:57 |
| `ch_nut%rk6` | `real` | 1/day | decay rate for arbitrary non-conservative constituent in reach | [[channel_data_module.f90#ch_nut]] | [[ch_read_nut.f90]]:57 |
| `ch_nut%bc1` | `real` | 1/hr | rate constant for biological oxidation of NH3 to NO2 in reach at 20 deg C | [[channel_data_module.f90#ch_nut]] | [[ch_read_nut.f90]]:57 |
| `ch_nut%bc2` | `real` | 1/hr | rate constant for biological oxidation of NO2 to NO3 in reach at 20 deg C | [[channel_data_module.f90#ch_nut]] | [[ch_read_nut.f90]]:57 |
| `ch_nut%bc3` | `real` | 1/hr | rate constant for hydrolysis of organic N to ammonia in reach at 20 deg C | [[channel_data_module.f90#ch_nut]] | [[ch_read_nut.f90]]:57 |
| `ch_nut%bc4` | `real` | 1/hr | rate constant for the decay of organic P to dissolved P in reach at 20 deg C | [[channel_data_module.f90#ch_nut]] | [[ch_read_nut.f90]]:57 |
| `ch_nut%lao` | `real` | NA | Qual2E light averaging option. Qual2E defines four light averaging options. The only option currently available in SWAT is #2. | [[channel_data_module.f90#ch_nut]] | [[ch_read_nut.f90]]:57 |
| `ch_nut%igropt` | `integer` | none | Qual2E option for calculating the local specific growth rate of algae 1: multiplicative: u = mumax * fll * fnn * fpp 2: limiting nutrient: u = mumax * fll * Min(fnn, fpp) 3: harmonic mean: u = mumax * fll * 2. / ((1/fnn)+(1/fpp)) | [[channel_data_module.f90#ch_nut]] | [[ch_read_nut.f90]]:57 |
| `ch_nut%ai0` | `real` | ug chla/mg alg | ratio of chlorophyll-a to algal biomass | [[channel_data_module.f90#ch_nut]] | [[ch_read_nut.f90]]:57 |
| `ch_nut%ai1` | `real` | mg N/mg alg | fraction of algal biomass that is nitrogen | [[channel_data_module.f90#ch_nut]] | [[ch_read_nut.f90]]:57 |
| `ch_nut%ai2` | `real` | mg P/mg alg | fraction of algal biomass that is phosphorus | [[channel_data_module.f90#ch_nut]] | [[ch_read_nut.f90]]:57 |
| `ch_nut%ai3` | `real` | mg O2/mg alg | the rate of oxygen production per unit of algal photosynthesis | [[channel_data_module.f90#ch_nut]] | [[ch_read_nut.f90]]:57 |
| `ch_nut%ai4` | `real` | mg O2/mg alg | the rate of oxygen uptake per unit of algae respiration | [[channel_data_module.f90#ch_nut]] | [[ch_read_nut.f90]]:57 |
| `ch_nut%ai5` | `real` | mg O2/mg N | the rate of oxygen uptake per unit of NH3 nitrogen oxidation | [[channel_data_module.f90#ch_nut]] | [[ch_read_nut.f90]]:57 |
| `ch_nut%ai6` | `real` | mg O2/mg N | the rate of oxygen uptake per unit of NO2 nitrogen oxidation | [[channel_data_module.f90#ch_nut]] | [[ch_read_nut.f90]]:57 |
| `ch_nut%mumax` | `real` | 1/hr | maximum specific algal growth rate at 20 deg C | [[channel_data_module.f90#ch_nut]] | [[ch_read_nut.f90]]:57 |
| `ch_nut%rhoq` | `real` | 1/day or 1/hr | algal respiration rate | [[channel_data_module.f90#ch_nut]] | [[ch_read_nut.f90]]:57 |
| `ch_nut%tfact` | `real` | none | fraction of solar radiation computed in the temperature heat balance that is photosynthetically active | [[channel_data_module.f90#ch_nut]] | [[ch_read_nut.f90]]:57 |
| `ch_nut%k_l` | `real` | MJ/(m2*hr) | half-saturation coefficient for light | [[channel_data_module.f90#ch_nut]] | [[ch_read_nut.f90]]:57 |
| `ch_nut%k_n` | `real` | mg N/L | michaelis-menton half-saturation constant for nitrogen | [[channel_data_module.f90#ch_nut]] | [[ch_read_nut.f90]]:57 |
| `ch_nut%k_p` | `real` | mg P/L | michaelis-menton half saturation constant for phosphorus | [[channel_data_module.f90#ch_nut]] | [[ch_read_nut.f90]]:57 |
| `ch_nut%lambda0` | `real` | 1/m | non-algal portion of the light extinction coefficient | [[channel_data_module.f90#ch_nut]] | [[ch_read_nut.f90]]:57 |
| `ch_nut%lambda1` | `real` | 1/(m*ug chla/L) | linear algal self-shading coefficient | [[channel_data_module.f90#ch_nut]] | [[ch_read_nut.f90]]:57 |
| `ch_nut%lambda2` | `real` | (1/m)(ug chla/L)**(-2/3) | nonlinear algal self-shading coefficient | [[channel_data_module.f90#ch_nut]] | [[ch_read_nut.f90]]:57 |
| `ch_nut%p_n` | `real` | none | algal preference factor for ammonia | [[channel_data_module.f90#ch_nut]] | [[ch_read_nut.f90]]:57 |
