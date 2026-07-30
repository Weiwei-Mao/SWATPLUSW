---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: soil_nutcarb_init.f90
note_file: soil_nutcarb_init.f90
subroutine: soil_nutcarb_init
module:
  - hru_module
  - soil_module
  - soil_data_module
  - basin_module
  - organic_mineral_mass_module
  - carbon_module
  - tillage_data_module
calls: []
uses_variables:
  - basin_module.f90#bsn_cc
  - carbon_module.f90#org_frac
  - hru_module.f90#hru
  - hru_module.f90#ihru
  - hru_module.f90#isol
  - hru_module.f90#sol_plt_ini
  - organic_mineral_mass_module.f90#soil1
  - soil_data_module.f90#solt_db
  - soil_module.f90#soil
  - tillage_data_module.f90#bmix_depth
  - tillage_data_module.f90#bmix_eff
input_variables: []
reads: []
writes: []
purpose: "this subroutine initializes soil chemical properties; and intial soil layer bmix efficiency"
---

# soil_nutcarb_init

> [!info] Summary
> this subroutine initializes soil chemical properties; and intial soil layer bmix efficiency

## Basic Information
- **Type**: `subroutine`
- **Source file**: `soil_nutcarb_init.f90`
- **Modules used**:
  - [[hru_module.f90]]
  - [[soil_module.f90]]
  - [[soil_data_module.f90]]
  - [[basin_module.f90]]
  - [[organic_mineral_mass_module.f90]]
  - [[carbon_module.f90]]
  - [[tillage_data_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 0 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by:**

- [[main.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[basin_module.f90#bsn_cc]] - `basin_control_codes`
- [[carbon_module.f90#org_frac]] - `organic_fractions`
- [[hru_module.f90#hru]] - `hydrologic_response_unit`
- [[hru_module.f90#ihru]] - `integer`
- [[hru_module.f90#isol]] - `integer`
- [[hru_module.f90#sol_plt_ini]] - `soil_plant_initialize`
- [[organic_mineral_mass_module.f90#soil1]] - `soil_profile_mass`
- [[soil_data_module.f90#solt_db]] - `soiltest_db`
- [[soil_module.f90#soil]] - `soil_profile`
- [[tillage_data_module.f90#bmix_depth]] - `real`
- [[tillage_data_module.f90#bmix_eff]] - `real`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.

- Line 33, check isol is exist
- Line 35, nlay, layers of isol
- Line 38, isol_pl, pointer in [[soil_plant.ini]]
- Line 39, isolt, pointer in [[nutrients.sol]]

- Line 41-47, set carbon concentration to each layer. Note a first layer of 10 mm is added.
- Line 49-110, iteration based on layer
	- Line 53-54, unit transfer constant, from input mg/kg -> kg/ha
	- Line 57, depth fraction parameter. More deeper, nutrient concentration is less,
		- $dep\_frac=e^{-exp_{co}*depth}$
		- exp_co, parameter in [[nutrients.sol]], depth, parameter in [[soils.sol]], depth from ground surface to the bottom of the layer
	- if no3 concentration is > 1e-9,
		- no3 = nitrate * dep_frac, nutrient is parameter in [[nutrients.sol]], mineral n pool dimensioned by layer
	- Else:
		- no3 = 7 * dep_frac, mineral n pool dimensioned by layer
	- Line 63, unit transfer
	- All the rest are P settings
- Line 112-230, iteration based on layer, organic pools
	- Line 119, organic matter = carbon / 0.58
	- Line 120, carbon = soil mass * carbon concentration, based on the value get from Line 41-47
	- Line 123, organic n = organic c / 10
	- Line 124, organic p = organic c / 100
	- cswat method
		- cswat = 0, original swat model
			- fraction of soil humus that is active = 0.02
			- **active humus pool**
				- humus organic matter = 0.02 * line 119 organic matter
				- humus organic c          = 0.02 * line 120 organic c
				- humus organic n = humus organic c / C:N ratio (default 10)
				- humus organic p = humus organic c / C:P ratio (default 80)
			- **stable humus pool**
				- stable humus organic matter = organic matter - humus organic matter
				- stable humus organic c          = organic c - humus organic c
				- stable humus n = stable c / C:N
				- stable humus p = stable c / C:P
		- cswat = 2, CENTURY method
			- frac_seq, fraction of total carbon that is sequestered carbon when initializing sequestered pools, defined in input file [[carbon.bsn]]
			- total organic pools
				- sequestered fraction
					- passive humus + slow humus + microbial biomass
				- non-sequestered fraction
					- metabolic litter + structural litter (lignin part + non-lignin part)
			- **passive humus pool**
				- hp organic matter = total organic matter * frac_hum_passive * frac_seq
				- hp c = total organic c * frac_hum_passive * frac_seq
				- hp n = hp c / 10
				- hp p = hp c / 100
			- **slow humus pool**
				- default method
					- hs organic matter = total organic matter * frac_hum_slow * frac_seq
					- hs c = total organic c * frac_hum_slow * frac_seq
					- hs n = hs c / 10
					- hs p = hs c / 100
				- Another method, Mathers approach
					- calculate mathers_frac
					- hs c = total organic c * frac_seq * mathers_frac
					- hs m = hs c / 0.58
					- hs n = hs c / 10
					- hs p = hs c / 100
			- **microbial pool**
				- microb organic matter = total organic matter * frac_hum_microb * frac_seq
				- microb c = total organic c * frac_hum_microb * frac_seq
				- microb n = microb c / 10
				- microb p = microb c / 100
			- **metabolic residue pool**
				- meta organic matter = total organic matter * 0.85 * frac_not_seq
				- meta c = total organic c * 0.85 * frac_not_seq
				- meta n = meta c / 10
				- meta p = meta c / 100
			- **structural residue pool**
				- str organic matter = total organic matter * 0.15 * frac_not_seq
				- str c = total organic c * 0.15 * frac_not_seq
				- str n = str c / 10
				- str p = str c / 100
			- **lignin residue pool**
				- lig organic matter =0.8 * str organic matter
				- lig c = 0.8 * str c
				- lig n = 0.2 * str n
				- lig p = 0.02 * str p
			- **non-lignin residue pool**
				-  str - lig
	- Calculate init_bmix for each layer
- End

<!-- USER-NOTES-END -->
