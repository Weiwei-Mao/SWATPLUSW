---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: hru_control.f90
note_file: hru_control.f90
subroutine: hru_control
module:
  - hru_module
  - soil_module
  - plant_module
  - basin_module
  - organic_mineral_mass_module
  - carbon_module
  - hydrograph_module
  - climate_module
  - septic_data_module
  - reservoir_data_module
  - plant_data_module
  - mgt_operations_module
  - reservoir_module
  - output_landscape_module
  - output_ls_pesticide_module
  - time_module
  - conditional_module
  - constituent_mass_module
  - water_body_module
  - salt_module
  - cs_module
  - gwflow_module
  - tillage_data_module
calls:
  - varinit
  - conditions
  - actions
  - pl_fert
  - albedo
  - salt_chem_hru
  - cs_rctn_hru
  - cs_sorb_hru
  - stmp_solt
  - sq_canopyint
  - sq_snom
  - rls_routesurf
  - rls_routesoil
  - rls_routetile
  - rls_routeaqu
  - sq_crackvol
  - et_pot
  - et_act
  - mgt_operatn
  - surface
  - wet_irrp
  - wetland_control
  - swr_percmain
  - pl_graze
  - rsd_decomp
  - nut_nminrl
  - mgt_biomix
  - cbn_surfrsd_decomp
  - cbn_rsd_transfer
  - cbn_zhang2
  - nut_nitvol
  - nut_pminrl2
  - nut_pminrl
  - sep_biozone
  - pl_community
  - pl_grow
  - pest_washp
  - pest_pl_up
  - pest_decay
  - pest_lch
  - pest_soil_tot
  - pest_enrsb
  - pest_pesty
  - nut_orgn
  - nut_orgnc2
  - nut_psed
  - nut_nrain
  - nut_nlch
  - nut_solp
  - salt_rain
  - salt_roadsalt
  - salt_lch
  - cs_rain
  - cs_lch
  - path_ls_swrouting
  - path_ls_runoff
  - path_ls_process
  - hru_urban
  - hru_urbanhr
  - swr_latsed
  - stor_surfstor
  - swr_substor
  - smp_filter
  - smp_buffer
  - smp_grass_wway
  - smp_bmpfixed
  - sq_surfst
  - swr_subwq
  - hru_urb_bmp
  - hru_hyds
reads: []
writes: []
purpose: "this subroutine controls the simulation of the land phase of the; hydrologic cycle"
---

# hru_control

> [!info] Summary
> this subroutine controls the simulation of the land phase of the; hydrologic cycle

## Basic Information
- **Type**: `subroutine`
- **Source file**: `hru_control.f90`
- **Modules used**: [[hru_module.f90]], [[soil_module.f90]], [[plant_module.f90]], [[basin_module.f90]], [[organic_mineral_mass_module.f90]], [[carbon_module.f90]], [[hydrograph_module.f90]], [[climate_module.f90]], [[septic_data_module.f90]], [[reservoir_data_module.f90]], [[plant_data_module.f90]], [[mgt_operations_module.f90]], [[reservoir_module.f90]], [[output_landscape_module.f90]], [[output_ls_pesticide_module.f90]], [[time_module.f90]], [[conditional_module.f90]], [[constituent_mass_module.f90]], [[water_body_module.f90]], [[salt_module.f90]], [[cs_module.f90]], [[gwflow_module.f90]], [[tillage_data_module.f90]]
- **Subroutine calls**: 70 | **Files read**: 0 | **Files written**: 0

## Call Relationships
**This routine calls:**

- [[varinit.f90]]
- [[conditions.f90]]
- [[actions.f90]]
- [[pl_fert.f90]]
- [[albedo.f90]]
- [[salt_chem_hru.f90]]
- [[cs_rctn_hru.f90]]
- [[cs_sorb_hru.f90]]
- [[stmp_solt.f90]]
- [[sq_canopyint.f90]]
- [[sq_snom.f90]]
- [[rls_routesurf.f90]]
- [[rls_routesoil.f90]]
- [[rls_routetile.f90]]
- [[rls_routeaqu.f90]]
- [[sq_crackvol.f90]]
- [[et_pot.f90]]
- [[et_act.f90]]
- [[mgt_operatn.f90]]
- [[surface.f90]]
- [[wet_irrp.f90]]
- [[wetland_control.f90]]
- [[swr_percmain.f90]]
- [[pl_graze.f90]]
- [[rsd_decomp.f90]]
- [[nut_nminrl.f90]]
- [[mgt_biomix.f90]]
- [[cbn_surfrsd_decomp.f90]]
- [[cbn_rsd_transfer.f90]]
- [[cbn_zhang2.f90]]
- [[nut_nitvol.f90]]
- [[nut_pminrl2.f90]]
- [[nut_pminrl.f90]]
- [[sep_biozone.f90]]
- [[pl_community.f90]]
- [[pl_grow.f90]]
- [[pest_washp.f90]]
- [[pest_pl_up.f90]]
- [[pest_decay.f90]]
- [[pest_lch.f90]]
- [[pest_soil_tot.f90]]
- [[pest_enrsb.f90]]
- [[pest_pesty.f90]]
- [[nut_orgn.f90]]
- [[nut_orgnc2.f90]]
- [[nut_psed.f90]]
- [[nut_nrain.f90]]
- [[nut_nlch.f90]]
- [[nut_solp.f90]]
- [[salt_rain.f90]]
- [[salt_roadsalt.f90]]
- [[salt_lch.f90]]
- [[cs_rain.f90]]
- [[cs_lch.f90]]
- [[path_ls_swrouting.f90]]
- [[path_ls_runoff.f90]]
- [[path_ls_process.f90]]
- [[hru_urban.f90]]
- [[hru_urbanhr.f90]]
- [[swr_latsed.f90]]
- [[stor_surfstor.f90]]
- [[swr_substor.f90]]
- [[smp_filter.f90]]
- [[smp_buffer.f90]]
- [[smp_grass_wway.f90]]
- [[smp_bmpfixed.f90]]
- [[sq_surfst.f90]]
- [[swr_subwq.f90]]
- [[hru_urb_bmp.f90]]
- [[hru_hyds.f90]]

**Called by** (live Dataview back-query):

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
