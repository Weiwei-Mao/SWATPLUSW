---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: soil_carbvar_write_legacy.f90
note_file: soil_carbvar_write_legacy.f90
subroutine: soil_carbvar_write_legacy
module:
  - basin_module
  - carbon_module
  - hydrograph_module
  - organic_mineral_mass_module
  - calibration_data_module
  - soil_module
calls: []
reads: []
writes: []
purpose: "this subroutine writes soil carbon output."
---

# soil_carbvar_write_legacy

> [!info] Summary
> this subroutine writes soil carbon output.

## Basic Information
- **Type**: `subroutine`
- **Source file**: `soil_carbvar_write_legacy.f90`
- **Modules used**: [[basin_module.f90]], [[carbon_module.f90]], [[hydrograph_module.f90]], [[organic_mineral_mass_module.f90]], [[calibration_data_module.f90]], [[soil_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 0 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by** (live Dataview back-query):

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
