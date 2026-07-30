---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: ch_read_nut.f90
note_file: ch_read_nut.f90
subroutine: ch_read_nut
module:
  - input_file_module
  - basin_module
  - time_module
  - maximum_data_module
  - channel_data_module
calls: []
uses_variables:
  - channel_data_module.f90#ch_nut
  - input_file_module.f90#in_cha
  - maximum_data_module.f90#db_mx
  - time_module.f90#time
input_variables:
  - channel_data_module.f90#ch_nut
reads:
  - in_cha%nut
writes: []
purpose: "this subroutine reads data from the lake water quality input file (.lwq).; This file contains data related to initial pesticide and nutrient levels; in the lake/reservoir and transformation processes occurring within the"
---

# ch_read_nut

> [!info] Summary
> this subroutine reads data from the lake water quality input file (.lwq).; This file contains data related to initial pesticide and nutrient levels; in the lake/reservoir and transformation processes occurring within the

## Basic Information
- **Type**: `subroutine`
- **Source file**: `ch_read_nut.f90`
- **Modules used**:
  - [[input_file_module.f90]]
  - [[basin_module.f90]]
  - [[time_module.f90]]
  - [[maximum_data_module.f90]]
  - [[channel_data_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 1 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by:**

- [[proc_cha.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[channel_data_module.f90#ch_nut]] - `channel_nut_data`
- [[input_file_module.f90#in_cha]] - `input_cha`
- [[maximum_data_module.f90#db_mx]] - `data_files_max_elements`
- [[time_module.f90#time]] - `time_current`

**Populated by file reads:**

- [[channel_data_module.f90#ch_nut]]

## File I/O
- **Reads**:
  - [[nutrients.cha]]

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.

- From [[input_file_module.f90#in_cha]] %nut, read [[nutrient.cha]]
- Define at [[channel_data_module.f90#ch_nut]], 
	- onco, channel organic n concentration
	- opco, channel organic p concentration
	- rs1, local algal settling rate in reach at 20 deg C
	- rs2, benthos source rate for dissolved phos in reach at 20 deg C, [mg disP-P/(m2 hour)]
	- rs3, benthos source rate for ammonia nitro in reach at 20 deg C, [mg NH4-N/(m2 hour)]
	- rs4, rate coefficient for organic nitrogen settling in reach at 20 deg C
	- rs5, organic P settling rate in reach at 20 deg C
	- rs6, rate coefficient for settling of arbitrary non-conservative constituent in reach
	- rs7, benthal source rate for arbitrary non-conservative constituent in reach
	- rk1, CBOD deoxygenation rate coefficient in reach at 20 deg C
	- rk2, reaeration rate in accordance with Fickian diffusion in reach at 20 deg C
	- rk3, rate of loss of CBOD due to settling in reach at 20 deg C
	- rk4, sed oxygen demand rate in reach at 20 deg C or mg O2/(m2 hour)
	- rk5, coliform die-off rate in reach
	- rk6, decay rate for arbitrary non-conservative constituent in reach
	- bc1, rate constant for biological oxidation of nh3 to no2 in reach at 20 deg C
	- bc2, rate constant for biological oxidation of no2 to no3 in reach at 20 deg C
	- bc3, rate constant for hydrolysis of organic N to ammonia in reach at 20 deg C
	- bc4, rate constant for the decay of organic P to dissolved P in reach at 20 deg C
	- lao, Qual2E light average option, only one is available in swat
	- igropt, Qual2E option for calculating the local specific growth rate of algae
	- ai0, ratio of chlorophyll-a to algal biomass
	- ai1, fraction of algal biomass that is nitrogen
	- ai2, fraction of algal biomass that is phosphorus
	- ai3, the rate of oxygen production per unit of algal photosynthesis
	- ai4, the rate of oxygen  uptake per unit of algae respiration
	- ai5, the ratio of oxygen uptake per unit of nh3 oxidation
	- ai6, the ratio of oxygen uptake per unit of n02 oxidation
	- mumax, maximum specific algal growth rate at 20 deg C
	- rhoq, algal respiration rate
	- tfact, fraction of solar radiation computed in the T heat balance that is photosynthetically active
	- k_l, half-saturation coefficient for light
	- k_n, michaelis-menton half-saturation constant for nitrogen
	- k_p,michaelis-menton half-saturation constant for nitrogen
	- lambda0, non-algal portion of the light extinction coefficient
	- lambda1, linear algal self-shading coefficient
	- lambda2, nonlinear algal self-shading coefficient
	- p_n, algal preference factor for ammonia\
- Line 62-80, set default parameters if <= 0
- Line 85-89, change mumax, rhoq, from day time step, to 
- To end, set default parameter values.

<!-- USER-NOTES-END -->
