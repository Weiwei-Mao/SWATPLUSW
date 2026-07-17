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
uses_variables:
  - climate_module.f90#wst
  - hru_module.f90#hru
  - hru_module.f90#ihru
  - hydrograph_module.f90#aqu
  - hydrograph_module.f90#dr
  - hydrograph_module.f90#exco
  - hydrograph_module.f90#hd_tot
  - hydrograph_module.f90#hru_swift_hdr
  - hydrograph_module.f90#ht5
  - hydrograph_module.f90#hz
  - hydrograph_module.f90#icmd
  - hydrograph_module.f90#iwst
  - hydrograph_module.f90#mobj_out
  - hydrograph_module.f90#ob
  - hydrograph_module.f90#ob_out
  - hydrograph_module.f90#rec_a
  - hydrograph_module.f90#res
  - hydrograph_module.f90#ru_def
  - hydrograph_module.f90#sp_ob
  - hydrograph_module.f90#sp_ob1
  - hydrograph_module.f90#wyld_rto
  - input_file_module.f90#in_con
  - input_file_module.f90#in_regs
  - input_file_module.f90#in_ru
  - input_file_module.f90#in_sim
  - maximum_data_module.f90#db_mx
  - recall_module.f90#recall_db
  - reservoir_data_module.f90#res_hyd
  - reservoir_data_module.f90#wet_dat
  - reservoir_data_module.f90#wet_hyd
  - sd_channel_module.f90#sd_chd
  - sd_channel_module.f90#sd_chd_hdr
  - sd_channel_module.f90#sd_dat
  - soil_module.f90#soil
  - time_module.f90#yrs_print
input_variables: []
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
- **Modules used**:
  - [[hydrograph_module.f90]]
  - [[hru_module.f90]]
  - [[soil_module.f90]]
  - [[output_landscape_module.f90]]
  - [[reservoir_data_module.f90]]
  - [[maximum_data_module.f90]]
  - [[climate_module.f90]]
  - [[aquifer_module.f90]]
  - [[input_file_module.f90]]
  - [[sd_channel_module.f90]]
  - [[time_module.f90]]
  - [[recall_module.f90]]
- **Subroutine calls**: 3 | **Files read**: 0 | **Files written**: 13

## Call Relationships
**This routine calls:**

- `system`
- [[copy_file.f90]]
- [[hydrograph_module.f90#hyd_convert_mass_to_conc]]

**Called by:**

- [[main.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[climate_module.f90#wst]] - `weather_station`
- [[hru_module.f90#hru]] - `hydrologic_response_unit`
- [[hru_module.f90#ihru]] - `integer`
- [[hydrograph_module.f90#aqu]] - `hyd_output`
- [[hydrograph_module.f90#dr]] - `hyd_output`
- [[hydrograph_module.f90#exco]] - `hyd_output`
- [[hydrograph_module.f90#hd_tot]] - `object_total_hydrographs`
- [[hydrograph_module.f90#hru_swift_hdr]] - `hru_swift_header`
- [[hydrograph_module.f90#ht5]] - `hyd_output`
- [[hydrograph_module.f90#hz]] - `hyd_output`
- [[hydrograph_module.f90#icmd]] - `integer`
- [[hydrograph_module.f90#iwst]] - `integer`
- [[hydrograph_module.f90#mobj_out]] - `integer`
- [[hydrograph_module.f90#ob]] - `object_connectivity`
- [[hydrograph_module.f90#ob_out]] - `object_output`
- [[hydrograph_module.f90#rec_a]] - `hyd_output`
- [[hydrograph_module.f90#res]] - `hyd_output`
- [[hydrograph_module.f90#ru_def]] - `routing_unit_data`
- [[hydrograph_module.f90#sp_ob]] - `spatial_objects`
- [[hydrograph_module.f90#sp_ob1]] - `spatial_objects`
- [[hydrograph_module.f90#wyld_rto]] - `real, allocatable`
- [[input_file_module.f90#in_con]] - `input_con`
- [[input_file_module.f90#in_regs]] - `input_regions`
- [[input_file_module.f90#in_ru]] - `input_ru`
- [[input_file_module.f90#in_sim]] - `input_sim`
- [[maximum_data_module.f90#db_mx]] - `data_files_max_elements`
- [[recall_module.f90#recall_db]] - `recall_databases`
- [[reservoir_data_module.f90#res_hyd]] - `reservoir_hyd_data`
- [[reservoir_data_module.f90#wet_dat]] - `reservoir_data`
- [[reservoir_data_module.f90#wet_hyd]] - `wetland_hyd_data`
- [[sd_channel_module.f90#sd_chd]] - `swatdeg_hydsed_data`
- [[sd_channel_module.f90#sd_chd_hdr]] - `sd_chd_header`
- [[sd_channel_module.f90#sd_dat]] - `swatdeg_datafiles`
- [[soil_module.f90#soil]] - `soil_profile`
- [[time_module.f90#yrs_print]] - `real`

## File I/O
- **Writes**:
  - [[SWIFT_file_cio.swf]]
  - [[SWIFT_precip.swf]]
  - [[SWIFT_hru_dat.swf]]
  - [[SWIFT_hru_exco.swf]]
  - [[SWIFT_hru_wet.swf]]
  - [[SWIFT_chan_dat.swf]]
  - [[SWIFT_chan_dr.swf]]
  - [[SWIFT_aqu_dr.swf]]
  - [[SWIFT_res_dat.swf]]
  - [[SWIFT_res_dr.swf]]
  - [[SWIFT_recall.swf]]
  - [[SWIFT__ __ trim(adjustl(recall_db(irec]]
  - [[SWIFT_object_prt.swf]]

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
