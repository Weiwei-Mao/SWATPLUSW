---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: salt_roadsalt_read.f90
note_file: salt_roadsalt_read.f90
subroutine: salt_roadsalt_read
module:
  - basin_module
  - input_file_module
  - climate_module
  - time_module
  - maximum_data_module
  - constituent_mass_module
calls: []
uses_variables:
  - climate_module.f90#atmodep_cont
  - climate_module.f90#pcp
  - climate_module.f90#rdapp_salt
  - climate_module.f90#tmp
  - constituent_mass_module.f90#cs_db
  - time_module.f90#time
input_variables:
  - climate_module.f90#rdapp_salt
reads:
  - salt_road
writes: []
purpose: ""
---

# salt_roadsalt_read

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `salt_roadsalt_read.f90`
- **Modules used**:
  - [[basin_module.f90]]
  - [[input_file_module.f90]]
  - [[climate_module.f90]]
  - [[time_module.f90]]
  - [[maximum_data_module.f90]]
  - [[constituent_mass_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 1 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by:**

- [[proc_read.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[climate_module.f90#atmodep_cont]] - `atmospheric_deposition_control`
- [[climate_module.f90#pcp]] - `climate_measured_data`
- [[climate_module.f90#rdapp_salt]] - `object_road_salt`
- [[climate_module.f90#tmp]] - `climate_measured_data`
- [[constituent_mass_module.f90#cs_db]] - `constituents`
- [[time_module.f90#time]] - `time_current`

**Populated by file reads:**

- [[climate_module.f90#rdapp_salt]]

## File I/O
- **Reads**:
  - `salt_road` _(variable; see [[file.cio]])_

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
