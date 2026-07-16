---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: hru_output_allo.f90
note_file: hru_output_allo.f90
subroutine: hru_output_allo
module:
  - output_landscape_module
  - maximum_data_module
  - hydrograph_module
  - constituent_mass_module
  - output_ls_pesticide_module
  - output_ls_pathogen_module
  - salt_module
  - cs_module
  - carbon_module
calls: []
uses_variables:
  - carbon_module.f90#hpc_a
  - carbon_module.f90#hpc_d
  - carbon_module.f90#hpc_m
  - carbon_module.f90#hpc_y
  - carbon_module.f90#hrc_a
  - carbon_module.f90#hrc_d
  - carbon_module.f90#hrc_m
  - carbon_module.f90#hrc_y
  - carbon_module.f90#hsc_a
  - carbon_module.f90#hsc_d
  - carbon_module.f90#hsc_m
  - carbon_module.f90#hsc_y
  - carbon_module.f90#hscf_a
  - carbon_module.f90#hscf_d
  - carbon_module.f90#hscf_m
  - carbon_module.f90#hscf_y
  - carbon_module.f90#lpc_a
  - carbon_module.f90#lpc_d
  - carbon_module.f90#lpc_m
  - carbon_module.f90#lpc_y
  - carbon_module.f90#lrc_a
  - carbon_module.f90#lrc_d
  - carbon_module.f90#lrc_m
  - carbon_module.f90#lrc_y
  - carbon_module.f90#lsc_a
  - carbon_module.f90#lsc_d
  - carbon_module.f90#lsc_m
  - carbon_module.f90#lsc_y
  - carbon_module.f90#lscf_a
  - carbon_module.f90#lscf_d
  - carbon_module.f90#lscf_m
  - carbon_module.f90#lscf_y
  - constituent_mass_module.f90#cs_db
  - cs_module.f90#hcsb_a
  - cs_module.f90#hcsb_d
  - cs_module.f90#hcsb_m
  - cs_module.f90#hcsb_y
  - hydrograph_module.f90#sp_ob
  - maximum_data_module.f90#db_mx
  - output_landscape_module.f90#hcyl_a
  - output_landscape_module.f90#hcyl_d
  - output_landscape_module.f90#hcyl_m
  - output_landscape_module.f90#hcyl_y
  - output_landscape_module.f90#hls_a
  - output_landscape_module.f90#hls_d
  - output_landscape_module.f90#hls_m
  - output_landscape_module.f90#hls_y
  - output_landscape_module.f90#hnb_a
  - output_landscape_module.f90#hnb_d
  - output_landscape_module.f90#hnb_m
  - output_landscape_module.f90#hnb_y
  - output_landscape_module.f90#hpw_a
  - output_landscape_module.f90#hpw_d
  - output_landscape_module.f90#hpw_m
  - output_landscape_module.f90#hpw_y
  - output_landscape_module.f90#hwb_a
  - output_landscape_module.f90#hwb_d
  - output_landscape_module.f90#hwb_m
  - output_landscape_module.f90#hwb_y
  - output_ls_pathogen_module.f90#hpath_bal
  - output_ls_pathogen_module.f90#hpathb_a
  - output_ls_pathogen_module.f90#hpathb_m
  - output_ls_pathogen_module.f90#hpathb_y
  - output_ls_pesticide_module.f90#bpestb_a
  - output_ls_pesticide_module.f90#bpestb_d
  - output_ls_pesticide_module.f90#bpestb_m
  - output_ls_pesticide_module.f90#bpestb_y
  - output_ls_pesticide_module.f90#hpestb_a
  - output_ls_pesticide_module.f90#hpestb_d
  - output_ls_pesticide_module.f90#hpestb_m
  - output_ls_pesticide_module.f90#hpestb_y
  - salt_module.f90#hsaltb_a
  - salt_module.f90#hsaltb_d
  - salt_module.f90#hsaltb_m
  - salt_module.f90#hsaltb_y
input_variables: []
reads: []
writes: []
purpose: ""
---

# hru_output_allo

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `hru_output_allo.f90`
- **Modules used**:
  - [[output_landscape_module.f90]]
  - [[maximum_data_module.f90]]
  - [[hydrograph_module.f90]]
  - [[constituent_mass_module.f90]]
  - [[output_ls_pesticide_module.f90]]
  - [[output_ls_pathogen_module.f90]]
  - [[salt_module.f90]]
  - [[cs_module.f90]]
  - [[carbon_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 0 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by:**

- [[proc_hru.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[carbon_module.f90#hpc_a]] - `carbon_plant_gain_losses`
- [[carbon_module.f90#hpc_d]] - `carbon_plant_gain_losses`
- [[carbon_module.f90#hpc_m]] - `carbon_plant_gain_losses`
- [[carbon_module.f90#hpc_y]] - `carbon_plant_gain_losses`
- [[carbon_module.f90#hrc_a]] - `carbon_residue_gain_losses`
- [[carbon_module.f90#hrc_d]] - `carbon_residue_gain_losses`
- [[carbon_module.f90#hrc_m]] - `carbon_residue_gain_losses`
- [[carbon_module.f90#hrc_y]] - `carbon_residue_gain_losses`
- [[carbon_module.f90#hsc_a]] - `carbon_soil_gain_losses`
- [[carbon_module.f90#hsc_d]] - `carbon_soil_gain_losses`
- [[carbon_module.f90#hsc_m]] - `carbon_soil_gain_losses`
- [[carbon_module.f90#hsc_y]] - `carbon_soil_gain_losses`
- [[carbon_module.f90#hscf_a]] - `carbon_soil_transformations`
- [[carbon_module.f90#hscf_d]] - `carbon_soil_transformations`
- [[carbon_module.f90#hscf_m]] - `carbon_soil_transformations`
- [[carbon_module.f90#hscf_y]] - `carbon_soil_transformations`
- [[carbon_module.f90#lpc_a]] - `carbon_plant_gain_losses`
- [[carbon_module.f90#lpc_d]] - `carbon_plant_gain_losses`
- [[carbon_module.f90#lpc_m]] - `carbon_plant_gain_losses`
- [[carbon_module.f90#lpc_y]] - `carbon_plant_gain_losses`
- [[carbon_module.f90#lrc_a]] - `carbon_residue_gain_losses`
- [[carbon_module.f90#lrc_d]] - `carbon_residue_gain_losses`
- [[carbon_module.f90#lrc_m]] - `carbon_residue_gain_losses`
- [[carbon_module.f90#lrc_y]] - `carbon_residue_gain_losses`
- [[carbon_module.f90#lsc_a]] - `carbon_soil_gain_losses`
- [[carbon_module.f90#lsc_d]] - `carbon_soil_gain_losses`
- [[carbon_module.f90#lsc_m]] - `carbon_soil_gain_losses`
- [[carbon_module.f90#lsc_y]] - `carbon_soil_gain_losses`
- [[carbon_module.f90#lscf_a]] - `carbon_soil_transformations`
- [[carbon_module.f90#lscf_d]] - `carbon_soil_transformations`
- [[carbon_module.f90#lscf_m]] - `carbon_soil_transformations`
- [[carbon_module.f90#lscf_y]] - `carbon_soil_transformations`
- [[constituent_mass_module.f90#cs_db]] - `constituents`
- [[cs_module.f90#hcsb_a]] - `object_cs_balance`
- [[cs_module.f90#hcsb_d]] - `object_cs_balance`
- [[cs_module.f90#hcsb_m]] - `object_cs_balance`
- [[cs_module.f90#hcsb_y]] - `object_cs_balance`
- [[hydrograph_module.f90#sp_ob]] - `spatial_objects`
- [[maximum_data_module.f90#db_mx]] - `data_files_max_elements`
- [[output_landscape_module.f90#hcyl_a]] - `output_nutcarb_cycling`
- [[output_landscape_module.f90#hcyl_d]] - `output_nutcarb_cycling`
- [[output_landscape_module.f90#hcyl_m]] - `output_nutcarb_cycling`
- [[output_landscape_module.f90#hcyl_y]] - `output_nutcarb_cycling`
- [[output_landscape_module.f90#hls_a]] - `output_losses`
- [[output_landscape_module.f90#hls_d]] - `output_losses`
- [[output_landscape_module.f90#hls_m]] - `output_losses`
- [[output_landscape_module.f90#hls_y]] - `output_losses`
- [[output_landscape_module.f90#hnb_a]] - `output_nutbal`
- [[output_landscape_module.f90#hnb_d]] - `output_nutbal`
- [[output_landscape_module.f90#hnb_m]] - `output_nutbal`
- [[output_landscape_module.f90#hnb_y]] - `output_nutbal`
- [[output_landscape_module.f90#hpw_a]] - `output_plantweather`
- [[output_landscape_module.f90#hpw_d]] - `output_plantweather`
- [[output_landscape_module.f90#hpw_m]] - `output_plantweather`
- [[output_landscape_module.f90#hpw_y]] - `output_plantweather`
- [[output_landscape_module.f90#hwb_a]] - `output_waterbal`
- [[output_landscape_module.f90#hwb_d]] - `output_waterbal`
- [[output_landscape_module.f90#hwb_m]] - `output_waterbal`
- [[output_landscape_module.f90#hwb_y]] - `output_waterbal`
- [[output_ls_pathogen_module.f90#hpath_bal]] - `object_pathogen_balance`
- [[output_ls_pathogen_module.f90#hpathb_a]] - `object_pathogen_balance`
- [[output_ls_pathogen_module.f90#hpathb_m]] - `object_pathogen_balance`
- [[output_ls_pathogen_module.f90#hpathb_y]] - `object_pathogen_balance`
- [[output_ls_pesticide_module.f90#bpestb_a]] - `object_pesticide_balance`
- [[output_ls_pesticide_module.f90#bpestb_d]] - `object_pesticide_balance`
- [[output_ls_pesticide_module.f90#bpestb_m]] - `object_pesticide_balance`
- [[output_ls_pesticide_module.f90#bpestb_y]] - `object_pesticide_balance`
- [[output_ls_pesticide_module.f90#hpestb_a]] - `object_pesticide_balance`
- [[output_ls_pesticide_module.f90#hpestb_d]] - `object_pesticide_balance`
- [[output_ls_pesticide_module.f90#hpestb_m]] - `object_pesticide_balance`
- [[output_ls_pesticide_module.f90#hpestb_y]] - `object_pesticide_balance`
- [[salt_module.f90#hsaltb_a]] - `object_salt_balance`
- [[salt_module.f90#hsaltb_d]] - `object_salt_balance`
- [[salt_module.f90#hsaltb_m]] - `object_salt_balance`
- [[salt_module.f90#hsaltb_y]] - `object_salt_balance`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
