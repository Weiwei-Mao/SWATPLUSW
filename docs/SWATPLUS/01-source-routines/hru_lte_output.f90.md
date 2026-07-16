---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: hru_lte_output.f90
note_file: hru_lte_output.f90
subroutine: hru_lte_output
module:
  - time_module
  - basin_module
  - output_landscape_module
  - hydrograph_module
calls: []
uses_variables:
  - basin_module.f90#pco
  - hydrograph_module.f90#ob
  - hydrograph_module.f90#sp_ob1
  - output_landscape_module.f90#hlsz
  - output_landscape_module.f90#hltls_a
  - output_landscape_module.f90#hltls_d
  - output_landscape_module.f90#hltls_m
  - output_landscape_module.f90#hltls_y
  - output_landscape_module.f90#hltnb_a
  - output_landscape_module.f90#hltnb_d
  - output_landscape_module.f90#hltnb_m
  - output_landscape_module.f90#hltnb_y
  - output_landscape_module.f90#hltpw_a
  - output_landscape_module.f90#hltpw_d
  - output_landscape_module.f90#hltpw_m
  - output_landscape_module.f90#hltpw_y
  - output_landscape_module.f90#hltwb_a
  - output_landscape_module.f90#hltwb_d
  - output_landscape_module.f90#hltwb_m
  - output_landscape_module.f90#hltwb_y
  - output_landscape_module.f90#hnbz
  - output_landscape_module.f90#hpwz
  - output_landscape_module.f90#hwbz
  - time_module.f90#ndays
  - time_module.f90#time
input_variables: []
reads: []
writes: []
purpose: ""
---

# hru_lte_output

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `hru_lte_output.f90`
- **Modules used**:
  - [[time_module.f90]]
  - [[basin_module.f90]]
  - [[output_landscape_module.f90]]
  - [[hydrograph_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 0 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by:**

- [[command.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[basin_module.f90#pco]] - `basin_print_codes`
- [[hydrograph_module.f90#ob]] - `object_connectivity`
- [[hydrograph_module.f90#sp_ob1]] - `spatial_objects`
- [[output_landscape_module.f90#hlsz]] - `output_losses`
- [[output_landscape_module.f90#hltls_a]] - `output_losses`
- [[output_landscape_module.f90#hltls_d]] - `output_losses`
- [[output_landscape_module.f90#hltls_m]] - `output_losses`
- [[output_landscape_module.f90#hltls_y]] - `output_losses`
- [[output_landscape_module.f90#hltnb_a]] - `output_nutbal`
- [[output_landscape_module.f90#hltnb_d]] - `output_nutbal`
- [[output_landscape_module.f90#hltnb_m]] - `output_nutbal`
- [[output_landscape_module.f90#hltnb_y]] - `output_nutbal`
- [[output_landscape_module.f90#hltpw_a]] - `output_plantweather`
- [[output_landscape_module.f90#hltpw_d]] - `output_plantweather`
- [[output_landscape_module.f90#hltpw_m]] - `output_plantweather`
- [[output_landscape_module.f90#hltpw_y]] - `output_plantweather`
- [[output_landscape_module.f90#hltwb_a]] - `output_waterbal`
- [[output_landscape_module.f90#hltwb_d]] - `output_waterbal`
- [[output_landscape_module.f90#hltwb_m]] - `output_waterbal`
- [[output_landscape_module.f90#hltwb_y]] - `output_waterbal`
- [[output_landscape_module.f90#hnbz]] - `output_nutbal`
- [[output_landscape_module.f90#hpwz]] - `output_plantweather`
- [[output_landscape_module.f90#hwbz]] - `output_waterbal`
- [[time_module.f90#ndays]] - `integer, dimension (13)`
- [[time_module.f90#time]] - `time_current`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
