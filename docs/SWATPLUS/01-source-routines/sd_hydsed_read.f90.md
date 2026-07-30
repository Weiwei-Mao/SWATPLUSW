---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: sd_hydsed_read.f90
note_file: sd_hydsed_read.f90
subroutine: sd_hydsed_read
module:
  - input_file_module
  - sd_channel_module
  - channel_velocity_module
  - maximum_data_module
  - hydrograph_module
  - time_module
calls: []
uses_variables:
  - input_file_module.f90#in_cha
  - maximum_data_module.f90#db_mx
  - sd_channel_module.f90#flo_dep
  - sd_channel_module.f90#hyd_rad
  - sd_channel_module.f90#maxint
  - sd_channel_module.f90#sd_chd
  - sd_channel_module.f90#sd_chd1
  - sd_channel_module.f90#timeint
  - sd_channel_module.f90#trav_time
  - time_module.f90#time
input_variables:
  - sd_channel_module.f90#sd_chd
  - sd_channel_module.f90#sd_chd1
reads:
  - in_cha%hyd_sed
  - sed_nut.cha
writes: []
purpose: ""
---

# sd_hydsed_read

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `sd_hydsed_read.f90`
- **Modules used**:
  - [[input_file_module.f90]]
  - [[sd_channel_module.f90]]
  - [[channel_velocity_module.f90]]
  - [[maximum_data_module.f90]]
  - [[hydrograph_module.f90]]
  - [[time_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 2 | **Files written**: 0

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
- [[input_file_module.f90#in_cha]] - `input_cha`
- [[maximum_data_module.f90#db_mx]] - `data_files_max_elements`
- [[sd_channel_module.f90#flo_dep]] - `real, dimension(:), allocatable`
- [[sd_channel_module.f90#hyd_rad]] - `real, dimension(:), allocatable`
- [[sd_channel_module.f90#maxint]] - `integer`
- [[sd_channel_module.f90#sd_chd]] - `swatdeg_hydsed_data`
- [[sd_channel_module.f90#sd_chd1]] - `swatdeg_sednut_data`
- [[sd_channel_module.f90#timeint]] - `real, dimension(:), allocatable`
- [[sd_channel_module.f90#trav_time]] - `real, dimension(:), allocatable`
- [[time_module.f90#time]] - `time_current`

**Populated by file reads:**

- [[sd_channel_module.f90#sd_chd]]
- [[sd_channel_module.f90#sd_chd1]]

## File I/O
- **Reads**:
  - [[hyd-sed-lte.cha]]
  - [[sed_nut.cha]]

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.

- From [[input_file_module.f90#in_cha]] %hyd_sed, read [[hyd-sed-lte.cha]]
- Get [[sd_channel_module.f90#sd_chd]]
	- order
	- channel width
	- channel depth
	- channel slope
	- channel length
	- channel manning's n
	- channel bottom conductivity
	- bank erosion exponent
	- channel cover factor
	- sinuousity
	- critical velocity coefficient
	- channel median sediment size
	- clay percent of bank and bed
	- carbon percent of bank anbd bed
	- dry bulk density
	- channel side slope
	- bank full flow rate
	- flood plain slope
	- flood plain manning's n
	- nitrogen concentration in channel bank
	- phosphorus concentration in channel bank
	- fraction of p in bank that is bioavailable
- Check file [[sed_nut.cha]] exist or not. out of [[file.cio]]
- End
<!-- USER-NOTES-END -->
