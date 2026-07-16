---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: swift_output.f90
note_file: swift_output.f90
subroutine: swift_output
module:
  - hydrograph_module
  - hru_module
  - soil_module
  - output_landscape_module
  - reservoir_data_module
  - maximum_data_module
  - climate_module
  - aquifer_module
  - input_file_module
  - sd_channel_module
  - time_module
  - recall_module
calls:
  - system
  - copy_file
  - hyd_convert_mass_to_conc
reads: []
writes:
  - SWIFT/file_cio.swf
  - SWIFT/precip.swf
  - SWIFT/hru_dat.swf
  - SWIFT/hru_exco.swf
  - SWIFT/hru_wet.swf
  - SWIFT/chan_dat.swf
  - SWIFT/chan_dr.swf
  - SWIFT/aqu_dr.swf
  - SWIFT/res_dat.swf
  - SWIFT/res_dr.swf
  - SWIFT/recall.swf
  - SWIFT/" // trim(adjustl(recall_db(irec
  - SWIFT/object_prt.swf
purpose: ""
---

# swift_output

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `swift_output.f90`
- **Modules used**: [[hydrograph_module.f90]], [[hru_module.f90]], [[soil_module.f90]], [[output_landscape_module.f90]], [[reservoir_data_module.f90]], [[maximum_data_module.f90]], [[climate_module.f90]], [[aquifer_module.f90]], [[input_file_module.f90]], [[sd_channel_module.f90]], [[time_module.f90]], [[recall_module.f90]]
- **Subroutine calls**: 3 | **Files read**: 0 | **Files written**: 13

## Call Relationships
**This routine calls:**

- `system`
- [[copy_file.f90]]
- `hyd_convert_mass_to_conc`

**Called by** (live Dataview back-query):

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## File I/O
- **Writes**: `SWIFT/file_cio.swf`, `SWIFT/precip.swf`, `SWIFT/hru_dat.swf`, `SWIFT/hru_exco.swf`, `SWIFT/hru_wet.swf`, `SWIFT/chan_dat.swf`, `SWIFT/chan_dr.swf`, `SWIFT/aqu_dr.swf`, `SWIFT/res_dat.swf`, `SWIFT/res_dr.swf`, `SWIFT/recall.swf`, `SWIFT/" // trim(adjustl(recall_db(irec`, `SWIFT/object_prt.swf`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
