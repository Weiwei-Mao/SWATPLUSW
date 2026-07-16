---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: basin_output.f90
note_file: basin_output.f90
subroutine: basin_output
module:
  - time_module
  - hydrograph_module
  - calibration_data_module
  - output_landscape_module
  - basin_module
  - carbon_module
calls: []
uses_variables:
  - basin_module.f90#ban_precip_aa
  - basin_module.f90#bsn
  - basin_module.f90#pco
  - calibration_data_module.f90#lsu_elem
  - hydrograph_module.f90#sp_ob
  - output_landscape_module.f90#bls_a
  - output_landscape_module.f90#bls_d
  - output_landscape_module.f90#bls_m
  - output_landscape_module.f90#bls_y
  - output_landscape_module.f90#bnb_a
  - output_landscape_module.f90#bnb_d
  - output_landscape_module.f90#bnb_m
  - output_landscape_module.f90#bnb_y
  - output_landscape_module.f90#bpw_a
  - output_landscape_module.f90#bpw_d
  - output_landscape_module.f90#bpw_m
  - output_landscape_module.f90#bpw_y
  - output_landscape_module.f90#bwb_a
  - output_landscape_module.f90#bwb_d
  - output_landscape_module.f90#bwb_m
  - output_landscape_module.f90#bwb_y
  - output_landscape_module.f90#hls_d
  - output_landscape_module.f90#hlsz
  - output_landscape_module.f90#hltls_d
  - output_landscape_module.f90#hltnb_d
  - output_landscape_module.f90#hltpw_d
  - output_landscape_module.f90#hltwb_d
  - output_landscape_module.f90#hnb_d
  - output_landscape_module.f90#hnbz
  - output_landscape_module.f90#hpw_d
  - output_landscape_module.f90#hpwz
  - output_landscape_module.f90#hwb_d
  - output_landscape_module.f90#hwbz
  - time_module.f90#cal_adj
  - time_module.f90#cal_sim
  - time_module.f90#ndays
  - time_module.f90#time
input_variables: []
reads: []
writes: []
purpose: ""
---

# basin_output

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `basin_output.f90`
- **Modules used**:
  - [[time_module.f90]]
  - [[hydrograph_module.f90]]
  - [[calibration_data_module.f90]]
  - [[output_landscape_module.f90]]
  - [[basin_module.f90]]
  - [[carbon_module.f90]]
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
- [[basin_module.f90#ban_precip_aa]] - `real`
- [[basin_module.f90#bsn]] - `basin_inputs`
- [[basin_module.f90#pco]] - `basin_print_codes`
- [[calibration_data_module.f90#lsu_elem]] - `landscape_elements`
- [[hydrograph_module.f90#sp_ob]] - `spatial_objects`
- [[output_landscape_module.f90#bls_a]] - `output_losses`
- [[output_landscape_module.f90#bls_d]] - `output_losses`
- [[output_landscape_module.f90#bls_m]] - `output_losses`
- [[output_landscape_module.f90#bls_y]] - `output_losses`
- [[output_landscape_module.f90#bnb_a]] - `output_nutbal`
- [[output_landscape_module.f90#bnb_d]] - `output_nutbal`
- [[output_landscape_module.f90#bnb_m]] - `output_nutbal`
- [[output_landscape_module.f90#bnb_y]] - `output_nutbal`
- [[output_landscape_module.f90#bpw_a]] - `output_plantweather`
- [[output_landscape_module.f90#bpw_d]] - `output_plantweather`
- [[output_landscape_module.f90#bpw_m]] - `output_plantweather`
- [[output_landscape_module.f90#bpw_y]] - `output_plantweather`
- [[output_landscape_module.f90#bwb_a]] - `output_waterbal`
- [[output_landscape_module.f90#bwb_d]] - `output_waterbal`
- [[output_landscape_module.f90#bwb_m]] - `output_waterbal`
- [[output_landscape_module.f90#bwb_y]] - `output_waterbal`
- [[output_landscape_module.f90#hls_d]] - `output_losses`
- [[output_landscape_module.f90#hlsz]] - `output_losses`
- [[output_landscape_module.f90#hltls_d]] - `output_losses`
- [[output_landscape_module.f90#hltnb_d]] - `output_nutbal`
- [[output_landscape_module.f90#hltpw_d]] - `output_plantweather`
- [[output_landscape_module.f90#hltwb_d]] - `output_waterbal`
- [[output_landscape_module.f90#hnb_d]] - `output_nutbal`
- [[output_landscape_module.f90#hnbz]] - `output_nutbal`
- [[output_landscape_module.f90#hpw_d]] - `output_plantweather`
- [[output_landscape_module.f90#hpwz]] - `output_plantweather`
- [[output_landscape_module.f90#hwb_d]] - `output_waterbal`
- [[output_landscape_module.f90#hwbz]] - `output_waterbal`
- [[time_module.f90#cal_adj]] - `real`
- [[time_module.f90#cal_sim]] - `character (len=29)`
- [[time_module.f90#ndays]] - `integer, dimension (13)`
- [[time_module.f90#time]] - `time_current`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
