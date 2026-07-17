---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: proc_cha.f90
note_file: proc_cha.f90
subroutine: proc_cha
module:
  - hydrograph_module
calls:
  - ch_read_init
  - ch_read_init_cs
  - sd_hydsed_read
  - ch_read_hyd
  - ch_read_sed
  - ch_read_nut
  - ch_read
  - sd_channel_read
  - sd_hydsed_init
  - aqu2d_init
  - ch_ttcoef
  - ch_initial
  - overbank_read
  - sd_channel_surf_link
  - time_conc_init
uses_variables:
  - hydrograph_module.f90#ich
  - hydrograph_module.f90#ob
  - hydrograph_module.f90#sp_ob
  - hydrograph_module.f90#sp_ob1
input_variables: []
reads: []
writes: []
purpose: ""
---

# proc_cha

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `proc_cha.f90`
- **Modules used**:
  - [[hydrograph_module.f90]]
- **Subroutine calls**: 15 | **Files read**: 0 | **Files written**: 0

## Call Relationships
**This routine calls:**

- [[ch_read_init.f90]]
- [[ch_read_init_cs.f90]]
- [[sd_hydsed_read.f90]]
- [[ch_read_hyd.f90]]
- [[ch_read_sed.f90]]
- [[ch_read_nut.f90]]
- [[ch_read.f90]]
- [[sd_channel_read.f90]]
- [[sd_hydsed_init.f90]]
- [[aqu2d_init.f90]]
- [[ch_ttcoef.f90]]
- [[ch_initial.f90]]
- [[overbank_read.f90]]
- [[sd_channel_surf_link.f90]]
- [[time_conc_init.f90]]

**Called by:**

- [[main.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[hydrograph_module.f90#ich]] - `integer`
- [[hydrograph_module.f90#ob]] - `object_connectivity`
- [[hydrograph_module.f90#sp_ob]] - `spatial_objects`
- [[hydrograph_module.f90#sp_ob1]] - `spatial_objects`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.

- Line 15: call [[ch_read_init.f90]], Reads channel initialization names/settings from [[initial.cha]]
	- org_min, pest, path, hmet, salt, description
- Line 16: call [[ch_read_init_cs.f90]], Reads optional channel salt/constituent initialization from [[initial.cha_cs]], out of [[file.cio]]
- Line 18: call [[sd_hydsed_read.f90]],   Reads SWAT-DEG hydrology/sediment control settings, [[hyd-sed-lte.cha]]
- Line 19: call [[ch_read_hyd.f90]], Reads regular-channel hydraulic parameters
- Line 20: call [[ch_read_sed.f90]], Reads regular-channel sediment parameters
- Line 21: call [[ch_read_nut.f90]], Reads regular-channel nutrient/water-quality parameters, [[nutrient.cha]]
- Line 22: call [[ch_read.f90]],        Read regular-channel definition
- Line 23: call [[sd_channel_read.f90]], Reads SWAT-DEG channel definition
- Line 24: call [[sd_hydsed_init.f90]]
	- [[object.cnt]] defines number of SWAT-DEG channels in column `lcha`; this becomes `sp_ob%chandeg`
	- [[file.cio]] points the model to the channel files: `chandeg.con`, `initial.cha`, `nutrients.cha`, `channel-lte.cha`, `hyd-sed-lte.cha`.
	- [[chandeg.con]] defines each actual SWAT-DEG channel object. Column 8, `lcha`, is the property/database pointer; it is read into `ob(i)%props`.
	- [[channel-lte.cha]] is not the actual object list. It is the SWAT-DEG channel database/crosswalk. [[sd_channel_read.f90]] reads it into `sd_dat(:)` and resolves text names to integer pointers.
	- [[hyd-sed-lte.cha]] contains hydraulic/sediment geometry records, read into `sd_chd(:)` by [[sd_hydsed_read.f90]].
	- [[initial.cha]] defines initial channel condition records, read into `ch_init(:)` and linked through `sd_init(:)`.
	- [[nutrients.cha]] defines channel nutrient/water-quality coefficients, read into `ch_nut(:)`.
	- [[sd_hydsed_init.f90]] copies the selected database records into actual runtime channel state `sd_ch(ich)`, builds rating curves `ch_rcurv(ich)`, Muskingum coefficients, and initial channel/floodplain storage.
	- Later [[command.f90]] calls [[sd_channel_control3.f90]] for daily/subdaily channel calculation.

| object                           | scope              | holds                                                                                        | mutability                                           |
| -------------------------------- | ------------------ | -------------------------------------------------------------------------------------------- | ---------------------------------------------------- |
| `sd_dat`                         | database crosswalk | records from `channel-lte.cha`; names plus resolved pointers to init/hyd/nut                 | static after read                                    |
| `sd_chd`                         | database           | raw hydraulic/sediment geometry from `hyd-sed-lte.cha`                                       | static input                                         |
| `sd_chd1`                        | database/default   | optional sediment-nutrient routing params from `sed_nut.cha`; default if file missing        | static/default                                       |
| `ch_init`                        | database           | raw initial-condition names from `initial.cha`                                               | static input                                         |
| `sd_init`                        | database pointers  | resolved initial water/pest/path/salt/cs pointers                                            | static after read                                    |
| `ch_nut`                         | database           | nutrient and water-quality coefficients from `nutrients.cha`                                 | static after read                                    |
| `ob(i)`                          | actual object      | channel connectivity, `props`, incoming/outgoing hydrographs                                 | connectivity static; hydrographs dynamic             |
| `sd_ch(ich)`                     | per channel        | actual initialized SWAT-DEG channel parameters: width, depth, slope, length, Manning n, etc. | mostly dynamic; morphology/calibration can change it |
| `ch_rcurv(ich)`                  | per channel        | rating curve and routing state                                                               | initialized, then updated in routing                 |
| `ch_stor`, `fp_stor`, `tot_stor` | per channel        | channel/floodplain/total water and OM nutrient storage                                       | dynamic                                              |
| `ch_water`, `ch_benthic`         | per channel        | pesticide/pathogen/salt/constituent masses if active                                         | dynamic                                              |
| `chsd_d/m/y/a`                   | output             | SWAT-DEG channel flow/sediment/morphology output                                             | dynamic accumulators                                 |
| `ch_sed_bud_d/m/y/a`             | output budget      | channel sediment, N, P budget terms                                                          | dynamic accumulators                                 |






<!-- USER-NOTES-END -->
